---
title: irrbb-supervisory-framework-measures-eve-and-nii-sensitivity-across-interest-rate-shocks
type: concept
tags: [banking, alm, irrbb, interest-rate-risk, banking-book, delta-eve, delta-nii, repricing-gap, regulation]
sources: [sbv_circular_83_2025]
status: draft
last_updated: 2026-09-26
---

Khuôn khổ giám sát rủi ro lãi suất trên sổ ngân hàng (Interest Rate Risk in the Banking Book - IRRBB) theo Thông tư 83/2025/TT-NHNN đặt ra chuẩn mực định lượng toàn diện nhằm bảo vệ cả thu nhập ngắn hạn lẫn giá trị kinh tế dài hạn của tổ chức tín dụng trước các biến động lãi suất thị trường (sbv_circular_83_2025, file TT83.md, Điều 3.22 & Điều 53–55, d.89–94, 912–951). Sau khi phân lập rõ ranh giới với sổ kinh doanh theo [[trading-book-and-banking-book-boundary-enforces-market-risk-containment]], sổ ngân hàng là nơi chứa đựng toàn bộ các tài sản và công nợ nhạy cảm lãi suất phục vụ hoạt động ngân hàng truyền thống theo [[interest-rate-risk-in-the-banking-book-irrbb]]. Quy chế yêu cầu bộ phận đo lường và kiểm soát rủi ro lãi suất sổ ngân hàng phải hoàn toàn độc lập với các đơn vị kinh doanh tạo ra rủi ro và phải duy trì tần suất đo lường định kỳ tối thiểu hàng quý (sbv_circular_83_2025, file TT83.md, Điều 54.1, d.927–928).

Về mặt nhận dạng, Thông tư chuẩn hóa 03 cấu phần rủi ro lãi suất cốt lõi theo khuyến nghị của Ủy ban Basel (sbv_circular_83_2025, file TT83.md, Điều 3.22, d.89–94):
1. Rủi ro chênh lệch (Gap Risk): Phát sinh từ sự không khớp về thời điểm tái định giá lãi suất hoặc không khớp về kỳ hạn hợp đồng giữa tài sản sinh lời và nguồn vốn huy động (bao gồm cả các cam kết ngoại bảng);
2. Rủi ro cơ sở (Basis Risk): Phát sinh do sự chênh lệch và biến động không đồng nhất giữa các chỉ số lãi suất tham chiếu (benchmarks) được sử dụng để định giá lại tài sản và nợ phải trả có cùng kỳ hạn (chẳng hạn chênh lệch giữa lãi suất huy động bình quân nhóm NHTMCP và lãi suất điều hành hoặc VNIBOR);
3. Rủi ro quyền chọn (Option Risk): Gồm rủi ro quyền chọn tự động (Automatic Option Risk - các điều khoản quyền chọn trần/sàn cap/floor được kích hoạt tự động theo hợp đồng) và rủi ro quyền lựa chọn hành vi (Behavioural Option Risk - khách hàng thay đổi hành vi tài chính khi mặt bằng lãi suất đảo chiều, như tất toán tiền gửi tiết kiệm trước hạn để chuyển kênh đầu tư hoặc trả nợ trước hạn khoản vay thế chấp).

Phương pháp đo lường IRRBB bắt buộc phải tích hợp phương pháp tiếp cận dòng thu nhập ngắn hạn và phương pháp tiếp cận giá trị kinh tế dài hạn thông qua hai chỉ số độ nhạy (sbv_circular_83_2025, file TT83.md, Điều 53.1.a.ii, d.918):
- Thay đổi thu nhập lãi thuần ($\Delta NII$ - Change in Net Interest Income): Lượng hóa mức độ biến động của thu nhập lãi ròng trên báo cáo kết quả kinh doanh trong khung thời gian 01 năm tiếp theo dựa trên mô hình bảng chênh lệch kỳ định lại lãi suất (Repricing Gap Profile);
- Thay đổi giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$ - Change in Economic Value of Equity): Đo lường sự suy giảm giá trị hiện tại ròng của toàn bộ dòng tiền dự kiến từ tài sản trừ đi dòng tiền nợ phải trả theo giá trị thị trường chiết khấu dưới tác động của các kịch bản sốc lãi suất.

Ngân hàng phải thiết lập hệ thống hạn mức rủi ro bắt buộc đối với cả mức sụt giảm $\Delta NII$ và $\Delta EVE$ tối đa có thể chấp nhận (sbv_circular_83_2025, file TT83.md, Điều 53.2, d.920–923). Công tác đo lường độ nhạy bắt buộc phải được bóc tách riêng biệt cho từng loại tiền tệ có giá trị tài sản hoặc nợ phải trả chiếm từ 5% trở lên trên tổng tài sản sổ ngân hàng (sbv_circular_83_2025, file TT83.md, Điều 54.3.c, d.933). Đối với các sản phẩm không có kỳ hạn cố định như tiền gửi thanh toán (CASA), ngân hàng phải xây dựng mô hình hành vi để phân rã dòng tiền và phải được cấp có thẩm quyền phê duyệt trước khi đưa vào tính toán (sbv_circular_83_2025, file TT83.md, Điều 54.4.a, d.936).

Kết quả đo lường độ nhạy $\Delta EVE$ và $\Delta NII$ là đầu vào thiết yếu phục vụ công tác điều phối bảng cân đối kế toán của Hội đồng ALCO theo [[senior-management-oversight-and-conflict-of-interest-containment-anchor-banking-governance]], đóng vai trò nền tảng để hiệu chỉnh đường cong lãi suất điều chuyển vốn nội bộ theo [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], hội nhập với chuẩn mực quốc tế tại [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]], và được cụ thể hóa bằng thuật toán đo lường 19 thang kỳ hạn, mô hình hóa NMDs, CPR, TDRR và 6 kịch bản sốc lãi suất chuẩn tại [[irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios]].

Xem thêm: [[trading-book-and-banking-book-boundary-enforces-market-risk-containment]], [[interest-rate-risk-in-the-banking-book-irrbb]], [[senior-management-oversight-and-conflict-of-interest-containment-anchor-banking-governance]], [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]], [[irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios]].

