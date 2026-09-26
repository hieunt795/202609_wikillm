---
title: market-risk-capital-requirements-aggregate-interest-equity-fx-and-commodity-charges
type: concept
tags: [banking, market-risk, capital-adequacy, fx-risk, interest-rate-risk, trading-book, regulation]
sources: [sbv_circular_14_2025]
status: draft
last_updated: 2026-09-26
---

Khuôn khổ xác định vốn yêu cầu cho rủi ro thị trường theo Thông tư 14/2025/TT-NHNN lượng hóa tổng tổn thất tiềm tàng phát sinh từ các biến động bất lợi của giá thị trường trên sổ kinh doanh và trạng thái ngoại hối của ngân hàng thương mại (sbv_circular_14_2025, file TT14_2.md, Điều 74, d.241–267). Rủi ro thị trường được phân rã thành năm cấu phần độc lập tương ứng với các nhóm tài sản tài chính cơ sở: lãi suất, cổ phiếu, ngoại hối và vàng, hàng hóa, cùng với các hợp đồng quyền chọn. Cơ chế cộng gộp trực tiếp này đảm bảo tính thận trọng tối đa của khung pháp lý tiêu chuẩn khi không giả định bất kỳ hiệu ứng đa dạng hóa hay tương quan giảm trừ rủi ro nào giữa các nhóm tài sản khác nhau.

Tổng vốn yêu cầu cho rủi ro thị trường ($K_{MR}$) được tổng hợp theo công thức tuyến tính (sbv_circular_14_2025, file TT14_2.md, Điều 74.1, d.243–256):

$$K_{MR} = K_{IRR} + K_{ER} + K_{FXR} + K_{CMR} + K_{OPT}$$

Trong đó:
- $K_{IRR}$ là vốn yêu cầu cho rủi ro lãi suất đối với các công cụ nợ và chứng khoán phái sinh lãi suất trên sổ kinh doanh (trừ quyền chọn). Cấu phần này tách biệt giữa rủi ro đặc thù (Specific Risk) của tổ chức phát hành và rủi ro thị trường chung (General Market Risk) xuất phát từ sự dịch chuyển của toàn bộ đường cong lợi suất, được đo lường qua thang đáo hạn (Maturity Method) hoặc thang thời lượng (Duration Method) (sbv_circular_14_2025, file TT14_2.md, Điều 74.2, d.256–258).
- $K_{ER}$ là vốn yêu cầu cho rủi ro giá cổ phiếu trên sổ kinh doanh, phản ánh biến động giá của các chứng khoán vốn do yếu tố doanh nghiệp và xu hướng chung của thị trường chứng khoán (sbv_circular_14_2025, file TT14_2.md, Điều 74.3, d.260–262).
- $K_{FXR}$ là vốn yêu cầu cho rủi ro ngoại hối, bao gồm cả trạng thái vàng vật chất và phái sinh tiền tệ (sbv_circular_14_2025, file TT14_2.md, Điều 74.4, d.264).
- $K_{CMR}$ là vốn yêu cầu cho rủi ro biến động giá hàng hóa cơ sở đối với các hợp đồng phái sinh hoặc giao dịch vật chất liên quan (sbv_circular_14_2025, file TT14_2.md, Điều 74.5, d.265).
- $K_{OPT}$ là vốn yêu cầu chuyên biệt cho các giao dịch quyền chọn tiền tệ, lãi suất hoặc chứng khoán, nhằm phản ánh các rủi ro phi tuyến tính đặc thù như hệ số Delta, Gamma và Vega (sbv_circular_14_2025, file TT14_2.md, Điều 74.6, d.266).

Điểm đáng chú ý trong thiết kế chính sách của Ngân hàng Nhà nước là việc áp dụng cơ chế ngưỡng miễn trừ tối thiểu (*de minimis threshold*) đối với hai cấu phần có tính biến động cao nhằm giảm tải gánh nặng tính toán hành chính cho các ngân hàng có quy mô giao dịch nhỏ (sbv_circular_14_2025, file TT14_2.md, Điều 74.4, 74.6, d.264–266):

- Vốn rủi ro ngoại hối $K_{FXR}$ chỉ bắt buộc áp dụng khi tổng giá trị trạng thái ngoại hối ròng (bao gồm cả vàng) vượt quá **2% vốn tự có** của ngân hàng. Khi trạng thái ròng nằm dưới ngưỡng 2%, vốn yêu cầu $K_{FXR}$ được miễn trừ và ghi nhận bằng 0.
- Tương tự, vốn yêu cầu cho giao dịch quyền chọn $K_{OPT}$ chỉ phát sinh nghĩa vụ trích lập vốn khi tổng giá trị danh nghĩa các giao dịch quyền chọn vượt quá **2% vốn tự có** của ngân hàng.

Nhằm đưa rủi ro thị trường vào mẫu số chung của tỷ lệ an toàn vốn (CAR), Thông tư quy định toàn bộ mức vốn yêu cầu $K_{MR}$ được nhân với hệ số nghịch đảo của tỷ lệ an toàn vốn tối thiểu $8\%$, tức nhân với $12{,}5$ để quy đổi thành tài sản có rủi ro thị trường tương đương (Regulatory Risk-Weighted Assets for Market Risk):

$$RWA_{MR} = K_{MR} \times 12{,}5 = \frac{K_{MR}}{8\%}$$

Đại lượng $RWA_{MR}$ này được cộng trực tiếp với $RWA_{CR}$ (rủi ro tín dụng) và $RWA_{OR}$ (rủi ro hoạt động) để hình thành tổng tài sản có rủi ro ($RWA$) theo [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]]. Cơ chế tính vốn này thiết lập rào cản tài chính đối với các bàn tự doanh, gắn chặt với nguyên tắc phân định sổ kinh doanh tại [[trading-book-and-banking-book-boundary-enforces-market-risk-containment]], đồng thời tác động trực tiếp lên việc xác lập phần bù rủi ro trong cấu trúc đường cong lãi suất điều chuyển vốn nội bộ [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]] và tỷ suất sinh lời trên vốn có điều chỉnh rủi ro [[ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital]].
