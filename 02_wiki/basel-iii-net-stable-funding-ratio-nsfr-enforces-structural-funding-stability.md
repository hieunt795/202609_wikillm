---
title: basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability
type: concept
tags: [banking, alm, liquidity-risk, nsfr, asf, rsf, basel-iii, funding-stability, derivatives, regulation]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-05
---

Tỷ lệ nguồn vốn ổn định ròng (Net Stable Funding Ratio - NSFR) là chuẩn mực Basel III về cấu trúc thanh khoản trung và dài hạn, yêu cầu ngân hàng duy trì cơ cấu nguồn vốn ổn định tương xứng với thành phần tài sản và hoạt động ngoại bảng (tata_bank_alm, Ch.2, 2.3.8.2 Net Stable Funding Ratio, d.1710). Tỷ lệ này so sánh nguồn vốn ổn định sẵn có (Available Stable Funding - $ASF$) với nguồn vốn ổn định yêu cầu (Required Stable Funding - $RSF$).

Khác với tỷ lệ khả năng chi trả ngắn hạn [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]] (tập trung vào bộ đệm tài sản thanh khoản cao 30 ngày), NSFR giải quyết triệt để rủi ro chênh lệch kỳ hạn cơ cấu (structural maturity mismatch), ngăn chặn tình trạng phụ thuộc quá mức vào nguồn vốn ngắn hạn bán buôn để tài trợ cho tăng trưởng tín dụng trung dài hạn.

Từ góc nhìn quản trị bảng cân đối, một số vị thế phái sinh (derivatives positions) không đòi hỏi tài trợ dòng tiền định kỳ (tự tài trợ — self-funded positions) nhưng vẫn gây suy giảm tỷ lệ NSFR; điều này buộc ngân hàng phải huy động thêm nguồn vốn dài hạn đắt đỏ hơn, và chi phí khắc phục NSFR phải được phản ánh trực tiếp vào đường cong FTP dưới dạng phạt (penalty) cho các vị thế gây suy giảm (tata_bank_alm, Ch.2, 2.3.8.2 Net Stable Funding Ratio, d.1710).

Chỉ số NSFR là động lực kỹ thuật trực tiếp định hình đường cong định giá điều chuyển vốn nội bộ (FTP) theo [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]]. Khối ALM lượng hóa chi phí tuân thủ NSFR bằng cách áp phụ phí thanh khoản kỳ hạn dài $\Delta Spread_{long}$ đối với các tài sản có hệ số $RSF$ cao (như tín dụng doanh nghiệp dài hạn, phái sinh không bảo đảm) và cấp điểm thưởng cho các nguồn huy động có hệ số $ASF$ cao theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]]. Trong mô hình tối ưu hóa bảng cân đối ALM hiện đại, chỉ số NSFR không chỉ là một báo cáo tuân thủ tĩnh hàng tháng mà được đưa vào hàm mục tiêu như một ràng buộc bất đẳng thức cơ cấu $ASF(x) - RSF(x) \ge 0$; giá trị nhân tử Lagrange (giá bóng $\lambda_{\text{NSFR}}$) phản ánh trực tiếp chi phí cơ hội biên để kéo dài kỳ hạn của nguồn tài trợ mà Treasury phải phân bổ vào biểu phí FTP (tata_bank_alm, Ch.1, Strategic Balance Sheet Management, d.579–584). Khi kết hợp cùng [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]] và [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]], NSFR tạo nên bộ khung điều hành cấu trúc thanh khoản toàn diện, bảo vệ bảng cân đối ngân hàng trước các cú sốc rút tiền hoặc đóng băng thị trường vốn. Bộ khung này đóng góp trực tiếp vào mục tiêu cân đối bền vững giữa dòng tiền, giá trị kinh tế và hạch toán nguồn vốn theo [[bank-balance-sheet-balancing-reconciles-monetary-accounting-liquidity-gaps-and-economic-value]].
