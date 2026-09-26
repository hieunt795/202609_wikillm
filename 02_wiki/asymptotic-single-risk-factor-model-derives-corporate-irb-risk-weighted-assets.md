---
title: asymptotic-single-risk-factor-model-derives-corporate-irb-risk-weighted-assets
type: concept
tags: [banking, credit-risk, corporate-irb, asrf, capital-requirement, sme, basel-iii]
sources: [sbv_circular_14_2025]
status: stable
last_updated: 2026-09-26
---

Hàm xác định tài sản có rủi ro tín dụng của khoản phải đòi doanh nghiệp theo phương pháp xếp hạng nội bộ (Corporate IRB) tại Điều 41–48 Thông tư 14/2025/TT-NHNN vận hành dựa trên mô hình một yếu tố rủi ro tiệm cận (Asymptotic Single Risk Factor — ASRF) của Ủy ban Basel sau khi danh mục đã được phân loại chuẩn tắc theo [[regulatory-default-definition-and-multi-tier-portfolio-segmentation-anchor-irb-models]] (sbv_circular_14_2025, file TT14_1.md, Điều 37, 41, d.933–950, 996–1048). Mô hình này giả định một danh mục cho vay được đa dạng hóa tối đa, trong đó rủi ro hệ thống của toàn bộ nền kinh tế được đại diện bởi một biến ngẫu nhiên chuẩn hóa duy nhất và rủi ro riêng biệt của từng doanh nghiệp bị triệt tiêu tiệm cận.

Trọng số rủi ro ($RW$) và yêu cầu vốn tự có ($K$) của từng khoản nợ doanh nghiệp được tính theo công thức phân phối chuẩn tích lũy hai biến tại mức độ tin cậy 99,9% trên chân trời 1 năm:

$$RW = 12{,}5 \times K$$

$$K = \left[ LGD \times N\left( \frac{G(PD)}{\sqrt{1 - R}} + \sqrt{\frac{R}{1 - R}} \times G(0{,}999) \right) - PD \times LGD \right] \times \frac{1 + (M - 2{,}5) \times b}{1 - 1{,}5 \times b}$$

Trong đó $N(x)$ là hàm phân phối tích lũy chuẩn, $G(z)$ là hàm nghịch đảo của phân phối chuẩn, $G(0{,}999) \approx 3{,}0902$, $M$ là kỳ hạn hiệu dụng (giới hạn từ 1 năm đến 5 năm), và $b = (0{,}11852 - 0{,}05478 \times \ln(PD))^2$ là hàm điều chỉnh kỳ hạn (sbv_circular_14_2025, file TT14_1.md, Điều 41.2, d.1010–1026). Đáng chú ý, số trừ $PD \times LGD$ trong ngoặc vuông phản ánh cấu phần tổn thất dự kiến được tách riêng để xử lý tại [[expected-loss-and-provisioning-shortfall-mechanics-adjust-regulatory-capital]], bảo đảm yêu cầu vốn $K$ chỉ thuần túy bù đắp cho tổn thất ngoài dự kiến (Unexpected Loss).

Hệ số tương quan tài sản ($R$) phản ánh mức độ nhạy cảm của doanh nghiệp với chu kỳ kinh tế vĩ mô, dao động nghịch đảo với xác suất vỡ nợ từ 24% (khi PD thấp) xuống 12% (khi PD cao) (sbv_circular_14_2025, file TT14_1.md, Điều 41.2.d, d.1018–1020). Đối với doanh nghiệp nhỏ và vừa (SME) có doanh thu bán hàng năm $S$ từ 20 đến 200–300 tỷ đồng, Ngân hàng Nhà nước cho phép điều chỉnh giảm hệ số tương quan tối đa $0{,}04$:

$$\Delta R_{SME} = -0{,}04 \times \left( 1 - \frac{S - S_{min}}{S_{max} - S_{min}} \right)$$

Chính sách này hạ thấp đáng kể mật độ RWA cho danh mục SME so với doanh nghiệp lớn, khuyến khích dòng vốn tín dụng lưu thông vào khu vực sản xuất kinh doanh (sbv_circular_14_2025, file TT14_1.md, Điều 41.3, d.1027–1048).

Về các tham số chuẩn tắc, Ngân hàng Nhà nước áp dụng cơ chế F-IRB (Foundation IRB) với các ngưỡng khống chế nghiêm ngặt: xác suất vỡ nợ bị chặn bởi mức sàn $PD \ge 0{,}05\%$ (sbv_circular_14_2025, file TT14_1.md, Điều 42.1, d.1049–1053). Tham số tổn thất khi vỡ nợ ($LGD$) được quy chuẩn cố định ở mức $40\%$ đối với khoản nợ không bảo đảm của doanh nghiệp thông thường (thấp hơn mức 45% của Basel II cũ theo cập nhật Basel III); $45\%$ đối với công ty chứng khoán, bảo hiểm; và $75\%$ đối với nợ thứ cấp (sbv_circular_14_2025, file TT14_1.md, Điều 43.1, d.1054–1061). Dữ liệu RWA tính từ hàm ASRF là căn cứ cốt lõi để xác định chi phí phân bổ vốn vốn chủ sở hữu và tính toán tỷ suất sinh lời điều chỉnh theo rủi ro [[ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc]].
