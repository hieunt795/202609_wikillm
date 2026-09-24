---
title: local-expectations-hypothesis-resolves-jensens-inequality-under-risk-neutrality
type: concept
tags: [expectations-hypothesis, no-arbitrage, quantitative-finance, term-structure, jensens-inequality]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Giả thuyết kỳ vọng cục bộ (local expectations hypothesis) khẳng định rằng trong một khoảng thời gian nắm giữ cực ngắn (holding period), mọi trái phiếu có cùng phẩm cấp tín dụng dù mang kỳ hạn đáo hạn khác nhau đều mang lại mức tỷ suất sinh lời kỳ vọng bằng đúng mức lãi suất phi rủi ro ngắn hạn (choudhry_analysing_yield_curve, Ch.1, The Expectations Hypothesis, d.655–659, d.733–737).

Nghiên cứu kinh điển của Cox, Ingersoll và Ross (1981) đã chứng minh rằng trong số 4 biến thể của giả thuyết kỳ vọng, giả thuyết kỳ vọng cục bộ là biến thể duy nhất hoàn toàn nhất quán với điều kiện cân bằng kinh tế phi kinh doanh chênh lệch giá (arbitrage-free) trong mô hình định giá liên tục (choudhry_analysing_yield_curve, Ch.1, d.655, d.701, d.737). Sự bất tương thích của các biến thể khác bắt nguồn từ độ lồi toán học (convexity) và bất đẳng thức Jensen: do mối quan hệ phi tuyến giữa giá trái phiếu và lãi suất ($P = e^{-rT}$), kỳ vọng của hàm phi tuyến không bằng hàm của kỳ vọng:
$$E\left[\frac{1}{1 + r}\right] > \frac{1}{1 + E[r]}$$
Hệ quả là, nếu giả thuyết kỳ vọng thuần túy (unbiased expectations hypothesis) được thỏa mãn trên đường cong lợi suất thì giả thuyết tỷ suất sinh lời đáo hạn (return-to-maturity hypothesis) buộc phải bị vi phạm khi các mức lãi suất có tương quan dương với nhau qua thời gian (choudhry_analysing_yield_curve, Ch.1, d.723–726).

Mặc dù giữ vị thế hoàn hảo về mặt cấu trúc toán học trong thế giới trung lập rủi ro (risk-neutral), giả thuyết kỳ vọng cục bộ không phản ánh được tâm lý ngại rủi ro thực tế trên thị trường, nơi các nhà đầu tư luôn đòi hỏi phần bù rủi ro biến động giá cho các kỳ hạn dài (choudhry_analysing_yield_curve, Ch.1, d.655, d.665–670). Sự thất bại thực nghiệm này phân định ranh giới giữa mô hình toán học thuần túy với [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates]], bổ sung cơ sở lý luận cho [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves]], liên kết trực tiếp với [[arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures|nguyên lý định giá trái phiếu martingale]] và hỗ trợ phát triển các mô hình cấu trúc kỳ hạn hiện đại tại [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]].
