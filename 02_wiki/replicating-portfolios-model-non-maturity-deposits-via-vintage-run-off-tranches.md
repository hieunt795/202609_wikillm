---
title: replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches
type: concept
tags: [alm, replicating-portfolio, vintage-run-off, non-maturity-deposits, duration, liquidity]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governs: [non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]
related: [modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases, rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates, replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates, sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]
---

Mô hình tái tạo (replicating model), đôi khi gọi là mô hình run-off theo thế hệ (vintage run-off model), tái tạo một sản phẩm không kỳ hạn ở trang [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]] bằng một danh mục gồm chủ yếu các công cụ tài chính thanh khoản và giao dịch được (tata_bank_alm, Ch.2, Replicating Model, d.1847). Diễn biến khối lượng và lãi suất của danh mục tái tạo là xấp xỉ sát thực tế cho hành vi kỳ vọng của sản phẩm (tata_bank_alm, Ch.2, Replicating Model, d.1847). Để quản trị rủi ro cho sản phẩm không kỳ hạn, ngân hàng phải đặt giả định về run-off, tức mức suy giảm của tiền gửi trên các tài khoản hiện có theo thời gian (tata_bank_alm, Ch.2, Intuition, d.1851).

Ví dụ của nguồn là một vị thế tiền gửi thanh toán 50 triệu EUR không có nghiệp vụ thay thế (tata_bank_alm, Ch.2, Intuition, d.1853). Khoảng 10 triệu EUR bị rút trong tháng tới, chẳng hạn từ khách hàng chỉ gửi tạm ngắn hạn; 40 triệu EUR còn lại bị rút thành các phần bằng nhau trong 5 năm, tức 8 triệu EUR mỗi năm (tata_bank_alm, Ch.2, Intuition, d.1853). Sổ tiền gửi trước đó đồng nhất được mô hình hóa thành một danh mục sáu vị thế tiền gửi có kỳ hạn kỳ vọng khác nhau (tata_bank_alm, Ch.2, Intuition, d.1859).

Danh mục mô hình cho hai thước đo. Duration kỳ vọng bình quân của sổ tiền gửi là tổng modified duration của sáu cấu phần, lấy trọng số theo giá trị danh nghĩa, và phản ánh rủi ro từ hồ sơ lãi suất (tata_bank_alm, Ch.2, Intuition, d.1861); modified duration được định nghĩa ở trang [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]]. Nguồn giả định modified duration của tiền gửi 1 tháng, 1, 2, 3, 4 và 5 năm lần lượt là 0,03; 0,9; 1,8; 2,7; 3,6 và 4,5 (tata_bank_alm, Ch.2, Intuition, d.1865). Kỳ hạn kỳ vọng bình quân là tổng kỳ hạn của sáu cấu phần theo cùng trọng số và đo rủi ro từ góc thanh khoản (tata_bank_alm, Ch.2, Intuition, d.1869). Hai dòng kết quả trong bản nguồn là công thức không giải mã được (tata_bank_alm, Ch.2, Intuition, d.1867, d.1871); tính lại từ các số trên, với trọng số 20% và năm phần 16%, cho duration khoảng 2,17 và kỳ hạn khoảng 2,42 năm.

Mô hình run-off giả định không có nghiệp vụ thay thế (tata_bank_alm, Ch.2, Intuition, d.1853). Trang [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]] bỏ giả định đó bằng danh mục cuốn chiếu, và trang [[replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates]] chọn tỷ trọng các kỳ hạn của danh mục. Trang [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]] nêu giới hạn của mô hình tái tạo khi lãi suất tiền gửi dính.
