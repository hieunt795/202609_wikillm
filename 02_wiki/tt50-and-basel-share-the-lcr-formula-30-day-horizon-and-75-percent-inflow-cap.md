---
title: tt50-and-basel-share-the-lcr-formula-30-day-horizon-and-75-percent-inflow-cap
type: analysis
tags: [lcr, vietnam, tt50, basel-iii, comparison, liquidity-regulation]
sources: [tt50_2026_sbv, basel_lcr]
status: draft
last_updated: 2026-11-14
reviewed: 2026-11-14
reviewed_by: model
related: [circular-50-2026-tt-nhnn-prudential-limits-and-ratios, high-quality-liquid-assets-hqla, total-net-cash-outflows, total-expected-cash-inflows, total-expected-cash-outflows, tt50-makes-the-lcr-minimum-a-binding-threshold-with-penalties-where-basel-lets-banks-draw-down-hqla-in-stress, tt50-binds-the-solo-vnd-equivalent-lcr-while-basel-applies-a-consolidated-ratio-in-one-reporting-currency, tt50-and-basel-hqla-operational-requirements-overlap-closely-except-for-the-periodic-monetisation-test]
---

Cấu trúc tính LCR của [[circular-50-2026-tt-nhnn-prudential-limits-and-ratios|TT50]] trùng với chuẩn Basel ở bốn điểm: công thức tỷ lệ, chân trời 30 ngày, trần 75% cho dòng tiền vào và các quy tắc chống tính trùng. Phần so sánh dưới đây đối chiếu từng điểm với trang Basel tương ứng trong wiki.

Công thức tỷ lệ giống nhau. TT50 chia giá trị HQLA đủ điều kiện cho dòng tiền ra ròng 30 ngày tiếp theo kể từ ngày chốt số liệu (tt50_2026_sbv, Điều 16, khoản 1b, d.583–591). Basel chia kho [[high-quality-liquid-assets-hqla|HQLA]] cho [[total-net-cash-outflows|tổng dòng tiền ra ròng]] của 30 ngày lịch tiếp theo (basel_lcr, LCR20, 20.4, d.68–70).

Công thức mẫu số giống nhau đến mức đại số. Cả hai lấy tổng dòng ra trừ phần nhỏ hơn giữa tổng dòng vào và 75% tổng dòng ra (tt50_2026_sbv, Điều 21, khoản 2, d.703–711) (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709). Hệ quả đã ghi ở trang [[total-expected-cash-inflows]] áp dụng nguyên cho TT50: dòng ra ròng không bao giờ thấp hơn 25% dòng ra. Cả hai cùng tính tiền gốc và tiền lãi phát sinh trong 30 ngày vào dòng vào hoặc dòng ra (tt50_2026_sbv, Điều 21, khoản 3b, d.717) (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709–713).

Quy tắc chống tính trùng và chống tính thiếu cũng giống nhau. Tài sản đã nằm trong kho HQLA thì dòng tiền vào từ tài sản đó không được tính làm dòng vào (tt50_2026_sbv, Điều 21, khoản 3c, d.719) (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). Khoản mục rơi vào nhiều nhóm dòng ra thì lấy hệ số rút tiền cao nhất, trong chuẩn Basel diễn đạt là dòng ra lớn nhất theo hợp đồng của sản phẩm (tt50_2026_sbv, Điều 21, khoản 3d, d.721) (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). Cả hai chỉ tính dòng tiền có khả năng phát sinh trong 30 ngày tiếp theo (tt50_2026_sbv, Điều 21, khoản 3a, d.715).

Cách tiếp cận tham số cũng gần nhau. TT50 nhân số dư nợ phải trả và cam kết ngoại bảng với hệ số rút tiền, và số dư tài sản, cam kết ngoại bảng với hệ số thu tiền, lấy hệ số từ Phụ lục I (tt50_2026_sbv, Điều 21, khoản 2a và 2b, d.709–711). Basel nhân số dư với tỷ lệ run-off hoặc drawdown và tỷ lệ dòng vào, trong đó một số ít tham số do cơ quan giám sát quốc gia đặt ([[total-expected-cash-outflows]]). Phụ lục I đã nạp vào wiki, nhưng giá trị từng hệ số chưa được so với Basel.

Ở các điểm này TT50 và Basel khác nhau về cách dùng tỷ lệ chứ không khác về cách tính nó; phần khác biệt đó nằm ở hai trang [[tt50-makes-the-lcr-minimum-a-binding-threshold-with-penalties-where-basel-lets-banks-draw-down-hqla-in-stress]] và [[tt50-binds-the-solo-vnd-equivalent-lcr-while-basel-applies-a-consolidated-ratio-in-one-reporting-currency]]. Kho HQLA cũng được so riêng ở trang [[tt50-and-basel-hqla-operational-requirements-overlap-closely-except-for-the-periodic-monetisation-test]].
