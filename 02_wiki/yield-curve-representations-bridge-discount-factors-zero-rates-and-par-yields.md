---
title: yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields
type: concept
tags: [yield-curve, term-structure, quantitative-finance, valuation]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Cấu trúc kỳ hạn của lãi suất được mô tả thông qua bốn dạng thức toán học tương đương gồm đường cong hệ số chiết khấu, đường cong lãi suất zero, đường cong lãi suất kỳ hạn tức thời và đường cong lợi suất par (fixed_income_during, Ch.19, Curves and Curve Models, d.34–46). Ba dạng đầu biểu thị giá trị thời gian phi rủi ro của dòng tiền theo hàm giải tích thuần túy, trong khi đường cong par rate bị ràng buộc bởi các quy ước thực tế của thị trường trái phiếu như tần suất trả coupon, lịch ngày làm việc và quy ước đếm ngày (fixed_income_during, Ch.19, Curves and Curve Models, d.42–44; Discount factors versus par curves, d.50–60).

Lợi suất par là mức lãi suất coupon định kỳ khiến giá bẩn của trái phiếu bằng đúng 100% mệnh giá tại ngày phát hành, thường chỉ tồn tại ở các điểm nút kỳ hạn rời rạc (fixed_income_during, Ch.19, Discount factors versus par curves, d.52–60). Do các trái phiếu đang lưu hành trên thị trường thứ cấp thường giao dịch trên hoặc dưới mệnh giá, đường cong par không thể quan sát trực tiếp từ dữ liệu giao dịch đơn lẻ mà phải được ước lượng thông qua các kỹ thuật nội suy và khớp mô hình (fixed_income_during, Ch.19, Discount factors versus par curves, d.60–63). Sự chuyển đổi chuẩn mực giữa các dạng biểu diễn đường cong này giúp khắc phục khiếm khuyết của thước đo lợi suất đáo hạn trong [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]], thiết lập đầu vào giải thuật cho [[bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles]], hỗ trợ tối ưu hóa mô hình tham số tại [[parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness]], và tương thích với quy ước bóc tách dòng tiền tại [[clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement]].
