# Session Handoff: 2026-09-23 14:23:15 — Sửa lỗi nesting `.claude/.claude/` và dọn file thừa

## Tóm tắt công việc

**Vấn đề phát hiện:** commit `abd8dbc` (2026-09-21) vô tình rename `.claude/{hooks,rules,skills,settings.json}` thành `.claude/.claude/{hooks,rules,skills,settings.json}` — lồng sai một cấp thư mục. Hậu quả:
- `.claude/settings.json` hook path tự tham chiếu không ở vị trí chuẩn mà harness tìm kiếm.
- 6 skill chính (`ingest`, `lint`, `promote`, `query`, `review-node`, `writing-style`) bị harness scope riêng cho `.claude/` → lệnh cốt lõi không xuất hiện bình thường khi làm việc trên `02_wiki/`.

**Công việc thực hiện:**
1. **Dùng `git mv` để sửa nesting** (rename-tracked, giữ lịch sử): `.claude/.claude/{hooks,rules,skills}` + `settings.json` lên `.claude/`.
2. **Sửa path tự tham chiếu** trong:
   - `.claude/settings.json` (1 dòng hook path)
   - 5 SKILL file: `ingest`, `lint`, `promote`, `query`, `review-node`
   - 1 rule file: `source-management.md`
3. **Xoá `.claude/CLAUDE.md`** (duplicate 88 dòng) → giữ root `CLAUDE.md` (110 dòng, có session status) làm bản chính thức duy nhất.
4. **Sửa root `CLAUDE.md:65`** path `log_questions.py`: `.claude/tools/...` → `Claude outputs/log_questions.py` (script local, gitignored).
5. **Archive tài liệu draft** (không xoá): `CLAUDEV4_1.local.md` + `CLAUDE_RULES_REPORT.md` → `.claude/archive/`.
6. **Cập nhật README.md**: bỏ ref `.old/` (directory đã bị xoá ở commit `b006659`); cập nhật ref `.claude/` (không dùng `.claude/.claude/`).

## Kiểm chứng

- Grep `\.claude/\.claude` trên toàn repo (trừ log cũ) → **rỗng**.
- `python .claude/hooks/validate_wiki_page.py --all` → **chạy được không lỗi**.
- 6 skill trở lại **project-wide scope** (xác nhận bằng tool listing hoặc đọc file `.claude/`).
- `git status` → toàn bộ file là rename (`R`), không có xoá/thêm mất lịch sử.

## Trạng thái repo

- Working tree: sạch ngoài các thay đổi dự kiến (staged).
- `.claude/` structure: `.claude/{hooks,rules,skills,settings.json,archive,session_handoffs,README.md}` ✓
- Root CLAUDE.md: chính thức, có session status ✓
- Không đụng: `01_sources/`, `02_wiki/`, `03_state/`, `log.md` (chỉ append entry fix nesting), 12 file ingest dở dang ✓

## Ghi chú cho session sau

- Hook `PostToolUse` từ `.claude/settings.json` lúc này sẽ chạy đúng khi ghi/sửa trang wiki.
- Skills sẽ tự động xuất hiện project-wide trong listing khi làm bất kỳ tác vụ nào.
- Các file draft ở `.claude/archive/` chỉ là reference — chưa implement `.claude/rules-draft/` hoặc `.claude/agents/` nên không trigger hook.
- Session status trong root `CLAUDE.md` cần cập nhật sau lần ingest tiếp theo.
