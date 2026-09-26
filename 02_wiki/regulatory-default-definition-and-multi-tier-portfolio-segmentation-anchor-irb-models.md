---
title: regulatory-default-definition-and-multi-tier-portfolio-segmentation-anchor-irb-models
type: concept
tags: [banking, credit-risk, default-definition, portfolio-segmentation, irb, basel-iii, regulation]
sources: [sbv_circular_14_2025]
status: draft
last_updated: 2026-09-26
---

Tiêu chuẩn nhận diện khách hàng vỡ nợ và khung phân đoạn danh mục tín dụng theo Thông tư 14/2025/TT-NHNN tạo lập nền tảng quy chuẩn để vận hành phương pháp xếp hạng nội bộ (IRB) trong việc ước tính xác suất vỡ nợ ($PD$) và tỷ lệ tổn thất khi vỡ nợ ($LGD$) (sbv_circular_14_2025, file TT14_1.md, Điều 36–40, d.898–991). Tính nhất quán của định nghĩa vỡ nợ là điều kiện tiên quyết để ngăn chặn sự méo mó trong dữ liệu lịch sử và bảo đảm tính hợp lệ của [[basel-output-floor-and-coverage-ratios-constrain-irb-capital-reductions]], đồng thời là đối tượng rà soát trọng tâm trong quy trình thử nghiệm sử dụng và kiểm định độc lập quy định tại [[irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility]].

Theo Điều 36 Thông tư 14/2025/TT-NHNN, khách hàng bị xác định là vỡ nợ khi phát sinh ít nhất một trong hai tiêu chí định lượng và định tính độc lập (sbv_circular_14_2025, file TT14_1.md, Điều 36.1, d.898–932). Tiêu chí thứ nhất là quá hạn thanh toán từ 90 ngày trở lên đối với bất kỳ nghĩa vụ trả nợ gốc hoặc lãi nào của khoản nợ. Tiêu chí thứ hai là sự suy giảm khả năng trả nợ (Unlikeliness to pay), thể hiện qua các sự kiện ngân hàng đánh giá khách hàng khó có khả năng hoàn trả đầy đủ nợ nếu không tiến hành xử lý tài sản bảo đảm: ngân hàng phải trích lập dự phòng cụ thể, thực hiện bán nợ chịu lỗ tài chính, chấp thuận cơ cấu lại thời hạn trả nợ kèm miễn giảm lãi gây thiệt hại kinh tế, hoặc khách hàng nộp đơn yêu cầu mở thủ tục phá sản. Đối với danh mục doanh nghiệp, Thông tư áp dụng nguyên tắc vỡ nợ ở cấp độ khách hàng: khi một khoản nợ của doanh nghiệp bị tuyên bố vỡ nợ, toàn bộ các khoản phải đòi khác của doanh nghiệp đó tại ngân hàng đều bị coi là vỡ nợ.

Dựa trên bản chất rủi ro và hành vi dòng tiền, Thông tư 14/2025/TT-NHNN phân chia các phơi nhiễm tín dụng thành ba khối danh mục độc lập phục vụ việc gán hàm vốn chuẩn tắc (sbv_circular_14_2025, file TT14_1.md, Điều 37–40, d.933–991):
1. **Khoản phải đòi doanh nghiệp**: Phân tách giữa doanh nghiệp thông thường, định chế tài chính, doanh nghiệp nhỏ và vừa (SME), và các khoản cấp tín dụng chuyên biệt (tài trợ dự án, tài trợ tài sản và hàng hóa) để đưa vào [[asymptotic-single-risk-factor-model-derives-corporate-irb-risk-weighted-assets]].
2. **Khoản phải đòi bán lẻ**: Phân loại thành ba nhóm con đồng nhất gồm khoản cho vay thế chấp nhà ở, khoản cấp tín dụng bán lẻ quay vòng đủ tiêu chuẩn (thẻ tín dụng cá nhân), và các khoản bán lẻ khác để tính toán theo [[retail-irb-portfolio-risk-weights-calibrate-mortgage-revolving-and-other-retail-correlations]].
3. **Khoản mua lại khoản phải thu (Purchased Receivables)**: Đo lường tách bạch giữa rủi ro vỡ nợ và rủi ro giảm giá trị (pha loãng do tranh chấp thương mại hoặc chiết khấu hàng bán bị trả lại).
