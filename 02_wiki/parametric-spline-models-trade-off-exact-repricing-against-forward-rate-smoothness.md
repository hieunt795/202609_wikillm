---
title: parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness
type: concept
tags: [yield-curve, spline-models, nelson-siegel, quantitative-finance]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Mô hình hóa đường cong lợi suất giải quyết sự đánh đổi căn bản giữa tính chuẩn xác khi tái định giá công cụ thị trường và độ mượt mà của cấu trúc kỳ hạn (fixed_income_during, Ch.19, Models, d.64–65; Parametric Curve Models, d.190–193). Các mô hình thị trường tái định giá chính xác toàn bộ tài sản đầu vào để loại trừ cơ hội chênh lệch giá lý thuyết, nhưng tạo ra các đường cong lãi suất kỳ hạn răng cưa và đòi hỏi số lượng tham số lớn (fixed_income_during, Ch.19, Models, d.64). Trái lại, các mô hình tham số chấp nhận một độ lệch nhỏ so với giá thực tế nhằm tạo ra cấu trúc đường cong trơn mượt và cô đọng số lượng biến số trạng thái (fixed_income_during, Ch.19, Models, d.64; Parametric Curve Models, d.190–193).

Mô hình Nelson-Siegel và phiên bản mở rộng Svensson phân rã lợi suất thành ba cấu phần trực quan gồm mức nền dài hạn, độ dốc ngắn hạn và điểm uốn trung hạn, trở thành công cụ phân tích ưa thích của các ngân hàng trung ương (fixed_income_during, Ch.19, The Nelson-Siegel and Nelson-Siegel-Svensson splines, d.198–213). Mặt khác, mô hình exponential spline định dạng trực tiếp trong không gian hệ số chiết khấu dưới dạng tổ hợp tuyến tính các hàm mũ suy giảm, giúp chuyển bài toán khớp giá trái phiếu thành bài toán tối ưu hóa bình phương tối thiểu tuyến tính có tốc độ tính toán vượt trội (fixed_income_during, Ch.19, The exponential spline, d.242–263). Sai số định giá từ các mô hình tham số phản ánh các cơ hội lệch giá tương đối, kết nối với chỉ báo thanh khoản gián tiếp tại [[spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias]], dựa trên các dạng thức toán học tại [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], đồng thời cung cấp nền tảng để triển khai [[composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition]] và [[dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches]].
