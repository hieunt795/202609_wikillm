# Handoff 2026-09-25 11:46 — research quasi-fiscal (công cụ QFO + hub)

## Kết quả
- Chạy `/research` trên 8 trang: hub `quasi-fiscal-operations`, các trang trợ cấp/bảo lãnh, `implicit-subsidies`, `state-owned-enterprises`, trang analysis 8 kênh và `primary-liquidity-injection-…`.
- Thêm 6 claim mới trên 3 trang. Hai trang `quasi-fiscal-operations` và `credit-subsidies` chuyển từ `stable` về `draft`.
- Chèn 4 link giữa các trang trợ cấp và các trang cơ chế.
- Ghi 1 mục `_inbox.md`: claim "NDC/NCG policy-controlled" ở `primary-liquidity-injection-…` lệch imf Ch.5 d.4653.
- Báo cáo: `Claude outputs/research-2026-09-25-quasi-fiscal.md`.

## Kiểm tra
- `validate_wiki_page.py --all`: 778 trang, 0 vấn đề, 0 mồ côi.

## Việc còn lại
- Chạy `/review-node` cho `primary-liquidity-injection-…` (mục inbox + không có chú thích bindseil), trang analysis 8 kênh (thiếu locator; 2 chỗ lệch khung hiểu nêu trong báo cáo) và hub (câu "không phải ý định lừa dối" không kèm nguồn).
- Research lượt sau: cơ chế trợ cấp tỷ giá (Ch.4 Box 4.8), và cụm con 8 trang cơ chế.
- Hai trang về `draft` cần qua lint + `/promote` để lên lại `stable`.
- Các việc còn lại từ handoff 2026-09-25-1003 vẫn giữ nguyên.

## Blocker
Không có. Chưa commit.
