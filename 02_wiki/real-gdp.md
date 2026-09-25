---
title: real-gdp
type: concept
tags: [national-accounts, prices, aggregates]
sources: [imf_macro_accounting]
status: draft
last_updated: 2026-09-25
reviewed: 2026-09-25
reviewed_by: model
---

GDP thực — SNA gọi là GDP theo giá cố định — đo giá trị sản lượng của nền kinh tế bằng giá của một năm gốc cố định (imf_macro_accounting, Ch.2, Nominal and Real GDP, d.887).

Cần đại lượng này vì [[nominal-gdp|GDP danh nghĩa]] đo sản lượng theo giá của chính năm đó, nên thay đổi của nó trộn lẫn thay đổi giá với thay đổi sản lượng vật chất; chia GDP danh nghĩa cho một chỉ số giá chung là [[gdp-deflator]] thì chỉ còn lại thay đổi sản lượng:

$$GDP_{thực} = \frac{GDP_{danh nghĩa}}{deflator} \times 100$$

(imf_macro_accounting, Ch.2, cùng mục, d.884–897). Theo tốc độ,

$$(1 + v) \approx (1 + g) \times (1 + p)$$

với $v$ là tăng trưởng GDP danh nghĩa, $g$ là tăng trưởng thực và $p$ là lạm phát đo bằng deflator (imf_macro_accounting, Ch.2, cùng mục, d.905–914).

GDP thực hữu ích để đo tăng trưởng sản lượng thực. Nó không phải thước đo lý tưởng của thu nhập thực hay mức sống, nhưng vẫn là thước đo thu nhập thực được dùng rộng rãi nhất (imf_macro_accounting, Ch.2, cùng mục, d.887). Những chỗ GDP đo sai, áp dụng cả cho GDP thực, nằm ở [[measured-gdp-is-an-imperfect-gauge-of-output-and-welfare]] (imf_macro_accounting, Ch.2, Problems of GDP Measurement, d.918). Ch.2 của IMF không bàn việc so GDP thực với [[potential-gdp-measures-productive-capacity-at-full-employment|GDP tiềm năng]]; phép so đó, từ nguồn khác, cho ra [[gdp-gap-measures-deviation-of-actual-output-from-potential|khoảng cách GDP]]. Ở kinh tế chuyển đổi, cơ cấu sản xuất và tiêu dùng đổi nhanh còn chỉ số giá thiếu tin cậy, nên thường nên dựng GDP thực từ chỉ số khối lượng thay vì giảm phát GDP danh nghĩa bằng deflator (imf_macro_accounting, Ch.2, chú thích 11, d.929) — cùng gốc với vấn đề ở [[a-real-output-index-needs-prices-that-reflect-relative-scarcity]] (imf_macro_accounting, Ch.2, Special Measurement Problems in Transition Economies, d.944).
