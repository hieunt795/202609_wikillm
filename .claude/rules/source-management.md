---
paths:
  - "01_sources/**"
  - "03_state/**"
  - "02_wiki/index.md"
---

# Source management

Bổ sung cho quy tắc bắt buộc 1 và 2 của `CLAUDE.md`; luật đầy đủ ở `00_schema.md` §10.

- Nguồn mới phải được đăng ký trong `03_state/_sources_manifest.md` ngay lượt đầu.
- Mỗi nguồn dài có đúng một file `03_state/<source-id>.md`; file này giữ bản đồ chunk và các mục `bỏ qua:`; tiến độ do `--coverage` tính.
- Không dựng lại trạng thái hiện tại từ `log.md` khi state hoặc manifest đã có dữ liệu chuyên trách.
- Dùng `python .claude/hooks/validate_wiki_page.py --verify-sources` để kiểm integrity nguồn.
