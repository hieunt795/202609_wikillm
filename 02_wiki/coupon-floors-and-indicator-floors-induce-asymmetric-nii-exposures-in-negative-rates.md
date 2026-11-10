---
title: coupon-floors-and-indicator-floors-induce-asymmetric-nii-exposures-in-negative-rates
type: concept
tags: [alm, coupon-floor, indicator-floor, negative-rates, nii, embedded-options]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]
related: [embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap, net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons, contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]
---

Có hai kiểu sàn 0%, tùy đặc điểm hợp đồng và cách luật bảo vệ người tiêu dùng được áp dụng: sàn coupon (*coupon floor*) và sàn chỉ báo (*indicator floor*) (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429); bối cảnh lãi suất âm của chúng nằm ở trang [[zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp]]. Với sàn coupon, lãi suất của khách hàng không thể xuống dưới 0%, nhưng lãi suất chỉ báo vẫn được âm miễn là biên cộng thêm giữ lãi suất khách hàng không âm:
$$r_{customer} = \max(r_I + x; 0\%)$$
Khách hàng không bị tính lãi âm nhưng có thể không nhận đủ biên $x$ kỳ vọng; ví dụ là tài khoản tiết kiệm bán lẻ (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429). Với sàn chỉ báo, chính lãi suất chỉ báo không thể thấp hơn 0%:
$$r_{customer} = \max(r_I; 0\%) + x$$
Biên $x$ được bảo vệ cả khi lãi suất chỉ báo xuống dưới 0%; ví dụ là khoản vay doanh nghiệp có điều khoản tương ứng (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429).

Sàn 0% tốt hay xấu với ngân hàng tùy nó gắn vào tài sản hay nợ (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2433). Sàn coupon bất lợi ở bên nợ, vì giới hạn khả năng tính lãi âm trên giao dịch huy động, và có lợi ở bên tài sản, vì ngân hàng không phải trả lãi âm trên khoản đầu tư (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2433). Nếu ngân hàng có sàn chỉ báo ở tài sản và sàn coupon ở nợ, môi trường lãi suất âm có lợi khi các yếu tố khác không đổi; nếu có sàn coupon ở tài sản và sàn chỉ báo ở nợ, môi trường đó gây lỗ tiềm ẩn (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2435).

Chú thích của nguồn minh hoạ trường hợp sau. Ngân hàng đầu tư ở $r_I + x$ và huy động cũng ở $r_I + x$; NII bằng 0 ở mọi mức lãi suất chỉ báo (tata_bank_alm, Ch.3, Notes, d.2512). Khi tài sản chịu sàn coupon và nợ chịu sàn chỉ báo:
$$NII = \max(r_I + x; 0) - [\max(r_I; 0) + x]$$
NII bằng 0 khi $r_I > 0$, bằng $r_I$ khi $-x \le r_I \le 0$, và bằng $-x$ khi $r_I < -x$; bản nguồn in thiếu dấu ở hai vế sau, kết quả ở đây tính từ công thức. NII vì vậy không lần nào dương và âm khi lãi suất chỉ báo âm (tata_bank_alm, Ch.3, Notes, d.2512).

Hai kiểu sàn là quyền chọn gắn trong hợp đồng, thuộc loại rủi ro ở trang [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]], và trang [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]] mô tả nhóm quyền chọn hành vi mà sàn tiền gửi bán lẻ thuộc về. Kế hoạch NII theo nhiều kịch bản lãi suất, nơi tác động của sàn hiện ra, nằm ở trang [[net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]]. Việc tính chi phí quyền chọn vào giá vốn nội bộ nằm ở trang [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]].
