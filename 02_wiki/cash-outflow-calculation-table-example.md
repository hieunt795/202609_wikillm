---
title: cash-outflow-calculation-table-example
type: concept
tags: [tt502026, alm, lcr, cash-outflow, calculation, template]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

Bảng tính dòng tiền ra được dùng để ghi nhận toàn bộ các nghĩa vụ thanh toán và cam kít của ngân hàng, phân loại theo thời gian đáo hạn (4 giai đoạn), áp dụng hệ số rút tiền tương ứng, rồi tổng hợp thành dòng tiền ra ròng sử dụng trong công thức LCR (sbv_circular_22_final, Phụ lục I Phần B, d.1274–1350).

**Cấu trúc bảng 9 cột:**

| (1) Mục | (2) Danh mục | (3) Ngày tiếp theo | (4) Ngày 2–7 | (5) Ngày 8–14 | (6) Ngày 15–30 | (7) Tổng | (8) Hệ số | (9) Giá trị ra |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Tiền gửi bán lẻ ổn định | 50 | 30 | 20 | 10 | 110 | 5% | 5.5 |
| 1.2 | Tiền gửi bán lẻ kém ổn định | 100 | 80 | 50 | 30 | 260 | 10% | 26 |
| 2.1 | SME ổn định | 20 | 10 | 5 | 5 | 40 | 5% | 2 |
| 2.2 | SME kém ổn định | 30 | 25 | 15 | 10 | 80 | 10% | 8 |
| 2.3 | Tiền gửi hoạt động | 0 | 0 | 10 | 0 | 10 | 25% | 2.5 |
| 2.4 | Vốn từ doanh nghiệp | 200 | 150 | 100 | 50 | 500 | 40% | 200 |
| 2.5 | Vốn khác không bảo đảm | 100 | 80 | 50 | 20 | 250 | 100% | 250 |
| 3.1 | Vốn bảo đảm HQLA cấp 1 | 300 | 200 | 150 | 100 | 750 | 0% | 0 |
| 3.2 | Vốn bảo đảm HQLA cấp 2A | 50 | 40 | 30 | 20 | 140 | 15% | 21 |
| 3.3 | Vốn bảo đảm HQLA cấp 2B khác | 30 | 20 | 15 | 10 | 75 | 50% | 37.5 |
| 4.1 | Phái sinh net | 100 | 50 | 30 | 20 | 200 | 100% | 200 |
| 5.1 | Hạn mức tín dụng cá nhân/SME | 0 | 10 | 5 | 5 | 20 | 5% | 1 |
| 5.2 | Hạn mức thanh khoản doanh nghiệp | 50 | 30 | 20 | 10 | 110 | 30% | 33 |
| 5.3 | Cam kít bảo lãnh | 20 | 10 | 5 | 0 | 35 | 5% | 1.75 |
| **Tổng dòng tiền ra** | | | | | | | | **789.25** |

**Giải thích chi tiết cột:**

**Cột (1) — Mục:** Sắp xếp theo các nhóm dòng tiền ra (tiền gửi bán lẻ, vốn bán buôn, phái sinh, cam kít), được đánh số thập phân để dễ theo dõi.

**Cột (2) — Danh mục:** Tên ghi chép rõ loại dòng tiền ra, bao gồm mức độ ổn định hoặc loại bảo đảm (nếu có).

**Cột (3–6) — Giá trị dòng tiền theo giai đoạn thời gian:** Phân chia các khoản thanh toán/cam kít theo 4 khoảng thời gian để tracking áp lực thanh khoản ở từng giai đoạn. Cột (3) = ngày tiếp theo (D+1), cột (4) = từ D+2 đến D+7, cột (5) = từ D+8 đến D+14, cột (6) = từ D+15 đến D+30.

**Cột (7) — Tổng giá trị:** (3) + (4) + (5) + (6) = tổng dư nợ/giá trị chưa điều chỉnh hệ số.

**Cột (8) — Hệ số rút tiền:** Hệ số áp dụng cho từng loại dòng tiền ra, được xác định theo từng loại khách hàng, loại bảo đảm, hoặc tính chất nghĩa vụ.

**Cột (9) — Giá trị dòng tiền ra:** Cột (7) × Cột (8) = giá trị cuối cùng tính vào LCR, sau khi đã áp dụng hệ số rút tiền.

**Ví dụ cụ thể:** Khoản vay bán buôn 500 tỷ từ doanh nghiệp, không bảo đảm, đáo hạn ngày 15–30 tiếp theo. Giá trị dòng tiền ra = 500 tỷ × 40% = 200 tỷ, ghi vào mục (6) Ngày 15–30 của vốn doanh nghiệp.

**Kiểm tra hợp lệ:** Tổng dòng tiền ra (789.25 tỷ) được đem vào công thức LCR làm mẫu số (hay tử số ròng nếu có cap 75% dòng tiền vào). Ngân hàng kiểm tra LCR = HQLA / Dòng tiền ra ròng ≥ 100%.

**Lưu ý vận hành:** Bảng này được cập nhật hàng ngày hoặc định kỳ tùy quy định nội bộ ngân hàng. Bất kỳ thay đổi về cam kít, phát sinh giao dịch phái sinh mới, hoặc khách hàng mới rút vốn đều phải được cập nhật ngay để phản ánh tỷ lệ LCR hiện tại.

[[cash-outflow-principles-30day-framework]] định nghĩa dòng tiền ra. [[lcr-hqla-definition-framework]] sử dụng bảng tính này để tính tỷ lệ LCR. [[cash-outflow-retail-deposits-stability-rates]], [[cash-outflow-wholesale-unsecured-secured]], [[cash-outflow-commitments-drawdown-rates]] chi tiết hệ số từng loại.
