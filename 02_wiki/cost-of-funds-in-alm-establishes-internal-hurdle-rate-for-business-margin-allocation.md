---
title: cost-of-funds-in-alm-establishes-internal-hurdle-rate-for-business-margin-allocation
type: concept
tags: [cost-of-funds, ftp, hurdle-rate, margin-attribution, treasury, alm]
sources: [tata_bank_alm]
status: draft
last_updated: 2026-09-28
---

Chi phí vốn (Cost of Funds — CoF) trong quản trị Tài sản – Nợ (ALM) và định giá chuyển nhượng vốn nội bộ (FTP) là mức lãi suất mà Khối Nguồn vốn trung tâm (Treasury) có thể huy động vốn trên thị trường tài chính bán buôn theo các kênh tài trợ đặc thù của ngân hàng, đóng vai trò là mức lãi suất cơ sở (internal hurdle rate) để phân định biên lợi nhuận kinh doanh thương mại và tập trung hóa rủi ro hoán đổi kỳ hạn (tata_bank_alm, Ch.2, 2.3.2 Cost of Funds, d.1601–1610). Vấn đề quản trị cốt lõi phát sinh khi quy mô và kỳ hạn của các vị thế tài sản và công nợ khách hàng không cân khớp hoàn hảo: ví dụ, khi một đơn vị kinh doanh cấp khoản tín dụng kỳ hạn 1 năm nhưng chi nhánh không có nguồn tiền gửi khách hàng đối ứng cùng kỳ hạn, Treasury phải đứng ra tài trợ khoản vay này thông qua thị trường vốn bán buôn; mức lãi suất mà Treasury ấn định cho giao dịch tài trợ này chính là chi phí vốn (d.1603–1609).

Chi phí vốn thiết lập ranh giới kinh tế khách quan để bóc tách đóng góp biên lợi nhuận của từng đơn vị tác nghiệp theo [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]]:
- *Đối với bộ phận tín dụng (Lending Area)*: Đóng góp biên lợi nhuận của khoản cho vay khách hàng được xác định bằng chênh lệch giữa lãi suất cho vay khách hàng và chi phí vốn tương ứng với kỳ hạn đó: $\text{Margin}_{\text{Lending}} = r_{\text{loan}} - \text{CoF}_{\text{tenor}}$ (tata_bank_alm, Ch.2, 2.3.2 Cost of Funds, d.1609–1610). 
- *Đối với bộ phận huy động tiền gửi (Deposit Area)*: Đóng góp biên lợi nhuận được tính bằng chênh lệch giữa chi phí vốn thị trường và lãi suất trả cho khách hàng gửi tiền: $\text{Margin}_{\text{Deposit}} = \text{CoF}_{\text{tenor}} - r_{\text{deposit}}$.

Cấu trúc kỳ hạn của chi phí vốn tuân thủ nghiêm ngặt nguyên lý định giá thị trường: nguồn vốn tài trợ kỳ hạn dài luôn đắt hơn nguồn vốn tài trợ kỳ hạn ngắn trong điều kiện đường cong lợi suất thông thường dốc lên (tata_bank_alm, Ch.2, 2.3.2 Cost of Funds, d.1611). Do đó, chi phí vốn cho một khoản cho vay khách hàng kỳ hạn 2 năm bắt buộc phải cao hơn chi phí vốn cho khoản vay 1 năm: $\text{CoF}(2Y) > \text{CoF}(1Y)$ (d.1611–1612). Việc tập hợp toàn bộ các mức chi phí vốn ứng với từng kỳ hạn hợp đồng khác nhau sẽ cấu thành Đường cong giá chuyển nhượng nội bộ (Transfer Price Curve / Cost of Funds Curve), đóng vai trò xương sống cho [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]] và bảo đảm việc định giá bán vốn nội bộ phản ánh trung thực chi phí huy động biên theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]].
