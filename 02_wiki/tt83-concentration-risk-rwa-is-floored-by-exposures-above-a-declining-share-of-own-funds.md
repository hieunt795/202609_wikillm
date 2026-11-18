---
title: tt83-concentration-risk-rwa-is-floored-by-exposures-above-a-declining-share-of-own-funds
type: concept
tags: [capital, icaap, concentration-risk, vietnam, tt83]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-17
part_of: [tt83-target-capital-is-the-larger-of-regulatory-capital-and-economic-capital]
governs: [concentration-risk]
---

Trong vốn kinh tế theo TT83, tổng tài sản tính theo [[concentration-risk|rủi ro tập trung]] $RWA_{COR}$ gồm phần của hoạt động cấp tín dụng $RWA^1_{COR}$ và phần của hoạt động tự doanh $RWA^2_{COR}$; cả hai do ngân hàng tự xây phương pháp, nhưng phần cấp tín dụng không được thấp hơn một sàn công thức (tt83_2025_sbv, Phụ lục VI, mục I, điểm 1.d.iii, d.2804–2837). Đây là một trong sáu cấu phần cộng thành tổng tài sản tính theo rủi ro dùng để tính [[tt83-target-capital-is-the-larger-of-regulatory-capital-and-economic-capital|vốn kinh tế và vốn mục tiêu]].

$$RWA_{COR} = RWA^{1}_{COR} + RWA^{2}_{COR}$$

$$RWA^{1*}_{COR} = \max\{E_{i} - A \times C;\ 0\} + \max\{E_{j} - B \times C;\ 0\}$$

$E_i$ là tổng dư nợ cấp tín dụng với một khách hàng, $E_j$ là tổng dư nợ với một khách hàng và người có liên quan; cả hai không tính khoản có hệ số rủi ro 0% và khoản đã trừ khỏi vốn tự có. $C$ là vốn tự có của ngân hàng. Sàn chỉ đếm phần dư nợ vượt A% vốn tự có với một khách hàng, và phần vượt B% vốn tự có với một khách hàng cùng người có liên quan; dư nợ dưới ngưỡng không làm tăng sàn.

A và B giảm dần theo lộ trình (tt83_2025_sbv, Phụ lục VI, mục I, điểm 1.d.iii, Bảng 10, d.2818–2827):

| Từ ngày | A (một khách hàng, %) | B (khách hàng và người có liên quan, %) |
|---|---|---|
| 01/07/2026 | 8,7 | 16,8 |
| 01/01/2027 | 8 | 15,2 |
| 01/01/2028 | 7,3 | 13,6 |
| 01/01/2029 | 6,5 | 12 |

Với cùng dư nợ và cùng vốn tự có, ngưỡng hạ dần làm sàn $RWA^{1*}_{COR}$ tăng qua từng mốc, kéo vốn kinh tế lên nếu ngân hàng không giảm dư nợ tập trung. TT83 không đặt sàn cho phần tự doanh $RWA^2_{COR}$.
