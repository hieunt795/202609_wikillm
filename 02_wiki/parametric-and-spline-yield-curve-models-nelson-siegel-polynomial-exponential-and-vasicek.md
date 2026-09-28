---
title: parametric-and-spline-yield-curve-models-nelson-siegel-polynomial-exponential-and-vasicek
type: concept
tags: [fixed-income, yield-curve, parametric-models, splines, vasicek]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-28
---
Đường cong lợi suất (yield curve) là sự biểu diễn toán học liên tục của tập hợp thông tin thị trường phản ánh qua mức giá đồng thời của các công cụ thu nhập cố định đang lưu hành (fixed_income_during, Ch.19, Curves and Curve Models, d.12–29). Khái niệm lợi suất đáo hạn truyền thống (yield to maturity - YTM) của một trái phiếu coupon đơn lẻ chịu một khuyết tật lý thuyết cốt tử: nó áp dụng cùng một mức lãi suất chiết khấu phẳng $y$ duy nhất cho toàn bộ các dòng tiền phát sinh tại các thời điểm khác nhau của trái phiếu đó (fixed_income_during, Ch.19, Curves and Curve Models, d.18). Khi thị trường có nhiều trái phiếu giao dịch ở các mức YTM khác nhau, các dòng tiền độc lập phát sinh tại cùng một mốc thời gian lại bị chiết khấu theo các mức lãi suất khác biệt, vi phạm nguyên lý không trọng tài (fixed_income_during, Ch.19, Curves and Curve Models, d.18). Để khắc phục mâu thuẫn này, đường cong lợi suất mô hình hóa lãi suất chiết khấu dưới dạng một hàm số liên tục theo thời gian $y(t)$, chuyển đổi giá của tập hợp các công cụ thị trường thành hàm hệ số chiết khấu $Df(t)$ nhất quán phục vụ việc định giá chính xác mọi dòng tiền tùy ý (fixed_income_during, Ch.19, Curves and Curve Models, d.20–28).

Các mô hình đường cong tham số (parametric curve models hoặc reduced-form models) không hướng tới việc khớp giá tuyệt đối mọi chứng khoán trên thị trường mà tìm kiếm một hàm giải tích trơn tru, cô đọng để nắm bắt cấu trúc kinh tế tổng thể và nhận diện các cơ hội kinh doanh chênh lệch định giá tương đối (fixed_income_during, Ch.19, PARAMETRIC CURVE MODELS, d.190–197). Bốn họ mô hình toán học trọng yếu bao gồm:

1. **Mô hình Nelson-Siegel (1987) và Nelson-Siegel-Svensson (1994)**:
Mô hình Nelson-Siegel biểu diễn cấu trúc kỳ hạn của lãi suất giao ngay (zero rate) $y(t)$ thông qua phương trình:
$$y(t) = \beta_1 + \beta_2 \left( \frac{1 - e^{-t/\lambda}}{t/\lambda} \right) + \beta_3 \left( \frac{1 - e^{-t/\lambda}}{t/\lambda} - e^{-t/\lambda} \right)$$
trong đó:
- $\beta_1$ đại diện cho nhân tố mức độ (level): đóng góp dài hạn không đổi khi $t \to \infty$.
- $\beta_2$ đại diện cho nhân tố độ dốc (slope): hàm suy giảm hàm mũ bắt đầu từ 1 tại $t=0$ và tiến về 0 ở kỳ hạn dài, phản ánh độ chênh lệch ngắn hạn - dài hạn.
- $\beta_3$ đại diện cho nhân tố độ cong hoặc bướu (curvature / hump): có giá trị bằng 0 tại $t=0$, đạt cực đại tại kỳ hạn trung gian quanh tham số thang thời gian $\lambda$, và triệt tiêu khi $t \to \infty$ (fixed_income_during, Ch.19, The Nelson-Siegel and Nelson-Siegel-Svensson splines, d.198–206).
Mô hình mở rộng Nelson-Siegel-Svensson bổ sung thêm thành phần độ cong thứ hai để tăng tính linh hoạt cho đường cong phức tạp:
$$y(t) = \beta_1 + \beta_2 \left( \frac{1 - e^{-t/\lambda_1}}{t/\lambda_1} \right) + \beta_3 \left( \frac{1 - e^{-t/\lambda_1}}{t/\lambda_1} - e^{-t/\lambda_1} \right) + \beta_4 \left( \frac{1 - e^{-t/\lambda_2}}{t/\lambda_2} - e^{-t/\lambda_2} \right)$$
Họ mô hình này được hầu hết các ngân hàng trung ương và chỉ số trái phiếu REX của Đức sử dụng nhờ tính chất trực quan kinh tế rõ ràng (fixed_income_during, Ch.19, The Nelson-Siegel and Nelson-Siegel-Svensson splines, d.208–216).

2. **Mô hình Spline đa thức (Polynomial Splines)**:
Về mặt giải tích, spline là một tập hợp các đa thức từng khúc (piecewise polynomials) bậc $n$ được xác định trên $N-1$ khoảng đóng giữa $N$ điểm nút kỳ hạn $t_i$ ($t_0 < t_1 < \dots < t_N$):
$$P_i(t) = \sum_{k=0}^n \beta_{i,k} (t - t_i)^k, \quad t \in [t_i, t_{i+1}]$$
Để đảm bảo đường cong trơn tru, các đa thức được ràng buộc phải đồng nhất giá trị và đồng nhất $n-1$ đạo hàm đầu tiên tại các điểm nút $t_i$:
$$P_i^{(m)}(t_{i+1}) = P_{i+1}^{(m)}(t_{i+1}) \quad \forall m = 0, 1, \dots, n-1$$
Hệ ràng buộc này thiết lập một hệ $(N-1)(n-1)$ phương trình tuyến tính (fixed_income_during, Ch.19, Polynomial splines, d.218–236). Bằng cách cố định giá trị tại các điểm nút trùng khớp với kỳ hạn của các trái phiếu chuẩn (benchmarks), mô hình spline đa thức tạo ra một đường cong có khả năng phòng hộ hoàn hảo bằng chính các công cụ giao dịch trên thị trường, từng là nền tảng cho chỉ số Jumbo Pfandbrief JEX tại Đức (fixed_income_during, Ch.19, Polynomial splines, d.238–240).

3. **Mô hình Spline hàm mũ (The Exponential Spline)**:
Khác với các mô hình trên, spline hàm mũ được thiết lập trực tiếp trong không gian của hệ số chiết khấu $Df(t)$:
$$Df(t) = \sum_{i=1}^K \beta_i e^{-i \cdot \alpha \cdot t}$$
với điều kiện biên tự nhiên tại thời điểm hiện tại $Df(0) = 1$ tương đương với ràng buộc tuyến tính $\sum_{i=1}^K \beta_i = 1$ (fixed_income_during, Ch.19, The exponential spline, d.242–250). Tham số $\alpha$ đóng vai trò là tham số tỷ lệ thời gian (time scale parameter), và ở giới hạn $t \to \infty$, $\alpha$ đại diện cho lãi suất zero kỳ hạn vô hạn được ghép lãi liên tục (fixed_income_during, Ch.19, The exponential spline, d.252–256). Ưu thế tính toán vượt trội của spline hàm mũ là giá của các trái phiếu coupon là một hàm tuyến tính thuần túy theo các hệ số $\beta_i$. Do đó, bài toán tối thiểu hóa tổng bình phương sai số giá (least squares error) trở thành một bài toán hồi quy tuyến tính thông thường có nghiệm giải tích duy nhất, loại bỏ hoàn toàn việc dò nghiệm số phi tuyến tính phức tạp (fixed_income_during, Ch.19, The exponential spline, d.262).

4. **Mô hình cấu trúc Vasicek (The Vasicek Spline)**:
Mô hình Vasicek (1977) là mô hình cấu trúc cân bằng bắt đầu từ quá trình khuếch tán hồi quy về giá trị trung bình (Ornstein-Uhlenbeck) của lãi suất ngắn hạn tức thời $r_t$:
$$dr_t = k(\theta - r_t) dt + \sigma dW_t$$
trong đó $k$ là tốc độ hồi quy trung bình, $\theta$ là mức lãi suất cân bằng dài hạn, $\sigma$ là độ biến động của lãi suất ngắn hạn, và $W_t$ là một quá trình Wiener chuẩn (fixed_income_during, Ch.19, The Vasicek spline, d.264–270). Mô hình Vasicek cho phép tính toán giải tích chính xác nghiệm đóng của hệ số chiết khấu $Df(t)$ từ thời điểm hiện tại với lãi suất ngắn hạn $r_0$:
$$Df(t) = A(t) e^{-B(t) r_0}$$
với hai hàm thời gian được xác định cụ thể:
$$B(t) = \frac{1 - e^{-kt}}{k}$$
$$A(t) = \exp \left( \left( \theta - \frac{\sigma^2}{2k^2} \right) (B(t) - t) - \frac{\sigma^2}{4k} B(t)^2 \right)$$
Mặc dù mô hình Vasicek thiết lập liên kết lý thuyết chặt chẽ giữa độ biến động ngắn hạn $\sigma$ và hình dạng của đường cong lợi suất, thực tế hiệu chuẩn mô hình với dữ liệu lợi suất trái phiếu Kho bạc Mỹ cho thấy tham số $\sigma$ ước lượng có hệ số tương quan rất thấp ($R^2 < 0{,}1$) với chỉ số biến động quyền chọn giao dịch trên thị trường (như CBOE VXTYN), phơi bày sự phân kỳ thực nghiệm giữa mô hình cấu trúc đơn nhân tố và cấu trúc biến động phức tạp của thị trường tài chính (fixed_income_during, Ch.19, The Vasicek spline, d.278–296). Sự kết hợp giữa các mô hình tham số này với phân tích cấu trúc kỳ hạn là điều kiện tiên quyết để giải mã phần bù rủi ro trong [[term-risk-premium-utility-foundations-and-market-technical-drivers]] và thực hiện phân tích thành phần chính tại [[principal-component-analysis-and-duration-neutral-hedging-mechanics]].
