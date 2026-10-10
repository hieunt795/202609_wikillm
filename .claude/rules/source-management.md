---
paths:
  - "01_sources/**"
  - "03_state/**"
  - "02_wiki/index.md"
---

# Source management

Bổ sung cho quy tắc bắt buộc 1, 2 và 6 của `CLAUDE.md`; luật đầy đủ ở `00_schema.md` §10.

- Nguồn mới phải được đăng ký trong `03_state/_sources_manifest.md` ngay lượt đầu.
- Mỗi nguồn dài có đúng một file `03_state/<source-id>.md`; state là nguồn sự thật về tiến độ ingest.
- Không dựng lại trạng thái hiện tại từ `log.md` khi state hoặc manifest đã có dữ liệu chuyên trách.
- Dùng `python .claude/hooks/validate_wiki_page.py --verify-sources` để kiểm integrity nguồn.
