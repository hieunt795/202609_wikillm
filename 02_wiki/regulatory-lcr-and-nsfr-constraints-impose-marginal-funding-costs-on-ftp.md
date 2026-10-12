---
title: regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp
type: concept
tags: [alm, ftp, lcr, nsfr, basel-iii, regulation, ccp, margining]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]
driven_by: [liquidity-coverage-ratio-lcr]
related: [funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks, lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days, ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding, contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons, liquidity-risk]
---

Sau khủng hoảng thị trường tài chính 2007–2008, một loạt yêu cầu quy định được ban hành và tác động tới chi phí tài trợ của cả vị thế nội bảng lẫn ngoại bảng (tata_bank_alm, Ch.2, Regulatory Requirements, d.1700). Mỗi yêu cầu, khi bị một vị thế cần định giá trên đường cong [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks|FTP]] kích hoạt, tạo ra một chi phí biên cho ngân hàng (tata_bank_alm, Ch.2, Regulatory Requirements, d.1700). Ví dụ: nếu phải kéo dài kỳ hạn nguồn vốn, nợ ngắn hạn rẻ phải được thay bằng nợ dài hạn đắt hơn khi đường cong dốc lên; nếu phải ký quỹ cho một giao dịch phái sinh, lãi trên tài khoản ký quỹ có thể thấp hơn chi phí vốn chung của ngân hàng (tata_bank_alm, Ch.2, Regulatory Requirements, d.1700).

Nguồn liệt kê bốn nguồn chi phí chính:
1. **LCR**: [[liquidity-coverage-ratio-lcr|tỷ lệ bao phủ thanh khoản]] yêu cầu ngân hàng giữ đủ tài sản thanh khoản chất lượng cao (HQLA) để chịu được [[lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days|kịch bản căng thẳng 30 ngày]]. Nguồn dẫn ý kiến rằng nếu một vị thế đòi thêm nguồn ngoài chiến lược thông thường, chi phí HQLA tăng thêm nên được định giá chuyển giao; nếu không, nghiệp vụ mới có xu hướng làm xấu LCR (tata_bank_alm, Ch.2, Liquidity Coverage Ratio, d.1704). Một số hệ thống FTP phân bổ chi phí LCR cho cả nợ lẫn tài sản, qua đó khuyến khích tài sản tạo dòng vào LCR (tata_bank_alm, Ch.2, Liquidity Coverage Ratio, d.1706);
2. **NSFR**: tỷ lệ nguồn vốn ổn định ròng yêu cầu cơ cấu nguồn ổn định tương ứng với thành phần tài sản và hoạt động ngoại bảng. Một số vị thế, như phái sinh, không cần tài trợ thường xuyên nhưng làm xấu NSFR và có thể buộc ngân hàng huy động thêm vốn dài hạn đắt hơn; nguồn cho rằng các vị thế tác động tới NSFR nên bị phạt trên đường cong FTP (tata_bank_alm, Ch.2, Net Stable Funding Ratio, d.1710);
3. **Nghĩa vụ bù trừ**: phái sinh OTC chuẩn hóa phải bù trừ qua đối tác bù trừ trung tâm (CCP), kéo theo chi phí tài trợ do yêu cầu ký quỹ của CCP (tata_bank_alm, Ch.2, Clearing Mandate, d.1714); cơ chế ký quỹ của CCP nằm ở trang [[ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding]];
4. **Yêu cầu ký quỹ** cho phái sinh không bù trừ tập trung, cũng tạo thêm chi phí (tata_bank_alm, Ch.2, Margin Requirements, d.1718–1720).

Các chi phí này cộng vào đường cong hai thành phần ở trang [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], cùng các phụ phí thanh khoản dự phòng và quyền chọn ở trang [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]]. LCR và NSFR là hai tỷ lệ quy định về [[liquidity-risk|rủi ro thanh khoản]].
