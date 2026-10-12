---
title: receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk
type: concept
tags: [alm, irrbb, swaps, hedging, nii, eve, trade-off]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
drives: [net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations, repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date, duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]
driven_by: [interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves]
related: [economic-value-and-earnings-perspectives-complement-each-other-in-alm]
---

Trong quản trị rủi ro thu nhập lãi thuần ([[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]]), một cách giữ NII ổn định khi lãi suất giảm là vào hợp đồng hoán đổi lãi suất nhận lãi cố định và trả lãi thả nổi (Receiver Interest Rate Swap) (tata_bank_alm, Ch.2, Hedging NII, d.1387). Trong bảng cân đối ALM, hai vế của hợp đồng hoán đổi được hạch toán tách biệt: chân nhận lãi cố định được ghi nhận tương đương một tài sản sinh lời ổn định (như trái phiếu coupon cố định), trong khi chân trả lãi thả nổi được ghi nhận tương đương một khoản nợ phải trả định kỳ (tương tự tiền gửi ngắn hạn) (tata_bank_alm, Ch.2, Hedging NII, d.1395). Khi lãi suất giảm 100 bps, chi phí chân thả nổi giảm xuống trong khi nguồn thu chân cố định được bảo toàn, bù đắp sự sụt giảm nguồn thu từ các khoản cho vay lãi suất thả nổi (tata_bank_alm, Ch.2, Hedging NII, d.1495–1505).

Tata nêu các lưu ý về kết quả mô phỏng này (tata_bank_alm, Ch.2, Caveats, d.1509–1518). Lưu ý thứ nhất là kết quả trông quá tốt (*too good to be true*): nếu ngân hàng lập mô hình dự phóng NII dựa trên giả định đường cong lãi suất không đổi ([[interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves]]) trong một môi trường đường cong dốc lên (*upward sloping*), hợp đồng receiver swap dường như cải thiện NII trong mọi chu kỳ mô phỏng (tata_bank_alm, Ch.2, Caveats, d.1511–1513). Trên thực tế, lãi suất cố định phản ánh mức bình quân kỳ vọng của lãi suất thả nổi tương lai; nếu lãi suất tăng đúng như lãi suất kỳ hạn hàm ý, lợi thế trả lãi thả nổi thấp mất dần và lãi suất ngắn hạn có lúc vượt lãi suất cố định (tata_bank_alm, Ch.2, Caveats, d.1513). Ví dụ ở châu Âu giai đoạn 2019–2020: một số bên tham gia thị trường vào hợp đồng hoán đổi 10 năm nhận mức cố định $-0{,}25\%$ khi EURIBOR đang ở mức $-0{,}50\%$ nhằm hưởng chênh lệch $+25$ bps; nhưng khi EURIBOR tăng vọt vượt 4% vào năm 2023, NII thực nhận của hợp đồng chuyển từ $+25$ bps thành $-425$ bps mỗi năm (tata_bank_alm, Ch.2, Caveats, d.1515).

Lưu ý thứ hai là góc nhìn thu nhập và góc nhìn giá trị kinh tế thường phản ứng ngược nhau trước thay đổi lãi suất: giao dịch hoán đổi làm NII ổn định hơn nhưng làm tăng rủi ro ở phía giá trị kinh tế (tata_bank_alm, Ch.2, Caveats, d.1517). Trong ví dụ của Tata, thêm hợp đồng hoán đổi 3 năm làm tổng khe hở tái định giá của ngân hàng tăng từ $1{,}74$ lên $3{,}63$, tức mức tổn thất giá trị kinh tế tăng khoảng gấp đôi theo [[repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date]] và [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]] khi lãi suất tăng (tata_bank_alm, Ch.2, Caveats, d.1517; tata_bank_alm, Ch.2, Caveats, d.1550). Quan hệ ngược chiều giữa hai góc đo được bàn ở trang [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]].
