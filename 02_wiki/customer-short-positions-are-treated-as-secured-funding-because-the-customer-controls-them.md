---
title: customer-short-positions-are-treated-as-secured-funding-because-the-customer-controls-them
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-outflows, secured-funding, short-selling]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
reviewed: 2026-10-13
reviewed_by: model
part_of: [secured-funding]
governed_by: [secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]
contrasts: [customer-shorts-covered-by-other-customers-collateral-carry-a-minimum-50-percent-run-off, firm-short-positions-covered-by-unsecured-borrowing-run-off-in-full]
related: [collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties]
---

LCR coi tài sản bảo đảm mà ngân hàng cho khách hàng mượn để thực hiện vị thế bán khống là một dạng [[secured-funding|tài trợ có bảo đảm]], kể cả vị thế không có kỳ hạn hợp đồng xác định (basel_lcr, LCR40, Secured funding run-off, 40.46, d.917). Vị thế bán khống của khách hàng là giao dịch trong đó khách hàng của ngân hàng bán một chứng khoán mình không sở hữu, rồi ngân hàng lấy đúng chứng khoán đó từ nguồn nội bộ hoặc bên ngoài để giao cho lệnh bán (basel_lcr, LCR40, Secured funding run-off, 40.46 chú thích, d.923). Nguồn nội bộ gồm tồn kho tài sản bảo đảm của chính ngân hàng và tài sản bảo đảm được phép tái thế chấp nằm trong tài khoản ký quỹ của khách hàng khác; nguồn bên ngoài gồm tài sản có được qua vay chứng khoán, repo đảo chiều hoặc giao dịch tương tự (basel_lcr, LCR40, Secured funding run-off, 40.46 chú thích, d.923–925). Chuỗi tái thế chấp nằm ở trang [[collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties]].

Chuẩn mực xử lý vị thế bán khống của khách hàng tách khỏi vị thế bán khống của chính ngân hàng, và giải thích lý do trong một câu hỏi thường gặp (basel_lcr, LCR40, Secured funding run-off, 40.46 FAQ1, d.929–931). Tiền thu từ lệnh bán khống của khách hàng có thể được ngân hàng dùng lại để tài trợ việc mua hoặc vay chứng khoán bị bán khống, nên vị thế này tương đương các giao dịch tài trợ có bảo đảm khác. Khác với vị thế của ngân hàng, vị thế của khách hàng được mở và giữ theo ý khách hàng, nên nguồn tài trợ này có thể không chắc chắn trong giai đoạn căng thẳng (basel_lcr, LCR40, Secured funding run-off, 40.46 FAQ1, d.931). Khi ngân hàng đáp ứng vị thế của khách hàng bằng tồn kho của chính mình, giao dịch chịu hệ số 100% ở trang [[secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]] (basel_lcr, LCR40, Secured funding run-off, 40.48, d.942). Trường hợp vị thế được phủ bằng tài sản bảo đảm của khách hàng khác, một nghĩa vụ ngoài hợp đồng, nằm ở trang [[customer-shorts-covered-by-other-customers-collateral-carry-a-minimum-50-percent-run-off]]. Vị thế bán khống của chính ngân hàng theo quy tắc khác, ở trang [[firm-short-positions-covered-by-unsecured-borrowing-run-off-in-full]].
