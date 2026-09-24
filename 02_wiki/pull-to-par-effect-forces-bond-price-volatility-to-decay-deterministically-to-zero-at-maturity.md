---
title: pull-to-par-effect-forces-bond-price-volatility-to-decay-deterministically-to-zero-at-maturity
type: concept
tags: [pull-to-par, bond-pricing, volatility-structure, term-structure, quantitative-finance]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Cấu trúc độ biến động giá của trái phiếu theo thời gian đáo hạn phản ánh hiện tượng kéo về mệnh giá (pull-to-par effect) — một thuộc tính cấu trúc phân biệt căn bản giữa chứng khoán nợ có thời hạn cố định và các tài sản vốn vô hạn hạn (choudhry_analysing_yield_curve, Ch.4, Uncertainty of Interest Rates, d.2487–2498). Dưới độ đo xác suất trung lập rủi ro $Q$, trong các mô hình cấu trúc kỳ hạn Gaussian với độ biến động lãi suất ngắn hạn $\sigma$ và tốc độ hoàn lương $a$ cố định (theo Merton 1973, Vasicek 1977, Jamshidian 1991), tỷ suất sinh lời của trái phiếu zero-coupon $P(t,T)$ tuân theo phương trình vi phân ngẫu nhiên:
$$\frac{dP(t,T)}{P(t,T)} = r(t)dt + \sigma_P(t,T) dW_t^Q$$
trong đó hàm độ biến động giá của trái phiếu $\sigma_P(t,T)$ được xác định tường minh bằng biểu thức tất định: $\sigma_P(t,T) = \sigma \frac{1 - e^{-a(T-t)}}{a}$ (choudhry_analysing_yield_curve, Ch.4, Uncertainty of Interest Rates, d.2491–2498).

Hàm độ biến động $\sigma_P(t,T)$ thiết lập quy luật suy giảm phi tuyến theo khoảng thời gian đáo hạn còn lại $(T-t)$ (choudhry_analysing_yield_curve, Ch.4, Uncertainty of Interest Rates, d.2496–2498). Ở các kỳ hạn rất dài ($(T-t) \to \infty$), hàm số hạng $e^{-a(T-t)}$ tiến dần về 0 khiến độ biến động giá tiệm cận mức trần hữu hạn $\sigma / a$. Trái lại, khi thời gian trôi đi và trái phiếu tiến gần đến thời điểm đáo hạn ($t \to T$), đại lượng $1 - e^{-a(T-t)}$ suy giảm đơn điệu và hội tụ về 0:
$$\lim_{t \to T} \sigma_P(t,T) = 0$$
Điều này đồng nghĩa với việc dù một trái phiếu dài hạn có thể chịu biến động giá dữ dội trong suốt vòng đời do nhạy cảm thời lượng, toàn bộ rủi ro biến động giá ngẫu nhiên bắt buộc phải triệt tiêu hoàn toàn tại ngày đáo hạn vì giá trị tài sản phải hội tụ chính xác về 100% mệnh giá danh nghĩa (choudhry_analysing_yield_curve, Ch.4, Uncertainty of Interest Rates, d.2491–2498).

Quy luật suy giảm tất định của độ biến động trái phiếu tạo ranh giới đối lập hoàn toàn với chuyển động Brown hình học của cổ phiếu tại [[geometric-brownian-motion-ensures-strictly-positive-asset-prices-via-multiplicative-increments]], nơi độ biến động tương đối được giả định không đổi vĩnh viễn. Đặc tính này giải thích cơ chế suy giảm rủi ro giá kết hợp với [[bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics|sự suy giảm thời lượng duration theo thời gian nắm giữ]], đóng vai trò đầu vào định hình bề mặt biến động của các hợp đồng quyền chọn trái phiếu trong [[yield-curve-pca-factors-link-curvature-convexity-to-implied-rate-volatility]], đồng thời hoàn thiện hệ thống biểu diễn giá trị chiết khấu ngẫu nhiên dưới [[arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures|nguyên lý định giá martingale]].
