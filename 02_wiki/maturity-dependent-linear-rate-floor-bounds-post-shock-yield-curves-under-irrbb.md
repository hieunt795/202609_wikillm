---
title: maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb
type: concept
tags: [irrbb, eba, linear-floor, interest-rate-floor, yield-curve, rts-2022-10, eu-2024-856]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Sàn lãi suất phụ thuộc kỳ hạn hậu cú sốc (Maturity-Dependent Post-Shock Interest Rate Floor) là giới hạn chặn dưới kỹ thuật bắt buộc áp dụng cho đường cong lợi suất phi rủi ro khi mô phỏng các kịch bản sốc lãi suất giảm trong khuôn khổ quản trị rủi ro lãi suất sổ ngân hàng (tata_bank_alm, Ch.5, 5.1.3 EBA, d.2867; tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919). Mục đích của sàn lãi suất này là ngăn chặn việc các mô hình ALM ngoại suy ra các mức lãi suất âm sâu phi thực tế tại các kỳ hạn dài — điều có thể làm méo mó nghiêm trọng hiện giá chiết khấu dòng tiền và thổi phồng giá trị kinh tế của ngân hàng (tata_bank_alm, Ch.5, 5.1.3 EBA, d.2867).

Trong các văn bản hướng dẫn ban đầu (EBA/GL/2018/02 đoạn 115(k)), EBA từng quy định một mức sàn lãi suất hậu sốc bắt đầu từ $-100$ điểm cơ bản ($-1{,}0\%$) ở kỳ hạn tức thời và tăng tuyến tính 5 điểm cơ bản mỗi năm, đạt mức $0\%$ tại kỳ hạn 20 năm trở đi (tata_bank_alm, Ch.5, 5.1.3 EBA, d.2847, d.2867; tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919). Tuy nhiên, thực tế thị trường tiền tệ Châu Âu trong các giai đoạn tháng 12/2020 và tháng 03/2022 đã bộc lộ sự lỗi thời của cấu trúc này: mặt bằng lãi suất cơ sở chưa chịu sốc (*unshocked baseline rate*) của đồng EUR trên thực tế đã giảm sâu xuống dưới mức sàn lý thuyết của EBA (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919).

Để khắc phục kẽ hở này, Quy chế Ủy quyền CDR (EU) 2024/856 (trực tiếp kế thừa Tiêu chuẩn Kỹ thuật RTS/2022/10) đã tái hiệu chuẩn toàn diện và ban hành **Sàn Lãi suất Tuyến tính Mới (New Linear Floor)** (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919; tata_bank_alm, Ch.5, Notes, d.3058):
- Mức chặn dưới bắt đầu từ **$-150$ điểm cơ bản ($-1{,}5\%$)** đối với kỳ hạn tức thời ($t = 0$ năm);
- Mức sàn tăng tuyến tính với tốc độ **3 điểm cơ bản (3 bps) cho mỗi năm kỳ hạn**;
- Mức sàn đạt ngưỡng **$0\%$ tại kỳ hạn 50 năm** và duy trì ở mức $0\%$ cho toàn bộ các kỳ hạn dài hơn.

Về mặt công thức đại số, mức sàn lãi suất hậu sốc $Floor(t)$ tại kỳ hạn $t$ (tính bằng năm, $0 \le t \le 50$) được xác định bằng:
$$Floor(t) = -150 \text{ bps} + 3 \text{ bps} \times t$$
Khi thực hiện bài kiểm tra ngoại lệ giám sát đối với giá trị kinh tế của vốn chủ sở hữu theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]], đường cong lãi suất chiết khấu sau khi chịu các cú sốc giảm (như parallel shock down hay short rates shock down) tại mỗi điểm kỳ hạn $t$ không bao giờ được phép thấp hơn giá trị $Floor(t)$ này (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919). Đáng chú ý, cơ chế sàn tuyến tính mới này hiện chỉ áp dụng bắt buộc đối với phép tính EVE trong [[eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement]], trong khi bài kiểm tra SOT trên thu nhập lãi thuần NII hiện chưa áp dụng quy tắc sàn tuyến tính này (tata_bank_alm, Ch.5, 5.3.2 Supervisory Outlier Test on NII, d.2930), phản ánh sự phân tách kỹ thuật giữa hai góc nhìn theo [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]].
