# Handoff — đơn giản hoá ký hiệu trong `CLAUDE.md`

## Kết quả

- `CLAUDE.md` chỉ còn một ký hiệu `§N` (định nghĩa ở đầu file). Luật con viết "§7 luật 5", "§7 luật 6"; bỏ `§7.5`, `§Sources`, `≥`, `·`; `→` chỉ còn ở `draft → stable`.
- Đoạn con trỏ file thành bảng "Cần gì / File". Bullet chú thích vị trí tách làm hai. Câu về hook "xem thêm" viết lại rõ chủ thể.
- Thêm ba dữ kiện: `01_sources/` và `Claude outputs/` không nằm trong git; exit 2 của hook phải xử lý ngay; không có lệnh kiểm riêng một trang.
- Mục "Công cụ ghi câu hỏi theo yêu cầu" gộp thành một bullet trong "Ghi chú vận hành".
- Không đổi luật nào; quy tắc bắt buộc 1–6 giữ số; tên các heading còn lại giữ nguyên.
- `log.md`: 1 mục `schema` [2026-10-10:14-46-45]. Chưa commit.

## Kiểm tra đã chạy

- `--all`: 790 trang, 0 lỗi, 4 trang mồ côi (có sẵn).
- Grep `CLAUDE.md`: không còn `§7.x`, `§Sources`, `≥`, `·`; mọi `§N` nằm trong §1–§13.

## Việc còn lại

- `CLAUDE.md` tăng từ 901 lên 999 từ (`wc -w`), vượt mốc khoảng 950 từ đặt trong plan. Muốn rút thì cắt câu mở đầu mục "Khởi động" (trùng `00_schema.md` §13).
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; đổi đồng bộ là một batch riêng nếu muốn.
- Docstring `.claude/hooks/validate_wiki_page.py` dòng 20, 27, 31 hỏng chữ / còn "luat cung 1".
- `README.md:27` và `.claude/README.md` thiếu skill `research`.
- Các việc tồn từ handoff 2026-10-10-1427 và 2026-10-09 không đổi.

## Bước tiếp theo

- Người dùng xem `git diff` rồi quyết định commit.
