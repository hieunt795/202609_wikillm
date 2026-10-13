---
title: lcr-cash-inflows-count-contractual-receivables-by-counterparty-under-a-75-percent-cap
type: analysis
tags: [lcr, basel-iii, liquidity-regulation, cash-inflows]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-13
---

[[total-expected-cash-inflows|Tổng dòng vào dự kiến]] của LCR bằng tổng các khoản phải thu theo hợp đồng nhân với tỷ lệ dòng vào của từng nhóm, và phần được dùng để bù dòng ra bị chặn ở 75% tổng dòng ra dự kiến (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709):

$$\text{Dòng vào được tính} = \min\left(\sum_j \text{Khoản phải thu}_j \times \text{Tỷ lệ dòng vào}_j,\ 75\% \times \text{Tổng dòng ra dự kiến}\right)$$

Ngân hàng [[only-contractual-inflows-from-fully-performing-exposures-count-in-the-lcr|chỉ tính dòng vào theo hợp đồng từ các khoản đang được trả nợ đầy đủ]] và không tính dòng vào tiềm tàng (basel_lcr, LCR40, Cash inflows, 40.75, d.1188). [[the-75-percent-inflow-cap-forces-an-hqla-stock-of-at-least-25-percent-of-outflows|Trần 75% buộc ngân hàng giữ kho HQLA tối thiểu bằng 25% tổng dòng ra]] (basel_lcr, LCR40, Cash inflows, 40.77, d.1195). Vế dòng ra nằm ở trang [[lcr-cash-outflows-apply-run-off-and-drawdown-rates-to-four-blocks-of-liabilities-and-commitments]], và phép gộp hai vế ở trang [[lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap]].

Nhóm 1 là cho vay có bảo đảm đáo hạn trong 30 ngày, gồm repo đảo chiều và vay chứng khoán, với bảng ở trang [[secured-lending-inflow-rates-mirror-secured-funding-run-off-rates-by-collateral-level]] (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.79, d.1207–1214):

| Tài sản bảo đảm | Tỷ lệ dòng vào | Khi tài sản đã dùng lại để phủ vị thế bán khống |
|---|---|---|
| Level 1 | 0% | 0% |
| Level 2A | 15% | 0% |
| RMBS thuộc Level 2B | 25% | 0% |
| Level 2B khác | 50% | 0% |
| Cho vay ký quỹ trên tài sản ngoài HQLA | 50% | 0% |
| Tài sản khác | 100% | 0% |

Dòng cho vay ký quỹ có trang riêng, [[margin-loans-against-non-hqla-collateral-yield-at-most-a-50-percent-inflow]], và cột thứ ba ở trang [[collateral-re-used-to-cover-short-positions-earns-no-inflow-and-triggers-no-outflow]]. Giả định quay vòng không miễn nghĩa vụ ở trang [[banks-must-be-able-to-return-collateral-regardless-of-lcr-rollover-assumptions]] (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.81, d.1230).

Các nhóm còn lại tính theo đối tác hoặc theo loại khoản thu:

| Nhóm | Thành phần | Tỷ lệ dòng vào | Trang |
|---|---|---|---|
| 2. Nguồn ở tổ chức khác | Hạn mức tín dụng, thanh khoản ngân hàng có ở tổ chức khác | 0% | [[facilities-held-at-other-institutions-receive-a-zero-inflow-rate-to-limit-contagion]] |
| | Tiền gửi vận hành đặt ở tổ chức khác | 0% | [[operational-deposits-placed-at-other-institutions-receive-a-zero-inflow-rate]] |
| 3. Theo đối tác | Khách hàng bán lẻ và doanh nghiệp nhỏ | 50% | [[other-inflows-assume-continued-lending-at-50-percent-to-non-financial-counterparties]] |
| | Bán buôn phi tài chính | 50% | cùng trang |
| | Tổ chức tài chính và ngân hàng trung ương | 100% | cùng trang |
| | Khoản vay không có kỳ hạn xác định | loại, trừ khoản trả tối thiểu đến hạn trong 30 ngày | cùng trang |
| 4. Khác | Chứng khoán đáo hạn ngoài kho HQLA | 100% | [[maturing-securities-outside-the-hqla-stock-count-as-full-inflows-while-maturing-hqla-stays-in-the-stock]] |
| | Dòng vào phái sinh ròng | 100% | [[total-expected-cash-inflows]] |
| | Dòng vào theo hợp đồng khác | do từng nước quyết định; doanh thu phi tài chính không tính | [[total-expected-cash-inflows]] |

Nhóm 2 lấy từ hai đoạn (basel_lcr, LCR40, Cash inflows – Committed facilities, 40.82, d.1242; basel_lcr, LCR40, Cash inflows – other inflows by counterparty, 40.89, d.1276). Nhóm 3 phản ánh giả định rằng ngân hàng tiếp tục cho khách hàng bán lẻ và phi tài chính vay một nửa số tiền thu về (basel_lcr, LCR40, Cash inflows – other inflows by counterparty, 40.85–40.87, d.1250–1267). Nhóm 4 gồm chứng khoán đáo hạn (basel_lcr, LCR40, Cash inflows – other inflows by counterparty, 40.88, d.1269) và hai dòng cuối (basel_lcr, LCR40, Cash inflows – other cash inflows, 40.91–40.93, d.1282–1286).

Hai vế của mẫu số khớp nhau ở giao dịch có bảo đảm và lệch nhau ở hai chỗ. Bảng của nhóm 1 được chuẩn mực viết cho khớp với bảng dòng ra của tài trợ có bảo đảm (basel_lcr, LCR40, Cash inflows – secured lending, including reverse repos and securities borrowing, 40.78, d.1199). Với hạn mức giữa các ngân hàng, bên cấp giả định bị rút 40% trong khi bên nhận tính dòng vào 0% (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.64, d.1087–1094). Với quyền thay tài sản bảo đảm HQLA bằng tài sản kém hơn, [[excess-uncalled-and-substitutable-collateral-each-count-as-a-100-percent-lcr-outflow|quyền của đối tác là dòng ra 100%]], còn quyền tương tự của ngân hàng là dòng vào tiềm tàng và không được tính (basel_lcr, LCR40, Cash inflows, 40.75 FAQ1, d.1189–1191).

Các tỷ lệ của bốn nhóm khớp với phần dòng vào của bảng tóm tắt chuẩn mực (basel_lcr, LCR99, 99.1, d.1402–1419).
