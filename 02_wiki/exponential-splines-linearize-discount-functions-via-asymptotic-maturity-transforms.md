---
title: exponential-splines-linearize-discount-functions-via-asymptotic-maturity-transforms
type: concept
tags: [yield-curve, term-structure, curve-fitting, exponential-splines, vasicek-fong, shea, discount-function]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Spline hàm mũ (Exponential Splines) do Oldrich Vasicek và Gifford Fong (1982) đề xuất là kỹ thuật ước lượng cấu trúc kỳ hạn giải quyết sự bất tương thích hình học căn bản giữa các hàm đa thức đại số và bản chất phân rã hàm mũ của hàm hệ số chiết khấu tài chính (choudhry_analysing_yield_curve, Ch.11, Sec. "Estimating Yield Curve Functions", d.4466–4477). Trong lý thuyết định giá tài sản tài chính, hàm hệ số chiết khấu liên tục $v(T) = \exp(-r(T) \cdot T)$ mang đặc tính phân rã tiệm cận về 0 khi kỳ hạn $T \to \infty$. Ngược lại, các hàm spline đa thức bậc ba truyền thống của McCulloch (1975) lại có bản chất phân kỳ tiến tới $\pm \infty$ ở các kỳ hạn xa nếu không áp đặt các ràng buộc biên chặt chẽ, dẫn đến hiện tượng đầu dài của đường cong lãi suất kỳ hạn ngụ ý bị sụp đổ dốc đứng hoặc tăng vọt phi thực tế [[forward-rate-oscillation-reveals-magnified-fitting-errors-and-disqualifies-linear-interpolation]].

Nhằm khắc phục sự chênh lệch độ cong tự nhiên giữa đa thức và hàm mũ, Vasicek và Fong đề xuất một phép biến đổi phi tuyến đối với biến số thời gian kỳ hạn $T$:
$$x = 1 - e^{-\alpha T}$$
Trong đó $\alpha > 0$ là một tham số quy mô được ước lượng từ dữ liệu thị trường, thể hiện giá trị giới hạn tiệm cận của mức lãi suất kỳ hạn khi thời gian tiến tới vô cực. Khi kỳ hạn $T$ biến thiên từ 0 đến vô hạn ($T \in [0, \infty)$), biến số mới $x$ được ánh xạ trọn vẹn vào đoạn khoảng đóng hữu hạn $[0, 1]$. Phép biến đổi tiệm cận này nén toàn bộ trục kỳ hạn vô hạn thành một miền xác định compact, đồng thời chuyển hóa hàm hệ số chiết khấu từ một hàm phân rã mũ phi tuyến phức tạp theo $T$ thành một hàm gần như tuyến tính (approximately linear function) theo biến số mới $x$ (choudhry_analysing_yield_curve, Ch.11, d.4470–4472).

Trên không gian tọa độ biến đổi $x$, mô hình áp dụng kỹ thuật spline bậc ba từng khúc để xấp xỉ hàm chiết khấu đã tuyến tính hóa. Khi biến đổi ngược về biến thời gian ban đầu $T$, dạng hàm chiết khấu $v(T)$ giữa mỗi cặp điểm nút liên tiếp trở thành một spline hàm mũ bậc ba có dạng tổng quát:
$$v(T) = a_i + b_i e^{-\alpha T} + c_i e^{-2\alpha T} + d_i e^{-3\alpha T}$$
Cấu trúc hàm số này tự động thiết lập tính ổn định tiệm cận: khi $T \to \infty$, các số hạng phân rã dần triệt tiêu, ép hàm chiết khấu hội tụ có kiểm soát và ngăn chặn triệt để hiện tượng phân kỳ hoang dã thường gặp ở các đa thức bậc ba thông thường [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity]].

Tuy nhiên, nghiên cứu thực nghiệm của Gary Shea (1985) đã chỉ ra rằng spline hàm mũ không mang lại kết quả ước lượng cấu trúc kỳ hạn ổn định hơn so với spline đa thức chuẩn (choudhry_analysing_yield_curve, Ch.11, d.4476–4477). Việc phải ước lượng đồng thời tham số phi tuyến $\alpha$ cùng hệ thống các hệ số spline khiến bài toán tối ưu hóa số học dễ rơi vào tình trạng ma trận suy biến và các điểm cực tiểu cục bộ không ổn định. Do đó, Shea khuyến nghị thay thế spline hàm mũ bằng các hàm cơ sở B-spline có giá đỡ cục bộ gọn [[b-splines-and-regression-splines-transform-piecewise-polynomial-curve-fitting-into-linear-least-squares]], hoặc chuyển sang áp dụng các mô hình phạt độ gập ghềnh biến thiên VRP [[variable-roughness-penalty-splines-balance-short-end-flexibility-and-long-end-smoothness]] và khung mô hình Anderson-Sleath [[anderson-sleath-model-weights-fitting-errors-by-inverse-modified-duration]] để dung hòa độ mịn dài hạn mà vẫn duy trì tính ổn định tính toán tuyến tính.
