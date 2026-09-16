---
title: valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks
type: concept
tags: [monetary-policy, exchange-rate, identities]
sources: [imf_macro_accounting]
status: stable
last_updated: 2026-09-16
---

Thay đổi tồn kho của một khoản mục bảng cân đối giữa hai kỳ không chỉ phản ánh dòng giao dịch mà còn phản ánh biến động giá thị trường hay tỷ giá dùng để định giá lại tồn kho đó; đánh đồng hai điều này dễ gây hiểu sai, nhất là khi tỷ giá biến động mạnh trong giai đoạn phân tích (imf_macro_accounting, Ch.5, Box 5.8, Valuation Adjustments, d.4841–4843).

Gọi $A_t^R$ là một khoản mục bảng cân đối tính bằng nội tệ, $A_t^S$ là cùng khoản mục đó tính bằng đô la, và $E_t$ là tỷ giá cuối kỳ (số đơn vị nội tệ trên 1 đô la) — đây chính là ký hiệu hoá tường minh của quy ước [[foreign-currency-items-in-monetary-statistics-are-converted-at-the-end-period-exchange-rate|quy đổi ngoại tệ theo tỷ giá cuối kỳ]] đã nêu ở phần nguyên tắc kế toán tiền tệ. Khi đó $A_t^R = E_t \cdot A_t^S$, nên tổng thay đổi tồn kho tính bằng nội tệ tách được thành

$$(A_t^R - A_{t-1}^R) = \underbrace{E_t^*(A_t^S - A_{t-1}^S)}_{\text{dòng giao dịch (quy theo tỷ giá bình quân kỳ } E_t^*\text{)}} + \text{thay đổi do định giá lại}$$

và phần thay đổi do định giá lại (valuation adjustment, VAd) có thể viết là

$$VAd = A_{t-1}^{S}(E_{t}-E_{t-1}) + \Delta A_{t}^{S}(E_{t}-E_{t}^{*})$$

(imf_macro_accounting, Ch.5, cùng mục, d.4844–4867). Nếu tài sản/nợ ngoại tệ trong khảo sát tiền tệ được điều chỉnh để loại trừ ảnh hưởng của biến động tỷ giá, phần điều chỉnh định giá đó cần được gộp vào "khoản mục khác ròng" ($OIN_b$ trong [[money-supply-equals-net-foreign-assets-plus-net-domestic-assets|đồng nhất thức M2]]) để bảng cân đối vẫn cân (imf_macro_accounting, Ch.5, cùng mục, d.4864–4867).

Đây là cơ chế cụ thể đứng sau yêu cầu phải loại trừ chênh lệch định giá khi so sánh $\Delta NFA$ (khảo sát tiền tệ) với $\Delta RES$ (cán cân thanh toán) ở [[change-in-net-foreign-assets-links-the-monetary-survey-to-the-balance-of-payments|liên kết khảo sát tiền tệ với cán cân thanh toán]], và là lời giải thích định lượng đầy đủ nhất trong nguồn cho phân biệt giữa đồng tiền định giá và đồng tiền nội tệ đã nêu ở [[exchange-rate|trang tỷ giá]].
