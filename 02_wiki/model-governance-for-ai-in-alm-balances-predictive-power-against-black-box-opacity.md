---
title: model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity
type: concept
tags: [ai, alm, governance, machine-learning, regulation, supervision]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Việc tích hợp trí tuệ nhân tạo (AI) và học máy (ML) vào công tác ALM đòi hỏi một khuôn khổ quản trị mô hình (*model governance*) chặt chẽ nhằm cân bằng giữa năng lực dự báo phi tuyến tính vượt trội và yêu cầu bắt buộc về tính minh bạch, khả năng giải trình (*explainability*) và kiểm toán trước cơ quan giám sát (tata_bank_alm, Ch.6, §6.3, d.3161–3168).

Theo Hướng dẫn Giám sát IRRBB của EBA (EBA GL/2022/14), khi thẩm định và kiểm định mô hình nội bộ, các định chế tài chính bắt buộc phải tài liệu hóa đầy đủ và giải thích rõ ràng các quyết định đặc tả mô hình (*model specification choices*) như một phần không thể tách rời của quy trình kiểm định độc lập (tata_bank_alm, Ch.6, §6.3, d.3161, d.3229). Điều này tạo ra rào cản pháp lý lớn đối với các thuật toán học sâu (*deep neural networks*) vốn chịu vấn đề "hộp đen" (*black-box problem*)—nơi các liên kết phi tuyến giữa biến số đầu vào và kết quả đầu ra không thể giải mã thành các quy tắc kinh tế rõ ràng.

Để giải quyết vấn đề này, Ủy ban Ổn định Tài chính (FSB) khuyến nghị các ngân hàng có thể áp dụng chiến lược kép: hoặc mô phỏng kết quả của các mô hình AI thông qua các mô hình truyền thống có thể giải thích được, hoặc tự giới hạn ứng dụng trong các phương pháp tiếp cận AI có tính minh bạch toán học cao hơn để phục vụ thẩm định giám sát (tata_bank_alm, Ch.6, §6.3, d.3161, d.3230).

Ngoài vấn đề kiểm toán tại từng ngân hàng, sự phổ biến rộng rãi của các thuật toán AI trong ALM tiềm ẩn những rủi ro mang tính hệ thống nghiêm trọng (tata_bank_alm, Ch.6, §6.3, d.3163–3165):
- **Sự đồng nhất tập dữ liệu (*dataset uniformity*) và hành vi bầy đàn mô hình (*model herding*)**: Khi nhiều định chế tài chính cùng huấn luyện các mô hình học máy dựa trên những tập dữ liệu thị trường tương đồng hoặc vô tình sử dụng các thuật toán cốt lõi giống nhau, các ngân hàng có xu hướng đưa ra cùng một phản ứng điều hành bảng cân đối (ví dụ: đồng loạt bán tài sản dài hạn hoặc cùng đổ xô mua một loại công cụ phòng hộ), dẫn đến hiện tượng khuếch đại biến động thị trường và tạo ra sự tích tụ rủi ro hệ thống mới (Aldasoro et al. 2024; tata_bank_alm, Ch.6, §6.3, d.3163, d.3231).
- **Tính chu kỳ thuận (*procyclicality*) và liên kết mạng lưới**: Sự tự động hóa các phản ứng thanh khoản qua thuật toán có thể đẩy nhanh tốc độ lan truyền cú sốc giữa các bên tham gia thị trường mà con người khó can thiệp kịp thời (tata_bank_alm, Ch.6, §6.3, d.3163, d.3165).

Về phía cơ quan quản lý, thách thức này mở ra làn sóng ứng dụng AI trong công tác giám sát (SupTech). Các nhà giám sát ngân hàng đang phát triển các hệ thống AI đóng vai trò "trợ lý thông minh" (*copilots*)—học từ dữ liệu báo cáo giám sát lịch sử, các quyết định can thiệp trước đây và diễn biến thị trường để phát hiện sớm các ngân hàng có hành vi bất thường (*outlier banks*) hoặc nhận diện các tích tụ rủi ro hệ thống tiềm ẩn (Araujo et al. 2024; tata_bank_alm, Ch.6, §6.3, d.3167, d.3233). Đây là sự bổ sung tối cần thiết cho các phương pháp [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]] và khuôn khổ [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]], ngăn ngừa tái diễn các bài học về thiếu kiểm soát rủi ro mô hình trong [[supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb]].

Xem thêm: [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]], [[supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb]], [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]], [[holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage]].
