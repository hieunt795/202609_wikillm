---
title: rfr-compounded-in-arrears-notes-require-observation-lags-and-synthetic-term-rates-to-quote-accrued-interest
type: concept
tags: [floating-rate-notes, rfr, market-infrastructure]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Việc chuyển dịch từ lãi suất kỳ hạn Libor sang các chỉ số phi rủi ro qua đêm buộc thị trường trái phiếu thả nổi phải áp dụng cơ chế tính lãi kép sau kỳ (fixed_income_during, Ch.17, Libor and OIS-Linked Notes, d.70–74). Do lãi suất qua đêm biến động hàng ngày, tổng số tiền coupon chỉ được xác định vào cuối kỳ hạn, cản trở việc tính toán lãi dồn tích trong suốt thời gian nắm giữ và có thể dẫn đến việc tính dồn lãi kép lên cả phần bù biên độ tín dụng (fixed_income_during, Ch.17, Libor and OIS-Linked Notes, d.74–76). Nhược điểm này đòi hỏi các định chế phát hành và trung tâm lưu ký chứng khoán phải cải tổ quy chuẩn tính toán dòng tiền để duy trì thanh khoản thứ cấp (fixed_income_during, Ch.17, Libor and OIS-Linked Notes, d.76–80).

Thị trường giải quyết trở ngại này bằng cách thiết lập chỉ số lãi suất trung gian tích lũy hàng ngày, giúp tính toán lãi dồn tích liên tục mà không làm méo mó biên độ yết giá cố định ban đầu (fixed_income_during, Ch.17, Libor and OIS-Linked Notes, d.76–80). Ngoài ra, các cơ quan quản lý và hiệp hội thị trường áp dụng quy ước trễ quan sát 5 ngày làm việc để bảo đảm các bên có đủ thời gian xác nhận nghĩa vụ trước khi bước vào chu kỳ thanh toán bù trừ (fixed_income_during, Ch.17, Libor and OIS-Linked Notes, d.80–85). Kỹ thuật điều chỉnh dòng tiền này liên quan trực tiếp đến độ trễ truyền dẫn lãi suất được phân tích tại [[lagged-compounded-overnight-rates-lack-term-risk-premia-and-delay-policy-transmission]], bảo đảm tính tương thích với quy trình thanh toán tại [[delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles]] trong bối cảnh tái lập chuẩn chỉ số tiền tệ tại [[overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume]].
