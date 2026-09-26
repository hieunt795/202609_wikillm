# Ingest Tài liệu FTP — Chunk 3 Complete (2026-09-26)

## Kết quả
- Ingest hoàn tất **Chunk 3** của nguồn dài `vab_ftp_methodology` (Phần B: Điều 7–15, dòng 984–1255: Giao dịch còn lại, Biến động giá, FTP Thị trường 2, Khối QL&KDV & Khung báo cáo).
- **Khép lại 100% Phần B (Quy định chi tiết và phương pháp luận cốt lõi)** của tài liệu FTP VietABank & EY (dòng 1–1255).
- **5 trang concept mới**:
  1. `interbank-market-2-ftp-curve-construction-relies-on-peer-quotes-and-vnibor`: Xây dựng đường cong FTP Thị trường 2 qua bình quân mid-rate nhóm NHTMCP cùng Peer (lọc ngoại lai $\pm 15\%$, nội suy biên độ ALCO) và tham chiếu VNIBOR 1 tuần.
  2. `treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers`: Cơ chế điều hòa vốn nội bộ cho Khối Treasury giữa mô hình từng bàn giao dịch (Desk-level) và bù trừ trạng thái ròng (Net-portfolio) gắn với hạn mức khả năng chi trả 30 ngày.
  3. `contractual-amendment-ftp-repricing-rules-govern-loan-and-deposit-restructuring`: Bộ quy tắc tái định giá FTP khi phát sinh thay đổi hợp đồng (tần suất định giá, fixed/floating, tái lập dòng tiền WAT, đổi đồng tiền nợ, ngưỡng can thiệp ALCO $\pm 0{,}2\%$).
  4. `non-earning-asset-and-nostro-vostro-ftp-treatment-precludes-double-counting`: Nguyên tắc xử lý FTP cho tiền mặt tồn quỹ, Nostro/Vostro, cổ phiếu đầu tư chiến lược dài hạn và tài sản khác, loại trừ triệt để nguy cơ tính trùng chi phí thanh khoản và vốn tự có.
  5. `ftp-reporting-architecture-synthesizes-multi-dimensional-nii-and-nim-performance`: Khung kiến trúc báo cáo FTP đo lường và phân tích hiệu quả NII/NIM đa chiều và hai phương án chu kỳ vận hành cắt sổ toàn hàng.
- **3 trang cập nhật**:
  1. `vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu`: Bổ sung cơ chế điều hòa vốn giữa CFU và Khối Treasury, vai trò hạn mức thanh khoản 30 ngày và khung báo cáo NII/NIM.
  2. `matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions`: Cập nhật cơ chế tương tác giữa Treasury và bàn điều chuyển vốn trung tâm CFU.
  3. `vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing`: Cập nhật cơ chế tái định giá FTP khi hợp đồng thay đổi điều kiện lãi suất hoặc dòng tiền.
- **Hệ thống wiki & index**:
  - `03_state/vab_ftp_methodology.md`: Đánh dấu Chunk 3 `[x]` (d.984–1255).
  - `02_wiki/index.md`: Cập nhật bảng `## Sources` (Điều 1–15 xong) và bổ sung 5 trang mới vào chuyên mục **Quản trị Tài sản - Nợ (ALM) & Định giá Điều chuyển Vốn Nội bộ (FTP)** (tổng cộng 25 trang liên kết).
  - `log.md`: Đã append mục log chuẩn 3 dòng thời gian `[2026-09-26:10-09-24]`.

## Kiểm tra
- `validate_wiki_page.py --all`: 808 trang quét, 0 lỗi định dạng/frontmatter/link/heading/nguồn. 0 trang mồ côi mới (vẫn giữ nguyên 4 trang mồ côi nợ cũ từ Clippings).

## Việc còn lại / bước tiếp
- Tiếp tục `/ingest` nguồn dài `vab_ftp_methodology`:
  - **Phụ lục 01–04 (d.1256–1742)**: Giải thích thuật ngữ chi tiết, minh họa tính toán các cấu phần Thị trường 1, cấu phần đặc biệt và khung mẫu báo cáo FTP.
  - **Phụ lục 05–06 & Mẫu biểu (d.1743–2118)**: Lưu đồ quy trình vận hành Thị trường 1/Thị trường 2 và hệ thống mẫu biểu MB01–MB07.
