---
title: rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates
type: concept
tags: [alm, replicating-portfolio, rolling-portfolio, moving-average, ftp, deposit-margin]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
drives: [funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]
contrasts: [dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]
related: [replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches, replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates, sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]
---

Danh mục cuốn chiếu (rolling portfolio) mô hình hóa sổ tiền gửi ở trạng thái ổn định, tiếp nối mô hình run-off ở trang [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]]: 80% tiền gửi thanh toán ở lại ngân hàng tới 5 năm, 20% còn lại bị rút và được thay hằng tháng (tata_bank_alm, Ch.2, Rolling Portfolio, d.1875). Tiền gửi suy giảm do bị rút được thay đủ bằng tiền gửi mới của khách hàng, nên tổng vị thế tiền gửi thanh toán không đổi theo thời gian (tata_bank_alm, Ch.2, Rolling Portfolio, d.1881). Nguồn coi cách nhìn sổ tiền gửi như một danh mục các khoản gửi theo thời gian là sát thực tế hơn cách coi nó là tổng các khoản đồng nhất, nhất là với ngân hàng đã gây dựng sổ trong thời gian dài (tata_bank_alm, Ch.2, Rolling Portfolio, d.1879).

Mô hình đặt một dòng thời gian cho dòng tiền: 8 triệu EUR dự kiến bị rút sau một năm có thể là khoản gửi từ bốn năm trước, và 8 triệu EUR gửi hôm nay dự kiến ở lại thêm năm năm (tata_bank_alm, Ch.2, Rolling Portfolio, d.1875–1877). Từ dòng thời gian đó ngân hàng suy ra lãi suất cơ hội (*opportunity interest rate*) mà vốn khách hàng lẽ ra được đầu tư trên thị trường (tata_bank_alm, Ch.2, Rolling Portfolio, d.1883). Cách tính giả định bộ phận ALM/Treasury nhận vốn khách hàng và quản lý theo lãi suất thị trường hiện hành; việc Treasury có thật sự đầu tư ra thị trường hay không thì không ảnh hưởng tới phép tính (tata_bank_alm, Ch.2, Rolling Portfolio, d.1883).

Các khoản đầu tư giả định diễn ra ở nhiều thời điểm, nên lãi suất cơ hội bình quân là hỗn hợp các lãi suất quá khứ, gọi là bình quân trượt (moving average, MA) (tata_bank_alm, Ch.2, Rolling Portfolio, d.1889). Ví dụ của nguồn dùng lãi suất swap EUR làm lãi suất đầu tư cơ hội: 8 triệu EUR gửi bốn năm trước được đầu tư 5 năm ở −0,3%, còn phần 8 triệu EUR mới nhất hưởng 3%, là lãi suất swap 5 năm hiện tại (tata_bank_alm, Ch.2, Rolling Portfolio, d.1891). Bình quân cho cả 50 triệu EUR là 0,8% (tata_bank_alm, Ch.2, Rolling Portfolio, d.1891).

Lãi suất cơ hội này chính là lãi suất của [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks|định giá chuyển vốn nội bộ (FTP)]] (tata_bank_alm, Ch.2, Rolling Portfolio, d.1883). Nếu Treasury chuyển 0,8% cho bộ phận khách hàng làm lãi suất FTP, biên đóng góp của bộ phận quản tiền gửi thanh toán bằng 0,8% trừ lãi suất đang trả cho khách hàng (tata_bank_alm, Ch.2, Rolling Portfolio, d.1893). Lãi suất khách hàng thường hình thành từ cạnh tranh giữa nhiều ngân hàng; nếu ngân hàng phải trả 1%, biên khách hàng là −0,2% (tata_bank_alm, Ch.2, Rolling Portfolio, d.1895).

Danh mục tự quay vòng khi tiền gửi mới thay phần bị rút, nên chiến lược tái tạo phải xử lý việc tái đầu tư phần thay thế (tata_bank_alm, Ch.2, Replication Over Time, d.1911). Sau một năm, khoản đầu tư 5 năm làm từ 5 năm trước đáo hạn; tiền gửi mới thay vào được giả định ở lại 5 năm, nên công cụ tái tạo là công cụ kỳ hạn 5 năm (tata_bank_alm, Ch.2, Replication Over Time, d.1913). Bình quân trượt ghi nhận hiệu ứng này bằng cách bỏ lãi suất cũ và thay bằng lãi suất hiện hành (tata_bank_alm, Ch.2, Replication Over Time, d.1915). Trong ví dụ, lãi suất 1 tháng tăng từ 2% lên 2,5% và lãi suất 5 năm mới là 3,5% (tata_bank_alm, Ch.2, Replication Over Time, d.1920–1922); bình quân trượt 5 năm tăng từ 0,5% lên 1,26%, lãi suất cơ hội tổng tăng từ 0,8% lên 1,5% (tata_bank_alm, Ch.2, Replication Over Time, d.1933). Bộ phận khách hàng được ghi nhận 1,5% qua FTP trong khi vẫn trả khách hàng 1%, nên biên lên +0,5% (tata_bank_alm, Ch.2, Replication Over Time, d.1935).

Trang [[replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates]] chọn tỷ trọng các kỳ hạn của danh mục cuốn chiếu. Danh mục cuốn chiếu giả định tổng khối lượng tiền gửi không đổi (tata_bank_alm, Ch.2, Rolling Portfolio, d.1881); trang [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]] xử lý trường hợp khối lượng thay đổi. Trang [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]] nêu trường hợp lãi suất tiền gửi không đi theo giả định của mô hình.
