---
title: interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves
type: concept
tags: [alm, irrbb, yield-curve, forward-rates, nii, forecasting]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
drives: [net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations, receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk]
related: [balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views, earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights]
---

Khi các vị thế tài sản hoặc nợ đến hạn và được tái tạo theo quy tắc của [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]], bộ phận ALM phải đặt giả định rõ ràng về mặt bằng lãi suất tương lai để tính toán [[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]] (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1045). Trong thực tiễn mô hình hóa ngân hàng, có hai trường phái lý thuyết và thực nghiệm đối lập nhau trong việc dự phóng đường cong lãi suất (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1047–1049).

Trường phái thứ nhất sử dụng lãi suất kỳ hạn (Forward Rates) làm thước đo dự báo tốt nhất cho lãi suất tương lai, bắt nguồn từ lý thuyết kỳ vọng (*expectation theory*) vốn giả định lãi suất dài hạn là kỳ vọng trung bình của các mức lãi suất ngắn hạn trong tương lai (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1047). Lãi suất kỳ hạn có thể tính từ đường cong giao ngay (*spot yield curve*) hoặc quan sát trực tiếp trên thị trường phái sinh thông qua hợp đồng kỳ hạn lãi suất (FRA) hay hợp đồng tương lai (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1047). Một ưu điểm thêm là lãi suất kỳ hạn cũng chính là mức lãi suất phòng hộ được trên thị trường (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1047).

Trường phái thứ hai — thường được các chuyên gia thực hành ALM ưa chuộng — xem môi trường lãi suất giao ngay hiện tại (*unchanged yield curve / current market levels*) là điểm tựa dự báo thực tế nhất (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1049). Lãi suất kỳ hạn trên thị trường không phải là ước lượng phi thiên lệch (*unbiased predictors*) bởi chúng luôn hàm chứa phần bù rủi ro thanh khoản (*liquidity risk premium*), tạo ra độ lệch có xu hướng thổi phồng lãi suất tương lai cao hơn thực tế (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1049). Hàng loạt nghiên cứu thực nghiệm học thuật đã kiểm định và bác bỏ năng lực dự báo của đường cong forward rates, và trường phái này hiểu một thế giới không đổi là lãi suất giữ ở mức thị trường hiện tại (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1049).

Theo Tata, mô hình ALM tính NII không dựa trên mô hình đường cong lợi suất quá phức tạp, vì khi đó độ nhạy NII tính được chủ yếu phản ánh giả định của mô hình (tata_bank_alm, Ch.2, Assumptions About Future Interest Rates, d.1051). Giả định lãi suất giữ nguyên là lý do hoán đổi nhận lãi cố định trông có lợi ở mọi kỳ trong ví dụ của trang [[receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk]] (tata_bank_alm, Ch.2, Caveats, d.1513). Phép đo độ nhạy NII một năm nằm ở trang [[earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights]].
