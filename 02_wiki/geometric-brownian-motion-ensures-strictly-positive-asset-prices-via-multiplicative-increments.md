---
title: geometric-brownian-motion-ensures-strictly-positive-asset-prices-via-multiplicative-increments
type: concept
tags: [geometric-brownian-motion, stochastic-processes, asset-pricing, quantitative-finance, valuation]
sources: [choudhry_analysing_yield_curve]
status: draft
last_updated: 2026-09-28
---

Chuyển động Brown hình học (Geometric Brownian Motion - GBM) là mô hình chuẩn mực trong toán tài chính được thiết lập nhằm khắc phục các khiếm khuyết cơ bản của quá trình Wiener số học khi mô hình hóa giá tài sản (choudhry_analysing_yield_curve, Ch.4, Generalised Wiener Process, d.2319–2320). Quá trình Wiener tổng quát $dX = a dt + b dW$ vận hành trên cơ sở gia số cộng dồn (additive increments) và giả định phân phối chuẩn đối xứng, dẫn đến hai hạn chế nghiêm trọng: (1) luôn tồn tại xác suất dương giá tài sản nhận giá trị âm ($X < 0$), mâu thuẫn với nguyên tắc trách nhiệm hữu hạn của cổ phiếu và giá trị thanh toán thực tế của chứng khoán nợ; (2) độ biến động tuyệt đối cố định khiến tỷ suất sinh lời tương đối $\Delta X / X$ bị suy giảm dần khi giá tài sản tăng trưởng lên mức cao hơn (choudhry_analysing_yield_curve, Ch.4, Generalised Wiener Process, d.2319–2320).

Chuyển động Brown hình học giải quyết triệt để sự phi lý này bằng phép biến đổi hàm mũ $S_t = S_0 \exp(X_t)$, thiết lập phương trình vi phân ngẫu nhiên dạng tỷ suất theo quá trình Itô tổng quát (choudhry_analysing_yield_curve, Ch.4, A Model of the Dynamics of Asset Prices, d.2333–2345):
$$dX = a X dt + b X dz$$
trong đó $a$ là tốc độ trôi kỳ vọng (drift rate), $b^2 X^2$ là tốc độ phương sai (variance rate) tức độ lệch chuẩn tỷ lệ thuận với quy mô giá $b X$, và thành phần bất định bắt nguồn từ quá trình Wiener chuẩn hóa $dz = \epsilon \sqrt{dt}$ với $\epsilon \sim N(0, 1)$ (choudhry_analysing_yield_curve, Ch.4, A Model of the Dynamics of Asset Prices, d.2341–2345).

Trong môi trường thời gian rời rạc trên một khoảng thời gian $\Delta t$, biến động giá tài sản được cụ thể hóa thành (choudhry_analysing_yield_curve, Ch.4, A Model of the Dynamics of Asset Prices, d.2345–2348):
$$\Delta X = a X \Delta t + b X \epsilon \sqrt{\Delta t} \iff \frac{\Delta X}{X} = a \Delta t + b \epsilon \sqrt{\Delta t}$$
Phương trình này chứng minh rằng tỷ suất sinh lời tương đối $\frac{\Delta X}{X}$ có kỳ vọng $a \Delta t$ và phương sai $b^2 \Delta t$, hoàn toàn độc lập với mức giá tuyệt đối $X$. Khi giả định độ biến động bằng không ($b = 0$), phương trình vi phân suy biến thành quy luật tất định:
$$\Delta X = a X \Delta t \implies \frac{dX}{dt} = a X \implies X(t) = X_0 e^{at}$$
xác nhận rằng động lực tăng trưởng hàm mũ liên tục là khung xương sống tất định bên dưới các cú sốc ngẫu nhiên (choudhry_analysing_yield_curve, Ch.4, A Model of the Dynamics of Asset Prices, d.2349–2356). Cấu trúc nhân tử (multiplicative) này ép giá tài sản luôn duy trì giá trị dương nghiêm ngặt ($X_t > 0$) tại mọi thời điểm, bảo đảm xác suất để giá tăng gấp đôi là đồng nhất bất kể xuất phát điểm (choudhry_analysing_yield_curve, Ch.4, Appendix 3.2, d.2119–2120).

Mặc dù đóng vai trò nền tảng để thiết lập [[itos-lemma-derives-the-lognormal-asset-price-distribution-via-convexity-drag-correction|phân phối log-normal của giá tài sản]] trong mô hình Black-Scholes, GBM lại bộc lộ giới hạn lớn khi mô tả cấu trúc kỳ hạn của lãi suất (choudhry_analysing_yield_curve, Ch.4, Stochastic Processes, d.2205–2210). Lãi suất thị trường không tăng trưởng không giới hạn theo thời gian mà vận động theo chu kỳ kinh tế, buộc các nhà kinh tế tài chính phải thay thế giả định GBM bằng [[ornstein-uhlenbeck-mean-reversion-prevents-infinite-drift-in-short-rate-diffusion|cơ chế hoàn lương trung bình Ornstein-Uhlenbeck]] và chấp nhận phân phối Gaussian. Khung mô hình này thiết lập nền tảng giải tích tương thích với [[arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures|nguyên lý định giá martingale]], hỗ trợ làm sáng tỏ [[bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics|phương trình khuếch tán giá trái phiếu]] và quy luật hội tụ tại [[pull-to-par-effect-forces-bond-price-volatility-to-decay-deterministically-to-zero-at-maturity]].
