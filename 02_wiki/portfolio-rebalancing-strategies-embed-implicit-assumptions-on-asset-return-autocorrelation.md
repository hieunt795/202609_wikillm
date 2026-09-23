---
title: portfolio-rebalancing-strategies-embed-implicit-assumptions-on-asset-return-autocorrelation
type: concept
tags: [portfolio-rebalancing, dynamic-asset-allocation, autocorrelation, trend-following, mean-reversion]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Tái cân bằng danh mục (portfolio rebalancing) là quá trình điều chỉnh tỷ trọng nắm giữ $w_i$ theo định kỳ hoặc theo sự kiện, đóng vai trò nhân tố quyết định trực tiếp đến tổng tỷ suất sinh lời của nhà đầu tư (fixed_income_during, Ch.38, Portfolio Rebalancing, d.12–20). Một bài toán phân bổ cơ bản với hai tài sản có tỷ suất sinh lời khác nhau có thể dẫn đến vô số kết quả tích lũy tài sản sau 5 năm, tùy thuộc vào việc dòng tiền thu về được rút ra nắm giữ tiền mặt, tái phân bổ định kỳ về tỷ trọng ban đầu, hay tự động tái đầu tư vào chính tài sản phát sinh (fixed_income_during, Ch.38, Portfolio Rebalancing, d.14–18). Bản chất của việc lựa chọn một chiến lược tái cân bằng cụ thể hàm ý một giả định tiên nghiệm về cấu trúc tự tương quan (autocorrelation) của chuỗi lợi suất tài sản (fixed_income_during, Ch.38, Portfolio Rebalancing, d.20).

Bốn trường phái tái cân bằng danh mục đại diện cho các quan điểm tương phản về động học thị trường (fixed_income_during, Ch.38, Passive and Semi-Passive Strategies, d.24–74):
Chiến lược không phân bổ lại (No Reallocation / Buy and Hold) giữ nguyên tài sản và để tỷ trọng tự do trôi dạt theo giá thị trường, khiến danh mục bị phụ thuộc hoàn toàn vào thời điểm khởi tạo ban đầu và thiếu tính bất biến theo thời gian (fixed_income_during, Ch.38, No Reallocation, d.28–30).
Chiến lược tỷ trọng cố định (Constant Asset Allocation) định kỳ bán bớt các tài sản tăng giá mạnh nhất để mua thêm các tài sản sụt giảm giá trị, về bản chất áp đặt một giả định hoàn lương trung bình (mean reversion) cưỡng bức lên danh mục (fixed_income_during, Ch.38, Constant Asset Allocation, d.52).
Chiến lược theo xu hướng (Trend-Following) chủ động gia tăng tỷ trọng các tài sản sinh lời vượt trội và cắt giảm tài sản yếu kém, khai thác triệt để hiện tượng tự tương quan dương của chuỗi giá (fixed_income_during, Ch.38, Trend-Following, d.62).
Chiến lược nghịch chiều (Mean Reversion) thực hiện điều chỉnh ngược lại nhằm đón đầu sự suy thoái của đà tăng và sự phục hồi của các tài sản bị bán tháo (fixed_income_during, Ch.38, Mean Reversion, d.70).

Các mô phỏng ngẫu nhiên trên quá trình dừng Ornstein-Uhlenbeck với ba lớp tài sản chứng minh rằng không có chiến lược tái cân bằng nào vượt trội tuyệt đối (fixed_income_during, Ch.38, Numerical Examples, d.76–114). Trong môi trường tốc độ hoàn lương $\lambda$ yếu, chiến lược theo xu hướng mang lại tỷ suất sinh lời áp đảo; ngược lại, khi thị trường có lực kéo về trung bình mạnh mẽ, chiến lược nghịch chiều và tỷ trọng cố định phát huy hiệu quả tối ưu (fixed_income_during, Ch.38, Numerical Examples, d.110). Đặc biệt, khi hiệp phương sai giữa các tài sản mang giá trị âm, tác động của quyết định tái cân bằng lên hiệu suất tổng thể sẽ được khuếch đại mạnh mẽ nhất (fixed_income_during, Ch.38, Numerical Examples, d.110). Động học này bổ trợ trực tiếp cho các nguyên lý giao dịch giá trị tương đối trong [[statistical-arbitrage-in-fixed-income-forfeits-initial-trend-movements-against-fundamental-dislocations]], tương tác với kỷ luật vị thế tại [[fixed-income-trade-governance-balances-probabilistic-stop-loss-and-epistemological-consistency]] và tạo bối cảnh để phân tích các biến dạng tỷ giá trong [[multi-currency-portfolio-rebalancing-distorts-asset-allocation-under-exchange-rate-shocks]].
