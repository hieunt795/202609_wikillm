# Handoff — luồng vận hành vào `00_schema.md` §13, `CLAUDE.md` rút gọn

## Kết quả

- `00_schema.md` thêm §13 "Luồng vận hành": trình tự 8 bước của một phiên + bảng operation 5 cột (Skill · Đọc thêm · Dừng chờ duyệt · Ghi log); nêu thứ tự ràng buộc `CLAUDE.md` → `00_schema.md` → skill. §1–§12 không đổi số.
- `CLAUDE.md`: thêm tiền tố `/init`; bỏ "Sáu operation" và "Trạng thái phiên làm việc", thay bằng "Khởi động" 2 bước (đọc handoff; đọc §13 trước mọi operation); bảng công cụ chia bắt buộc / theo nhu cầu. 1.144 → 901 từ. Quy tắc bắt buộc 1–6 giữ số; quy tắc 4 sửa research chờ duyệt ở Pha 3.
- `query/SKILL.md:8`, `research/SKILL.md:25`: khi chưa ghi trang chỉ đọc §13, không đọc data model §1–§12.
- `README.md` bảng "Đọc từ đâu" sửa theo (hết chữ "Luật cứng").
- `decisions.md` [2026-10-10]; `log.md` 2 mục `schema` (mục sau đính chính mục trước). Chưa commit.

## Kiểm tra đã chạy

- `--all`: 790 trang, 0 lỗi, 4 trang mồ côi (có sẵn).
- Bảng operation chỉ còn ở `00_schema.md`; `CLAUDE.md` không giữ bản sao.
- Các số "quy tắc bắt buộc N" trích trong skill vẫn khớp nội dung.

## Việc còn lại

- Lệch ngoài phạm vi, chưa sửa: `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query; `.claude/README.md` và `README.md` liệt kê skill thiếu `research`; `ingest/SKILL.md:13` ghi "(§1–§12)"; docstring hook còn "luat cung 1"; `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- Các việc tồn từ handoff 2026-10-09 (247 mục chưa phủ, ingest bù) không đổi.

## Bước tiếp theo

- Người dùng xem `git diff` rồi quyết định commit.
- Chạy thử một lượt `/query` để xem bước mồi có dẫn tới đọc §13 không.
