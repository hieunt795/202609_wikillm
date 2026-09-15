#!/usr/bin/env python3
"""PostToolUse hook: kiem tra trang wiki ngay sau khi ghi.

Ap dung cho file .md trong 02_wiki/ (tru index.md). Kiem cac luat trong
00_schema.md: frontmatter (§1), taxonomy (§2), ten file khop title (§3),
than bai khong heading + link kem ly do (§7), vong doi status (§9).

Exit 0 = dat. Exit 2 = co van de, stderr duoc chuyen lai cho agent.
Moi loi khong luong truoc deu exit 0 de khong chan luong lam viec.
"""
import json
import os
import re
import sys

REQUIRED_FIELDS = ["title", "type", "tags", "sources", "status", "last_updated"]
VALID_TYPES = {"entity", "concept", "case", "analysis"}
VALID_STATUS = {"stub", "draft", "stable", "stale"}


DEBUG = os.environ.get("WIKI_HOOK_DEBUG") == "1"


def bail(exc):
    """Fail-open: khong bao gio chan luong lam viec vi loi cua chinh hook.

    Dat WIKI_HOOK_DEBUG=1 de in traceback khi can go loi hook.
    """
    if DEBUG:
        import traceback

        traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)
    sys.exit(0)


def read_stdin_path():
    # stdin co the mang BOM (PowerShell) hoac encoding la cua console,
    # nen doc byte roi tu giai ma bang utf-8-sig.
    raw = sys.stdin.buffer.read().decode("utf-8-sig", errors="replace")
    payload = json.loads(raw)
    tool_input = payload.get("tool_input") or {}
    return tool_input.get("file_path") or tool_input.get("notebook_path")


def in_wiki(path):
    parts = [p.lower() for p in os.path.normpath(path).split(os.sep)]
    return "02_wiki" in parts and path.lower().endswith(".md")


def split_frontmatter(text):
    """Tra ve (dict_tho, than_bai). dict_tho la {key: raw_value_string}."""
    if not text.startswith("---"):
        return None, text
    end = re.search(r"^---\s*$", text[3:], re.MULTILINE)
    if not end:
        return None, text
    raw = text[3 : 3 + end.start()]
    body = text[3 + end.end() :]
    fields = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields, body


def strip_code_fences(body):
    out, fenced = [], False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(line)
    return "\n".join(out)


def kebab(s):
    s = s.strip().strip("\"'").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def check(path):
    problems = []
    # utf-8-sig: file co BOM van phai doc duoc, khong thi startswith("---") truot
    # va hook bao nham "thieu frontmatter".
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()

    fields, body = split_frontmatter(text)
    if fields is None:
        return ["Thieu frontmatter YAML (§1). Trang wiki phai mo dau bang khoi ---."]

    for field in REQUIRED_FIELDS:
        if field not in fields:
            problems.append("Frontmatter thieu truong `%s` (§1)." % field)

    ptype = fields.get("type", "")
    if ptype and ptype not in VALID_TYPES:
        problems.append(
            "type=`%s` khong hop le (§2). Chi chap nhan: %s."
            % (ptype, ", ".join(sorted(VALID_TYPES)))
        )

    status = fields.get("status", "")
    if status and status not in VALID_STATUS:
        problems.append(
            "status=`%s` khong hop le (§9). Chi chap nhan: %s."
            % (status, ", ".join(sorted(VALID_STATUS)))
        )

    title = fields.get("title", "")
    stem = os.path.splitext(os.path.basename(path))[0]
    if title and kebab(title) != stem.lower():
        problems.append(
            "Ten file `%s` khong khop kebab-case cua title `%s` (§3)." % (stem, title)
        )

    clean = strip_code_fences(body)

    for i, line in enumerate(clean.splitlines(), 1):
        if re.match(r"^#{1,6}\s+\S", line):
            problems.append(
                "Dong %d co heading trong than bai (§7.1): %s\n"
                "  -> Can heading de tach y = dau hieu phai TACH TRANG (§5), "
                "khong them heading." % (i, line.strip()[:60])
            )
            break

    links = re.findall(r"\[\[([^\]]+)\]\]", clean)
    if status != "stub" and not links:
        problems.append(
            "Than bai khong co [[wikilink]] nao (§6). Trang se thanh mo coi o lint. "
            "Neu khai niem can link chua co trang -> tao trang status: stub roi link ngay, "
            "khong hoan sang batch sau."
        )

    for i, line in enumerate(clean.splitlines(), 1):
        if re.match(r"^\s*[-*+]\s*\[\[", line):
            problems.append(
                "Dong %d don link thanh danh sach kieu \"xem them\" (§7.3). "
                "[[wikilink]] phai nam TRONG cau van kem ly do lien ket." % i
            )
            break

    return problems


def main():
    # stderr Windows mac dinh cp1252 -> ky tu § / tieng Viet se nem loi.
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    try:
        path = read_stdin_path()
    except Exception as exc:
        bail(exc)

    if not path or not in_wiki(path):
        sys.exit(0)
    if os.path.basename(path).lower() == "index.md":
        sys.exit(0)
    if not os.path.isfile(path):
        sys.exit(0)

    try:
        problems = check(path)
    except Exception as exc:
        bail(exc)

    if problems:
        rel = os.path.basename(path)
        sys.stderr.write("Kiem tra trang wiki `%s` — %d van de:\n" % (rel, len(problems)))
        for p in problems:
            sys.stderr.write("  - %s\n" % p)
        sys.stderr.write("Sua ngay truoc khi di tiep; khong de don toi luot lint.\n")
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
