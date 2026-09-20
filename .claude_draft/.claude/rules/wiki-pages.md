---
paths:
  - "02_wiki/*.md"
---

# Wiki pages

- Tên file là kebab-case của `title`; `title` viết bằng tiếng Anh và thân bài viết bằng tiếng Việt.
- Mỗi trang trình bày một ý tưởng atomic, độc lập; thân bài không có heading. `index.md` được miễn quy tắc thân bài atomic.
- Wikilink phải nằm trong câu và thể hiện lý do liên hệ; `tags` chỉ phục vụ phân loại, không thay thế liên kết.
- Claim lấy từ nguồn dài phải có locator theo `00_schema.md`.
- Chỉ nâng `last_updated` khi claim thay đổi; chỉ thêm link, locator hoặc metadata không đủ để nâng ngày.
- Không tự promote trang hoặc ghi đè `reviewed_by: user`.
- Data model, taxonomy và lifecycle chi tiết lấy từ `00_schema.md`; không suy diễn thêm từ rule này.
