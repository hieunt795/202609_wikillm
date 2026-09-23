---
title: dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates
type: concept
tags: [alm, dynamic-replication, volume-risk, balance-sheet-dynamics, ftp, mark-to-market]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Tái tạo động (Dynamic Replication) là kỹ thuật mở rộng bậc cao của mô hình danh mục tái tạo, nhằm giải quyết bài toán biến động quy mô nguồn vốn tiền gửi không kỳ hạn khi giả định về sự ổn định số dư bị phá vỡ trong điều kiện kinh tế thực tế (tata_bank_alm, Ch.2, Dynamic Replication, d.1993–1997). Sự phát triển của các phương pháp ALM gắn liền với ba góc nhìn tiến hóa về bảng cân đối kế toán theo [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]] (tata_bank_alm, Ch.2, Volume Changes, d.1967–1975):
1. **Góc nhìn thanh lý (Run-off view)**: Bảng cân đối đóng, các vị thế đáo hạn không được thay thế bằng tài sản/nợ mới;
2. **Góc nhìn tĩnh cuốn chiếu (Static view)**: Giả định quy mô tiền gửi không đổi, các vị thế đáo hạn được bù đắp hoàn hảo bởi các khoản tiền gửi mới có quy mô tương đương;
3. **Góc nhìn động (Dynamic view)**: Điều chỉnh liên tục danh mục tái tạo để phản ánh dự báo thay đổi thực tế về quy mô tổng tài sản và dòng tiền mới trong tương lai.

Giả định về một danh mục cuốn chiếu có quy mô không đổi theo [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]] chỉ cung cấp định giá chính xác chừng nào tổng số dư tiền gửi duy trì ổn định (tata_bank_alm, Ch.2, Dynamic Replication, d.1993). Tuy nhiên, số liệu thực nghiệm từ hệ thống ngân hàng Đức giai đoạn 2003–2024 chỉ ra rằng tiền gửi thanh toán của hộ gia đình hoàn toàn không cố định: trong giai đoạn lãi suất giảm sâu và rơi vào vùng âm (2009–2022), quy mô tiền gửi thanh toán bùng nổ mạnh mẽ; và khi lãi suất tăng trở lại, khối lượng tiền gửi lại chịu biến động dữ dội (tata_bank_alm, Ch.2, Volume Changes, d.1979). Nếu bỏ qua tác động của biến động quy mô, ngân hàng sẽ tính toán sai lệch nghiêm trọng tỷ suất lãi suất cơ hội, bóp méo biên lợi nhuận của sản phẩm và đánh giá sai hiệu quả bán hàng của mạng lưới (tata_bank_alm, Ch.2, Dynamic Replication, d.1997).

Ý tưởng cốt lõi của tái tạo động là tích hợp sự thay đổi quy mô thông qua một **danh mục phòng hộ riêng biệt được định giá theo mức lãi suất thị trường hiện hành** (tata_bank_alm, Ch.2, Dynamic Replication, d.2001). Bởi vì bộ phận Nguồn vốn (Treasury) không thể "quay ngược thời gian" để thiết lập các vị thế phòng hộ ở mức lãi suất lịch sử trong quá khứ, toàn bộ quy mô tiền gửi tăng thêm bắt buộc phải được phòng hộ ở mức lãi suất giao ngay (*spot market rates*) tại thời điểm phát sinh dòng tiền (tata_bank_alm, Ch.2, Dynamic Replication, d.2003).

Ví dụ, khi tiền gửi thanh toán tăng đột biến gấp đôi từ 50 triệu lên 100 triệu EUR trong môi trường lãi suất thị trường tăng (tata_bank_alm, Ch.2, Dynamic Replication, d.1999–2005):
- Quy mô 50 triệu EUR ban đầu vẫn vận hành theo danh mục cuốn chiếu lịch sử, trong đó một phân đoạn 8 triệu EUR đầu tư từ 4 năm trước chỉ tạo ra lợi suất -0,4%;
- Ngược lại, khoản tiền gửi gia tăng mới 50 triệu EUR được Treasury giải ngân ngay vào các công cụ thị trường hiện hành với mức lợi suất 2,7%;
- Nhờ đó, phần tiền gửi tăng thêm này đóng góp mức biên thương mại khách hàng lên tới 2,0% (thay vì mức 0,5% của danh mục cũ), tạo động lực kinh tế to lớn để khen thưởng mạng lưới chi nhánh (tata_bank_alm, Ch.2, Dynamic Replication, d.2005).

Tuy nhiên, rủi ro lớn nhất của tái tạo động xuất hiện khi **quy mô tiền gửi sụt giảm trong môi trường lãi suất tăng** (tata_bank_alm, Ch.2, Dynamic Replication, d.2021). Khi dòng tiền khách hàng rút ra vượt quá khả năng bù đắp tự nhiên, ALM buộc phải thanh lý trước hạn các công cụ thu nhập cố định dài hạn đã mua trong quá khứ để chi trả thanh khoản; do lãi suất thị trường lúc này đã tăng cao, giá trị các chứng khoán này sụt giảm mạnh, buộc ngân hàng phải ghi nhận những khoản **thua lỗ thanh lý theo giá thị trường (mark-to-market loss)** rất nặng nề (tata_bank_alm, Ch.2, Dynamic Replication, d.2021).

Nhằm giảm thiểu rủi ro này, các mô hình phát triển sau Jarrow và Van Deventer (1998) đã đưa ra nhiều cải tiến tinh vi (tata_bank_alm, Ch.2, Further Developments, d.2025–2039): Maes và Timmermans (2005) đề xuất bóc tách tiền gửi thành ba cấu phần độc lập gồm phần cốt lõi cứng nhắc (*core* — ít nhạy cảm lãi suất, phân bổ kỳ hạn dài), phần biến động ngắn hạn (*volatile* — phòng hộ bằng kỳ hạn ngắn dưới 1 tháng) và phần còn lại (*remaining* — áp dụng mô hình tái tạo); các mô hình mô phỏng Monte Carlo đa kịch bản lãi suất; các mô hình kinh tế tiền tệ phân loại tiền gửi theo mục đích giao dịch, dự phòng và đầu cơ; và các mô hình lập trình ngẫu nhiên đa giai đoạn thích ứng liên tục với biến động thị trường (tata_bank_alm, Ch.2, Further Developments, d.2027–2035).

Kỹ thuật tái tạo động là cầu nối trực tiếp giữa kế hoạch ALM trung tâm và [[replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates]]. Tuy vậy, mô hình sẽ hoàn toàn bị bẻ gãy khi chạm trán [[behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales]], đồng thời luôn bị đe dọa bởi tính bất ổn định của [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]].
