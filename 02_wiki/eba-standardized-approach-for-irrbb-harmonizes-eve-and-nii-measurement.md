---
title: eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement
type: concept
tags: [irrbb, eba, standardized-approach, eve, nii, rts-2022-09, eu-2024-857]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]
has_part: [monitoring-market-value-changes-outside-nii-horizon-prevents-deferred-interest-rate-losses]
governs: [economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows, net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]
contrasts: [simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks]
related: [balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views, embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap, supervisory-irrbb-reporting-mandates-five-standardized-templates-under-eu-2024-855]
---

Phương pháp chuẩn hóa (standardized approach, SA) của EBA là phương pháp đo IRRBB cho cả giá trị kinh tế của vốn chủ sở hữu ([[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows|EVE]]) lẫn thu nhập lãi thuần ([[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations|NII]]), quy định trong tiêu chuẩn kỹ thuật RTS/2022/09 (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2883). Nguồn ghi tiêu chuẩn này được soạn theo ủy quyền của Điều 98 CRD IV (2013) (tata_bank_alm, Ch.5, 5.2 IRRBB Measures, d.2877), được thực thi bằng Quy định ủy quyền (EU) 2024/857 và có hiệu lực ngày 14/5/2024 (tata_bank_alm, Ch.5, 5.1.3 EBA, d.2869). SA được soạn với mục tiêu phản ánh rủi ro chính xác nhất trong khuôn khổ các giả định chuẩn hóa và tương xứng (tata_bank_alm, Ch.5, 5.2 IRRBB Measures, d.2879). Vị trí của tiêu chuẩn này trong hệ thống quy định nằm ở trang [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]].

Với EVE, SA tính thay đổi của giá trị kinh tế của vốn chủ sở hữu bằng EVE ở kịch bản sốc trừ EVE ở kịch bản cơ sở (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2885). Với NII, SA tính NII cho kịch bản cơ sở và cho từng kịch bản sốc lãi suất, mỗi lần là tổng của ba thành phần (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2887):
1. tổng các khoản lãi cho tới và gồm cả ngày định giá lại, tức các dòng NII đã cố định và không đổi khi lãi suất đổi (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2889);
2. lợi suất phi rủi ro dự phóng cho từng dòng tiền định giá lại, từ lúc định giá lại tới hết kỳ dự phóng, theo giả định bảng cân đối không đổi (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2890);
3. biên thương mại dự phóng cho từng dòng tiền danh nghĩa định giá lại, từ lúc biên được đặt lại (thường là ngày đáo hạn của công cụ) tới hết kỳ dự phóng, cũng theo giả định bảng cân đối không đổi (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2891). Biên thương mại của nghiệp vụ mới lấy theo biên thương mại của các công cụ phát sinh trong năm trước (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2895).

Các giả định về diễn biến bảng cân đối nằm ở trang [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]].

Cả SA cho EVE lẫn SA cho NII đều tính một phụ phí cho quyền chọn tự động (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2893). SA cũng đặt giới hạn lên giả định hành vi về thời điểm và số tiền của dòng tiền khách hàng, ví dụ với tiền gửi không kỳ hạn bán lẻ và bán buôn, trả nợ trước hạn, tỷ lệ rút tiền gửi có kỳ hạn trước hạn và cam kết cho vay (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2893). Giới hạn 5 năm với kỳ hạn định giá lại bình quân của tiền gửi không kỳ hạn thuộc hướng dẫn GL/2022/14 và nằm ở trang [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]] (tata_bank_alm, Ch.5, Notes, d.3059).

Phép tính NII không cho thấy tác động của thay đổi lãi suất nằm ngoài kỳ tính NII. Để xử lý điểm này, EBA đưa vào SA cho NII một thành phần đo thay đổi giá trị thị trường của các công cụ đó (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2897). Phép tính tương tự phép tính EVE nhưng loại các công cụ không ghi nhận theo giá thị trường, và loại các dòng tiền rơi trong kỳ tính NII để tránh tính trùng (tata_bank_alm, Ch.5, 5.2.1 EBA Standardized Approach, d.2897). Yêu cầu theo dõi này nằm ở trang [[monitoring-market-value-changes-outside-nii-horizon-prevents-deferred-interest-rate-losses]], và các mẫu báo cáo giám sát ở trang [[supervisory-irrbb-reporting-mandates-five-standardized-templates-under-eu-2024-855]]. Phương pháp dành cho tổ chức nhỏ và không phức tạp nằm ở trang [[simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks]] (tata_bank_alm, Ch.5, 5.2 IRRBB Measures, d.2879).
