---
title: rapid-rate-tightening-exposes-duration-gaps-and-asymmetric-prepayment-speeds
type: analysis
tags: [alm, rate-hiking-cycle, duration-gap, prepayment-risk, complacency, svb]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Giai đoạn lãi suất thấp và ổn định kéo dài suốt hơn một thập kỷ trước năm 2022 đã hình thành nên một tâm lý tự mãn nguy hiểm (*risk management complacency*) ăn sâu vào tư duy của cả một thế hệ chuyên gia quản trị rủi ro ngân hàng, gieo rắc niềm tin sai lầm rằng rủi ro lãi suất sẽ vĩnh viễn duy trì ở mức thấp (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2471). Sự tự mãn này đã phá hủy tính chuẩn xác của các mô hình quản trị bảng cân đối kế toán khi chu kỳ thắt chặt tiền tệ toàn cầu bất ngờ nổ ra với tốc độ nhanh kỷ lục trong giai đoạn 2022–2023 (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2471–2475).

Theo phân tích của Acharya et al. (2023), trong chu kỳ tăng lãi suất tương đối nông 2016–2019, các khoản tiền gửi thanh toán và tiết kiệm không được bảo hiểm có vẻ rất "dính" (*sticky*) và tiếp tục nằm yên trong ngân hàng bất chấp deposit beta ở mức thấp lịch sử (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2475; tata_bank_alm, Ch.3, References, d.2530). Các ngân hàng đã ngây thơ giả định rằng hệ số beta thấp này sẽ tiếp tục duy trì trong chu kỳ thắt chặt mới; thế nhưng, tiền gửi không kỳ hạn có thể nhanh chóng "bung ra" (*unstuck*) và hệ số deposit beta vọt tăng với tốc độ hủy diệt (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2475), xác nhận trực tiếp hiện tượng [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]].

Thực tế trong hai năm 2022–2023, khách hàng ngân hàng tại Châu Âu đã ồ ạt rút tiền khỏi các tài khoản thanh toán không kỳ hạn để chuyển sang các sản phẩm tiền gửi có kỳ hạn nhằm tìm kiếm mức sinh lời cao hơn (tata_bank_alm, Ch.3, Composition of Banks' Balance Sheets Over Time, d.2209; tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2477). Tỷ trọng tiền gửi có kỳ hạn dưới 1 năm tăng vọt từ 2,6% lên 5,9%, khiến các ngân hàng cạn kiệt thanh khoản dự trữ dư thừa và làm bùng nổ **khe hở thời lượng (Duration Gap)** theo [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]], trực tiếp hiện thực hóa tổn thất rủi ro lãi suất (Coulier et al. 2024; tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2477; tata_bank_alm, Ch.3, Notes, d.2521).

Đáng chú ý, thảm họa này đã từng được Ngân hàng Trung ương Châu Âu (ECB) cảnh báo chính xác từ 5 năm trước đó trong đợt kiểm tra sức chịu đựng độ nhạy IRRBB năm 2017 đối với hơn 100 ngân hàng lớn nhất Châu Âu:
> Các ngân hàng đang phụ thuộc nặng nề vào các mô hình hành vi khách hàng vốn được hiệu chuẩn thuần túy trong môi trường lãi suất giảm (ECB 2017, 2; tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2479; tata_bank_alm, Ch.3, Notes, d.2522–2523).

Thế nhưng, lời cảnh báo sớm từ cơ quan giám sát đã bị đa số các tổ chức tín dụng phớt lờ, không chịu kiểm định sức ép và tái hiệu chuẩn mô hình sang môi trường lãi suất tăng (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2479).

Cú sốc tăng lãi suất thần tốc làm đảo lộn hoàn toàn các mô hình trả nợ trước hạn (**Prepayment Models**) theo hai chiều hướng bất đối xứng (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2481), làm biến dạng sâu sắc các [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]]:
1. **Đối với các khoản vay thế chấp mua nhà lãi suất cố định thấp**: Những khách hàng may mắn khóa chặt mức lãi suất cố định siêu rẻ trong thời kỳ [[zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp]] có xu hướng duy trì khoản nợ lâu nhất có thể; tốc độ trả nợ trước hạn suy giảm đột ngột (*prepayment speeds drop sharply*) vì việc giữ tiền nhàn rỗi gửi vào ngân hàng hưởng lãi suất cao có lợi hơn nhiều so với việc dùng tiền tất toán khoản nợ giá rẻ;
2. **Đối với các khoản vay lãi suất thả nổi**: Tốc độ trả nợ trước hạn lại tăng vọt do người đi vay chịu áp lực chi phí lãi vay tăng cao và tìm mọi cách tất toán trước hạn để cắt giảm gánh nặng nợ nần (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2481).

Đồng thời, sự sụt giảm nghiêm trọng giá trị thị trường của danh mục trái phiếu đầu tư sẵn sàng để bán (AFS/FVOCI) do lãi suất tăng vọt đã tạo ra những khoản lỗ chưa thực hiện khổng lồ, ăn mòn vốn tự có Tier 1 theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]], cấu thành nguyên nhân cốt lõi dẫn tới sự sụp đổ dây chuyền của [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs|Ngân hàng Silicon Valley (SVB)]] và cuộc khủng hoảng ngân hàng mùa xuân năm 2023 (tata_bank_alm, Ch.3, Rapid Rise in Interest Rates, d.2485; tata_bank_alm, Ch.3, References, d.2530).
