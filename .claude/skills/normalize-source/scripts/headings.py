"""Heading plan for Vietnamese legal texts: one unit type -> one level, label and title on one line.

plan(lines) -> list of ops, each a dict:
  {"line": n, "new": "<full new line>", "why": "...", "kind": "level" | "sep" | "join" | "moved"}
"moved" ops blank a line whose text was pulled up into the heading above it.
Used by audit.py (to list what would change) and apply.py --fix-headings (to do it).
"""
import re

# level 7 means "no heading level left": written as a bold line
LEVELS = {
    "Chương": 2, "Phụ lục": 2,
    "Mục": 3, "PHẦN": 3, "mục A.": 3,
    "Điều": 4, "mục La Mã": 4,
    "mục N.": 5, "mục N.N.": 6, "mục N.N.N.": 7,
}
NUM = r"(?:[IVXLC]+|\d+)(?![\wÀ-ỹ])"
UNITS = [
    ("Chương", r"(?:Chương|CHƯƠNG)\s+" + NUM),
    ("Phụ lục", r"(?:Phụ lục|PHỤ LỤC)(?:\s+" + NUM + r")?(?![\wÀ-ỹ])"),
    ("Mục", r"(?:Mục|MỤC)\s+\d+(?![\wÀ-ỹ])"),
    ("PHẦN", r"(?:PHẦN|Phần)\s+(?:[A-ZĐ]|\d+)(?![\wÀ-ỹ])"),
    ("Điều", r"Điều\s+\d+[a-zđ]?(?![\wÀ-ỹ])"),
    ("mục La Mã", r"[IVX]+[.](?=\s)"),
    ("mục A.", r"[A-HJ-UWYZĐ][.](?=\s)"),  # single capital letter other than I, V, X (read as Roman numerals)
    ("mục N.N.N.", r"\d+[.]\d+[.]\d+(?:[.]\d+)*[.]?(?=\s)"),
    ("mục N.N.", r"\d+[.]\d+[.]?(?=\s)"),
    ("mục N.", r"\d+[.](?=\s)"),
]
# labels that Vietnamese legal drafting puts on their own centred line, title on the next line
SPLIT_LABEL = ("Chương", "Mục", "Phụ lục", "PHẦN")


def unit_of(title):
    t = re.sub(r"^[*_“\"]+", "", title)
    for name, pat in UNITS:
        m = re.match(pat, t)
        if m:
            return name, m.group(0), t[m.end():]
    return "khác", "", t


def _plain(s):
    s = s.strip()
    s = re.sub(r"^#{1,6}\s+", "", s)
    return re.sub(r"^[*_]+|[*_]+$", "", s).strip()


def _is_caps(s):
    letters = [c for c in s if c.isalpha()]
    return len(letters) >= 3 and sum(c.isupper() for c in letters) >= 0.8 * len(letters)


def _is_structural(s):
    s = s.strip()
    return (not s or s.startswith(("|", "<!--", "$", "- ", "(", "*(", "_(", ">")) or
            re.match(r"(\d+[.)]|[a-zđ][)])\s", s) is not None)


def plan(lines, skip=None):
    """skip: 1-based line numbers that must not be rewritten nor moved (lines edited by hand)."""
    skip = skip or set()
    ops, taken = [], set()
    n = len(lines)
    for i, l in enumerate(lines):
        if i in taken:
            continue
        hand = (i + 1) in skip
        m = re.match(r"(#{1,6})\s+(.*?)\s*$", l)
        if not m:
            continue
        lv, title = len(m.group(1)), m.group(2)
        unit, label, rest = unit_of(title)
        if unit == "khác":
            continue
        # keep an opening quote of the source (“Điều 3a. …): unit_of strips it to find the label
        label = re.match(r"[“\"]*", re.sub(r"^[*_]+", "", title)).group(0) + label
        why, kind = [], None
        new_lv = LEVELS[unit]
        # an existing separator is kept: '.', ':' or a dash between spaces ("Mục 1 - Báo cáo…")
        sep_m = re.match(r"(\s*(?:[.:]|[-–—](?=\s))?\s*)(.*)$", rest)
        sep, body = sep_m.group(1), sep_m.group(2)
        dash = re.search(r"[-–—]", sep) is not None
        # drop only the closing markers that pair with the opening ones unit_of removed
        # ("**Điều 5. Tên**"), never an italic closer of the text ("13. Tên *(ghi chú)*")
        lead_n = len(re.match(r"[*_]*", title).group(0))

        def strip_close(s):
            t = re.search(r"[*_]+$", s)
            k = min(lead_n, len(t.group(0))) if t else 0
            return s[: len(s) - k] if k else s

        body = strip_close(body).strip()
        moved = []

        if unit in SPLIT_LABEL or unit == "Điều":
            # 1. title missing: it sits on the next non-blank line(s)
            if not body:
                j = i + 1
                while j < n and j <= i + 4 and not lines[j].strip():
                    j += 1
                if j < n and j <= i + 4 and (j + 1) not in skip and not _is_structural(lines[j]):
                    cand = _plain(lines[j])
                    cu = unit_of(cand)[0]
                    ok = cu == "khác" and cand and (
                        _is_caps(cand) if unit != "Điều" else (len(cand) < 200 and not re.search(r"[.;:]$", cand)))
                    if ok:
                        body = cand
                        moved.append(j)
            # 2. caps title continued on the directly following line(s) (no blank line between)
            if body and unit in SPLIT_LABEL and _is_caps(body) and not (hand and not moved):
                j = (moved[-1] if moved else i) + 1
                while j < n and (j + 1) not in skip and lines[j].strip() and not _is_structural(lines[j]) and not lines[j].startswith("#"):
                    cand = _plain(lines[j])
                    if not (_is_caps(cand) and unit_of(cand)[0] == "khác"):
                        break
                    body += " " + cand
                    moved.append(j)
                    j += 1
            if moved:
                why.append("nối tiêu đề từ d.%s" % ", ".join(str(x + 1) for x in moved))
                kind = "join"

        if hand and not moved:
            continue  # heading edited by hand in edits.json: final, unless its title still has to be pulled up

        # separator between label and title
        if unit in ("Chương", "Mục", "Phụ lục"):
            if body and dash:
                sep = " " + sep.strip() + " "
            elif body and "." not in sep and ":" not in sep:
                sep = ": "
                if not moved and not kind:
                    kind = "sep"
                why.append("nhãn và tiêu đề cách nhau bằng dấu hai chấm")
            elif body:
                sep = sep.strip() + " "
            head = label + (sep if body else "") + body
        elif unit == "Điều":
            if body and dash:
                sep = " " + sep.strip() + " "
            elif body and not sep.strip():
                sep = ". "
            elif body:
                sep = sep.strip() + " "
            head = label + (sep if body else sep.strip()) + body
        else:
            head = (label + rest).rstrip()
            head = strip_close(head)

        if new_lv != lv:
            why.append("cấp %s → %s (%s)" % ("#" * lv, "#" * new_lv if new_lv <= 6 else "in đậm", unit))
            kind = kind or "level"
        new_line = ("#" * new_lv + " " + head) if new_lv <= 6 else "**" + re.sub(r"^[*_]+|[*_]+$", "", head) + "**"
        if new_line != l:
            ops.append({"line": i + 1, "new": new_line, "why": "; ".join(why) or "viết lại heading", "kind": kind or "sep"})
            for j in moved:
                taken.add(j)
                ops.append({"line": j + 1, "new": "", "why": "tiêu đề dời lên d.%d" % (i + 1), "kind": "moved"})
    return sorted(ops, key=lambda o: o["line"])
