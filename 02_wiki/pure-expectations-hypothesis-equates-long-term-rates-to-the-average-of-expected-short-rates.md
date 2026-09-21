---
title: pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates
type: concept
tags: [term-structure, expectations-hypothesis, yield-curve, interest-rates]
sources: [cargill_central_bank_policy]
status: draft
last_updated: 2026-09-21
---

Giả thuyết kỳ vọng thuần túy (unbiased expectations hypothesis hay pure expectations hypothesis) là lý thuyết nền tảng đầu tiên giải thích cấu trúc kỳ hạn của lãi suất và hình thái của đường cong lợi suất (cargill_central_bank_policy, Ch.6, Unbiased Expectations Hypothesis, d.1949–1951). Giả thuyết này dựa trên giả định cốt lõi rằng các nhà đầu tư trên thị trường là trung lập với rủi ro và hoàn toàn không có thiên kiến về kỳ hạn (indifferent to maturity): trong một khoảng thời gian hoạch định nhất định, mục tiêu duy nhất của nhà đầu tư là tối đa hóa của cải, do đó họ hoàn toàn bàng quan giữa việc nắm giữ một chuỗi các trái phiếu ngắn hạn liên tiếp hay mua một trái phiếu dài hạn có kỳ hạn tương đương (cargill_central_bank_policy, Ch.6, d.1951).

Bỏ qua chi phí giao dịch, cơ chế kinh doanh chênh lệch giá (arbitrage) bắt buộc lãi suất của một trái phiếu có kỳ hạn $m$ thời kỳ ($r_t^m$) tại thời điểm $t$ phải bằng đúng trung bình cộng số học của lãi suất ngắn hạn 1 thời kỳ hiện tại và các lãi suất ngắn hạn 1 thời kỳ kỳ vọng trong tương lai (cargill_central_bank_policy, Ch.6, d.1957–1963):
$$r_t^m = \frac{r_t^1 + E_t(r_{t+1}^1) + E_t(r_{t+2}^1) + \dots + E_t(r_{t+m-1}^1)}{m}$$
Nếu lãi suất dài hạn cao hơn mức trung bình kỳ vọng này, dòng tiền sẽ đổ xô mua trái phiếu dài hạn, đẩy giá tăng và kéo lợi suất xuống; ngược lại nếu lãi suất dài hạn thấp hơn, nhà đầu tư sẽ chuyển sang mua chuỗi trái phiếu ngắn hạn, đẩy lợi suất dài hạn tăng lên mức cân bằng (cargill_central_bank_policy, Ch.6, d.1957).

Công thức kỳ vọng thuần túy có thể tạo ra cả ba hình thái hình học của đường cong lợi suất tùy thuộc vào quỹ đạo lãi suất ngắn hạn kỳ vọng (cargill_central_bank_policy, Ch.6, d.1965–1998, Bảng 6.1):
- Đường cong dốc lên (Ascending): Khi thị trường kỳ vọng lãi suất ngắn hạn sẽ gia tăng liên tục trong tương lai ($E_t(r_{t+i}^1)$ tăng dần);
- Đường cong phẳng (Flat): Khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sẽ giữ nguyên bằng lãi suất hiện tại;
- Đường cong dốc xuống / đảo ngược (Descending / Inverted): Khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sẽ sụt giảm liên tục.

Khi đánh giá dựa trên hai quy luật thực nghiệm căn bản của cấu trúc kỳ hạn, giả thuyết kỳ vọng thuần túy bộc lộ một thành công lớn và một hạn chế chí tử (cargill_central_bank_policy, Ch.6, d.2001):
- Thành công: Lý giải hoàn hảo lý do tại sao các mức lãi suất có kỳ hạn khác nhau luôn vận động cùng chiều theo thời gian (tương quan rất cao), bởi mọi mức lãi suất dài hạn đều được tính toán từ cùng một gốc lãi suất ngắn hạn hiện tại $r_t^1$;
- Hạn chế: Thất bại hoàn toàn trong việc giải thích tại sao đường cong lợi suất dốc lên lại là hình thái xuất hiện thường xuyên và áp đảo nhất trong lịch sử, bởi giả thuyết này không cung cấp được cơ sở kinh tế nào cho thấy tại sao thị trường lại luôn có xu hướng kỳ vọng lãi suất ngắn hạn tăng trong tương lai.

Hạn chế mang tính cấu trúc này là động lực thúc đẩy sự ra đời của [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản]], đồng thời tương phản với cách tiếp cận thể chế hóa của [[segmented-markets-hypothesis-views-maturities-as-disconnected-institutional-compartments|giả thuyết thị trường phân khúc]] trong bức tranh [[interest-rate-structure-is-determined-by-default-risk-liquidity-taxes-and-maturity|cấu trúc lãi suất tổng thể]].
