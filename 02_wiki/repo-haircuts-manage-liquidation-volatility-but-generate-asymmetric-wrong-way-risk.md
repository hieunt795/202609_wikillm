---
title: repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk
type: concept
tags: [repo-market, haircut, risk-management, central-bank-operations]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Tỷ lệ khấu trừ tài sản bảo đảm (haircut) trong giao dịch repo là tỷ lệ phần trăm bị khấu trừ khỏi giá trị thị trường của chứng khoán nhằm bảo vệ bên cho vay tiền mặt trước rủi ro sụt giảm giá trị tài sản trong thời gian xử lý thanh lý khi đối tác vỡ nợ (fixed_income_during, Ch.14, Haircut, d.30). Mức haircut biến thiên theo chất lượng tín nhiệm và biên độ biến động giá của tài sản thế chấp, dao động từ 0% đến 1% đối với trái phiếu chính phủ ngắn hạn và có thể lên tới 50% đối với cổ phiếu (fixed_income_during, Ch.14, Haircut, d.30).

Tuy nhiên, việc áp đặt haircut tạo ra sự bất đối xứng về rủi ro tín dụng đối tác (fixed_income_during, Ch.14, Haircut, d.32). Một mức haircut cao đồng nghĩa với việc bên vay tiền phải chuyển giao một lượng giá trị chứng khoán lớn hơn nhiều so với khoản tiền mặt nhận về (fixed_income_during, Ch.14, Haircut, d.32). Cấu trúc này đẩy bên cung cấp chứng khoán vào tình thế chịu rủi ro mất mát phần giá trị tài sản vượt mức nếu bên cho vay tiền mặt mất khả năng thanh toán (fixed_income_during, Ch.14, Haircut, d.32).

Ngân hàng trung ương tận dụng ưu thế độc quyền tiền tệ để áp đặt các mức haircut cao bất đối xứng lên các định chế vay mượn nhằm triệt tiêu rủi ro sai chiều (wrong-way risk) (fixed_income_during, Ch.14, Haircut, d.32). Rủi ro sai chiều phát sinh từ mức độ tương quan thuận cao giữa sự suy giảm chất lượng tín nhiệm của ngân hàng đi vay và sự sụt giá của chính tài sản mà ngân hàng đó đem thế chấp trong các cuộc khủng hoảng hệ thống (fixed_income_during, Ch.14, Haircut, d.32).

Quy chế haircut hoạt động bổ trợ cho [[central-bank-collateral-framework-design-and-risk-control|khung quản trị tài sản bảo đảm của ngân hàng trung ương]], đồng thời ảnh hưởng trực tiếp đến tốc độ luân chuyển tài sản trong các [[collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties|chuỗi tái thế chấp tài sản bảo đảm]].
