---
title: secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-inflows, secured-lending, reverse-repo]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
part_of: [total-expected-cash-inflows]
has_part: [margin-loans-against-non-hqla-collateral-yield-at-most-a-50-percent-inflow, collateral-re-used-to-cover-short-positions-earns-no-inflow-and-triggers-no-outflow]
analogous: [secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]
related: [level-1-assets, banks-must-be-able-to-return-collateral-regardless-of-lcr-rollover-assumptions]
---

Với các giao dịch cho vay có bảo đảm đáo hạn trong 30 ngày, gồm repo đảo chiều và vay chứng khoán, LCR đặt tỷ lệ dòng vào theo loại tài sản bảo đảm (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1207–1214):

| Tài sản bảo đảm | Tài sản không dùng để phủ vị thế bán khống | Tài sản dùng để phủ vị thế bán khống |
|---|---|---|
| Level 1 | 0% | 0% |
| Level 2A | 15% | 0% |
| Level 2B: RMBS đủ điều kiện | 25% | 0% |
| Level 2B: loại khác | 50% | 0% |
| Cho vay ký quỹ trên tài sản bảo đảm khác | 50% | 0% |
| Tài sản bảo đảm khác | 100% | 0% |

Đây là một nhóm của [[total-expected-cash-inflows|tổng dòng vào dự kiến]].

Lập luận của chuẩn mực đi theo giả định quay vòng. Giao dịch bảo đảm bằng [[level-1-assets|tài sản Level 1]] được giả định quay vòng và không tạo dòng tiền vào (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78, d.1199). Giao dịch bảo đảm bằng HQLA Level 2 tạo dòng vào bằng haircut của tài sản đó (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78, d.1199). Giao dịch bảo đảm bằng tài sản không phải HQLA được giả định không quay vòng, nên ngân hàng nhận lại 100% tiền (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78, d.1199). Chuẩn mực ghi cách xử lý này khớp với các giả định cho tài trợ có bảo đảm ở vế dòng ra (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78, d.1199): cùng một loại tài sản bảo đảm cho cùng một tỷ lệ ở hai bảng, như ở trang [[secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]].

Bảng chỉ áp cho khoản vay có bảo đảm có kỳ hạn hợp đồng tới và gồm 30 ngày (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78 FAQ1, d.1203). Hai trường hợp riêng có trang riêng: cho vay ký quỹ, ở trang [[margin-loans-against-non-hqla-collateral-yield-at-most-a-50-percent-inflow]], và cột thứ ba của bảng, khi tài sản bảo đảm nhận về bị dùng lại để phủ vị thế bán khống, ở trang [[collateral-re-used-to-cover-short-positions-earns-no-inflow-and-triggers-no-outflow]]. Giả định quay vòng không miễn cho ngân hàng nghĩa vụ trả lại tài sản bảo đảm, ở trang [[banks-must-be-able-to-return-collateral-regardless-of-lcr-rollover-assumptions]].
