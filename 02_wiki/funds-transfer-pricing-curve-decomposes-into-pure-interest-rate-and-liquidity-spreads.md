---
title: funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads
type: concept
tags: [alm, ftp, yield-curve, liquidity-premium, risk-free-rate, pricing]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]
has_part: [regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp, contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]
---

Đường cong [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks|FTP]] bù cho Treasury cả rủi ro lãi suất lẫn rủi ro thanh khoản, nên nguồn tách hai thành phần: dựng một đường cong rủi ro lãi suất thuần rồi cộng thêm chênh lệch tài trợ (*funding spread*) (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1641). Có năm cách dựng cấu trúc kỳ hạn của lãi suất phi rủi ro, mỗi cách có ưu và nhược điểm (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1643):
1. **Trái phiếu chính phủ** ở nước mà chính phủ có quyền in tiền, như đường cong Kho bạc Mỹ; ở châu Âu không nước nào có quyền in đồng euro, nên nợ chính phủ có phần bù rủi ro vỡ nợ khác nhau giữa các nước (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1645);
2. **Trái phiếu chính phủ trung ương khu vực euro xếp hạng AAA**, cho đường cong gần như phi rủi ro; nhược điểm là rất ít chính phủ đạt hạng này, chỉ năm tính tới 2024 (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1646–1652);
3. **Lãi suất ngắn hạn euro (€STR) và phái sinh dựa trên €STR**; nhược điểm là lợi suất dựa trên €STR chưa có cấu trúc kỳ hạn hướng tới tương lai và được tính sau, dồn theo thời gian (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1653);
4. **Lãi suất repo**, dựa trên vay và cho vay có bảo đảm; nhược điểm là thị trường repo ngắn hạn, thường chỉ thanh khoản tới một hoặc hai năm, và có lúc mất thanh khoản như năm 2007–2008 (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1654);
5. **Đường cong hoán đổi lãi suất dựa trên EURIBOR**, kéo tới 30 năm và khá thanh khoản; nhưng lãi suất được hoán đổi dựa trên vay không bảo đảm giữa các ngân hàng, nên lãi suất swap phản ánh rủi ro tín dụng đối tác giữa các ngân hàng (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1655–1657).

Chênh lệch tài trợ trên lãi suất phi rủi ro phụ thuộc vào từng tài sản: chứng khoán thanh khoản, chất lượng cao có thể được tài trợ trên thị trường repo, còn tài sản kém thanh khoản, chất lượng thấp hơn phải được tài trợ không bảo đảm, đắt hơn (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1659). Vì có nhiều đường cong riêng là không thực tế, nguồn cho rằng nên dùng một đường cong FTP phản ánh chênh lệch tài trợ bình quân rồi chỉnh theo từng trường hợp (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1659). Phần bù thanh khoản bình quân được tính bằng cách hiệu chuẩn theo cơ hội huy động và đầu tư hiện có của ngân hàng: nếu ngân hàng đang phát hành giấy nợ 2 năm lãi suất cố định ở 3% và lãi suất thả nổi ở 2,2%, chênh lệch tài trợ kỳ hạn 2 năm là 80 điểm cơ bản (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1659).

Việc tách hai thành phần cho phép định giá sản phẩm có kỳ hạn của lãi suất tham chiếu khác kỳ hạn hợp đồng (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1661). Ví dụ: một khoản vay khách hàng 2 năm, lãi suất cố định 1 năm đầu rồi định lại, có lãi suất FTP bằng 1,6% rủi ro lãi suất cộng 80 điểm cơ bản phần bù thanh khoản, tức 2,4% (tata_bank_alm, Ch.2, Interest Rate vs. Liquidity Risk, d.1661). Với vị thế bằng đồng tiền khác đồng tiền gốc của đường cong, bàn ALM địa phương có thể dựng đường cong riêng, hoặc bàn ALM tập trung định giá trên đường cong gốc sau khi áp điều chỉnh chéo tiền tệ vào chênh lệch tài trợ, mức điều chỉnh quan sát được trên thị trường hoán đổi chéo tiền tệ (tata_bank_alm, Ch.2, Multi-currency FTP Curve, d.1665–1673). Trang [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] và trang [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]] ghi các phụ phí cộng thêm vào đường cong này.
