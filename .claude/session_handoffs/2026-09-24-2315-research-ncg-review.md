# 2026-09-24 23:15 — research net-credit-to-government + review-node 5 trang

## Kết quả
- `/research net-credit-to-government`: cluster 14 trang (người dùng yêu cầu vượt trần 10). 6 claim mới ở 4 trang (NCG, government-deposits, high-government-financing-needs-…, government-borrowing-…), 6 link. government-deposits chuyển stable → draft. Báo cáo: `Claude outputs/research-2026-09-24-net-credit-to-government.md`.
- `/review-node` 5 trang: net-credit-to-government, net-domestic-credit, government-borrowing-…, high-government-financing-needs-…, fiscal-imbalance-…. Cả 5 đã sửa claim sai và đặt `reviewed_by: model`. Các claim sai phần lớn nằm trong đoạn thêm ở lượt research OINs trước đó (chưa commit).

## Kiểm tra
- `validate_wiki_page.py --all`: 745 trang, 0 vấn đề, 0 mồ côi (chạy sau cả hai op).
- log.md có 2 mục: research 23-10-20, review 23-14-41.

## Còn lại
- `_inbox.md`: 5 mục ngày 2026-09-24 về research NCG đã được lượt review này xử lý, chờ lint xoá khi triage. 1 mục mới cho credit-to-the-private-sector (sai tên mục ở chú thích d.5142).
- ~~Ký hiệu chưa thống nhất~~ → đã xử lý 23:25 (log research "thống nhất ký hiệu NCG"). money-supply-equals-… chuyển stable → draft, cần promote lại. Chưa xử lý: $\Delta NDC_p$ so với $CPS$ (phạm vi CPS* rộng hơn khu vực tư, chưa quy đổi).
- Case Ba Lan Ch.5 d.5147–5177 chưa `[x]`.
- Toàn bộ thay đổi chưa commit (gồm cả thay đổi của các phiên trước trong ngày).

## Bổ sung 23:41 — research bảng cân đối MA
- Cluster 17 trang; 7 claim ở 4 trang, 7 link, 1 trang analysis mới `the-policy-anchor-decides-whether-net-foreign-assets-are-autonomous-on-the-central-bank-balance-sheet` (đã vào index). Ba trang typical, central-bank và autonomous-factors chuyển stable → draft. `--all` sạch (746 trang).
- 7 mục _inbox.md chờ /review-node: analytical (OIN* ngược chiều), typical, monetary-accounts-net, consolidation, claims-on-DMB, sterilization-capacity (đọc sai Bindseil), central-bank (lệch dòng).

## Bổ sung 23:46 — review 5 trang bảng cân đối MA
- Đã sửa và đặt reviewed: analytical, sterilization-capacity, claims-on-DMB, monetary-accounts-net, consolidation. Ba trang sterilization-capacity, monetary-accounts-net và consolidation chuyển stable → draft. `--all` sạch.

## Bổ sung 23:51 — review 4 trang còn lại
- the-typical-…, credit-to-the-private-sector, central-bank đã sửa claim; sterilization-offsets-… chỉ sửa chú thích. Cả 4 đặt reviewed_by: model. `--all` sạch. Hàng chờ review từ inbox hôm nay đã hết.

## Bước tiếp theo
- Lint: sửa title Title Case và type của 4 trang IMF, triage inbox (nhiều mục ngày 2026-09-24 đã xử lý).
- Review git diff rồi commit.
- Review git diff rồi commit.
- `/review-node credit-to-the-private-sector`.
