---
title: level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock
type: concept
tags: [lcr, basel-iii, liquidity-regulation, hqla]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-10
---

Kho [[high-quality-liquid-assets-hqla|HQLA]] nhận [[level-1-assets|Level 1]] không giới hạn, nhưng Level 2 chỉ được chiếm tối đa 40% kho và riêng [[level-2b-assets|Level 2B]] tối đa 15% kho, trong đó trần 15% nằm bên trong trần 40% (basel_lcr, LCR30, Definition of HQLA, 30.31, d.214) (basel_lcr, LCR30, Definition of HQLA, 30.33, d.218).

Tài sản được xếp cấp theo những gì ngân hàng đang giữ vào ngày đầu của giai đoạn căng thẳng, không phụ thuộc kỳ hạn còn lại (basel_lcr, LCR30, Definition of HQLA, 30.31, d.214). Hai trần được tính sau khi áp haircut và sau khi dùng [[adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days|số điều chỉnh của từng cấp]], tức số đã tháo ngược các giao dịch có bảo đảm đáo hạn trong 30 ngày (basel_lcr, LCR30, Definition of HQLA, 30.34, d.220).

Chuẩn mực quy đổi hai trần thành tỷ lệ so với các cấp khác. Level 2 điều chỉnh tối đa bằng hai phần ba Level 1 điều chỉnh, vì 40/60 = 2/3 (basel_lcr, LCR30, Definition of HQLA, 30.35, d.222). Level 2B điều chỉnh tối đa bằng 15/85 lần tổng Level 1 và [[level-2a-assets|Level 2A]] điều chỉnh. Khi trần 40% đã ràng buộc, mức tối đa của Level 2B là một phần tư Level 1 điều chỉnh (basel_lcr, LCR30, Definition of HQLA, 30.36, d.225).

Ký hiệu $L_1$, $L_{2A}$, $L_{2B}$ là giá trị sau haircut và $\hat{L}_1$, $\hat{L}_{2A}$, $\hat{L}_{2B}$ là số điều chỉnh. Hai khoản điều chỉnh trần là (basel_lcr, LCR30, Definition of HQLA, 30.39, d.231–235):

$$A_{15} = \max\left(\hat{L}_{2B} - \frac{15}{85}\left(\hat{L}_1 + \hat{L}_{2A}\right),\ \hat{L}_{2B} - \frac{15}{60}\hat{L}_1,\ 0\right)$$

$$A_{40} = \max\left(\hat{L}_{2A} + \hat{L}_{2B} - A_{15} - \frac{2}{3}\hat{L}_1,\ 0\right)$$

$$\text{Kho HQLA} = L_1 + L_{2A} + L_{2B} - A_{15} - A_{40}$$

Ba công thức trên có độ chắc khác nhau. Bản nguồn mất hẳn công thức kho HQLA ở đoạn 30.38 khi chuyển đổi, chỉ còn câu dẫn (basel_lcr, LCR30, Definition of HQLA, 30.38, d.229). Công thức $A_{15}$ trong nguồn bị hỏng ký tự. Công thức thứ ba và $A_{15}$ ở đây được dựng lại từ lời văn của 30.35, 30.36 và tên gọi "adjustment" ở 30.39; chỉ $A_{40}$ đọc được nguyên vẹn từ nguồn.

Trần 40% được tính sau khi đã cắt Level 2B theo trần 15%, vì vậy $A_{15}$ xuất hiện trong $A_{40}$ (basel_lcr, LCR30, Definition of HQLA, 30.35, d.222). Minh hoạ bằng số tự đặt, không lấy từ nguồn và bỏ qua giao dịch cần tháo ngược: với $L_1 = 60$, $L_{2A} = 50$, $L_{2B} = 0$ thì $A_{40} = 50 - 40 = 10$ và kho HQLA là 100, trong đó Level 2 chiếm đúng 40%.

Hai trần này buộc ngân hàng giữ ít nhất 60% kho bằng Level 1. Trang [[liquidity-regulation-and-central-bank-operations-arbitrage]] ghi lại cách ngân hàng tạo thêm Level 1 bằng tiền gửi tại ngân hàng trung ương.
