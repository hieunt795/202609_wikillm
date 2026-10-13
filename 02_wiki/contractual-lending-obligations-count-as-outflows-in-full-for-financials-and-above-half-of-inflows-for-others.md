---
title: contractual-lending-obligations-count-as-outflows-in-full-for-financials-and-above-half-of-inflows-for-others
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-outflows, lending-commitments]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
reviewed: 2026-10-13
reviewed_by: model
part_of: [total-expected-cash-outflows]
driven_by: [total-expected-cash-inflows]
related: [committed-credit-and-liquidity-facilities, multilateral-development-bank-mdb, public-sector-entity-pse, other-inflows-assume-continued-lending-at-50-percent-to-non-financial-counterparties]
---

Ngoài các [[committed-credit-and-liquidity-facilities|hạn mức cam kết]], LCR tính riêng nghĩa vụ cấp vốn theo hợp đồng trong 30 ngày, cũng trong khối yêu cầu bổ sung của [[total-expected-cash-outflows|tổng dòng ra dự kiến]]. Mọi nghĩa vụ cho vay theo hợp đồng đối với tổ chức tài chính, kể cả ngân hàng trung ương, chưa được tính ở chỗ khác trong chuẩn mực, chịu tỷ lệ dòng ra 100% (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.65, d.1102).

Với khách hàng bán lẻ và khách hàng bán buôn phi tài chính, gồm doanh nghiệp nhỏ và vừa, doanh nghiệp khác, chính phủ, [[multilateral-development-bank-mdb|ngân hàng phát triển đa phương]] và [[public-sector-entity-pse|PSE]], quy tắc dựa trên so sánh với dòng vào. Nếu tổng nghĩa vụ cấp vốn theo hợp đồng cho các khách hàng này trong 30 ngày lịch tới, chưa tính ở các nhóm trước, vượt 50% tổng dòng vào theo hợp đồng đến hạn trong 30 ngày từ chính các khách hàng này, thì phần chênh lệch được báo cáo là dòng ra 100% (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.66, d.1104):
$$\text{Dòng ra} = \max\left(0,\ \text{Nghĩa vụ cấp vốn} - 50\% \times \text{Dòng vào theo hợp đồng}\right)$$
Công thức là cách viết lại lời văn của đoạn 40.66. Dòng vào dùng trong phép so thuộc vế [[total-expected-cash-inflows|tổng dòng vào dự kiến]]. Ở vế đó, dòng vào từ đối tác phi tài chính được tính 50% theo giả định ngân hàng tiếp tục cho vay, ở trang [[other-inflows-assume-continued-lending-at-50-percent-to-non-financial-counterparties]].
