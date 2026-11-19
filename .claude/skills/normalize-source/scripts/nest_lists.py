#!/usr/bin/env python3
"""Give khoản / điểm / tiết their nesting level by indentation, on a COPY written by apply.py.

For sources whose điểm a), b) sit at column 0 like the khoản (common in .docx converted from HTML).
apply.py refuses every indentation change, so this runs after it, on its output, and checks its own
guarantees before writing (any failure -> exit 1, no file):
  1. same number of lines
  2. line N keeps the letters and digits of line N of the input
  3. only leading spaces, a list marker "- " and the escape of a leading "\\-" change

Inside a Điều (a heading whose label is "Điều N."):
  khoản   "1." / "1.[^7]"            col 0; "1.[^7] x" -> "1. [^7] x" so it is a list item
  điểm    "a)"                       "- a)" indented by the width of the khoản marker ("1. " = 3);
                                     col 0 when the Điều has no khoản
  "a.1." / "a.1)" / "(i)"            "- " at the content column of the điểm
  "\\- …" (dash written as text)     "- …" at the content column of the deepest khoản/điểm/tiết
  other paragraph after an item      indented to the content column of the deepest khoản/điểm/tiết
                                     (a continuation paragraph), except lines given in --keep-col0
Outside a Điều only "a)" lines at col 0 become "- a)" (a list under a heading).
A heading, a bold line, a table, a footnote definition or an indented line ends the current item;
indented lines are left as they are, so the script can run twice.

Usage:
  python -I nest_lists.py --src <apply output.md> --out <copy.md> [--keep-col0 170,233] [--log <tsv>]
"""
import argparse
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
FN = r"(?:\[\^[^\]\s]+\])*"
VN = "a-zđ"


def canon(s):
    s = re.sub(r"<!--.*?-->", "", s)
    s = re.sub(r"</?[A-Za-z][^<>\n]*>", "", s)
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s).lower())


def fail(msg):
    print("LỖI: " + msg)
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--keep-col0", default="", help="line numbers of paragraphs that close a Điều (not continuation)")
    ap.add_argument("--dieu-word", action="append", default=["Điều"],
                    help="extra word read as 'Điều' in headings (a typo of the source, e.g. Điền)")
    ap.add_argument("--log", help="write one TSV row per changed line")
    a = ap.parse_args()
    out_abs = os.path.abspath(a.out).replace("\\", "/")
    if "/01_sources/" in out_abs + "/" or os.path.abspath(a.out) == os.path.abspath(a.src):
        fail("--out không được nằm trong 01_sources/ và không được trùng --src.")
    keep = {int(x) for x in a.keep_col0.split(",") if x.strip()}
    dieu_re = re.compile(r"#{1,6}\s+[*_“\"]*(?:%s)\s+\d+[%s]?[.]" % ("|".join(map(re.escape, a.dieu_word)), VN))

    src = open(a.src, encoding="utf-8").read()
    L = src.split("\n")
    N = list(L)
    log = []

    def setl(i, new, why):
        if N[i] != new:
            N[i] = new
            log.append((i + 1, why, L[i], new))

    in_dieu = False
    k_w = d_w = sub_w = None
    active = in_table = False
    for i, l in enumerate(L):
        if l.startswith("<table>"):
            in_table = True
        if in_table:
            if l.startswith("</table>"):
                in_table = False
            continue
        if re.match(r"\[\^[^\]]+\]:", l):
            break  # footnote definitions: end of the body
        if l.startswith("#"):
            in_dieu = bool(dieu_re.match(l))
            k_w = d_w = sub_w = None
            active = False
            continue
        if l.startswith("**") or l.startswith("|"):
            k_w = d_w = sub_w = None
            active = False
            continue
        if not l.strip():
            continue
        if l[0] == " ":
            continue  # already indented: leave it
        if not in_dieu:
            if re.match(r"[%s]\)" % VN + FN + r"\s", l):
                setl(i, "- " + l, "điểm dưới heading → mục danh sách")
            continue
        m = re.match(r"(\d+)\.(" + FN + r")(\s|$)", l)
        if m:
            rest = l[m.end():].lstrip(" ")
            new = m.group(1) + ". " + (m.group(2) + " " if m.group(2) else "") + rest
            setl(i, new.rstrip(" "), "khoản")
            k_w, d_w, sub_w, active = len(m.group(1)) + 2, None, None, True
            continue
        base = k_w or 0
        if re.match(r"[%s]\)" % VN + FN + r"(\s|$)", l):
            setl(i, " " * base + "- " + l, "điểm → dưới khoản" if k_w else "điểm (Điều không chia khoản)")
            d_w, sub_w, active = base + 2, None, True
            continue
        if re.match(r"(?:[%s]\.\d+[.)]?|\([ivx]+\))" % VN + FN + r"\s", l):
            ind = d_w if d_w is not None else base
            setl(i, " " * ind + "- " + l, "điểm con / tiết → dưới điểm")
            sub_w, active = ind + 2, True
            continue
        deepest = sub_w if sub_w is not None else (d_w if d_w is not None else k_w)
        if l.startswith("\\- "):
            setl(i, " " * (deepest or 0) + "- " + l[3:], "gạch đầu dòng → mục danh sách dưới mục chứa nó")
            continue
        if (i + 1) in keep:
            k_w = d_w = sub_w = None
            active = False
            continue
        if active and deepest:
            setl(i, " " * deepest + l, "đoạn tiếp nối → thụt theo mục chứa nó")

    # ---------- guarantees
    if len(N) != len(L):
        fail("số dòng đổi")
    for i in range(len(L)):
        if N[i] == L[i]:
            continue
        if canon(N[i]) != canon(L[i]):
            fail("d.%d đổi chữ hoặc số" % (i + 1))
        a_, b_ = L[i].lstrip(" "), N[i].lstrip(" ")
        b_ = b_[2:] if b_.startswith("- ") and not a_.startswith("- ") else b_
        a_ = a_[3:] if a_.startswith("\\- ") else a_
        if re.sub(r"\s+", "", a_) != re.sub(r"\s+", "", b_):
            fail("d.%d đổi ngoài thụt đầu dòng và dấu '- ': %r -> %r" % (i + 1, L[i][:80], N[i][:80]))
    open(a.out, "w", encoding="utf-8", newline="\n").write("\n".join(N))
    if a.log:
        with open(a.log, "w", encoding="utf-8") as f:
            f.write("dòng\tlý do\ttrước\tsau\n")
            for n, w, x, y in log:
                f.write("%d\t%s\t%s\t%s\n" % (n, w, x, y))
    from collections import Counter
    print("ĐÃ GHI %s | dòng đổi: %d" % (a.out, len(log)))
    for w, c in Counter(w for _, w, _, _ in log).most_common():
        print("  %4d  %s" % (c, w))


main()
