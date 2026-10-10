---
title: general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing
type: concept
tags: [repo-market, general-collateral, specials, market-microstructure]
sources: [fixed_income_during, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-10-10
reviewed: 2026-10-10
reviewed_by: model
---

Thị trường hợp đồng mua lại (repo) chia thành ba phân khúc: tài trợ tài sản chung (General Collateral - GC), tài trợ đặc biệt (Specials) và thị trường liên đại lý nối hai phân khúc kia. GC và Specials tách động cơ đặt hoặc vay tiền mặt khỏi động cơ mượn một chứng khoán cụ thể (fixed_income_during, Ch.14, The Repurchase Market, d.10–20).

Phân khúc GC là giao dịch định hướng tiền mặt (cash-driven), trong đó các bên vay và cho vay vốn giao dịch trên một rổ chứng khoán đạt chuẩn quy định rộng rãi, chẳng hạn như trái phiếu chính phủ Đức, Pháp hoặc Hà Lan kỳ hạn 1–10 năm (fixed_income_during, Ch.14, The Repurchase Market, d.12). Bên nhận tiền mặt có toàn quyền lựa chọn loại chứng khoán cụ thể trong rổ để bàn giao sau khi lãi suất repo GC đã được thống nhất (fixed_income_during, Ch.14, The Repurchase Market, d.12). Lãi suất repo GC thường thấp hơn lãi suất không bảo đảm áp cho cùng hai đối tác, phản ánh rủi ro tín dụng thấp hơn (fixed_income_during, Ch.14, The Repurchase Market, d.12).

Trái lại, phân khúc Specials là giao dịch định hướng chứng khoán (collateral-driven), nơi loại chứng khoán dùng làm tài sản thế chấp được chỉ định cụ thể ngay tại thời điểm đàm phán hợp đồng (fixed_income_during, Ch.14, The Repurchase Market, d.16). Khi nhu cầu mượn một mã trái phiếu xác định lớn (để giao cho sàn hợp đồng tương lai hoặc phục vụ tạo lập thị trường), bên cho vay tiền mặt sẵn sàng chấp nhận một mức lãi suất repo thấp hơn đáng kể so với mức GC, ví dụ "20 điểm cơ bản special", và tình trạng khan hiếm nguồn cung này có thể leo thang thành hiện tượng ép giá giao nhận tại [[futures-squeezes-and-repo-scarcity-invert-net-basis-into-negative-territory]] (fixed_income_during, Ch.14, The Repurchase Market, d.16, d.24). Phân khúc liên đại lý (interdealer) là cầu nối tìm kiếm các tài sản đang bị khóa trong các hợp đồng GC dài hạn để giải phóng sang phân khúc specials (fixed_income_during, Ch.14, The Repurchase Market, d.18).

Sự phân hóa này làm rõ cơ chế vận hành của [[repurchase-agreement|hợp đồng mua lại repo]], đồng thời chi phối việc áp dụng [[repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk|tỷ lệ khấu trừ tài sản haircut]] và hạ tầng đối trừ chi phí qua [[tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers|hệ thống repo ba bên]]. Chi phí tài trợ repo GC là lãi suất cơ sở để tính toán [[bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing|carry và định giá kỳ hạn trái phiếu]], là mỏ neo so sánh với lãi suất mua lại ngụ ý trong các chiến lược kinh doanh chênh lệch giá tại [[bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships]], trong khi hiện tượng thắt chặt nguồn vốn cuối kỳ của các ngân hàng kích hoạt [[turn-premium-reflects-year-end-balance-sheet-constraints-rather-than-policy-rate-expectations|phần bù chuyển năm turn premium]] trên lãi suất repo ngắn hạn.

Với giao dịch spread trên đường cong lợi suất, Choudhry nêu việc tài trợ giao dịch trên thị trường repo định mức hòa vốn của giao dịch (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4926). Trong ví dụ mua trái phiếu 10 năm và bán khống trái phiếu 2 năm theo tỷ lệ BPV, nếu trái phiếu bị bán khống đang special thì chi phí tài trợ chịu tác động bất lợi (choudhry_analysing_yield_curve, Ch.12, Bond Spread Weighting, d.4922–4926). Lý do là bên mượn trái phiếu special nhận lãi suất thấp hơn GC trên số tiền cho vay (fixed_income_during, Ch.14, The Repurchase Market, d.24). Mức hòa vốn này được bàn ở [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]], còn kỷ luật mục tiêu spread và cắt lỗ ở [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]].

