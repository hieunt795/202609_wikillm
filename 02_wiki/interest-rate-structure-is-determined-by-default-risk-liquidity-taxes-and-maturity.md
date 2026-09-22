---
title: interest-rate-structure-is-determined-by-default-risk-liquidity-taxes-and-maturity
type: concept
tags: [interest-rates, term-structure, yield-curve, bond-market]
sources: [cargill_central_bank_policy]
status: stable
last_updated: 2026-09-21
---

Cấu trúc lãi suất (structure of interest rates) mô tả mối quan hệ giữa các mức lãi suất khác nhau tại một thời điểm nhất định và cách thức mối quan hệ này biến đổi theo thời gian (cargill_central_bank_policy, Ch.6, Introduction, d.1851). Khác với mặt bằng lãi suất chung được xác lập trong [[loanable-funds-framework-determines-equilibrium-interest-rate-and-bond-price|khung quỹ cho vay]], các công cụ nợ cụ thể trên thị trường tài chính phân hóa mạnh mẽ về mức sinh lời dựa trên bốn yếu tố quyết định căn bản: rủi ro vỡ nợ (default risk), tính thanh khoản (liquidity / marketability), chế độ thuế (tax treatment), và kỳ hạn đáo hạn (maturity) (cargill_central_bank_policy, Ch.6, d.1853).

Để cô lập và định lượng tác động của từng yếu tố, phương pháp phân tích chuẩn tắc là so sánh lợi suất của hai chứng khoán bằng cách giữ cố định ba yếu tố còn lại (cargill_central_bank_policy, Ch.6, d.1855):
- Chứng khoán kho bạc chính phủ (Treasury constant maturities) được chọn làm chuẩn mực tham chiếu nền tảng (benchmark), bởi chúng có rủi ro vỡ nợ thực tế bằng không ($df = 0$), sở hữu tính thanh khoản thứ cấp cao nhất ($lp = 0$), chịu cùng một chế độ thuế đồng nhất, và có sẵn dữ liệu liên tục cho một dải kỳ hạn rất rộng (cargill_central_bank_policy, Ch.6, d.1861).
- So sánh chứng khoán chịu rủi ro với chứng khoán kho bạc cùng kỳ hạn, thanh khoản và thuế cho phép bóc tách [[default-risk-premium-widens-during-recessions-and-narrows-during-expansions|phần bù rủi ro vỡ nợ]].
- So sánh chứng khoán kém thanh khoản với chứng khoán có thanh khoản vượt trội cho phép xác định [[liquidity-premium-compensates-for-secondary-market-depth-and-transaction-costs|phần bù thanh khoản]].
- So sánh trái phiếu chịu thuế với trái phiếu được miễn thuế giúp giải mã tác động của [[tax-exemption-lowers-municipal-bond-yields-and-reveals-implicit-marginal-tax-rates|chế độ thuế và thuế suất biên ngầm]].
- So sánh các chứng khoán có kỳ hạn khác nhau khi giữ cố định ba yếu tố còn lại hình thành nên cấu trúc kỳ hạn của lãi suất (term structure of interest rates), được giải thích qua [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates|giả thuyết kỳ vọng thuần túy]] và [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản]].

Bốn yếu tố cấu trúc này được tích hợp toàn diện vào [[fisher-effect-shifts-nominal-interest-rates-one-to-one-with-expected-inflation|phương trình Fisher]] mở rộng để xác định lãi suất danh nghĩa trước thuế ($nr$) của bất kỳ công cụ tài chính nào:
$$nr = \frac{rr + P^e + df + lp}{1 - tr}$$
Trong đó $rr$ là lãi suất thực phi rủi ro, $P^e$ là tỷ lệ lạm phát kỳ vọng, $df$ là phần bù rủi ro vỡ nợ, $lp$ là phần bù thanh khoản, và $tr$ là thuế suất biên áp dụng (cargill_central_bank_policy, Ch.6, Extended Fisher Relationship, d.1889–1897, d.1907–1911, d.1925–1929). Đối với chứng khoán kho bạc, $df = 0$ và $lp = 0$; đối với trái phiếu chính quyền địa phương, $tr = 0$. Mô hình tổng quát này là chìa khóa giải mã toàn bộ phổ lãi suất trên thị trường tài chính hiện đại.
