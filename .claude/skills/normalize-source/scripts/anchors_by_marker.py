#!/usr/bin/env python3
"""Append <!-- @id --> address comments, reading the level from the marker, not the indentation.

Use instead of apply.py --anchors when the source does not encode nesting reliably by indentation
(or after nest_lists.py). Only appends " <!-- @id -->" to line ends; checks that removing the
comments gives back the input exactly, and refuses to write otherwise.

Inside a Điều heading:   khoản "1."  -> Đ5.K1 ; điểm "a)" -> Đ5.K1.a (Đ5.a without khoản)
                         "a.1." -> Đ5.K1.a.1 ; tiết "(i)" -> Đ5.K1.a.i ; "1.1." under khoản 1 -> Đ5.K1.1
Bold "**Điều N.** body" paragraphs before the first Điều heading (the issuing Quyết định / Thông tư
of a consolidated text): <prefix>.ĐN, prefix from --preamble-prefix (default QĐ).
Outside a Điều: "a)" items get the path of the enclosing headings' labels (roman "I." / "I-",
numbers "N." / "Na."), optionally led by a key from --section-key "HEADING PREFIX=KEY".
Duplicated ids get ~2, ~3 and are listed: each one is a structure the md does not make clear.

Usage:
  python -I anchors_by_marker.py --src <in.md> --out <out.md> [--dieu-word Điền]
         [--preamble-prefix QĐ] [--section-key "THUYẾT MINH BÁO CÁO TÀI CHÍNH CHỌN LỌC=B05a" ...]
"""
import argparse
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
FN = r"(?:\[\^[^\]\s]+\])*"
VN = "a-zđ"


def fail(msg):
    print("LỖI: " + msg)
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dieu-word", action="append", default=["Điều"])
    ap.add_argument("--preamble-prefix", default="QĐ")
    ap.add_argument("--section-key", action="append", default=[],
                    help="'HEADING PREFIX=KEY': a heading starting with the prefix opens section KEY (first match wins)")
    a = ap.parse_args()
    out_abs = os.path.abspath(a.out).replace("\\", "/")
    if "/01_sources/" in out_abs + "/" or os.path.abspath(a.out) == os.path.abspath(a.src):
        fail("--out không được nằm trong 01_sources/ và không được trùng --src.")
    words = "|".join(map(re.escape, a.dieu_word))
    dieu_h = re.compile(r"(#{1,6})\s+[*_“\"]*(?:%s)\s+(\d+[%s]?)[.]" % (words, VN))
    dieu_bold = re.compile(r"\*\*[“\"]?(?:%s)\s+(\d+[%s]?)[.]" % (words, VN))
    keys = [tuple(x.split("=", 1)) for x in a.section_key]

    src = open(a.src, encoding="utf-8").read()
    L = src.split("\n")
    ids, seen, dups = {}, {}, []

    def emit(i, aid):
        seen[aid] = seen.get(aid, 0) + 1
        if seen[aid] > 1:
            dups.append((i + 1, aid))
            aid += "~%d" % seen[aid]
        ids[i] = aid

    seen_dieu_heading = False
    dieu = k = d = sub = None
    hpath = []  # (level, label) outside a Điều
    section, section_lv = None, 0
    in_table = False
    for i, l in enumerate(L):
        if l.startswith("<table>"):
            in_table = True
        if in_table:
            if l.startswith("</table>"):
                in_table = False
            continue
        if re.match(r"\[\^[^\]]+\]:", l):
            break
        if not l.strip() or l.startswith("|"):
            continue
        h = re.match(r"(#{1,6})\s+(.*)", l)
        if h:
            lv, t = len(h.group(1)), h.group(2)
            m = dieu_h.match(l)
            if m:
                seen_dieu_heading = True
                dieu, k, d, sub = m.group(2), None, None, None
                continue
            dieu = None
            for pre, key in keys:
                if t.startswith(pre):
                    section, section_lv, hpath = key, lv, []
                    break
            else:
                if section is not None and lv <= section_lv:
                    section = None  # a sibling or higher heading closes the section
            lab = None
            g = re.match(r"([IVXLC]+)[.\-–]\s", t) or re.match(r"(\d+[a-z]?)[.]\s", t)
            if g:
                lab = g.group(1)
            while hpath and hpath[-1][0] >= lv:
                hpath.pop()
            hpath.append((lv, lab))
            d = None
            continue
        s = l.lstrip(" ")
        if s.startswith("- "):
            s = s[2:]
        if not seen_dieu_heading and dieu is None:
            m = dieu_bold.match(s)
            if m:
                emit(i, "%s.Đ%s" % (a.preamble_prefix, m.group(1)))
            continue
        if dieu is not None:
            m = re.match(r"(\d+)\." + FN + r"(?:\s|$)", s)
            if m:
                k, d, sub = m.group(1), None, None
                emit(i, "Đ%s.K%s" % (dieu, k))
                continue
            m = re.match(r"(\d+)\.(\d+)\.?" + FN + r"\s", s)
            if m and k == m.group(1):
                d = sub = None
                emit(i, "Đ%s.K%s.%s" % (dieu, k, m.group(2)))
                continue
            kk = ".K" + k if k else ""
            m = re.match(r"([%s])\)" % VN + FN + r"(?:\s|$)", s)
            if m:
                d, sub = m.group(1), None
                emit(i, "Đ%s%s.%s" % (dieu, kk, d))
                continue
            m = re.match(r"([%s])\.(\d+)[.)]?" % VN + FN + r"\s", s)
            if m:
                d, sub = m.group(1), m.group(2)
                emit(i, "Đ%s%s.%s.%s" % (dieu, kk, d, sub))
                continue
            m = re.match(r"\(([ivx]+)\)" + FN + r"\s", s)
            if m:
                emit(i, "Đ%s%s%s%s.%s" % (dieu, kk, "." + d if d else "", "." + sub if sub else "", m.group(1)))
            continue
        m = re.match(r"([%s])\)" % VN + FN + r"\s", s)
        if m:
            parts = ([section] if section else []) + [x for _, x in hpath if x] + [m.group(1)]
            emit(i, ".".join(parts))

    N = list(L)
    for i, aid in ids.items():
        N[i] = N[i] + " <!-- @%s -->" % aid
    back = [re.sub(r" <!-- @[^>]* -->$", "", x) for x in N]
    if back != L:
        fail("bỏ chú thích địa chỉ không ra lại đúng file vào")
    open(a.out, "w", encoding="utf-8", newline="\n").write("\n".join(N))
    print("ĐÃ GHI %s | địa chỉ: %d | trùng phải thêm hậu tố ~n: %d" % (a.out, len(ids), len(dups)))
    for n, aid in dups[:30]:
        print("  [XEM] trùng d.%d %s" % (n, aid))


main()
