---
title: liquidity-premium
type: concept
tags: [liquidity, yield-curve, alm, term-structure, fixed-income]
sources: [choudhry_analysing_yield_curve, tata_bank_alm]
status: stable
last_updated: 2026-09-29
---

Phần bù thanh khoản (liquidity premium) là mức lợi suất thặng dư mà nhà đầu tư đòi hỏi để chấp nhận nắm giữ các công cụ tài chính có kỳ hạn dài hơn hoặc kém thanh khoản hơn trên thị trường, nhằm bù đắp cho rủi ro không thể chuyển đổi tài sản thành tiền mặt ngay lập tức mà không chịu tổn thất đáng kể về thị giá (choudhry_analysing_yield_curve, Ch.1, The Liquidity Preference Theory, d.749–755). Trong lý thuyết cấu trúc kỳ hạn, sự tồn tại của phần bù thanh khoản giải thích tại sao [[yield-curve|đường cong lợi suất]] thực tế thường có độ dốc dương ngay cả khi thị trường kỳ vọng lãi suất ngắn hạn trong tương lai không đổi, do quy mô phần bù thanh khoản có xu hướng tăng dần theo thời gian đáo hạn (choudhry_analysing_yield_curve, Ch.1, The Combined Theory, d.799–803).

Trong hoạt động quản trị tài sản nợ - có ([[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]]) và định giá chuyển vốn nội bộ ([[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]]), phần bù thanh khoản kỳ hạn ($LP$) là một cấu phần độc lập được cộng vào lãi suất phi rủi ro chuẩn để thiết lập đường cong chuyển vốn chuẩn mực theo [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]] (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1643–1658). Việc đo lường và định giá phần bù thanh khoản giúp ngân hàng phản ánh chính xác chi phí tạo thanh khoản dài hạn của Treasury vào biểu lãi suất kinh doanh, ngăn chặn các chi nhánh tín dụng khai thác quá mức nguồn vốn dài hạn mà không bù đắp thỏa đáng cho chi phí bảo đảm thanh khoản theo chuẩn mực Basel III quy định tại [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]] và [[term-liquidity-premium-matrix-calibrates-two-dimensional-floating-rate-spreads]] (choudhry_analysing_yield_curve, Ch.8, The Internal Funding Curve and FTP, d.3684).

Phần bù thanh khoản trong FTP được nhất kỳ hóa (calibrate) dựa trên mức độ cõng (tenor) và tình trạng vốn của ngân hàng; khi ngân hàng gặp tình trạng thặng dư vốn dài hạn (deposit overhang), ALCO hạ thấp phần bù thanh khoản trên đường cong FTP mua vốn để giảm sức hấp dẫn huy động và chuyển hướng dòng chảy vào cho vay, trong khi nâng cao phần bù trên đường cong bán vốn để tăng lợi nhuận cho hoạt động cho vay, tạo động lực điều hướng cơ cấu bảng cân đối ngân hàng mà không cần thay đổi chính sách tín dụng (tata_bank_alm, Ch.2, 2.3.6, d.1631–1642).
