---
paths:
  - "log.md"
  - "decisions.md"
  - "_inbox.md"
  - "Claude outputs/**"
---

# Project records

- `log.md` lưu kết quả operation; `decisions.md` lưu quyết định và lý do.
- `_inbox.md` lưu ý tưởng chưa đủ chín; state chuyên trách lưu tiến độ hiện tại.
- `log.md` là append-only. Mỗi operation có thay đổi ghi đúng một mục theo `00_schema.md`.
- `/query` chỉ trả lời, không tạo trang hoặc đổi trạng thái, thì không ghi log.
- `/lint` chỉ tạo báo cáo và triage; không tự sửa wiki.
- Báo cáo lint/audit đi vào `Claude outputs/`, không phải `02_wiki/`.
- Research, audit, draft, log và transcript không phải tri thức đã được chấp nhận.
