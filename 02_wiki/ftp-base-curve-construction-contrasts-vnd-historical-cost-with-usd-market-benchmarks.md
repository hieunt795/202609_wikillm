---
title: ftp-base-curve-construction-contrasts-vnd-historical-cost-with-usd-market-benchmarks
type: concept
tags: [alm, ftp, base-curve, yield-curve, sofr, irs, vnd, usd]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-26
---

Đường cong lãi suất FTP cơ sở (Base curve) phản ánh chi phí vốn mà ngân hàng phải bỏ ra trên các kỳ hạn khác nhau để tài trợ cho hoạt động kinh doanh trên Thị trường 1 (vab_ftp_methodology, Điều 4.2.1, d.241–244). Do cấu trúc thị trường tài chính tại Việt Nam có sự phân hóa sâu sắc giữa đồng nội tệ và ngoại tệ, Trung tâm Điều chuyển Vốn Nội bộ (CFU) áp dụng hai phương pháp luận hoàn toàn khác biệt để xây dựng đường cong cơ sở cho VND và USD (vab_ftp_methodology, Điều 4.2.1, d.247–276).

Đường cong cơ sở đối với VND được xây dựng dựa trên chi phí huy động bình quân thực tế toàn hàng từ các khoản tiền gửi có kỳ hạn tiêu chuẩn phát sinh trong 3 tháng liền kề trước thời điểm tính toán (vab_ftp_methodology, Điều 4.2.1, d.249). Lãi suất bình quân cho từng kỳ hạn tiêu chuẩn $i$ được tính theo phương pháp bình quân gia quyền số dư phát sinh:
$$\bar{r}_{VND, i} = \frac{\sum (SD_j \times LS_j)}{\sum SD_j}$$
Trong đó $SD_j$ là số dư huy động của khoản tiền gửi $j$ và $LS_j$ là lãi suất huy động thực tế của khoản tiền gửi đó (vab_ftp_methodology, Điều 4.2.1, d.261–263). Việc sử dụng chi phí huy động lịch sử thực tế thay vì đường cong lãi suất liên ngân hàng VNIBOR xuất phát từ thực trạng thị trường liên ngân hàng VND thường thiếu thanh khoản ở các kỳ hạn trung và dài hạn trên 3 tháng (vab_ftp_methodology, Điều 4.2.1, d.249).

Trái ngược với VND, đường cong cơ sở đối với USD được xây dựng hoàn toàn dựa trên các lãi suất tham chiếu giao dịch trên thị trường tài chính quốc tế (vab_ftp_methodology, Điều 4.2.1, d.266). Đối với kỳ hạn ngắn hạn từ 1 năm trở xuống, ngân hàng sử dụng bình quân không trọng số trong 3 tháng liền kề của các lãi suất chuẩn như SOFR (Secured Overnight Financing Rate), SIBOR hoặc LIBOR (vab_ftp_methodology, Điều 4.2.1, d.268–270). Đối với kỳ hạn trung và dài hạn trên 1 năm, CFU sử dụng lãi suất giao dịch hoán đổi lãi suất USD (Interest Rate Swap — IRS) bình quân không trọng số 3 tháng từ hệ thống Thomson Reuters hoặc các công cụ thị trường tương đương (vab_ftp_methodology, Điều 4.2.1, d.271–276). Lãi suất cơ sở của các loại ngoại tệ khác cũng được quy đổi và tham chiếu theo khung USD này (vab_ftp_methodology, Điều 4.2.1, d.279).

Hội đồng ALCO rà soát và cập nhật đường cong cơ sở định kỳ hàng quý nhằm đảm bảo chi phí vốn nội bộ bám sát sự dịch chuyển của mặt bằng lãi suất huy động và thị trường quốc tế (vab_ftp_methodology, Điều 4.4, d.523). Cơ sở định giá này là nền tảng đầu vào để hoàn thiện bảng biểu giá vốn theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] và phục vụ quản trị rủi ro tập trung theo [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]].
