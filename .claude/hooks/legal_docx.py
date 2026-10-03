#!/usr/bin/env python3
"""Doc van ban quy pham tu .docx (chi doc nguon): cay dia chi, trang node nguyen van, tham chieu, doi chieu.

Dung boi skill /ingest-legal. Don vi trang = 1 Dieu, hoac 1 Muc La Ma cua phu luc; khoan/diem/tiet la
block ID `^d12-k4-a-iv`. Trich dan noi bo trong nguyen van duoc boc link, chu hien thi giu nguyen.

  legal_docx.py <docx> --tree [<dia chi>]      cay dia chi + thong ke + diem nghi van (so nhay coc, dia chi trung)
  legal_docx.py <docx> --refs [<dia chi>]      tham chieu: noi bo / chua giai duoc / van ban ngoai
  legal_docx.py <docx> --check-formulas        tu/mau moi phan so trong LaTeX == trong XML goc
  legal_docx.py <docx> --nodes  --short S --sid ID          danh sach node va ten trang
  legal_docx.py <docx> --node <dia chi> --short S --sid ID  in mot trang ra stdout
  legal_docx.py <docx> --write <thu muc> --short S --sid ID [--tags "a, b"] [--date YYYY-MM-DD]
                                               ghi moi trang + trang muc luc; giu khoi chu giai da viet
  legal_docx.py <docx> --state [<thu muc>] --short S --sid ID   bang node cho 03_state/<ID>.md
  legal_docx.py <docx> --verify <thu muc|trang>             nguyen van trang == nguon; link #^anchor; node thieu

Exit 0 = dat; 1 = co lech; 2 = sai tham so. Khong bao gio ghi vao 01_sources/.
"""
import datetime
import hashlib
import os
import re
import sys
import unicodedata
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}


# ---------- OMML -> LaTeX ----------
def tex_text(s):
    s = re.sub(r"([%_#&$])", r"\\\1", s)
    return r"\text{%s}" % s if s else ""


def omml(e):
    tag = e.tag.replace(M, "")
    if tag == "r":
        return tex_text("".join(t.text or "" for t in e.iter(M + "t")))
    if tag == "f":
        return r"\frac{%s}{%s}" % (omml(e.find(M + "num")), omml(e.find(M + "den")))
    if tag == "d":
        pr = e.find(M + "dPr")
        beg, end, sep = "(", ")", "|"
        if pr is not None:
            for name in ("begChr", "endChr", "sepChr"):
                x = pr.find(M + name)
                if x is not None:
                    v = x.get(M + "val") or ""
                    if name == "begChr":
                        beg = v
                    elif name == "endChr":
                        end = v
                    else:
                        sep = v
        esc = lambda c: {"[": "[", "]": "]", "{": r"\{", "}": r"\}"}.get(c, c)
        return r"\left%s %s \right%s" % (
            esc(beg) or ".", (" %s " % sep).join(omml(x) for x in e.findall(M + "e")), esc(end) or ".")
    if tag == "sSub":
        return "%s_{%s}" % (omml(e.find(M + "e")), omml(e.find(M + "sub")))
    if tag == "sSup":
        return "%s^{%s}" % (omml(e.find(M + "e")), omml(e.find(M + "sup")))
    if tag == "nary":
        ch = e.find(M + "naryPr").find(M + "chr")
        op = {"∑": r"\sum", "∏": r"\prod"}.get(ch.get(M + "val") if ch is not None else "∫", r"\int")
        sub, sup = omml(e.find(M + "sub")), omml(e.find(M + "sup"))
        return op + ("_{%s}" % sub if sub else "") + ("^{%s}" % sup if sup else "") + " " + omml(e.find(M + "e"))
    if tag == "eqArr":
        return " ".join(omml(x) for x in e.findall(M + "e"))
    if tag.endswith("Pr"):
        return ""
    out, run = [], []
    for c in e:  # gop cac run lien nhau o CUNG cap; khong gop xuyen qua phan so/ngoac
        if c.tag == M + "r":
            run.append("".join(t.text or "" for t in c.iter(M + "t")))
            continue
        if run:
            out.append(tex_text("".join(run)))
            run = []
        out.append(omml(c))
    if run:
        out.append(tex_text("".join(run)))
    return "".join(out)


def math_plain(e):
    return "".join(t.text or "" for t in e.iter(M + "t"))


# ---------- khoi ----------
def para(p):
    """-> (text co $latex$, text phang, co phai thuan cong thuc)"""
    out, plain, nonmath = [], [], []

    def walk(e):
        for c in e:
            if c.tag == M + "oMath":
                out.append("$" + omml(c) + "$")
                plain.append(math_plain(c))
            elif c.tag == W + "t":
                out.append(c.text or "")
                plain.append(c.text or "")
                nonmath.append(c.text or "")
            elif c.tag in (W + "tab", W + "br"):
                out.append(" ")
                plain.append(" ")
            elif c.tag == W + "tbl":
                continue
            else:
                walk(c)

    walk(p)
    sq = lambda xs: re.sub(r"\s+", " ", unicodedata.normalize("NFC", "".join(xs))).strip()
    text = sq(out).replace("$$", "$ $")
    return text, sq(plain), ("$" in text and not sq(nonmath))


def table(tbl):
    rows = []
    for tr in tbl.findall(W + "tr"):
        cells = []
        for tc in tr.findall(W + "tc"):
            pr = tc.find(W + "tcPr")
            span, cont = 1, False
            if pr is not None:
                g, v = pr.find(W + "gridSpan"), pr.find(W + "vMerge")
                if g is not None:
                    span = int(g.get(W + "val"))
                if v is not None and v.get(W + "val") != "restart":
                    cont = True
            txt = "<br>".join(x for x in (para(p)[0] for p in tc.findall(W + "p")) if x)
            cells.append("" if cont else txt)
            cells.extend([""] * (span - 1))
        rows.append(cells)
    return rows


def load(path):
    z = zipfile.ZipFile(path)
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    blocks = []
    for ch in body:
        if ch.tag == W + "p":
            text, plain, is_math = para(ch)
            if text:
                blocks.append({"kind": "p", "text": text, "plain": plain, "math": is_math})
        elif ch.tag == W + "tbl":
            blocks.append({"kind": "t", "rows": table(ch), "text": "", "plain": "", "math": False})
    for i, b in enumerate(blocks):
        b["n"] = i
    return blocks


# ---------- cay dia chi ----------
LV = {"phan": 1, "muc": 2, "khoan": 3, "diem": 4, "tiet": 5, "leaf": 6}


def classify(blocks):
    scope = None  # ("D", n) | ("PL", n) | None
    stack = []  # [(level, comp)]
    counters = {}
    seen = {}
    inquote = False
    hub_n, path = {}, []  # dem khoi cua trang muc luc; duong dan Chuong > Muc hien tai

    def addr_of():
        return ".".join(c for _, c in stack)

    amend = [None]

    def push(level, comp):
        while stack and stack[-1][0] >= level:
            stack.pop()
        if amend[0] and level <= amend[0][0]:
            amend[0] = None
        stack.append((level, comp))

    def leaf(prefix):
        base = addr_of()
        counters[(base, prefix)] = counters.get((base, prefix), 0) + 1
        return "%s.%s%d" % (base, prefix, counters[(base, prefix)])

    for b in blocks:
        t = b["plain"]
        b["role"] = "p"
        m = re.match(r"Điều (\d+)\. ?", t) if b["kind"] == "p" else None
        if m and (scope is None or scope[0] != "PL"):
            scope = ("D", int(m.group(1)))
            stack[:] = [(0, "D%s" % m.group(1))]
            b["addr"], b["role"] = addr_of(), "head"
        elif b["kind"] == "p" and re.match(r"Phụ lục [IVX]+$", t):
            num = ROMAN[t.split()[-1]]
            scope = ("PL", num)
            stack[:] = [(0, "PL%d" % num)]
            b["addr"], b["role"] = addr_of(), "head"
        elif b["kind"] == "p" and scope and scope[0] == "D" and (
                re.match(r"(Chương [IVX]+|Mục \d+)\b", t) or (t.isupper() and len(stack) == 0)):
            scope, stack[:] = None, []
            b["addr"], b["role"] = "", "struct"
        elif scope is None:
            b["addr"], b["role"] = "", ("struct" if t.isupper() or re.match(r"(Chương|Mục) ", t) else "pre")
        elif b["kind"] == "t" and scope[0] == "D" and len(stack) == 1 and any(
                "Nơi nhận" in c for row in b["rows"] for c in row):
            b["addr"], b["role"] = "", "pre"  # bang chu ky cuoi van ban: thuoc trang muc luc, khong thuoc Dieu cuoi
        elif b["kind"] == "t":
            b["addr"], b["role"] = leaf("t"), "table"
        elif inquote or t.startswith("“"):
            b["addr"], b["role"] = leaf("q"), "quote"
            inquote = not re.search(r"”[.;]?$", t)
        else:
            head = t
            mp = re.match(r"PHẦN ([A-Z])\. ", t) if scope[0] == "PL" else None
            mm = re.match(r"([IVX]+)\. ", t) if scope[0] == "PL" else None
            mk = re.match(r"(\d+(?:\.\d+)*)\. ?" if scope[0] == "PL" else r"(\d+)\. ?", head)
            md = re.match(r"([a-zđ])\) ", t)
            mt = re.match(r"\(([ivx]+)\) ", t)
            if mp:
                push(LV["phan"], mp.group(1)); b["role"] = "head"; b["addr"] = addr_of()
            elif mm and mm.group(1) in ROMAN:
                push(LV["muc"], mm.group(1)); b["role"] = "head"; b["addr"] = addr_of()
            elif mk:
                push(LV["khoan"], "k" + mk.group(1).replace(".", "_")); b["role"] = "khoan"; b["addr"] = addr_of()
            elif md:
                push(LV["diem"], md.group(1)); b["role"] = "diem"; b["addr"] = addr_of()
            elif mt:
                push(LV["tiet"], mt.group(1)); b["role"] = "tiet"; b["addr"] = addr_of()
            elif re.match(r"Ví dụ\b", t):
                while stack and stack[-1][0] >= LV["diem"]:
                    stack.pop()
                base = addr_of()
                counters[(base, "vd")] = counters.get((base, "vd"), 0) + 1
                stack.append((LV["diem"], "vd%d" % counters[(base, "vd")]))
                b["role"] = "vidu"; b["addr"] = addr_of()
            elif t.startswith("- "):
                b["role"] = "gach"; b["addr"] = leaf("g")
            elif b["math"]:
                b["role"] = "formula"; b["addr"] = leaf("f")
            else:
                b["addr"] = leaf("p")
        hub = not b.get("addr")
        if hub:  # can cu, tieu de Chuong/Muc, bang dau/cuoi van ban -> trang muc luc
            kind = "t" if b["kind"] == "t" else "p"
            hub_n[kind] = hub_n.get(kind, 0) + 1
            b["addr"] = "H.%s%d" % (kind, hub_n[kind])
            if b["role"] == "struct":
                if re.match(r"Chương [IVX]+", t):
                    path[:] = [t]
                elif re.match(r"Mục \d+", t):
                    path[:] = path[:1] + [t]
                elif path:
                    path[-1] += (". " if re.match(r"(Chương [IVX]+|Mục \d+)$", path[-1]) else " ") + t
        elif b["role"] == "head" and scope and scope[0] == "D" and len(stack) == 1:
            b["path"] = list(path)
        if b["addr"] in seen:
            b["dup"] = seen[b["addr"]]
        seen.setdefault(b["addr"], b["n"])
        b["stack"] = [(0, "H")] if hub else list(stack)
        if amend[0]:
            b["amend"] = amend[0][1]
        ma = re.search(r"Sửa đổi, bổ sung.*?((?:Thông tư|Nghị định|Luật) số \S+)", t) if b["kind"] == "p" and b["role"] in ("khoan", "diem") else None
        if ma:
            amend[0] = (stack[-1][0], ma.group(1))
        b["depth"] = 1 if hub else len(stack) - 1 + (1 if b["role"] in ("gach", "formula", "p", "table", "quote") else 0)
    tree = {b["addr"]: b for b in blocks if b.get("addr")}
    for b in blocks:
        if b["kind"] == "t" and b.get("addr"):
            for rid, _ in table_rows(b):
                tree.setdefault("%s.%s" % (b["addr"], rid), b)
    return tree


def anchor(addr):
    return "^" + re.sub(r"[._]", "-", addr).lower().replace("đ", "dd").replace("~", "x").replace("#", "n")


def node_of(addr, tree=None):
    """Dia chi -> dia chi node chua no (Dieu, hoac Muc La Ma cua phu luc; con lai ve hub phu luc)."""
    b = tree.get(addr) if tree else None
    if b is None:
        return addr.split(".")[0]
    st = b["stack"]
    if any(l == LV["muc"] for l, _ in st):
        return ".".join(c for l, c in st if l <= LV["muc"])
    return st[0][1]


def page_name(node, short):
    p = node.split(".")
    if node == "H":
        return short
    if p[0].startswith("D"):
        return "%s-article-%s" % (short, p[0][1:])
    return "-".join([short, "appendix", p[0][2:]] + [x.lower() for x in p[1:]])


# ---------- tham chieu ----------
REF = re.compile(
    r"(?:[Đđ]iểm\s+(?P<d>(?:\d+)?[a-zđ](?:\([ivx]+\))?(?:(?:\s*,\s*|\s+(?:và|hoặc)\s+)(?:điểm\s+)?[a-zđ](?:\([ivx]+\))?)*)\s+)?"
    r"(?:Điểm\s+(?P<dn>\d+)\s+(?=Mục))?"
    r"(?:[Kk]hoản\s+(?P<k>\d+(?:\.\d+)*(?:(?:\s*,\s*|\s+(?:và|hoặc)\s+)(?:khoản\s+)?\d+(?:\.\d+)*)*)\s+)?"
    r"(?P<base>Điều\s+\d+|Điều này|khoản này"
    r"|Mục\s+(?P<muc>[IVX]+(?:\s*,\s*[IVX]+)*)\b(?:\s+Phần\s+(?P<mphan>[A-Z]\b|này))?(?:\s+Phụ lục\s+(?P<mpl>[IVX]+\b|này))?"
    r"|Mục này|Phần\s+(?P<phan>[A-Z])\b(?:\s+Phụ lục\s+(?P<ppl>[IVX]+\b|này))?|Phần này"
    r"|Phụ lục\s+(?P<pl>[IVX]+)\b|Phụ lục này)"
    r"(?=(?P<tail>[^;.]{0,70}))")
EXT = re.compile(r"^\s*(?:,\s*(?:Điều\s+)?\d+[^;.]*?)?\s*(Luật|Nghị định|Thông tư số|Bộ luật)")
EXT_PL = re.compile(r"^\s*(?:kèm theo\s+)?(Thông tư số|Thông tư quy định|quy định của|Luật|Nghị định)")
LIST_TAIL = re.compile(r"Phần\s+([A-Z])\s+Phụ lục\s+([IVX]+)\b")
# Ten van ban ngoai: luat da biet ten truoc (ten luat khong co dau ket thuc), mau chung sau.
LAWS = ["Luật Các tổ chức tín dụng", "Luật Ngân hàng Nhà nước Việt Nam", "Luật Ngân hàng Nhà nước"]
DOCNO = r"\d+/\d{4}/[\w\-]+"
DOC = re.compile(r"(?:Thông tư|Nghị định|Quyết định|Nghị quyết|Chỉ thị) số %s|(?:%s|(?:Bộ luật|Luật)(?: [^\s,;:.()]+){1,5}?(?= số \d)|Luật(?= số \d))(?: số %s)?" % (
    DOCNO, "|".join(LAWS), DOCNO))
MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "03_state", "_sources_manifest.md")
_INGESTED = None


def ext_note(cite):
    """Ghi chu cho dan chieu van ban ngoai: da co nguon trong ban ke (theo so hieu o dong Nhan de) hay chua."""
    global _INGESTED
    if _INGESTED is None:
        _INGESTED, sid = {}, None
        if os.path.isfile(MANIFEST):
            for l in open(MANIFEST, encoding="utf-8"):
                h = re.match(r"## (\S+)\s*$", l)
                t = re.match(r"\| Nhan đề \| \*(?:Thông tư|Nghị định|Luật[^|*]*?) số (%s)" % DOCNO, l)
                sid = h.group(1) if h else sid
                if t and sid:
                    _INGESTED[t.group(1)] = sid
    m = re.search(DOCNO, cite)
    if m and m.group(0) in _INGESTED:
        return "văn bản ngoài — đã ingest dạng khái niệm, nguồn `%s`; chưa có trang điều khoản" % _INGESTED[m.group(0)]
    return "văn bản ngoài, chưa ingest vào wiki"


def resolve(m, b):
    """-> (danh sach dia chi dich, 'int'|'ext'|'sect')"""
    base, tail = m.group("base"), m.group("tail") or ""
    if base.startswith("Điều ") and base != "Điều này" and not tail.lstrip().startswith("Thông tư này") and EXT.match(tail):
        return [], "ext"
    if b.get("amend"):
        return [], "ext"
    if ("Phụ lục" in base and base != "Phụ lục này") and EXT_PL.match(tail):
        return [], "ext"
    st = b["stack"]
    upto = lambda lv: ".".join(c for l, c in st if l <= lv)
    has = lambda lv: any(l == lv for l, _ in st)
    root0 = st[0][1]
    in_pl = root0.startswith("PL")
    plnum = lambda v: root0 if v in (None, "này") else "PL%d" % ROMAN[v]
    roots = []
    if base == "Điều này":
        roots = [root0]
    elif base.startswith("Điều"):
        roots = ["D" + base.split()[1]]
    elif base == "khoản này":
        roots = [upto(LV["khoan"])] if has(LV["khoan"]) else []
    elif base == "Mục này":
        if not has(LV["muc"]):
            return [], "sect"
        roots = [upto(LV["muc"])]
    elif base == "Phần này":
        roots = [upto(LV["phan"])]
    elif base == "Phụ lục này":
        roots = [root0]
    elif m.group("muc"):
        mpl, mph = m.group("mpl"), m.group("mphan")
        if not in_pl and mpl in (None, "này"):
            lt = LIST_TAIL.search(re.split(r"\.(?:\s|$)", m.string[m.end("base"):])[0])
            if not lt:
                return ["?.Mục " + m.group("muc")], "int"
            mph, mpl = mph or lt.group(1), lt.group(2)
        pl = plnum(mpl)
        if mph and mph != "này":
            part = mph
        elif mpl in (None, "này") or mph == "này":
            part = next((c for l, c in st if l == LV["phan"]), None)
        else:
            part = None
        roots = [".".join(x for x in (pl, part, r.strip()) if x) for r in m.group("muc").split(",")]
    elif m.group("phan"):
        if not in_pl and m.group("ppl") in (None, "này"):
            return ["?.Phần " + m.group("phan")], "int"
        roots = ["%s.%s" % (plnum(m.group("ppl")), m.group("phan"))]
    elif m.group("pl"):
        roots = ["PL%d" % ROMAN[m.group("pl")]]
    ks = [k.replace(".", "_") for k in re.findall(r"\d+(?:\.\d+)*", m.group("k") or m.group("dn") or "")]
    ds = re.findall(r"(\d+)?([a-zđ])(?:\(([ivx]+)\))?(?![a-zà-ỹ])", re.sub(r"điểm|và|hoặc", " ", m.group("d") or ""))
    out = []
    for r in roots:
        for ki, k in enumerate(["k" + k for k in ks] or [None]):
            if ds and ki == 0:
                for num, d, ti in ds:
                    out.append(".".join([r] + (["k" + num] if num else ([k] if k else [])) + [d] + ([ti] if ti else [])))
            else:
                out.append(".".join([r] + ([k] if k else [])))
    return out, "int"


def fix_row(t, tree):
    """'X.a' khong co nhung bang X.t<n> co dong 'ra' -> tro vao dong bang."""
    if t in tree or "." not in t:
        return t
    par, last = t.rsplit(".", 1)
    for n in range(1, 4):
        cand = "%s.t%d.r%s" % (par, n, last)
        if cand in tree:
            return cand
    return t


def all_refs(blocks, tree):
    refs = []
    for b in blocks:
        if not b.get("addr"):
            continue
        texts = [(b["addr"], b["plain"])] if b["kind"] == "p" else [
            ("%s.%s" % (b["addr"], rid), c) for rid, row in table_rows(b) for c in row]
        for src, txt in texts:
            if b["role"] == "quote" or (b["role"] == "head" and b["kind"] == "p" and re.match(r"(Điều \d+\.|Phụ lục)", txt)):
                continue
            ws = lambda s: re.sub(r"\s+", " ", s).strip()
            ext_cites, cov = [], 0
            for m in REF.finditer(txt):
                tg, kind = resolve(m, b)
                tg = [fix_row(x, tree) for x in tg]
                cite = ws(m.group(0))
                if kind == "ext":
                    if m.start() < cov:  # da nam trong trich dan lien ke truoc do ("Điều 135, Điều 136 Luật ...")
                        continue
                    if b.get("amend"):
                        cite += " " + b["amend"]
                    else:
                        rest = txt[m.end("base"):]
                        mi = DOC.search(rest)
                        if mi and mi.start() <= len(m.group("tail")):
                            tl, cov = ws(rest[: mi.end()]), m.end("base") + mi.end()
                        else:
                            tl = ws(m.group("tail")) + ("…" if len(m.group("tail")) == 70 else "")
                        cite += ("" if tl.startswith(",") else " ") + tl
                    cite = cite.rstrip(",:")
                    ext_cites.append(cite)
                refs.append({"src": src, "cite": cite, "targets": tg, "kind": kind})
            for dm in DOC.finditer(txt):  # nhac ca van ban, khong kem dieu khoan
                doc = ws(dm.group(0))
                if not any(doc in c for c in ext_cites):
                    refs.append({"src": src, "cite": doc, "targets": [], "kind": "doc"})
    return refs


# ---------- bang ----------
def table_rows(b):
    out, used = [], {}
    for i, row in enumerate(b["rows"]):
        first = row[0].strip() if row else ""
        m = re.match(r"(\d+(?:\.\d+)*)\.?$", first) or re.match(r"([a-zđ])\)", first)
        rid = "r" + m.group(1) if m else "h%d" % i if i < 3 and not any(re.search(r"\d%$", c) for c in row) else "r#%d" % i
        if rid in used:
            rid += "~%d" % i
        used[rid] = 1
        out.append((rid, row))
    return out


TOK_D = re.compile(r"(?<![a-zà-ỹ])(?:\d+)?[a-zđ](?:\([ivx]+\))?(?![a-zà-ỹ(])")
TOK_K = re.compile(r"\d+(?:\.\d+)*")
TOK_M = re.compile(r"[IVX]+")


def ref_spans(m, b, tree):
    """Mot trich dan -> [(start, end, dia chi dich)] de boc link ngay trong nguyen van."""
    tg, kind = resolve(m, b)
    tg = [fix_row(x, tree) for x in tg]
    if kind != "int" or not tg or any(t not in tree for t in tg):
        return []
    if len(tg) == 1:
        return [(m.start(), m.end(), tg[0])]
    toks = []
    grp = lambda name: m.groupdict().get(name)
    kname = "k" if grp("k") else "dn" if grp("dn") else None
    if grp("d"):
        toks += [(m.start("d") + x.start(), m.start("d") + x.end()) for x in TOK_D.finditer(grp("d"))]
        if kname:  # diem chi gan voi khoan dau; cac khoan sau dung rieng
            toks += [(m.start(kname) + x.start(), m.start(kname) + x.end()) for x in TOK_K.finditer(grp(kname))][1:]
    elif kname:
        toks += [(m.start(kname) + x.start(), m.start(kname) + x.end()) for x in TOK_K.finditer(grp(kname))]
    elif grp("muc"):
        toks += [(m.start("muc") + x.start(), m.start("muc") + x.end()) for x in TOK_M.finditer(grp("muc"))]
    if len(toks) != len(tg):
        return [(m.start(), m.end(), tg[0])]
    toks[-1] = (toks[-1][0], m.end())  # token cuoi keo het cum "... khoan 2 Dieu nay"
    return [(s, e, t) for (s, e), t in zip(toks, tg)]


def linkify(text, b, ctx, in_table=False):
    """Boc [[...|chu goc]] quanh tung trich dan noi bo; chu hien thi giu nguyen van."""
    if not ctx or b["role"] == "quote" or (b["role"] == "head" and re.match(r"(Điều \d+\.|Phụ lục)", text)):
        return text
    tree, short, node = ctx["tree"], ctx["short"], ctx["node"]
    math = [(x.start(), x.end()) for x in re.finditer(r"\$[^$]*\$", text)]
    spans = []
    for m in REF.finditer(text):
        if any(s <= m.start() < e for s, e in math):
            continue
        spans += ref_spans(m, b, tree)
    out, pos = [], 0
    bar = "\\|" if in_table else "|"
    for s, e, t in sorted(spans):
        if s < pos:
            continue
        blk, tn = tree[t], node_of(t, tree)
        anc = anchor(blk["addr"] if blk["kind"] == "t" else t)
        target = ("" if tn == node else page_name(tn, short)) + ("" if t == tn else "#" + anc)
        if not target:  # tro ve chinh node hien tai
            target = "#" + anchor(node)
        out += [text[pos:s], "[[%s%s%s]]" % (target, bar, text[s:e])]
        pos = e
    return "".join(out) + text[pos:]


def unlink(s):
    return re.sub(r"\[\[[^\]|\\]*\\?\|([^\]]*)\]\]", r"\1", s)


def table_md(b, ctx=None):
    rows = table_rows(b)
    width = max(len(r) for _, r in rows)
    esc = lambda s: linkify(s.replace("|", "\\|"), b, ctx, in_table=True)
    lines = []
    for i, (rid, row) in enumerate(rows):
        row = row + [""] * (width - len(row))
        lines.append("| `%s` | %s |" % (rid, " | ".join(esc(c) for c in row)))
        if i == 0:
            lines.append("|" + "---|" * (width + 1))
    return lines


# ---------- xuat node ----------
HUB = "H"
NOTE_HEAD = "Chú giải (diễn giải, không phải quy phạm):"
NOTE_EMPTY = "(chưa viết)"
REF_OUT_HEAD = "Tham chiếu ra (ngoài các link đã có trong nguyên văn):"
DIEM_ORDER = list("abcdđeghiklmnopqrstuvxy")
TIET_ORDER = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv"]


def node_blocks(blocks, node, tree=None):
    return [b for b in blocks if b.get("addr") and node_of(b["addr"], tree) == node]


def node_order(blocks, tree):
    order = []
    for b in blocks:
        if b.get("addr"):
            n = node_of(b["addr"], tree)
            if n != HUB and n not in order:
                order.append(n)
    return order


def node_label(node):
    p = node.split(".")
    if p[0].startswith("D"):
        return "Điều " + p[0][1:]
    inv = {v: k for k, v in ROMAN.items()}
    out = "Phụ lục " + inv[int(p[0][2:])]
    if len(p) == 3:
        out += ", Phần %s, Mục %s" % (p[1], p[2])
    elif len(p) == 2:  # node hai cap luon la Muc (phu luc khong chia Phan)
        out += ", Mục " + p[1]
    return out


def position_line(node, blocks, tree, short):
    order = node_order(blocks, tree)
    i = order.index(node)
    head = tree[node]
    if node.startswith("D"):
        path = head.get("path") or []
    else:
        p = node.split(".")
        path = [tree[".".join(p[:k])]["plain"] for k in range(1, len(p)) if ".".join(p[:k]) in tree]
    parts = ["[[%s|Mục lục]]" % short] + path
    line = "Vị trí: " + " › ".join(parts)
    if i > 0:
        line += " · trước: [[%s|%s]]" % (page_name(order[i - 1], short), node_label(order[i - 1]))
    if i + 1 < len(order):
        line += " · sau: [[%s|%s]]" % (page_name(order[i + 1], short), node_label(order[i + 1]))
    return line


def render(blocks, node, tree, short):
    lines = []
    ctx = {"tree": tree, "short": short, "node": node}
    base_depth = len(node.split(".")) - 1
    for b in node_blocks(blocks, node, tree):
        a = anchor(b["addr"])
        d = max(0, b["depth"] - base_depth - 1)
        text = linkify(b["text"], b, ctx) if b["kind"] == "p" else ""
        if b["kind"] == "t":
            lines += [""] + table_md(b, ctx) + ["", a, ""]
        elif b["addr"] == node:
            lines += [text + " " + a, ""]
        elif d == 0 and b["role"] in ("khoan", "head"):
            lines.append(text + " " + a)
        else:
            txt = text if b["role"] == "gach" else "- " + text
            lines.append("   " * max(d, 1) + txt + " " + a)
    return lines


def render_hub(blocks, tree, short):
    """Trang muc luc: can cu + tieu de Chuong/Muc (nguyen van) xen link toi tung node theo thu tu van ban."""
    lines, done = [], set()
    for b in blocks:
        a = b.get("addr")
        if not a:
            continue
        n = node_of(a, tree)
        if n == HUB:
            if lines and lines[-1] != "":
                lines.append("")
            if b["kind"] == "t":
                lines += [""] + table_md(b) + ["", anchor(a), ""]
            else:
                lines += [b["text"] + " " + anchor(a), ""]
        elif n not in done:
            done.add(n)
            if n.startswith("D"):
                label = tree[n]["plain"]
            elif "." in n:  # "Phu luc I, Phan B — III. Nguon von ban buon"
                label = "%s — %s" % (node_label(n).rsplit(", ", 1)[0], tree[n]["plain"])
            else:
                label = node_label(n) + (" — " + tree[n + ".p1"]["plain"] if n + ".p1" in tree else "")
            lines.append("- [[%s|%s]]" % (page_name(n, short), label))
    return lines


def frontmatter(node, nb, path, short, sid, tags, sha, date):
    return "\n".join([
        "---",
        "title: %s" % page_name(node, short),
        "type: provision",
        "tags: [%s]" % tags,
        "sources: [%s]" % sid,
        "status: draft",
        "last_updated: %s" % date,
        "address: %s" % node,
        "span: ¶%d–%d" % (min(b["n"] for b in nb), max(b["n"] for b in nb)),
        "source_file: %s" % path.replace("\\", "/").split("/")[-1],
        "source_sha256: %s" % sha,
        "---",
    ])


def dedupe(refs):
    seen, out = set(), []
    for r in refs:
        key = (r["src"], r["cite"], tuple(r["targets"]))
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def build_page(blocks, tree, refs, node, cfg, date, note=NOTE_EMPTY):
    short = cfg["short"]
    nb = node_blocks(blocks, node, tree)
    out = [frontmatter(node, nb, cfg["path"], short, cfg["sid"], cfg["tags"], cfg["sha"], date), ""]
    if node == HUB:
        return "\n".join(out + render_hub(blocks, tree, short)).rstrip("\n") + "\n"
    out += [position_line(node, blocks, tree, short), ""]
    out += render(blocks, node, tree, short)
    inside = lambda a: node_of(a, tree) == node

    def link(t):
        tn = node_of(t, tree)
        if t == tn:
            return "[[%s]]" % page_name(t, short)
        blk = tree.get(t)
        if blk is not None and blk["kind"] == "t" and t != blk["addr"]:
            return "[[%s#%s]] dòng `%s`" % (page_name(tn, short), anchor(blk["addr"]), t[len(blk["addr"]) + 1:])
        return "[[%s#%s]]" % (page_name(tn, short), anchor(t))

    def inlined(r):
        if r["kind"] != "int" or not r["targets"] or any(t not in tree for t in r["targets"]):
            return False
        blk = tree[r["src"]]
        if blk["kind"] == "t":
            return True
        return r["cite"] in re.sub(r"\s+", " ", re.sub(r"\$[^$]*\$", " ", blk["text"]))

    out += ["", REF_OUT_HEAD]
    rest = [r for r in refs if inside(r["src"]) and not inlined(r)]
    for r in rest:
        if r["kind"] in ("ext", "doc"):
            out.append("- `%s` → %s (%s)" % (r["src"], r["cite"], ext_note(r["cite"])))
        elif r["kind"] == "sect":
            out.append("- `%s` → Mục (thuộc Chương) chứa Điều này — \"%s\" (không phải node)" % (r["src"], r["cite"]))
        else:
            tg = ", ".join((link(t) if t in tree else "⚠️ không thấy `%s`" % t) for t in r["targets"]) or "⚠️ không giải được"
            out.append("- `%s` → %s — \"%s\" (trong công thức)" % (r["src"], tg, r["cite"]))
    if not rest:
        out.append("- (không có)")
    out += ["", "Tham chiếu vào:"]
    n_in = 0
    for r in refs:
        if r["kind"] == "int" and not inside(r["src"]):
            for t in r["targets"]:
                if t in tree and inside(t):
                    n_in += 1
                    out.append("- `%s` (%s) → `%s` — \"%s\"" % (r["src"], link(r["src"]), anchor(tree[t]["addr"] if tree[t]["kind"] == "t" else t), r["cite"]))
    if not n_in:
        out.append("- (không có)")
    out += ["", NOTE_HEAD, note.strip() or NOTE_EMPTY]
    return "\n".join(out).rstrip("\n") + "\n"


def split_note(page):
    """-> (phan truoc chu giai, chu giai)."""
    i = page.find("\n" + NOTE_HEAD)
    if i < 0:
        return page, NOTE_EMPTY
    return page[:i], page[i + len(NOTE_HEAD) + 1:].strip() or NOTE_EMPTY


def norm(s):
    s = unlink(unicodedata.normalize("NFC", s))
    s = re.sub(r"\s*\^[a-z0-9][-a-z0-9]*\s*$", "", s.strip())
    s = re.sub(r"^-\s+", "", s.strip())
    return re.sub(r"\s+", " ", s).strip()


# ---------- kiem ----------
def audit(blocks, tree):
    """Day so lien tuc: Dieu 1..N, khoan 1..n, diem a,b,c,d,đ..., tiet (i),(ii)... Nhay coc = diem nghi van."""
    out, last = [], {}
    arts = [int(b["addr"][1:]) for b in blocks if b.get("role") == "head" and re.match(r"D\d+$", b.get("addr", ""))]
    if arts != list(range(1, len(arts) + 1)):
        out.append("Số Điều không liên tục: %s" % arts)
    for b in blocks:
        role, a = b.get("role"), b.get("addr", "")
        if role not in ("khoan", "diem", "tiet") or "dup" in b:
            continue
        par, comp = a.rsplit(".", 1)
        prev = last.get((par, role))
        if role == "khoan":
            nums = [int(x) for x in comp[1:].split("_")]
            if len(nums) > 1:  # khoan con 2.1, 3.2.1: so sanh trong cung khoan me
                key = (par, "k" + "_".join(map(str, nums[:-1])))
                prev, last[key] = last.get(key), nums[-1]
                ok = nums[-1] == (prev or 0) + 1
            else:
                ok = nums[0] == (prev or 0) + 1
                last[(par, role)] = nums[0]
        else:
            seq = DIEM_ORDER if role == "diem" else TIET_ORDER
            idx = seq.index(comp) if comp in seq else -1
            ok = idx == (prev if prev is not None else -1) + 1
            last[(par, role)] = idx
        if not ok:
            out.append("¶%d %s: thứ tự nhảy cóc — \"%s\"" % (b["n"], a, b["plain"][:50]))
    for b in blocks:
        if "dup" in b:
            out.append("¶%d %s: địa chỉ trùng với ¶%d" % (b["n"], b["addr"], b["dup"]))
    return out


def check_formulas(path):
    body = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml")).find(W + "body")
    plain = lambda e: "".join(t.text or "" for t in e.iter(M + "t"))
    untext = lambda s: re.sub(r"\\text\{([^{}]*)\}", r"\1", s).replace("\\%", "%").replace("\\_", "_")
    frac = re.compile(r"\\frac\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}")
    sq = lambda xs: [tuple(re.sub(r"\\left|\\right|[\s()\[\]]", "", v) for v in x) for x in xs]
    bad = n = 0
    for n, om in enumerate(body.iter(M + "oMath"), 1):
        tex = omml(om)
        got = sq([(untext(a), untext(b)) for a, b in frac.findall(tex)])
        want = sq([(plain(f.find(M + "num")), plain(f.find(M + "den"))) for f in om.iter(M + "f")])
        bad += got != want
        print("%2d %s %s" % (n, "OK  " if got == want else "LỆCH", untext(tex)))
    print("%d công thức, %d lệch phân số" % (n, bad))
    return bad


def verify_page(page, blocks, tree, sha, refs=None):
    """-> (so khoi, so lech, link chet, ghi chu)"""
    fm, body = page.split("---", 2)[1:]
    node = re.search(r"^address:\s*(\S+)", fm, re.M).group(1)
    msgs = []
    psha = re.search(r"^source_sha256:\s*(\S+)", fm, re.M)
    if psha and psha.group(1) != sha:
        msgs.append("SHA nguồn trong trang khác file hiện tại — nguồn đã đổi")
    verb = body.split("\nTham chiếu ra")[0]
    got = {}
    for l in verb.split("\n"):
        m = re.search(r"\^([a-z0-9][-a-z0-9]*)\s*$", l)
        if m and l.strip() != "^" + m.group(1):
            got["^" + m.group(1)] = norm(l)
    nb = node_blocks(blocks, node, tree)
    bad = 0
    for b in nb:
        a = anchor(b["addr"])
        ok = ("\n".join(table_md(b)) in unlink(verb)) if b["kind"] == "t" else got.get(a) == norm(b["text"])
        if not ok:
            bad += 1
            msgs.append("LỆCH ¶%d %s" % (b["n"], a))
    extra = set(got) - {anchor(b["addr"]) for b in nb}
    for a in sorted(extra):
        bad += 1
        msgs.append("THỪA %s (không có trong nguồn)" % a)
    valid = {anchor(a) for a in tree}
    dead = [x for x in re.findall(r"\[\[[^\]|#\\]*#(\^[-a-z0-9]+)", page) if x not in valid]
    msgs += ["LINK CHẾT %s" % x for x in dead]
    if not bad and not dead and refs is not None:
        # Ca trang (tru chu giai) phai dung bang ban sinh tu nguon: bat link bi doi dich, bo cuc bi sua tay.
        fld = lambda k: (re.search(r"^%s:\s*(.*)$" % k, fm, re.M) or [None, ""])[1].strip()
        title = fld("title")
        suffix = page_name(node, "")
        cfg = {"short": title[: len(title) - len(suffix)] if suffix else title, "sid": fld("sources").strip("[]"),
               "tags": fld("tags").strip("[]"), "path": fld("source_file"), "sha": sha}
        if build_page(blocks, tree, refs, node, cfg, fld("last_updated"), split_note(page)[1]) != page:
            bad += 1
            msgs.append("KHÁC BẢN SINH TỪ NGUỒN (link hoặc bố cục bị sửa tay) — chạy lại --write")
    return len(nb), bad, len(dead), msgs


USAGE = __doc__


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        sys.stdout.write(USAGE)
        sys.exit(0)
    path, cmd = sys.argv[1], sys.argv[2]
    arg = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith("--") else ""
    opt = lambda k, dflt: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else dflt
    short, sid = opt("--short", ""), opt("--sid", "")
    if cmd in ("--node", "--write", "--nodes", "--state") and not (short and sid):
        sys.stderr.write("Thiếu --short <tiền tố tên trang> và --sid <source id>.\n")
        sys.exit(2)
    if cmd == "--check-formulas":
        sys.exit(1 if check_formulas(path) else 0)
    blocks = load(path)
    tree = classify(blocks)
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    cfg = {"short": short, "sid": sid, "path": path, "sha": sha, "tags": opt("--tags", short)}
    today = opt("--date", datetime.date.today().isoformat())

    if cmd == "--tree":
        for b in blocks:
            a = b.get("addr", "")
            if arg and not (a == arg or a.startswith(arg + ".")):
                continue
            label = "[bảng %d dòng]" % len(b["rows"]) if b["kind"] == "t" else b["plain"][:70]
            print("¶%-4d %-8s %-28s %s%s" % (b["n"], b["role"], a, label, "  !!TRÙNG ¶%d" % b["dup"] if "dup" in b else ""))
        if not arg:
            roles = {}
            for b in blocks:
                roles[b["role"]] = roles.get(b["role"], 0) + 1
            nodes = node_order(blocks, tree)
            print("-- %d khối; %d node (%d Điều, %d node phụ lục); khoản %d, điểm %d, tiết %d, bảng %d, công thức %d" % (
                len(blocks), len(nodes), sum(n.startswith("D") for n in nodes), sum(n.startswith("PL") for n in nodes),
                roles.get("khoan", 0), roles.get("diem", 0), roles.get("tiet", 0), roles.get("table", 0),
                sum(1 for b in blocks if b["kind"] == "p" and "$" in b["text"])))
            issues = audit(blocks, tree)
            print("-- %d điểm nghi vấn về thứ tự/địa chỉ" % len(issues))
            for x in issues:
                print("   " + x)
            head = " ".join(b["plain"] for b in blocks[:4] if b["kind"] == "p") + " ".join(
                c for b in blocks[:1] if b["kind"] == "t" for r in b["rows"] for c in r)
            if re.search(r"Số:\s*(/|…|\.\.\.)|ngày\s+(…|\.\.\.|tháng\s+năm)", head) or re.search(r"Số:\s*<br>\s*/", head):
                print("-- ⚠️ Văn bản chưa điền số hiệu/ngày ban hành: ghi doc_status, không tự điền.")
    elif cmd == "--nodes":
        for n in [HUB] + node_order(blocks, tree):
            print("%s\t%s\t%d khối\t%s" % (n, page_name(n, short), len(node_blocks(blocks, n, tree)), tree[n]["plain"][:60] if n != HUB else "Mục lục"))
    elif cmd == "--refs":
        cnt = {}
        for r in all_refs(blocks, tree):
            st = "EXT" if r["kind"] == "ext" else "DOC" if r["kind"] == "doc" else "SEC" if r["kind"] == "sect" else "OK " if r["targets"] and all(t in tree for t in r["targets"]) else "?? "
            cnt[st] = cnt.get(st, 0) + 1
            if arg and not (r["src"] == arg or r["src"].startswith(arg + ".")):
                continue
            if arg or st == "?? ":
                print("%s %-26s %-50s -> %s" % (st, r["src"], r["cite"][:50], ", ".join(r["targets"])))
        print("-- nội bộ giải được %d, chưa giải được %d, văn bản ngoài %d (+%d nhắc cả văn bản), Mục của Chương %d" % (
            cnt.get("OK ", 0), cnt.get("?? ", 0), cnt.get("EXT", 0), cnt.get("DOC", 0), cnt.get("SEC", 0)))
    elif cmd == "--node":
        print(build_page(blocks, tree, dedupe(all_refs(blocks, tree)), arg, cfg, today), end="")
    elif cmd == "--write":
        refs = dedupe(all_refs(blocks, tree))
        new = same = upd = 0
        for n in [HUB] + node_order(blocks, tree):
            f = os.path.join(arg, page_name(n, short) + ".md")
            old = open(f, encoding="utf-8").read() if os.path.isfile(f) else None
            note, date = NOTE_EMPTY, today
            if old is not None:
                note = split_note(old)[1]
                m = re.search(r"^last_updated:\s*(\S+)", old, re.M)
                keep = build_page(blocks, tree, refs, n, cfg, m.group(1) if m else today, note)
                if keep == old:
                    same += 1
                    continue
                if keep.split("\n" + REF_OUT_HEAD)[0] == old.split("\n" + REF_OUT_HEAD)[0]:
                    date = m.group(1) if m else today  # nguyen van khong doi -> giu last_updated (§13)
            page = build_page(blocks, tree, refs, n, cfg, date, note)
            with open(f, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(page)
            new, upd = new + (old is None), upd + (old is not None)
        print("%d trang mới, %d cập nhật, %d không đổi → %s" % (new, upd, same, arg))
    elif cmd == "--state":
        print("| Xong | Node | Trang | Khối | Số khối | Chú giải |\n|---|---|---|---|---|---|")
        for n in [HUB] + node_order(blocks, tree):
            nb = node_blocks(blocks, n, tree)
            f = os.path.join(arg, page_name(n, short) + ".md") if arg else ""
            page = open(f, encoding="utf-8").read() if f and os.path.isfile(f) else None
            note = "—" if n == HUB else "chưa" if page is None or split_note(page)[1] == NOTE_EMPTY else "có"
            print("| `[%s]` | %s | `%s` | ¶%d–%d | %d | %s |" % (
                "x" if page is not None else " ", n, page_name(n, short), min(b["n"] for b in nb), max(b["n"] for b in nb), len(nb), note))
    elif cmd == "--verify":
        if os.path.isdir(arg):
            name = path.replace("\\", "/").split("/")[-1]
            files = []
            for f in sorted(os.listdir(arg)):
                if f.endswith(".md"):
                    with open(os.path.join(arg, f), encoding="utf-8") as fh:
                        headtxt = fh.read(600)
                    if "type: provision" in headtxt and "source_file: %s" % name in headtxt:
                        files.append(os.path.join(arg, f))
        else:
            files = [arg]
        tot = [0, 0, 0]
        seen_nodes = set()
        refs = dedupe(all_refs(blocks, tree))
        for f in files:
            page = open(f, encoding="utf-8").read()
            k, bad, dead, msgs = verify_page(page, blocks, tree, sha, refs)
            seen_nodes.add(re.search(r"^address:\s*(\S+)", page, re.M).group(1))
            tot = [tot[0] + k, tot[1] + bad, tot[2] + dead]
            for x in msgs:
                print("%s: %s" % (os.path.basename(f), x))
        missing = []
        if os.path.isdir(arg):
            missing = [n for n in [HUB] + node_order(blocks, tree) if n not in seen_nodes]
            for n in missing:
                print("THIẾU TRANG cho node %s" % n)
        orphan = sum(1 for b in blocks if not b.get("addr"))
        print("%d trang, %d/%d khối nguồn đã đối chiếu, %d lệch, %d link chết, %d node thiếu trang, %d khối ngoài mọi node" % (
            len(files), tot[0], len(blocks), tot[1], tot[2], len(missing), orphan))
        sys.exit(1 if (tot[1] or tot[2] or missing or orphan) else 0)
    else:
        sys.stderr.write("Lệnh không hợp lệ: %s\n" % cmd)
        sys.exit(2)


if __name__ == "__main__":
    main()
