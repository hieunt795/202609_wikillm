---
title: maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb
type: concept
tags: [irrbb, eba, linear-floor, interest-rate-floor, yield-curve, rts-2022-10, eu-2024-856]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
related: [multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]
---

Sàn lãi suất sau sốc phụ thuộc kỳ hạn (maturity-dependent post-shock interest rate floor) là mức chặn dưới áp cho lãi suất sau khi áp kịch bản sốc trong phép thử ở trang [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]]. Hướng dẫn EBA/GL/2018/02, đoạn 115(k), định nghĩa sàn này cho từng đồng tiền: bắt đầu ở −100 điểm cơ bản với kỳ hạn tức thời, tăng 5 điểm cơ bản mỗi năm và đạt 0% ở kỳ hạn từ 20 năm trở lên (tata_bank_alm, Ch.5, 5.1.3 EBA, d.2847, d.2867).

Tiêu chuẩn kỹ thuật RTS/2022/10 hiệu chỉnh lại sàn này, vì trong tháng 12/2020 và tháng 3/2022 lãi suất cơ sở (chưa sốc) đã xuống dưới mức sàn (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919). Sàn mới, gọi là sàn tuyến tính (linear floor), bắt đầu ở −150 điểm cơ bản với kỳ hạn tức thời, tăng tuyến tính 3 điểm cơ bản mỗi năm và đạt 0% ở kỳ hạn 50 năm (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2919). Viết thành công thức theo mô tả đó, sàn ở kỳ hạn $t$ năm là $-150 + 3t$ điểm cơ bản với $0 \le t \le 50$.

Nguồn ghi sàn tuyến tính trong phần về phép thử SOT trên EVE; phép tính SOT trên NII theo RTS/2022/10 hiện không có sàn tuyến tính (tata_bank_alm, Ch.5, 5.3.2 Supervisory Outlier Test on NII, d.2930). RTS/2022/10 là một trong các văn bản của EBA ở trang [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]].
