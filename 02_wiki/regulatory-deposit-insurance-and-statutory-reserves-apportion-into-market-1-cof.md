---
title: regulatory-deposit-insurance-and-statutory-reserves-apportion-into-market-1-cof
type: concept
tags: [alm, ftp, cof, deposit-insurance, statutory-reserves, tt22, tt30]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-26
---

Trong hệ thống định giá điều chuyển vốn nội bộ tại các ngân hàng thương mại Việt Nam, chi phí bảo hiểm tiền gửi (BHTG) và chi phí dự trữ bắt buộc (DTBB) được phân bổ tập trung vào giá bán vốn (COF) áp dụng cho các tài sản có, thay vì khấu trừ trực tiếp vào giá mua vốn (VOF) của các đơn vị huy động tiền gửi (vab_ftp_methodology, Điều 4.3.1 & 4.3.2, d.384, d.424). Nguyên tắc này bảo vệ động lực huy động vốn của các chi nhánh mạng lưới, đồng thời buộc các đơn vị kinh doanh sử dụng vốn phải gánh chịu đầy đủ mọi chi phí pháp lý phát sinh để tạo ra nguồn vốn tài trợ (vab_ftp_methodology, Điều 4.1 & 4.3.1, d.196, d.384).

Chi phí bảo hiểm tiền gửi phát sinh từ nghĩa vụ thanh toán định kỳ cho Bảo hiểm tiền gửi Việt Nam theo tỷ lệ 0,15%/năm trên số dư tiền gửi VND của khách hàng cá nhân (vab_ftp_methodology, Điều 4.3.1, d.380). Trung tâm Điều chuyển Vốn Nội bộ (CFU) tính toán tổng chi phí BHTG thực tế phát sinh cuối tháng trong 3 tháng liền kề quy đổi ra 1 năm, sau đó chia cho quy mô danh mục tài sản chịu phí (vab_ftp_methodology, Điều 4.3.1, d.396–400):
$$Chi\ phí\ BHTG\ (\%) = \frac{Tổng\ chi\ phí\ BHTG\ thực\ tế\ 3\ tháng\ \times 4}{Bình\ quân\ Tổng\ tài\ sản\ bị\ tính\ FTP}$$

Chi phí dự trữ bắt buộc phản ánh tổn thất cơ hội vốn do ngân hàng phải gửi một tỷ lệ tiền gửi bắt buộc tại Ngân hàng Nhà nước với mức lãi suất thấp hơn mặt bằng huy động thị trường theo quy định của Thông tư 30/2019/TT-NHNN (vab_ftp_methodology, Điều 2 & Điều 4.3.2, d.133, d.420–424). Khoản chi phí này được lượng hóa theo công thức (vab_ftp_methodology, Điều 4.3.2, d.430):
$$Chi\ phí\ DTBB\ (\%) = \frac{Số\ dư\ DTBB\ bình\ quân \times (VOF\ bình\ quân - Lãi\ suất\ DTBB)}{Bình\ quân\ Tổng\ tài\ sản\ bị\ tính\ FTP}$$
Trong đó $VOF\ bình\ quân$ là lãi suất mua vốn bình quân thực tế của tất cả các kỳ hạn trên Thị trường 1, và $Lãi\ suất\ DTBB$ là lãi suất tiền gửi dự trữ bắt buộc do Ngân hàng Nhà nước trả (vab_ftp_methodology, Điều 4.3.2, d.434).

Mẫu số chung của cả hai công thức phân bổ trên là **Bình quân Tổng tài sản bị tính FTP**, được xác định bằng cách lấy Tổng tài sản trên bảng cân đối trừ đi ba cấu phần đặc thù (vab_ftp_methodology, Điều 4.3.1, d.403–412):
1. **Tài sản thanh khoản cao**: Danh mục đệm thanh khoản nắm giữ theo Phụ lục 3 Thông tư 22/2019/TT-NHNN bị loại trừ vì đã được phân bổ riêng qua cấu phần Phần bù tài sản thanh khoản (Liquidity premium) (vab_ftp_methodology, Điều 4.3.1, d.406–407);
2. **Tài sản ghi nhận cho Khối Nguồn vốn**: Toàn bộ tài sản có giao dịch trên Thị trường 2 (tiền gửi liên ngân hàng, FX, trái phiếu chính phủ) bị loại trừ vì áp dụng cơ chế định giá riêng của Thị trường 2 (vab_ftp_methodology, Điều 4.3.1, d.408–410);
3. **Tài sản có khác**: Tài sản cố định và các tài sản phi tài chính bị loại trừ vì được tài trợ bởi vốn chủ sở hữu (vab_ftp_methodology, Điều 4.3.1, d.411–412).

Cơ chế phân bổ chuẩn xác này hoàn thiện cấu trúc định giá COF theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]], hỗ trợ việc điều phối bảng cân đối kế toán theo [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]] và gắn kết chặt chẽ với các chỉ tiêu an toàn thanh khoản theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]].
