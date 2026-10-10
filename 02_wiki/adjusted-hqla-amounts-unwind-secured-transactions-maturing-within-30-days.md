---
title: adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days
type: concept
tags: [lcr, basel-iii, liquidity-regulation, hqla, repo]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Số điều chỉnh (adjusted amount) của một cấp HQLA là lượng tài sản cấp đó mà ngân hàng sẽ có sau khi tháo ngược mọi giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm ngắn hạn có trao đổi HQLA (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Giao dịch ngắn hạn ở đây là giao dịch đáo hạn trong vòng 30 ngày lịch, tính cả ngày thứ 30. Mỗi cấp có một số điều chỉnh riêng. Số điều chỉnh của [[level-1-assets|Level 1]] tháo ngược các giao dịch đổi HQLA bất kỳ lấy Level 1, kể cả tiền mặt. Số điều chỉnh của [[level-2a-assets|Level 2A]] và của [[level-2b-assets|Level 2B]] được định nghĩa tương tự cho từng cấp. Tài sản được xét là tài sản đạt, hoặc sẽ đạt nếu không bị ràng buộc, [[hqla-operational-requirements|các yêu cầu vận hành]] ở 30.13 đến 30.25 (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Khi tài sản bảo đảm nhận về từ một giao dịch cho vay có bảo đảm lại được tái thế chấp trong một giao dịch tài trợ có bảo đảm ngắn hạn khác, cả hai giao dịch đều được tháo ngược. Haircut của từng cấp được áp trước khi tính trần (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Số điều chỉnh chỉ dùng để tính [[level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock|trần 40% của Level 2 và trần 15% của Level 2B]] (basel_lcr, LCR30, Definition of HQLA, 30.34, d.220). Phép tháo ngược trả lời câu hỏi cơ cấu kho sẽ ra sao khi các giao dịch ngắn hạn đáo hạn trong kỳ căng thẳng. Minh hoạ ngoài nguồn: ngân hàng repo trái phiếu Level 2A lấy tiền mặt kỳ hạn 7 ngày sẽ có thêm Level 1 trên sổ hôm nay, nhưng số điều chỉnh đưa khoản tiền đó về lại Level 2A. Nhờ vậy ngân hàng không nới được trần bằng [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing|repo]] ngắn hạn quanh ngày báo cáo.
