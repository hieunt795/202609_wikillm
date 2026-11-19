#!/usr/bin/env python3
"""Write a normalized COPY of a source .md. Never writes inside 01_sources/.

Usage:
  python -I apply.py --src <source.md> --out <copy.md> [--edits edits.json]
                     [--fix-headings] [--sub-to-math] [--nfc] [--anchors] [--changes <changes.md>]
                     [--wiki 02_wiki --source-id <id>]

edits.json: [{"line": 1624, "old": "###### 3.2.1.", "new": "**3.2.1.", "why": "..."}, ...]
  "old" must occur exactly once in that line of the SOURCE; "new" replaces it.

Guarantees, checked before anything is written (any failure -> exit 1, no file):
  1. same number of lines, LF only
  2. line N of the copy carries the same letters and digits as line N of the source
     (HTML tags, HTML comments and LaTeX commands are ignored; \\times == x, \\sum == ∑)
  3. leading indentation of every changed line is unchanged
  4. only lines named by an edit or by a flag differ
Content repair (needs --docx; every piece of text added must be found in the docx):
  {"line": 2758, "old": "cập nhật", "new": "cập nhập", "why": "...", "content": true}   fix letters on a line
  {"after": 412, "insert": ["", "3. Văn bản của khoản bị thiếu;"], "why": "..."}       insert lines after source line 412
Inserting lines changes the line count; --linemap writes the source-line -> copy-line table.

--fix-headings may pull a title up into the heading line above it (the title's own line becomes
empty). For those lines guarantee 2 is checked on the whole file instead: the letters and digits
of the copy, read top to bottom, are exactly those of the source.
"""
import argparse, glob, json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir from sys.path
import headings

sys.stdout.reconfigure(encoding="utf-8")
VN = "a-zđ"


def canon(s):
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"</?[A-Za-z][^<>\n]*>", "", s)  # real tags only: "A2<0 ... >" is text, not a tag
    s = s.replace("\\times", "x").replace("×", "x").replace("∑", "").replace("\\%", "%")
    s = re.sub(r"\\[A-Za-z]+", "", s)
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s).lower())


def quotes(s):
    """Quotes and brackets of the text (outside comments, tags, footnote refs and LaTeX \\left/\\right)."""
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"</?[A-Za-z][^<>\n]*>", "", s)
    s = re.sub(r"\[\^[^\]\s]+\]", "", s)
    s = re.sub(r"\\(?:left|right)\s*[(\[\])]", "", s)
    s = re.sub(r"\\[\[\]()]", "", s)  # escaped brackets are markdown escapes of the same character
    return "".join(c for c in s if c in "“”‘’\"'()")


def fail(msg):
    print("LỖI: " + msg)
    sys.exit(1)


def anchors(lines):
    """Append <!-- @id --> to every khoản / điểm / tiết / numbered item. Returns {line_no: id}."""
    hpath, lpath, out, seen = [], [], {}, {}
    in_table = False
    for i, l in enumerate(lines):
        s = l.strip()
        if not s or s.startswith("|") or s.startswith("<!--") or s.startswith("$$"):
            continue
        m = re.match(r"(#{1,6})\s+(.*)", l)
        if m:
            lv, t = len(m.group(1)), re.sub(r"^[*_“\"]+", "", m.group(2))
            lab = None
            for pat, fn in (
                (r"Điều\s+(\d+[%s]?)[.]" % VN, lambda g: "Đ" + g.group(1)),
                (r"(?:Phụ lục|PHỤ LỤC)\s*([IVXLC\d]*)", lambda g: "PL" + (g.group(1) or "")),
                (r"(?:PHẦN|Phần)\s+([A-ZĐ\d]+)", lambda g: g.group(1)),
                (r"([IVXLC]+)[.]\s", lambda g: g.group(1)),
                (r"(\d+(?:[.]\d+)*)[.]?\s", lambda g: g.group(1)),
            ):
                g = re.match(pat, t)
                if g:
                    lab = fn(g)
                    break
            while hpath and hpath[-1][0] >= lv:
                hpath.pop()
            hpath.append((lv, lab))
            lpath = []
            continue
        ind = len(l) - len(l.lstrip())
        b = re.fullmatch(r"[*]{2}(\d+(?:[.]\d+)+)[.]?\s.*[*]{2}", s) if ind == 0 else None
        if b:  # bold line standing in for a 7th heading level (N.N.N.)
            while hpath and hpath[-1][0] >= 7:
                hpath.pop()
            hpath.append((7, b.group(1)))
            lpath = []
            continue
        g = re.match(r"(- )?[*_]{0,3}(\d+(?:[.]\d+)+[.]?|\d+[.]|[%s][)]|[(][ivx]+[)]|[%s][.]\d+[)])\s" % (VN, VN), s)
        while lpath and lpath[-1][0] >= ind:
            lpath.pop()
        if not g:
            if s.startswith("- "):
                lpath.append((ind, None))
            continue
        raw = g.group(2)
        hl = [x for _, x in hpath if x]
        if re.fullmatch(r"\d+[.]", raw):
            lab = ("K" if (hl and hl[-1].startswith("Đ") and ind == 0) else "") + raw[:-1]
        else:
            lab = raw.strip("().")
        lpath.append((ind, lab))
        parts = hl + [x for _, x in lpath if x]
        # drop a numeric parent repeated by its child: 2 › 2.1 -> 2.1 ; a › a.1 -> a.1
        keep = [p for k, p in enumerate(parts) if not (k + 1 < len(parts) and parts[k + 1].startswith(p + "."))]
        aid = ".".join(keep)
        seen[aid] = seen.get(aid, 0) + 1
        if seen[aid] > 1:
            aid += "~%d" % seen[aid]
        out[i + 1] = aid
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--edits")
    ap.add_argument("--fix-headings", action="store_true", help="one unit type -> one level; join label and title: 'Mục 3: TITLE'")
    ap.add_argument("--sub-to-math", action="store_true", help="X<sub>y</sub> -> $X_{y}$ on lines not covered by an edit")
    ap.add_argument("--nfc", action="store_true", help="normalize Unicode to NFC")
    ap.add_argument("--anchors", action="store_true", help="append <!-- @Đ16.K3.b --> address comments")
    ap.add_argument("--changes", help="write the change table (markdown) to this file")
    ap.add_argument("--docx", help="original .docx; required when edits.json inserts or corrects content")
    ap.add_argument("--linemap", help="write source-line -> copy-line map (TSV) when lines were inserted")
    ap.add_argument("--wiki")
    ap.add_argument("--source-id")
    a = ap.parse_args()

    out_abs = os.path.abspath(a.out).replace("\\", "/")
    if "/01_sources/" in out_abs + "/" or os.path.abspath(a.out) == os.path.abspath(a.src):
        fail("--out không được nằm trong 01_sources/ và không được trùng --src (nguồn bất biến).")

    raw = open(a.src, encoding="utf-8", newline="").read()
    crlf = "\r\n" in raw
    L = raw.replace("\r\n", "\n").split("\n")
    N = list(L)
    why = {}

    def note(n, w):
        why.setdefault(n, [])
        if w not in why[n]:
            why[n].append(w)

    cedit = set()   # source lines whose letters/digits are corrected from the docx
    inserts = {}    # source line n -> lines to insert after it (content missing from the md)
    docx_canon = None
    if a.docx:
        import zipfile
        import xml.etree.ElementTree as ET
        Wn = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        Mn = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
        body = ET.fromstring(zipfile.ZipFile(a.docx).read("word/document.xml")).find(Wn + "body")
        docx_canon = "".join(canon("".join(t.text or "" for t in p.iter() if t.tag in (Wn + "t", Mn + "t")))
                             for p in body.iter(Wn + "p"))

    def in_docx(line, where):
        """Every piece of text written into the copy must exist in the docx: nothing is composed from memory."""
        unchecked = 0
        for piece in re.split(r"[|]|<br\s*/?>", line):
            p = re.sub(r"<!--.*?-->", "", piece).strip()
            p = re.sub(r"^#{1,6}\s+", "", p)
            p = re.sub(r"^(- )?[*_]{0,3}(\d+(?:[.]\d+)*[.]?|[%s][)]|[(][ivx]+[)]|[%s][.]\d+[)])\s+" % (VN, VN), "", p)
            p = re.sub(r"^(?:Chương|CHƯƠNG|Mục|MỤC|Phụ lục|PHỤ LỤC)\s+[IVXLC\d]+\s*:\s*", "", p)
            c = canon(p)
            if len(c) < 4 or re.fullmatch(r"[\s:\-|]*", p):
                continue
            if "$" in p:
                unchecked += 1
                continue
            if c not in docx_canon:
                fail("%s: đoạn sau không có trong docx, không được thêm vào bản sao: %r" % (where, p[:120]))
        return unchecked

    math_unchecked = 0
    if a.edits:
        all_edits = json.load(open(a.edits, encoding="utf-8"))
        if any(("insert" in e or e.get("content")) for e in all_edits) and docx_canon is None:
            fail("edits.json có mục chèn hoặc sửa nội dung: phải truyền --docx để kiểm từng đoạn với bản gốc.")
        for e in all_edits:
            if "insert" in e:
                n = e["after"]
                if not (0 <= n <= len(L)):
                    fail("insert sau dòng %d: ngoài phạm vi file" % n)
                for k, ln in enumerate(e["insert"]):
                    if "\n" in ln:
                        fail("insert sau dòng %d: mỗi phần tử của 'insert' là một dòng, không chứa xuống dòng" % n)
                    math_unchecked += in_docx(ln, "insert sau d.%d, dòng thứ %d" % (n, k + 1))
                inserts.setdefault(n, []).append((e["insert"], e.get("why", "bổ sung nội dung thiếu từ docx")))
                continue
            n, old, new = e["line"], e["old"], e["new"]
            if e.get("content"):
                cedit.add(n)
            if not (1 <= n <= len(L)):
                fail("edit dòng %d: ngoài phạm vi file" % n)
            if L[n - 1].count(old) != 1:
                fail("edit dòng %d: 'old' xuất hiện %d lần trong dòng nguồn (cần đúng 1): %r" % (n, L[n - 1].count(old), old))
            if old not in N[n - 1]:
                fail("edit dòng %d: 'old' đã bị một edit trước đó thay mất: %r" % (n, old))
            if "\n" in new:
                fail("edit dòng %d: 'new' chứa xuống dòng (phá ràng buộc giữ số dòng)" % n)
            N[n - 1] = N[n - 1].replace(old, new)
            note(n, e.get("why", "edit"))

    joined = set()  # lines whose text moved between lines (label + title join)
    if a.fix_headings:
        # a line edited by hand in edits.json is final: --fix-headings neither rewrites nor moves it
        hand = {e["line"] for e in (all_edits if a.edits else []) if "line" in e}
        ops = headings.plan(N, skip=hand)
        for o in ops:
            N[o["line"] - 1] = o["new"]
            note(o["line"], o["why"])
            if o["kind"] in ("join", "moved"):
                joined.add(o["line"])
        kinds = [o["kind"] for o in ops]
        print("Heading: đổi cấp/viết lại %d dòng, nối tiêu đề %d chỗ (dời %d dòng tiêu đề lên)" % (
            len([k for k in kinds if k != "moved"]), kinds.count("join"), kinds.count("moved")))

    if a.sub_to_math:
        for i, line in enumerate(N):
            if "<sub>" in line or "<sup>" in line:
                new = re.sub(r"([A-Za-zĐđ]+)<sub>([^<]+)</sub>", r"$\1_{\2}$", line)
                new = re.sub(r"([A-Za-zĐđ0-9]+)<sup>([^<]+)</sup>", r"$\1^{\2}$", new)
                if new != line:
                    N[i] = new
                    note(i + 1, "ký hiệu <sub>/<sup> → $…$")

    if a.nfc:
        for i, line in enumerate(N):
            new = unicodedata.normalize("NFC", line)
            if new != line:
                N[i] = new
                note(i + 1, "Unicode → NFC")

    for n in sorted(cedit):
        math_unchecked += in_docx(N[n - 1], "sửa nội dung d.%d" % n)

    # ---------- guarantees (on the lines that come from the source)
    if len(N) != len(L):
        fail("số dòng đổi: %d → %d" % (len(L), len(N)))
    changed = [i + 1 for i in range(len(L)) if L[i] != N[i]]
    unexpected = [n for n in changed if n not in why]
    if unexpected:
        fail("dòng đổi ngoài danh sách: %s" % unexpected[:20])
    bad = [i + 1 for i in range(len(L)) if (i + 1) not in joined and (i + 1) not in cedit and canon(L[i]) != canon(N[i])]
    if "".join(canon(x) for k, x in enumerate(L) if k + 1 not in cedit) != "".join(canon(x) for k, x in enumerate(N) if k + 1 not in cedit):
        fail("chữ-số của toàn văn (đọc từ trên xuống) khác nguồn ở ngoài các dòng sửa nội dung; không ghi.")
    # quotes and brackets are text, not markdown: canon() ignores them, so check them separately
    qbad = [i + 1 for i in range(len(L)) if (i + 1) not in joined and (i + 1) not in cedit and quotes(L[i]) != quotes(N[i])]
    if "".join(quotes(x) for k, x in enumerate(L) if k + 1 not in cedit) != "".join(quotes(x) for k, x in enumerate(N) if k + 1 not in cedit):
        qbad = qbad or ["toàn văn"]
    if qbad:
        for n in [x for x in qbad if isinstance(x, int)][:10]:
            print("  d.%d\n    nguồn: %s\n    mới:   %s" % (n, L[n - 1].strip()[:160], N[n - 1].strip()[:160]))
        fail("dấu ngoặc kép hoặc ngoặc đơn/vuông bị thêm hoặc mất ở %s. Chuẩn hóa chỉ được đổi ký hiệu markdown." % qbad[:10])
    if bad:
        for n in bad[:10]:
            print("  d.%d\n    nguồn: %s\n    mới:   %s" % (n, L[n - 1].strip()[:160], N[n - 1].strip()[:160]))
        fail("%d dòng đổi chữ hoặc số so với nguồn (xem trên). Chuẩn hóa chỉ được đổi ký hiệu markdown." % len(bad))
    for n in changed:
        if n in joined:
            continue
        if len(L[n - 1]) - len(L[n - 1].lstrip()) != len(N[n - 1]) - len(N[n - 1].lstrip()):
            fail("d.%d đổi độ thụt đầu dòng (sẽ đổi cấp lồng danh sách)" % n)

    # ---------- insert missing content, keeping a source-line -> copy-line map
    OUT, linemap, ins_rows = [], {}, []
    for blk, w in inserts.get(0, []):
        ins_rows.append((0, len(OUT) + 1, blk, w))
        OUT += blk
    for i in range(len(N)):
        OUT.append(N[i])
        linemap[i + 1] = len(OUT)
        for blk, w in inserts.get(i + 1, []):
            ins_rows.append((i + 1, len(OUT) + 1, blk, w))
            OUT += blk
    n_ins = sum(len(r[2]) for r in ins_rows)

    ids = {}
    if a.anchors:
        ids = anchors(OUT)
        for n, aid in ids.items():
            OUT[n - 1] = OUT[n - 1].rstrip() + " <!-- @%s -->" % aid + ("  " if OUT[n - 1].endswith("  ") else "")
        dups = sum(1 for v in ids.values() if "~" in v)
        print("Địa chỉ đã gắn: %d dòng (trùng phải thêm hậu tố ~n: %d)" % (len(ids), dups))

    text = "\n".join(OUT)
    for n in changed:
        ln = N[n - 1]
        if re.sub(r"<!--.*?-->", "", ln).count("$") % 2:
            fail("d.%d số dấu $ lẻ sau khi sửa" % n)
        if ln.count("\\left") != ln.count("\\right"):
            fail("d.%d \\left và \\right không cân sau khi sửa" % n)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    nl = len(L) - 1 if raw.endswith("\n") else len(L)
    content_changed = [n for n in changed if n in why]
    print("ĐÃ GHI %s" % a.out)
    print("Dòng: nguồn %d, bản mới %d | CRLF nguồn: %s → bản mới LF | dòng đổi ký hiệu markdown: %d | dòng sửa nội dung theo docx: %d | dòng chèn thêm: %d (tại %d chỗ) | dòng chỉ thêm địa chỉ: %d" % (
        nl, nl + n_ins, "có" if crlf else "không", len([n for n in content_changed if n not in cedit]), len(cedit), n_ins, len(ins_rows),
        len(ids) - len([n for n in content_changed if linemap[n] in ids])))
    if math_unchecked:
        print("LƯU Ý: %d đoạn có công thức ($) trong phần chèn/sửa nội dung không kiểm tự động được với docx; so tay với OMML ở mục F của audit." % math_unchecked)
    if n_ins:
        print("SỐ DÒNG ĐÃ ĐỔI: dòng N của bản sao không còn ứng với dòng N của nguồn kể từ d.%d. Dùng bản đồ dòng để quy đổi." % (ins_rows[0][0] + 1))
        if a.linemap:
            with open(a.linemap, "w", encoding="utf-8", newline="") as f:
                f.write("dong_nguon\tdong_ban_sao\n")
                for k in range(1, nl + 1):
                    f.write("%d\t%d\n" % (k, linemap[k]))
                for after, at, blk, w in ins_rows:
                    f.write("# chen sau dong nguon %d: ban sao d.%d-%d\n" % (after, at, at + len(blk) - 1))
            print("Bản đồ dòng: %s" % a.linemap)
        else:
            print("  (truyền --linemap <file.tsv> để ghi bản đồ dòng nguồn → bản sao)")

    esc = lambda s: s.strip().replace("|", "\\|")
    rows = ["| Dòng nguồn | Lý do | Trước | Sau |", "|---|---|---|---|"]
    for n in content_changed:
        before, after = esc(L[n - 1]), esc(N[n - 1])
        if len(before) > 150 and n not in cedit:
            before, after = before[:150] + "…", after[:150] + "…"
        rows.append("| d.%d | %s%s | `%s` | `%s` |" % (n, "SỬA NỘI DUNG theo docx: " if n in cedit else "", "; ".join(why[n]), before, after or "(dòng trống)"))
    for after, at, blk, w in ins_rows:
        for k, ln in enumerate(blk):
            if ln.strip():
                rows.append("| sau d.%d (bản sao d.%d) | CHÈN: %s | (không có) | `%s` |" % (after, at + k, w, esc(ln)))
    if a.changes:
        with open(a.changes, "w", encoding="utf-8", newline="") as f:
            f.write("\n".join(rows) + "\n")
        print("Bảng thay đổi: %s" % a.changes)
    else:
        print("\n".join(rows))

    if a.wiki and a.source_id:
        cites = []
        for fpath in glob.glob(os.path.join(a.wiki, "*.md")):
            for m in re.finditer(r"[(]%s,[^()]*?d[.](\d+)(?:[–-](\d+))?[)]" % re.escape(a.source_id), open(fpath, encoding="utf-8").read()):
                cites.append((os.path.basename(fpath), int(m.group(1)), int(m.group(2) or m.group(1))))
        cs = set(content_changed)
        hit = sorted({(f, x, y) for f, x, y in cites if any(x <= n <= y for n in cs)})
        print("Chú thích wiki của %s: %d; dải dòng có chứa dòng đã đổi: %d" % (a.source_id, len(cites), len(hit)))
        for f, x, y in hit[:20]:
            print("  %s d.%d–%d" % (f, x, y))
        if ins_rows or cedit:
            pts = [r[0] for r in ins_rows]
            near = sorted({(f, x, y) for f, x, y in cites if any(x - 1 <= p <= y for p in pts) or any(x <= n <= y for n in cedit)})
            print("Chú thích wiki dẫn đúng vùng nguồn bị thiếu hoặc sai nội dung (claim trên trang cần /review-node): %d" % len(near))
            for f, x, y in near[:20]:
                print("  %s d.%d–%d" % (f, x, y))


main()
