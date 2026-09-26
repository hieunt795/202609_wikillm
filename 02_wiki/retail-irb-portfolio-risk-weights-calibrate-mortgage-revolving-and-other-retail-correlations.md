---
title: retail-irb-portfolio-risk-weights-calibrate-mortgage-revolving-and-other-retail-correlations
type: concept
tags: [banking, credit-risk, retail-irb, mortgages, qrre, correlations, basel-iii]
sources: [sbv_circular_14_2025]
status: draft
last_updated: 2026-09-26
---

Phương pháp xác định tài sản có rủi ro tín dụng của khoản phải đòi bán lẻ (Retail IRB) tại Điều 49–54 Thông tư 14/2025/TT-NHNN phân tách danh mục khách hàng cá nhân thành các phân khúc đồng nhất theo [[regulatory-default-definition-and-multi-tier-portfolio-segmentation-anchor-irb-models]] để gán hệ số tương quan tài sản chuẩn tắc ($R$) mà không áp dụng hệ số điều chỉnh kỳ hạn $M$ như danh mục doanh nghiệp (sbv_circular_14_2025, file TT14_1.md, Điều 38, 49, d.951–972, 1198–1250). Trọng số rủi ro ($RW$) và yêu cầu vốn tự có ($K$) của danh mục bán lẻ tuân theo cấu trúc mô hình tiệm cận:

$$RW = 12{,}5 \times K$$

$$K = LGD \times N\left( \frac{G(PD)}{\sqrt{1 - R}} + \sqrt{\frac{R}{1 - R}} \times G(0{,}999) \right) - PD \times LGD$$

Ngân hàng Nhà nước Việt Nam phân loại danh mục bán lẻ thành ba nhóm con với các giả định hệ số tương quan $R$ phản ánh độ nhạy cảm khác biệt đối với chu kỳ kinh tế vĩ mô:
1. **Khoản cho vay thế chấp nhà ở**: Áp dụng hệ số tương quan cố định $R = 0{,}15$ (sbv_circular_14_2025, file TT14_1.md, Điều 49.2, d.1201–1215). Mức tương quan 15% phản ánh tính đồng pha tương đối giữa giá trị bất động sản dân cư và chu kỳ vĩ mô, đồng thời bổ trợ cho cơ chế quản trị rủi ro dựa trên [[loan-to-value-and-specialised-lending-criteria-differentiate-real-estate-risk-weights]].
2. **Khoản cấp tín dụng bán lẻ quay vòng đủ tiêu chuẩn (QRRE)**: Áp dụng hệ số tương quan cố định ở mức rất thấp $R = 0{,}04$ đối với thẻ tín dụng cá nhân và hạn mức thấu chi tiêu dùng chưa bảo đảm (sbv_circular_14_2025, file TT14_1.md, Điều 49.3, d.1216–1232). Tỷ lệ tương quan 4% dựa trên bằng chứng thực nghiệm cho thấy hành vi vỡ nợ của dư nợ thẻ tín dụng mang tính phân tán cao và chủ yếu do các sự kiện cá nhân (mất việc làm, bệnh tật) thay vì các cú sốc mang tính hệ thống toàn ngành.
3. **Khoản cấp tín dụng bán lẻ khác**: Áp dụng hệ số tương quan biến thiên nghịch đảo từ $0{,}16$ (khi PD thấp) xuống $0{,}03$ (khi PD cao) đối với các khoản cho vay mua ô tô, vay tiêu dùng trả góp và khoản vay hộ kinh doanh cá thể (sbv_circular_14_2025, file TT14_1.md, Điều 49.4, d.1233–1250).

Để ngăn chặn các ngân hàng thương mại lạc quan hóa các tham số đầu vào trong mô hình định lượng nội bộ, Thông tư 14/2025/TT-NHNN thiết lập hệ thống mức sàn tham số rủi ro bắt buộc (Input Parameter Floors) (sbv_circular_14_2025, file TT14_1.md, Điều 50–51, d.1251–1270). Mức sàn xác suất vỡ nợ được ấn định tại $PD \ge 0{,}10\%$ đối với khoản tín dụng quay vòng đủ chuẩn và $PD \ge 0{,}05\%$ đối với thế chấp nhà ở và bán lẻ khác. Đối với tham số tổn thất khi vỡ nợ, mức sàn được kiểm soát chặt chẽ với $LGD \ge 5\%$ đối với các khoản cho vay thế chấp nhà ở đủ tiêu chuẩn hoặc nhà ở xã hội. Hệ thống các mức sàn này triệt tiêu nguy cơ hạ thấp RWA quá mức, bảo đảm tính bền vững tương hỗ với [[asymptotic-single-risk-factor-model-derives-corporate-irb-risk-weighted-assets]].
