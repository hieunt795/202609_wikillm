---
title: collateral-re-used-to-cover-short-positions-earns-no-inflow-and-triggers-no-outflow
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-inflows, secured-lending, short-selling, rehypothecation]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
part_of: [secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]
related: [collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties, customer-short-positions-are-treated-as-secured-funding-because-the-customer-controls-them, firm-short-positions-covered-by-unsecured-borrowing-run-off-in-full]
---

Nếu tài sản bảo đảm nhận qua repo đảo chiều, vay chứng khoán hoặc hoán đổi tài sản bảo đảm đáo hạn trong 30 ngày đã bị dùng lại, tức tái thế chấp, để phủ các vị thế bán khống có thể kéo dài quá 30 ngày, ngân hàng phải giả định giao dịch đó được quay vòng và không tạo dòng tiền vào (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1205). Lý do là ngân hàng vẫn phải tiếp tục phủ vị thế bán khống hoặc mua lại chứng khoán. Vị thế bán khống được xử lý đối xứng và không tạo dòng ra (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1205). Đây là cột 0% trong bảng ở trang [[secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]]; tái thế chấp nằm ở trang [[collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties]].

Vị thế bán khống ở đây gồm hai trường hợp: ngân hàng bán khống hẳn một chứng khoán trong chiến lược giao dịch hoặc phòng hộ; và ngân hàng thiếu một chứng khoán trong sổ repo khớp lệnh (matched book), tức đã mượn chứng khoán trong một kỳ và cho mượn nó trong một kỳ dài hơn (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1205). Vị thế được đánh giá vào cuối ngày tính; khả năng thay tài sản bảo đảm trong giao dịch tạo ra vị thế bán khống không được xét khi xác định tỷ lệ dòng vào (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1205).

Một câu hỏi thường gặp làm rõ phạm vi: tỷ lệ 0% áp cho mọi repo đảo chiều, vay chứng khoán hoặc hoán đổi tài sản bảo đảm mà tài sản nhận về được dùng để phủ vị thế bán khống, không chỉ khi vị thế còn kỳ hạn trên 30 ngày (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79 FAQ2, d.1224–1226). Cụm "có thể kéo dài quá 30 ngày" nhằm nhắc rằng vị thế có thể được gia hạn, khi đó ngân hàng phải quay vòng giao dịch cho vay hoặc mua chứng khoán; cả hai cách đều không cho dòng tiền vào tính được trong LCR (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79 FAQ2, d.1226). Vị thế của khách hàng và vị thế của chính ngân hàng được xử lý riêng, ở trang [[customer-short-positions-are-treated-as-secured-funding-because-the-customer-controls-them]] và trang [[firm-short-positions-covered-by-unsecured-borrowing-run-off-in-full]].
