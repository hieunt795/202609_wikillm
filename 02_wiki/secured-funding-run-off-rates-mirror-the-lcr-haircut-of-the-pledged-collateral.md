---
title: secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-outflows, secured-funding, haircut]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
reviewed: 2026-10-13
reviewed_by: model
part_of: [secured-funding]
analogous: [level-2a-assets, level-2b-assets, secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]
related: [the-lcr-scenario-assumes-only-hqla-backed-or-public-counterparty-secured-funding-rolls-over, adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days, short-selling, haircut]
---

Với mọi giao dịch [[secured-funding|tài trợ có bảo đảm]] đang còn và đáo hạn trong 30 ngày lịch của kịch bản, LCR áp một hệ số dòng ra theo loại tài sản bảo đảm và loại đối tác (basel_lcr, LCR40, Secured funding run-off, 40.46 và 40.48, d.917, d.944–951):

| Giao dịch đáo hạn | Cộng vào dòng ra |
|---|---|
| Bảo đảm bằng tài sản Level 1, hoặc với ngân hàng trung ương | 0% |
| Bảo đảm bằng tài sản Level 2A | 15% |
| Với chính phủ trong nước, PSE có trọng số rủi ro từ 20% trở xuống hoặc ngân hàng phát triển đa phương, không bảo đảm bằng Level 1 hay 2A | 25% |
| Bảo đảm bằng RMBS đủ điều kiện Level 2B | 25% |
| Bảo đảm bằng tài sản Level 2B khác | 50% |
| Còn lại | 100% |

Các mức 15%, 25% và 50% trùng với [[haircut]] của [[level-2a-assets|Level 2A]] và [[level-2b-assets|Level 2B]] ở tử số: chuẩn mực viết rằng mức giảm khả năng vay với tài sản Level 2 tương đương haircut bắt buộc (basel_lcr, LCR40, Secured funding run-off, 40.47, d.933). Lý do của từng giả định nằm ở trang [[the-lcr-scenario-assumes-only-hqla-backed-or-public-counterparty-secured-funding-rolls-over]].

Dòng ra được tính trên số tiền huy động qua giao dịch, không trên giá trị của tài sản bảo đảm (basel_lcr, LCR40, Secured funding run-off, 40.46, d.917). Mức 100% gồm cả giao dịch trong đó ngân hàng đáp ứng vị thế [[short-selling|bán khống]] của khách hàng bằng chính tồn kho của mình (basel_lcr, LCR40, Secured funding run-off, 40.48, d.942). Cách xử lý ưu đãi chỉ áp cho giao dịch đang còn: tài sản bảo đảm chưa dùng, hoặc chỉ là năng lực vay, xác định vào cuối ngày báo cáo ở nước liên quan, không được tính (basel_lcr, LCR40, Secured funding run-off, 40.47 và FAQ1, d.933–936).

Các giao dịch được báo cáo theo tài sản thực tế đã cầm cố tại thời điểm đóng cửa của ngày tính LCR (basel_lcr, LCR40, Secured funding run-off, 40.48, d.942). Khi ngân hàng cầm cố một rổ tài sản và không xác định được tài sản nào bảo đảm cho các giao dịch còn kỳ hạn trên 30 ngày, ngân hàng được giả định tài sản bị ràng buộc theo thứ tự giá trị thanh khoản tăng dần: tài sản có giá trị thanh khoản thấp nhất trong LCR được gán trước cho giao dịch có kỳ hạn còn lại dài nhất (basel_lcr, LCR40, Secured funding run-off, 40.48, d.942). Cùng các giao dịch này, nhìn từ tử số, được tháo ngược khi tính trần Level 2 ở trang [[adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days]]. Bảng đối xứng ở vế dòng vào, cho các giao dịch cho vay có bảo đảm đáo hạn, nằm ở trang [[secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]].
