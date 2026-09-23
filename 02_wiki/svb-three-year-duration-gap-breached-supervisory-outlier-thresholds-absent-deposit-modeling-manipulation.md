---
title: svb-three-year-duration-gap-breached-supervisory-outlier-thresholds-absent-deposit-modeling-manipulation
type: concept
tags: [alm, irrbb, duration-gap, supervisory-outlier-test, eve, svb]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Phân tích khe hở thời lượng theo [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]] bộc lộ bản chất rủi ro cơ cấu trên bảng cân đối của Silicon Valley Bank trước khi sụp đổ: sự lệch pha sâu sắc giữa tài sản có thời lượng rất dài và nguồn vốn nợ có thời lượng rất ngắn (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2609). Bên phía tài sản, các khoản đầu tư nắm giữ đến ngày đáo hạn (HTM) có thời lượng bình quân lên tới 6,25 năm (tata_bank_alm, Ch.4, 4.3.1 At a Glance: GAAP vs. Non-GAAP, d.2591; tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2609). Bên phía nguồn vốn nợ, khoảng 45% tổng tiền gửi là dòng tiền nhàn rỗi tạm thời (*parked tech money*) của các công ty khởi nghiệp và quỹ đầu tư mạo hiểm đang chờ đợi cơ hội giải ngân, có kỳ hạn thực tế ngắn hơn 1 năm (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2609).

Ngay cả khi giả định thời lượng bình quân của dòng tiền gửi công nghệ này là 1 năm, khe hở thời lượng ($DG$) của SVB vẫn ở mức xấp xỉ 3 năm (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2617). Áp dụng công thức biến thiên giá trị kinh tế $\Delta EVE \approx -DG \times A \times \Delta r$ với quy mô tài sản $A = 209$ tỷ USD và cú sốc lãi suất tăng chuẩn 200 điểm cơ bản (2%) của Ủy ban Basel, mức tổn thất giá trị kinh tế được tính toán là:
$$\Delta EVE \approx 209 \text{ tỷ USD} \times 2\% \times 3 \text{ [năm]} \approx 12{,}5 \text{ tỷ USD}$$
(tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2617; tata_bank_alm, Ch.4, Notes, d.2671). Mức sụt giảm 12,5 tỷ USD này vượt quá 100% quy mô vốn chủ sở hữu sổ sách 12 tỷ USD của SVB, đồng nghĩa với việc ngân hàng rơi vào trạng thái mất toàn bộ vốn tự có trước một cú sốc lãi suất tiêu chuẩn (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2617).

Khi đối chiếu với quy định kiểm tra ngoại lệ giám sát theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]], cơ quan giám sát yêu cầu mức giảm EVE trước cú sốc lãi suất 2% không được vượt quá 15% vốn chủ sở hữu (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2619). Để SVB không bị xếp vào nhóm ngân hàng ngoại lệ (*outlier bank*), thời lượng của nguồn tiền gửi ($D_L$) trên mô hình phải thỏa mãn điều kiện toán học:
$$D_L > 4{,}1 \text{ [năm]} - \frac{15\% \times 12 \text{ tỷ USD}}{209 \text{ tỷ USD} \times 2\%} \approx 3{,}7 \text{ năm}$$
(tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2619; tata_bank_alm, Ch.4, Notes, d.2676). Việc gán thời lượng vượt 3,7 năm cho nguồn tiền gửi không kỳ hạn không bảo hiểm của các quỹ đầu tư mạo hiểm là một giả định hoàn toàn phi thực tế (tata_bank_alm, Ch.4, 4.3.3 Duration Gap, d.2619), thúc đẩy SVB thực hiện [[regulatory-arbitrage-via-deposit-duration-assumptions-distorts-supervisory-irrbb-compliance]] và trở thành nguyên nhân kỹ thuật hàng đầu dẫn tới [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs]].
