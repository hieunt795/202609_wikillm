---
paths:
  - "02_wiki/*.md"
---

# Wiki pages

Lời nhắc những điều dễ sai nhất khi ghi trang; luật đầy đủ ở `00_schema.md` mục ghi trong ngoặc.

- Tên file là kebab-case của `title`; `title` viết bằng tiếng Anh và thân bài viết bằng tiếng Việt (§3).
- Mỗi trang trình bày một ý tưởng atomic, độc lập; thân bài không có heading, cần heading nghĩa là phải tách trang (§5, §7). `index.md` được miễn quy tắc thân bài atomic.
- `[[wikilink]]` nằm trong câu văn kèm lý do liên hệ; không mở đầu bullet, không dồn thành danh sách "xem thêm" (§7). Hook báo lỗi danh sách link; cách sửa là lồng từng link vào câu diễn giải.
- `tags` chỉ là chỉ mục lọc, không thay thế liên kết (§6).
- Link mới viết thì gắn loại quan hệ ở frontmatter của trang chứa link: `part_of`, `has_part`, `governs`, `governed_by`, `drives`, `driven_by`, `contrasts`, `analogous`, `related`, mỗi field một dòng inline list. Trang đích phải có `[[wikilink]]` trong thân bài; loại lấy từ câu chứa link (§6).
- Viết lại bằng lời mình, không sao chép nguyên văn nguồn (§7). Áp skill `writing-style` profile wiki.
- `sources:` dùng source id, bắt buộc inline list `[id1, id2]`; hook đọc theo dòng, không hiểu YAML nhiều dòng (§1, §10).
- Claim từ nguồn dài kèm chú thích `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7 luật 5). Luật áp cho trang có `last_updated` từ 2026-09-14 trở đi.
- Chỉ nâng `last_updated` khi claim thay đổi; chỉ thêm link, chú thích, field quan hệ hoặc metadata thì không nâng (§7 luật 5).
- Không ghi `status: stable`/`stale` và không ghi đè `reviewed_by: user` (§9).
