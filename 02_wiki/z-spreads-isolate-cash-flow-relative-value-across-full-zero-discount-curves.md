---
title: z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves
type: concept
tags: [z-spread, spline-spread, relative-value, cash-flow-discounting, curve-spreads]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Z-spread là biên độ chênh lệch lợi suất cố định được cộng thêm song song vào toàn bộ đường cong lãi suất zero nhằm làm cho giá trị hiện tại của mọi dòng tiền tương lai của một chứng khoán bằng đúng giá thị trường của nó (fixed_income_during, Ch.22, Z-Spread, d.26–30). Khi đường cong chiết khấu được xây dựng bằng phương pháp spline, thước đo này còn được gọi là spline spread (fixed_income_during, Ch.22, Z-Spread, d.30). So với chênh lệch giá đơn thuần giữa giá thị trường và giá định giá lại lý thuyết, z-spread có ưu thế vì tự động điều chỉnh theo rủi ro thời lượng của chứng khoán đang phân tích (fixed_income_during, Ch.22, Curve Spreads, d.20; Z-Spread, d.26).

Do z-spread vận hành bằng cách chiết khấu từng dòng tiền riêng biệt như một trái phiếu zero-coupon độc lập, chỉ số này trở thành công cụ định giá tương đối tự nhiên cho các cấu trúc dòng tiền phức tạp, tiêu biểu như [[capital-indexed-tips-structure-operates-as-a-synthetic-foreign-currency-investment|trái phiếu liên kết lạm phát kiểu TIPS có dòng tiền thực đa tầng]], đặc biệt khi kết hợp với [[comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves|mô hình đường cong chiết khấu thực toàn diện có hiệu chỉnh mùa vụ]] (fixed_income_during, Ch.22, Z-Spread, d.30). Tuy nhiên, rào cản tính toán của z-spread xuất phát từ việc đòi hỏi hệ thống phải bóc tách chi tiết từng dòng tiền coupon và nợ gốc trong tương lai, một thao tác mà các thư viện tính toán tài chính phổ thông thường bỏ qua khi chỉ cung cấp phép tính lợi suất tổng hợp (fixed_income_during, Ch.22, Z-Spread, d.32).

Quy ước thị trường tại châu Âu và Nhật Bản coi z-spread cao hơn là tín hiệu cho thấy chứng khoán đang được định giá rẻ hơn tương đối so với đường cong chuẩn (fixed_income_during, Ch.22, Z-Spread, d.34). Ngược lại, tại thị trường Mỹ, việc niêm yết spread hoán đổi theo quy ước par spread làm đảo ngược cách diễn giải và tạo ra sự nhầm lẫn khi các nhà cung cấp dữ liệu thương mại áp dụng quy ước Mỹ cho thị trường toàn cầu (fixed_income_during, Ch.22, Z-Spread, d.34). Bản chất định giá theo từng dòng tiền của z-spread cung cấp nền tảng lý thuyết cho việc đo lường độ phân tán phi kinh doanh chênh lệch giá trong [[spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias]], đồng thời phân định rõ ranh giới với phương pháp so sánh ngang giá trong [[par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities]].
