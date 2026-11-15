---
title: tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket
type: concept
tags: [vietnam, tt83, irrbb, term-deposits, early-redemption, behavioral-modeling, eve]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
driven_by: [tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay]
analogous: [tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario]
related: [interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options, retail-term-deposits-beyond-30-days-leave-lcr-outflows-unless-withdrawable-without-penalty]
---

Với tiền gửi có kỳ hạn của cá nhân có rủi ro rút trước hạn, TT83 tính tỷ lệ rút trước hạn (term deposit redemption ratio, TDRR) của từng kịch bản sốc bằng tỷ lệ cơ sở nhân hệ số 1,2 hoặc 0,8, chặn trên ở 100%, và đưa toàn bộ phần rút trước vào thang qua đêm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2574–2603). Quyền rút tiền trước hạn của người gửi là một quyền lựa chọn hành vi thuộc [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options|rủi ro quyền chọn]] phía nợ phải trả.

Ngân hàng tự đặt tiêu chí nhận diện tiền gửi có kỳ hạn có rủi ro rút trước hạn trong quy định nội bộ, cho cả cá nhân lẫn tổ chức (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2572). Với cá nhân, ngân hàng gom tiền gửi cùng đặc điểm và cùng đồng tiền $c$ thành danh mục $p$, ước tỷ lệ rút trước cơ sở $TDRR^{p}_{0,c}$ trong điều kiện hiện hành, rồi tính tỷ lệ theo kịch bản $i$ (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2576–2580):

$$TDRR^{p}_{i,c} = \min\left(1,\ u_i \times TDRR^{p}_{0,c}\right)$$

Hệ số $u_i$ bằng 1,2 ở cú sốc tăng song song, phẳng và tăng lãi suất ngắn hạn; bằng 0,8 ở cú sốc giảm song song, dốc và giảm lãi suất ngắn hạn (tt83_2025_sbv, Phụ lục V, phần A Bước 2, Bảng 4, d.2586–2593). So với hệ số của [[tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario|tỷ lệ trả nợ trước hạn]], bốn kịch bản song song và ngắn hạn đảo chiều, còn hai kịch bản dốc và phẳng giữ cùng hệ số. Sáu kịch bản lấy từ [[tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay|bộ kịch bản sốc của TT83]].

Dòng tiền rút trước hạn bằng số dư còn lại của danh mục nhân tỷ lệ rút, và nằm ở thang đầu tiên trong [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|19 thang kỳ hạn]], thang qua đêm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2597–2603):

$$CF^{p}_{i,c}(1) = TD^{p}_{0,c} \times TDRR^{p}_{i,c}$$

Khác với khoản vay trả trước, nơi phần trả trước được tính dần trên dư nợ từng thang, TT83 coi phần tiền gửi rút trước là rút ngay ở thang qua đêm. Với tiền gửi có kỳ hạn của tổ chức, ngân hàng tự xác định dòng tiền để đo ΔEVE (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2605). Cùng loại tiền gửi này xuất hiện ở LCR theo tiêu chí khác, xem [[retail-term-deposits-beyond-30-days-leave-lcr-outflows-unless-withdrawable-without-penalty]]: ở đó câu hỏi là tiền gửi có rút được trong 30 ngày không, còn ở TT83 câu hỏi là lãi suất thay đổi làm tỷ lệ rút đổi bao nhiêu.
