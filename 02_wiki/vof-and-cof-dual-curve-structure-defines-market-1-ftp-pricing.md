---
title: vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing
type: concept
tags: [alm, ftp, vof, cof, pricing, balance-sheet, market-1]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-26
---

Đường cong định giá điều chuyển vốn nội bộ trên Thị trường 1 (giữa Hội sở và mạng lưới chi nhánh phục vụ khách hàng) tại các ngân hàng thương mại Việt Nam được thiết lập theo cấu trúc hai vế đối xứng: Giá mua vốn (Value of Funds — VOF) áp dụng cho tài sản nợ và Giá bán vốn (Cost of Funds — COF) áp dụng cho tài sản có (vab_ftp_methodology, Điều 4.1, d.201–234). Cấu trúc hai vế này cho phép Trung tâm Điều chuyển Vốn Nội bộ (CFU) phân bổ độc lập biên thu nhập lãi thuần kế hoạch và thu hồi đầy đủ các chi phí tuân thủ quy chuẩn của Ngân hàng Nhà nước từ các đơn vị sử dụng vốn (vab_ftp_methodology, Điều 4, d.196–200).

Giá mua vốn VOF là tỷ suất sinh lời nội bộ mà CFU thanh toán cho các đơn vị kinh doanh huy động tiền gửi, bao gồm ba cấu phần cơ bản (vab_ftp_methodology, Điều 4.1, d.203–208):
$$VOF = Base\ Curve + Margin + ALCO\ adjust_{nợ}$$
Trong đó, lãi suất cơ sở ($Base\ Curve$) xây dựng theo phương pháp tại [[ftp-base-curve-construction-contrasts-vnd-historical-cost-with-usd-market-benchmarks]], hỗ trợ huy động ($Margin$) là biên lợi nhuận phân bổ từ kế hoạch kinh doanh theo [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]], và $ALCO\ adjust_{nợ}$ là mức điều chỉnh chính sách do Hội đồng ALCO ban hành nhằm kích thích huy động các kỳ hạn hoặc phân khúc mục tiêu (vab_ftp_methodology, Điều 4.1, d.205–207).

Giá bán vốn COF là chi phí vốn nội bộ mà CFU tính cho các đơn vị kinh doanh khi giải ngân cho vay hoặc đầu tư tài sản, bao gồm bảy cấu phần tách biệt (vab_ftp_methodology, Điều 4.1, d.211–220):
$$COF = Base\ Curve + Margin + Chi\ phí\ DTBB + Chi\ phí\ BHTG + Liquidity\ Premium + Term\ Liquidity\ Premium + ALCO\ adjust_{có}$$
Trong cấu trúc này, CFU kết chuyển toàn bộ $Base\ Curve$ và $Margin$ đã cam kết chi trả cho bên huy động sang bên sử dụng vốn, đồng thời cộng thêm các chi phí pháp lý phát sinh theo [[regulatory-deposit-insurance-and-statutory-reserves-apportion-into-market-1-cof]] (vab_ftp_methodology, Điều 4.1, d.213–216). Phần bù tài sản thanh khoản ($Liquidity\ Premium$) bù đắp chi phí nắm giữ đệm tài sản thanh khoản cao theo Thông tư 22/2019/TT-NHNN, còn phần bù thanh khoản kỳ hạn ($Term\ Liquidity\ Premium$) áp dụng cho các khoản vay lãi suất thả nổi nhằm bảo đảm lãi suất sau điều chỉnh tương đương với sản phẩm lãi suất cố định có cùng kỳ hạn gốc theo [[matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch]] (vab_ftp_methodology, Điều 4.3.3 & 4.3.4, d.441, d.476).

Tất cả các cấu phần trong VOF và COF đều được tính toán độc lập cho từng loại tiền tệ (VND, USD và các ngoại tệ khác) để phản ánh trung thực chi phí cơ hội thực tế của từng đồng tiền (vab_ftp_methodology, Điều 4.1, d.221). Bằng việc phân rã rạch ròi các cấu phần trên, hệ thống quản trị CFU tại [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]] bảo đảm việc bóc tách rủi ro thanh khoản và rủi ro lãi suất theo đúng nguyên lý chuẩn mực của [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], đồng thời làm cơ sở triển khai các quy tắc tính giá cho từng cấu trúc sản phẩm cụ thể theo [[deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles]], [[promotional-and-behavioral-loan-ftp-pricing-decomposes-hybrid-cash-flows]], và kích hoạt quy trình tái định giá khi phát sinh biến cố cơ cấu nợ theo [[contractual-amendment-ftp-repricing-rules-govern-loan-and-deposit-restructuring]].


