# Handoff 2026-09-25 12:37 — review-node unit-of-account

## Kết quả
- `/review-node` trang `unit-of-account-in-the-balance-of-payments`: sửa đoạn 2 (bỏ cảnh báo "đọc sai chiều", đối chiếu số liệu tài khoá/tiền tệ — không có trong d.3508) và bỏ câu cuối về hai bút toán lệch (không có trong d.3510; d.3467 quy sai số cho nguồn dữ liệu khác nhau). Đặt `reviewed: 2026-09-25`, `reviewed_by: model`; trang vẫn `draft`.
- Bỏ link tới `double-entry-accounting-in-the-balance-of-payments` theo câu bị xoá; trang đích còn 9 backlink.
- `_inbox.md`: đánh dấu mục unit-of-account đã xử lý; thêm mục `exchange-rate` dòng 13 mắc cùng claim không nguồn.

## Kiểm tra
- `validate_wiki_page.py --all`: 778 trang, 0 vấn đề, 0 mồ côi.

## Việc còn lại
- `/review-node`: `exchange-rate` (mục inbox mới), `primary-liquidity-injection-…`, trang analysis 8 kênh, hub `quasi-fiscal-operations`.
- 6 trang `draft` trong ngày cần lint + `/promote`.
- Các việc từ handoff 11:55, 11:46, 10:03 giữ nguyên.

## Blocker
Không có. Chưa commit.
