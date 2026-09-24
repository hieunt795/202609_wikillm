---
title: itos-lemma-derives-the-lognormal-asset-price-distribution-via-convexity-drag-correction
type: concept
tags: [itos-lemma, lognormal-distribution, convexity-drag, asset-pricing, quantitative-finance]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Phép dẫn xuất phân phối log-normal của giá tài sản từ phương trình chuyển động Brown hình học là một trong những ứng dụng kinh điển và quan trọng nhất của Bổ đề Itô trong toán tài chính (choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2437–2455). Một biến tài chính được xác định là có phân phối log-normal nếu logarit tự nhiên của biến đó tuân theo phân phối chuẩn (choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2439). Khi giá tài sản $S$ tuân theo quá trình khuếch tán dạng nhân tử $dS = \mu S dt + \sigma S dW$ tại [[geometric-brownian-motion-ensures-strictly-positive-asset-prices-via-multiplicative-increments]], việc xác định quy luật tiến hóa của giá trị logarit được thực hiện bằng cách đặt hàm khả vi $F(S) = \ln S$ (choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2445).

Áp dụng Bổ đề Itô cho hàm biến số $F(S)$, các đạo hàm riêng tương ứng được tính toán tường minh: đạo hàm bậc một theo giá tài sản là $F_S = \frac{1}{S}$, đạo hàm bậc hai phản ánh độ cong là $F_{SS} = -\frac{1}{S^2}$, và đạo hàm theo thời gian là $F_t = 0$ (choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2446–2450). Khi thế các thành phần này vào phương trình khai triển Itô tổng quát, phương trình vi phân của hàm logarit giá tài sản xác lập:
$$d(\ln S) = \left[ 0 + \mu S \left(\frac{1}{S}\right) + \frac{1}{2}\sigma^2 S^2 \left(-\frac{1}{S^2}\right) \right] dt + \sigma S \left(\frac{1}{S}\right) dW = \left(\mu - \frac{1}{2}\sigma^2\right) dt + \sigma dW$$
(choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2451–2454).

Sự xuất hiện của số hạng khấu trừ độ lồi (convexity drag hay Itô drift correction) mang giá trị $-\frac{1}{2}\sigma^2$ là hệ quả toán học tất yếu bắt nguồn từ đạo hàm bậc hai âm của hàm logarit lõm (choudhry_analysing_yield_curve, Ch.4, Example 4.2(i), d.2451–2455). Khi tích phân phương trình vi phân qua khoảng thời gian $T$, tỷ suất sinh lời liên tục $\ln(S_T / S_0)$ tuân theo phân phối chuẩn $N\left( \left(\mu - \frac{1}{2}\sigma^2\right)T, \sigma^2 T \right)$, trong khi giá trị kỳ vọng toán học của tài sản tăng trưởng theo cấp số nhân $\mathbb{E}[S_T] = S_0 e^{\mu T}$ (choudhry_analysing_yield_curve, Ch.4, Appendix 3.2, d.2121–2125; Example 4.2(i), d.2455). Khoảng chênh lệch $-\frac{1}{2}\sigma^2$ phản ánh sự suy giảm hiệu suất tích lũy do độ biến động gây ra, kết nối phương pháp vi phân ngẫu nhiên này với [[itos-lemma-transforms-short-rate-stochastic-dynamics-into-bond-pricing-pdes|bổ đề Itô trong cấu trúc kỳ hạn]], tạo tiền đề tính toán thặng dư độ lồi tại [[bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics]] và liên hệ với hiện tượng nén lợi suất trong [[convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end]].
