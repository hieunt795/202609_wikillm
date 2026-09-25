# Handoff 2026-09-25 12:46 — review-node 4 trang (quasi-fiscal + exchange-rate)

## Kết quả
- `exchange-rate`: bỏ cảnh báo "đọc sai chiều" (không có trong d.3508), link chế độ tỷ giá dẫn d.3708; câu clippings thu về case Nhật Bản, thêm d.22–24. `stable` → `draft`, `last_updated` 2026-09-25.
- `primary-liquidity-injection-…`: sửa claim policy-controlled theo d.4653; link autonomous-factors dẫn Bindseil d.591; ghi rõ "primary liquidity injection" là thuật ngữ wiki; câu nhân tiền dẫn d.4707, d.4711–4719.
- `quasi-fiscal-operations`: bỏ câu "không phải ý định lừa dối"; câu PSBR dẫn d.2099–2107.
- Trang analysis 8 kênh: viết lại claim từng kênh kèm locator đã đối chiếu; giới hạn phạm vi vào cho vay ưu đãi; bỏ seigniorage, "bù trừ tự động", "dự trữ cạn thì dừng", RM↑50; ví dụ r = 10% ghi là minh hoạ; kết luận PSBR sửa theo Box 3.7 + d.2107.
- Cả 4 trang `reviewed: 2026-09-25`, `reviewed_by: model`.
- `_inbox.md`: đánh dấu 2 mục đã xử lý; thêm 4 mục mới: current-account-monitoring (claim d.3508), quasi-fiscal-spending (d.3105–3125 sai), money-multiplier-cascade (d.4777–4780 sai), quasi-fiscal-losses (d.4772–4780 sai mục).

## Kiểm tra
- `validate_wiki_page.py --all`: 778 trang, 0 vấn đề, 0 mồ côi.
- `_inbox.md` đã được đổi lại về LF sau khi Python ghi CRLF.

## Việc còn lại
- `/review-node` cho 4 trang trong inbox mới.
- 7 trang `draft` trong ngày cần lint + `/promote` (exchange-rate thêm vào danh sách).
- Các việc từ handoff 12:37, 11:55, 11:46, 10:03 giữ nguyên.

## Blocker
Không có. Chưa commit.
