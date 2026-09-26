---
title: planned-nim-allocation-determines-ftp-deposit-mobilization-margins
type: concept
tags: [alm, ftp, margin, nim, planned-nii, alco, budget]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-26
---

Hỗ trợ huy động (Margin) là cấu phần thù lao biên lợi nhuận được Hội đồng ALCO bổ sung vào đường cong FTP mua vốn nhằm tạo động lực kinh doanh cho các đơn vị huy động tiền gửi trên toàn hệ thống ngân hàng (vab_ftp_methodology, Điều 4.2.2, d.284–287). Thay vì áp đặt một mức hỗ trợ tùy ý, Trung tâm Điều chuyển Vốn Nội bộ (CFU) tính toán mức hỗ trợ này dựa trên kế hoạch kinh doanh năm do ban lãnh đạo phê duyệt, thực hiện phân rã thu nhập lãi thuần toàn hàng (NII) thành tỷ lệ NIM mục tiêu cho hoạt động huy động và hoạt động cho vay (vab_ftp_methodology, Điều 4.2.2, d.285, d.296–320).

Quá trình lượng hóa khởi đầu bằng việc xác định chỉ tiêu NII thuần túy từ hoạt động vay gửi theo kế hoạch (vab_ftp_methodology, Điều 4.2.2, d.298–342):
$$NII_{vay\ g\text{ử}i} = NII_{k\text{ế}\ ho\text{ạ}ch} - Chi\ ph\acute{\imath}\ qu\text{ả}n\ l\yacute;_{k\text{ế}\ ho\text{ạ}ch} - Chi\ ph\acute{\imath}\ d\text{ự}\ ph\grave{o}ng\ RRTD_{k\text{ế}\ ho\text{ạ}ch}$$
Trong đó, tổng chi phí quản lý kế hoạch bao gồm các khoản chi phí trực tiếp liên quan đến tiếp thị, quảng cáo và chương trình khuyến mại kích thích huy động hoặc cho vay (không bao gồm lương nhân viên), và chi phí dự phòng rủi ro tín dụng kế hoạch bao gồm cả dự phòng chung và dự phòng cụ thể (vab_ftp_methodology, Điều 4.2.2, d.304–306). Trên cơ sở đó, ban lãnh đạo ấn định tỷ lệ phân bổ NIM mục tiêu cho huy động vốn ($n_1$) và cho vay ($n_2$) thỏa mãn $n_1 + n_2 = 100\%$ (vab_ftp_methodology, Điều 4.2.2, d.315–321).

Từ tỷ lệ phân bổ trên, CFU xác định tỷ lệ Margin hỗ trợ huy động vốn áp dụng cho toàn bộ các sản phẩm tiền gửi khách hàng theo công thức (vab_ftp_methodology, Điều 4.2.2, d.357–364):
$$Margin\ (\%) = \frac{Chi\ ph\acute{\imath}\ qu\text{ả}n\ l\yacute;\ ti\text{ề}n\ g\text{ử}i\ k\text{ế}\ ho\text{ạ}ch}{S\text{ố}\ d\text{ư}\ huy\ \dstrok\text{ộ}ng\ b\grave{\imath}nh\ qu\hat{a}n\ k\text{ế}\ ho\text{ạ}ch} + T\text{ỷ}\ l\text{ệ}\ NIM\ huy\ \dstrok\text{ộ}ng\ k\text{ỳ}\ v\text{ọ}ng\ (\%)$$
Cấu phần này bù đắp toàn bộ chi phí bán hàng và chi phí vận hành huy động vốn, đồng thời bảo đảm các đơn vị mạng lưới nhận được phần chia công bằng từ thành quả NIM chung của ngân hàng (vab_ftp_methodology, Điều 4.2.2, d.361). Khi ngân hàng triển khai các gói tín dụng chính sách với lãi suất cho vay ưu đãi thấp hơn mức COF thông thường, khoản thâm hụt biên độ thương mại được bù đắp từ quỹ thù lao tập trung của ALCO chứ không làm suy giảm tỷ lệ Margin $n_1$ đã cam kết cho bên huy động (vab_ftp_methodology, Điều 4.2.2, d.320–325; Điều 4.3.5, d.510–515).

Khoản hỗ trợ huy động được tính toán định kỳ vào đầu năm và duy trì cố định trong suốt chu kỳ kế hoạch kinh doanh, trừ trường hợp Hội đồng ALCO quyết định điều chỉnh lại kế hoạch vào bán niên hoặc khi có biến động bất thường về cơ cấu kinh doanh (vab_ftp_methodology, Điều 4.2.2, d.291, d.363; Điều 4.4, d.524). Cấu phần Margin này xuất hiện đồng thời trong cả giá mua vốn VOF và giá bán vốn COF theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]], giúp hài hòa quyền lợi giữa các khối kinh doanh theo [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]], củng cố nguyên lý phân lập đóng góp cấu trúc của Treasury theo [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]], và đóng vai trò như một đòn bẩy quản trị chiến lược theo [[ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation]].
