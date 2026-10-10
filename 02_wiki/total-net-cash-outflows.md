---
title: total-net-cash-outflows
type: concept
tags: [lcr, basel-iii, liquidity-regulation]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Tổng dòng tiền ra ròng (total net cash outflows) là mẫu số của [[liquidity-coverage-ratio-lcr|LCR]]: lượng tiền ròng ngân hàng phải chi trong 30 ngày lịch tiếp theo, tính theo các tham số của kịch bản căng thẳng do chuẩn mực quy định (basel_lcr, LCR20, 20.4, d.68–70).

Chuẩn mực định nghĩa nó là [[total-expected-cash-outflows|tổng dòng ra dự kiến]] trừ [[total-expected-cash-inflows|tổng dòng vào dự kiến]] trong kịch bản, với dòng vào bị chặn ở 75% dòng ra (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709):

$$\text{Tổng dòng tiền ra ròng} = \text{Tổng dòng ra dự kiến} - \min\left(\text{Tổng dòng vào dự kiến},\ 75\% \times \text{Tổng dòng ra dự kiến}\right)$$

Ngân hàng không được tính trùng một khoản ở cả tử số và mẫu số của LCR: tài sản đã nằm trong kho HQLA thì dòng tiền vào gắn với nó không được tính làm dòng vào (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719).

Con số này là kết quả áp các tham số chuẩn của [[lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days|kịch bản gộp cú sốc riêng và cú sốc toàn thị trường]], không phải dự báo dòng tiền do ngân hàng tự lập. Chân trời tính toán cố định ở 30 ngày lịch kể từ ngày tính (basel_lcr, LCR20, 20.5, d.72). Kho [[high-quality-liquid-assets-hqla|HQLA]] ngoài thời kỳ căng thẳng ít nhất bằng con số này (basel_lcr, LCR20, 20.5, d.72).

Tổng dòng tiền ra ròng cũng được tính riêng cho từng pháp nhân trong tập đoàn. Con số của từng pháp nhân là giới hạn cho phần HQLA chịu hạn chế chuyển thanh khoản được đưa vào LCR hợp nhất, theo quy tắc ở trang [[liquidity-transfer-restrictions-exclude-trapped-surplus-hqla-from-the-consolidated-lcr]] (basel_lcr, LCR10, Treatment of liquidity transfer restrictions, 10.7, d.39). Một số tham số của mẫu số thuộc quyền quyết định của từng quốc gia. Vì vậy [[consolidated-lcr-applies-home-parameters-except-host-rules-for-retail-and-small-business-deposits|tập đoàn xuyên biên giới phải chọn tham số nước nhà hay nước sở tại]] cho từng loại dòng tiền (basel_lcr, LCR10, Differences in home / host liquidity requirements, 10.4, d.27).
