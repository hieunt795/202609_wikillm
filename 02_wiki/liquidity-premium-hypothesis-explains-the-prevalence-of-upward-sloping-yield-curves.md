---
title: liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves
type: concept
tags: [term-structure, liquidity-premium, yield-curve, interest-rate-risk, interest-rates]
sources: [cargill_central_bank_policy, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Giả thuyết phần bù thanh khoản (liquidity premium hypothesis hay biased expectations hypothesis) kế thừa mô hình toán học của [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates|giả thuyết kỳ vọng thuần túy]], nhưng loại bỏ giả định phi thực tế rằng nhà đầu tư thờ ơ với kỳ hạn đáo hạn (cargill_central_bank_policy, Ch.6, Liquidity Premium Hypothesis or Biased Expectations Hypothesis, d.2003; choudhry_analysing_yield_curve, Ch.1, Liquidity Preference Theory, d.739–745). Trong thực tế, các nhà đầu tư là những chủ thể ngại rủi ro và luôn có xu hướng thiên vị việc nắm giữ các công cụ nợ ngắn hạn hơn dài hạn nhằm né tránh [[interest-rate-risk-increases-with-maturity-and-separates-total-return-from-yield|rủi ro lãi suất gia tăng theo kỳ hạn đáo hạn]]. Để chấp nhận mua và nắm giữ các trái phiếu dài hạn có biến động giá lớn hơn, nhà đầu tư đòi hỏi một phần bù thanh khoản (liquidity premium, $L_n$ hoặc $lp_t^m$) dương và tăng dần theo kỳ hạn đáo hạn (cargill_central_bank_policy, Ch.6, d.2003–2007; choudhry_analysing_yield_curve, Ch.1, d.749–755).

Mô hình cấu trúc kỳ hạn tổng quát kết hợp (Combined Theory hay Eclectic Theory) của Choudhry xác định rằng mức lãi suất kỳ hạn ngụ ý $f_{0,n}$ được cấu thành bởi kỳ vọng lãi suất giao ngay cộng với phần bù thanh khoản tương ứng (choudhry_analysing_yield_curve, Ch.1, The Combined Theory, d.798–805):
$$f_{0,n} = E[rs_n] + L_n \quad \text{với} \quad L_n > L_{n-1} > 0$$
Do $L_n$ là hàm đồng biến theo kỳ hạn, mô hình này chứng minh rằng đường cong lợi suất giao ngay (spot curve) vẫn sẽ có dạng dốc lên bình thường ngay cả khi thị trường kỳ vọng lãi suất ngắn hạn tương lai hoàn toàn đi ngang không đổi (choudhry_analysing_yield_curve, Ch.1, Bảng 1.3, d.807–824).

Ưu thế vượt trội của giả thuyết phần bù thanh khoản là giải thích trọn vẹn và nhất quán cả hai quy luật thực nghiệm căn bản của cấu trúc kỳ hạn (cargill_central_bank_policy, Ch.6, d.2043; choudhry_analysing_yield_curve, Ch.1, d.755):
1. Tính đồng biến cùng chiều: Giống như giả thuyết kỳ vọng thuần túy, mọi mức lãi suất dài hạn đều chứa cấu phần trung bình của các lãi suất ngắn hạn kỳ vọng, đảm bảo các mức lãi suất kỳ hạn khác nhau biến động tương quan chặt chẽ cùng nhau qua thời gian;
2. Ưu thế áp đảo của đường cong dốc lên: Sự hiện diện của phần bù thanh khoản tăng dần theo kỳ hạn tạo ra một lực đẩy nghiêng đường cong lợi suất lên phía trên (cargill_central_bank_policy, Ch.6, d.2039–2043; choudhry_analysing_yield_curve, Ch.1, d.755). Cụ thể:
   - Khi thị trường kỳ vọng lãi suất ngắn hạn tăng, đường cong dốc lên càng dốc mạnh hơn;
   - Khi thị trường kỳ vọng lãi suất ngắn hạn không đổi (vốn sẽ tạo ra đường cong phẳng trong thuyết kỳ vọng thuần túy), phần bù thanh khoản bẻ cong đồ thị thành đường cong dốc lên;
   - Khi thị trường kỳ vọng lãi suất ngắn hạn giảm nhẹ, đường cong vẫn có thể dốc lên hoặc phẳng; chỉ khi thị trường kỳ vọng lãi suất ngắn hạn tương lai sụt giảm cực kỳ dữ dội lấn át cả phần bù thanh khoản thì đường cong đảo ngược (inverted yield curve) mới xuất hiện.

Sự tương tác giữa phần bù thanh khoản dốc lên với kỳ vọng lãi suất đảo chiều còn có thể tạo ra [[humped-yield-curves-reflect-peaked-interest-rate-expectations-or-maturity-habitat-imbalances|đường cong hình bướu]], đồng thời tái định vị bản chất của [[implied-forward-rates-function-as-hedge-rates-rather-than-accurate-market-forecasts|lãi suất kỳ hạn ngụ ý]] và đóng vai trò là nền tảng giải thích các tín hiệu thị trường trên [[yield-curve|đường cong lợi suất tổng thể]].

