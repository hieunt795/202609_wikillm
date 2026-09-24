---
title: coupon-bias-induces-relative-yield-distortions-along-ytm-curves
type: concept
tags: [fixed-income, yield-curve, bond-pricing, taxation, reinvestment-risk]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Hiệu ứng coupon (coupon bias) là hiện tượng các trái phiếu có cùng thời gian đáo hạn và phẩm cấp tín dụng nhưng mang lãi suất coupon khác nhau lại giao dịch ở các mức lợi suất đáo hạn (YTM) chênh lệch đáng kể, tạo ra các điểm lồi lõm méo mó dọc theo đường cong lợi suất thông thường (choudhry_analysing_yield_curve, Ch.1, The Coupon Yield Curve, d.357–364).

Nguyên nhân cốt lõi khiến trái phiếu coupon cao thường giao dịch ở mức lợi suất cao hơn (rẻ hơn so với đường cong - cheap to the curve) so với trái phiếu coupon thấp cùng kỳ hạn xuất phát từ hai lực đẩy kinh tế (choudhry_analysing_yield_curve, Ch.1, d.357–363):
1. Rủi ro tái đầu tư (reinvestment risk): Trái phiếu coupon cao hoàn trả phần lớn dòng tiền về sớm hơn trong suốt vòng đời, buộc người nắm giữ phải đối mặt với nguy cơ phải tái đầu tư các khoản tiền coupon này ở mức lãi suất thị trường thấp hơn trong tương lai, trừ khi nắm giữ trái phiếu zero-coupon;
2. Cơ chế đối xử thuế bất cân xứng (tax treatment): Tại nhiều thị trường phát triển như thị trường Gilt của Vương quốc Anh, tiền coupon định kỳ bị đánh thuế thu nhập lập tức trong khi phần lãi vốn (capital gains) do mua trái phiếu coupon thấp dưới mệnh giá lại được miễn thuế hoặc hoãn thuế cho tới khi đáo hạn (choudhry_analysing_yield_curve, Ch.1, d.363).

Để loại trừ sự nhiễu loạn do hiệu ứng coupon gây ra, các nhà phân tích định lượng xây dựng các đường cong coupon riêng biệt cho từng mức coupon danh nghĩa, hoặc áp dụng kỹ thuật tách dòng tiền thành các trái phiếu zero-coupon tương đương để bóc tách cấu trúc kỳ hạn thực chất (choudhry_analysing_yield_curve, Ch.1, d.363–364, d.395–396). Hiệu ứng này chứng minh khiếm khuyết nội tại của mô hình [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]], đặt ra yêu cầu xây dựng [[par-yield-curve-derives-required-coupons-for-at-par-debt-issuance|đường cong lợi suất ngang giá]] để chuẩn hóa định giá và thúc đẩy ứng dụng [[z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves|thước đo z-spread]] nhằm triệt tiêu hoàn toàn độ méo dòng tiền trên [[yield-curve|đường cong lợi suất tổng thể]].

Tại Chương 12, Choudhry làm sâu sắc thêm cơ chế này khi chứng minh rằng ngay cả khi thời lượng (duration) của các trái phiếu được giữ cố định ở mức xấp xỉ nhau, mức coupon vẫn tạo ra sự phân kỳ lợi suất rất lớn (choudhry_analysing_yield_curve, Ch.12, d.4809–4821). Trong môi trường đường cong đảo ngược, một nghịch lý xuất hiện là nhà đầu tư có thể vừa rút ngắn thời lượng vừa thu được lợi suất cao hơn nếu chuyển đổi sang trái phiếu coupon cao. Để lượng hóa hiệu ứng này, Choudhry thiết lập mô hình chênh lệch thặng dư coupon tuyến tính $r_m - r_{mp} = c(C_{PD} - r_{mp}) + d$, phản ánh sự chênh lệch lợi suất giữa trái phiếu coupon cao và trái phiếu par như một hàm của độ lệch coupon (choudhry_analysing_yield_curve, Ch.12, d.4860–4877). Mô hình này đóng vai trò nền tảng để bóc tách chênh lệch lợi suất thặng dư cục bộ [[excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions]] và xây dựng các chiến lược giao dịch hoán đổi giá trị tương đối được cân bằng theo BPV [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]].
