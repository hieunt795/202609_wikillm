---
title: debt-dynamics-equation-links-the-stock-of-external-debt-to-disbursements-and-amortization
type: concept
tags: [external-sector, external-debt, identities]
sources: [imf_macro_accounting]
status: stable
last_updated: 2026-09-24
reviewed: 2026-09-24
reviewed_by: model
---

Tồn kho [[gross-external-debt-is-defined-by-contractual-and-disbursed-obligations|nợ nước ngoài gộp]] cuối kỳ xấp xỉ bằng tồn kho cuối kỳ trước cộng luồng tạo nợ ròng trong kỳ:

$$D_t = D_{t-1} + B_t - A_t$$

trong đó $D_t$ là tồn kho nợ đã giải ngân còn lưu hành cuối kỳ $t$, $B_t$ là giải ngân khoản vay mới trong kỳ $t$, và $A_t$ là trả gốc (amortization) trong kỳ $t$ (imf_macro_accounting, Ch.4, Debt Stocks and Debt-Creating Flows, d.3855–3867). Phương trình này dựng được vì phần lớn luồng ghi trong tài khoản vốn và tài chính của cán cân thanh toán là luồng tạo nợ, nên tồn kho nợ gộp gắn trực tiếp với các luồng đó (imf_macro_accounting, Ch.4, cùng mục, d.3855).

Đây chỉ là một xấp xỉ, không phải đẳng thức chính xác, vì ba lý do: nợ bằng nhiều đồng tiền khác nhau nên tồn kho quy đổi (ví dụ theo đô la Mỹ) còn biến động theo định giá lại khi tỷ giá giữa các đồng tiền đó thay đổi; lãi đôi khi được nhập gốc, cộng thêm nghĩa vụ lãi chưa trả (nợ lãi quá hạn) vào tồn kho; và nợ đang lưu hành đôi khi bị xóa hoặc miễn (imf_macro_accounting, Ch.4, cùng mục, d.3869). Lý do thứ nhất là cùng hiện tượng mà thống kê tiền tệ xử lý bằng [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks|tách luồng giao dịch khỏi phần định giá lại theo tỷ giá]]. Vì các sai lệch này, IMF khuyến nghị đọc luồng tạo nợ trong tài khoản vốn và tài chính cùng với tổng mức nợ nước ngoài gộp của quốc gia, không đọc riêng từng luồng (imf_macro_accounting, Ch.4, cùng mục, d.3871). Phương trình này cùng logic với [[public-debt-dynamics-depend-on-the-primary-balance-seigniorage-and-the-interest-growth-gap|phương trình động thái nợ công]] ở Ch.3, tức tồn kho kỳ này bằng tồn kho kỳ trước cộng luồng ròng, nhưng áp cho nợ đối ngoại thay vì nợ chính phủ. Nó không có số hạng tăng trưởng vì được viết theo tồn kho tuyệt đối, không theo tỷ lệ GDP. Nó cũng không có số hạng lãi, vì lãi phải trả được ghi ở tài khoản vãng lai, còn trả gốc ghi ở tài khoản vốn và tài chính (imf_macro_accounting, Ch.4, Indicators of External Debt, d.3875); lãi chỉ cộng vào tồn kho khi được nhập gốc (imf_macro_accounting, Ch.4, Debt Stocks and Debt-Creating Flows, d.3869). Theo quy ước, gánh nặng nợ được đo bằng tồn kho $D_t$ so với một chỉ số nguồn lực sẵn có như kim ngạch xuất khẩu, như ở [[indicators-of-external-debt-burden]] (imf_macro_accounting, Ch.4, Indicators of External Debt, d.3877).
