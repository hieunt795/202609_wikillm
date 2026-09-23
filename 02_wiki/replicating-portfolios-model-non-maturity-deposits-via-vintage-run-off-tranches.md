---
title: replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches
type: concept
tags: [alm, replicating-portfolio, vintage-run-off, non-maturity-deposits, duration, liquidity]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Mô hình danh mục tái tạo (Replicating Model), hay còn được gọi là mô hình suy giảm theo thế hệ (Vintage Run-off Model), là phương pháp toán tài chính kinh điển do Jarrow và Van Deventer (1998) khởi xướng nhằm giải quyết bài toán mô hình hóa rủi ro của các [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]] (tata_bank_alm, Ch.2, Replicating Model, d.1847; tata_bank_alm, Ch.2, References, d.2168). Mục tiêu của mô hình là tái tạo dòng tiền và độ nhạy lãi suất của các khoản tiền gửi không kỳ hạn thông qua một danh mục đầu tư giả định gồm các công cụ thu nhập cố định có tính thanh khoản cao và được giao dịch chủ động trên thị trường, sao cho sự phát triển về quy mô và lãi suất của danh mục tái tạo tiệm cận sát với hành vi kỳ vọng của tiền gửi (tata_bank_alm, Ch.2, Replicating Model, d.1847).

Trọng tâm trực giác của mô hình dựa trên việc thiết lập giả định về tốc độ suy giảm dòng tiền (*run-off*), đo lường mức độ tiêu hao dần của số dư tiền gửi trên các tài khoản hiện hữu theo thời gian do khách hàng thực hiện các giao dịch rút tiền (tata_bank_alm, Ch.2, Intuition, d.1851). Thay vì đối xử với toàn bộ khối tiền gửi thanh toán như một tập hợp đồng nhất có kỳ hạn bằng 0, mô hình phân rã khối tiền gửi thành các tầng kỳ hạn (tranches) độc lập (tata_bank_alm, Ch.2, Intuition, d.1853–1859). Ví dụ, đối với một danh mục tiền gửi thanh toán quy mô 50 triệu EUR không có dòng tiền mới bù đắp, ngân hàng phân tích hành vi và chia thành:
- Tầng tiền gửi ngắn hạn biến động: 10 triệu EUR (chiếm 20%) dự kiến sẽ bị khách hàng rút hết trong vòng 1 tháng tới (tiền gửi thanh toán vãng lai phục vụ chi tiêu tức thì);
- Tầng tiền gửi ổn định: 40 triệu EUR còn lại (chiếm 80%) được phân bổ đều thành 4 hoặc 5 phân đoạn có kỳ hạn hành vi kéo dài từ 1 năm đến 5 năm (mỗi phân đoạn 8 triệu EUR) (tata_bank_alm, Ch.2, Intuition, d.1853).

Nhờ cấu trúc phân rã thành các tầng thế hệ, mô hình danh mục tái tạo cho phép bộ phận ALM tính toán chính xác hai thước đo rủi ro trung tâm của bảng cân đối kế toán (tata_bank_alm, Ch.2, Intuition, d.1861–1871):
1. **Duration kỳ vọng bình quân của danh mục tiền gửi**: Phản ánh mức độ nhạy cảm của tiền gửi trước biến động của đường cong lợi suất thị trường (đo lường rủi ro theo góc nhìn lãi suất). Thước đo này được tính bằng tổng modified duration ($ModD_i$) của từng cấu phần nhân với tỷ trọng danh nghĩa tương ứng:
$$ModD_{deposit} = \sum_{i=1}^{n} w_i \cdot ModD_i$$
Trong đó với ví dụ danh mục 50 triệu EUR, giả định modified duration của các phân đoạn 1 tháng, 1 năm, 2 năm, 3 năm, 4 năm và 5 năm lần lượt là 0,03; 0,9; 1,8; 2,7; 3,6 và 4,5, thì duration kỳ vọng bình quân tổng thể của sổ tiền gửi thanh toán đạt mức 2,29 năm (tata_bank_alm, Ch.2, Intuition, d.1863–1867), kết nối trực tiếp với các kỹ thuật [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]];
2. **Kỳ hạn kỳ vọng bình quân của danh mục tiền gửi**: Đo lường rủi ro theo góc nhìn thanh khoản (thời gian lưu giữ nguồn vốn thực tế trong hệ thống). Thước đo này được tính bằng tổng kỳ hạn danh nghĩa ($M_i$) của từng cấu phần nhân với tỷ trọng danh nghĩa:
$$M_{deposit} = \sum_{i=1}^{n} w_i \cdot M_i$$
Với ví dụ trên, kỳ hạn kỳ vọng bình quân đạt mức 2,42 năm (tata_bank_alm, Ch.2, Intuition, d.1869–1871).

Mặc dù mô hình run-off thế hệ cung cấp cơ sở tĩnh vững chắc để đo lường trạng thái rủi ro đóng, thực tế ngân hàng luôn vận hành liên tục và dòng tiền rút đi được bù đắp bởi nguồn khách hàng mới. Để phản ánh trạng thái động này, mô hình run-off được mở rộng thành kỹ thuật danh mục cuốn chiếu [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]] và được tối ưu hóa toán học qua [[replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates]]. Tuy nhiên, độ tin cậy của mô hình phụ thuộc hoàn toàn vào tính ổn định của các giả định tái định giá, vốn đang bị thử thách nghiêm trọng bởi [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]].
