---
title: total-expected-cash-inflows
type: concept
tags: [lcr, basel-iii, liquidity-regulation, cash-flows]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-12
part_of: [total-net-cash-outflows]
has_part: [only-contractual-inflows-from-fully-performing-exposures-count-in-the-lcr, secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level, facilities-held-at-other-institutions-receive-a-zero-inflow-rate-to-limit-contagion, other-inflows-assume-continued-lending-at-50-percent-to-non-financial-counterparties, maturing-securities-outside-the-hqla-stock-count-as-full-inflows-while-maturing-hqla-stays-in-the-stock, operational-deposits-placed-at-other-institutions-receive-a-zero-inflow-rate]
governs: [high-quality-liquid-assets-hqla]
governed_by: [total-expected-cash-outflows, the-75-percent-inflow-cap-forces-an-hqla-stock-of-at-least-25-percent-of-outflows]
contrasts: [level-1-assets, other-contractual-cash-outflows-receive-a-100-percent-factor-while-operating-costs-are-excluded]
related: [net-derivative-cash-outflows-receive-a-100-percent-factor-in-the-lcr]
---

Tổng dòng vào dự kiến (total expected cash inflows) là vế bị trừ trong [[total-net-cash-outflows|tổng dòng tiền ra ròng]], tính bằng cách nhân số dư của từng nhóm khoản phải thu theo hợp đồng với tỷ lệ mà nhóm đó được giả định chảy về trong kịch bản, và bị chặn ở 75% [[total-expected-cash-outflows|tổng dòng ra dự kiến]] (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

$$\text{Dòng vào được tính} = \min\left(\sum_j \text{Số dư phải thu}_j \times \text{Tỷ lệ dòng vào}_j,\ 75\% \times \text{Tổng dòng ra dự kiến}\right)$$

Dòng vào chỉ lấy từ khoản phải thu theo hợp đồng và gồm cả tiền lãi dự kiến nhận trong 30 ngày (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709–713). Trần 75% áp cho tổng dòng vào, không áp cho từng nhóm (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709).

Hệ quả số học của trần này: tổng dòng tiền ra ròng không bao giờ thấp hơn 25% tổng dòng ra dự kiến. Một ngân hàng có dòng vào theo hợp đồng lớn hơn dòng ra vẫn phải giữ [[high-quality-liquid-assets-hqla|HQLA]] ít nhất bằng một phần tư dòng ra. Trần ngăn ngân hàng dựa hoàn toàn vào dòng tiền thu về, loại dòng tiền phụ thuộc việc đối tác trả đúng hạn trong căng thẳng.

Ngân hàng không được tính trùng một khoản ở hai vế của LCR. Tài sản đã nằm trong kho HQLA ở tử số thì dòng tiền vào gắn với nó không được tính làm dòng vào ở mẫu số (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). Ranh giới này có một ví dụ ở [[level-1-assets|Level 1]]: tiền gửi có kỳ hạn tại ngân hàng trung ương không đủ điều kiện làm HQLA được tính là dòng vào nếu đáo hạn trong 30 ngày (basel_lcr, LCR30, Level 1 assets, 30.41 chú thích 7, d.257).

Chương chia dòng vào thành các nhóm, mỗi nhóm một trang. Nguyên tắc ghi nhận nằm ở trang [[only-contractual-inflows-from-fully-performing-exposures-count-in-the-lcr]] và lý do của trần 75% ở trang [[the-75-percent-inflow-cap-forces-an-hqla-stock-of-at-least-25-percent-of-outflows]]. Cho vay có bảo đảm đáo hạn theo bảng ở trang [[secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]]; hạn mức có ở tổ chức khác chịu 0%, ở trang [[facilities-held-at-other-institutions-receive-a-zero-inflow-rate-to-limit-contagion]]; các khoản thu khác tính theo đối tác, ở trang [[other-inflows-assume-continued-lending-at-50-percent-to-non-financial-counterparties]], với hai trường hợp riêng là chứng khoán đáo hạn, ở trang [[maturing-securities-outside-the-hqla-stock-count-as-full-inflows-while-maturing-hqla-stays-in-the-stock]], và tiền gửi vận hành đặt ở tổ chức khác, ở trang [[operational-deposits-placed-at-other-institutions-receive-a-zero-inflow-rate]].

Nhóm cuối là các dòng vào khác. Tổng các dòng tiền vào ròng từ phái sinh chịu hệ số 100%, tính theo cùng phương pháp với [[net-derivative-cash-outflows-receive-a-100-percent-factor-in-the-lcr|dòng ra phái sinh]] (basel_lcr, LCR40, Cash inflows – other cash inflows, 40.91, d.1282). Khi phái sinh được bảo đảm bằng HQLA, dòng vào được tính sau khi trừ các dòng tiền hoặc tài sản bảo đảm mà ngân hàng phải nộp theo hợp đồng, vì các nghĩa vụ đó làm giảm kho HQLA (basel_lcr, LCR40, Cash inflows – other cash inflows, 40.92, d.1284). Các dòng vào theo hợp đồng khác được đưa vào theo quyền quyết định của quốc gia, với tỷ lệ do cơ quan giám sát từng nước đặt cho từng loại; dòng vào từ doanh thu phi tài chính không được tính (basel_lcr, LCR40, Cash inflows – other cash inflows, 40.93, d.1286). Phần đối ứng ở vế dòng ra chịu 100%, ở trang [[other-contractual-cash-outflows-receive-a-100-percent-factor-while-operating-costs-are-excluded]].
