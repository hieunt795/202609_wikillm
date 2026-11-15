---
title: tt83-delta-eve-excludes-cet1-deductions-fixed-assets-and-equity-and-sorts-items-into-three-standardisation-groups
type: concept
tags: [vietnam, tt83, irrbb, eve, banking-book, behavioral-modeling]
sources: [tt83_2025_sbv]
status: draft
last_updated: 2026-11-15
part_of: [tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios]
drives: [tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints]
related: [interest-rate-risk-in-the-banking-book-irrbb, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options, tt83-core-non-maturity-deposits-are-capped-at-90-70-and-50-percent-of-each-segment, tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario, tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket]
---

Bước 1 của [[tt83-delta-eve-is-the-largest-sum-of-currency-level-eve-losses-across-six-shock-scenarios|phép tính ΔEVE trong TT83]] xác định khoản mục nào nhạy cảm lãi suất trên sổ ngân hàng rồi chia chúng thành ba nhóm theo mức độ chuẩn hóa được dòng tiền (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2401–2439). Ngân hàng tự xác định danh sách khoản mục theo quy định nội bộ, trong một số ràng buộc của thông tư (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2403).

Phía tài sản loại ra ba thứ: các khoản giảm trừ khỏi vốn cấp 1 cơ sở (CET1), tài sản cố định, và các khoản đầu tư vốn chủ sở hữu trên sổ ngân hàng (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2405–2411). Phạm vi này gần với phạm vi IRRBB ở trang [[interest-rate-risk-in-the-banking-book-irrbb]], vốn cũng loại các khoản đã khấu trừ khỏi CET1 và vị thế vốn cổ phần. Phía nợ phải trả giữ lại cả tiền gửi không hưởng lãi (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2413).

Đối tượng đo là dòng tiền định giá lại giả định trong tương lai, gồm ba loại (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2415–2425). Loại thứ nhất là mọi khoản trả gốc, ví dụ tại ngày đáo hạn hợp đồng. Loại thứ hai là phần gốc được định giá lại, tính tại ngày sớm nhất mà ngân hàng hoặc đối tác có quyền đơn phương đổi lãi suất, hoặc tại ngày lãi suất thả nổi tự động đổi theo chỉ số tham chiếu. Loại thứ ba là các khoản trả lãi trên phần gốc chưa hoàn trả hoặc chưa định giá lại. Ngày của mỗi khoản trên là ngày định giá lại (repricing date) của dòng tiền đó.

Ba nhóm được xử lý khác nhau ở [[tt83-delta-eve-slots-repricing-cash-flows-into-19-time-buckets-or-their-midpoints|bước xếp dòng tiền vào thang kỳ hạn]] (tt83_2025_sbv, Phụ lục V, phần A Bước 1, d.2427–2439). Nhóm đáp ứng đủ tiêu chuẩn (amenable to standardisation) gồm khoản mục lãi suất cố định và lãi suất thả nổi; nếu khoản mục có gắn quyền chọn lãi suất thì ngân hàng bỏ qua việc thực hiện quyền chọn và đưa riêng quyền chọn đó sang nhóm thứ hai. Nhóm chưa đáp ứng đủ tiêu chuẩn (less amenable) gồm các quyền chọn lãi suất tự động. Nhóm không đáp ứng đủ tiêu chuẩn (not amenable) gồm ba loại sản phẩm mang quyền lựa chọn hành vi: [[tt83-core-non-maturity-deposits-are-capped-at-90-70-and-50-percent-of-each-segment|tiền gửi không kỳ hạn (NMD)]], [[tt83-retail-prepayment-rates-scale-by-0-8-or-1-2-under-each-shock-scenario|khoản cho vay lãi suất cố định có rủi ro trả trước hạn]], và [[tt83-retail-term-deposit-early-redemption-rates-scale-by-1-2-or-0-8-and-fall-in-the-overnight-bucket|tiền gửi có kỳ hạn có rủi ro rút trước hạn]]. Cách chia này tách hai nhánh của [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options|rủi ro quyền chọn]]: quyền chọn tự động sang nhóm thứ hai, quyền chọn hành vi sang nhóm thứ ba.
