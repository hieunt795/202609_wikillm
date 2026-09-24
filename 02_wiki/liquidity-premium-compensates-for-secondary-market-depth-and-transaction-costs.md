---
title: liquidity-premium-compensates-for-secondary-market-depth-and-transaction-costs
type: concept
tags: [liquidity, liquidity-premium, secondary-markets, bond-market, interest-rates]
sources: [cargill_central_bank_policy, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Tính thanh khoản (liquidity hay marketability) của một tài sản tài chính là khả năng chuyển đổi tài sản đó thành tiền mặt nhanh chóng trên thị trường thứ cấp mà không phải chịu tổn thất lớn về giá trị (cargill_central_bank_policy, Ch.6, Liquidity or Marketability Effect, d.1901). Tính thanh khoản của chứng khoán phụ thuộc vào hai nhân tố cấu trúc: sự tồn tại, quy mô và độ sâu rộng của thị trường thứ cấp, và mức chi phí giao dịch (hoa hồng môi giới, chênh lệch giá mua - giá bán bid-ask spread) phát sinh khi bán chứng khoán (cargill_central_bank_policy, Ch.6, d.1901). Vấn đề thanh khoản chỉ phát sinh ý nghĩa kinh tế khi tồn tại xác suất khác không rằng nhà đầu tư có nhu cầu bán lại chứng khoán trước ngày đáo hạn.

Trong [[loanable-funds-framework-determines-equilibrium-interest-rate-and-bond-price|khung quỹ cho vay]], một chứng khoán có tính thanh khoản thấp làm giảm sút mức độ hấp dẫn đối với các nhà đầu tư, khiến đường cung quỹ cho vay dịch chuyển sang trái và đòi hỏi một mức lãi suất cao hơn để bù đắp rủi ro thanh khoản (cargill_central_bank_policy, Ch.6, d.1903). Mức chênh lệch lợi suất phụ trội bắt nguồn từ sự khác biệt về thanh khoản được gọi là phần bù thanh khoản (liquidity premium, $lp$), được tích hợp trực tiếp vào [[interest-rate-structure-is-determined-by-default-risk-liquidity-taxes-and-maturity|phương trình cấu trúc lãi suất]]:
$$nr = rr + P^e + df + lp$$
Trong đó $lp = 0$ đối với chứng khoán kho bạc chính phủ và $lp > 0$ đối với tất cả các công cụ nợ khác (cargill_central_bank_policy, Ch.6, d.1909–1911).

Chứng khoán kho bạc Hoa Kỳ là tài sản có tính thanh khoản cao nhất trong hệ thống tài chính toàn cầu nhờ thị trường thứ cấp khổng lồ, sâu rộng, có vô số thành viên tham gia và chi phí giao dịch tối thiểu (cargill_central_bank_policy, Ch.6, d.1905). Trong khi [[money-is-the-only-one-hundred-percent-liquid-asset|tiền tệ là tài sản duy nhất có thanh khoản tuyệt đối 100%]], chứng khoán kho bạc là tài sản sinh lãi tiệm cận gần nhất với tiền về phương diện thanh khoản. 

Hệ quả phân tích thực tiễn là: khoảng chênh lệch lợi suất quan sát được giữa các chứng khoán tư nhân (như trái phiếu doanh nghiệp Baa) và chứng khoán kho bạc luôn phản ánh đồng thời cả [[default-risk-premium-widens-during-recessions-and-narrows-during-expansions|phần bù rủi ro vỡ nợ (df)]] lẫn phần bù thanh khoản ($lp$); trong thực tế, không có phương pháp kỹ thuật giản đơn nào có thể phân định rạch ròi quy mô tuyệt đối của từng thành phần này (cargill_central_bank_policy, Ch.6, d.1905). Khái niệm phần bù thanh khoản này cũng là nền tảng cốt lõi được mở rộng sang trục thời gian để xây dựng [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản trong cấu trúc kỳ hạn]].

Trong phân tích cấu trúc kỳ hạn hậu khủng hoảng 2008, Moorad Choudhry mở rộng khái niệm này thành phần bù thanh khoản kỳ hạn (term liquidity premium - TLP) để giải thích sự phân tách giữa đường cong hoán đổi OIS và đường cong hoán đổi thông thường (conventional swap curve) (choudhry_analysing_yield_curve, Ch.8, d.3480). Do các khoản vay liên ngân hàng kỳ hạn 3 tháng hoặc 6 tháng chứa đựng rủi ro thiếu hụt thanh khoản cao hơn đáng kể so với việc tái cấp vốn qua đêm, đường cong OIS luôn nằm thấp hơn đường cong hoán đổi LIBOR một khoảng bằng đúng chênh lệch TLP giữa hai kỳ hạn [[dual-curve-discounting-separates-rate-projection-from-collateralized-cash-flow-discounting]]. Hơn nữa, trong hoạt động quản trị nguồn vốn ngân hàng toàn cầu, đường cong phần bù thanh khoản kỳ hạn tiền tệ chéo (cross-currency TLP curve) đóng vai trò định lượng giá trị thanh khoản tương đối giữa các đồng tiền, bảo đảm rằng chi phí thanh khoản ngoại tệ được phản ánh trung thực vào lãi suất chuyển vốn nội bộ [[cross-currency-basis-and-quanto-adjustments-align-internal-funding-curves-across-currencies]].

