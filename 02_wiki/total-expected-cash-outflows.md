---
title: total-expected-cash-outflows
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-flows]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Tổng dòng ra dự kiến (total expected cash outflows) là vế thứ nhất của [[total-net-cash-outflows|tổng dòng tiền ra ròng]], tính bằng cách nhân số dư của từng nhóm nợ phải trả và cam kết ngoại bảng với tỷ lệ mà nhóm đó được giả định bị rút (run-off) hoặc bị giải ngân (drawdown) trong 30 ngày (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

$$\text{Tổng dòng ra dự kiến} = \sum_i \text{Số dư}_i \times \text{Tỷ lệ run-off hoặc drawdown}_i$$

Mỗi nhóm $i$ là một loại nợ phải trả hoặc cam kết ngoại bảng. Các tỷ lệ là tham số của [[lcr-stress-scenario-combines-idiosyncratic-and-market-wide-shocks-over-30-days|kịch bản căng thẳng LCR]], không phải ước lượng của ngân hàng. Dòng ra gồm cả tiền lãi dự kiến phải trả trong 30 ngày (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709–713).

Phần lớn tỷ lệ run-off và drawdown được hài hoà giữa các nước. Một số ít tham số do cơ quan giám sát quốc gia quyết định; các tham số này phải minh bạch và công bố công khai (basel_lcr, LCR40, Definition of total net cash outflows, 40.2, d.715). Bảng tóm tắt hệ số cho từng nhóm nằm ở chương LCR99 (basel_lcr, LCR40, Definition of total net cash outflows, 40.3, d.717). Phần tham số quốc gia là lý do có quy tắc [[consolidated-lcr-applies-home-parameters-except-host-rules-for-retail-and-small-business-deposits|chọn tham số nước nhà hay nước sở tại]] khi hợp nhất.

Khi một khoản có thể rơi vào nhiều nhóm dòng ra, ngân hàng chỉ giả định tối đa bằng dòng ra lớn nhất theo hợp đồng của sản phẩm đó. Ví dụ của chuẩn mực là hạn mức thanh khoản cam kết cấp để phủ khoản nợ đáo hạn trong chính 30 ngày ấy (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719).

Chương LCR40 có hiệu lực từ 15/12/2019 và được bổ sung FAQ ngày 30/3/2023 (basel_lcr, LCR40, d.703–705). Theo các đề mục của chương, dòng ra chia thành bốn khối: tiền gửi bán lẻ, vốn bán buôn không có bảo đảm, tài trợ có bảo đảm và các yêu cầu bổ sung. Vế còn lại của mẫu số là [[total-expected-cash-inflows|tổng dòng vào dự kiến]].
