---
title: total-expected-cash-inflows
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-flows]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Tổng dòng vào dự kiến (total expected cash inflows) là vế bị trừ trong [[total-net-cash-outflows|tổng dòng tiền ra ròng]], tính bằng cách nhân số dư của từng nhóm khoản phải thu theo hợp đồng với tỷ lệ mà nhóm đó được giả định chảy về trong kịch bản, và bị chặn ở 75% [[total-expected-cash-outflows|tổng dòng ra dự kiến]] (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

$$\text{Dòng vào được tính} = \min\left(\sum_j \text{Số dư phải thu}_j \times \text{Tỷ lệ dòng vào}_j,\ 75\% \times \text{Tổng dòng ra dự kiến}\right)$$

Dòng vào chỉ lấy từ khoản phải thu theo hợp đồng và gồm cả tiền lãi dự kiến nhận trong 30 ngày (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709–713). Trần 75% áp cho tổng dòng vào, không áp cho từng nhóm (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

Hệ quả số học của trần này: tổng dòng tiền ra ròng không bao giờ thấp hơn 25% tổng dòng ra dự kiến. Một ngân hàng có dòng vào theo hợp đồng lớn hơn dòng ra vẫn phải giữ [[high-quality-liquid-assets-hqla|HQLA]] ít nhất bằng một phần tư dòng ra. Trần ngăn ngân hàng dựa hoàn toàn vào dòng tiền thu về, loại dòng tiền phụ thuộc việc đối tác trả đúng hạn trong căng thẳng.

Ngân hàng không được tính trùng một khoản ở hai vế của LCR. Tài sản đã nằm trong kho HQLA ở tử số thì dòng tiền vào gắn với nó không được tính làm dòng vào ở mẫu số (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). Ranh giới này có một ví dụ ở [[level-1-assets|Level 1]]: tiền gửi có kỳ hạn tại ngân hàng trung ương không đủ điều kiện làm HQLA được tính là dòng vào nếu đáo hạn trong 30 ngày (basel_lcr, LCR30, Level 1 assets, 30.41 chú thích 7, d.257).
