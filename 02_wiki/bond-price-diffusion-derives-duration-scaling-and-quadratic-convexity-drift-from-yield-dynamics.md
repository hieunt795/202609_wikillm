---
title: bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics
type: concept
tags: [bond-pricing, stochastic-calculus, duration, convexity, itos-lemma, quantitative-finance]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Phép dẫn xuất phương trình vi phân ngẫu nhiên cho giá trái phiếu chiết khấu từ động học khuếch tán của lợi suất đáo hạn là một ứng dụng định lượng then chốt của Bổ đề Itô, làm sáng tỏ cơ chế hình thành thời lượng và thặng dư độ lồi (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2457–2484). Giả sử lợi suất đáo hạn gộp liên tục $x(t,T)$ của một trái phiếu zero-coupon mệnh giá chuẩn 1 đơn vị đáo hạn tại thời điểm $T$ tiến hóa theo phương trình vi phân Ornstein-Uhlenbeck: $dx = a(b - x)dt + s dz$, trong đó $a, b, s$ là các hằng số dương đo lường tốc độ hoàn lương, mức cân bằng dài hạn và độ biến động của lợi suất (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2459–2463). Giá trị lý thuyết của trái phiếu chiết khấu được xác định qua hàm giải tích $P(t,T) = \exp(-x(T-t))$ (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2464–2466).

Để chuyển đổi động học của lợi suất $dx$ sang phương trình vi phân của giá trái phiếu $dP$, Bổ đề Itô được áp dụng cho hàm hai biến $P(t, x)$ với các đạo hàm riêng được giải tích tường minh (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2467–2471):
- Đạo hàm riêng theo thời gian: $\frac{\partial P}{\partial t} = x \exp(-x(T-t)) = x P$;
- Đạo hàm riêng bậc một theo lợi suất: $\frac{\partial P}{\partial x} = -(T-t)\exp(-x(T-t)) = -(T-t)P$;
- Đạo hàm riêng bậc hai theo lợi suất (độ cong lồi): $\frac{\partial^2 P}{\partial x^2} = (T-t)^2 \exp(-x(T-t)) = (T-t)^2 P$.

Thế các biểu thức đạo hàm này vào công thức khai triển Itô tổng quát $dP = \left( \frac{\partial P}{\partial t} + \mu_x \frac{\partial P}{\partial x} + \frac{1}{2}\sigma_x^2 \frac{\partial^2 P}{\partial x^2} \right) dt + \sigma_x \frac{\partial P}{\partial x} dz$, ta thu được phương trình vi phân giá trái phiếu chiết khấu (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2472–2483):
$$dP = P \left[ x - (T-t)a(b-x) + \frac{1}{2}s^2(T-t)^2 \right] dt - s(T-t)P dz$$

Phương trình vi phân này xác lập hai nguyên lý kinh tế học cấu trúc kỳ hạn căn bản:
1. Độ biến động tương đối của giá trái phiếu $\frac{\sigma_P}{P} = s(T-t)$ tỷ lệ thuận tuyến tính với thời gian đáo hạn còn lại $(T-t)$, cung cấp bằng chứng toán học vi mô cho khái niệm Modified Duration;
2. Thành phần trôi dạt (drift) của giá trái phiếu nhận được một lực đẩy gia tăng tỷ suất sinh lời thực dương $+\frac{1}{2}s^2(T-t)^2$ tỷ lệ thuận với bình phương thời gian đáo hạn $(T-t)^2$ (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2480–2483).

Lực đẩy thặng dư độ lồi bậc hai này giải thích tại sao các nhà đầu tư chấp nhận mức lợi suất danh nghĩa thấp hơn ở các kỳ hạn siêu dài, cung cấp cơ sở toán học cấu trúc cho hiện tượng đảo ngược và nén lợi suất tại [[convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end]], tương tác mật thiết với [[itos-lemma-transforms-short-rate-stochastic-dynamics-into-bond-pricing-pdes]], và làm tiền đề cho quy luật triệt tiêu rủi ro giá tại [[pull-to-par-effect-forces-bond-price-volatility-to-decay-deterministically-to-zero-at-maturity]].
