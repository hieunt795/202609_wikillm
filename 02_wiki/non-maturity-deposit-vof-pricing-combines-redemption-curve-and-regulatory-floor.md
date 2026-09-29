---
title: non-maturity-deposit-vof-pricing-combines-redemption-curve-and-regulatory-floor
type: concept
tags: [alm, ftp, vof, casa, non-maturity-deposits, redemption-curve, circular-22]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Sản phẩm tiền gửi không kỳ hạn (CASA) của khách hàng đặt ra thách thức phức tạp nhất trong hệ thống định giá mua vốn (VOF) do khách hàng nắm quyền đơn phương rút tiền bất kỳ lúc nào nhưng một tỷ lệ lớn số dư tổng thể vẫn duy trì bền bỉ trên bảng cân đối qua thời gian (vab_ftp_methodology, Điều 6.1.d.i, d.649–654). Để lượng hóa đúng giá trị kinh tế của nguồn vốn chi phí thấp này, phương pháp luận FTP phân nhánh thành hai cơ chế xác định giá VOF cơ sở tùy thuộc vào mức độ hoàn thiện của hạ tầng mô hình hành vi tại ngân hàng (vab_ftp_methodology, Điều 6.1.d.i, d.655–676).

Khi ngân hàng đã xây dựng mô hình hành vi (MHHV), CFU phân bổ số dư tiền gửi không kỳ hạn vào các khoảng thời gian đáo hạn khác nhau tương ứng với phần dòng tiền biến động ngắn hạn ($Non\text{-}CoreCasa_i$) và phần dòng tiền duy trì ổn định dài hạn ($1 - Non\text{-}CoreCasa_i$) căn cứ theo kết quả phân tích thống kê chuỗi dữ liệu lịch sử khách hàng (vab_ftp_methodology, Điều 6.1.d.i, d.657–658). Hệ thống FTP áp dụng kỹ thuật Đường cong hoàn trả (Redemption Curve) để xác lập giá VOF cơ sở hàng ngày theo công thức bình quân gia quyền (vab_ftp_methodology, Điều 6.1.d.i, d.658–666):
$$VOF_{\text{CASA}} = FTP_i \times Non\text{-}CoreCasa_i + FTP_j \times (1 - Non\text{-}CoreCasa_i)$$
Trong đó, $FTP_i$ là lãi suất VOF cơ sở tương ứng với kỳ hạn không ổn định $i$, $FTP_j$ là lãi suất VOF cơ sở tương ứng với kỳ hạn ổn định $j$, với các kỳ hạn $i$ và $j$ cùng tỷ lệ $Non\text{-}CoreCasa_i$ do Hội đồng ALCO phê duyệt định kỳ theo từng khối kinh doanh và từng loại tiền tệ (vab_ftp_methodology, Điều 6.1.d.i, d.663–666, d.684–686).

Trường hợp ngân hàng chưa vận hành mô hình hành vi, CFU áp dụng khung quy chuẩn thận trọng căn cứ theo điểm 2 Phần III Phụ lục 3 Thông tư 22/2019/TT-NHNN của Ngân hàng Nhà nước Việt Nam, quy định tỷ lệ rút vốn giả định $a\%$ không được thấp hơn 15% số dư bình quân tiền gửi không kỳ hạn của 30 ngày liền kề ngày tính toán (vab_ftp_methodology, Điều 6.1.d.i, d.672; Chú thích 2, d.700). Lãi suất VOF cơ sở khi đó được tính toán theo công thức (vab_ftp_methodology, Điều 6.1.d.i, d.675–682):
$$VOF = VOF_{\text{KKH}} \times a\% + VOF_{\text{CKH}} \times (1 - a\%)$$
trong đó $VOF_{\text{KKH}}$ là giá VOF không kỳ hạn, $a\%$ là tỷ lệ rút ra tối thiểu 15%, và $VOF_{\text{CKH}}$ là lãi suất VOF kỳ hạn 2 tháng hoặc theo phê duyệt của ALCO (vab_ftp_methodology, Điều 6.1.d.i, d.680–682). Đối với tiền gửi không kỳ hạn, phần bù thanh khoản kỳ hạn được ấn định bằng 0% và không áp dụng cấu phần hỗ trợ huy động Margin (vab_ftp_methodology, Điều 6.1.d.i, d.687–688). Kỹ thuật phân tầng Core/Non-core này bổ trợ trực tiếp cho cấu trúc định giá hai vế tại [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]], tương thích với các giới hạn trần thời lượng hành vi theo [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]], và phản ánh sự hội tụ với các tiêu chuẩn phân tầng thanh khoản quốc tế tại [[standardised-nmd-categorisation-and-core-deposit-caps-framework]].
