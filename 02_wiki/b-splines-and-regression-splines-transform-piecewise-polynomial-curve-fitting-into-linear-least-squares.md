---
title: b-splines-and-regression-splines-transform-piecewise-polynomial-curve-fitting-into-linear-least-squares
type: concept
tags: [yield-curve, term-structure, curve-fitting, b-splines, regression-splines, ols, financial-econometrics]
sources: [choudhry_analysing_yield_curve]
status: draft
last_updated: 2026-09-28
---

B-splines và hồi quy spline (regression splines) là kỹ thuật kinh tế lượng tài chính chuyển hóa bài toán khớp cấu trúc kỳ hạn lãi suất đa thức từng khúc phức tạp thành một mô hình hồi quy tuyến tính bội giải được trực tiếp bằng phương pháp bình phương tối thiểu thông thường (Ordinary Least Squares - OLS) (choudhry_analysing_yield_curve, Ch.1, Regression Models, d.962–997; Ch.10, Sec. "Spline-Based Methods", d.4137–4188; Appendix 10.2, d.4291–4366). Trong giai đoạn đầu của lý thuyết khớp đường cong, việc áp dụng một hàm đa thức bậc ba toàn cục đơn lẻ $d(t) = 1 + a_1 t + a_2 t^2 + a_3 t^3$ cho toàn bộ dải kỳ hạn đã bộc lộ khiếm khuyết mất ổn định phi cục bộ nghiêm trọng: sự biến động nhỏ của giá một trái phiếu ngắn hạn sẽ làm lệch lạc toàn bộ hình thái đường cong ở kỳ hạn 30 năm (choudhry_analysing_yield_curve, Ch.10, d.4131).

Phương pháp hồi quy cơ bản thiết lập phương trình giá bẩn thị trường của trái phiếu phụ thuộc vào dòng tiền coupon và nợ gốc (choudhry_analysing_yield_curve, Ch.1, Regression Models, d.964–976):
$$P_i^d = \sum_{n=1}^N d_n C_{ni} + u_i$$
Trong đó $P_i^d$ là giá bẩn (dirty price) quan sát được của trái phiếu thứ $i$, $C_{ni}$ là khoản thanh toán tiền mặt (coupon hoặc mệnh giá) của trái phiếu $i$ tại kỳ hạn $n$, $u_i$ là sai số ngẫu nhiên, và hệ số hồi quy $d_n$ thu được chính là ước lượng của hệ số chiết khấu (discount factor), từ đó suy ra đường cong lãi suất giao ngay qua quan hệ $s_n = (1/d_n)^{1/n} - 1$.

Tuy nhiên, phương trình trên không thể hồi quy trực tiếp trên thực tế do ngày chi trả coupon giữa các trái phiếu trong mẫu rất phân tán, dẫn đến số lượng dòng tiền coupon riêng lẻ vượt xa số lượng trái phiếu hiện có (choudhry_analysing_yield_curve, Ch.1, Regression Models, d.980). Để giải quyết tình trạng thiếu xác định này, cấu trúc kỳ hạn được phân chia thành các mốc lưới cố định (grid points) $d_{ni}^*$ dọc theo trục thời gian:
$$P_i^d = \sum_{n=1}^K d_{ni}^* C_{ni} + u_i$$
Mọi dòng tiền phát sinh giữa hai mốc lưới kế tiếp được phân bổ tuyến tính giữa hai điểm nút lân cận sao cho tổng giá trị hiện tại của dòng tiền được bảo toàn nguyên vẹn (choudhry_analysing_yield_curve, Ch.1, Regression Models, d.988). Mật độ điểm lưới được bố trí dày đặc ở đầu ngắn (short end) nơi dữ liệu thị trường dồi dào và độ cong lợi suất lớn, trong khi thưa dần về đầu dài (long end) nơi số lượng mã trái phiếu khan hiếm nhằm duy trì số bậc tự do kinh tế lượng và hạn chế sai lệch ước lượng (choudhry_analysing_yield_curve, Ch.1, Regression Models, d.990).

Để khắc phục hiện tượng mất ổn định của đa thức toàn cục, phương pháp spline chia trục kỳ hạn thành nhiều phân đoạn riêng biệt thông qua các điểm nút (knot points) $X_0, X_1, \dots, X_n$. Trên mỗi khoảng giữa hai điểm nút kế tiếp, đường cong được mô tả bởi một hàm đa thức bậc ba độc lập. Nhằm bảo đảm tính trơn tru kinh tế và ngăn ngừa các cú nhảy gián đoạn trên đường cong lãi suất kỳ hạn ngụ ý, mô hình áp đặt các điều kiện biên liên tục bậc hai ($C^2$ continuity) tại mọi điểm nút nối:
1. Tính liên tục của giá trị hàm số: $d_{i-1}(X_i) = d_i(X_i)$
2. Tính liên tục của đạo hàm bậc nhất (độ dốc): $d'_{i-1}(X_i) = d'_i(X_i)$
3. Tính liên tục của đạo hàm bậc hai (độ cong): $d''_{i-1}(X_i) = d''_i(X_i)$
Đồng thời, ràng buộc tự nhiên (natural spline constraints) được thiết lập tại hai điểm đầu mút: độ cong tức thời tại điểm bắt đầu kỳ hạn ngắn nhất và điểm kết thúc kỳ hạn dài nhất phải triệt tiêu về 0 ($r''(0) = 0$ và $r''(T_{max}) = 0$), bảo đảm đường cong thẳng tức thời ở hai đầu (choudhry_analysing_yield_curve, Ch.10, d.4158) [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity]].

Trong phân tích của Steeley (1991) và Choudhry (2001), phương pháp B-splines (basis splines) tối ưu hóa quy trình giải toán bằng cách biểu diễn hàm chiết khấu như một tổ hợp tuyến tính của các hàm cơ sở B-spline $B_p(t)$ có giá đỡ cục bộ gọn (compact local support):
$$d(t) = \sum_{p=1}^k c_p B_p(t)$$
Do mỗi hàm cơ sở $B_p(t)$ chỉ nhận giá trị khác 0 trên một số hữu hạn các phân đoạn kỳ hạn liền kề, sai số định giá hoặc cú sốc thanh khoản của một trái phiếu tại một kỳ hạn cụ thể chỉ tác động cục bộ lên các trọng số $c_p$ tương ứng mà không làm méo mó các phân đoạn kỳ hạn ở xa [[mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds]].

Phương pháp hồi quy spline do Suits, Mason và Chan (1978) phát triển (trình bày chi tiết tại Phụ lục 10.2 của Choudhry) cung cấp một cơ chế giải tích thanh lịch: bằng cách tích hợp trực tiếp các ràng buộc liên tục bậc hai vào phương trình hồi quy có biến giả (dummy variables), mô hình quy đổi hệ phương trình spline từng khúc thành một phương trình hồi quy tuyến tính của giá trái phiếu phụ thuộc vào các biến số tổng hợp (composite variables) (choudhry_analysing_yield_curve, Ch.10, d.4319–4360). Thuật toán OLS sau đó dễ dàng tìm ra các hệ số ước lượng tối thiểu hóa tổng bình phương sai số định giá trái phiếu trên toàn thị trường.

Tuy nhiên, việc gia tăng số lượng điểm nút để tăng độ khớp với dữ liệu thị trường đòi hỏi bổ sung thêm các biến tổng hợp, dẫn đến sự suy giảm số bậc tự do (loss of degrees of freedom) của mẫu dữ liệu kinh tế lượng (choudhry_analysing_yield_curve, Ch.10, d.4336, d.4366). Nếu chọn quá nhiều điểm nút hoặc đặt điểm nút tại các vùng dữ liệu thưa thớt, mô hình sẽ rơi vào tình trạng quá khớp (overfitting), biến các sai số vi mô của giá trái phiếu thành các đợt dao động giả tạo nguy hiểm trên đường cong kỳ hạn [[forward-rate-oscillation-reveals-magnified-fitting-errors-and-disqualifies-linear-interpolation]]. Sự đánh đổi này là lý do các mô hình tham số Nelson-Siegel thường được ưu tiên khi mục tiêu là xây dựng đường cong trơn tru dài hạn [[nelson-siegel-and-svensson-models-fit-parsimonious-forward-curves-with-asymptotic-long-rate-stability]].
