---
title: par-yield-curve-derives-required-coupons-for-at-par-debt-issuance
type: concept
tags: [yield-curve, bond-issuance, primary-market, valuation, term-structure]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Đường cong lợi suất ngang mệnh giá (par yield curve) là đồ thị biểu diễn mức lãi suất coupon định kỳ cần thiết để một trái phiếu mới phát hành được định giá đúng bằng 100% mệnh giá tương ứng với từng kỳ hạn đáo hạn trên thị trường (choudhry_analysing_yield_curve, Ch.1, The Par Yield Curve, d.371–373).

Do các trái phiếu đang giao dịch trên thị trường thứ cấp hiếm khi có thị giá đúng bằng mệnh giá tại tất cả các điểm kỳ hạn, đường cong par không được quan sát trực tiếp mà phải được nội suy và suy diễn toán học từ hệ thống lãi suất giao ngay (spot rates) hoặc hệ số chiết khấu zero-coupon $df_n$ (choudhry_analysing_yield_curve, Ch.1, Zero-Coupon Discount Factors, d.411–420). Đối với một trái phiếu kỳ hạn $N$ năm trả coupon hàng năm với mức lợi suất par $r_m^N$, phương trình cân bằng dòng tiền quy định:
$$100 = r_m^N \sum_{n=1}^N df_n + 100 \cdot df_N$$
Từ đó, mức lợi suất par được xác định trực tiếp thông qua tỷ lệ giữa phần bù mệnh giá và giá trị niên kim của các hệ số chiết khấu:
$$r_m^N = \frac{100 \cdot (1 - df_N)}{\sum_{n=1}^N df_n}$$

Vai trò thực tiễn hàng đầu của đường cong par nằm ở thị trường sơ cấp: các tổ chức phát hành nợ và ngân hàng bảo lãnh phát hành sử dụng đường cong này để ấn định lãi suất coupon danh nghĩa chính xác cho các đợt huy động vốn mới, đáp ứng thị hiếu của các nhà đầu tư tổ chức vốn tránh mua trái phiếu phát hành trên mệnh giá (choudhry_analysing_yield_curve, Ch.1, d.371–373, d.558–563). Đường cong par là một thành phần trọng yếu trong bộ tứ biểu diễn cấu trúc kỳ hạn tại [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], đồng thời là nền tảng so sánh để nhận diện [[coupon-bias-induces-relative-yield-distortions-along-ytm-curves|độ lệch lợi suất coupon]] và xác lập thứ bậc toán học trong [[upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields]].
