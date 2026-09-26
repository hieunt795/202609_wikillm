#!/usr/bin/env python3
"""PostToolUse hook: kiem tra trang wiki ngay sau khi ghi.

Ap dung cho file .md trong 02_wiki/ (tru index.md). Kiem cac luat trong
00_schema.md: frontmatter (§1), taxonomy (§2), ten file khop title (§3),
than bai khong heading + link kem ly do + chu thich vi tri (§7), quy uoc
title (§8), vong doi status + cap reviewed/reviewed_by (§9).

Che do:
  - hook              : doc JSON tu stdin (PostToolUse tren Write|Edit).
  - --all             : quet toan bo 02_wiki/. Dung cho file ghi bang shell, vi
                        hook chi bat duoc tool Write|Edit. Lint phai chay che do nay.
  - --backlinks [p]   : khong co p -> bang so backlink moi trang (giam dan);
                        co p -> liet ke trang tro toi p (ca dang [[p|nhan]]).
  - --ocr             : quet than bai (bo [[link]], $cong thuc$, `code`) tim 6 ho
                        mau loi OCR (lint). Ket qua la ung vien, can doc xac nhan.
  - --stub-debt       : moi trang stub + so luot ingest trong log.md tu khi tao.
  - --inbox-debt      : moi muc _inbox.md + so luot lint tu ngay ghi.
  - --verify-sources  : so bytes/dong/SHA-256 cua 01_sources/ voi
                        03_state/_sources_manifest.md (luat cung 1).
  - --coverage [sid]  : chunk trong 03_state/ -> % dong duoc chu thich §7.5 trich va
                        cac muc (heading) chua trang nao trich. Exit 2 neu chunk [x]
                        con muc chua phu (§10). Khong doi so -> tong ket moi nguon.
  - --now             : gio Viet Nam dang YYYY-MM-DD:hh-MM-ss cho log.md (§12).

Exit 0 = dat. Exit 2 = co van de, stderr duoc chuyen lai cho agent.
Moi loi khong luong truoc deu exit 0 de khong chan luong lam viec.
"""
import datetime
import hashlib
import json
import os
import re
import subprocess
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


def manifest_sources(root):
    """Bang Source id trong 03_state/_sources_manifest.md -> {id: phan loai}."""
    path = os.path.join(root, "03_state", "_sources_manifest.md")
    out = {}
    try:
        with open(path, encoding="utf-8-sig") as fh:
            for line in fh:
                m = re.match(r"^\|\s*`([^`]+)`\s*\|\s*`[^|]*/`\s*\|\s*([^|]+?)\s*\|", line)
                if m:
                    out[m.group(1)] = m.group(2)
    except OSError:
        pass
    return out


def long_sources(wiki_dir):
    """Nguon dai (§10) = nguon ban ke xep 'Nguon dai' HOAC co file trang thai
    trong 03_state/. Doc ban ke de nguon dai chua dung state file van bi ep §7.5."""
    if not wiki_dir:
        return set()
    root = os.path.dirname(wiki_dir)
    found = {k for k, v in manifest_sources(root).items() if "dài" in v.lower()}
    state = os.path.join(root, "03_state")
    if os.path.isdir(state):
        found |= {
            os.path.splitext(f)[0]
            for f in os.listdir(state)
            if f.lower().endswith(".md") and not f.startswith("_")
        }
    return found


def known_sources(wiki_dir):
    return set(manifest_sources(os.path.dirname(wiki_dir))) if wiki_dir else set()


def parse_date(raw):
    try:
        return datetime.date.fromisoformat((raw or "").strip().strip("\"'"))
    except ValueError:
        return None


def check(path, pages=None, longsrc=None, known=None):
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

    if known:
        unknown = [s for s in srcs if s not in known]
        if unknown:
            problems.append(
                "`sources:` co nguon khong co trong 03_state/_sources_manifest.md: %s (§10). "
                "Dung dung source id cua ban ke; nguon moi phai them vao ban ke o luot ingest dau."
                % ", ".join(unknown)
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
    known = known_sources(wiki_dir)
    total = bad = 0
    for f in sorted(os.listdir(wiki_dir)):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        total += 1
        p = os.path.join(wiki_dir, f)
        try:
            problems = check(p, pages, longsrc, known)
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


# ---------------------------------------------------------------------------
# Lenh phu tro cho skill (B14 audit 2026-09-17): gom viec lap lai vao script
# de model khong phai tu dung grep/awk moi luot.

VN_TZ = datetime.timezone(datetime.timedelta(hours=7))
LOG_HEAD = re.compile(r"^## \[(\d{4}-\d{2}-\d{2}):(\d{2})-(\d{2})-(\d{2})\] (\w+) \|")


def now_vn():
    return datetime.datetime.now(VN_TZ).strftime("%Y-%m-%d:%H-%M-%S")


def log_entries(root):
    """[(datetime VN hoac None gio, date, op)] tu log.md. Muc 00-00-00 = khong ro gio."""
    out = []
    try:
        with open(os.path.join(root, "log.md"), encoding="utf-8-sig") as fh:
            for line in fh:
                m = LOG_HEAD.match(line)
                if not m:
                    continue
                d = datetime.date.fromisoformat(m.group(1))
                hms = tuple(int(x) for x in m.group(2, 3, 4))
                when = None if hms == (0, 0, 0) else datetime.datetime(d.year, d.month, d.day, *hms, tzinfo=VN_TZ)
                out.append((when, d, m.group(5)))
    except OSError:
        pass
    return out


def cmd_backlinks(wiki_dir, target):
    pages = existing_pages(wiki_dir)
    if target:
        target = os.path.splitext(os.path.basename(target))[0]
        if target not in pages:
            sys.stdout.write("Khong co trang `%s` trong 02_wiki/.\n" % target)
            sys.exit(2)
        hits = []
        for f in sorted(os.listdir(wiki_dir)):
            stem = os.path.splitext(f)[0]
            if not f.lower().endswith(".md") or f.lower() == "index.md" or stem == target:
                continue
            with open(os.path.join(wiki_dir, f), encoding="utf-8-sig") as fh:
                _, body = split_frontmatter(fh.read())
            if target in link_targets(strip_code_fences(body)):
                hits.append(stem)
        for h in hits:
            sys.stdout.write(h + "\n")
        sys.stdout.write("%d backlink toi %s (khong tinh index.md).\n" % (len(hits), target))
        sys.exit(0)
    counts = backlink_counts(wiki_dir, pages)
    for name, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        sys.stdout.write("%d\t%s\n" % (c, name))
    sys.exit(0)


OCR_PATTERNS = [
    ("l/O thay chu so hoac I hoa", re.compile(r"\bl[bcdfgkmnpqstvwxz][a-z]+\b|\b[a-z]{1,3}O\b|[a-z]lO\b")),
    ("so chu thich dinh vao tu", re.compile(r"\b[A-Za-z]{4,}l?\d{1,2}\b")),
    ("chu so bi tach", re.compile(r"\b(?:1 9|2 0)\d{2}\b")),
    ("HOA-thuong lan trong mot tu", re.compile(r"\b[A-Z]{2,}[a-z]{3,}\b")),
    ("nguyen am nhan doi bat thuong", re.compile(r"\b(?=[A-Za-z]{4,}\b)[A-Za-z]*(?:aa|ii|uu)[A-Za-z]*\b")),
    ("rac markdown OCR", re.compile(r"<sup>|<span id=|\[#page-|�")),
]


def ocr_clean(line):
    line = re.sub(r"\[\[[^\]]*\]\]", " ", line)
    line = re.sub(r"\$[^$]*\$", " ", line)
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"\([^()]*d\.\d+[^()]*\)", " ", line)  # chu thich §7.5 chua ten muc tieng Anh
    return line


def cmd_ocr(wiki_dir):
    hits = 0
    for f in sorted(os.listdir(wiki_dir)):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        with open(os.path.join(wiki_dir, f), encoding="utf-8-sig") as fh:
            _, body = split_frontmatter(fh.read())
        for i, raw in enumerate(strip_code_fences(body).splitlines(), 1):
            line = ocr_clean(raw)
            for label, rx in OCR_PATTERNS:
                for m in rx.finditer(line):
                    hits += 1
                    sys.stdout.write("%s:%d\t%s\t%s\n" % (f, i, label, m.group(0)))
    sys.stdout.write(
        "%d ung vien OCR. Mo trang de xac nhan; ten rieng (Paasche...) la bao gia.\n" % hits
    )
    sys.exit(0)


def page_created(root):
    """{stem: datetime tao} theo commit dau tien them file; fallback mtime."""
    created = {}
    try:
        out = subprocess.run(
            ["git", "-c", "core.quotepath=off", "--no-optional-locks", "log",
             "--diff-filter=A", "--name-only", "--format=@%cI", "--", "02_wiki"],
            cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=30,
        ).stdout
        when = None
        for line in out.splitlines():
            if line.startswith("@"):
                when = datetime.datetime.fromisoformat(line[1:])
            elif line.strip() and when:
                stem = os.path.splitext(os.path.basename(line.strip()))[0]
                created[stem] = when  # git log moi -> cu: gia tri cuoi = lan them dau tien
    except Exception:
        pass
    return created


def cmd_stub_debt(wiki_dir):
    root = os.path.dirname(wiki_dir)
    created = page_created(root)
    ingests = [e for e in log_entries(root) if e[2] == "ingest"]
    rows = []
    for f in sorted(os.listdir(wiki_dir)):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        p = os.path.join(wiki_dir, f)
        with open(p, encoding="utf-8-sig") as fh:
            fields, _ = split_frontmatter(fh.read())
        if not fields or fields.get("status") != "stub":
            continue
        stem = os.path.splitext(f)[0]
        when = created.get(stem) or datetime.datetime.fromtimestamp(os.path.getmtime(p), VN_TZ)
        when = when.astimezone(VN_TZ)
        n = sum(1 for w, d, _ in ingests if (w > when if w else d > when.date()))
        rows.append((n, stem, when))
    for n, stem, when in sorted(rows, key=lambda r: (-r[0], r[1])):
        flag = "NO" if n >= 3 else "  "
        sys.stdout.write("%s\t%d\t%s\t%s\n" % (flag, n, when.strftime("%Y-%m-%d:%H-%M"), stem))
    sys.stdout.write(
        "%d stub, %d no stub (>= 3 luot ingest tu khi tao, §9).\n"
        % (len(rows), sum(1 for r in rows if r[0] >= 3))
    )
    sys.exit(0)


def cmd_inbox_debt(root):
    lints = [d for _, d, op in log_entries(root) if op == "lint"]
    rows = []
    try:
        with open(os.path.join(root, "_inbox.md"), encoding="utf-8-sig") as fh:
            for line in fh:
                m = re.match(r"^- \[(\d{4}-\d{2}-\d{2})\]\s*(.*)", line)
                if m:
                    d = datetime.date.fromisoformat(m.group(1))
                    rows.append((sum(1 for x in lints if x > d), m.group(1), m.group(2)[:90]))
    except OSError:
        pass
    for n, d, text in rows:
        sys.stdout.write("%s\t%d\t%s\t%s\n" % ("NO" if n >= 3 else "  ", n, d, text))
    sys.stdout.write(
        "%d muc inbox, %d no (>= 3 luot lint sau ngay ghi, §11). "
        "Dem theo ngay nen luot lint cung ngay voi muc khong duoc tinh.\n"
        % (len(rows), sum(1 for r in rows if r[0] >= 3))
    )
    sys.exit(0)


def cmd_verify_sources(root):
    manifest = os.path.join(root, "03_state", "_sources_manifest.md")
    rx = re.compile(r"^\|\s*`(01_sources/[^`]+)`\s*\|\s*([\d.]+)\s*\|\s*([\d.]+|—)\s*\|\s*`([0-9a-f]{64})`\s*\|")
    listed, bad = set(), []
    with open(manifest, encoding="utf-8-sig") as fh:
        for line in fh:
            m = rx.match(line)
            if not m:
                continue
            rel, size, lines, sha = m.groups()
            listed.add(rel)
            p = os.path.join(root, *rel.split("/"))
            if not os.path.isfile(p):
                bad.append("THIEU   %s" % rel)
                continue
            h = hashlib.sha256()
            nl = n = 0
            with open(p, "rb") as src:
                for chunk in iter(lambda: src.read(1 << 20), b""):
                    h.update(chunk)
                    n += len(chunk)
                    nl += chunk.count(b"\n")
            if h.hexdigest() != sha:
                bad.append(
                    "LECH    %s (ban ke %s byte, thuc te %d byte; dong ban ke %s, thuc te %d)"
                    % (rel, size, n, lines, nl)
                )
    extra = []
    src_root = os.path.join(root, "01_sources")
    for d, _, files in os.walk(src_root):
        for f in files:
            if not f.lower().endswith((".md", ".pdf")):
                continue  # file phu cua OCR (json, anh) khong can ke
            rel = os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/")
            if rel not in listed:
                extra.append("CHUA KE %s" % rel)
    for line in bad + extra:
        sys.stdout.write(line + "\n")
    sys.stdout.write(
        "%d file trong ban ke, %d lech/thieu, %d file .md/.pdf chua ke.\n"
        % (len(listed), len(bad), len(extra))
    )
    if bad:
        sys.stdout.write(
            "  -> Luat cung 1: khong sua lai nguon cho khop. Bao nguoi dung; "
            "lech CRLF/LF thi noi dung va so dong co the van dung.\n"
        )
    sys.exit(2 if (bad or extra) else 0)


# --coverage: muc (heading) nao trong chunk chua duoc chu thich §7.5 nao trich.
COV_SKIP_HEAD = re.compile(
    r"^(references|bibliography|index|(table of )?contents|exercises?|questions|acknowledg\w*|tài liệu tham khảo"
    r"|introduction|overview|summary|conclusions?|concluding)\b",  # gioi thieu/tom tat chuong: lo trinh, lap y
    re.I,
)
COV_MIN_LINES = 3  # muc ngan hon (vd "## Period 1:") khong tinh


def cov_norm(s):
    s = re.sub(r"<[^>]+>|\]\([^)]*\)|[\[\]]", "", s)  # bo the HTML va cu phap link markdown cua ban OCR
    s = re.sub(r"^[#\s]*", "", s)
    s = re.sub(r"^(chapter\s+)?[\dIVX]+(\.\d+)*[.:)]?\s+", "", s, flags=re.I)  # bo so muc dau heading
    return re.sub(r"\s+", " ", s).strip().lower()


def cov_state(root, sid):
    """-> (danh sach file nguon, [(trang thai, a, b, file, dong state)])."""
    with open(os.path.join(root, "03_state", sid + ".md"), encoding="utf-8-sig") as fh:
        text = fh.read()
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    raw = []
    if fm:
        m = re.search(r"^file:[ \t]*(.*)$((?:\n[ \t]+-[ \t]*.*)*)", fm.group(1), re.M)
        if m:
            raw = [m.group(1).strip()] if m.group(1).strip() else []
            raw += [x.strip()[1:].strip() for x in m.group(2).split("\n") if x.strip()]
    files = []
    for r in raw:
        r = r.split(" (")[0].strip()
        if "<" in r:  # mau ten file -> moi .md trong thu muc
            d = os.path.join(root, os.path.dirname(r))
            if os.path.isdir(d):
                files += sorted(os.path.join(d, f) for f in os.listdir(d) if f.lower().endswith(".md"))
        else:
            files.append(os.path.join(root, *r.split("/")))
    chunks = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*`\[(.)\]`\s*\|", line)
        r = re.search(r"d\.(\d+)\s*[–-]\s*(\d+)", line)
        if not m or not r:
            continue
        f = files[0] if len(files) == 1 else None
        if not f:
            for tok in re.findall(r"`([^`]+\.md)`", line):
                hit = [p for p in files if os.path.basename(p).endswith(tok)]
                if hit:
                    f = hit[0]
                    break
        chunks.append((m.group(1), int(r.group(1)), int(r.group(2)), f, line))
    return files, chunks


def cov_cited(wiki_dir, sid, files):
    """{duong dan file: tap dong duoc trich}, so chu thich khong xac dinh duoc file."""
    cited, lost = {}, 0
    head = re.compile(r"^\s*" + re.escape(sid) + r"\b")

    def by_name(name):
        name = name.strip()
        hit = [p for p in files if os.path.basename(p).endswith(name)]
        if not hit and not name.endswith(".md"):  # "file -5", "file TT14_1" (khong .md)
            hit = [p for p in files if os.path.basename(p).endswith(name + ".md")]
        return hit[0] if hit else None

    for f in os.listdir(wiki_dir):
        if not f.lower().endswith(".md") or f.lower() == "index.md":
            continue
        with open(os.path.join(wiki_dir, f), encoding="utf-8-sig") as fh:
            body = fh.read()
        prev = None  # file cua chu thich truoc cung nguon trong trang -> cho "cung file"/"cung bai"
        # mot ngoac co the gop nhieu nguon, ngan bang ";" -> xet tung doan bat dau bang source id
        for grp in re.finditer(r"\(([^()]*)\)", body):
            for inner in grp.group(1).split(";"):
                if not head.match(inner):
                    continue
                inner = head.sub("", inner, count=1)
                pos = inner.find("d.")
                if pos < 0:
                    continue
                target = files[0] if len(files) == 1 else None
                fm = re.search(r"\bfile\s+(.+?\.md)", inner) or re.search(r"\bfile\s+([^\s,]+)", inner)
                if fm:
                    target = by_name(fm.group(1))
                elif re.search(r"\bcùng (file|bài)\b", inner):
                    target = prev
                elif not target:
                    ch = re.search(r"\bCh\.(\d+)", inner)  # fixed_income_during: Ch.n nam o file -(n+1).md
                    if ch:
                        target = by_name("-%d.md" % (int(ch.group(1)) + 1))
                if not target:
                    lost += 1
                    continue
                prev = target
                tail = re.match(r"[\sd.,–\-0-9]*", inner[pos:]).group(0)
                lines = cited.setdefault(target, set())
                for a, b in re.findall(r"(\d+)(?:\s*[–-]\s*(\d+))?", tail):
                    lines.update(range(int(a), int(b or a) + 1))
    return cited, lost


def cov_source(root, wiki_dir, sid):
    """-> (lost, [(trang thai, a, b, % phu | None, [(tu, den, heading)])])."""
    files, chunks = cov_state(root, sid)
    cited, lost = cov_cited(wiki_dir, sid, files)
    cache, out = {}, []
    for st, a, b, f, row in chunks:
        if "bỏ qua, không tạo trang" in row.lower() or not f or not os.path.isfile(f):
            out.append((st, a, b, "mien" if f else "?", []))
            continue
        if f not in cache:
            with open(f, "rb") as fh:
                cache[f] = [x.decode("utf-8", "replace").rstrip("\r") for x in fh.read().split(b"\n")]
        src, got = cache[f], cited.get(f, set())
        body = [i for i in range(a, min(b, len(src)) + 1) if src[i - 1].strip()]
        hit = sum(1 for i in body if i in got)
        if not hit:
            out.append((st, a, b, None, []))
            continue
        skip = [cov_norm(x) for x in re.findall(r"bỏ qua:\s*([^—;|]+)", row, re.I)]
        starts = [a] + [i for i in range(a + 1, min(b, len(src)) + 1) if src[i - 1].startswith("#")]
        miss = []
        for k, s in enumerate(starts):
            e = starts[k + 1] - 1 if k + 1 < len(starts) else b
            head = src[s - 1] if src[s - 1].startswith("#") else "(đầu chunk)"
            if src[s - 1].strip() == "---":  # frontmatter YAML cua file chuyen doi, khong phai noi dung
                continue
            h = cov_norm(head)
            if COV_SKIP_HEAD.match(h) or any(x and (x in h or h in x) for x in skip):
                continue
            rng = [i for i in range(s, e + 1) if i <= len(src) and src[i - 1].strip()]
            if len(rng) >= COV_MIN_LINES and not any(i in got for i in rng):
                miss.append((s, e, head.strip()))
        out.append((st, a, b, round(100.0 * hit / max(1, len(body))), miss))
    return lost, out


def cmd_coverage(root, wiki_dir, sid):
    state = os.path.join(root, "03_state")
    sids = [sid] if sid else sorted(
        os.path.splitext(f)[0] for f in os.listdir(state) if f.endswith(".md") and not f.startswith("_")
    )
    bad = 0
    for s in sids:
        if not os.path.isfile(os.path.join(state, s + ".md")):
            sys.stdout.write("Khong co 03_state/%s.md\n" % s)
            sys.exit(2)
        lost, rows = cov_source(root, wiki_dir, s)
        flagged = [r for r in rows if r[0] == "x" and r[4]]
        bad += len(flagged)
        if sid:
            for st, a, b, pct, miss in rows:
                tag = {"mien": "mien (bo qua)", "?": "khong xac dinh file", None: "khong do duoc (0 chu thich)"}
                p = tag[pct] if pct in tag else "%d%%" % pct
                sys.stdout.write("[%s] d.%d–%d\t%s\t%d muc chua phu\n" % (st, a, b, p, len(miss)))
                for x, y, h in miss:
                    sys.stdout.write("      d.%d–%d  %s\n" % (x, y, h[:90]))
        else:
            meas = [r for r in rows if isinstance(r[3], int)]
            sys.stdout.write("%s\t%s\t%d/%d chunk do duoc; %d chunk [x] con muc chua phu\n" % (
                "NO" if flagged else "  ", s, len(meas), len(rows), len(flagged)))
        if lost:
            sys.stdout.write("  (%s: %d chu thich khong xac dinh duoc file)\n" % (s, lost))
    sys.stdout.write("%d chunk [x] con muc chua phu (§10: [x] = moi muc da trich hoac 'bo qua: <heading>').\n" % bad)
    sys.exit(2 if bad else 0)


def main():
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    args = sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        sys.stdout.write(__doc__)
        sys.exit(0)
    if args and args[0] == "--now":
        sys.stdout.write(now_vn() + "\n")
        sys.exit(0)
    if args and args[0].startswith("--"):
        here = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
        wiki = os.path.join(here, "02_wiki")
        if not os.path.isdir(wiki):
            sys.stderr.write("Khong tim thay 02_wiki/ duoi %s\n" % here)
            sys.exit(0 if args[0] == "--all" else 2)
        cmd = args[0]
        if cmd == "--all":
            run_all(wiki)
        elif cmd == "--backlinks":
            cmd_backlinks(wiki, args[1] if len(args) > 1 else None)
        elif cmd == "--ocr":
            cmd_ocr(wiki)
        elif cmd == "--stub-debt":
            cmd_stub_debt(wiki)
        elif cmd == "--inbox-debt":
            cmd_inbox_debt(here)
        elif cmd == "--verify-sources":
            cmd_verify_sources(here)
        elif cmd == "--coverage":
            cmd_coverage(here, wiki, args[1] if len(args) > 1 else None)
        sys.stderr.write("Lenh khong hop le: %s. Xem --help.\n" % cmd)
        sys.exit(2)

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
        problems = check(path, existing_pages(wiki), long_sources(wiki), known_sources(wiki))
    except Exception as exc:
        bail(exc)

    if problems:
        report(path, problems)
        sys.stderr.write("Sua ngay truoc khi di tiep; khong de don toi luot lint.\n")
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:  # vd `--backlinks | head`: nguoi doc dong pipe som
        try:
            sys.stdout = open(os.devnull, "w")
        except Exception:
            pass
        sys.exit(0)
