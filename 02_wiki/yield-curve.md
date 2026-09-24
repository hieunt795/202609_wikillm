---
title: yield-curve
type: concept
tags: [financial-markets, interest-rates, fixed-income, term-structure]
sources: [choudhry_analysing_yield_curve, cargill_central_bank_policy, bindseil_monetary_policy]
status: stable
last_updated: 2026-09-24
---

Đường cong lợi suất (yield curve) là đồ thị biểu diễn mối quan hệ giữa lợi suất và thời gian đáo hạn của một nhóm các công cụ nợ có cùng phẩm cấp tín dụng và mức độ thanh khoản tại một thời điểm xác định (choudhry_analysing_yield_curve, Ch.1, What is the Yield Curve, d.235–240; cargill_central_bank_policy, Ch.6, d.1845–1849). Trong thực tế thị trường, đường cong lợi suất trái phiếu chính phủ đóng vai trò là đường cong chuẩn định chuẩn (benchmark) để xác lập chi phí vốn nền tảng cho toàn bộ các công cụ nợ khác (choudhry_analysing_yield_curve, Ch.1, Using the Yield Curve, d.298–301).

Đường cong lợi suất thực hiện 4 chức năng vận hành cốt lõi trong hệ thống tài chính (choudhry_analysing_yield_curve, Ch.1, Using the Yield Curve, d.298–306):
1. Định giá phát hành công cụ nợ sơ cấp và làm sàn tham chiếu cho các khoản vay thương mại;
2. Đóng vai trò phong vũ biểu phản ánh kỳ vọng của thị trường về quỹ đạo lãi suất ngắn hạn và áp lực lạm phát tương lai;
3. Cung cấp thước đo so sánh tỷ suất sinh lời trên toàn bộ phổ kỳ hạn giúp các nhà quản lý danh mục trái phiếu nhận diện định giá tương đối;
4. Làm đầu vào xác lập mức lãi suất phi rủi ro để định giá các sản phẩm phái sinh lãi suất và hợp đồng hoán đổi.

Về mặt kỹ thuật, đường cong lợi suất đáo hạn thông thường (Yield to Maturity / Gross Redemption Yield curve) thường chứa đựng sai lệch vì giả định phi thực tế rằng mọi dòng coupon đều được tái đầu tư tại mức lợi suất đáo hạn cố định [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]]. Do đó, chỉ có đường cong lợi suất zero-coupon (spot rate curve) mới cấu thành cấu trúc kỳ hạn lãi suất đích thực bởi nó loại trừ hoàn toàn rủi ro tái đầu tư (choudhry_analysing_yield_curve, Ch.1, The Zero-Coupon (or Spot) Yield Curve, d.393–396). Mối liên hệ chuyển đổi giữa các dạng thức đường cong được hoàn thiện qua [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], đồng thời chịu sự chi phối của [[coupon-bias-induces-relative-yield-distortions-along-ytm-curves|hiệu ứng coupon]] và nhu cầu xác định mức coupon phát hành ngang giá tại [[par-yield-curve-derives-required-coupons-for-at-par-debt-issuance]]. Trong khi [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates|giả thuyết kỳ vọng thuần túy]] và [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản]] tìm cách giải mã độ dốc của đồ thị, các nhà thực hành thị trường còn phải ứng phó với hiện tượng [[humped-yield-curves-reflect-peaked-interest-rate-expectations-or-maturity-habitat-imbalances|đường cong hình bướu]], áp dụng kỹ thuật [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity|nội suy cubic spline]] để làm mịn dữ liệu và giải mã nghịch lý [[collateralized-clearing-and-hedging-demand-drive-interest-rate-swaps-below-sovereign-yields|đường cong swap thấp hơn lợi suất trái phiếu chính phủ]].

