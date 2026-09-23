---
title: constant-maturity-floaters-fail-par-reset-due-to-coupon-and-discount-tenor-mismatch
type: concept
tags: [floating-rate-notes, derivatives, interest-rate-risk]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Các cấu trúc trái phiếu thả nổi kỳ hạn cố định tham chiếu lãi suất dài hạn như trái phiếu kho bạc 10 năm hoặc lãi suất hoán đổi 10 năm không thể duy trì đặc tính tự động hồi quy về mệnh giá (fixed_income_during, Ch.17, CMS and CMT Floaters, d.115–120). Sự mất cân bằng này xảy ra do kỳ hạn của lãi suất ấn định coupon mang bản chất dài hạn, trong khi hệ số chiết khấu dòng tiền áp dụng cho từng kỳ thanh toán lại thuộc kỳ hạn ngắn hạn của thị trường tiền tệ (fixed_income_during, Ch.17, CMS and CMT Floaters, d.120). Khi lãi suất dài hạn biến động, kỳ vọng coupon tương lai và hệ số chiết khấu dịch chuyển ngược chiều nhau, làm phát sinh rủi ro thời lượng phức tạp và đòi hỏi một khoản điều chỉnh độ lồi đáng kể trong định giá (fixed_income_during, Ch.17, CMS and CMT Floaters, d.120–121).

Việc phòng ngừa rủi ro cho danh mục trái phiếu tham chiếu kho bạc kỳ hạn cố định tạo ra chi phí đòn bẩy lớn nếu phải bán khống trái phiếu qua thị trường tài trợ có tài sản bảo đảm (fixed_income_during, Ch.17, CMS and CMT Floaters, d.126). Nhằm tối ưu hóa bảng cân đối kế toán, các định chế kinh doanh thường phòng hộ gián tiếp bằng các hợp đồng hoán đổi lãi suất cố định, chấp nhận chịu rủi ro cơ sở từ sự co giãn của chênh lệch hoán đổi chính phủ (fixed_income_during, Ch.17, CMS and CMT Floaters, d.126). Đặc tính cấu trúc này bổ sung danh mục phân loại chứng khoán nợ tại [[fixed-income-instruments]], đối lập trực diện với cơ chế bình ổn giá của các công cụ thả nổi ngắn hạn trong [[floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread]], đồng thời yêu cầu kỹ thuật xử lý phi tuyến tương tự như [[futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows]].
