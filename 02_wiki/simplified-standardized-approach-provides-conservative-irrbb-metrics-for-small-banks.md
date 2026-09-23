---
title: simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks
type: concept
tags: [irrbb, eba, s-sa, snci, proportionality, rts-2022-09, eu-2024-857]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Phương pháp tiếp cận chuẩn hóa đơn giản (Simplified Standardized Approach — S-SA) là khung đo lường rủi ro lãi suất sổ ngân hàng được định nghĩa trong Quy chế Ủy quyền của Ủy ban Châu Âu (EU) 2024/857, thiết kế riêng cho các tổ chức tín dụng nhỏ và phi phức tạp (Small and Non-Complex Institutions — SNCIs) theo nguyên tắc cân xứng tỷ lệ (*proportionality principle*) (tata_bank_alm, Ch.5, 5.2 IRRBB Measures, d.2880; tata_bank_alm, Ch.5, 5.2.2 EBA Simplified Standardized Approach, d.2901). Xuất phát từ năng lực kỹ thuật và hệ thống công nghệ thông tin hạn chế hơn của các ngân hàng quy mô nhỏ, phương pháp S-SA tinh giản các thuật toán định giá phức tạp nhưng áp đặt nguyên tắc pháp lý tối thượng: kết quả đo lường rủi ro của S-SA bắt buộc phải đạt độ thận trọng tối thiểu tương đương hoặc cao hơn phương pháp chuẩn hóa đầy đủ SA (*at least as conservative as the standardized approach*) (tata_bank_alm, Ch.5, 5.2.2 EBA Simplified Standardized Approach, d.2901).

Các tinh giản kỹ thuật của phương pháp S-SA bao gồm bốn khía cạnh vận hành chính (tata_bank_alm, Ch.5, 5.2.2 EBA Simplified Standardized Approach, d.2903):
1. *Quy tắc đối với tiền gửi không kỳ hạn*: Áp dụng công thức phân bổ chuẩn hóa cố định đối với tỷ trọng tiền gửi cốt lõi (*core deposits*) và lịch biểu dòng tiền giả định, thay vì đòi hỏi các mô hình hồi quy kinh tế lượng phức tạp theo [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]];
2. *Quyền chọn tự động*: Đơn giản hóa việc tính toán tác động của sự gia tăng độ biến động (*volatility increase*) lên giá trị của các quyền chọn tự động nội bảng và ngoại bảng;
3. *Mức độ chi tiết của biên thương mại*: Cho phép gộp các nhóm sản phẩm có đặc tính tương đồng khi ước lượng biên thương mại dự phóng cho dòng tiền tái định giá, giảm bớt yêu cầu bóc tách chi tiết từng hợp đồng đơn lẻ;
4. *Tính toán dòng lãi đến ngày repricing*: Giản lược thuật toán chiết khấu và dồn tích lãi cho các khoản mục có lịch tái định giá dày đặc trong kỳ.

Mặc dù được thiết kế để giảm gánh nặng tuân thủ cho các ngân hàng địa phương và ngân hàng tiết kiệm, quyền áp dụng phương pháp S-SA không phải là đặc quyền tự động tuyệt đối (tata_bank_alm, Ch.5, Notes, d.3063). Căn cứ theo Điều 84(4) của Chỉ thị CRD IV, các cơ quan giám sát quốc gia có thẩm quyền (NCAs như BaFin tại Đức hay FMA tại Áo) có toàn quyền tước bỏ quyền sử dụng S-SA và buộc tổ chức tín dụng phải áp dụng phương pháp chuẩn hóa SA đầy đủ theo [[eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement]], nếu cơ quan quản lý nhận thấy phương pháp đơn giản hóa không đủ năng lực phản ánh thỏa đáng hồ sơ rủi ro lãi suất thực tế của ngân hàng đó (tata_bank_alm, Ch.5, Notes, d.3063). Quy định này bảo đảm các tổ chức tín dụng không thể lợi dụng tính chất giản lược của S-SA để thực hiện các hành vi trọng tài mô hình, duy trì tính nghiêm minh của bài kiểm tra an toàn theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]] và hỗ trợ quản trị bảng cân đối thích ứng theo [[bank-specific-alm-tailors-balance-sheet-governance-to-business-models-and-regional-habitats]].
