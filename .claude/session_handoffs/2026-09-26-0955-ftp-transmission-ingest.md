# Ingest Tài liệu FTP — 2026-09-26

## Kết quả
- Kê khai 2 nguồn tài liệu FTP mới vào `03_state/_sources_manifest.md` và `02_wiki/index.md` §Sources:
  - `ftp_transmission_analysis` (nguồn ngắn, 189 dòng): Ingest trọn vẹn 100%.
  - `vab_ftp_methodology` (nguồn dài, 2.118 dòng): Xong Chunk 1 (d.1–530: Tổng quan, Căn cứ & Phương pháp luận Thị trường 1).
- 8 trang concept mới:
  - Lượt 1 (`ftp_transmission_analysis`): `ftp-transmission-channels-steer-bank-balance-sheet-risks`, `ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc`, `balance-sheet-optimization-models-calibrate-ftp-as-a-control-variable`.
  - Lượt 2 (`vab_ftp_methodology` d.1–530): `vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu`, `vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing`, `ftp-base-curve-construction-contrasts-vnd-historical-cost-with-usd-market-benchmarks`, `regulatory-deposit-insurance-and-statutory-reserves-apportion-into-market-1-cof`, `planned-nim-allocation-determines-ftp-deposit-mobilization-margins`.
- 5 trang cập nhật (`stable → draft`):
  - `funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks`, `regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp`, `matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions`, `funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads`, `ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation`.
- `02_wiki/index.md` đã cập nhật bảng `## Sources` và bổ sung 8 trang mới vào mục FTP.
- `log.md` đã ghi 2 mục log tương ứng.

## Kiểm tra
- `validate_wiki_page.py --all`: 798 trang quét, 0 lỗi định dạng/frontmatter/link/heading/nguồn. (4 trang mồ côi tồn đọng từ các phiên trước của cụm Clippings).

## Việc còn lại / bước tiếp
- Tiếp tục `/ingest` nguồn dài `vab_ftp_methodology`: Chunk 2 (d.531–750: Điều 5 — Phương pháp xác định cấu phần FTP đặc biệt: Cost of Equity, Contingency liquidity, Embedded options).
- Tồn đọng từ phiên trước: Duyệt promote 5 trang đủ điều kiện stable; dedupe dollarization vs currency-substitution; kê file Clippings "Term premia models...".

