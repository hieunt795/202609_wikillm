---
title: adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days
type: concept
tags: [lcr, basel-iii, liquidity-regulation, hqla, repo]
sources: [basel_lcr, tt50_2026_sbv]
status: draft
last_updated: 2026-11-14
reviewed: 2026-11-14
reviewed_by: model
governs: [level-1-assets, level-2a-assets, level-2b-assets]
governed_by: [hqla-operational-requirements]
drives: [level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock]
related: [general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing, secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]
---

Số điều chỉnh (adjusted amount) của một cấp HQLA là lượng tài sản cấp đó mà ngân hàng sẽ có sau khi tháo ngược mọi giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm ngắn hạn có trao đổi HQLA (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Giao dịch ngắn hạn ở đây là giao dịch đáo hạn trong vòng 30 ngày lịch, tính cả ngày thứ 30. Mỗi cấp có một số điều chỉnh riêng. Số điều chỉnh của [[level-1-assets|Level 1]] tháo ngược các giao dịch đổi HQLA bất kỳ lấy Level 1, kể cả tiền mặt. Số điều chỉnh của [[level-2a-assets|Level 2A]] và của [[level-2b-assets|Level 2B]] được định nghĩa tương tự cho từng cấp. Tài sản được xét là tài sản đạt, hoặc sẽ đạt nếu không bị ràng buộc, [[hqla-operational-requirements|các yêu cầu vận hành]] ở 30.13 đến 30.25 (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Khi tài sản bảo đảm nhận về từ một giao dịch cho vay có bảo đảm lại được tái thế chấp trong một giao dịch tài trợ có bảo đảm ngắn hạn khác, cả hai giao dịch đều được tháo ngược. Haircut của từng cấp được áp trước khi tính trần (basel_lcr, LCR30, Definition of HQLA, 30.37, d.227).

Số điều chỉnh chỉ dùng để tính [[level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock|trần 40% của Level 2 và trần 15% của Level 2B]] (basel_lcr, LCR30, Definition of HQLA, 30.34, d.220). Phép tháo ngược trả lời câu hỏi cơ cấu kho sẽ ra sao khi các giao dịch ngắn hạn đáo hạn trong kỳ căng thẳng. Minh hoạ ngoài nguồn: ngân hàng repo trái phiếu Level 2A lấy tiền mặt kỳ hạn 7 ngày sẽ có thêm Level 1 trên sổ hôm nay, nhưng số điều chỉnh đưa khoản tiền đó về lại Level 2A. Suy từ quy tắc, nguồn không nói thẳng: nhờ vậy ngân hàng không nới được trần bằng [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing|repo]] ngắn hạn quanh ngày báo cáo. Cùng các giao dịch này, nhìn từ mẫu số, chịu tỷ lệ run-off ở trang [[secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]].

TT50 nêu cùng quy tắc ở Phụ lục I. Giá trị điều chỉnh là giá trị HQLA đủ tiêu chuẩn sau khi hoàn tất việc đảo ngược các giao dịch có bảo đảm bằng tài sản tài chính hoặc repo, reverse repo đáo hạn trong 30 ngày có trao đổi HQLA với tài sản cấp 1 kể cả tiền mặt, cấp 2A hoặc cấp 2B (tt50_2026_sbv, Phụ lục I, Phần A, mục I khoản 3b(i), d.1153). Ngân hàng đảo ngược cả hai giao dịch khi tài sản bảo đảm nhận từ một khoản cấp tín dụng có bảo đảm trong 30 ngày được thế chấp lại cho đối tác khác, hoặc khi tài sản nhận từ repo, reverse repo trong 30 ngày được dùng bảo đảm nghĩa vụ với đối tác khác; ở cả hai trường hợp, giao dịch thứ hai cũng phải đáo hạn trong 30 ngày (tt50_2026_sbv, Phụ lục I, Phần A, mục I khoản 3b(ii), d.1155–1159). Nếu không có giao dịch nào cần đảo ngược, số điều chỉnh bằng số chưa điều chỉnh (tt50_2026_sbv, Phụ lục I, Phần A, mục I khoản 3c, d.1161).

Ví dụ trong Thông tư: ngân hàng A có 100 tỷ đồng tiền mặt và đã repo một tài sản cấp 2A, cam kết mua lại trong 30 ngày với giá 40 tỷ đồng. Đảo ngược cho 60 tỷ đồng tiền mặt và 40 tỷ đồng tài sản cấp 2A. Nếu tài sản cấp 2A đạt yêu cầu vận hành, KĐC.L1 là 60 tỷ và KĐC.L2A là 40 × 85% = 34 tỷ. Nếu không đạt, KĐC.L2A bằng 0 và chỉ còn 60 tỷ cấp 1 (tt50_2026_sbv, Phụ lục I, Phần A, mục I khoản 3, d.1163–1183). Công thức dùng các số điều chỉnh này nằm ở [[level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock]].
