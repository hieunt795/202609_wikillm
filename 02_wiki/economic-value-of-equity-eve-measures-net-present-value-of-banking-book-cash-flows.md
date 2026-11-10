---
title: economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows
type: concept
tags: [alm, irrbb, eve, valuation, discount-rate]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governs: [interest-rate-risk-in-the-banking-book-irrbb]
governed_by: [repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date, duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
contrasts: [held-to-maturity-gaap-accounting-masks-unrealized-economic-value-losses-in-banking-books]
related: [economic-value-and-earnings-perspectives-complement-each-other-in-alm, silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs]
---

Giá trị kinh tế của vốn chủ sở hữu (Economic Value of Equity — EVE) là thước đo định lượng dài hạn cốt lõi trong quản trị [[interest-rate-risk-in-the-banking-book-irrbb]], phản ánh giá trị hiện tại ròng ($NPV$) của toàn bộ các dòng tiền kỳ vọng phát sinh từ các công cụ tài chính nhạy cảm với lãi suất thuộc sổ ngân hàng cho đến khi tất toán hoàn toàn (*run-off*) (tata_bank_alm, Ch.2, Economic Value Measures, d.818–822). Giá trị kinh tế ($EV$) của một vị thế nội bảng hoặc ngoại bảng có thể khác giá trị ghi sổ kế toán (accounting value); ví dụ, một khoản cho vay có thể được ghi nhận theo mệnh giá 100% trên bảng cân đối kế toán nhưng lại sở hữu giá trị kinh tế cao hơn nếu lãi suất danh nghĩa ký kết cao hơn mặt bằng lãi suất chiết khấu thị trường hiện hành (tata_bank_alm, Ch.2, Economic Value Measures, d.824).

Về mặt cấu trúc đại số, EVE được xác định tại một thời điểm xác định bằng hiệu số giữa giá trị kinh tế của tổng tài sản ($A$) và tổng nợ phải trả ($L$), cộng trừ giá trị kinh tế của các cam kết ngoại bảng ($OBS$): $EVE = EV(A) - EV(L) + EV(OBS_A) - EV(OBS_L)$ (tata_bank_alm, Ch.2, Economic Value of Equity, d.830). Trong mô hình định giá chiết khấu dòng tiền, vốn chủ sở hữu ($E$) không thể là một biến số đầu vào (*input*) của phép tính EVE, vì khi đó nó sẽ tác động lên giá trị kinh tế của chính nó (tata_bank_alm, Ch.2, Economic Value of Equity, d.830).

Giá trị kinh tế của từng công cụ đơn lẻ được tính toán dựa trên tổng hiện giá của các dòng tiền kỳ vọng: $EV = \sum_{t=1}^{T} \frac{CF_t}{(1 + r)^t}$, trong đó $CF_t$ là dòng tiền tại năm $t$, $T$ là kỳ hạn tất toán cuối cùng và $r$ là lãi suất chiết khấu năm, giả định không đổi theo thời gian và phù hợp với môi trường lãi suất hiện tại (tata_bank_alm, Ch.2, Economic Value Calculation, d.862–866). Khi mặt bằng lãi suất dịch chuyển một biên độ $\Delta r$, lãi suất chiết khấu chuyển thành $(r + \Delta r)$, dẫn đến biến thiên giá trị kinh tế $\Delta EV$ (tata_bank_alm, Ch.2, Economic Value Calculation, d.868). Nếu các dòng tiền có tính nhạy cảm nội sinh với lãi suất — ví dụ các khoản vay có quyền chọn trả trước hoặc các công cụ thả nổi — mô hình bắt buộc phải tái điều chỉnh dòng tiền $CF_t$ thay vì giả định dòng tiền cố định (tata_bank_alm, Ch.2, Economic Value Calculation, d.870).

Mức thay đổi $\Delta EVE$ trước một thay đổi lãi suất cho trước được ước lượng qua [[repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date]] hoặc [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]]. Kết hợp với góc nhìn thu nhập theo [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]], biến thiên $\Delta EVE$ được giám sát chặt chẽ nhằm bảo đảm không làm xói mòn quá 15% vốn cấp 1 (Tier 1) trong khuôn khổ [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]] (tata_bank_alm, Ch.2, Economic Value of Equity, d.843–848).

Sự phân kỳ sống còn giữa giá trị kinh tế EVE và giá trị sổ sách kế toán đã được bộc lộ trong vụ sụp đổ [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs]]: trong khi chuẩn mực kế toán ghi nhận danh mục 95 tỷ USD theo giá gốc phân bổ giúp che giấu khoản lỗ 15,2 tỷ USD theo [[held-to-maturity-gaap-accounting-masks-unrealized-economic-value-losses-in-banking-books]], góc nhìn giá trị kinh tế EVE định giá theo giá thị trường cho thấy toàn bộ 12 tỷ USD vốn tự có của ngân hàng đã bị xóa sổ hoàn toàn từ cuối năm 2022 trước khi cuộc tháo chạy tiền gửi chính thức diễn ra (tata_bank_alm, Ch.4, 4.3.1 At a Glance: GAAP vs. Non-GAAP, d.2587–2591).
