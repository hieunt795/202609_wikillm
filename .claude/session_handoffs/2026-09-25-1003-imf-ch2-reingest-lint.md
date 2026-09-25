# Handoff 2026-09-25 10:03 — ingest lại IMF Ch.2 (B1–B2), review, lint 766

## Kết quả
- Ingest lại `imf_macro_accounting` Ch.2 ở chế độ đối chiếu + lấp gap, xong B1 (d.607–934) và B2 (d.935–1058). Có 16 trang mới; 7 trang bị sửa claim và về `draft`; khoảng 20 trang chỉ thêm link hoặc locator.
- Review-node chạy 2 lượt, mỗi lượt 5 trang. Lượt đầu lấy hàng đợi mặc định; lượt 1/5 lấy từ luồng ingest lại Ch.2. Đã sửa claim ở `reserve-money`, `reserve-assets-…-flows-not-stocks` và `cpi`.
- Lint 766 trang; báo cáo ở `Claude outputs/lint-2026-09-25-766.md` (gitignored). Kết quả xử lý lint:
  - chuẩn hoá `title` = tên file cho 29 trang;
  - đổi 5 trang Ch.5 từ `analysis` sang `concept`;
  - đổi tên trang Ba Lan thành `to-what-extent-was-polands-early-transition-output-decline-overstated`;
  - tạo `broad-money` (draft) và `velocity-of-money` (stub);
  - xoá hết 16 mục inbox;
  - ghi 2 quyết định mới vào `decisions.md` (ngoại lệ stale, quy ước title).

## Kiểm tra
- `validate_wiki_page.py --all`: 768 trang, 0 vấn đề, 0 mồ côi.
- `--verify-sources`: 182 file khớp bản kê. Có 1 file chưa kê: `01_sources/Clippings/Term premia models and some stylised facts.md`. Người dùng chốt chưa xử lý file này.

## Việc còn lại
- Ingest lại Ch.2 **B3** (d.1059–1241) và **B4** (d.1524–1650), theo plan `~/.claude/plans/o-c-la-i-ta-i-li-u-mossy-hippo.md`. Khi làm cần:
  - kiểm câu d.1204 ở `transition-statistics-understate-private-sector-growth` và câu d.1158 ở `inertial-inflation-persists-…`;
  - xử lý 2 conflict Ba Lan (d.1609 so với Table 2.3 d.1394; d.1206 so với d.1404).
- Review-node 17 trang còn lại của luồng Ch.2, gồm `intermediate-consumption`, `compensation-of-employees`, `wholesale-price-index`, `paasche-price-index`, `nominal-gdp`… Làm thêm 3 trang Ch.6 chưa review.
- Nợ stub 14 trang: nâng qua `/research`, cần người dùng duyệt đề xuất. Ưu tiên `interbank-market`, `money-supply`, `sterilization`, `foreign-exchange-reserves` và `deposit-insurance`.
- 4 trang `tata_bank_alm` gắn `type: analysis` dù chỉ một nguồn: cần đọc thân bài để chọn `concept` hay `case`.
- Có 28 trang đã review đủ điều kiện `stable`, chờ người dùng duyệt `/promote`.
- Hook chưa bắt được `title` viết Title Case; nên siết phép so khi sửa hook lần tới.

## Blocker
Không có.
