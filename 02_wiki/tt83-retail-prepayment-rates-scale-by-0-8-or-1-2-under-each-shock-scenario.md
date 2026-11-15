---
title: tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario
type: concept
tags: [vietnam, tt83, irrbb, prepayment, behavioral-modeling, eve]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
driven_by: [tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay]
analogous: [tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket]
related: [mortgage-prepayments-combine-demographic-attrition-economic-refinancing-and-burn-out-effects, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]
---

Với khoản cho vay cá nhân lãi suất cố định có rủi ro trả trước hạn, TT83 tính tỷ lệ trả trước có điều kiện (conditional prepayment rate, CPR) của từng kịch bản sốc bằng tỷ lệ cơ sở nhân hệ số 0,8 hoặc 1,2, chặn trên ở 100% (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2529–2552). Đây là cách TT83 đưa quyền trả nợ trước hạn, một nhánh hành vi của [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options|rủi ro quyền chọn]], vào phép tính ΔEVE.

Ngân hàng tự đặt tiêu chí nhận diện khoản vay có rủi ro trả trước hạn trong quy định nội bộ, cho cả khách hàng cá nhân lẫn tổ chức (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2527). Với khách hàng cá nhân, ngân hàng gom khoản vay cùng đặc điểm và cùng đồng tiền $c$ thành danh mục $p$, ước tỷ lệ trả trước cơ sở $CPR^{p}_{0,c}$ trong điều kiện hiện hành, rồi tính tỷ lệ theo kịch bản $i$ (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2531–2539):

$$CPR^{p}_{i,c} = \min\left(1,\ \gamma_i \times CPR^{p}_{0,c}\right)$$

Hệ số $\gamma_i$ bằng 0,8 ở ba kịch bản cú sốc tăng song song, dốc và tăng lãi suất ngắn hạn; bằng 1,2 ở ba kịch bản cú sốc giảm song song, phẳng và giảm lãi suất ngắn hạn (tt83_2025_sbv, Phụ lục V, phần A Bước 2, Bảng 3, d.2545–2552). Thông tư không giải thích cách chọn hệ số; các động cơ trả trước hạn của người vay, trong đó có tái cấp vốn khi lãi suất giảm, nằm ở trang [[mortgage-prepayments-combine-demographic-attrition-economic-refinancing-and-burn-out-effects]]. Sáu kịch bản lấy từ [[tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay|bộ kịch bản sốc của TT83]].

Dòng tiền của danh mục ở thang kỳ hạn $k$ là khoản trả gốc, lãi định kỳ theo lịch cộng phần trả trước tính trên dư nợ gốc còn lại ở thang trước (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2556–2566):

$$CF^{p}_{i,c}(k) = CF^{S}_{i,c}(k) + CPR^{p}_{i,c} \times N^{p}_{i,c}(k-1)$$

Dòng tiền này đi vào [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|19 thang kỳ hạn]] như dòng tiền thường. Với khoản vay của tổ chức, thông tư không cho công thức; ngân hàng tự xác định dòng tiền để đo ΔEVE (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2568). Tiền gửi có kỳ hạn dùng cùng kiểu hệ số nhân ở [[tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket|tỷ lệ rút trước hạn]], với hướng ngược lại ở các kịch bản song song và ngắn hạn.
