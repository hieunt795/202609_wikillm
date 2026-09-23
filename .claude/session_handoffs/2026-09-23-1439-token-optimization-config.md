# 2026-09-23 14:39 — Tối ưu token: config global + CLAUDE.md project

## Kết quả

- Root `CLAUDE.md`: bỏ mục "Trạng thái phiên làm việc" (~35 dòng, đã lỗi thời), thay bằng 1 dòng trỏ tới handoff mới nhất + `index.md` §Sources. Hai quy tắc định dạng (`sources:` inline list; bullet không mở đầu bằng `[[wikilink]]`) chuyển vào "Nhắc nhanh về trang wiki".
- `decisions.md`: thêm mục 2026-09-23 ghi lý do + quyết định Ch.17 chuyển từ `CLAUDE.md`.
- Ngoài repo (`~/.claude/`):
  - `CLAUDE.md` global: sửa quy tắc ngôn ngữ, thêm ngưỡng context 20%, ngưỡng 60% nhắc `/compact`, thêm mục 6 "Sử dụng Agent" (luôn phải hỏi trước).
  - `settings.json`: `"model": "opus"` → `"haiku"`.
  - `statusline-command.sh`: thay `jq` (máy không có) bằng Python; hiện `⚠ /compact` đỏ khi context ≥ 60%.

## Kiểm tra đã chạy

- Chạy thử statusline với input 65% / 30% / `{}`: đúng, không lỗi.

## Việc còn lại / bước tiếp theo

- Chưa làm: tắt MCP không dùng cho project (Gmail, Drive, Claude Docs, codebase-memory); rút gọn output của hook `--all`.
- Nguồn ingest kế tiếp: xem handoff `2026-09-23-1432-fixed-income-during-part-two-complete.md`.
