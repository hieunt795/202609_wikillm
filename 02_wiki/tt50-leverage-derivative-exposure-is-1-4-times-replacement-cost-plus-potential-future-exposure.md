---
title: tt50-leverage-derivative-exposure-is-1-4-times-replacement-cost-plus-potential-future-exposure
type: concept
tags: [vietnam, tt50, leverage-ratio, derivatives, replacement-cost, variation-margin]
sources: [tt50_2026_sbv]
status: draft
last_updated: 2026-11-14
part_of: [tt50-leverage-exposure-measure-adds-on-balance-derivative-off-balance-and-failed-trade-exposures-with-no-collateral-offset]
analogous: [tt50-nsfr-nets-only-cash-variation-margin-that-meets-four-conditions-and-gives-other-margin-0-percent-asf, tt50-nsfr-measures-derivative-liabilities-and-assets-at-replacement-cost-and-nets-variation-margin]
related: [tt50-leverage-on-balance-exposure-includes-pledged-and-trust-assets-and-nets-only-qualifying-cash-pools]
---

Trạng thái phái sinh $E_D$ trong [[tt50-leverage-exposure-measure-adds-on-balance-derivative-off-balance-and-failed-trade-exposures-with-no-collateral-offset|tổng trạng thái rủi ro]] là tổng giá trị trạng thái của từng giao dịch phái sinh; mỗi giao dịch bằng 1,4 lần tổng chi phí thay thế (replacement cost, RC) và giá trị tương lai của trạng thái rủi ro (potential future exposure, PFE) (tt50_2026_sbv, Phụ lục III, mục II khoản 2.1, d.2240–2252):

$$E_{D} = \sum E_{Di}, \qquad E_{Di} = 1{,}4 \times (RC_{i} + PFE_{i})$$

PFE xác định theo Phụ lục II của thông tư vốn mà ngân hàng đang áp dụng (tt50_2026_sbv, Phụ lục III, mục II khoản 2.1c, d.2252). TT50 không ghi cách tính PFE và không giải thích hệ số 1,4; cách tính PFE cần ingest thêm Thông tư 41/2016/TT-NHNN hoặc Thông tư 14/2025/TT-NHNN.

Chi phí thay thế là phần dương của giá trị thị trường sau bù trừ, trừ ký quỹ biến động bằng tiền mặt nhận về và cộng ký quỹ biến động bằng tiền mặt phải trả (tt50_2026_sbv, Phụ lục III, mục II khoản 2.2, d.2254–2264):

$$RC = \max\left(V - CVM_{r} + CVM_{p},\ 0\right)$$

$V$ là giá trị thị trường của giao dịch sau khi trừ giá trị thỏa thuận bù trừ hai bên đủ điều kiện. $CVM_r$ là ký quỹ biến động bằng tiền mặt ngân hàng nhận từ đối tác, $CVM_p$ là phần ngân hàng phải trả cho đối tác; cả hai chỉ được tính khi coi như khoản thanh toán trước khi đáo hạn (pre-settlement payment). Điều kiện để coi như vậy là bốn điều kiện của Điều 25 khoản 4b (tt50_2026_sbv, Phụ lục III, mục II khoản 2.5, d.2270), tức cùng bộ điều kiện mà NSFR dùng ở [[tt50-nsfr-nets-only-cash-variation-margin-that-meets-four-conditions-and-gives-other-margin-0-percent-asf]]. Chi phí thay thế ròng khi có thỏa thuận bù trừ hai bên đủ điều kiện cũng là cơ sở tính nợ và tài sản phái sinh NSFR, xem [[tt50-nsfr-measures-derivative-liabilities-and-assets-at-replacement-cost-and-nets-variation-margin]].

Ngân hàng chỉ được bù trừ hai bên với hợp đồng không chứa điều khoản cho phép khách hàng chỉ thanh toán một phần hoặc không thanh toán cho ngân hàng (tt50_2026_sbv, Phụ lục III, mục II khoản 2.3, d.2266). Tài sản bảo đảm ngân hàng đã cung cấp cho đối tác, nếu việc cung cấp làm giảm giá trị tài sản trên Báo cáo tình hình tài chính theo chuẩn mực kế toán hiện hành, được tính lại như tài sản nội bảng (tt50_2026_sbv, Phụ lục III, mục II khoản 2.4, d.2268); cách tính tài sản nội bảng nằm ở [[tt50-leverage-on-balance-exposure-includes-pledged-and-trust-assets-and-nets-only-qualifying-cash-pools]].
