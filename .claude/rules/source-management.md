---
paths:
  - "01_sources/**"
  - "03_state/**"
  - "02_wiki/index.md"
---

# Source management

- `01_sources/` tuyệt đối chỉ đọc: không thêm, sửa, đổi tên, xoá hoặc đổi line ending.
- Nguồn mới phải được đăng ký trong `03_state/_sources_manifest.md` ngay lượt đầu.
- Mỗi nguồn dài có đúng một file `03_state/<source-id>.md`; state là nguồn sự thật về tiến độ ingest.
- Không dựng lại trạng thái hiện tại từ `log.md` khi state hoặc manifest đã có dữ liệu chuyên trách.
- Mỗi lượt ingest cập nhật đồng bộ state và mục Sources trong `02_wiki/index.md`, kể cả khi không tạo trang mới.
- Dùng `python .claude/hooks/validate_wiki_page.py --verify-sources` để kiểm integrity nguồn.
- Khi hai nguồn mâu thuẫn, ghi `⚠️ Conflict` kèm cả hai claim và locator rồi chờ người dùng; không tự hòa giải.
