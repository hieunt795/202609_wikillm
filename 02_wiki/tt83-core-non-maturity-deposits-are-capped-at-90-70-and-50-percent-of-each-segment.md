---
title: tt83-core-non-maturity-deposits-are-capped-at-90-70-and-50-percent-of-each-segment
type: concept
tags: [vietnam, tt83, irrbb, non-maturity-deposits, core-deposits, behavioral-modeling]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
contrasts: [embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]
related: [non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles, tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups]
---

Trong phép tính ΔEVE của TT83, phần tiền gửi không kỳ hạn (non-maturity deposits, NMD) được coi là lõi, tức được xếp ra ngoài thang qua đêm, bị chặn ở 90%, 70% và 50% của từng phân khúc, với kỳ hạn trung bình tối đa lần lượt 5 năm, 4,5 năm và 4 năm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, Bảng 2, d.2501–2515). NMD thuộc nhóm không đáp ứng đủ tiêu chuẩn ở [[tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups|bước 1]], cùng hai loại sản phẩm mang quyền lựa chọn hành vi khác.

Ngân hàng chia NMD làm ba phân khúc (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2493–2497). Tiền gửi cá nhân được ghi vào tài khoản giao dịch khi tài khoản đó có giao dịch thường xuyên, ví dụ nhận lương định kỳ trên tài khoản thanh toán; tiền gửi cá nhân còn lại thuộc tài khoản không giao dịch. Tiền gửi của tổ chức là phân khúc thứ ba.

Trong mỗi phân khúc, ngân hàng dùng dữ liệu lịch sử tách NMD ổn định, tức phần khách hàng có khả năng cao sẽ giữ lại, khỏi NMD không ổn định (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2499). Từ phần ổn định, ngân hàng xác định NMD lõi: phần gần như không được định giá lại kể cả khi lãi suất đổi đáng kể (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2501). Tỷ trọng và kỳ hạn trung bình của NMD lõi bị chặn như sau (tt83_2025_sbv, Phụ lục V, phần A Bước 2, Bảng 2, d.2507–2513):

| Phân khúc | Trần tỷ trọng NMD lõi | Trần kỳ hạn trung bình NMD lõi |
|---|---|---|
| Cá nhân, tài khoản giao dịch | 90% | 5 năm |
| Cá nhân, tài khoản không giao dịch | 70% | 4,5 năm |
| Tổ chức | 50% | 4 năm |

NMD lõi được xếp vào các [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|thang kỳ hạn]] miễn là thỏa hai trần trên; toàn bộ NMD không lõi, gồm cả phần không ổn định, nằm ở thang qua đêm (tt83_2025_sbv, Phụ lục V, phần A Bước 2, d.2517–2523). Thông tư không quy định dạng phân bổ trong phạm vi trần, nên cách rải NMD lõi theo kỳ hạn thuộc mô hình nội bộ, ví dụ các [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles|hồ sơ lãi suất tách khỏi hồ sơ thanh khoản]] của sản phẩm không kỳ hạn. Ở EU, [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap|EBA chặn kỳ định giá lại bình quân của NMD ở 5 năm]]; TT83 chặn theo từng phân khúc và thêm trần tỷ trọng.
