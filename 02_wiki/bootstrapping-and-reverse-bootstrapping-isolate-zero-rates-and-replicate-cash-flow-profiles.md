---
title: bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles
type: concept
tags: [yield-curve, bootstrapping, fixed-income, quantitative-methods]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Phương pháp bootstrapping là giải thuật đệ quy chuẩn mực dùng để bóc tách hệ số chiết khấu và lãi suất zero từ các công cụ trả lãi định kỳ cách đều nhau như hợp đồng hoán đổi lãi suất hoặc trái phiếu chính phủ (fixed_income_during, Ch.19, Bootstrapping, d.100–124). Quá trình tính toán khởi đầu từ công cụ kỳ hạn ngắn nhất có tính chất tương đương chứng khoán chiết khấu thuần túy, sau đó sử dụng các hệ số chiết khấu đã biết để chiết khấu dòng tiền coupon trung gian của các kỳ hạn tiếp theo, giải ra hệ số chiết khấu tại mốc đáo hạn mới (fixed_income_during, Ch.19, Bootstrapping, d.125–149).

Trái lại, kỹ thuật reverse bootstrapping tiến hành giải ngược từ kỳ hạn dài nhất về kỳ hạn ngắn nhất để phân rã một nghĩa vụ dòng tiền nợ bất kỳ thành danh mục các hợp đồng par tương đương (fixed_income_during, Ch.19, Reverse bootstrapping, d.153–189). Khác với các công thức niên kim truyền thống sử dụng một mức lãi suất phẳng cố định, reverse bootstrapping chiết khấu từng khoản thanh toán theo đúng hệ số chiết khấu thị trường, cho phép các định chế tài chính thiết lập danh mục tài sản tự cân đối dòng tiền hoàn hảo (fixed_income_during, Ch.19, Reverse bootstrapping, d.188–189). Hai thuật toán đối ngẫu này dựa trên nền tảng chuyển hóa của các dạng thức đường cong tại [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], cung cấp công cụ sao chép dòng tiền cho các nghĩa vụ an sinh xã hội tại [[statutory-welfare-entitlements-function-as-virtual-fixed-income-claims-on-taxpayers]], đồng thời tương tác với kỹ thuật tối ưu hóa đường cong tại [[dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches]].
