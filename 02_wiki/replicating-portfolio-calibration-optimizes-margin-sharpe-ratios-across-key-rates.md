---
title: replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates
type: concept
tags: [alm, replicating-portfolio, calibration, sharpe-ratio, key-rate-duration, margin-stability]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Hiệu chuẩn danh mục tái tạo (Replicating Portfolio Calibration) là quy trình tối ưu hóa toán tài chính nhằm xác định cơ cấu phân bổ tỷ trọng đầu tư vào một tập hợp các tài sản thu nhập cố định có các kỳ hạn định giá lại then chốt (*key rates*) khác nhau trên đường cong lợi suất, nhằm mục tiêu mô phỏng tối ưu hành vi của dòng tiền tiền gửi không kỳ hạn theo một tiêu chí mục tiêu cụ thể dưới các ràng buộc pháp lý và kinh doanh (tata_bank_alm, Ch.2, Calibration, d.1939). Thời lượng (*duration*) của tiền gửi tiết kiệm và thanh toán sau đó được xác định bằng chính duration của danh mục tái tạo tối ưu này (tata_bank_alm, Ch.2, Calibration, d.1951).

Tiêu chí mục tiêu tối ưu hóa mang tính đặc thù cho từng ngân hàng và phụ thuộc chặt chẽ vào chiến lược kinh doanh cũng như khẩu vị rủi ro ALM của ban điều hành (tata_bank_alm, Ch.2, Calibration, d.1945):
1. **Tối thiểu hóa độ biến động biên lợi nhuận ($\min \sigma(M)$)**: Mục tiêu là tạo ra biên thu nhập ổn định nhất trên mức lãi suất tiền gửi trong suốt giai đoạn quan sát lịch sử, tức tìm kiếm danh mục có độ lệch chuẩn của biên thu nhập lãi thuần là nhỏ nhất (tata_bank_alm, Ch.2, Calibration, d.1946);
2. **Tối đa hóa biên lợi nhuận kỳ vọng ($\max E(M)$)**: Hướng tới việc thu được mức lợi nhuận bình quân cao nhất từ nguồn vốn tiền gửi, chấp nhận mức độ biến động lớn hơn khi lãi suất thị trường đảo chiều (tata_bank_alm, Ch.2, Calibration, d.1947);
3. **Tối đa hóa biên lợi nhuận đã điều chỉnh rủi ro ($\max [E(M) / \sigma(M)]$ — Tỷ số Sharpe của Biên Lợi nhuận)**: Tiêu chuẩn hóa mức sinh lời kỳ vọng trên một đơn vị rủi ro biến động biên, giúp xác định danh mục hiệu quả nhất trên đường biên tối ưu Markovitz ứng dụng cho sổ ngân hàng (tata_bank_alm, Ch.2, Calibration, d.1948).

Các ràng buộc tối ưu hóa bao gồm yêu cầu danh mục phải tái tạo sát nhất động thái biến động số dư tiền gửi thực tế trong quá khứ, các giới hạn giám sát quản lý (như lệnh cấm bán khống - *no short selling*, hoặc giới hạn trần kỳ hạn 5 năm của EBA), và danh mục các công cụ tài chính đủ điều kiện đầu tư (tata_bank_alm, Ch.2, Calibration, d.1949).

Trong thực tế thiết kế, luôn tồn tại sự đánh đổi (*trade-off*) sâu sắc giữa các kỳ hạn lãi suất then chốt (tata_bank_alm, Ch.2, Calibration, d.1953). Điển hình trong mô hình hóa tiền gửi thanh toán:
- Sử dụng kỳ hạn then chốt 5 năm (lãi suất swap 5Y) mang lại độ biến động biên kỳ vọng rất thấp ($\sigma = 38$ bps), nhưng mức biên kỳ vọng chỉ đạt 39 bps (tỷ số Sharpe biên = $39 / 38 = 1,026$);
- Sử dụng kỳ hạn then chốt 10 năm (lãi suất swap 10Y) tạo ra mức biên kỳ vọng vượt trội đạt 83 bps, dù độ biến động biên tăng lên $\sigma = 46$ bps;
- Khi so sánh theo tỷ số Sharpe của biên lợi nhuận ($E(M)/\sigma(M)$), cấu trúc 10 năm hấp dẫn hơn đáng kể với tỷ số đạt $1,804$ so với mức $1,026$ của cấu trúc 5 năm (tata_bank_alm, Ch.2, Calibration, d.1953).

Nhằm dung hòa bài toán đánh đổi giữa lợi suất kỳ vọng và tính ổn định dòng thu nhập, các mô hình tái tạo thực tế thường kết hợp từ **2 đến 4 lãi suất then chốt khác nhau** (ví dụ: kết hợp EURIBOR 1 tháng, Swap 5 năm và Swap 10 năm) (tata_bank_alm, Ch.2, Calibration, d.1959). Sự kết hợp đa kỳ hạn này tận dụng phân tích [[key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts]], mang lại đặc tính rủi ro/lợi nhuận ưu việt hơn bất kỳ kỳ hạn đơn lẻ nào (tata_bank_alm, Ch.2, Calibration, d.1959). Khi đó, chênh lệch lãi suất giữa danh mục cuốn chiếu tối ưu nhất và lãi suất trả cho khách hàng chính là biên thu nhập kỳ vọng của ngân hàng (tata_bank_alm, Ch.2, Calibration, d.1961).

Về mặt hạch toán nội bộ theo [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]], mô hình hiệu chuẩn thiết lập ranh giới trách nhiệm minh bạch: mức biên lợi nhuận kỳ vọng từ danh mục tối ưu được ghi nhận toàn bộ cho bộ phận kinh doanh khách hàng; trong khi mọi sai lệch thực tế phát sinh ngoài biên kỳ vọng này được kết chuyển trực tiếp và quy trách nhiệm cho bàn ALM Desk / Treasury (tata_bank_alm, Ch.2, Calibration, d.1963). Danh mục hiệu chuẩn này đóng vai trò hạt nhân trong cơ chế [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]], làm tiền đề triển khai [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]] khi quy mô bảng cân đối biến động, đồng thời liên tục được kiểm định tính nhạy cảm trước [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]].
