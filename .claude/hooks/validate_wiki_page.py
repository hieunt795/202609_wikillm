#!/usr/bin/env python3
"""PostToolUse hook: kiem tra trang wiki ngay sau khi ghi.

Ap dung cho file .md trong 02_wiki/ (tru index.md). Kiem cac luat trong
00_schema.md: frontmatter (§1), taxonomy (§2), ten file khop title (§3),
than bai khong heading + link kem ly do + chu thich vi tri (§7), quy uoc
title (§8), vong doi status + cap reviewed/reviewed_by (§9).

Hai che do:
  - hook  : doc JSON tu stdin (PostToolUse tren Write|Edit).
  - --all : quet toan bo 02_wiki/. Dung cho file ghi bang shell, vi hook
            chi bat duoc tool Write|Edit. Lint phai chay che do nay.

Exit 0 = dat. Exit 2 = co van de, stderr duoc chuyen lai cho agent.
Moi loi khong luong truoc deu exit 0 de khong chan luong lam viec.
"""
import datetime
import json
import os
import re
import sys

REQUIRED_FIELDS = ["title", "type", "tags", "sources", "status", "last_updated"]
VALID_TYPES = {"entity", "concept", "case", "analysis"}
VALID_STATUS = {"stub", "draft", "stable", "stale"}
VALID_REVIEWERS = {"user", "model"}

# §7.5 chi ap cho trang duoc ghi TU ngay luat co hieu luc tro di.
# 51 trang cu giu nguyen, khong backfill hang loat -- nhung trang nao
# duoc cham vao (last_updated duoc nang len) thi phai co chu thich.
CITATION_RULE_FROM = datetime.date(2026, 9, 14)

DEBUG = os.environ.get("WIKI_HOOK_DEBUG") == "1"


def bail(exc):
    """Fail-open: khong bao gio chan luong lam viec vi loi cua chinh hook."""
    if DEBUG:
        import traceback

        traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)
    sys.exit(0)


def read_stdin_path():
    raw = sys.stdin.buffer.read().decode("utf-8-sig", errors="replace")
    payload = json.loads(raw)
    tool_input = payload.get("tool_input") or {}
    return tool_input.get("file_path") or tool_input.get("notebook_path")


def in_wiki(path):
    parts = [p.lower() for p in os.path.normpath(path).split(os.sep)]
    return "02_wiki" in parts and path.lower().endswith(".md")


def split_frontmatter(text):
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


def yaml_list(raw):
    """`[a, b]` hoac `[]` -> list cac phan tu khong rong."""
    raw = (raw or "").strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [x.strip().strip("\"'") for x in raw.split(",") if x.strip().strip("\"'")]


def link_targets(clean):
    """[[a]] va [[a|nhan hien thi]] deu tra ve 'a' (§6)."""
    return [m.group(1).split("|")[0].strip() for m in re.finditer(r"\[\[([^\]]+)\]\]", clean)]


def wiki_dir_of(path):
    d = os.path.dirname(os.path.abspath(path))
    return d if os.path.basename(d).lower() == "02_wiki" else None


def existing_pages(wiki_dir):
    if not wiki_dir or not os.path.isdir(wiki_dir):
        return None
    return {
        os.path.splitext(f)[0]
        for f in os.listdir(wiki_dir)
        if f.lower().endswith(".md") and f.lower() != "index.md"
    }


def long_sources(wiki_dir):
    """Nguon dai = nguon co file trang thai trong 03_state/ (§10)."""
    if not wiki_dir:
        return set()
    state = os.path.join(os.path.dirname(wiki_dir), "03_state")
    if not os.path.isdir(state):
        return set()
    return {
        os.path.splitext(f)[0]
        for f in os.listdir(state)
        if f.lower().endswith(".md") and not f.startswith("_")
    }


def parse_date(raw):
    try:
        return datetime.date.fromisoformat((raw or "").strip().strip("\"'"))
    except ValueError:
        return None


def check(path, pages=None, longsrc=None):
    problems = []
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

    # §8: case/analysis phai dat title dang cau, khong phai danh tu.
    # Chi bat truong hop ro rang (<= 2 tu) de khong bao gia.
    if ptype in ("case", "analysis") and stem.count("-") < 2:
        problems.append(
            "Trang `%s` dat title dang danh tu (§8). `case`/`analysis` phai dung "
            "cau khang dinh hoan chinh, hoac cau hoi neu nguon chua ket luan." % ptype
        )

    srcs = yaml_list(fields.get("sources", ""))
    if "sources" in fields and not srcs:
        problems.append(
            "`sources: []` rong (§1). Moi trang phai tro ve it nhat 1 nguon trong "
            "01_sources/ -- tru khi trang duoc sinh tu Query, khi do ghi nguon goc "
            "cua cac trang da tong hop."
        )

    updated = parse_date(fields.get("last_updated", ""))
    if "last_updated" in fields and updated is None:
        problems.append(
            "`last_updated: %s` khong phai ngay dang YYYY-MM-DD (§1)."
            % fields.get("last_updated", "")
        )

    # §9: reviewed + reviewed_by di thanh cap.
    if "reviewed" in fields or "reviewed_by" in fields:
        if parse_date(fields.get("reviewed", "")) is None:
            problems.append(
                "`reviewed: %s` phai la ngay YYYY-MM-DD va di kem `reviewed_by` (§9)."
                % fields.get("reviewed", "")
            )
        who = fields.get("reviewed_by", "").strip().strip("\"'")
        if who not in VALID_REVIEWERS:
            problems.append(
                "`reviewed_by: %s` khong hop le (§9). Chi chap nhan: user, model."
                % fields.get("reviewed_by", "")
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

    targets = link_targets(clean)
    if status != "stub" and not targets:
        problems.append(
            "Than bai khong co [[wikilink]] nao (§6). Trang se thanh mo coi o lint. "
            "Neu khai niem can link chua co trang -> tao trang status: stub roi link ngay, "
            "khong hoan sang batch sau."
        )

    # Link chet: [[x]] va [[x|nhan]] deu phai tro toi trang co that.
    if pages is not None:
        for t in sorted(set(targets)):
            if t and t != stem and t not in pages:
                problems.append(
                    "[[%s]] tro toi trang khong ton tai (§6). Tao trang `status: stub` "
                    "roi link, hoac sua lai ten trang." % t
                )

    for i, line in enumerate(clean.splitlines(), 1):
        if re.match(r"^\s*[-*+]\s*\[\[", line):
            problems.append(
                "Dong %d don link thanh danh sach kieu \"xem them\" (§7.3). "
                "[[wikilink]] phai nam TRONG cau van kem ly do lien ket." % i
            )
            break

    # §7.5: claim tu nguon dai phai kem chu thich vi tri.
    if longsrc and status != "stub" and updated and updated >= CITATION_RULE_FROM:
        from_long = [s for s in srcs if s in longsrc]
        if from_long:
            has_cite = re.search(r"d\.\d+\s*[–-]\s*\d+", clean) or any(
                re.search(r"\(\s*%s\s*," % re.escape(s), clean) for s in from_long
            )
            if not has_cite:
                problems.append(
                    "Claim lay tu nguon dai (%s) ma than bai khong co chu thich vi tri (§7.5).\n"
                    "  -> Moi claim ghi `(<nguon>, <chuong>, <muc>, d.<tu>-<den>)` ngay sau claim.\n"
                    "  -> Dai dong lay tu chunk dang doc trong 03_state/<nguon>.md."
                    % ", ".join(from_long)
                )

    return problems


def report(path, problems, stream=sys.stderr):
    stream.write("Kiem tra trang wiki `%s` — %d van de:\n" % (os.path.basename(path), len(problems)))
    for p in problems:
        stream.write("  - %s\n" % p)


def backlink_counts(wiki_dir, pages):
    """Dem backlink cho tung trang. Day la thuoc tinh cua CA DO THI nen hook
    chay tren mot file khong the biet duoc -- chi che do --all tinh duoc."""
    counts = {p: 0 for p in pages}
    for f in sorted(os.listdir(wiki_dir)):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        stem = os.path.splitext(f)[0]
        try:
            with open(os.path.join(wiki_dir, f), encoding="utf-8-sig") as fh:
                _, body = split_frontmatter(fh.read())
        except Exception:
            continue
        for t in set(link_targets(strip_code_fences(body))):
            if t in counts and t != stem:
                counts[t] += 1
    return counts


def run_all(wiki_dir):
    pages = existing_pages(wiki_dir)
    longsrc = long_sources(wiki_dir)
    total = bad = 0
    for f in sorted(os.listdir(wiki_dir)):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        total += 1
        p = os.path.join(wiki_dir, f)
        try:
            problems = check(p, pages, longsrc)
        except Exception as exc:  # mot file hong khong duoc chan ca luot quet
            problems = ["Khong doc duoc: %s" % exc]
        if problems:
            bad += 1
            report(p, problems, sys.stdout)

    # Trang mo coi theo chieu BACKLINK (§6). Hook tren tung file khong bat duoc
    # vi no khong nhin thay do thi -- day la lo hong da tao ra 12 trang mo coi
    # o hai luot ingest 2026-09-14.
    orphans = sorted(n for n, c in backlink_counts(wiki_dir, pages).items() if c == 0)
    if orphans:
        sys.stdout.write(
            "\n%d trang MO COI — khong trang nao tro toi (§6):\n" % len(orphans)
        )
        for n in orphans:
            sys.stdout.write("  - %s\n" % n)
        sys.stdout.write(
            "  -> Them lien ket co ly do that tu trang lien quan; khong va cho du chi tieu.\n"
        )

    sys.stdout.write(
        "\n%d trang quet, %d trang co van de, %d trang mo coi.\n"
        % (total, bad, len(orphans))
    )
    sys.exit(2 if (bad or orphans) else 0)


def main():
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    if "--all" in sys.argv:
        here = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
        wiki = os.path.join(here, "02_wiki")
        if not os.path.isdir(wiki):
            sys.stderr.write("Khong tim thay 02_wiki/ duoi %s\n" % here)
            sys.exit(0)
        run_all(wiki)

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
        wiki = wiki_dir_of(path)
        problems = check(path, existing_pages(wiki), long_sources(wiki))
    except Exception as exc:
        bail(exc)

    if problems:
        report(path, problems)
        sys.stderr.write("Sua ngay truoc khi di tiep; khong de don toi luot lint.\n")
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
