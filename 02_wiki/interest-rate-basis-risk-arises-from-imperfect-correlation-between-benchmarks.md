---
title: interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks
type: concept
tags: [irrbb, alm, basis-risk, benchmarks]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Rủi ro cơ sở lãi suất (Interest Rate Basis Risk) là cấu phần thứ hai trong khuôn khổ đo lường [[interest-rate-risk-in-the-banking-book-irrbb]], phát sinh khi các vị thế tài sản và nợ trên bảng cân đối của ngân hàng có kỳ hạn tương đồng nhưng được neo vào các chỉ số tham chiếu lãi suất khác nhau (tata_bank_alm, Ch.1, Types of Interest Rate Risk, d.623; tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.659). Theo định nghĩa của Cơ quan Giám sát Ngân hàng Châu Âu (EBA), basis risk xuất phát từ sự biến động tương đối bất lợi giữa các mức lãi suất thị trường, do sự tương quan không hoàn hảo (imperfect correlation) trong biên độ điều chỉnh lãi suất giữa các công cụ nhạy cảm lãi suất có đặc tính kỳ hạn tương tự (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.668).

Trong thực tiễn ngân hàng, các chỉ số tham chiếu thường được áp dụng bao gồm lãi suất thị trường liên ngân hàng (như EURIBOR hay LIBOR trước đây), lãi suất hoán đổi qua đêm (Overnight Index Swap — OIS), lãi suất phi rủi ro mới (Risk-Free Rates — RFR như €STR, SOFR) và lãi suất tái cấp vốn qua đêm hay hợp đồng mua lại Repo (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.660–664). Hiện tượng basis risk xảy ra khi chênh lệch giữa các chỉ số này (spread) nới rộng hoặc co hẹp đột ngột ngoài dự kiến của bộ phận ALM (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.668).

Ví dụ định lượng của Fidelio Tata minh họa rõ nét cơ chế này: một tài sản và một khoản nợ có cùng thời điểm định giá lại vào tháng 6, nhưng tài sản hưởng lãi suất theo 6-month EURIBOR còn nợ chịu chi phí theo 1-month EURIBOR (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.674–681). Nếu trong tháng 5 xuất hiện cú sốc thanh khoản ngắn hạn khiến 1-month EURIBOR tăng vọt 200 điểm cơ bản (từ 4% lên 6%) trong khi 6-month EURIBOR chỉ tăng 100 điểm cơ bản (từ 4% lên 5%), thì bước sang tháng 6, ngân hàng phải trả chi phí vốn 6% nhưng chỉ thu về lợi suất tài sản 5% (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.676–681). Ngân hàng phải chịu mức thâm hụt biên lợi nhuận lãi thuần ngay cả khi không hề có sự lệch pha về thời gian như trong [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]].

Theo yêu cầu của EBA, các tổ chức tín dụng phải thực hiện kiểm kê định kỳ toàn bộ danh mục tài sản và nợ phân loại theo từng hệ chỉ số tham chiếu lãi suất, đồng thời rà soát mức độ hiệu quả của các công cụ phái sinh phòng hộ nhằm phát hiện các rủi ro phát sinh từ chênh lệch cơ sở, độ lồi (*convexity*) và độ trễ phản ứng giữa các thị trường mà các mô hình khe hở tái định giá truyền thống thường bỏ sót (tata_bank_alm, Ch.1, Interest Rate Basis Risk, d.670). Cùng với [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]], basis risk đòi hỏi ngân hàng phải mô hình hóa tương quan chuỗi thời gian giữa các đường cong lợi suất thay vì giả định chúng luôn biến động song hành.
