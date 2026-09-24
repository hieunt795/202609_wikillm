---
title: pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates
type: concept
tags: [term-structure, expectations-hypothesis, yield-curve, interest-rates]
sources: [cargill_central_bank_policy, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Giả thuyết kỳ vọng thuần túy (unbiased expectations hypothesis hay pure expectations hypothesis) là lý thuyết nền tảng đầu tiên giải thích cấu trúc kỳ hạn của lãi suất và hình thái của đường cong lợi suất (cargill_central_bank_policy, Ch.6, Unbiased Expectations Hypothesis, d.1949–1951; choudhry_analysing_yield_curve, Ch.1, The Expectations Hypothesis, d.653–655). Giả thuyết này dựa trên giả định cốt lõi rằng các nhà đầu tư trên thị trường là trung lập với rủi ro và hoàn toàn không có thiên kiến về kỳ hạn (indifferent to maturity): trong một khoảng thời gian hoạch định nhất định, mục tiêu duy nhất của nhà đầu tư là tối đa hóa của cải, do đó họ hoàn toàn bàng quan giữa việc nắm giữ một chuỗi các trái phiếu ngắn hạn liên tiếp hay mua một trái phiếu dài hạn có kỳ hạn tương đương (cargill_central_bank_policy, Ch.6, d.1951; choudhry_analysing_yield_curve, Ch.1, d.673–674).

Bỏ qua chi phí giao dịch, cơ chế kinh doanh chênh lệch giá (arbitrage) bắt buộc lãi suất của một trái phiếu có kỳ hạn $m$ thời kỳ ($r_t^m$) tại thời điểm $t$ phải bằng đúng trung bình của lãi suất ngắn hạn 1 thời kỳ hiện tại và các lãi suất ngắn hạn 1 thời kỳ kỳ vọng trong tương lai (cargill_central_bank_policy, Ch.6, d.1957–1963; choudhry_analysing_yield_curve, Ch.1, d.679–683). Trong mô hình tính toán hình học rời rạc của Choudhry:
$$(1 + rs_N)^N = (1 + rs_1)(1 + E[_1rf_2])(1 + E[_2rf_3]) \dots (1 + E[_{N-1}rf_N])$$
Nếu lãi suất dài hạn cao hơn mức trung bình kỳ vọng này, dòng tiền sẽ đổ xô mua trái phiếu dài hạn, đẩy giá tăng và kéo lợi suất xuống; ngược lại nếu lãi suất dài hạn thấp hơn, nhà đầu tư sẽ chuyển sang mua chuỗi trái phiếu ngắn hạn, đẩy lợi suất dài hạn tăng lên mức cân bằng (cargill_central_bank_policy, Ch.6, d.1957; choudhry_analysing_yield_curve, Ch.1, d.673).

Theo tổng hợp toán học của Choudhry và Ingersoll (1987), giả thuyết kỳ vọng thực chất tồn tại dưới 4 biến thể phân kỳ (choudhry_analysing_yield_curve, Ch.1, Mathematical Description of Expectations Hypothesis, d.707–738):
1. Giả thuyết kỳ vọng không thiên lệch (Unbiased expectations): Lãi suất kỳ hạn $f_{t,T,T+1}$ là ước lượng không thiên lệch của lãi suất giao ngay tương lai $E_t[r_T]$;
2. Giả thuyết tỷ suất sinh lời đáo hạn (Return to maturity): Lợi nhuận nắm giữ trái phiếu zero-coupon đến đáo hạn bằng kỳ vọng lợi nhuận từ việc liên tục tái đầu tư chuỗi trái phiếu 1 kỳ;
3. Giả thuyết lợi suất đáo hạn (Yield to maturity): Lợi suất hàng năm của trái phiếu dài hạn bằng trung bình lợi suất chuỗi tái đầu tư;
4. Giả thuyết kỳ vọng cục bộ (Local expectations): Mọi trái phiếu mang lại cùng một tỷ suất sinh lời kỳ vọng phi rủi ro trong khoảng thời gian cực ngắn [[local-expectations-hypothesis-resolves-jensens-inequality-under-risk-neutrality]].

Choudhry nhấn mạnh rằng do độ lồi giá trái phiếu và bất đẳng thức Jensen, biến thể không thiên lệch và biến thể tỷ suất đáo hạn không tương thích với nhau khi lãi suất có tương quan thời gian, và các bằng chứng thực nghiệm (Fama 1976) đều chỉ ra rằng lãi suất forward liên tục phóng đại lãi suất tương lai, biến chúng thành công cụ phòng hộ hơn là dự báo [[implied-forward-rates-function-as-hedge-rates-rather-than-accurate-market-forecasts]] (choudhry_analysing_yield_curve, Ch.1, d.699, d.725).

Công thức kỳ vọng thuần túy có thể tạo ra cả ba hình thái hình học của đường cong lợi suất tùy thuộc vào quỹ đạo lãi suất ngắn hạn kỳ vọng (cargill_central_bank_policy, Ch.6, d.1965–1998; choudhry_analysing_yield_curve, Ch.1, d.699):
- Đường cong dốc lên (Ascending): Khi thị trường kỳ vọng lãi suất ngắn hạn sẽ gia tăng liên tục trong tương lai;
- Đường cong phẳng (Flat): Khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sẽ giữ nguyên bằng lãi suất hiện tại;
- Đường cong dốc xuống / đảo ngược (Descending / Inverted): Khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sẽ sụt giảm liên tục.

Khi đánh giá dựa trên hai quy luật thực nghiệm căn bản của cấu trúc kỳ hạn, giả thuyết kỳ vọng thuần túy bộc lộ một thành công lớn và một hạn chế chí tử (cargill_central_bank_policy, Ch.6, d.2001; choudhry_analysing_yield_curve, Ch.1, d.665–671):
- Thành công: Lý giải hoàn hảo lý do tại sao các mức lãi suất có kỳ hạn khác nhau luôn vận động cùng chiều theo thời gian (tương quan rất cao), bởi mọi mức lãi suất dài hạn đều được tính toán từ cùng một gốc lãi suất ngắn hạn hiện tại;
- Hạn chế: Thất bại hoàn toàn trong việc giải thích tại sao đường cong lợi suất dốc lên lại là hình thái xuất hiện thường xuyên và áp đảo nhất trong lịch sử, bởi giả thuyết này không cung cấp được cơ sở kinh tế nào cho thấy tại sao thị trường lại luôn có xu hướng kỳ vọng lãi suất ngắn hạn tăng trong tương lai.

Hạn chế mang tính cấu trúc này là động lực thúc đẩy sự ra đời của [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản]], đóng vai trò nền tảng để phân tích [[yield-curve|đường cong lợi suất]], đồng thời tương phản với cách tiếp cận thể chế hóa của [[segmented-markets-hypothesis-views-maturities-as-disconnected-institutional-compartments|giả thuyết thị trường phân khúc]] trong bức tranh [[interest-rate-structure-is-determined-by-default-risk-liquidity-taxes-and-maturity|cấu trúc lãi suất tổng thể]].

