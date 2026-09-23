---
title: "Futures Rolls Maintain Interest Rate Hedges via PVBP-Neutral Roll Ratios Below Parity"
type: concept
tags:
  - derivatives
  - bond-futures
  - futures-roll
  - calendar-spread
  - roll-ratio
  - open-interest
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Hoạt động đảo kỳ hạn hợp đồng tương lai (futures roll hay calendar spread) là quá trình các định chế tài chính đồng thời đóng vị thế tại hợp đồng sắp đáo hạn (front contract) và tái lập trạng thái rủi ro tương đương tại hợp đồng kỳ hạn kế tiếp (back contract) nhằm duy trì trạng thái phòng hộ danh mục liên tục mà không phải tiếp nhận chuyển giao vật chất [[bond-futures-market-microstructure-differentiates-clearing-netting-and-cftc-trader-categories]]. Chênh lệch giá đảo kỳ hạn được định nghĩa toán học là giá hợp đồng kỳ hạn gần trừ đi giá hợp đồng kỳ hạn xa (fixed_income_during, Ch.28, Sec.28.4, d.333–349):

$$F_{\text{roll}} = F_{\text{front}} - F_{\text{back}}$$

Trong môi trường đường cong lợi suất dốc lên bình thường, các trái phiếu chấp nhận giao nộp mang lại chi phí nắm giữ (carry) dương, khiến giá kỳ hạn của trái phiếu thấp hơn giá giao ngay; kết quả là hợp đồng tương lai kỳ hạn xa thường giao dịch ở mức giá thấp hơn hợp đồng kỳ hạn gần, đặt cấu trúc kỳ hạn hợp đồng vào trạng thái bù hoãn mua (backwardation), tức mức chênh lệch $F_{\text{roll}}$ mang giá trị dương (fixed_income_during, Ch.28, Sec.28.4, d.347–350). Trạng thái đảo kỳ hạn chỉ chuyển sang bù hoãn bán (contango) khi trái phiếu rẻ nhất để giao nộp (Cheapest-to-Deliver - CTD) của hợp đồng kỳ hạn xa là một chứng khoán hoàn toàn khác biệt với CTD của hợp đồng kỳ hạn gần [[conversion-factors-induce-duration-dependent-cheapest-to-deliver-biases-around-notional-coupons]].

Do hợp đồng kỳ hạn gần và hợp đồng kỳ hạn xa thường có mức độ nhạy cảm rủi ro lãi suất (PVBP) khác nhau, việc đảo vị thế theo tỷ lệ số lượng một đổi một (one-for-one) sẽ tạo ra sự lệch pha rủi ro thời lượng có định hướng. Nhằm bảo đảm danh mục phòng hộ giữ nguyên mức độ miễn nhiễm trước biến động lãi suất, các nhà giao dịch phải áp dụng tỷ lệ đảo vị thế trung hòa rủi ro lãi suất (PVBP-neutral roll ratio) (fixed_income_during, Ch.28, Sec.28.4.1, d.377–387):

$$\text{Roll Ratio} = \frac{\text{PVBP}_{\text{front}}}{\text{PVBP}_{\text{back}}}$$

Trên thực tế, tỷ lệ đảo vị thế này thường có giá trị nhỏ hơn 1 (tức $\text{Roll Ratio} < 1$). Hiện tượng này xuất hiện do trái phiếu CTD của hợp đồng kỳ hạn xa có thời điểm giao nhận muộn hơn 3 tháng, do đó để đáp ứng tiêu chuẩn kỳ hạn của giỏ giao nhận, CTD của hợp đồng kỳ hạn xa thường là cùng một trái phiếu nhưng ở thời điểm lùi lại, hoặc là một mã trái phiếu có kỳ hạn còn lại dài hơn, dẫn đến mức PVBP của hợp đồng kỳ hạn xa cao hơn so với hợp đồng kỳ hạn gần (fixed_income_during, Ch.28, Sec.28.4.1, d.385–388). Để phòng hộ một khối lượng rủi ro thời lượng cố định, nhà đầu tư cần mua hoặc bán số lượng hợp đồng kỳ hạn xa ít hơn số lượng hợp đồng kỳ hạn gần đang đóng.

Sự kiện tỷ lệ đảo vị thế mang giá trị nhỏ hơn 1 làm nảy sinh một nghịch lý toán học: nếu mọi nhà đầu tư đều giảm số lượng hợp đồng nắm giữ qua mỗi chu kỳ đáo hạn theo một chuỗi cấp số nhân có hệ số nhân nhỏ hơn 1, thì khối lượng vị thế mở (open interest) của các hợp đồng tương lai trái phiếu chính phủ lý thuyết phải suy giảm dần về 0. Tuy nhiên, trên thực tế, tổng khối lượng vị thế mở của thị trường tương lai kho bạc Mỹ và châu Âu lại liên tục gia tăng bền vững qua nhiều thập kỷ (fixed_income_during, Ch.28, Sec.28.4.1, d.389–393). Lời giải kinh tế học cho nghịch lý này nằm ở dòng phát hành nợ công mới liên tục từ các kho bạc chính phủ [[sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand]]. Trong dài hạn, thời lượng trung bình của các đợt phát hành trái phiếu mới luôn vượt trội so với thời lượng của lượng trái phiếu hiện hữu đang bị rút ngắn dần theo thời gian (aging). Nhu cầu phòng hộ rủi ro lãi suất đối với khối lượng trái phiếu mới phát hành khổng lồ này đòi hỏi các định chế tài chính và nhà tạo lập thị trường phải mở thêm nhiều hợp đồng bán tương lai mới, bù đắp và vượt xa sự suy giảm vị thế cơ học từ tỷ lệ đảo hợp đồng (fixed_income_during, Ch.28, Sec.28.4.1, d.389–392).

Việc định giá chuẩn xác tỷ lệ đảo vị thế và giá trị hợp lý của hợp đồng hoán đổi kỳ hạn đòi hỏi các mô hình phân tích nâng cao vượt ra ngoài khuôn khổ một nhân tố dịch chuyển song song truyền thống (fixed_income_during, Ch.28, Sec.28.4.2, d.401–410). Trong các giỏ giao nhận có phạm vi kỳ hạn rộng lớn như hợp đồng tương lai trái phiếu kho bạc dài hạn Mỹ (US Long Bond), các biến động hình dạng đường cong (độ dốc và độ cong) cùng với rủi ro đặc thù của từng mã trái phiếu làm thay đổi xác suất chuyển đổi CTD [[quality-delivery-options-embed-negative-convexity-and-convexity-drag-in-bond-futures]]. Các hệ thống quản trị rủi ro hiện đại bắt buộc phải tích hợp kỹ thuật phân tích thành phần chính (PCA) để giảm số chiều rủi ro của giỏ giao nhận, đồng thời mô hình hóa sự tương quan biến động giữa lãi suất mua lại repo và lợi suất trái phiếu chính phủ trước khi các bên bước vào cửa sổ giao hàng [[futures-delivery-windows-confer-timing-options-governed-by-carry-sign-and-repo-fails-risk]].
