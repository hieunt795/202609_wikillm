# Handoff 2026-09-25 11:55 — research cơ chế trợ cấp tỷ giá

## Kết quả
- Chạy `/research` trên 8 trang quanh `exchange-rate-subsidies` (cụm trợ cấp + cụm tỷ giá).
- Thêm 8 claim trên 4 trang, cả 4 chuyển `stable` → `draft`: `exchange-rate-subsidies`, `exchange-rate-appropriateness-…`, `polands-exchange-rate-path-…`, `unit-of-account-in-the-balance-of-payments`.
- Chèn 1 link: hub `exchange-rate` → `exchange-rate-subsidies`.
- Dùng Table 4.6 (d.4279–4280) từ chunk đã ghi "bỏ qua bảng"; người dùng đã duyệt.
- Ghi 1 mục `_inbox.md`: câu không nguồn ở `unit-of-account-…` (hai bút toán lệch nhau).
- Báo cáo: `Claude outputs/research-2026-09-25-exchange-rate-subsidies.md`.

## Kiểm tra
- `validate_wiki_page.py --all`: 778 trang, 0 vấn đề, 0 mồ côi.

## Việc còn lại
- `/review-node`: `unit-of-account-…` (mục inbox mới), cộng 3 trang từ handoff 11:46 (primary-liquidity, analysis 8 kênh, hub quasi-fiscal).
- 6 trang về `draft` trong ngày (2 từ lượt quasi-fiscal, 4 từ lượt này) cần lint + `/promote`.
- Gap: cơ chế trợ cấp tỷ giá, đa tỷ giá, thị trường song song, hợp nhất tỷ giá cần nguồn khác ngoài IMF.
- Các việc còn lại từ handoff 2026-09-25-1146 và 1003 giữ nguyên.

## Blocker
Không có. Chưa commit.
