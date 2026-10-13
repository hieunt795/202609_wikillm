---
title: collateral-swaps-are-treated-as-repo-or-reverse-repo-in-the-lcr
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-outflows, secured-funding, collateral-swap]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
reviewed: 2026-10-13
reviewed_by: model
part_of: [secured-funding]
governed_by: [secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]
contrasts: [securities-lending-programmes-and-central-bank-collateral-swaps]
related: [adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days]
---

Trong LCR, hoán đổi tài sản bảo đảm (collateral swap) được xử lý như hợp đồng repo hoặc repo đảo chiều, và mọi giao dịch khác có hình thức tương tự cũng vậy (basel_lcr, LCR40, Secured funding run-off, 40.46, d.917). Quy tắc này đưa hoán đổi tài sản bảo đảm vào khối [[secured-funding|tài trợ có bảo đảm]], nên phần đáo hạn trong 30 ngày chịu tỷ lệ run-off theo tài sản đã cầm cố ở trang [[secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]].

Cùng nhóm giao dịch này cũng xuất hiện ở tử số: khi tính trần Level 2, các hoán đổi tài sản bảo đảm đáo hạn trong 30 ngày được tháo ngược theo cách ở trang [[adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days]]. Hoán đổi tài sản bảo đảm do ngân hàng trung ương thực hiện, một công cụ khác với giao dịch giữa các bên thị trường nói ở đây, nằm ở trang [[securities-lending-programmes-and-central-bank-collateral-swaps]].
