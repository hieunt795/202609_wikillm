---
title: collateralized-clearing-and-hedging-demand-drive-interest-rate-swaps-below-sovereign-yields
type: concept
tags: [interest-rate-swaps, sovereign-debt, market-microstructure, central-clearing, post-2008]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Nghịch lý chênh lệch hoán đổi âm (negative swap spread) là hiện tượng lãi suất hoán đổi (interest-rate swap rate) giao dịch ở mức thấp hơn lợi suất trái phiếu chính phủ cùng kỳ hạn (như USD swap curve nằm dưới US Treasury curve ở các kỳ hạn từ 5 đến 30 năm), phá vỡ quan niệm tài chính truyền thống tiền khủng hoảng 2008 vốn luôn coi trái phiếu chính phủ là sàn lãi suất phi rủi ro thấp nhất (choudhry_analysing_yield_curve, Ch.1, The Interest-Rate Swap Curve and the Sovereign Bond Curve, d.1020–1038).

Choudhry lý giải sự đảo lộn cấu trúc này thông qua ba động lực vi cấu trúc và thể chế hậu 2008 (choudhry_analysing_yield_curve, Ch.1, d.1036–1044):
1. Triệt tiêu rủi ro tín dụng đối tác qua bù trừ trung tâm (CCP): Toàn bộ các giao dịch hoán đổi lãi suất liên ngân hàng bắt buộc phải bù trừ qua CCP với cơ chế ký quỹ ban đầu (initial margin) và điều chỉnh giá trị thị trường hàng ngày (variation margin), biến hợp đồng swap thành công cụ phái sinh gần như phi rủi ro tương đương tín nhiệm của chính phủ;
2. Cầu phòng hộ nhận lãi suất cố định vượt trội: Các ngân hàng và định chế tài chính phi ngân hàng đối mặt với nhu cầu phòng hộ khổng lồ đối với các khoản phải thu lãi suất cố định dài hạn, tạo áp lực trả thả nổi / nhận cố định (pay-floating / receive-fixed) liên tục đẩy lãi suất swap dài hạn xuống thấp;
3. Ràng buộc chi phí vốn và tính thanh khoản: Các quy định khắt khe về tỷ lệ đòn bẩy và vốn cho sổ kinh doanh (Trading Book) khiến các ngân hàng tạo lập thị trường tốn kém chi phí bảng cân đối rất lớn khi nắm giữ trái phiếu kho bạc vật chất, trong khi thị trường phái sinh swap ngoại bảng sở hữu thanh khoản vượt trội và không tiêu tốn tỷ lệ đòn bẩy tương đương.

Hiện tượng này đánh dấu bước chuyển biến căn bản trong phân tích cấu trúc kỳ hạn hậu khủng hoảng, liên kết trực tiếp với cơ chế điều chỉnh chi phí tài trợ [[xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices]], tái định hình sự phân kỳ giữa đường cong swap và trái phiếu ngân hàng tại [[swap-rate-term-structures-diverge-from-bank-bond-yields-due-to-panel-survivorship-bias]], và phản ánh tác động phân bổ vốn trong [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]].
