---
title: treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves
type: concept
tags: [yield-curve, curve-fitting, treasury-bills, fixed-income]
sources: [choudhry_analysing_yield_curve]
status: draft
last_updated: 2026-10-10
related: [ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets, geometric-programming-optimizes-continuous-discount-curves-under-bounded-uncertainty, liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest]
---

Ở Ch.13, Kortanek và Medvedev dẫn Fisher (2005): khi khớp đường cong lợi suất, nhóm của Fisher thấy trái phiếu coupon còn dưới một năm tới đáo hạn được định giá khác rõ so với tín phiếu, và kết luận tín phiếu với trái phiếu coupon cần hai đường cong riêng (choudhry_analysing_yield_curve, Ch.13, What to Expect When Bills Are Excluded from the Fitting Computations, d.5349). Hai tác giả coi tín phiếu vốn đã là trái phiếu zero-coupon và loại các trái phiếu coupon dưới một năm, gọi là "earlies", khỏi tập trích xuất đường cong. Trong dữ liệu Kho bạc Hoa Kỳ của họ, mỗi ngày có khoảng 306 báo giá, trong đó khoảng 33 tín phiếu và 48 earlies (choudhry_analysing_yield_curve, Ch.13, About the Bond Equivalent Yield, d.5126). Với các giao dịch spread của chương, họ yêu cầu ít nhất một công cụ thuộc [[ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets|tập Ancillary]], tập trái phiếu gần đường cong nhất theo sai số MAPE (choudhry_analysing_yield_curve, Ch.13, What to Expect When Bills Are Excluded from the Fitting Computations, d.5353). Đường cong của chương được trích xuất bằng [[geometric-programming-optimizes-continuous-discount-curves-under-bounded-uncertainty|quy hoạch hình học]]. Tác động của thanh khoản lên lợi suất tín phiếu, theo Ch.12, nằm ở trang [[liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest]].
