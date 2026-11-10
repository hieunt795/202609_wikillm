---
title: svb-three-year-duration-gap-breached-supervisory-outlier-thresholds-absent-deposit-modeling-manipulation
type: concept
tags: [alm, irrbb, duration-gap, supervisory-outlier-test, eve, svb]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs]
governed_by: [supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
drives: [regulatory-arbitrage-via-deposit-duration-assumptions-distorts-supervisory-irrbb-compliance]
related: [duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]
---

Xét duration của các khoản mục trên bảng cân đối của [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs|Silicon Valley Bank]], nguồn chỉ ra một lệch pha cấu trúc giữa tài sản duration dài và nợ duration ngắn (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2609); phép đo dùng ở đây nằm ở trang [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]]. Một phần tài sản có duration dài, nhất là các vị thế giữ tới đáo hạn (HTM), với duration 6,25 năm mà nguồn suy ra cho sổ HTM (tata_bank_alm, Ch.4, 4.3.1 At a Glance: GAAP vs. Non-GAAP, d.2591). Nguồn vốn thì nhiều khả năng có duration ngắn: khoảng 45% tiền gửi là tiền của các công ty công nghệ giai đoạn đầu và giai đoạn sau, đến từ công ty khởi nghiệp và quỹ đầu tư mạo hiểm, vốn chỉ gửi tạm cho tới khi có cơ hội đầu tư (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2609).

Ngay cả khi giả định duration bình quân của số tiền gửi tạm đó là 1 năm, duration gap của ngân hàng vẫn vào khoảng 3 năm (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2617). Với cú sốc lãi suất tăng 200 điểm cơ bản của Basel, duration gap 3 năm hàm ý khoản lỗ 12,5 tỷ USD, hơn 100% vốn chủ sở hữu (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2617). Nguồn ghi phép tính:
$$209 \text{ tỷ USD} \times 2\% \times 3 \text{ năm} \approx 12{,}5 \text{ tỷ USD}$$
(tata_bank_alm, Ch.4, Notes, d.2671).

Để không là ngân hàng ngoại lệ theo phép thử ở trang [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]], mà nguồn tóm tắt là rủi ro EVE với cú sốc 2% phải dưới 15% vốn chủ sở hữu, duration của tiền gửi phải lớn hơn 3,7 năm (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2619). Nguồn ghi phép tính:
$$4{,}1 \text{ năm} - \frac{15\% \times 12 \text{ tỷ USD}}{209 \text{ tỷ USD} \times 2\%} \approx 3{,}7 \text{ năm}$$
(tata_bank_alm, Ch.4, Notes, d.2677). Nguồn đánh giá đó là một giả định rất thiếu hợp lý (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2619). Cách SVB xử lý giả định duration tiền gửi nằm ở trang [[regulatory-arbitrage-via-deposit-duration-assumptions-distorts-supervisory-irrbb-compliance]].
