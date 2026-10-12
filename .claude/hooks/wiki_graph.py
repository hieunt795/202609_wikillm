"""Do thi quan he cua wiki (00_schema.md §6): nhom tu index.md + link trong than bai +
loai quan he o frontmatter. Goi qua validate_wiki_page.py:

  --graph [--no-save]                 dung do thi, so voi anh chup truoc, in thong bao, luu anh chup
  --neighbors <trang> [--type t] [--hops n]   lang gieng theo loai, ca hai chieu
  --relations [<trang | nhom>]        so link chua co loai va cap gan loai lech; co doi so thi
                                      in tung link kem cau chua no (de gan loai)
  --map <linh vuc>                    ban do HTML vao Claude outputs/

Moi thu o day la du lieu dan xuat, khong phai tri thuc da chap nhan.
Do manh: 3 = link nam trong cau dau tien cua trang; 2 = link o phan con lai.
Link mat / doi loai duoc tinh so voi HEAD cua git (cac trang da doi tu commit gan nhat);
xep hang va do manh cap nhom duoc so voi 03_state/_graph_snapshot.tsv.
"""
import collections
import json
import os
import re
import subprocess
import sys

import validate_wiki_page as V

TYPES = V.RELATION_FIELDS
BASE = {"has_part": "part_of", "governed_by": "governs", "driven_by": "drives"}
INVERSE = {"part_of": "has_part", "has_part": "part_of", "governs": "governed_by",
           "governed_by": "governs", "drives": "driven_by", "driven_by": "drives",
           "contrasts": "contrasts", "analogous": "analogous", "related": "related"}
TYPE_LABEL = {
    "part_of": "là thành phần của", "has_part": "gồm",
    "governs": "đo lường / quy định / giới hạn", "governed_by": "chịu quy định / giới hạn bởi",
    "drives": "tác động tới / là đầu vào của", "driven_by": "chịu tác động từ",
    "contrasts": "đối chiếu với", "analogous": "cùng cơ chế với",
    "related": "liên quan tới", "": "chưa gắn loại",
}
INV_LABEL = dict({k: TYPE_LABEL[v] for k, v in INVERSE.items()}, **{"": "chưa gắn loại"})
BASE_LABEL = {"part_of": "Thành phần", "governs": "Đo lường / quy định / giới hạn",
              "drives": "Tác động / đầu vào", "contrasts": "Đối chiếu", "analogous": "Cùng cơ chế",
              "related": "Liên quan", "": "Chưa gắn loại"}

CITE_RE = re.compile(r"\s*\((?:[a-z_]+|Modern Money Mechanics), [^()]*?d\.[^()]*?\)")
SENT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-ỸĐ\[\$])")

# Nguong thong bao (tam thoi, chinh sau luot ingest that dau tien)
TOP_N = 25
RANK_JUMP = 50
RANK_WATCH = 200
PAIR_REL = 0.20
PAIR_ABS = 5

PALETTE = ["#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#b07aa1", "#76b7b2", "#edc948",
           "#9c755f", "#ff9da7", "#86bc86", "#5fa2ce", "#c85200", "#8cd17d", "#a0cbe8"]


def snap_path(root):
    return os.path.join(root, "03_state", "_graph_snapshot.tsv")


def sentences(par):
    return SENT_RE.split(CITE_RE.sub("", par))


def parse_page(text):
    """-> (fields, cac doan, {dich: nam trong cau dau}, {dich: [loai]})."""
    fields, body = V.split_frontmatter(text.replace("\r\n", "\n").lstrip("﻿"))
    fields = fields or {}
    pars = [p for p in re.split(r"\n\s*\n", V.strip_code_fences(body).strip()) if p.strip()]
    first = set(V.link_targets(sentences(pars[0])[0])) if pars else set()
    links = collections.OrderedDict()
    for p in pars:
        for t in V.link_targets(p):
            links.setdefault(t, t in first)
    rel = {}
    for ty in TYPES:
        for t in V.yaml_list(fields.get(ty, "")):
            rel.setdefault(t, []).append(ty)
    return fields, pars, links, rel


def read_index(wiki):
    """page -> (linh vuc, nhom); thu tu nhom; trang bi liet ke hai lan."""
    where, order, dup = {}, [], []
    domain = group = None
    with open(os.path.join(wiki, "index.md"), encoding="utf-8-sig") as fh:
        for line in fh:
            line = line.rstrip("\r\n")
            if line.startswith("## "):
                domain = line[3:].strip()
            m = re.match(r"^\*\*(.+)\*\*\s*$", line)
            if m:
                group = m.group(1)
                if (domain, group) not in order:
                    order.append((domain, group))
            elif line.startswith("- [["):
                t = V.link_targets(line)
                if not t:
                    continue
                if t[0] in where:
                    dup.append(t[0])
                else:
                    where[t[0]] = (domain, group)
    return where, order, dup


def build(wiki):
    where, order, dup = read_index(wiki)
    pages = {}
    for f in sorted(os.listdir(wiki)):
        if f.lower().endswith(".md") and f.lower() != "index.md":
            with open(os.path.join(wiki, f), encoding="utf-8-sig") as fh:
                fields, pars, links, rel = parse_page(fh.read())
            pages[f[:-3]] = {"fm": fields, "pars": pars, "links": links, "rel": rel}
    edges = {}
    for s, p in pages.items():
        for t, first in p["links"].items():
            if t != s and t in pages:
                edges[(s, t)] = {"w": 3 if first else 2, "tys": p["rel"].get(t, [])}
    return where, order, dup, pages, edges


def pagerank(pages, edges, d=0.85, iters=60):
    names = list(pages)
    n = len(names)
    out = collections.defaultdict(float)
    inc = collections.defaultdict(list)
    for (s, t), e in edges.items():
        out[s] += e["w"]
        inc[t].append((s, e["w"]))
    pr = dict.fromkeys(names, 1.0 / n)
    for _ in range(iters):
        dangling = sum(pr[x] for x in names if out[x] == 0)
        pr = {x: (1 - d) / n + d * dangling / n + d * sum(pr[s] * w / out[s] for s, w in inc[x])
              for x in names}
    return pr


def mismatches(edges):
    """Cap trang link qua lai ma hai phia gan loai khong phai dang nguoc cua nhau."""
    out = []
    for (s, t), e in edges.items():
        back = edges.get((t, s))
        if s < t and back and e["tys"] and back["tys"]:
            if e["tys"] == ["related"] or back["tys"] == ["related"]:
                continue  # `related` khong noi ro quan he nen khong mau thuan voi loai nao
            if {INVERSE[x] for x in e["tys"]} != set(back["tys"]):
                out.append((s, e["tys"], t, back["tys"]))
    return out


def snapshot(where, pages, edges):
    pr = pagerank(pages, edges)
    ranked = sorted(pages, key=lambda x: (-pr[x], x))
    gp = collections.Counter()
    gp_edges = collections.defaultdict(list)
    for (s, t), e in edges.items():
        gs, gt = where.get(s, (None, "?"))[1], where.get(t, (None, "?"))[1]
        if gs != gt:
            key = " || ".join(sorted([gs, gt]))
            gp[key] += e["w"]
            gp_edges[key].append((s, t))
    bridges = {}
    for key, es in gp_edges.items():
        if len(es) >= 2:
            common = set(es[0])
            for e in es[1:]:
                common &= set(e)
            if len(common) == 1:
                bridges[key] = next(iter(common))
    by_type = collections.Counter(ty for e in edges.values() for ty in e["tys"])
    return {
        "meta": {"taken": V.now_vn(), "pages": len(pages), "edges": len(edges),
                 "strong": sum(1 for e in edges.values() if e["w"] == 3),
                 "typed": sum(1 for e in edges.values() if e["tys"])},
        "type": dict(by_type), "pair": dict(gp), "bridge": bridges,
        "rank": {x: i + 1 for i, x in enumerate(ranked)},
    }


def write_snapshot(path, snap):
    rows = ["# Anh chup do thi quan he (00_schema.md §6). May ghi bang --graph; khong sua tay."]
    for sec in ("meta", "type", "pair", "bridge"):
        rows += ["%s\t%s\t%s" % (sec, k, v) for k, v in sorted(snap[sec].items())]
    rows += ["rank\t%s\t%d" % (k, v) for k, v in sorted(snap["rank"].items(), key=lambda x: x[1])
             if v <= RANK_WATCH]
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(rows) + "\n")


def read_snapshot(path):
    snap = {"meta": {}, "type": {}, "pair": {}, "bridge": {}, "rank": {}}
    with open(path, encoding="utf-8-sig") as fh:
        for line in fh:
            p = line.rstrip("\r\n").split("\t")
            if len(p) == 3 and p[0] in snap:
                snap[p[0]][p[1]] = p[2] if p[0] in ("bridge",) or (p[0] == "meta" and p[1] == "taken") else int(p[2])
    return snap


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def edge_changes(root, pages):
    """Link them / mat / doi loai / vua gan loai, so cac trang da doi voi HEAD. None = khong co git."""
    st = git(root, "status", "--porcelain", "--", "02_wiki")
    if st is None:
        return None
    added, removed, retyped, typed = [], [], [], 0
    for line in st.splitlines():
        path = line[3:].split(" -> ")[0].strip().strip('"')
        name = os.path.splitext(os.path.basename(path))[0]
        if not path.endswith(".md") or name == "index":
            continue
        old_text = git(root, "show", "HEAD:" + path.replace("\\", "/"))
        o_links, o_rel = ({}, {})
        if old_text is not None:
            _, _, o_links, o_rel = parse_page(old_text)
        new = pages.get(name)
        n_links, n_rel = (new["links"], new["rel"]) if new else ({}, {})
        for t in o_links:
            if t not in n_links:
                removed.append((name, t, o_rel.get(t, [])))
        for t in n_links:
            if t not in o_links:
                added.append((name, t))
            elif sorted(o_rel.get(t, [])) != sorted(n_rel.get(t, [])):
                if o_rel.get(t):
                    retyped.append((name, t, o_rel[t], n_rel.get(t, [])))
                else:
                    typed += 1
    return {"added": added, "removed": removed, "retyped": retyped, "typed": typed}


def diff(old, new, ch):
    """Danh sach dong thong bao; rong = khong co gi vuot nguong."""
    out = []
    newp = new["meta"]["pages"] - old["meta"].get("pages", 0)
    if ch and (newp or ch["added"] or ch["removed"] or ch["typed"] or ch["retyped"]):
        out.append("Tong: %+d trang, +%d link, -%d link, %d link vua duoc gan loai, %d doi loai (da gan %d/%d)."
                   % (newp, len(ch["added"]), len(ch["removed"]), ch["typed"], len(ch["retyped"]),
                      new["meta"]["typed"], new["meta"]["edges"]))
        for s, t, tys in ch["removed"][:20]:
            out.append("  LINK MAT: %s -> %s%s" % (s, t, " [%s]" % ", ".join(tys) if tys else ""))
        if len(ch["removed"]) > 20:
            out.append("  ... va %d link mat khac" % (len(ch["removed"]) - 20))
        for s, t, a, b in ch["retyped"]:
            out.append("  DOI LOAI: %s -> %s: %s => %s" % (s, t, ", ".join(a), ", ".join(b) or "(bo loai)"))
    elif newp:
        out.append("Tong: %+d trang." % newp)
    orank, nrank = old["rank"], new["rank"]
    otop = {p for p, r in orank.items() if r <= TOP_N}
    ntop = {p for p, r in nrank.items() if r <= TOP_N}
    for p in sorted(ntop - otop, key=lambda x: nrank[x]):
        out.append("  VAO TOP %d: %s (hang %s -> %d)" % (TOP_N, p, orank.get(p, "moi"), nrank[p]))
    for p in sorted(otop - ntop):
        out.append("  RA TOP %d: %s (hang %d -> %s)" % (TOP_N, p, orank[p], nrank.get(p, "da xoa")))
    # Anh chup chi giu RANK_WATCH hang dau; trang ngoai do coi nhu hang RANK_WATCH + 1.
    far = RANK_WATCH + 1
    watch = set(orank) | {x for x, r in nrank.items() if r <= RANK_WATCH}
    for p in sorted(watch, key=lambda x: nrank.get(x, far)):
        if p in ntop or p in otop or p not in nrank:
            continue
        a, b = orank.get(p, far), min(nrank[p], far)
        if abs(a - b) >= RANK_JUMP:
            out.append("  DOI HANG: %s (%s -> %s)" % (
                p, a if a < far else "ngoai %d" % RANK_WATCH, b if b < far else "ngoai %d" % RANK_WATCH))
    og, ng = old["pair"], new["pair"]
    for k in sorted(set(og) | set(ng)):
        a, b = og.get(k, 0), ng.get(k, 0)
        if abs(b - a) >= PAIR_ABS and (a == 0 or abs(b - a) / a >= PAIR_REL):
            out.append("  NHOM: %s: do manh %d -> %d" % (k.replace(" || ", " <-> "), a, b))
    ob, nb = old["bridge"], new["bridge"]
    for k in sorted(nb):
        if ob.get(k) != nb[k]:
            out.append("  DIEM NOI DUY NHAT: %s giua %s" % (nb[k], k.replace(" || ", " <-> ")))
    return out


def cmd_graph(root, wiki, no_save):
    where, order, dup, pages, edges = build(wiki)
    snap = snapshot(where, pages, edges)
    m = snap["meta"]
    w = sys.stdout.write
    noidx = sorted(p for p in pages if p not in where)
    if noidx:
        w("Trang khong co trong index (khong vao nhom nao): %s\n" % ", ".join(noidx))
    if dup:
        w("Trang bi liet ke hai lan trong index (lay nhom dau): %s\n" % ", ".join(sorted(set(dup))))
    path = snap_path(root)
    if os.path.exists(path):
        old = read_snapshot(path)
        lines = diff(old, snap, edge_changes(root, pages))
        w("So voi anh chup %s (link so voi HEAD cua git):\n" % old["meta"].get("taken", "?"))
        w(("\n".join(lines) if lines else "  Khong co thay doi vuot nguong.") + "\n")
    else:
        w("Chua co anh chup truoc de so.\n")
    if not no_save:
        write_snapshot(path, snap)
    w("%d trang, %d link (%d manh), %d da gan loai, %d cap nhom co link cheo.%s\n"
      % (m["pages"], m["edges"], m["strong"], m["typed"], len(snap["pair"]),
         "" if no_save else " Da luu anh chup."))


def cmd_neighbors(wiki, args):
    if not args:
        sys.exit("Thieu ten trang. Dung: --neighbors <trang> [--type <loai>] [--hops <n>]")
    page, want, hops = args[0], None, 1
    for i, a in enumerate(args):
        if a == "--type" and i + 1 < len(args):
            want = args[i + 1]
        if a == "--hops" and i + 1 < len(args):
            hops = int(args[i + 1])
    if want and want not in TYPES:
        sys.exit("Loai khong hop le: %s. Chap nhan: %s" % (want, ", ".join(TYPES)))
    where, _, _, pages, edges = build(wiki)
    if page not in pages:
        sys.exit("Khong co trang `%s`." % page)
    w = sys.stdout.write
    seen, frontier, n, untyped = {page}, [page], 0, 0
    for hop in range(1, hops + 1):
        nxt = []
        for cur in frontier:
            got = {}  # gop hai chieu cua cung mot trang thanh mot dong
            for (s, t), e in edges.items():
                if s == cur:
                    other, arrow, tys = t, ">", e["tys"]
                elif t == cur:
                    other, arrow, tys = s, "<", [INVERSE[x] for x in e["tys"]]
                else:
                    continue
                g = got.setdefault(other, ["", [], 0])
                g[0] = "<>" if g[0] and g[0] != arrow else arrow
                g[1] += [x for x in tys if x not in g[1]]
                g[2] = max(g[2], e["w"])
            rows = [(o, a, sorted(tys, key=TYPES.index), wgt) for o, (a, tys, wgt) in got.items()]
            for other, arrow, tys, wgt in sorted(rows, key=lambda r: (-r[3], r[0])):
                if want and want not in tys:
                    untyped += not tys
                    continue
                n += 1
                w("%d\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                    hop, cur if hop > 1 else "", arrow, ", ".join(tys) or "(chua co loai)",
                    other, "manh" if wgt == 3 else "vua", where.get(other, ("", "?"))[1]))
                if other not in seen:
                    seen.add(other)
                    nxt.append(other)
        frontier = nxt
    w("%d quan he quanh %s%s (cot: vong, tu, chieu link, loai nhin tu trang goc, trang, do manh, nhom).\n"
      % (n, page, " loai %s" % want if want else ""))
    if want and untyped:
        w("%d link chua co loai khong duoc loc; chay lai khong co --type de xem.\n" % untyped)


def link_sentence(page, target):
    pat = re.compile(r"\[\[" + re.escape(target) + r"(\||\]\])")
    for par in page["pars"]:
        if pat.search(par):
            for s in sentences(par):
                if pat.search(s):
                    return s.strip()
            return CITE_RE.sub("", par).strip()[:300]
    return ""


def cmd_relations(wiki, arg):
    where, _, _, pages, edges = build(wiki)
    w = sys.stdout.write
    if arg:
        if arg in pages:
            members, head = [arg], "Trang: %s" % arg
        else:
            hit = sorted({g for (_, g) in where.values() if arg.lower() in g.lower()})
            if len(hit) != 1:
                sys.exit("Can dung 1 trang hoac 1 nhom khop '%s'; nhom tim thay: %s" % (arg, hit))
            members = [p for p in pages if where.get(p, (None, None))[1] == hit[0]]
            head = "Nhom: %s — %d trang" % (hit[0], len(members))
        w("# %s\n" % head)
        n = 0
        for s in members:
            w("\n## %s\n" % s)
            for t in pages[s]["links"]:
                e = edges.get((s, t))
                if e:
                    n += 1
                    w("- -> %s  [%s%s]\n    %s\n" % (t, "manh" if e["w"] == 3 else "vua",
                                                     "; " + ", ".join(e["tys"]) if e["tys"] else "; chua co loai",
                                                     link_sentence(pages[s], t)))
        w("\n# %d link\n" % n)
        return
    bad = mismatches(edges)
    for s, a, t, b in bad:
        w("LECH: %s -[%s]-> %s | chieu nguoc ghi [%s]\n" % (s, ", ".join(a), t, ", ".join(b)))
    by = collections.Counter(ty for e in edges.values() for ty in e["tys"])
    if by:
        w("Theo loai: %s\n" % ", ".join("%s %d" % (k, by[k]) for k in TYPES if by[k]))
    typed = sum(1 for e in edges.values() if e["tys"])
    w("%d/%d link da gan loai, %d cap gan loai lech nhau.\n" % (typed, len(edges), len(bad)))


def debt(root):
    _, _, _, _, edges = build(os.path.join(root, "02_wiki"))
    typed = sum(1 for e in edges.values() if e["tys"])
    return "link chua co loai %d/%d; %d cap quan he lech" % (len(edges) - typed, len(edges), len(mismatches(edges)))


def cmd_map(root, wiki, key):
    where, order, _, pages, edges = build(wiki)
    snap = snapshot(where, pages, edges)
    doms = []
    for d, _ in order:
        if d not in doms:
            doms.append(d)
    hit = [d for d in doms if key.lower() in d.lower()]
    if len(hit) != 1:
        sys.exit("Can dung 1 linh vuc khop '%s', tim thay: %s" % (key, hit))
    dom = hit[0]
    groups = [g for d, g in order if d == dom]
    gid = {g: i for i, g in enumerate(groups)}
    members = [p for p in pages if where.get(p, (None, None))[0] == dom]
    mset = set(members)
    inl, outl = collections.Counter(), collections.Counter()
    for (s, t) in edges:
        outl[s] += 1
        inl[t] += 1
    nodes = [{"id": p, "g": gid[where[p][1]], "rank": snap["rank"][p],
              "rev": bool(pages[p]["fm"].get("reviewed")), "status": pages[p]["fm"].get("status", ""),
              "inl": inl[p], "outl": outl[p]} for p in sorted(members, key=lambda x: snap["rank"][x])]
    es = []
    for (s, t), e in edges.items():
        if s in mset and t in mset:
            ty = e["tys"][0] if e["tys"] else ""
            es.append({"s": s, "t": t, "w": e["w"], "ty": ty, "tys": e["tys"],
                       "b": BASE.get(ty, ty), "inv": ty in BASE})
    gnodes = [{"name": g, "ext": False, "n": sum(1 for p in members if where[p][1] == g)} for g in groups]
    ext = [d for d in doms if d != dom]
    xid = {d: len(groups) + i for i, d in enumerate(ext)}
    gnodes += [{"name": d, "ext": True, "n": sum(1 for p in pages if where.get(p, (None,))[0] == d)} for d in ext]
    gw = collections.Counter()
    for (s, t), e in edges.items():
        if s in where and t in where and (s in mset or t in mset):
            a = gid[where[s][1]] if s in mset else xid[where[s][0]]
            b = gid[where[t][1]] if t in mset else xid[where[t][0]]
            if a != b:
                gw[tuple(sorted((a, b)))] += e["w"]
    data = {"domain": dom, "taken": snap["meta"]["taken"], "total_pages": len(pages),
            "groups": gnodes, "nodes": nodes, "edges": es,
            "gpairs": [{"a": a, "b": b, "w": v} for (a, b), v in gw.items()],
            "palette": PALETTE, "typeLabel": TYPE_LABEL, "invLabel": INV_LABEL, "baseLabel": BASE_LABEL,
            "typed": sum(1 for e in es if e["tys"])}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiki_graph_map.html"), encoding="utf-8") as fh:
        html = fh.read()
    out_dir = os.path.join(root, "Claude outputs")
    os.makedirs(out_dir, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-") or "domain"
    path = os.path.join(out_dir, "graph-map-%s.html" % slug)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__TITLE__", dom))
    sys.stdout.write("Da ghi %s — %d trang, %d link noi linh vuc (%d da gan loai).\n"
                     % (os.path.relpath(path, root), len(nodes), len(es), data["typed"]))


def run(cmd, args, root, wiki):
    if cmd == "--graph":
        cmd_graph(root, wiki, "--no-save" in args)
    elif cmd == "--neighbors":
        cmd_neighbors(wiki, args)
    elif cmd == "--relations":
        cmd_relations(wiki, args[0] if args else None)
    elif cmd == "--map":
        if not args:
            sys.exit("Thieu ten linh vuc. Dung: --map <linh vuc>")
        cmd_map(root, wiki, args[0])
