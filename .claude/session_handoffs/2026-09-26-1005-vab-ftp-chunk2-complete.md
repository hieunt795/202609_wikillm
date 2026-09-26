# Ingest Tài liệu FTP — Chunk 2 Complete (2026-09-26)

## Kết quả
- Ingest hoàn tất **Chunk 2** của nguồn dài `vab_ftp_methodology` (Phần B: Điều 5 & Điều 6, dòng 531–983: Phương pháp xác định cấu phần FTP đặc biệt & Cơ chế FTP giao dịch Thị trường 1).
- **5 trang concept mới**:
  1. `ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital`: Phân bổ chi phí vốn chủ sở hữu theo thặng dư vốn tự có (VOF bình quân) và mô hình RAROC dựa trên WAT danh mục và $(ROE\% - COF\%)$.
  2. `contingent-liquidity-charge-prices-undrawn-credit-commitments`: Định giá phần bù rủi ro thanh khoản tiềm tàng cho hạn mức cam kết chưa sử dụng theo BIS 2011, CCF Thông tư 41/2016/TT-NHNN và chi phí duy trì TSTK.
  3. `deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles`: Quy tắc VOF cho tiền gửi trả cuối kỳ, gửi góp bù spread, CASA theo Redemption Curve và sàn rút 15% Thông tư 22/2019/TT-NHNN, ký quỹ và GTCG.
  4. `matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch`: Bóc tách phần bù thanh khoản kỳ hạn trong định giá COF cho khoản vay thả nổi và trả nợ định kỳ theo kỳ hạn hiệu lực WAT.
  5. `promotional-and-behavioral-loan-ftp-pricing-decomposes-hybrid-cash-flows`: Cơ chế định giá COF cho các gói vay ưu đãi bóc tách cấu phần và mô hình hành vi xử lý quyền chọn tất toán trước hạn.
- **4 trang cập nhật**:
  1. `contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons`: Tích hợp công thức BIS 2011, CCF TT41 và liên kết trang chuyên biệt (`stable → draft`).
  2. `ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc`: Tích hợp công thức chi phí VCSH theo RAROC và WAT danh mục.
  3. `funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads`: Bổ sung liên kết và cơ chế bóc tách phần bù thanh khoản kỳ hạn cho hợp đồng thả nổi.
  4. `vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing`: Bổ sung liên kết tới các quy tắc định giá sản phẩm và phần bù thanh khoản kỳ hạn.
- **Hệ thống wiki & index**:
  - `03_state/vab_ftp_methodology.md`: Đánh dấu Chunk 2 `[x]` (d.531–983).
  - `02_wiki/index.md`: Cập nhật bảng `## Sources` và bổ sung chuyên mục lớn **Quản trị Tài sản - Nợ (ALM) & Định giá Điều chuyển Vốn Nội bộ (FTP)** gom toàn bộ 20 trang liên quan.
  - `log.md`: Đã append mục log chuẩn 3 dòng thời gian `[2026-09-26:10-04-30]`.

## Kiểm tra
- `validate_wiki_page.py --all`: 803 trang quét, 0 lỗi định dạng/frontmatter/link/heading/nguồn. Không phát sinh bất kỳ trang mồ côi mới nào (vẫn giữ nguyên 4 trang mồ côi nợ cũ từ Clippings).

## Việc còn lại / bước tiếp
- Tiếp tục `/ingest` nguồn dài `vab_ftp_methodology`:
  - **Chunk 3 (d.984–1050)**: Phần B: Điều 7 (Cơ chế FTP các giao dịch còn lại: Tiền mặt, Nostro/Vostro, Cổ phiếu đầu tư dài hạn, Tài sản khác) & Điều 8 (Trường hợp thay đổi giá mua bán vốn: thay đổi tần suất định giá, điều chỉnh ALCO, tái tục).
  - **Chunk 4 (d.1051–1255)**: Điều 9–15 (FTP Thị trường 2, Khối QL&KDV, Phát hành GTCG, Khung báo cáo & Quy trình).
  - **Phụ lục 01–06 (d.1256–2118)**: Minh họa tính toán, mẫu biểu MB01–MB07 và lưu đồ quy trình.
