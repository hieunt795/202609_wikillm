---
title: the-money-multiplier-links-reserve-money-to-the-money-supply
type: concept
tags: [monetary-policy, identities]
sources: [imf_macro_accounting, cargill_central_bank_policy]
status: stable
last_updated: 2026-09-24
---

Dưới hệ thống dự trữ phân đoạn, mức tăng ban đầu của [[reserve-money|tiền cơ sở]] làm nền cho [[deposit-money-banks|ngân hàng nhận tiền gửi]] mở rộng tiếp tiền gửi thành một bội số của mức tăng đó, vì mỗi khoản tiền gửi chỉ cần giữ lại một phần làm dự trữ, phần còn lại được cho vay và cuối cùng lại trở thành tiền gửi mới (imf_macro_accounting, Ch.5, The Concept of the Money Multiplier, d.4937–4942).

Với $RM = CY + R$ ([[currency-in-circulation|tiền mặt]] cộng dự trữ ngân hàng) và $M = CY + DD$ (tiền mặt cộng [[demand-deposits|tiền gửi không kỳ hạn]]), số nhân tiền là

$$mm = \frac{M}{RM} = \frac{CY+DD}{CY+R}$$

Đặt $c$ là tỷ lệ tiền mặt trên tiền gửi và $r$ là tỷ lệ dự trữ trên tiền gửi, số nhân trở thành $mm = (c+1)/(c+r)$, và cung tiền là $M = mm \cdot RM$: số nhân càng lớn khi tỷ lệ dự trữ bắt buộc càng nhỏ và tỷ lệ tiền mặt trên tiền gửi càng nhỏ (imf_macro_accounting, Ch.5, cùng mục, d.4943–4964).

Dạng tổng quát hơn tách tỷ lệ dự trữ theo loại tiền gửi ([[required-reserves|dự trữ bắt buộc]] trên tiền gửi không kỳ hạn $r_d$, trên tiền gửi có kỳ hạn $r_t$, và [[excess-reserves|dự trữ vượt mức]] $r_e$) cho $mm = (c+1+b)/(c+r_d+br_t+r_e)$, với $b$ là tỷ lệ tiền gửi có kỳ hạn trên tiền gửi không kỳ hạn (imf_macro_accounting, Ch.5, cùng mục, d.4965–4980). Trên bảng cân đối thực tế của một DMB, $r$ (gộp [[required-reserves|dự trữ bắt buộc]] và [[excess-reserves|dự trữ vượt mức]]) chính là khoản "Dự trữ" tách thành hai dòng Required/Excess ở [[the-analytical-deposit-money-bank-balance-sheet-separates-required-from-excess-reserves]]. Số nhân vì vậy không cố định theo thời gian mà phản ánh hành vi của ba nhóm tác nhân khác nhau: nhà chức trách tiền tệ (đặt tỷ lệ dự trữ bắt buộc), ngân hàng thương mại (chọn mức dự trữ vượt mức), và công chúng phi ngân hàng (chọn tỷ lệ tiền mặt/tiền gửi và cơ cấu tiền gửi) — nghĩa là nhà chức trách tiền tệ không kiểm soát hoàn toàn khối tiền, kể cả khi kiểm soát trọn vẹn tiền cơ sở (imf_macro_accounting, Ch.5, cùng mục, d.4981–4990).

Khung phân tích của Thomas F. Cargill hệ thống hóa quá trình này thành [[money-supply-expansion-stops-when-absorbing-factors-exhaust-high-powered-money|phương trình các yếu tố hấp thụ tiền cơ sở]], trong đó [[currency-deposit-ratio-reflects-opportunity-costs-and-underground-economy-incentives|tỷ lệ tiền mặt trên tiền gửi giao dịch]] ($k$) phản ánh chi phí cơ hội lãi suất và động cơ trốn thuế trong nền kinh tế ngầm, đồng thời khẳng định [[central-bank-controls-the-monetary-base-but-cannot-predictably-control-the-money-supply|ngân hàng trung ương kiểm soát tiền cơ sở nhưng không thể dự đoán kiểm soát cung tiền]]. Thực tiễn hậu khủng hoảng 2008 cho thấy [[money-multiplier-collapsed-post-2008-due-to-interest-on-excess-reserves-and-bank-risk-aversion|số nhân tiền sụp đổ do chính sách trả lãi dự trữ vượt mức (IOER) và tâm lý né tránh rủi ro của các ngân hàng]], khiến các ngân hàng trung ương hiện đại chuyển trọng tâm điều hành từ cung tiền sang lãi suất thị trường (cargill_central_bank_policy, Ch.12, d.3855–3863, d.3985–3994).
