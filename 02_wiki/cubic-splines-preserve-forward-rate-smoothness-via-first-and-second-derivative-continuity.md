---
title: cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity
type: concept
tags: [curve-fitting, splines, quantitative-finance, forward-rates, term-structure]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Kỹ thuật nội suy cubic spline (cubic spline method) là phương pháp mô hình hóa đường cong lợi suất bằng cách chia phổ kỳ hạn thành nhiều phân đoạn rời rạc giữa các điểm nút quan sát (vertices) và khớp một phương trình đa thức bậc ba riêng biệt cho từng phân đoạn (choudhry_analysing_yield_curve, Ch.1, Cubic Splines, d.933–944; Appendix: Cubic Spline Interpolation, d.1046–1052).

Ưu thế vượt trội của cubic spline so với phương pháp nội suy tuyến tính hay đa thức đơn lẻ nằm ở việc bảo đảm độ trơn nhẵn (smoothness) đồng thời kiểm soát độ cứng (stiffness) của đường cong (choudhry_analysing_yield_curve, Ch.1, d.934). Trong khi nội suy tuyến tính gây gãy khúc đột ngột tại các điểm nối và đa thức bậc cao dễ gặp hiện tượng quá khớp (over-fitting) gây dao động hoang dã làm forward rate bị âm, cubic spline áp đặt ba điều kiện biên toán học nghiêm ngặt để giải hệ phương trình ma trận (choudhry_analysing_yield_curve, Ch.1, d.887, d.926–930, d.1052–1080):
1. Tính liên tục điểm: Mỗi phương trình bậc ba phải đi qua chính xác cặp điểm nút kỳ hạn tương ứng của nó;
2. Tính liên tục đạo hàm: Đạo hàm bậc một (độ dốc) và đạo hàm bậc hai (độ lồi / curvature) của hai phương trình liền kề phải bằng nhau tuyệt đối tại điểm tiếp giáp ($rm'_{i}(n_i) = rm'_{i+1}(n_i)$ và $rm''_{i}(n_i) = rm''_{i+1}(n_i)$);
3. Điều kiện biên tự nhiên: Đạo hàm bậc hai tại hai điểm mút đầu và cuối phổ kỳ hạn được gán bằng không để ngăn chặn đường cong vểnh lên hoặc cắm xuống mất kiểm soát.

Việc bảo tồn tính liên tục của đạo hàm bậc hai là điều kiện tiên quyết trong toán tài chính, bởi đường cong lãi suất kỳ hạn tức thời (forward curve) vốn được tính từ đạo hàm của hàm chiết khấu hoặc spot rate, do đó bất kỳ sự gãy khúc nào về độ dốc cũng sẽ kích hoạt các bước nhảy vọt phi lý trên đường cong forward (choudhry_analysing_yield_curve, Ch.1, d.860, d.954). Kỹ thuật này kế thừa và mở rộng phương pháp spline ban đầu của [[mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds|McCulloch trên hàm chiết khấu coupon]], thiết lập nền tảng giải thuật cho [[composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition]], cung cấp đường cong đầu vào chuẩn xác để triển khai [[implied-forward-rates-function-as-hedge-rates-rather-than-accurate-market-forecasts]], và hỗ trợ tối ưu hóa khớp giá trái phiếu trong [[dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches]].

Trong phân tích sâu hơn ở Chương 10, Choudhry chứng minh phương pháp chuyển đổi phương trình định giá trái phiếu coupon $P = \sum C_t d(t) + M d(T)$ thành hệ phương trình tuyến tính giải các hệ số của hàm đa thức bậc ba (choudhry_analysing_yield_curve, Ch.10, d.4097–4132). Đối với hệ thống gồm $n$ phân đoạn giữa $n+1$ điểm nút, mô hình tạo ra $4n$ hệ số ẩn cần xác định; các điều kiện biên tự nhiên bắt buộc đường cong phải thẳng tức thời ở cả hai đầu ($r''(0) = 0$ và $r''(T_{max}) = 0$) (choudhry_analysing_yield_curve, Ch.10, d.4158). Khi số lượng điểm nút gia tăng, phương pháp này được nâng cấp thành các hàm cơ sở B-spline và hồi quy spline OLS [[b-splines-and-regression-splines-transform-piecewise-polynomial-curve-fitting-into-linear-least-squares]] để ngăn ngừa hiện tượng phóng đại sai số và dao động dữ dội trên đường cong kỳ hạn [[forward-rate-oscillation-reveals-magnified-fitting-errors-and-disqualifies-linear-interpolation]], đóng vai trò đối trọng với các mô hình tham số Nelson-Siegel [[nelson-siegel-and-svensson-models-fit-parsimonious-forward-curves-with-asymptotic-long-rate-stability]].

