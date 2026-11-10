---
title: net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations
type: concept
tags: [alm, irrbb, nii, forecasting, baseline]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governs: [interest-rate-risk-in-the-banking-book-irrbb]
governed_by: [earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights]
drives: [earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
driven_by: [balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views, interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves]
related: [net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons, economic-value-and-earnings-perspectives-complement-each-other-in-alm]
---

Dự báo thu nhập lãi thuần (Net Interest Income Forecast — NII Forecast) là kịch bản cơ sở (baseline) để bộ phận ALM đo lường mức độ nhạy cảm của lợi nhuận ngân hàng trước các kịch bản sốc lãi suất thị trường (tata_bank_alm, Ch.2, NII Forecast, d.1019). Thu nhập lãi thuần ($NII$) là chênh lệch giữa doanh thu lãi phát sinh từ tài sản và chi phí lãi phải trả cho nguồn vốn nợ trong một kỳ xác định (tata_bank_alm, Ch.2, Earnings Measures, d.983). Trong khi khối kế toán tài chính tiếp cận NII theo góc nhìn hồi tố (retrospective / backward-looking) nhằm ghi nhận kết quả kinh doanh thực tế trong quá khứ, khối ALM đo mức phơi nhiễm lãi thuần theo hướng tương lai (prospective / forward-looking); EBA cũng yêu cầu thước đo này đối với [[interest-rate-risk-in-the-banking-book-irrbb]] (tata_bank_alm, Ch.2, Earnings Measures, d.987–991).

Khung thời gian dự báo của mô hình NII trong ALM thường giới hạn từ 1 đến 3 năm với các bước chia theo tháng, quý hoặc năm (tata_bank_alm, Ch.2, NII Forecast, d.1025). Việc kéo dài chân trời dự báo NII ra quá xa thường tạo ra cảm giác chính xác giả tạo (*false sense of accuracy*), bởi hành vi khách hàng và quy mô danh mục kinh doanh không thể duy trì độ tin cậy cao trong dài hạn (tata_bank_alm, Ch.2, NII Forecast, d.1025). Trong thực tiễn điều hành ngân hàng, dự báo NII được tích hợp trong quy trình quản trị tài chính đa tầng theo [[net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]], phân định rõ giữa Dự báo (Forecast) năm hiện hành, Ngân sách (Budget) năm tới và Kế hoạch chiến lược (Plan) trung hạn. Khi lập kế hoạch biên lãi, nhà quản lý thường tránh giả định biên giảm và giữ nguyên biên hiện tại; nếu thừa nhận một hệ số margin-beta thì biên kế hoạch được điều chỉnh theo từng môi trường lãi suất (tata_bank_alm, Ch.3, Planning Horizons, d.2289–2293; tata_bank_alm, Ch.3, Margin Planning, d.2325–2333). Để đo lường độ nhạy thuần túy với lãi suất, toàn bộ các khoản mục không nhạy cảm lãi suất — bao gồm bất động sản, tài sản vô hình, vốn góp đầu tư cổ phần và vốn tự có của ngân hàng — đều được loại trừ khỏi phạm vi tính toán (tata_bank_alm, Ch.2, NII Forecast, d.1027).

Khi ALM đo độ nhạy NII, độ chính xác của con số dự báo NII cơ sở ít quan trọng hơn (tata_bank_alm, Ch.2, NII Forecast, d.1021). Độ nhạy thu nhập lãi thuần ($\Delta NII$) được xác định bằng hiệu số giữa NII trong kịch bản sốc và NII kịch bản cơ sở ($\Delta NII = NII_{shock} - NII_{baseline}$); do đó, nếu có sai số trong các giả định mô hình cơ sở, những sai số này sẽ lặp lại ở cả hai vế và tự động triệt tiêu phần lớn (*cancelled out*) trong phép trừ chênh lệch (tata_bank_alm, Ch.2, NII Forecast, d.1021). 

Điểm xuất phát của mô hình là bảng cân đối kế toán hiện hành, kết hợp chặt chẽ với [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]] để tái cấu trúc dòng vốn khi các công cụ đáo hạn, và [[interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves]] để ấn định mặt bằng lãi suất tái định giá (tata_bank_alm, Ch.1, Purpose of ALM and IRRBB, d.490). Kết quả dự báo NII baseline là nền móng để triển khai [[earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights]], phép thử NII của [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]], tức mức giảm NII so với vốn cấp 1, và để đối chiếu với [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]] (tata_bank_alm, Ch.2, Earnings Measures, d.1015).
