---
title: tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints
type: concept
tags: [vietnam, tt83, irrbb, eve, time-buckets, repricing]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios]
driven_by: [tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups]
analogous: [repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date]
related: [tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay, tt83-core-non-maturity-deposits-are-capped-at-90-70-and-50-percent-of-each-segment, tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario, tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket]
---

Bước 2 của [[tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios|phép tính ΔEVE trong TT83]] xếp dòng tiền định giá lại vào một trong 19 thang kỳ hạn theo ngày định giá lại, hoặc vào điểm giữa $t_k$ của các thang (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2441–2445). Khi dùng điểm giữa, ngân hàng chia một dòng tiền thành hai phần đặt ở hai điểm giữa liền kề sao cho kỳ hạn của dòng tiền không đổi (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2445).

Mười chín thang đi từ qua đêm, với $t_k$ = 0,0028 năm, tới trên 20 năm, với $t_k$ = 25 năm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, Bảng 1, d.2459–2483). Dưới một năm có sáu thang: qua đêm, tới 1 tháng, tới 3 tháng, tới 6 tháng, tới 9 tháng, tới 1 năm. Từ 1 năm tới 2 năm có hai thang nửa năm, từ 2 năm tới 10 năm có tám thang một năm, sau đó là ba thang 10–15 năm, 15–20 năm và trên 20 năm. Điểm giữa $t_k$ được dùng lại ở [[tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay|công thức cú sốc]] và trong hệ số chiết khấu.

Cách xếp phụ thuộc nhóm mà [[tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups|bước 1]] đã gán (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2449–2489). Khoản mục lãi suất cố định đưa gốc và lãi vào thang của ngày trả. Khoản mục lãi suất thả nổi đưa gốc và lãi định kỳ tới ngày định giá lại kế tiếp vào thang của ngày trả, rồi đưa toàn bộ gốc còn lại vào thang của ngày định giá lại kế tiếp. Quy tắc thả nổi này giống quy tắc "chỉ tính tới ngày điều chỉnh lãi suất kế tiếp" của [[repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date|phân tích khe hở tái định giá]]. Nhóm quyền chọn lãi suất tự động không được xếp dòng tiền; ngân hàng đo riêng phần này ở bước 4.

Nhóm sản phẩm hành vi có quy tắc riêng: [[tt83-core-non-maturity-deposits-are-capped-at-90-70-and-50-percent-of-each-segment|tiền gửi không kỳ hạn]] chia lõi và không lõi, [[tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario|khoản vay có rủi ro trả trước]] thêm dòng trả trước theo kịch bản, [[tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket|tiền gửi có kỳ hạn có rủi ro rút trước]] đưa phần rút trước vào thang qua đêm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2489–2605).
