---
title: straight-term-bullet-loan-cof-pricing-decomposes-repricing-and-term-risk
type: concept
tags: [alm, ftp, cof, bullet-loans, straight-term, floating-rate, term-liquidity-spread, market-1]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Trong cơ chế định giá bán vốn (COF) Thị trường 1, sản phẩm cho vay thanh toán toàn bộ nợ gốc một lần khi đáo hạn (bullet loan hay straight-term) được phân tách thành hai quy trình định giá riêng biệt tùy thuộc vào cơ chế lãi suất theo hợp đồng tín dụng: cố định hoặc thả nổi (vab_ftp_methodology, Điều 6.2.b–c, d.725–741). Sự phân tách này phản ánh chính xác ranh giới kinh tế giữa rủi ro định giá lại lãi suất ngắn hạn và nghĩa vụ cam kết thanh khoản dài hạn của ngân hàng theo cấu trúc hai vế tại [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]].

Đối với khoản cho vay thanh toán gốc cuối kỳ áp dụng lãi suất cố định suốt đời hợp đồng, Trung tâm Điều chuyển Vốn Nội bộ (CFU) xác định lãi suất COF cơ sở tương ứng trực tiếp với kỳ hạn gốc của khoản vay (tính bằng ngày đáo hạn trừ ngày giải ngân) căn cứ vào biểu lãi suất COF Thị trường 1 ban hành tại ngày giải ngân (vab_ftp_methodology, Điều 6.2.b.ii, d.728). Mức lãi suất COF cơ sở này được áp dụng cố định trong suốt thời hạn cho vay, đồng thời phần bù thanh khoản kỳ hạn được ấn định bằng 0% do kỳ hạn tái định giá lãi suất trùng khớp hoàn toàn với kỳ hạn cam kết nguồn vốn (vab_ftp_methodology, Điều 6.2.b.iii–iv, d.729–730).

Ngược lại, đối với khoản cho vay thanh toán gốc cuối kỳ áp dụng lãi suất thả nổi định kỳ (ví dụ khoản vay 5 năm thả nổi 3 tháng một lần), phương pháp luận FTP thực hiện bóc tách kép hai cấu phần độc lập (vab_ftp_methodology, Điều 6.2.c.ii–iv, d.736–739):
1. **Lãi suất COF cơ sở**: Lấy tương ứng với kỳ hạn tái định giá (ví dụ 3 tháng) theo biểu COF Thị trường 1 có hiệu lực tại ngày giải ngân hoặc ngày điều chỉnh lãi suất gần nhất, áp dụng cho đến ngày điều chỉnh lãi suất tiếp theo của hợp đồng tín dụng (vab_ftp_methodology, Điều 6.2.c.ii–iii, d.736–737);
2. **Phần bù thanh khoản kỳ hạn (Term Liquidity Spread)**: Được xác định bằng chênh lệch giữa lãi suất của kỳ hạn gốc hợp đồng (5 năm) và lãi suất của kỳ hạn tái định giá (3 tháng) tại ngày xác lập mức giá:
$$\text{Phần bù thanh khoản kỳ hạn} = COF_{\text{kỳ hạn gốc}} - COF_{\text{kỳ hạn tái định giá}}$$
Khoản phần bù này có hiệu lực cho đến ngày điều chỉnh lãi suất tiếp theo, bảo đảm thu hồi đầy đủ chi phí thanh khoản mà khối Treasury phải duy trì để bảo đảm nguồn vốn không bị gián đoạn (vab_ftp_methodology, Điều 6.2.c.iv–v, d.738–740).

Quy tắc định giá bullet này thiết lập chuẩn mực cơ sở để bóc tách rủi ro kỳ hạn theo [[matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch]], làm điểm tham chiếu để so sánh với phương pháp kỳ hạn hiệu lực của [[amortizing-loan-cof-pricing-applies-weighted-average-tenor]], đồng thời tạo nền tảng để xây dựng các gói tín dụng ưu đãi theo [[promotional-hybrid-loan-ftp-pricing-evaluates-dual-tenor-and-component-decomposition]].
