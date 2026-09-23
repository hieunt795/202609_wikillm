---
title: earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights
type: concept
tags: [alm, irrbb, earning-gap, nii, sensitivity, gap-analysis]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Phân tích khe hở thu nhập (Earning Gap Analysis, hay Income Gap Analysis) là kỹ thuật tổng hợp tinh gọn dùng để đo lường độ nhạy cảm của thu nhập lãi thuần ([[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]]) trước một cú sốc thay đổi lãi suất song song 1% (100 bps) trong chân trời ngắn hạn một năm (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1065). Về mặt quy trình, phương pháp này có nhiều điểm tương đồng với [[repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date]], nhưng có sự khác biệt bản chất: phân tích Earning Gap giới hạn nghiêm ngặt phạm vi quan sát trong năm tài chính đầu tiên (thường chia thành 4 dải kỳ hạn: dưới 1 tháng, 1–3 tháng, 3–6 tháng và 6–12 tháng) thay vì kéo dài toàn bộ vòng đời đến khi tất toán (*run-off*) như phương pháp EVE (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1065–1069).

Cốt lõi toán học của mô hình nằm ở việc xác định điểm giữa (*midpoint*) của từng dải kỳ hạn và tính toán khoảng thời gian chịu tác động còn lại trong năm đầu tiên (*1st year impact* = 12 tháng trừ đi điểm giữa) (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1075–1084). Trực giác kinh tế rất rõ ràng: các vị thế được điều chỉnh lãi suất sớm (ví dụ dải 1–3 tháng có điểm giữa là 2 tháng, chịu tác động 10 tháng còn lại) sẽ có nhiều thời gian khuếch đại tác động lên doanh thu hoặc chi phí lãi hàng năm; ngược lại, các vị thế tái định giá muộn (như dải 6–12 tháng có điểm giữa 9 tháng, chỉ chịu tác động 3 tháng) sẽ ảnh hưởng rất hạn chế tới NII của năm đó (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1075).

Khe hở thu nhập định kỳ (*Periodic Earning Gap*) cho từng dải kỳ hạn trước cú sốc lãi suất dịch chuyển $\Delta r = 1\%$ được xác định theo công thức:
$$Periodic\ Earning\ Gap = Net\ Repricing\ Gap \times 1\% \times \left(\frac{1st\ Year\ Impact}{12}\right)$$
trong đó $Net\ Repricing\ Gap$ là chênh lệch tài sản trừ nợ trong dải kỳ hạn tương ứng (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1095). Tổng khe hở thu nhập (*Total Earning Gap*) là tổng đại số của các khe hở định kỳ trong năm đầu tiên (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1095).

Trong ví dụ định lượng của Tata, dải 1–3 tháng có $Net\ Repricing\ Gap = -150$, tạo ra khe hở thu nhập định kỳ âm là $-150 \times 1\% \times (10 / 12) = -1{,}25$, hàm ý chi phí lãi vay tăng nhanh hơn thu nhập lãi khi lãi suất tăng (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1095). Kết hợp với các dải 3–6 tháng ($+0{,}625$) và 6–12 tháng ($+0{,}375$), Total Earning Gap của ngân hàng đạt mức $-0{,}25$ (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1092–1097). Con số $-0{,}25$ chỉ ra rằng cứ mỗi 1% (100 bps) lãi suất tăng song song, NII năm đầu tiên của ngân hàng sẽ suy giảm 0,25 đơn vị; nếu lãi suất tăng vọt 400 bps ngay lập tức, ngân hàng dự kiến mất 1,0 đơn vị thu nhập lãi thuần (tata_bank_alm, Ch.2, Earning Gap Analysis, d.1097). Chỉ tiêu này giúp ban điều hành ALM đánh giá trực tiếp [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]] đối với lợi nhuận kế toán và lập kế hoạch phòng hộ phái sinh theo [[receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk]].
