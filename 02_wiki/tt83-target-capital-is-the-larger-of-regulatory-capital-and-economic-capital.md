---
title: tt83-target-capital-is-the-larger-of-regulatory-capital-and-economic-capital
type: concept
tags: [capital, icaap, economic-capital, vietnam, tt83]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-17
part_of: [internal-capital-adequacy-assessment-process-icaap]
has_part: [tt83-concentration-risk-rwa-is-floored-by-exposures-above-a-declining-share-of-own-funds]
driven_by: [tt83-capital-stress-tests-map-rate-fx-gold-and-credit-assumptions-onto-each-risk-type-rwa]
related: [capital-adequacy-ratio-car, vietnamese-banks-may-measure-irrbb-by-delta-nii-or-delta-eve-alone-until-end-2027, risk-adjusted-return-on-capital-raroc]
---

Theo TT83, vốn mục tiêu của ngân hàng là số lớn hơn giữa vốn cần để đáp ứng [[capital-adequacy-ratio-car|tỷ lệ an toàn vốn]] theo quy định và vốn kinh tế do ngân hàng tự tính trong [[internal-capital-adequacy-assessment-process-icaap|ICAAP]] (tt83_2025_sbv, Phụ lục VI, mục I, điểm 2, d.2843–2851):

$$C_{Target} = \max(C_R, C_E)$$

$C_R$ là vốn tự có cần để đạt tỷ lệ an toàn vốn theo quy định của NHNN. Vốn kinh tế $C_E$ cộng hai phần (tt83_2025_sbv, Phụ lục VI, mục I, điểm 1, d.2768–2782):

$$C_{E} = RWA^{*}_{E} \times CAR_{Target} + \Delta RWA_{B} \times CAR_{R}$$

Phần thứ nhất nhân tổng tài sản tính theo rủi ro trong kịch bản bình thường $RWA^*_E$ với tỷ lệ an toàn vốn mục tiêu $CAR_{Target}$ mà ngân hàng ghi trong khẩu vị rủi ro. Phần thứ hai nhân $\Delta RWA_B$, phần tăng dương của tổng tài sản tính theo rủi ro khi chuyển sang kịch bản bất lợi, với tỷ lệ an toàn vốn theo quy định $CAR_R$. Như vậy, phần đệm cho kịch bản bất lợi chỉ phải đạt mức tối thiểu luật định, còn phần cho kịch bản bình thường phải đạt mức mục tiêu. $\Delta RWA_B$ lấy từ [[tt83-capital-stress-tests-map-rate-fx-gold-and-credit-assumptions-onto-each-risk-type-rwa|kiểm tra sức chịu đựng về vốn]].

$RWA^*_E$ gồm sáu cấu phần (tt83_2025_sbv, Phụ lục VI, mục I, điểm 1.d, d.2782–2841):

$$RWA^{*}_{E} = RWA_{CR} + RWA_{OR} + RWA_{MR} + RWA_{IRRBB} + RWA_{COR} + RWA_{OMR}$$

Rủi ro tín dụng $RWA_{CR}$, rủi ro hoạt động $RWA_{OR}$ và rủi ro thị trường $RWA_{MR}$ tính theo quy định của NHNN về tỷ lệ an toàn vốn. [[tt83-concentration-risk-rwa-is-floored-by-exposures-above-a-declining-share-of-own-funds|Rủi ro tập trung $RWA_{COR}$]] do ngân hàng tự tính nhưng có sàn. Rủi ro lãi suất trên sổ ngân hàng $RWA_{IRRBB}$ do ngân hàng tự tính, và từ 01/01/2028 phải tính theo ΔEVE, như ghi ở [[vietnamese-banks-may-measure-irrbb-by-delta-nii-or-delta-eve-alone-until-end-2027]]. Rủi ro trọng yếu khác $RWA_{OMR}$ do ngân hàng tự tính và không gồm rủi ro thanh khoản. Vốn kinh tế cũng là mẫu số của [[risk-adjusted-return-on-capital-raroc|RAROC]].
