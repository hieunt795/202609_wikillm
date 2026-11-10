---
title: funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks
type: concept
tags: [alm, ftp, treasury, balance-sheet, nim, risk-management]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
has_part: [matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions, funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads, ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation]
governs: [interest-rate-risk-in-the-banking-book-irrbb]
driven_by: [rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]
contrasts: [funds-transfer-pricing-contrasts-with-derivatives-funding-value-adjustments]
related: [climate-risk-transmission-channels-impact-bank-balance-sheets-and-ftp-pricing, alm-balance-sheet-balancing-progresses-through-four-operational-dimensions, bank-steering-rules-run-from-internal-funds-transfer-pricing-to-eu-irrbb-measurement-outlier-tests-and-reporting]
---

Định giá chuyển vốn nội bộ (funds transfer pricing, FTP) là một quy trình nội bộ gán lãi suất tài trợ cho từng vị thế bên tài sản và lãi suất thu nhập cho từng vị thế bên nợ trong sổ ngân hàng (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1583). Nguồn dựa trên nguyên tắc chi phí cơ hội: không thể coi nguồn tài trợ là miễn phí vì ngân hàng đang có thanh khoản dư, bởi thanh khoản dùng để tài trợ một khoản vay thì không còn dùng được để trả nợ của ngân hàng, và phần lãi tiết kiệm được từ việc trả nợ bị bỏ lỡ (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1585). Dùng một lãi suất duy nhất, như chi phí vốn bình quân gia quyền (WACC), cho mọi tài sản và nợ cũng không phù hợp, vì tài sản dài hạn cần nguồn dài hạn, loại nguồn thường đắt hơn nguồn ngắn hạn (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1585).

Khi đã có lãi suất phản ánh đúng việc tài trợ của từng vị thế, thu nhập lãi của vị thế được phân bổ nội bộ (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1587). Mảng khách hàng nhận phần thu nhập đến từ khả năng đạt lãi suất khách hàng tốt hơn thị trường, và không phải lo việc tài trợ (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1587). Treasury nhận phần thu nhập đến từ việc vay hoặc đầu tư vốn ở lãi suất thị trường hiện hành, và không phải lo lãi suất khách hàng của từng giao dịch (tata_bank_alm, Ch.2, Funds Transfer Pricing, d.1587).

Nguồn nêu ba chức năng của FTP (tata_bank_alm, Ch.2, Steering the Bank's Customer Business, d.1679–1682):
1. **Phân bổ biên lãi thuần** cho các đơn vị kinh doanh, bằng phương pháp ở trang [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]];
2. **Tập trung rủi ro lãi suất và rủi ro thanh khoản về Treasury** ở một giá chuyển giao phù hợp với mức rủi ro của vị thế; hai thành phần của giá đó nằm ở trang [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], và rủi ro lãi suất được chuyển về là [[interest-rate-risk-in-the-banking-book-irrbb|IRRBB]];
3. **Điều hướng nghiệp vụ khách hàng** và tác động tới diễn biến cấu trúc bảng cân đối, chức năng mà nguồn gọi là có thể có, ở trang [[ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation]].

Với tiền gửi thanh toán, lãi suất cơ hội bình quân trượt của danh mục cuốn chiếu ở trang [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]] được Treasury chuyển cho bộ phận khách hàng làm lãi suất FTP; biên của bộ phận quản tiền gửi bằng lãi suất đó trừ lãi suất đang trả khách hàng (tata_bank_alm, Ch.2, Rolling Portfolio, d.1893). Nguồn kết luận FTP là công cụ đo kết quả và khả năng sinh lời đã điều chỉnh rủi ro, và việc phân bổ biên lãi thuần trên cơ sở đó gắn hoạt động của đơn vị kinh doanh với khẩu vị rủi ro chung của ngân hàng (tata_bank_alm, Ch.2, Conclusion, d.1768). Trang [[funds-transfer-pricing-contrasts-with-derivatives-funding-value-adjustments]] phân biệt FTP với các điều chỉnh giá trị tài trợ của phái sinh. Trang [[climate-risk-transmission-channels-impact-bank-balance-sheets-and-ftp-pricing]] ghi ý của nguồn về việc lãi suất FTP phạt các mảng tập trung rủi ro khí hậu (tata_bank_alm, Ch.6, §6.4, d.3182). Các bước cân đối bảng cân đối mà Treasury thực hiện sau khi nhận rủi ro nằm ở trang [[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]]. Trang [[bank-steering-rules-run-from-internal-funds-transfer-pricing-to-eu-irrbb-measurement-outlier-tests-and-reporting]] xếp trang này cùng các trang khác về FTP và về quy định IRRBB của EU.
