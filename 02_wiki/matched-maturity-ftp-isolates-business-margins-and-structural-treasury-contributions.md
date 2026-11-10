---
title: matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions
type: concept
tags: [alm, ftp, nim, matched-maturity, structural-contribution, treasury]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]
governs: [liquidity-risk]
drives: [interest-rate-gap-risk-stems-from-repricing-timing-mismatches]
related: [funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]
---

Biên lãi thuần (net interest margin, NIM) là chênh lệch giữa thu nhập lãi và chi phí lãi, tính được cho từng vị thế hoặc gộp tới cấp toàn ngân hàng (tata_bank_alm, Ch.2, Net Interest Margin, d.1591). Một phép tính NIM đơn giản không trả lời được cách chia biên giữa bộ phận tiền gửi, nơi huy động vốn, và bộ phận cho vay, nơi cho vay tương ứng; việc chia đó cần một hệ thống [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks|FTP]] (tata_bank_alm, Ch.2, Net Interest Margin, d.1599). Trong phương pháp khớp kỳ hạn (*matched maturity*), mỗi vị thế tài sản hoặc nợ mới phát sinh được gán một lãi suất FTP lấy từ đường cong giá chuyển giao ở đúng kỳ hạn của vị thế (tata_bank_alm, Ch.2, Transfer Price Curve, d.1617).

Ví dụ của nguồn: bộ phận tiền gửi nhận một khoản tiền gửi 1 năm ở 1%, bộ phận cho vay cho vay 2 năm ở 4%, nên NIM năm đầu là 3% mỗi năm (tata_bank_alm, Ch.2, Transfer Price Curve, d.1623). Lãi suất tiền gửi 1 năm được so với lãi suất chuyển giao nội bộ 1 năm là 2%, cho biên đóng góp của mảng tiền gửi là 1%; lãi suất cho vay 2 năm được so với lãi suất chuyển giao 2 năm là 3%, cho biên đóng góp của bộ phận cho vay là 1% (tata_bank_alm, Ch.2, Transfer Price Curve, d.1623). Chênh lệch giữa lãi suất 1 năm và 2 năm trên đường cong FTP gọi là đóng góp cấu trúc (*structural contribution*) (tata_bank_alm, Ch.2, Transfer Price Curve, d.1623).

Đóng góp cấu trúc là khoản bù cho Treasury vì nhận hai rủi ro, rủi ro thanh khoản và rủi ro lãi suất (tata_bank_alm, Ch.2, Structural Contribution, d.1631). Hết kỳ 1 năm, vị thế tiền gửi phải được quay vòng vì vốn còn nằm thêm một năm trong khoản vay 2 năm; nếu không quay vòng được, ngân hàng thiếu thanh khoản. Đó là rủi ro tái tài trợ, một dạng của [[liquidity-risk|rủi ro thanh khoản]] (tata_bank_alm, Ch.2, Structural Contribution, d.1633). Lãi suất của khoản nợ chỉ cố định trong 1 năm; nếu lãi suất tăng ở năm thứ hai, tiền gửi được quay vòng ở lãi suất cao hơn và biên lãi thuần bị bào mòn. Đó là rủi ro lãi suất, thuộc loại ở trang [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]] (tata_bank_alm, Ch.2, Structural Contribution, d.1633). Cách tách đường cong FTP thành phần lãi suất và phần thanh khoản nằm ở trang [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]].
