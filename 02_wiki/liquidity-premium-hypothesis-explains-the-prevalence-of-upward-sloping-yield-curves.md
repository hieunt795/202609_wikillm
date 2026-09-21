---
title: liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves
type: concept
tags: [term-structure, liquidity-premium, yield-curve, interest-rate-risk, interest-rates]
sources: [cargill_central_bank_policy]
status: draft
last_updated: 2026-09-21
---

Giả thuyết phần bù thanh khoản (liquidity premium hypothesis hay biased expectations hypothesis) kế thừa mô hình toán học của [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates|giả thuyết kỳ vọng thuần túy]], nhưng loại bỏ giả định phi thực tế rằng nhà đầu tư thờ ơ với kỳ hạn đáo hạn (cargill_central_bank_policy, Ch.6, Liquidity Premium Hypothesis or Biased Expectations Hypothesis, d.2003). Trong thực tế, các nhà đầu tư là những chủ thể ngại rủi ro và luôn có xu hướng thiên vị việc nắm giữ các công cụ nợ ngắn hạn hơn dài hạn nhằm né tránh [[interest-rate-risk-increases-with-maturity-and-separates-total-return-from-yield|rủi ro lãi suất gia tăng theo kỳ hạn đáo hạn]]. Để chấp nhận mua và nắm giữ các trái phiếu dài hạn có biến động giá lớn hơn, nhà đầu tư đòi hỏi một phần bù thanh khoản (liquidity premium, $lp_t^m$) dương và tăng dần theo kỳ hạn $m$ (cargill_central_bank_policy, Ch.6, d.2003–2007).

Công thức xác định lãi suất dài hạn được điều chỉnh thành:
$$r_t^m = \frac{1}{m} \sum_{i=0}^{m-1} E_t(r_{t+i}^1) + lp_t^m$$
Trong đó phần bù thanh khoản $lp_t^m$ là hàm đồng biến theo kỳ hạn $m$ ($\frac{\partial lp}{\partial m} > 0$). Vì lãi suất dài hạn là một mức trung bình có thiên lệch hướng lên trên (biased average) so với kỳ vọng thuần túy, lý thuyết này còn được gọi là giả thuyết kỳ vọng thiên lệch (cargill_central_bank_policy, Ch.6, d.2007, d.2041).

Ưu thế vượt trội của giả thuyết phần bù thanh khoản là giải thích trọn vẹn và nhất quán cả hai quy luật thực nghiệm căn bản của cấu trúc kỳ hạn (cargill_central_bank_policy, Ch.6, d.2043):
1. Tính đồng biến cùng chiều: Giống như giả thuyết kỳ vọng thuần túy, mọi mức lãi suất dài hạn đều chứa cấu phần trung bình của các lãi suất ngắn hạn kỳ vọng, đảm bảo các mức lãi suất kỳ hạn khác nhau biến động tương quan chặt chẽ cùng nhau qua thời gian;
2. Ưu thế áp đảo của đường cong dốc lên: Sự hiện diện của phần bù thanh khoản tăng dần theo kỳ hạn tạo ra một lực đẩy nghiêng đường cong lợi suất lên phía trên (cargill_central_bank_policy, Ch.6, d.2039–2043, Bảng 6.2). Cụ thể:
   - Khi thị trường kỳ vọng lãi suất ngắn hạn tăng, đường cong dốc lên càng dốc mạnh hơn;
   - Khi thị trường kỳ vọng lãi suất ngắn hạn không đổi (vốn sẽ tạo ra đường cong phẳng trong thuyết kỳ vọng thuần túy), phần bù thanh khoản bẻ cong đồ thị thành đường cong dốc lên;
   - Khi thị trường kỳ vọng lãi suất ngắn hạn giảm nhẹ, đường cong vẫn có thể dốc lên hoặc phẳng; chỉ khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sụt giảm cực kỳ dữ dội lấn át cả phần bù thanh khoản thì đường cong đảo ngược (inverted yield curve) mới xuất hiện.

Cargill khẳng định rằng trong số các lý thuyết về đường cong lợi suất, giả thuyết phần bù thanh khoản là lý thuyết có tính thuyết phục khoa học cao nhất và phù hợp nhất với hành vi thực tế trên thị trường tài chính (cargill_central_bank_policy, Ch.6, d.2047). Nó đóng vai trò là chiếc cầu nối lý luận giải thích các tín hiệu cảnh báo sớm khi [[yield-curve-functions-as-a-rorschach-test-of-inflation-and-business-cycle-expectations|đường cong lợi suất phản ánh kỳ vọng lạm phát và chu kỳ kinh tế]].
