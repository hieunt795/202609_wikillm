---
title: geometric-programming-optimizes-continuous-discount-curves-under-bounded-uncertainty
type: concept
tags: [yield-curve, term-structure, optimization, geometric-programming, non-stochastic-uncertainty, duality, us-treasury]
sources: [choudhry_analysing_yield_curve]
status: draft
last_updated: 2026-09-28
---

Quy hoạch hình học (Geometric Programming - GP) dưới điều kiện bất định phi ngẫu nhiên (Non-Stochastic / Set-Membership Uncertainty) do Kenneth Kortanek và Vladimir Medvedev phát triển là phương pháp luận tối ưu hóa phi tuyến chuyển đổi bài toán chiết khấu dòng tiền phức tạp trên thị trường trái phiếu thành một bài toán quy hoạch lồi giải được bằng các thuật toán điểm trong với tốc độ hội tụ vượt trội (choudhry_analysing_yield_curve, Ch.13, Sec. "The Nature of the Underlying Optimisation...", d.4954–5058; "An Approach to Treating Uncertainty Quantification", d.5059–5088; Appendix, d.5407–5453).

Trong bài toán khớp đường cong phi ngẫu nhiên, thay vì sử dụng hàm tổn thất tổng bình phương sai số vốn không có cơ sở kinh tế thực chất ngoài sự tiện lợi kinh tế lượng (như Robert Bliss 1997 chỉ ra, trích trong Choudhry d.5083), Kortanek và Medvedev chuẩn hóa sai số định giá thông qua sai số phần trăm tuyệt đối trung bình (Mean Absolute Percentage Error - MAPE) (choudhry_analysing_yield_curve, Ch.13, Definition 13.1, d.5075–5088):
$$\text{MAPE} = \frac{1}{n} \sum_{t=1}^n \left| \frac{P_t - \hat{P}_t}{P_t} \right| \times 100\%$$
trong đó $P_t$ là chuỗi giá trái phiếu quan sát trên thị trường, $\hat{P}_t$ là chuỗi giá tính toán từ mô hình, và đơn vị tính là điểm phần trăm (ví dụ MAPE = 0.05% tương đương 5 điểm cơ bản). Chỉ số này phản ánh trực quan độ lệch giá trị tương đối mà không làm sai lệch trọng số do quy mô mệnh giá.

Xuất phát từ phương trình định giá dòng tiền chiết khấu liên tục $P = \sum C_i \exp(-\int_0^{T_i} f(s) ds)$, việc lấy tích phân hàm lãi suất kỳ hạn $f(s)$ trên các phân đoạn thời gian tạo ra các biến trạng thái tích lũy $y_i$. Do toán tử chiết khấu chứa số mũ tự nhiên của $y_i$, Kortanek và Medvedev thực hiện phép đổi biến sang hệ biến số dương ngặt (choudhry_analysing_yield_curve, Ch.13, Appendix: Geometric Programming, d.5409–5416):
$$x_j = e^{z_j} > 0$$
Phép biến đổi hàm mũ này quy đổi phương trình giá trái phiếu và các điều kiện biên của đường cong thành các đa thức biến thực với hệ số dương (posynomials) $g_k(t) = \sum c_i \prod t_j^{a_{ij}}$ mang số mũ thực tùy ý. 

Bài toán quy hoạch hình học nguyên thủy (Primal GP) sau đó được chuyển đổi giải tích sang bài toán đối ngẫu (Dual GP). Bằng cách ký hiệu hàm đối ngẫu là $F$ và thay thế bằng $-\ln F$, bài toán đối ngẫu trở thành một bài toán quy hoạch lồi có ràng buộc tuyến tính (choudhry_analysing_yield_curve, Ch.13, Remark 13.4, d.5417–5426). Bậc khó (Degree of Difficulty - DoD) của bài toán được xác định chuẩn xác theo công thức của Duffin, Peterson và Zener (1967) (choudhry_analysing_yield_curve, Ch.13, d.5425–5430):
$$\text{Degree of Difficulty} = (\text{Số lượng số hạng posynomial}) - (\text{Số biến nguyên thủy}) - 1$$
Trong cấu hình thực nghiệm trên thị trường Kho bạc Mỹ với 505 biến nguyên thủy, 487 số hạng và 568 ràng buộc bất đẳng thức, thuật toán điểm trong giải quyết bài toán đối ngẫu trong thời gian tính toán gần như tức thời (choudhry_analysing_yield_curve, Ch.13, Remark 13.5, d.5431–5434).

Khác với kinh tế lượng tài chính thông thường vốn giả định sai số tuân theo phân phối chuẩn, Kortanek và Medvedev áp dụng lý thuyết điều khiển tập hợp (guaranteed set-membership approach của Gusev và Romanov 2001), mô tả sự bất định dưới dạng hàm nhiễu động từng đoạn bị chặn trong các tập xác định hữu hạn (choudhry_analysing_yield_curve, Ch.13, d.5065–5072):
$$w_* \le w(t) \le w^*$$
Trong lý thuyết quy hoạch hình học, việc đạt được "tính đối ngẫu hoàn hảo" (Perfect Duality — khi giá trị hàm mục tiêu của bài toán nguyên thủy và bài toán đối ngẫu trùng khít hoàn toàn, tức khoảng cách đối ngẫu $\text{duality gap} \to 0$) là điều kiện tiên quyết để thực hiện phân tích độ nhạy giải tích (sensitivity analysis) đối với cấu trúc kỳ hạn (choudhry_analysing_yield_curve, Ch.13, d.5034; d.5373–5390). 

Thực nghiệm của Fisher (2005) và nghiên cứu của Kortanek chứng minh rằng chứng khoán có coupon kỳ hạn dưới 1 năm có cơ chế định giá khác biệt rõ rệt so với tín phiếu T-Bills (choudhry_analysing_yield_curve, Ch.13, What to Expect When Bills are Excluded..., d.5347–5360):
- Khi đưa 33 tín phiếu T-bills vào cùng tập mẫu với 29 trái phiếu, bài toán dừng ở vòng lặp 19 với giá trị mục tiêu đối ngẫu là $-6.3396$ và nguyên thủy là $-6.5879$ (dual infeasibility 0.01, primal infeasibility $1.26 \times 10^{-3}$), không đạt được Perfect Duality và vô hiệu hóa khả năng phân tích độ nhạy (choudhry_analysing_yield_curve, Ch.13, d.5361–5378);
- Ngược lại, khi loại bỏ hoàn toàn 33 tín phiếu T-bills, thuật toán hội tụ tuyệt đối sau 31 vòng lặp: giá trị mục tiêu nguyên thủy và đối ngẫu trùng khớp hoàn toàn ở mức $-6.324066328$, khoảng cách đối ngẫu thu hẹp về mức $7.8 \times 10^{-10}$, sai số vi phạm ràng buộc nguyên thủy chỉ còn $4.08 \times 10^{-8}$ (choudhry_analysing_yield_curve, Ch.13, d.5379–5402). 

Trạng thái Perfect Duality này cho phép tính toán các đạo hàm nhạy cảm rủi ro chính xác phục vụ tối ưu hóa đường cong [[dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches]], hỗ trợ bóc tách đường cong Ancillary [[ancillary-yield-curves-expand-benchmark-definitions-via-strict-irr-admissibility]] và xác lập ngưỡng hòa vốn cho các chiến lược spread [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]].
