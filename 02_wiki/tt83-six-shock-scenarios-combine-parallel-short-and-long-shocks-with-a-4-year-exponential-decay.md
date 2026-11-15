---
title: tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay
type: concept
tags: [vietnam, tt83, irrbb, interest-rate-shocks, yield-curve, stress-testing]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
driven_by: [tt83-shock-sizes-come-from-a-currency-table-or-a-16-year-average-rate-scaled-by-60-85-and-40-percent]
drives: [tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios, tt83-delta-nii-is-the-larger-one-year-nii-loss-under-parallel-up-and-down-shocks]
analogous: [supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
contrasts: [maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb]
related: [tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
---

TT83 dựng sáu kịch bản sốc lãi suất từ ba cú sốc gốc của mỗi đồng tiền: song song, ngắn hạn và dài hạn, trong đó cú sốc ngắn hạn tắt dần theo kỳ hạn với hệ số $e^{-t_k/4}$ và cú sốc dài hạn là phần bù của nó (tt83_2025_sbv, Phụ lục V, phần C mục I, d.2734–2756). Sáu kịch bản dùng cho [[tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios|ΔEVE]]; hai kịch bản song song dùng cho [[tt83-delta-nii-is-the-larger-one-year-nii-loss-under-parallel-up-and-down-shocks|ΔNII]].

Sáu kịch bản là cú sốc tăng song song, giảm song song, dốc, phẳng, tăng lãi suất ngắn hạn và giảm lãi suất ngắn hạn (tt83_2025_sbv, Phụ lục V, phần A Bước 3, d.2609–2621). Hai kịch bản song song đổi lãi suất bằng nhau ở mọi kỳ hạn. Kịch bản dốc hạ lãi suất ngắn hạn và nâng lãi suất dài hạn; kịch bản phẳng làm ngược lại. Hai kịch bản ngắn hạn chỉ đổi lãi suất ngắn hạn. Danh sách này trùng tên với sáu kịch bản của [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital|phép thử ngoại lệ giám sát của EU]].

Với tham số gốc $\bar{R}$ lấy từ [[tt83-shock-sizes-come-from-a-currency-table-or-a-16-year-average-rate-scaled-by-60-85-and-40-percent|bảng đồng tiền hoặc phép tính bình quân 16 năm]], cú sốc tại điểm giữa $t_k$ của mỗi [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|thang kỳ hạn]] là (tt83_2025_sbv, Phụ lục V, phần C mục I, d.2736–2750):

$$\Delta R_{parallel,c}(t_k) = \pm \bar{R}_{parallel,c}$$

$$\Delta R_{short,c}(t_k) = \pm \bar{R}_{short,c} \times S_{short}(t_k), \qquad S_{short}(t_k) = e^{-t_k/x},\ x = 4$$

$$\Delta R_{long,c}(t_k) = \pm \bar{R}_{long,c} \times S_{long}(t_k), \qquad S_{long}(t_k) = 1 - e^{-t_k/x}$$

Cú sốc dài hạn không phải một kịch bản riêng; nó chỉ là thành phần của hai kịch bản dốc và phẳng (tt83_2025_sbv, Phụ lục V, phần C mục I, d.2752–2756):

$$\Delta R_{steepener,c}(t_k) = -0{,}65\,\lvert \Delta R_{short,c}(t_k) \rvert + 0{,}9\,\lvert \Delta R_{long,c}(t_k) \rvert$$

$$\Delta R_{flattener,c}(t_k) = +0{,}8\,\lvert \Delta R_{short,c}(t_k) \rvert - 0{,}6\,\lvert \Delta R_{long,c}(t_k) \rvert$$

Với $x = 4$ và $t_k$ tính bằng năm, $S_{short}$ bằng 0,5 ở kỳ hạn khoảng 2,8 năm ($4 \ln 2$), nên cú sốc ngắn hạn còn một nửa ở quanh thang 2–3 năm và gần như bằng không ở thang trên 20 năm ($e^{-25/4} \approx 0{,}002$); đây là phép tính từ công thức, không phải số trong thông tư. Phụ lục V không quy định sàn chặn lãi suất sau sốc, khác với [[maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb|sàn lãi suất sau sốc phụ thuộc kỳ hạn]] của EBA.
