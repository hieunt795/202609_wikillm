---
title: liquidity-coverage-ratio-lcr
type: concept
tags: [lcr, basel-iii, liquidity-regulation]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-13
has_part: [high-quality-liquid-assets-hqla, total-net-cash-outflows, lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days]
governs: [liquidity-risk]
governed_by: [lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days, banks-may-use-hqla-and-fall-below-the-lcr-minimum-during-stress, lcr-applies-to-internationally-active-banks-on-a-consolidated-basis, lcr-is-reported-at-least-monthly-and-a-breach-is-notified-immediately]
drives: [regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]
related: [liquidity-regulation-and-central-bank-operations-arbitrage, regulatory-ratios-can-relocate-liquidity-mismatch-without-reducing-it, bank-liquidity-rules-pair-a-stressed-30-day-hqla-buffer-with-ratio-limits-on-funding-structure, the-hqla-stock-weights-three-asset-levels-by-haircut-under-40-and-15-percent-caps, lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap]
---

Tỷ lệ bao phủ thanh khoản (Liquidity Coverage Ratio, LCR) là tỷ lệ giữa kho [[high-quality-liquid-assets-hqla|tài sản thanh khoản chất lượng cao (HQLA)]] và [[total-net-cash-outflows|tổng dòng tiền ra ròng]] của ngân hàng trong 30 ngày lịch tiếp theo, cả hai đo trong một kịch bản căng thẳng (basel_lcr, LCR20, 20.4, d.68–70).

$$LCR = \frac{\text{Kho HQLA}}{\text{Tổng dòng tiền ra ròng trong 30 ngày lịch}} \ge 100\%$$

Ủy ban Basel (BCBS) xây dựng LCR để ngân hàng có đủ HQLA sống qua một kịch bản căng thẳng đáng kể kéo dài 30 ngày lịch, qua đó tăng sức chống chịu ngắn hạn trước [[liquidity-risk|rủi ro thanh khoản]] (basel_lcr, LCR20, 20.1, d.54). Tử số là giá trị kho HQLA trong điều kiện căng thẳng. Mẫu số được tính theo các tham số của [[lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days|kịch bản căng thẳng chuẩn]] do chuẩn mực quy định (basel_lcr, LCR20, 20.4, d.68–70).

LCR kế thừa phương pháp "coverage ratio" mà các ngân hàng vẫn dùng nội bộ để đo mức phơi nhiễm trước sự kiện thanh khoản bất ngờ. Ngoài thời kỳ căng thẳng tài chính, chuẩn mực yêu cầu tỷ lệ không thấp hơn 100% một cách liên tục, tức kho HQLA ít nhất bằng tổng dòng tiền ra ròng. Mức 100% không phải sàn cứng trong mọi hoàn cảnh, vì [[banks-may-use-hqla-and-fall-below-the-lcr-minimum-during-stress|ngân hàng được dùng HQLA khi căng thẳng xảy ra]] (basel_lcr, LCR20, 20.5, d.72).

Hai chương nền của chuẩn mực, LCR10 về phạm vi áp dụng và LCR20 về cách tính, có hiệu lực từ ngày 15/12/2019 (basel_lcr, LCR10, d.13–15) (basel_lcr, LCR20, d.50–52). Yêu cầu tối thiểu 100% có hiệu lực từ 1/1/2019 (basel_lcr, LCR90, 90.1, d.1327–1331). Nước đang nhận hỗ trợ tài chính cho cải cách kinh tế vĩ mô và cơ cấu được chọn lộ trình khác cho hệ thống ngân hàng của mình, khớp với chương trình tái cơ cấu kinh tế (basel_lcr, LCR90, 90.2, d.1333). Về phạm vi, [[lcr-applies-to-internationally-active-banks-on-a-consolidated-basis|LCR áp dụng cho ngân hàng hoạt động quốc tế trên cơ sở hợp nhất]]. Về tần suất, [[lcr-is-reported-at-least-monthly-and-a-breach-is-notified-immediately|ngân hàng báo cáo LCR ít nhất hằng tháng]].

Ba trang khác đọc LCR từ phía ngoài chuẩn mực. Trang [[liquidity-regulation-and-central-bank-operations-arbitrage]] ghi lại cách ngân hàng nâng LCR bằng cách vay rồi gửi lại ngân hàng trung ương mà rủi ro không đổi. Trang [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] tính chi phí giữ HQLA vào giá vốn nội bộ. Trang [[regulatory-ratios-can-relocate-liquidity-mismatch-without-reducing-it]] nêu giới hạn chung của các tỷ lệ quản lý. Toàn cảnh các quy tắc thanh khoản, từ hai vế của LCR tới giới hạn của các tỷ lệ quản lý, nằm ở trang [[bank-liquidity-rules-pair-a-stressed-30-day-hqla-buffer-with-ratio-limits-on-funding-structure]].

Bảng tóm tắt của chuẩn mực khép lại bằng hai công thức: tổng dòng tiền ra ròng bằng tổng dòng ra trừ số nhỏ hơn giữa tổng dòng vào và 75% dòng ra gộp, và LCR bằng kho HQLA chia tổng dòng tiền ra ròng (basel_lcr, LCR99, 99.1, d.1337–1341, d.1420–1421). Từng thành phần của hai vế được xếp thành bảng ở hai trang tổng quan, [[the-hqla-stock-weights-three-asset-levels-by-haircut-under-40-and-15-percent-caps|tử số]] và [[lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap|mẫu số]].
