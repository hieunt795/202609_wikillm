# `.claude`

Gói chỉ dẫn đang hoạt động cho dự án LLM Wiki — Macroeconomics.

## Cấu trúc

- `CLAUDE.md` — bối cảnh dự án, guardrail và quy tắc áp dụng chéo (ở root level).
- `rules/` — rule chuyên biệt theo chủ đề; không dùng `@import`.
- `skills/` — workflow chi tiết cho từng operation (`/ingest`, `/query`, `/lint`, `/promote`, `/review-node`).
- `hooks/` — script kiểm tra xác định được bằng máy (validator).
- `settings.json` — cấu hình guardrail thực thi tự động.
- `session_handoffs/` — handoff giữa các phiên làm việc có thay đổi repo.

## Chạy validator thủ công

```powershell
python .claude/hooks/validate_wiki_page.py --all
python .claude/hooks/validate_wiki_page.py --verify-sources
python .claude/hooks/validate_wiki_page.py --now
```
