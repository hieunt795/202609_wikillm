#!/usr/bin/env python3
"""Read-only audit of a source .md against its original .docx.

Usage:
  python -I audit.py --md <file.md> [--docx <file.docx>] [--wiki 02_wiki --source-id <id>] [-v]

Prints one report with sections A-H. Writes nothing. Every finding is tagged:
  [OK]    checked, nothing to do
  [SỬA]   can be fixed inside the line (candidate for edits.json)
  [XEM]   needs a human/agent look before deciding
  [BÁO]   cannot be fixed without changing line count or meaning: report only
"""
import argparse, collections, difflib, html, os, re, shutil, subprocess, sys, unicodedata, zipfile
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir from sys.path
import headings

sys.stdout.reconfigure(encoding="utf-8")
TAGS = collections.Counter()
_print = print


def print(*args, **kw):  # count finding tags for the closing summary
    for t in re.findall(r"\[(OK|SỬA|THÊM|XEM|BÁO)\]", " ".join(str(x) for x in args)):
        TAGS[t] += 1
    _print(*args, **kw)


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
VN_ALPHA = list("abcdđeghiklmnopqrstuvxy")
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]

UNIT_PATTERNS = [
    ("Chương", r"Chương\s+[IVXLC\d]+"),
    ("Phụ lục", r"(Phụ lục|PHỤ LỤC)(\s+[IVXLC\d]+)?"),
    ("Mục", r"Mục\s+\d+"),
    ("PHẦN", r"(PHẦN|Phần)\s+[A-ZĐ\d]+"),
    ("Điều", r"Điều\s+\d+[a-zđ]?[.]"),
    ("mục La Mã", r"[IVXLC]+[.]\s"),
    ("mục N.N.N.", r"\d+[.]\d+[.]\d+[.]?\s"),
    ("mục N.N.", r"\d+[.]\d+[.]?\s"),
    ("mục N.", r"\d+[.]\s"),
    ("mục a)", r"[a-zđ][)]\s"),
]


def norm(s):
    # NFKC: Word's maths italics (𝑖, 𝐾) and full-width forms compare equal to plain letters
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", s).lower())


def strip_md(s, drop_math=False):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"\[\^[^\]]+\]:?", "", s)  # footnote marks [^1]
    s = re.sub(r"</?[A-Za-z][^<>\n]*>", "", s)  # real tags only: "A2<0 ... >" is text, not a tag
    s = re.sub(r"\{[.#][^}]*\}", "", s)
    if drop_math:
        # an in-sentence symbol such as $E_{OnB}$ is text in the docx (E + subscript run): keep its letters
        s = re.sub(r"(?<![$])[$]([A-Za-z]+)_\{([^$]*?)\}[$](?![$])",
                   lambda m: m.group(1) + re.sub(r"[_{}]", "", m.group(2)), s)
        s = re.sub(r"\${1,2}[^$]*\${1,2}", " ", s)
    return s


def unit_of(title):
    for name, pat in UNIT_PATTERNS:
        if re.match(pat, title):
            return name
    return "khác"


# ---------- docx ----------
def ptext(p):
    out = []
    for el in p.iter():
        if el.tag in (W + "t", M + "t"):
            out.append(el.text or "")
        elif el.tag == W + "tab":
            out.append(" ")
    return "".join(out)


def pinfo_num(p):
    return p.find(W + "pPr/" + W + "numPr") is not None


def pstyle(p):
    st = p.find(W + "pPr/" + W + "pStyle")
    return st.get(W + "val") if st is not None else None


def omml_linear(el):
    t = el.tag
    f = omml_linear
    if t == M + "f":
        return "frac{%s}{%s}" % (f(el.find(M + "num")), f(el.find(M + "den")))
    if t == M + "sSub":
        return "%s_{%s}" % (f(el.find(M + "e")), f(el.find(M + "sub")))
    if t == M + "sSup":
        return "%s^{%s}" % (f(el.find(M + "e")), f(el.find(M + "sup")))
    if t == M + "sSubSup":
        return "%s_{%s}^{%s}" % (f(el.find(M + "e")), f(el.find(M + "sub")), f(el.find(M + "sup")))
    if t == M + "rad":
        return "sqrt{%s}" % f(el.find(M + "e"))
    if t == M + "nary":
        ch = el.find(M + "naryPr/" + M + "chr")
        return "%s[%s][%s]{%s}" % (ch.get(M + "val") if ch is not None else "∫", f(el.find(M + "sub")), f(el.find(M + "sup")), f(el.find(M + "e")))
    if t == M + "d":
        pr = el.find(M + "dPr")
        b, e = "(", ")"
        if pr is not None:
            bb, ee = pr.find(M + "begChr"), pr.find(M + "endChr")
            b = bb.get(M + "val") if bb is not None else b
            e = ee.get(M + "val") if ee is not None else e
        return b + ",".join(f(x) for x in el.findall(M + "e")) + e
    if t in (M + "t", W + "t"):
        return el.text or ""
    if t.endswith("Pr"):
        return ""
    return "".join(f(c) for c in el)


def docx_tables(body):
    res = []
    for tbl in body.iter(W + "tbl"):
        rows = []
        for tr in tbl.findall(W + "tr"):
            cells = []
            gb = tr.find(W + "trPr/" + W + "gridBefore")
            if gb is not None:
                cells += [([], 1, "before")] * int(gb.get(W + "val"))
            for tc in tr.findall(W + "tc"):
                span, vm = 1, None
                gs = tc.find(W + "tcPr/" + W + "gridSpan")
                if gs is not None:
                    span = int(gs.get(W + "val"))
                v = tc.find(W + "tcPr/" + W + "vMerge")
                if v is not None:
                    vm = v.get(W + "val") or "continue"
                paras = [x for x in (ptext(p).strip() for p in tc.findall(W + "p")) if x]
                cells.append((paras, span, vm))
            rows.append(cells)
        res.append(rows)
    return res


# ---------- md ----------
def md_tables(lines):
    out, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


def split_row(l):
    return [c.strip() for c in re.split(r"(?<![\\])[|]", l.strip())[1:-1]]


def find_pandoc():
    p = shutil.which("pandoc")
    if p:
        return p
    cand = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Pandoc", "pandoc.exe")
    return cand if os.path.exists(cand) else None


def head(title):
    print("\n## " + title)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--docx")
    ap.add_argument("--wiki")
    ap.add_argument("--source-id")
    ap.add_argument("-v", action="store_true", help="print every item, not only the first 15")
    a = ap.parse_args()
    cap = 10 ** 6 if a.v else 15

    raw = open(a.md, encoding="utf-8", newline="").read()
    L = raw.split("\n")
    nlines = len(L) - 1 if raw.endswith("\n") else len(L)

    # ---------------- A. file facts
    head("A. Tệp")
    print("md: %d dòng, %d byte, CRLF %d, tab %d, dòng có khoảng trắng thừa cuối %d, NFC %s" % (
        nlines, len(raw.encode("utf-8")), raw.count("\r\n"), raw.count("\t"),
        sum(1 for l in L if l != l.rstrip() and not l.endswith("  ")),
        "OK" if unicodedata.is_normalized("NFC", raw) else "KHÔNG (có ký tự tổ hợp rời)"))
    body = None
    if a.docx:
        z = zipfile.ZipFile(a.docx)
        x = z.read("word/document.xml").decode("utf-8")
        body = ET.fromstring(x).find(W + "body")
        fn = x.count("<w:footnoteReference") + x.count("<w:endnoteReference")
        print("docx: bảng %d, công thức OMML %d, tracked ins/del %d/%d, footnote %d, ảnh %d, run tô sáng %d, comment %d" % (
            x.count("<w:tbl>"), sum(1 for p in body.iter(W + "p") if p.find(".//" + M + "oMath") is not None),
            x.count("<w:ins "), x.count("<w:del "), fn, x.count("<w:drawing"), x.count("<w:highlight"), x.count("<w:commentReference")))
        if x.count("<w:ins ") or x.count("<w:del "):
            print("[XEM] docx còn tracked changes: nội dung đọc được gồm cả phần chèn; quyết định bản nào là gốc trước khi so.")
        if fn:
            print("[XEM] docx có footnote: kiểm md có giữ chú thích không (grep nội dung footnote).")

    # ---------------- B. text parity
    if body is not None:
        head("B. Chữ: docx so với md")
        import bisect

        def mdtext(l):  # read LaTeX as plain text so that formulas typed as text in the docx still match
            return norm(re.sub(r"\[A-Za-z]+", "", strip_md(l).replace("\times", "x")))

        line_c = [mdtext(l) for l in L]
        starts, pos = [], 0
        for c in line_c:
            starts.append(pos)
            pos += len(c)
        mdn = "".join(line_c)
        math_paras = {id(p) for p in body.iter(W + "p") if p.find(".//" + M + "oMath") is not None}
        intbl = {id(p) for t in body.iter(W + "tbl") for p in t.iter(W + "p")}
        paras = []
        for p in body.iter(W + "p"):
            t = ptext(p).strip()
            c = norm(t)
            if len(c) < 8:
                continue
            occ, k = [], mdn.find(c)
            while k >= 0 and len(occ) < 3000:  # short cells ("Đối tượng") recur often; the right one must be among them
                occ.append(k)
                k = mdn.find(c, k + 1)
            paras.append((p, t, c, occ))
        # Longest chain of docx paragraphs that appear in the md in the same order. A paragraph whose
        # text exists only somewhere else (a quoted "Điều 2." further down) is not "present here".
        items = [(i, pos) for i, x in enumerate(paras) for pos in sorted(x[3], reverse=True)]
        tails, tail_pos, back = [], [], [-1] * len(items)
        for n, (i, pos) in enumerate(items):
            j = bisect.bisect_left(tail_pos, pos)
            back[n] = tails[j - 1] if j else -1
            if j == len(tails):
                tails.append(n)
                tail_pos.append(pos)
            else:
                tails[j], tail_pos[j] = n, pos
        chain, n = {}, (tails[-1] if tails else -1)
        while n >= 0:
            chain[items[n][0]] = items[n][1]
            n = back[n]

        def to_line(pos):
            return bisect.bisect_right(starts, pos)

        seq = [[p, t, c, to_line(chain[i]) if i in chain else None, [to_line(o) for o in occ]]
               for i, (p, t, c, occ) in enumerate(paras)]
        total = len(seq)
        found_lines = [s[3] for s in seq]
        missing, differ, formula_miss, reported_md = [], [], 0, set()
        for idx, (p, t, c, ln, occ_lines) in enumerate(seq):
            if ln is not None:
                continue
            if id(p) in math_paras and not occ_lines:
                formula_miss += 1
                continue
            prev = next((x for x in reversed(found_lines[:idx]) if x), 0)
            nxt = next((x for x in found_lines[idx + 1:] if x and x >= prev), min(len(L), prev + 60))
            if any(prev - 20 <= o <= nxt + 20 for o in occ_lines):
                continue  # present, only the local order differs (letterhead, signature block, table cells)
            if occ_lines:
                missing.append((prev, nxt, id(p) in intbl, pinfo_num(p), t, occ_lines[:3]))
                continue
            best, best_j = 0.0, None
            for j in range(max(prev - 1, 0), min(nxt, len(L))):
                lc = line_c[j]
                if len(lc) < 8:
                    continue
                sm = difflib.SequenceMatcher(None, c, lc, autojunk=False)
                if sm.quick_ratio() > best:
                    r = sm.ratio()
                    if r > best:
                        best, best_j = r, j
            if best >= 0.8:
                dw, mw = t.split(), strip_md(L[best_j]).split()
                diffs = ["docx[%s] md[%s]" % (" ".join(dw[i1:i2])[:70], " ".join(mw[j1:j2])[:70])
                         for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, dw, mw, autojunk=False).get_opcodes() if tag != "equal"]
                differ.append((best_j + 1, diffs, t))
                reported_md.add(best_j + 1)
            else:
                missing.append((prev, nxt, id(p) in intbl, pinfo_num(p), t, []))
        print("Đoạn docx (>=8 ký tự) có mặt nguyên văn trong md: %d/%d; THIẾU %d; KHÁC CHỮ %d; công thức chưa khớp dạng chữ %d (so ở mục F)" % (
            total - len(missing) - len(differ) - formula_miss, total, len(missing), len(differ), formula_miss))
        for prev, nxt, tb, num, t, elsewhere in missing[:cap]:
            print("  [THÊM] thiếu trong md, vị trí: sau d.%d, trước d.%d%s%s%s" % (
                prev, nxt, " (trong bảng: xem hàng dựng sẵn ở mục E)" if tb else "",
                " (Word tự đánh số: số/chữ đầu mục không nằm trong chữ, suy từ mục liền kề)" if num else "",
                " (có đoạn trùng chữ ở d.%s nhưng không đúng thứ tự: kiểm đó là đoạn khác trùng lời hay chính đoạn này bị đặt lệch)" % ", ".join(map(str, elsewhere)) if elsewhere else ""))
            print("         docx: %s" % t)
        for ln, diffs, t in differ[:cap]:
            print("  [XEM] khác chữ ở d.%d: %s" % (ln, " ; ".join(diffs[:6]) or "(chỉ khác dấu câu/khoảng trắng)"))
        if not missing and not differ:
            print("[OK] mọi đoạn văn bản của docx đều có trong md")
        if total and len(missing) + len(differ) > 0.05 * total:
            print("[XEM] hơn 5%% đoạn của docx không khớp md (%d/%d): docx và md có thể không cùng một bản, hoặc md được chuyển từ nguồn khác (PDF). "
                  "DỪNG: xác nhận với người dùng docx nào là gốc trước khi chuẩn hóa hay bổ sung; các mục D, E dưới đây kém tin cậy." % (len(missing) + len(differ), total))
        dn = "".join(norm(ptext(p)) for p in body.iter(W + "p"))
        for part in ("word/footnotes.xml", "word/endnotes.xml"):
            if part in z.namelist():
                dn += "".join(norm(ptext(p)) for p in ET.fromstring(z.read(part)).iter(W + "p"))
        extra = []
        for j, l in enumerate(L):
            s = l.strip()
            if not s or s.startswith(("|", "<!--")) or "$" in s or (j + 1) in reported_md:
                continue
            s = re.sub(r"^#{1,6}\s+", "", s)
            s = re.sub(r"^(- )?[*_]{0,3}(\d+(?:[.]\d+)*[.]?|[a-zđ][)]|[(][ivx]+[)]|[a-zđ][.]\d+[)]|[-+])\s+", "", s)
            c = mdtext(s)
            if len(c) >= 12 and c not in dn:
                if l.startswith("#"):  # label and title are separate paragraphs in Word, sometimes not adjacent
                    _, lab, rest = headings.unit_of(s)
                    if lab and mdtext(rest) in dn:
                        continue
                extra.append((j + 1, l.strip()))
        print("Dòng md (ngoài bảng, công thức) không có trong docx: %d %s" % (len(extra), "[OK]" if not extra else ""))
        for ln, s in extra[:cap]:
            print("  [XEM] md có, docx không: d.%d %s" % (ln, s[:140]))
        pandoc = find_pandoc()
        if pandoc:
            r = subprocess.run([pandoc, "-f", "docx", "-t", "markdown", "--wrap=none", a.docx], capture_output=True)
            pm = r.stdout.decode("utf-8", "replace")
            pm = re.sub(r"(?<=\S)[~^](?=\S)", "", pm)  # pandoc writes subscripts as E~OnB~

            def toks(s):
                s = unicodedata.normalize("NFC", strip_md(s, drop_math=True)).lower()
                return collections.Counter(re.findall(r"[^\W_]+", s))
            ta, tb = toks(pm), toks(raw)
            da, db = ta - tb, tb - ta
            print("pandoc: %d từ, md: %d từ (bỏ công thức, không xét thứ tự)" % (sum(ta.values()), sum(tb.values())))
            print("  chỉ có ở docx: %s" % (dict(da.most_common(cap)) or "không"))
            print("  chỉ có ở md:   %s" % (dict(db.most_common(cap)) or "không"))
            if sum(da.values()) + sum(db.values()) > 20:
                print("  [XEM] lệch từ nhiều hơn mức thường gặp (số thứ tự gộp vào công thức, công thức gõ bằng chữ); tìm các từ trên trong hai bản")
        else:
            print("[BÁO] không tìm thấy pandoc: bỏ phép so tập từ (cài: winget install JohnMacFarlane.Pandoc)")

    # ---------------- C. structure inventory
    head("C. Cấu trúc md")
    heads = [(i + 1, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(L) for m in [re.match(r"(#{1,6})\s+(.*)", l)] if m]
    by_unit = collections.defaultdict(collections.Counter)
    for ln, lv, t in heads:
        by_unit[unit_of(re.sub(r"^[*_]+", "", t))][lv] += 1
    print("Heading: %d" % len(heads))
    for u, c in by_unit.items():
        tag = "" if len(c) == 1 else "   [XEM] một loại đơn vị nằm ở %d cấp" % len(c)
        print("  %-12s %s%s" % (u, ", ".join("%s×%d" % ("#" * k, v) for k, v in sorted(c.items())), tag))
    prev = 0
    for ln, lv, t in heads:
        # a jump is expected when the heading already sits at the level its unit type is assigned
        if prev and lv > prev + 1 and headings.LEVELS.get(headings.unit_of(t)[0]) != lv:
            print("  [XEM] d.%d nhảy cấp %d→%d: %s" % (ln, prev, lv, t[:70]))
        prev = lv
    hops = headings.plan(L)
    kinds = collections.Counter(o["kind"] for o in hops)
    if hops:
        print("  [SỬA] --fix-headings sẽ đổi %d dòng: đổi cấp %d, thêm dấu ':' giữa nhãn và tiêu đề %d, nối tiêu đề xuống dòng %d (dời %d dòng)" % (
            len(hops), kinds["level"], kinds["sep"], kinds["join"], kinds["moved"]))
        for o in hops[:cap]:
            print("      d.%d %s" % (o["line"], o["why"]))
            print("          trước: %s" % L[o["line"] - 1][:100])
            print("          sau:   %s" % (o["new"][:100] or "(dòng trống)"))
        if len(hops) > cap:
            print("      … và %d dòng khác (chạy -v để xem hết)" % (len(hops) - cap))
    else:
        print("  [OK] heading đã đúng sơ đồ cấp và đã có tiêu đề trên cùng dòng")
    dieu = [int(re.match(r"Điều\s+(\d+)", t).group(1)) for ln, lv, t in heads if re.match(r"Điều\s+\d+[.]", t)]
    if dieu:
        gaps = [(x, y) for x, y in zip(dieu, dieu[1:]) if y != x + 1]
        print("  Điều: %d (từ %d đến %d)%s" % (len(dieu), dieu[0], dieu[-1], " [OK] liên tục" if not gaps else " [XEM] đứt quãng tại %s" % gaps[:cap]))

    # list items: khoản / điểm / tiết, numbering continuity and nesting
    cnt = collections.Counter()
    stack = [0]
    seq = {}  # indent -> last label within current parent
    khoan_last = None
    issues = []
    in_quote = False
    for i, l in enumerate(L, 1):
        if not l.strip():
            continue
        if l.startswith("#"):
            stack, seq, khoan_last = [0], {}, None
            continue
        if l.lstrip().startswith("|") or l.startswith("<!--"):
            continue
        ind = len(l) - len(l.lstrip())
        body_l = l.strip()
        while stack and stack[-1] > ind:
            stack.pop()
        if not stack or stack[-1] != ind:
            if not (L[i - 2].strip() == "" and any(x.lstrip().startswith("<!--") or x.lstrip().startswith("|") for x in L[max(0, i - 4):i - 1])):
                issues.append("  [XEM] d.%d thụt %d không khớp cấp cha %s: %s" % (i, ind, stack, body_l[:60]))
            stack.append(ind)
        for k in [k for k in seq if k > ind]:
            del seq[k]
        m = re.match(r"(- )?[*_]{0,3}(\d+[.]\d+(?:[.]\d+)*[.]?|\d+[.]|[a-zđ][)]|[(][ivx]+[)]|[a-zđ][.]\d+[)])\s", body_l)
        mk = re.match(r"(- |\d+[.] )", body_l)
        if mk:
            stack.append(ind + len(mk.group(1)))
        if not m:
            if body_l.startswith("- "):
                cnt["gạch đầu dòng khác"] += 1
            elif ind > 0 and not body_l.startswith("$"):
                cnt["đoạn tiếp nối (thụt dòng)"] += 1
            elif ind == 0 and not re.match(r"[*$]", body_l):
                cnt["đoạn thường (cột 0)"] += 1
            continue
        lab = m.group(2)
        if re.fullmatch(r"\d+[.]", lab):
            cnt["khoản N."] += 1
            n = int(lab[:-1])
            last = seq.get(ind)
            if isinstance(last, int) and n != last + 1 and n != 1:
                issues.append("  [XEM] d.%d khoản %d đứng sau khoản %d" % (i, n, last))
            if last is None and n != 1:
                issues.append("  [XEM] d.%d danh sách số bắt đầu từ %d" % (i, n))
            seq[ind] = n
        elif re.fullmatch(r"[a-zđ][)]", lab):
            cnt["điểm a)"] += 1
            c = lab[0]
            last = seq.get(ind)
            if isinstance(last, str) and last in VN_ALPHA and c in VN_ALPHA:
                if VN_ALPHA.index(c) != VN_ALPHA.index(last) + 1 and c != "a":
                    issues.append("  [XEM] d.%d điểm %s) đứng sau điểm %s)" % (i, c, last))
            elif last is None and c != "a":
                issues.append("  [XEM] d.%d danh sách điểm bắt đầu từ %s)" % (i, c))
            seq[ind] = c
        elif lab.startswith("("):
            cnt["tiết (i)"] += 1
            r = lab[1:-1]
            last = seq.get(ind)
            if isinstance(last, str) and last in ROMAN and r in ROMAN:
                if ROMAN.index(r) != ROMAN.index(last) + 1 and r != "i":
                    issues.append("  [XEM] d.%d tiết (%s) đứng sau tiết (%s)" % (i, r, last))
            seq[ind] = r
        else:
            cnt["mục N.N. / a.1) dạng danh sách"] += 1
    for k, v in cnt.most_common():
        print("  %-34s %d" % (k, v))
    print("  Thứ tự và độ thụt: %s" % ("[OK] không lệch" if not issues else "%d chỗ cần xem (văn bản trích dẫn trong ngoặc kép thường là báo động giả)" % len(issues)))
    for s in issues[:cap]:
        print(s)

    # ---------------- D. headings vs docx styles
    if body is not None:
        head("D. Heading: style Word so với md")
        md_joined = [(ln, lv, norm(t)) for ln, lv, t in heads]
        used = set()
        last_ln = 0
        style_to_levels = collections.defaultdict(collections.Counter)
        nd = 0
        for p in body.iter(W + "p"):
            st = pstyle(p)
            if not (st and re.match(r"(Heading|heading|Title)", st)):
                continue
            t = ptext(p).strip()
            n = norm(t)
            if not n:
                continue
            nd += 1
            hit = None
            # walk forward only: repeated titles ("I. Nguyên tắc chung") must pair in document order;
            # "Mục 1" + its title are two docx paragraphs but one md heading, hence >= last_ln
            for ln, lv, k in md_joined:
                if ln >= last_ln and (k == n or (len(n) >= 4 and n in k)) and not (ln == last_ln and k == n and ln in used and False):
                    if k == n and ln in used:
                        continue
                    hit = (ln, lv)
                    break
            if hit:
                last_ln = hit[0]
                used.add(hit[0])
                style_to_levels[st][hit[1]] += 1
            else:
                where = [i + 1 for i, l in enumerate(L) if n in norm(l)][:1]
                print("  [XEM] %s ở docx nhưng không phải heading md (d.%s): %s" % (st, where[0] if where else "?", t[:80]))
        orphan = [(ln, lv, t) for ln, lv, t in heads if ln not in used]
        if nd:
            for ln, lv, t in orphan[:cap]:
                print("  [XEM] heading md d.%d không mang style Heading ở docx: %s %s" % (ln, "#" * lv, t[:70]))
            if len(orphan) > cap:
                print("  … và %d heading md khác (chạy -v để xem hết)" % (len(orphan) - cap))
        print("  Đoạn style Heading ở docx: %d; heading md: %d" % (nd, len(heads)))
        if nd == 0:
            print("  [BÁO] docx không dùng style Heading (tiêu đề chỉ là chữ in đậm): không so được cấp heading với Word; dựa vào mục C")
        for st, c in sorted(style_to_levels.items()):
            print("  %-10s → %s" % (st, ", ".join("%s×%d" % ("#" * k, v) for k, v in sorted(c.items()))))
        print("  (md được phép chia mịn hơn Word; chỉ là lỗi khi một style Word cao hơn lại nằm ở cấp md thấp hơn style thấp hơn)")

    # ---------------- E. tables
    head("E. Bảng")
    mts = md_tables(L)
    starts = [i + 1 for i, l in enumerate(L) if re.match(r"<!--\s*BẢNG\s+\d+\s*[|]\s*bắt đầu", l)]
    ends = [i + 1 for i, l in enumerate(L) if re.match(r"<!--\s*BẢNG\s+\d+\s*[|]\s*kết thúc", l)]
    print("Khối bảng md: %d; chú thích BẢNG bắt đầu/kết thúc: %d/%d %s" % (
        len(mts), len(starts), len(ends), "[OK]" if len(starts) == len(ends) == len(mts) else "[XEM] số chú thích không khớp số bảng"))
    for a0, b0 in mts:
        cols = collections.Counter(len(split_row(L[k])) for k in range(a0, b0))
        if len(cols) > 1:
            print("  [SỬA] bảng d.%d–%d có hàng lệch số cột: %s" % (a0 + 1, b0, dict(cols)))
        if not (b0 - a0 >= 2 and re.fullmatch(r"[|\s:\-]+", L[a0 + 1])):
            print("  [XEM] bảng d.%d–%d thiếu hàng phân cách |---|" % (a0 + 1, b0))
    if body is not None:
        dts = docx_tables(body)

        def row_grid(r):
            g = []
            for paras_, span, vm in r:
                g.append([] if vm == "continue" else paras_)
                g += [[]] * (span - 1)
            return g

        md_rows = []
        for a0, b0 in mts:
            idx = [k for k in range(a0, b0) if not re.fullmatch(r"[|\s:\-]+", L[k])]
            md_rows.append((idx, [norm(strip_md(L[k])) for k in idx]))
        # pair tables by shared rows, not by position: one table with a lost row must not unpair the rest
        used, pairs = set(), []
        for t in dts:
            dkeys = [norm("".join("".join(c) for c in row_grid(r))) for r in t]
            best, bj = 0.0, None
            for j, (idx, keys) in enumerate(md_rows):
                if j in used or not keys:
                    continue
                ks = set(keys)
                score = sum(1 for d in dkeys if d in ks) / max(len(dkeys), 1)
                if score > best:
                    best, bj = score, j
            if bj is None or best < 0.4:
                print("  [XEM] bảng docx %d hàng × %d ô (hàng đầu: %s) không có khối bảng md tương ứng — thường là bảng dàn trang (quốc hiệu, nơi nhận, chữ ký); nếu là bảng nội dung thì md thiếu cả bảng" % (
                    len(t), max(len(r) for r in t), "".join("".join(c[0]) for c in t[0])[:50]))
                continue
            used.add(bj)
            pairs.append((t, dkeys, bj))
        if len(used) < len(mts):
            print("  [XEM] %d khối bảng md không ghép được với bảng docx nào: d.%s" % (
                len(mts) - len(used), ", ".join(str(mts[j][0] + 1) for j in range(len(mts)) if j not in used)[:120]))
        bad = n_missing_rows = 0
        for t, dkeys, bj in pairs:
            idx, keys = md_rows[bj]
            a0, b0 = mts[bj]
            ncol = max(sum(c[1] for c in r) for r in t)
            if len(idx) != len(t):
                print("  [XEM] bảng d.%d–%d: md %d hàng, docx %d hàng" % (a0 + 1, b0, len(idx), len(t)))
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, dkeys, keys, autojunk=False).get_opcodes():
                if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
                    for r, k in zip(t[i1:i2], idx[j1:j2]):
                        grid = row_grid(r)
                        mc = split_row(L[k])
                        probs = []
                        if len(mc) != ncol:
                            probs.append("md %d ô, lưới %d cột" % (len(mc), ncol))
                        for ci in range(min(len(grid), len(mc))):
                            exp = "".join(grid[ci])
                            if norm(exp) != norm(strip_md(mc[ci])):
                                probs.append("cột %d docx[%s] md[%s]" % (ci + 1, exp[:40], mc[ci][:40]))
                            elif grid[ci] and mc[ci].count("<br>") != len(grid[ci]) - 1:
                                probs.append("cột %d: %d <br>, docx có %d đoạn" % (ci + 1, mc[ci].count("<br>"), len(grid[ci])))
                        if probs:
                            bad += 1
                            if bad <= cap:
                                print("  [SỬA] d.%d %s" % (k + 1, "; ".join(probs)))
                    continue
                if i2 > i1:  # rows the docx has and the md lacks: print them ready to insert
                    after = idx[j1 - 1] + 1 if j1 else a0 + 2
                    for r in t[i1:i2]:
                        n_missing_rows += 1
                        cells = ["<br>".join(x.replace("|", "\\|") for x in c) for c in row_grid(r)]
                        print("  [THÊM] hàng bảng thiếu trong md, chèn sau d.%d:" % after)
                        print("         | " + " | ".join(cells) + " |")
                if j2 > j1:
                    for k in idx[j1:j2]:
                        print("  [XEM] hàng md d.%d không có trong bảng docx: %s" % (k + 1, L[k][:100]))
        print("  Bảng ghép được: %d, hàng lệch ô: %d, hàng thiếu trong md: %d %s" % (
            len(pairs), bad, n_missing_rows, "[OK]" if not bad and not n_missing_rows else ""))

    # ---------------- F. formulas
    head("F. Công thức và chỉ số")
    math_lines = [(i + 1, l) for i, l in enumerate(L) if "$" in l and not l.lstrip().startswith("|")]
    sub_lines = [(i + 1, l) for i, l in enumerate(L) if re.search(r"<su[bp]>", l)]
    print("Dòng md có $: %d (khối $$: %d); dòng còn <sub>/<sup>: %d" % (len(math_lines), sum(1 for _, l in math_lines if "$$" in l), len(sub_lines)))
    for ln, l in math_lines:
        if l.count("$") % 2:
            print("  [SỬA] d.%d số dấu $ lẻ" % ln)
        if l.count(r"\left") != l.count(r"\right"):
            print("  [SỬA] d.%d \\left và \\right không cân" % ln)
        inside = "".join(re.findall(r"[$]{1,2}([^$]*)[$]{1,2}", l))  # only what sits between $ signs
        for o, c in ("()", "[]", "{}"):
            if inside.count(o) != inside.count(c):
                print("  [XEM] d.%d ngoặc %s%s không cân trong công thức" % (ln, o, c))
    for ln, l in sub_lines:
        s = strip_md(l).strip()
        standalone = len(s) < 80 and re.search(r"\s=\s", s) and not re.match(r"- ", s)
        print("  [SỬA] d.%d %s: %s" % (ln, "công thức đứng riêng viết bằng chữ → $$…$$" if standalone else "ký hiệu trong câu → $…$", l.strip()[:90]))
    for i, l in enumerate(L, 1):
        s = l.strip()
        if "$" not in s and "<sub>" not in s and len(s) < 90 and re.search(r"[∑√×÷≤≥]|\s=\s.*[x*/]\s", s) and not s.startswith(("|", "#", "-", "<!--")) and not re.match(r"\d+[.]\s", s):
            print("  [XEM] d.%d trông như công thức chưa đánh dấu: %s" % (i, s[:90]))
    if body is not None:
        om = [omml_linear(p) for p in body.iter(W + "p") if p.find(".//" + M + "oMath") is not None]
        print("Công thức OMML ở docx: %d — so tay từng công thức với dòng $ của md (tử số, mẫu số, Σ, ngoặc, chỉ số):" % len(om))
        for o in om:
            print("  docx: " + o.strip()[:200])
        for ln, l in math_lines:
            print("  md d.%d: %s" % (ln, l.strip()[:200]))
        va = []
        for p in body.iter(W + "p"):
            if p.find(".//" + W + "vertAlign") is None:
                continue
            s = ""
            for r in p.iter(W + "r"):
                t = "".join(x.text or "" for x in r.findall(W + "t"))
                v = r.find(W + "rPr/" + W + "vertAlign")
                s += ("<%s>%s</>" % (v.get(W + "val")[:3], t)) if (v is not None and t.strip()) else t
            va += re.findall(r"\S*<\w+>.*?</>\S*", s)
        print("Run chỉ số trên/dưới ở docx: %d; md đã đánh dấu (<sub>, <sup>, _{…}, ^{…}): %d" % (
            len(va), len(re.findall(r"<su[bp]>|_\{|\^\{", raw))))

    # ---------------- G. formatting the md cannot carry
    if body is not None:
        head("G. Định dạng docx mà md không giữ")
        hl = []
        for p in body.iter(W + "p"):
            if p.find(".//" + W + "highlight") is not None:
                hl.append(ptext(p).strip())
        hl = [h for h in hl if h]
        print("Đoạn có chữ tô sáng: %d %s" % (len(hl), "[BÁO] ghi vào báo cáo, không tự thêm vào md" if hl else "[OK]"))
        for h in hl[:cap]:
            where = [i + 1 for i, l in enumerate(L) if norm(h)[:50] and norm(h)[:50] in norm(l)][:1]
            print("  d.%s %s" % (where[0] if where else "?", h[:110]))

    # ---------------- H. citations
    if a.wiki and a.source_id:
        head("H. Chú thích wiki đang dẫn theo số dòng")
        import glob
        n, pages = 0, set()
        for f in glob.glob(os.path.join(a.wiki, "*.md")):
            c = len(re.findall(r"[(]%s,[^()]*?d[.]\d+" % re.escape(a.source_id), open(f, encoding="utf-8").read()))
            if c:
                n += c
                pages.add(f)
        print("%d chú thích trên %d trang → %s" % (n, len(pages), "bắt buộc giữ số dòng" if n else "chưa có trang nào dẫn; vẫn giữ số dòng để bản đồ chunk không lệch"))


main()
_print("")
_print("## Tổng kết")
_print("[THÊM] %d · [SỬA] %d · [XEM] %d · [BÁO] %d · [OK] %d" % (TAGS["THÊM"], TAGS["SỬA"], TAGS["XEM"], TAGS["BÁO"], TAGS["OK"]))
