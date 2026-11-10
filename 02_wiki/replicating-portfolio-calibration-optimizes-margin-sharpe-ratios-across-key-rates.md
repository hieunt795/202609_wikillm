---
title: replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates
type: concept
tags: [alm, replicating-portfolio, calibration, sharpe-ratio, key-rate-duration, margin-stability]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
drives: [rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]
related: [key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts, matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions, dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates, sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]
---

Hiệu chuẩn danh mục tái tạo (Replicating Portfolio Calibration) là quy trình tối ưu hóa toán tài chính nhằm xác định cơ cấu phân bổ tỷ trọng đầu tư vào một tập hợp các tài sản thu nhập cố định có các kỳ hạn định giá lại then chốt (*key rates*) khác nhau trên đường cong lợi suất, nhằm mục tiêu mô phỏng tối ưu hành vi của dòng tiền tiền gửi không kỳ hạn theo một tiêu chí mục tiêu cụ thể dưới các ràng buộc pháp lý và kinh doanh (tata_bank_alm, Ch.2, Calibration, d.1939). Duration của tiền gửi tiết kiệm sau đó được xác định bằng duration của danh mục tái tạo và tính được bằng giải tích (tata_bank_alm, Ch.2, Calibration, d.1951).

Tiêu chí mục tiêu là riêng của từng ngân hàng và phụ thuộc vào chiến lược kinh doanh và chiến lược quản trị rủi ro của ngân hàng đó (tata_bank_alm, Ch.2, Calibration, d.1945):
1. **Tối thiểu hóa độ lệch chuẩn của biên**: tạo biên ổn định nhất trên lãi suất tiền gửi trong một kỳ mẫu (tata_bank_alm, Ch.2, Calibration, d.1946);
2. **Tối đa hóa biên kỳ vọng** thu được trên lãi suất tiền gửi (tata_bank_alm, Ch.2, Calibration, d.1947);
3. **Tối đa hóa biên đã điều chỉnh rủi ro**, đo bằng tỷ số Sharpe của biên, tức biên kỳ vọng bình quân chia cho độ lệch chuẩn của biên (tata_bank_alm, Ch.2, Calibration, d.1948).

Ràng buộc gồm yêu cầu danh mục tái tạo sát nhất diễn biến số dư tiền gửi trong một kỳ mẫu lịch sử, cùng các giới hạn do cơ quan quản lý, cơ quan giám sát và ban điều hành ngân hàng đặt ra về sản phẩm nào được dùng trong danh mục và dùng tới mức nào (tata_bank_alm, Ch.2, Calibration, d.1949).

Có sự đánh đổi giữa các lãi suất then chốt (tata_bank_alm, Ch.2, Calibration, d.1953). Trong ví dụ của nguồn về tiền gửi thanh toán, lãi suất then chốt 5 năm (swap 5 năm) cho độ biến động của biên kỳ vọng thấp hơn, còn lãi suất then chốt 10 năm (swap 10 năm) cho biên kỳ vọng cao hơn (tata_bank_alm, Ch.2, Calibration, d.1953). Theo tỷ số Sharpe của biên, $E(M)/\sigma(M)$, lãi suất then chốt 10 năm đạt 1,804 (83 bp / 46 bp), so với 1,026 (39 bp / 38 bp) của lãi suất then chốt 5 năm (tata_bank_alm, Ch.2, Calibration, d.1953).

Mô hình tái tạo thường kết hợp hai đến bốn lãi suất then chốt để có biên khách hàng kỳ vọng dương và ổn định (tata_bank_alm, Ch.2, Calibration, d.1959); lãi suất then chốt ở đây là các điểm kỳ hạn trên đường cong, như ở trang [[key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts]]. Kết hợp hai lãi suất then chốt có thể cho đặc tính rủi ro và lợi nhuận tốt hơn từng lãi suất riêng lẻ (tata_bank_alm, Ch.2, Calibration, d.1959). Danh mục cuốn chiếu tốt nhất là danh mục có tỷ số Sharpe của biên cao nhất với một số lượng lãi suất then chốt hợp lý (tata_bank_alm, Ch.2, Calibration, d.1959). Chênh lệch giữa lãi suất của danh mục cuốn chiếu khớp nhất và lãi suất khách hàng là biên kỳ vọng của ngân hàng, với điều kiện ALM cấp vốn được cho mảng khách hàng đúng theo danh mục đó (tata_bank_alm, Ch.2, Calibration, d.1961).

Biên kỳ vọng được ghi cho mảng kinh doanh khách hàng, còn mọi sai lệch so với biên này được ghi cho bàn ALM (tata_bank_alm, Ch.2, Calibration, d.1963); trang [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]] mô tả cách tách biên kinh doanh khỏi phần của Treasury trong FTP. Danh mục đã hiệu chuẩn là danh mục cuốn chiếu ở trang [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]]. Trang [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]] xử lý trường hợp khối lượng tiền gửi thay đổi, và trang [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]] nêu giới hạn của mô hình khi lãi suất tiền gửi dính.
