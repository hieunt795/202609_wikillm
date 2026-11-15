---
title: tt83-shock-sizes-come-from-a-currency-table-or-a-16-year-average-rate-scaled-by-60-85-and-40-percent
type: concept
tags: [vietnam, tt83, irrbb, interest-rate-shocks, calibration]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
drives: [tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay]
part_of: [circular-83-2025-tt-nhnn-internal-control-systems-of-banks]
---

[[circular-83-2025-tt-nhnn-internal-control-systems-of-banks|TT83]] cho ngân hàng ba cách lấy độ lớn cú sốc gốc $\bar{R}_{\text{loại sốc},c}$ của mỗi đồng tiền $c$: dùng bảng tham số có sẵn cho 21 đồng tiền, tự tính từ lãi suất bình quân 16 năm nhân hệ số 60%, 85% hoặc 40%, hoặc tự xác định theo hướng dẫn hiệu chỉnh cú sốc của Ủy ban Basel (tt83_2025_sbv, Phụ lục V, phần C, d.2673–2760). Mỗi đồng tiền có ba tham số: song song, ngắn hạn và dài hạn, đơn vị điểm cơ bản (bp); ba tham số này là đầu vào của [[tt83-six-shock-scenarios-combine-parallel-short-and-long-shocks-with-a-4-year-exponential-decay|công thức sáu kịch bản sốc]].

Bảng có sẵn (tt83_2025_sbv, Phụ lục V, phần C mục I, Bảng 5, d.2677–2699):

| Đồng tiền | Song song | Ngắn hạn | Dài hạn |
|---|---|---|---|
| ARS, BRL, INR, MXN, RUB, TRY, ZAR | 400 | 500 | 300 |
| IDR | 400 | 500 | 350 |
| AUD | 300 | 450 | 200 |
| KRW | 300 | 400 | 200 |
| CNY, GBP | 250 | 300 | 150 |
| CAD, SAR, SEK, USD | 200 | 300 | 150 |
| EUR, HKD | 200 | 250 | 100 |
| SGD | 150 | 200 | 100 |
| CHF | 100 | 150 | 100 |
| JPY | 100 | 100 | 100 |

Bảng không có VND. Với đồng tiền không có trong bảng, hoặc khi ngân hàng không muốn dùng bảng, ngân hàng tự tính tham số theo hai bước (tt83_2025_sbv, Phụ lục V, phần C mục I, d.2701–2732). Bước đầu thu thập lãi suất hằng ngày của đồng tiền trong 16 năm, hoặc khoảng thời gian khác do ngân hàng chọn, ở chín kỳ hạn 3 tháng, 6 tháng, 1, 2, 5, 7, 10, 15 và 20 năm, rồi lấy bình quân của toàn bộ các quan sát đó. Bước sau nhân lãi suất bình quân với tham số cú sốc toàn cầu cơ sở $\bar{\alpha}$: 60% cho cú sốc song song, 85% cho ngắn hạn, 40% cho dài hạn. Kết quả bị chặn dưới ở 100 bp và chặn trên ở 400 bp cho song song, 500 bp cho ngắn hạn, 300 bp cho dài hạn. Ví dụ tính theo quy tắc này: một đồng tiền có lãi suất bình quân 6% cho tham số song song 360 bp, ngắn hạn 510 bp nhưng bị chặn còn 500 bp, dài hạn 240 bp.

Cách thứ ba áp dụng khi ngân hàng không làm theo mục I phần C: ngân hàng tự xác định cú sốc cho các kịch bản, miễn phù hợp với hướng dẫn cập nhật của Ủy ban Basel về phương pháp xác định cú sốc (tt83_2025_sbv, Phụ lục V, phần C mục II, d.2758). Chú thích của thông tư ghi văn bản đó là BCBS d578, bản hiệu chỉnh cú sốc lãi suất trên sổ ngân hàng năm 2024 (tt83_2025_sbv, Phụ lục V, chú thích 1, d.2760).
