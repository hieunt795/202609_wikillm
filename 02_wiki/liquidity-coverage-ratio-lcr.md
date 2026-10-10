---
title: liquidity-coverage-ratio-lcr
type: concept
tags: [lcr, basel-iii, liquidity-regulation]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Tỷ lệ bao phủ thanh khoản (Liquidity Coverage Ratio, LCR) là tỷ lệ giữa kho [[high-quality-liquid-assets-hqla|tài sản thanh khoản chất lượng cao (HQLA)]] và [[total-net-cash-outflows|tổng dòng tiền ra ròng]] của ngân hàng trong 30 ngày lịch tiếp theo, cả hai đo trong một kịch bản căng thẳng (basel_lcr, LCR20, 20.4, d.68–70).

$$LCR = \frac{\text{Kho HQLA}}{\text{Tổng dòng tiền ra ròng trong 30 ngày lịch}} \ge 100\%$$

Ủy ban Basel (BCBS) xây dựng LCR để ngân hàng có đủ HQLA sống qua một kịch bản căng thẳng đáng kể kéo dài 30 ngày lịch, qua đó tăng sức chống chịu ngắn hạn trước [[liquidity-risk|rủi ro thanh khoản]] (basel_lcr, LCR20, 20.1, d.54). Tử số là giá trị kho HQLA trong điều kiện căng thẳng. Mẫu số được tính theo các tham số của [[lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days|kịch bản căng thẳng chuẩn]] do chuẩn mực quy định (basel_lcr, LCR20, 20.4, d.68–70).

LCR kế thừa phương pháp "coverage ratio" mà các ngân hàng vẫn dùng nội bộ để đo mức phơi nhiễm trước sự kiện thanh khoản bất ngờ. Ngoài thời kỳ căng thẳng tài chính, chuẩn mực yêu cầu tỷ lệ không thấp hơn 100% một cách liên tục, tức kho HQLA ít nhất bằng tổng dòng tiền ra ròng. Mức 100% không phải sàn cứng trong mọi hoàn cảnh, vì [[banks-may-use-hqla-and-fall-below-the-lcr-minimum-during-stress|ngân hàng được dùng HQLA khi căng thẳng xảy ra]] (basel_lcr, LCR20, 20.5, d.72).

Hai chương nền của chuẩn mực, LCR10 về phạm vi áp dụng và LCR20 về cách tính, có hiệu lực từ ngày 15/12/2019 (basel_lcr, LCR10, d.13–15) (basel_lcr, LCR20, d.50–52). Về phạm vi, [[lcr-applies-to-internationally-active-banks-on-a-consolidated-basis|LCR áp dụng cho ngân hàng hoạt động quốc tế trên cơ sở hợp nhất]]. Về tần suất, [[lcr-is-reported-at-least-monthly-and-a-breach-is-notified-immediately|ngân hàng báo cáo LCR ít nhất hằng tháng]].

Ba trang khác đọc LCR từ phía ngoài chuẩn mực. Trang [[liquidity-regulation-and-central-bank-operations-arbitrage]] ghi lại cách ngân hàng nâng LCR bằng cách vay rồi gửi lại ngân hàng trung ương mà rủi ro không đổi. Trang [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] tính chi phí giữ HQLA vào giá vốn nội bộ. Trang [[regulatory-ratios-can-relocate-liquidity-mismatch-without-reducing-it]] nêu giới hạn chung của các tỷ lệ quản lý.
