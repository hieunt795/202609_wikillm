# Ingest Tài liệu FTP — Hoàn tất 100% (2026-09-26)

## Kết quả Ingest Lượt Cuối (Phụ lục 01–06 & Mẫu biểu, d.1256–2118)
- Ingest hoàn tất **Phụ lục 01–06 và Hệ thống Biểu mẫu MB01–MB07** của nguồn dài `vab_ftp_methodology` (dòng 1256–2118).
- **Chính thức hoàn tất 100% toàn bộ tài liệu `VAB - Phương pháp luận FTP.md`** (2.118 dòng / 243 KB).
- **3 trang concept mới**:
  1. `term-liquidity-premium-matrix-calibrates-two-dimensional-floating-rate-spreads`: Ma trận phần bù thanh khoản kỳ hạn 2 chiều (kỳ tái định giá x kỳ đáo hạn) lượng hóa spread cho hợp đồng cho vay thả nổi và cơ chế nội suy song tuyến tính ALCO.
  2. `two-tier-ftp-operational-workflows-govern-market-1-and-market-2-cycles`: Quy trình vận hành FTP hai tầng: 9 bước Thị trường 1 chu kỳ quý/tháng và 9 bước Thị trường 2 tác nghiệp hàng ngày từ 9h-10h sáng.
  3. `interbank-tenor-ladder-and-deal-ticket-standardization-enforce-internal-treasury-transfers`: Chuẩn hóa 21 thang kỳ hạn từ Overnight đến 120M, quy cách lập Phiếu giao dịch mua bán vốn MB06 và Báo cáo hoạt động Desk MM/FX/Bond MB07.
- **2 trang cập nhật**:
  1. `matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch`: Bổ sung liên kết và cơ chế tra cứu ma trận 2 chiều Phụ lục 02.
  2. `treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers`: Bổ sung chuẩn hóa quy trình điều chuyển hàng ngày và biểu mẫu MB06/MB07.

---

## Tổng kết Chiến dịch Ingest Toàn bộ Tài liệu FTP
Toàn bộ 2 tài liệu FTP trong thư mục `01_sources/` đã được tiếp nhận trọn vẹn 100%:
1. **`ftp_transmission_analysis.md.md`** (189 dòng / 16 KB): Hoàn tất 100% trong 1 lượt (3 trang mới, 3 trang cập nhật).
2. **`VAB - Phương pháp luận FTP.md`** (2.118 dòng / 243 KB): Hoàn tất 100% qua 4 chunks (18 trang mới, 11 lượt trang cập nhật).
- **Tổng số trang tạo mới**: **21 trang concept chuẩn atomic profile wiki**.
- **Tổng số trang cập nhật làm giàu**: **11 trang concept hiện hữu**.
- **Chuyên mục ALM & FTP trên `02_wiki/index.md`**: Đã mở rộng lên 28 trang liên kết chuyên sâu, bao phủ từ lý thuyết ngân hàng hiện đại (Choudhry, Basel III LCR/NSFR, RAROC) đến cẩm nang thực hành chi tiết tại NHTMCP Việt Nam (CFU, VOF/COF, VNIBOR, Thông tư 22/41, ma trận 2 chiều, quy trình tác nghiệp 2 tầng).

---

## Trạng thái Hệ thống & Kiểm tra
- `validate_wiki_page.py --all`: **811 trang quét, 0 lỗi định dạng, 0 heading trong thân trang, 0 link chết, 0 mồ côi mới** (giữ nguyên 4 trang mồ côi nợ cũ từ Clippings).
- `03_state/vab_ftp_methodology.md`: Đã đánh dấu `[x]` toàn bộ 4/4 chunk, ghi nhận hoàn tất 100%.
- `03_state/_sources_manifest.md`: Đầy đủ mã SHA-256 và kích thước cho cả 2 nguồn.
- `02_wiki/index.md`: Bảng `## Sources` cập nhật cả 2 nguồn đạt `**Hoàn tất 100%**`; danh mục chuyên đề cập nhật đủ 28 links.
- `log.md`: Đã ghi nhận nhật ký chuẩn 3 dòng với timestamp `[2026-09-26:10-14-43]`.
