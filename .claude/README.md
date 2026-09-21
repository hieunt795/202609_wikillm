# `.claude_draft`

Gói thử nghiệm này mô phỏng hệ thống chỉ dẫn Claude đề xuất trong `CLAUDE_RULES_REPORT.md`. Nó không được Claude Code tự nạp và không thay thế `CLAUDE.md` hoặc `.claude/` đang hoạt động ở root.

## Phạm vi

- `CLAUDE.md` và `.claude/rules/` chứa bối cảnh, guardrail và rule thử nghiệm.
- `.claude/skills/` và `.claude/hooks/` là bản sao của logic hiện hành, với đường dẫn runtime đổi sang gói draft.
- Validator vẫn đọc dữ liệu thật tại root thông qua working directory hoặc `CLAUDE_PROJECT_DIR`.
- Handoff thử nghiệm được ghi trong `.claude_draft/session_handoffs/`.
- Chưa tạo agents, agent memory hoặc `settings.local.json` vì chưa có nhu cầu vận hành tương ứng.

## Kiểm thủ công

Chạy từ root project:

```powershell
python .claude_draft/.claude/hooks/validate_wiki_page.py --all
python .claude_draft/.claude/hooks/validate_wiki_page.py --verify-sources
python .claude_draft/.claude/hooks/validate_wiki_page.py --now
```

## Kích hoạt sau review

1. Đối chiếu `CLAUDE.md` và bốn rules với `00_schema.md`, năm skills và validator.
2. Chạy thử từng nhóm wiki, source/state, records và handoff.
3. Chỉ chuyển nội dung đã duyệt sang `CLAUDE.md` và `.claude/` ở root.
4. Không xoá bản hiện hành hoặc bản thử nghiệm cũ trước khi xác nhận hệ thống mới ổn định.
