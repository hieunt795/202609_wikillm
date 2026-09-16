---
title: money-supply-equals-net-foreign-assets-plus-net-domestic-assets
type: concept
tags: [monetary-policy, identities]
sources: [imf_macro_accounting]
status: draft
last_updated: 2026-09-16
---

Vì tài sản luôn bằng nợ trên bảng cân đối, khối tiền rộng ([[money-aggregates-form-a-nested-hierarchy-from-narrow-money-to-broad-liquidity|M2]]) của toàn hệ thống ngân hàng — hợp nhất [[central-bank|nhà chức trách tiền tệ]] với [[deposit-money-banks|ngân hàng nhận tiền gửi]] thành khảo sát tiền tệ — luôn khớp đúng bằng tổng đối ứng của nó ở phía tài sản: tài sản đối ngoại ròng (NFA, quy theo nội tệ) cộng tài sản trong nước ròng (NDA):

$$M2 = NFA + NDA$$

và vì NDA lại tách thành tín dụng trong nước ròng (NDC) và khoản mục khác ròng ($OIN_b$):

$$M2 = NFA + NDC + OIN_b$$

(imf_macro_accounting, Ch.5, The Monetary Survey, d.4768–4776). Bản trình bày dạng bảng của đúng cách nhóm NFA/NDA này ở phía DMB nằm ở [[the-analytical-deposit-money-bank-balance-sheet-separates-required-from-excess-reserves]].

$M2$ cũng có thể viết trực tiếp theo loại công cụ mà công chúng nắm giữ — tiền mặt lưu thông ($CY$), tiền gửi không kỳ hạn ($DD$), [[quasi-money|tiền gửi có kỳ hạn/tiết kiệm]] ($TD$) — một cách viết khác của cùng đại lượng, không phải một đồng nhất thức độc lập:

$$M2 = CY + DD + TD$$

(imf_macro_accounting, Ch.5, cùng mục, d.4766).

Đồng nhất thức này là bản sao ở cấp toàn hệ thống ngân hàng của [[reserve-money|đồng nhất thức bảng cân đối nhà chức trách tiền tệ]] — cùng cấu trúc "tài sản đối ngoại + tài sản trong nước", chỉ khác phạm vi hợp nhất. Áp cùng phép chia cho giá trị kỳ trước như với RM, tốc độ tăng trưởng M2 cũng tách thành tổng đóng góp thô của từng khoản mục tài sản:

$$\frac{\Delta M2}{M2_{t-1}} = \frac{\Delta NFA}{M2_{t-1}} + \frac{\Delta NDCG}{M2_{t-1}} + \frac{\Delta CPS}{M2_{t-1}} + \frac{\Delta OIN_b}{M2_{t-1}}$$

rồi viết lại thành tích tốc độ tăng trưởng riêng nhân tỷ trọng trong M2:

$$\frac{\Delta M2}{M2_{t-1}} = \frac{\Delta NFA}{NFA_{t-1}}\cdot\frac{NFA_{t-1}}{M2_{t-1}} + \frac{\Delta NDCG}{NDCG_{t-1}}\cdot\frac{NDCG_{t-1}}{M2_{t-1}} + \frac{\Delta CPS}{CPS_{t-1}}\cdot\frac{CPS_{t-1}}{M2_{t-1}} + \frac{\Delta OIN_b}{OIN_{b,t-1}}\cdot\frac{OIN_{b,t-1}}{M2_{t-1}}$$

(imf_macro_accounting, Ch.5, cùng mục, d.4794, d.4798–4802 — nguồn không định nghĩa lại $NDCG$ ở đây; theo cấu trúc song song với $NCG^*$ trong đồng nhất thức RM ở [[reserve-money]], khả năng cao đây là tín dụng ròng cho chính phủ tách riêng khỏi CPS, nhưng nguồn không nói rõ — không tự khẳng định chắc chắn. Nguồn cũng không đánh số hai công thức này, chỉ ghi "algebraic manipulations similar to equations 5.1–5.4").

Trong [[the-flow-of-funds-table-decomposes-the-economy-wide-identity-into-sector-columns|bảng flow of funds]], chính đồng nhất thức này đóng vai trò cột tài trợ của khu vực ngân hàng — khu vực duy nhất có khoảng chênh phi tài chính bằng 0 theo quy ước. Với mục đích phân tích tiền tệ, thay đổi NFA cần loại trừ phần [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks|điều chỉnh định giá lại do biến động tỷ giá]] — trong thực hành, việc này được thực hiện bằng cách định giá các khoản mục ngoại tệ trên bảng cân đối theo một tỷ giá cố định và gộp phần chênh lệch định giá vào $OIN_b$, để $\Delta NFA$ chỉ còn phản ánh giao dịch thật (imf_macro_accounting, Ch.5, cùng mục, chú thích 14, d.4776).
