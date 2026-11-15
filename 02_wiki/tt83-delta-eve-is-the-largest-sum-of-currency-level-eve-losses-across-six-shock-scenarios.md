---
title: tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios
type: concept
tags: [vietnam, tt83, irrbb, eve, discounting, stress-testing]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [circular-83-2025-tt-nhnn-internal-control-systems-of-banks]
has_part: [tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups, tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
driven_by: [tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay]
governs: [economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows]
contrasts: [eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement, tt83-delta-nii-is-the-larger-one-year-nii-loss-under-parallel-up-and-down-shocks]
related: [interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]
---

Theo Phụ lục V của [[circular-83-2025-tt-nhnn-internal-control-systems-of-banks|TT83]], số đo IRRBB theo ΔEVE là tổng mức giảm giá trị kinh tế của vốn chủ sở hữu trên các đồng tiền bị lỗ, lấy ở kịch bản cho tổng lỗ lớn nhất trong sáu kịch bản sốc lãi suất (tt83_2025_sbv, Phụ lục V, phần A Bước 5, d.2661–2663). ΔEVE ở đây là thay đổi của giá trị hiện tại ròng giữa dòng tiền vào của tài sản nhạy cảm lãi suất và dòng tiền ra của nợ phải trả nhạy cảm lãi suất, tính cả ngoại bảng, khi lãi suất đổi (tt83_2025_sbv, Phụ lục V, phần A, d.2395–2399); đây là phiên bản quy định của [[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows|giá trị kinh tế của vốn chủ sở hữu (EVE)]].

Phép tính có năm bước. Bước 1 [[tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups|chọn khoản mục và chia ba nhóm]], bước 2 [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|xếp dòng tiền vào 19 thang kỳ hạn]]. Bước 3 tính EVE cho từng đồng tiền $c$ dưới mỗi kịch bản $i$ trong [[tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay|sáu kịch bản sốc]] (tt83_2025_sbv, Phụ lục V, phần A Bước 3, d.2607–2645). Ở mỗi thang $k$, ngân hàng lấy dòng tiền vào trừ dòng tiền ra thành dòng tiền ròng $CF_{i,c}(k)$, rồi chiết khấu bằng hệ số chiết khấu lãi kép liên tục theo lãi suất phi rủi ro của kịch bản đó:

$$DF_{i,c}(t_k) = \exp\left(-R_{i,c}(t_k) \times t_k\right), \qquad EVE^{nao}_{i,c} = \sum_{k=1}^{K} CF_{i,c}(k) \times DF_{i,c}(t_k)$$

Chỉ số $nao$ nghĩa là chưa gồm quyền chọn lãi suất tự động; nếu ngân hàng xếp dòng tiền vào điểm giữa thang thì thay $CF_{i,c}(k)$ bằng $CF_{i,c}(t_k)$ (tt83_2025_sbv, Phụ lục V, phần A Bước 3, d.2637–2645). Khác với công thức chiết khấu một lãi suất không đổi ở trang EVE, TT83 dùng lãi suất riêng cho từng điểm $t_k$. Bước 4 để ngân hàng tự đo phần [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options|quyền chọn lãi suất tự động]] của từng đồng tiền dưới từng kịch bản, ký hiệu $KAO_{i,c}$ (tt83_2025_sbv, Phụ lục V, phần A Bước 4, d.2647).

Bước 5 lấy EVE hiện hành trừ EVE theo kịch bản rồi cộng $KAO_{i,c}$ (tt83_2025_sbv, Phụ lục V, phần A Bước 5, d.2649–2659):

$$\Delta EVE_{i,c} = \sum_{k=1}^{K} CF_{0,c}(k)\, DF_{0,c}(t_k) - \sum_{k=1}^{K} CF_{i,c}(k)\, DF_{i,c}(t_k) + KAO_{i,c}$$

Với quy ước này, $\Delta EVE_{i,c} > 0$ là giá trị kinh tế giảm. Trang [[eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement|phương pháp chuẩn hóa của EBA]] ghi thay đổi EVE theo chiều ngược lại, EVE kịch bản sốc trừ EVE cơ sở, nên cùng một mức lỗ mang dấu ngược nhau ở hai khung. Mỗi kịch bản, ngân hàng chỉ cộng các đồng tiền có $\Delta EVE_{i,c} > 0$; đồng tiền có lãi giá trị không được bù trừ (tt83_2025_sbv, Phụ lục V, phần A Bước 5, d.2661–2663):

$$\Delta EVE = \max_{i \in \{1,\dots,6\}} \left\{ \max\left(0;\ \sum_{c:\ \Delta EVE_{i,c} > 0} \Delta EVE_{i,c}\right) \right\}$$

Nguồn viết chỉ số tổng là "K=1 tới K"; trang này ghi lại thành $k = 1, \dots, K$. Số đo ΔEVE đi cùng [[tt83-delta-nii-is-the-larger-one-year-nii-loss-under-parallel-up-and-down-shocks|số đo ΔNII]], vốn dùng hai thay vì sáu kịch bản và chân trời một năm thay vì toàn bộ dòng tiền.
