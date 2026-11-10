---
title: total-expected-cash-inflows
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-flows]
sources: [basel_lcr, tt50_2026_sbv]
status: draft
last_updated: 2026-11-10
---

Tổng dòng vào dự kiến (total expected cash inflows) là vế bị trừ trong [[total-net-cash-outflows|tổng dòng tiền ra ròng]], tính bằng cách nhân số dư của từng nhóm khoản phải thu theo hợp đồng với tỷ lệ mà nhóm đó được giả định chảy về trong kịch bản, và bị chặn ở 75% [[total-expected-cash-outflows|tổng dòng ra dự kiến]] (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

$$\text{Dòng vào được tính} = \min\left(\sum_j \text{Số dư phải thu}_j \times \text{Tỷ lệ dòng vào}_j,\ 75\% \times \text{Tổng dòng ra dự kiến}\right)$$

Dòng vào chỉ lấy từ khoản phải thu theo hợp đồng và gồm cả tiền lãi dự kiến nhận trong 30 ngày (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709–713). Trần 75% áp cho tổng dòng vào, không áp cho từng nhóm (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

Hệ quả số học của trần này: tổng dòng tiền ra ròng không bao giờ thấp hơn 25% tổng dòng ra dự kiến. Một ngân hàng có dòng vào theo hợp đồng lớn hơn dòng ra vẫn phải giữ [[high-quality-liquid-assets-hqla|HQLA]] ít nhất bằng một phần tư dòng ra. Trần ngăn ngân hàng dựa hoàn toàn vào dòng tiền thu về, loại dòng tiền phụ thuộc việc đối tác trả đúng hạn trong căng thẳng.

Ngân hàng không được tính trùng một khoản ở hai vế của LCR. Tài sản đã nằm trong kho HQLA ở tử số thì dòng tiền vào gắn với nó không được tính làm dòng vào ở mẫu số (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). Ranh giới này có một ví dụ ở [[level-1-assets|Level 1]]: tiền gửi có kỳ hạn tại ngân hàng trung ương không đủ điều kiện làm HQLA được tính là dòng vào nếu đáo hạn trong 30 ngày (basel_lcr, LCR30, Level 1 assets, 30.41 chú thích 7, d.257).

TT50 tính dòng vào theo cùng khung: nhân khoản phải đòi đủ điều kiện, tức nợ nhóm 1 và không vỡ nợ, với hệ số thu tiền 0%, 15%, 25%, 50% hoặc 100% (tt50_2026_sbv, Phụ lục I, Phần C, mục I khoản 1, mục IV khoản 5–6, d.1862–1866, 1925–1941). Điều kiện ghi nhận và các dòng vào bị loại nằm ở [[tt50-counts-an-inflow-only-from-performing-contractual-receivables-and-excludes-contingent-and-cancellable-inflows]]; hệ số theo đối tượng ở [[receivables-run-in-at-50-percent-from-retail-and-non-financial-customers-and-100-percent-from-financial-institutions-in-tt50]]; giao dịch có bảo đảm ở [[reverse-repo-and-secured-lending-inflows-run-in-at-0-to-100-percent-by-collateral-tier-in-tt50]]; tiền gửi hoạt động và ngân hàng đại lý ở [[operational-and-correspondent-deposits-placed-with-other-institutions-run-in-at-0-percent-except-the-excess-in-tt50]]; phái sinh ở [[net-derivative-inflows-run-in-at-100-percent-after-deducting-collateral-outflows-in-tt50]]; doanh thu phi tài chính bị loại ở [[non-financial-revenue-is-excluded-from-tt50-lcr-inflows]]; biểu mẫu ở [[the-tt50-inflow-form-has-seven-inflow-groups-in-four-time-buckets-and-restates-the-text]].
