---
title: simultaneous-compliance-problem-constrains-fixed-rate-allocation-under-dual-sot-limits
type: concept
tags: [alm, irrbb, simultaneous-compliance, sot, eve, nii, linear-programming, optimization]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governed_by: [supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
related: [economic-value-and-earnings-perspectives-complement-each-other-in-alm, eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement]
---

Bài toán tuân thủ đồng thời (simultaneous compliance problem) là tình huống trong đó việc tuân thủ một ràng buộc, thường là ràng buộc quy định, đe dọa việc tuân thủ một ràng buộc khác (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2934). Với phép thử ở trang [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital|supervisory outlier test (SOT)]], tình huống này xảy ra khi ngân hàng muốn không là ngân hàng ngoại lệ cả về EVE lẫn về NII (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2934). Ngưỡng ngoại lệ về EVE là EVE giảm hơn 15% vốn Tier 1 trong một kịch bản sốc (tata_bank_alm, Ch.5, 5.3.1 Supervisory Outlier Test on EVE, d.2913); ngưỡng về NII là thay đổi của NII kế toán một năm so với vốn Tier 1 vượt 5% (tata_bank_alm, Ch.5, 5.3.2 Supervisory Outlier Test on NII, d.2923). Hai phép thử ứng với hai góc nhìn ở trang [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]].

Nguồn lấy trường hợp một ngân hàng tìm lượng và duration của tài sản lãi suất cố định sao cho khớp với một vị thế tiền gửi không kỳ hạn lớn mà vẫn đạt SOT, trong đó tiền gửi được mô hình hóa theo [[eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement|phương pháp chuẩn hóa của EBA]] (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2936). Hai yêu cầu xung đột nhau một phần:
1. giới hạn SOT trên EVE đặt cả chặn trên lẫn chặn dưới cho tỷ trọng tài sản lãi suất cố định, như một hàm của duration tài sản (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2938);
2. giới hạn SOT trên NII đặt một lượng tối thiểu tài sản lãi suất cố định (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2939).

Mỗi yêu cầu xác định một dải riêng các tổ hợp giữa tỷ trọng tài sản lãi suất cố định và duration của chúng, nên muốn thỏa cả hai cùng lúc thì ngân hàng phải giải một bài toán tối ưu (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2941). Hình 5.2 của nguồn phác các ràng buộc của một bài toán tối ưu tuyến tính giữa yêu cầu SOT EVE và SOT NII, với vùng vi phạm tô xám và vùng nghiệm khả thi để trắng (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2941–2945). Vùng tuân thủ có thể rất nhỏ và có thể dịch chuyển theo thời gian khi khối lượng thay đổi (tata_bank_alm, Ch.5, 5.4 The Simultaneous Compliance Problem, d.2943).
