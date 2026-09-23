---
title: "Curve Trading Hierarchies Systematically Immunize Lower-Order Risk Dimensions"
type: concept
tags:
  - trading
  - curve-trading
  - immunization
  - risk-hierarchy
  - pvbp-neutrality
  - fixed-income
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Giao dịch đường cong (curve trading) là thuật ngữ bao quát các chiến lược đầu tư và kinh doanh chênh lệch giá dựa trên kỳ vọng về sự thay đổi hình dạng của đường cong lợi suất trái phiếu chính phủ hoặc hoán đổi lãi suất (fixed_income_during, Ch.31, d.10–13). Hai nguyên lý nền tảng chi phối mọi phân tích giao dịch đường cong: thứ nhất, dù quan điểm phân tích được hình thành dựa trên mô hình đường cong vĩ mô, việc thực thi luôn đòi hỏi phải mua bán các công cụ nợ cụ thể vốn chứa đựng rủi ro định giá đặc thù (idiosyncratic risk) lệch khỏi đường cong chung; thứ hai, chi phí nắm giữ (carry) và hiệu ứng trượt dốc (roll-down) tại mỗi điểm kỳ hạn là khác nhau, đồng nghĩa với việc sự thay đổi hình thái đường cong đã được phản ánh trước một phần vào cấu trúc kỳ hạn lý thuyết [[upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields]]. Do đó, mọi trạng thái rủi ro đường cong bắt buộc phải được đánh giá so sánh với đường cong kỳ hạn (forward curve) tại chân trời đầu tư thay vì đường cong giao ngay hiện tại (fixed_income_during, Ch.31, d.12–35).

Các chiến lược giao dịch đường cong được phân tầng có hệ thống dựa trên số lượng chân tham gia (number of legs, $n$), phản ánh các chiều kích rủi ro hình học tăng dần (fixed_income_during, Ch.31, d.14–25):
1. Chiến lược đơn lẻ ($n = 1$): Outright Long (cược lợi suất giảm) hoặc Outright Short (cược lợi suất tăng);
2. Chiến lược 2 chân ($n = 2$): Làm dốc đường cong (Steepeners) hoặc Làm phẳng đường cong (Flatteners) [[steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks]];
3. Chiến lược 3 chân ($n = 3$): Bướm (Butterflies), cược vào sự biến động của điểm trung tâm (bullet) so với hai điểm đầu mút (wings) [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]];
4. Chiến lược 4 chân ($n = 4$): Kền kền (Condors), cược vào sự tương quan độ dốc giữa hai cặp kỳ hạn độc lập dọc theo cấu trúc kỳ hạn.

Nguyên lý toán học tối thượng để thiết lập một chiến lược giao dịch bậc $n$ là: chiến lược bậc $n$ đòi hỏi xác định $n$ quy mô danh nghĩa ($N_1, \dots, N_n$) thông qua việc giải một hệ gồm $n$ phương trình độc lập (fixed_income_during, Ch.31, d.36–41). Phương trình đầu tiên ấn định quy mô rủi ro tổng thể của vị thế theo giá trị một điểm cơ bản (Risk $R = N \times \text{PVBP}$). Điểm then chốt mang tính quy chuẩn là $n-1$ phương trình còn lại được thiết lập sao cho vị thế bậc $n$ tự động được phòng hộ miễn nhiễm (hedged) hoàn toàn trước mọi rủi ro của các chiến lược có bậc thấp hơn từ $1$ đến $n-1$. Ví dụ, một giao dịch Butterfly ($n=3$) bắt buộc phải giải hệ phương trình để vừa triệt tiêu rủi ro dịch chuyển song song tuyệt đối ($n=1$), vừa triệt tiêu rủi ro làm dốc hay làm phẳng đường cong ($n=2$). Logic của phương pháp phân tầng này bảo đảm rằng nhà giao dịch cô lập chính xác chiều kích rủi ro độ cong mong muốn; nếu muốn tiếp nhận thêm rủi ro độ dốc, họ có thể mở một vị thế Steepener độc lập song song (fixed_income_during, Ch.31, d.40).

Cấu trúc phân tầng này làm bộc lộ một nghịch lý kinh tế giữa biên độ lợi nhuận và chi phí giao dịch (fixed_income_during, Ch.31, d.42–49). Các biến động hình học bậc cao (như sự thay đổi độ cong của Butterfly hay Condor) luôn có biên độ biến động tuyệt đối nhỏ hơn rất nhiều so với các đợt dịch chuyển định hướng bậc thấp (Outright hay Steepener) [[yield-curve-pca-factors-link-curvature-convexity-to-implied-rate-volatility]]. Đồng thời, do chi phí ma sát và chênh lệch giá mua bán (bid-offer spread) tăng tỷ lệ thuận với số lượng chân hợp đồng, tỷ suất sinh lời kỳ vọng biên của các chiến lược phức tạp chịu áp lực suy giảm mạnh.

Động lực kinh tế thúc đẩy các tổ chức chuyên nghiệp tham gia vào các chiến lược bậc cao không phải là mức độ biến động tổng thể, mà là lợi thế thông tin bất cân xứng (information advantage) và nhu cầu phòng hộ tạo lập thị trường [[fixed-income-trade-governance-balances-probabilistic-stop-loss-and-epistemological-consistency]]. Hầu hết mọi thành viên thị trường đều có quan điểm về xu hướng lãi suất chung (outright), khiến giá thị trường phản ánh rất nhanh các kỳ vọng này; ngược lại, các biến động cục bộ của Butterfly và Condor thường gắn liền với các đứt gãy cung cầu ngắn hạn rất dễ dự báo, chẳng hạn như áp lực phát hành nợ công tại một đợt đấu thầu trái phiếu cụ thể hoặc hoạt động phòng hộ danh mục trái phiếu kém thanh khoản của các nhà tạo lập thị trường (fixed_income_during, Ch.31, d.44–47). Cấu trúc phân tầng giải hệ phương trình tuyến tính này được tổng quát hóa thành kỹ thuật phòng hộ mô hình đường cong đa nhân tố trong [[yield-curve-model-hedges-immunize-state-variable-sensitivities-via-linear-systems]], đồng thời số lượng công cụ phòng hộ cần thiết được định hướng định lượng qua chỉ số tập trung giá trị riêng tại [[pca-eigenvalue-herfindahl-index-measures-yield-curve-complexity-and-hedging-breadth]].
