---
title: sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models
type: analysis
tags: [alm, deposit-beta, sticky-rates, pass-through, duration-shortening, svb, replication-critique]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Mặc dù mô hình danh mục tái tạo theo [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]] là trụ cột kinh điển trong quản trị bảng cân đối kế toán ngân hàng, phương pháp này đang đối mặt với những làn sóng phê phán thực nghiệm sâu sắc về tính tương thích kém trước các biến động lãi suất hiện đại (tata_bank_alm, Ch.2, Criticism, d.2043). Thách thức căn bản nhất xuất phát từ việc lãi suất chi trả cho người gửi tiền không hề biến động tương quan chặt chẽ với lãi suất thị trường (tata_bank_alm, Ch.2, Criticism, d.2045). Lãi suất tiền gửi là loại lãi suất chỉ định (*administered rates*), được ngân hàng điều hành như một biến số chính sách nội bộ nhằm chủ động điều tiết quy mô thanh khoản huy động (tata_bank_alm, Ch.2, Criticism, d.2049).

Nghiên cứu thực nghiệm toàn diện của Hoffmann, Frontczak và Pierobon (2023) chỉ ra rằng tốc độ truyền dẫn (*pass-through*) từ lãi suất thị trường sang lãi suất tiền gửi thanh toán diễn ra hết sức chậm chạp và không hoàn hảo: trong ngắn hạn, chỉ có **9%** mức thay đổi của lãi suất thị trường được phản ánh vào lãi suất tiền gửi; và ngay cả trong dài hạn, tỷ lệ này cũng chỉ đạt mức **29%** (tata_bank_alm, Ch.2, Criticism, d.2045; tata_bank_alm, Ch.2, Notes, d.2134). Tính chất này làm cho lãi suất tiền gửi mang đặc tính "dính" (*sticky deposit rates*), phản ánh sự phân mảnh thị trường (*market segmentation*) mà Jarrow và Van Deventer (1998) từng lý giải: chỉ có các tổ chức tín dụng mới được phép phát hành tiền gửi thanh toán, khiến công cụ này tương đương với một hợp đồng hoán đổi lãi suất kỳ dị (exotic swap) có mệnh giá phụ thuộc vào toàn bộ lịch sử lãi suất trong quá khứ (tata_bank_alm, Ch.2, Criticism, d.2045–2047).

Thước đo trung tâm phản ánh mức độ nhạy cảm của lãi suất tiền gửi trước biến động của lãi suất thị trường phi rủi ro ngắn hạn là **Hệ số Beta Tiền gửi (Deposit Beta)**, được xác định bằng công thức:
$$\beta_{deposit} = \frac{\Delta r_{deposit}}{\Delta r_{market}}$$
Trong đó $\Delta r_{deposit}$ là mức biến động của lãi suất tiền gửi khách hàng và $\Delta r_{market}$ là mức biến động tương ứng của lãi suất thị trường chuẩn mực (như lợi suất trái phiếu chính phủ ngắn hạn AAA kỳ hạn 3 tháng) (tata_bank_alm, Ch.2, Criticism, d.2055–2057).

Dữ liệu hồi quy thực nghiệm đối với các ngân hàng thương mại Châu Âu qua ba giai đoạn lịch sử khác nhau đã bộc lộ sự bất ổn định trầm trọng của Deposit Beta (tata_bank_alm, Ch.2, Criticism, d.2059):
1. **Giai đoạn 2014–2017 (Môi trường lãi suất giảm dần)**: Deposit beta ước tính duy trì ở mức khoảng 21%;
2. **Giai đoạn 2017–2021 (Kỷ nguyên lãi suất âm)**: Deposit beta sụp đổ xuống dưới mức **3%**, khi các ngân hàng không thể và không sẵn sàng áp dụng lãi suất âm đối với tiền gửi cá nhân bán lẻ;
3. **Giai đoạn 2022–2024 (Chu kỳ tăng lãi suất thắt chặt nhanh kỷ lục)**: Deposit beta tăng vọt trở lại vượt mức **20%** (tata_bank_alm, Ch.2, Criticism, d.2059).

Sự bùng nổ dữ dội của Deposit Beta trong chu kỳ thắt chặt tiền tệ được Acharya et al. (2023) trong nghiên cứu về sự sụp đổ của Ngân hàng Silicon Valley (SVB) giải thích rõ ràng: khi lợi suất của các tài sản thay thế gần gũi với tiền gửi ngân hàng (đặc biệt là các quỹ thị trường tiền tệ — Money Market Funds / MMFs) tăng vọt, áp lực cạnh tranh giữ chân dòng vốn đã buộc các ngân hàng phải nâng lãi suất huy động với tốc độ chưa từng thấy kể từ cuộc khủng hoảng tài chính 2008 (tata_bank_alm, Ch.2, Criticism, d.2055; tata_bank_alm, Ch.2, References, d.2142).

Sự bất ổn của Deposit Beta gây ra hậu quả nhức nhối: **hiện tượng rút ngắn Duration thực nghiệm (Empirical Duration Shortening)** (tata_bank_alm, Ch.2, Criticism, d.2063). Các ước lượng duration dài hạn (từ 2 đến 5 năm) của danh mục tái tạo được xây dựng trong thập kỷ lãi suất thấp thực chất là một "ảo ảnh thống kê", do người gửi tiền không có bất kỳ động lực chi phí cơ hội nào để rút tiền hay chuyển dịch dòng vốn (tata_bank_alm, Ch.2, Criticism, d.2063). Khi lãi suất thị trường tăng cao, chi phí cơ hội của việc giữ tiền nhàn rỗi bộc lộ rõ rệt, tính dính của tiền gửi bị xói mòn nhanh chóng, khách hàng lập tức chuyển vốn sang các tài sản sinh lời cao hơn, khiến thời gian tồn tại thực tế của tiền gửi bị co ngắn đột ngột và quy mô tiền gửi sụt giảm mạnh (tata_bank_alm, Ch.2, Criticism, d.2063).

Hiện tượng này kết nối trực tiếp với [[behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales]] và làm gia tăng [[interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]]. Việc áp dụng cứng nhắc các tham số duration quá khứ trong các kỹ thuật [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]] và [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]] sẽ đẩy ngân hàng vào tình trạng định giá sai rủi ro nghiêm trọng khi chu kỳ vĩ mô đảo chiều.
