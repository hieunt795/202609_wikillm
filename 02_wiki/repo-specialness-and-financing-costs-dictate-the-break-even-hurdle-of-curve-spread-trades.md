---
title: repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades
type: concept
tags: [yield-curve, relative-value, repo-market, special-repo, carry-costs, break-even, fixed-income-trading]
sources: [choudhry_analysing_yield_curve, fixed_income_during]
status: stable
last_updated: 2026-10-10
related: [liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest, treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves]
---

Việc tài trợ một giao dịch spread trên thị trường repo định mức hòa vốn của giao dịch đó. Nếu trái phiếu bị bán khống đang special thì việc tài trợ chịu tác động bất lợi (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4926). Choudhry không triển khai tiếp điểm này ở Ch.12 mà dẫn sang cuốn *The Global Repo Markets* của ông (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4926). Ngay cả khi lợi suất hai trái phiếu đổi cùng một mức và giao dịch không sinh lãi, vị thế vẫn chịu một khoản tài trợ (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4924).

Ví dụ của nguồn là mua 10 triệu bảng trái phiếu 10 năm và bán khống 31,47 triệu bảng trái phiếu 2 năm, tỷ lệ lấy theo BPV của hai trái phiếu (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4922), cách cân vị thế được bàn ở [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]]. Chân bán khống là chỗ special gây bất lợi: bên mượn một trái phiếu special nhận lãi suất thấp hơn lãi suất GC trên số tiền cho vay (fixed_income_during, Ch.14, The Repurchase Market, file -15, d.24), theo phân biệt ở [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]]. Thu nhập ròng của từng chân sau tài trợ repo được tính như ở [[bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing]]. Hai ý khác của cùng nguồn về lợi suất trái phiếu ngắn hạn có trang riêng: thanh khoản làm lệch lợi suất ở trang [[liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest]], và việc tách tín phiếu khỏi trái phiếu coupon ngắn khi khớp đường cong ở trang [[treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves]].
