---
title: matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch
type: concept
tags: [alm, ftp, matched-maturity, term-liquidity-spread, floating-rate, repricing-mismatch, wat]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-26
---

Trong cấu trúc định giá bán vốn (Cost of Funds — COF) của hệ thống [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]], các khoản tín dụng lãi suất thả nổi đặt ra một nghịch lý kép về quản trị kỳ hạn: rủi ro lãi suất chỉ tồn tại trong chu kỳ tái định giá ngắn hạn (ví dụ 1 tháng hoặc 3 tháng một lần), nhưng rủi ro thanh khoản — tức nghĩa vụ cam kết tài trợ nguồn vốn của ngân hàng cho khách hàng vay — lại kéo dài suốt toàn bộ kỳ hạn gốc của khoản vay (ví dụ 5 năm hoặc 10 năm) (vab_ftp_methodology, Điều 6.2.c, d.732–739). Nếu ngân hàng chỉ áp giá FTP theo kỳ hạn tái định giá 3 tháng, đơn vị kinh doanh sẽ được hưởng chi phí vốn ngắn hạn rất thấp trong khi đẩy toàn bộ rủi ro thanh khoản dài hạn cho khối Nguồn vốn gánh chịu mà không phải trả phí (vab_ftp_methodology, Điều 6.2.c.iv, d.738–739). Ngược lại, nếu áp giá FTP theo kỳ hạn gốc 5 năm cố định, đơn vị kinh doanh sẽ bị thiệt thòi khi lãi suất thị trường suy giảm và chịu rủi ro lệch pha định giá lại theo [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]].

Để giải quyết triệt để sự xung đột này, phương pháp luận FTP của ngân hàng thực hiện phân rã giá bán vốn thành hai cấu phần độc lập theo nguyên lý của [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]]:
$$\text{COF tổng thể} = \text{Lãi suất COF cơ sở} + \text{Phần bù thanh khoản kỳ hạn}$$
Trong đó, Lãi suất COF cơ sở được xác định tương ứng với kỳ hạn tái định giá của hợp đồng tín dụng căn cứ vào biểu COF Thị trường 1 theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] tại ngày giải ngân hoặc ngày điều chỉnh lãi suất, và có hiệu lực cho đến ngày điều chỉnh lãi suất tiếp theo (vab_ftp_methodology, Điều 6.2.c.ii–iii, d.736–737). Cấu phần thứ hai — Phần bù thanh khoản kỳ hạn (Term Liquidity Spread) — được tính toán bằng mức chênh lệch giữa lãi suất của kỳ hạn gốc hợp đồng và lãi suất của kỳ hạn tái định giá tại thời điểm phát sinh:
$$\text{Phần bù thanh khoản kỳ hạn} = COF_{\text{kỳ hạn gốc}} - COF_{\text{kỳ hạn tái định giá}}$$
Khoản phần bù này phản ánh chính xác chi phí cam kết thanh khoản dài hạn mà khối Nguồn vốn (Treasury) phải duy trì để bảo đảm nguồn tài trợ không bị gián đoạn (vab_ftp_methodology, Điều 6.2.c.iv, d.738–740).

Đối với các khoản vay có lịch trình trả gốc định kỳ từng lần (amortizing loans) thay vì trả một lần khi đáo hạn, dòng tiền gốc giảm dần làm cho kỳ hạn rủi ro thực tế của khoản vay ngắn hơn đáng kể so với kỳ hạn pháp lý cuối cùng của hợp đồng (vab_ftp_methodology, Điều 6.2.d.iii, d.746). Khi đó, hệ thống FTP áp dụng phương pháp Bình quân gia quyền (Weighted Average) để lượng hóa Kỳ hạn hiệu lực (Weighted Average Tenor — WAT) của khoản vay theo công thức:
$$WAT = \frac{\sum_{i=1}^N (P_i \times T_i)}{\sum_{i=1}^N P_i}$$
trong đó $N$ là tổng số kỳ trả nợ gốc theo lịch trình hợp đồng, $P_i$ là số dư gốc được thanh toán trong kỳ thứ $i$, và $T_i$ là số ngày từ ngày giải ngân đến ngày thanh toán kỳ thứ $i$ (vab_ftp_methodology, Điều 6.2.d.iii, d.748–754). 

Nếu khoản vay trả nợ định kỳ có lãi suất cố định suốt đời hợp đồng, lãi suất COF cơ sở được xác định trực tiếp theo kỳ hạn hiệu lực $WAT$ và duy trì cố định, còn phần bù thanh khoản kỳ hạn được gán bằng 0 (vab_ftp_methodology, Điều 6.2.d.ii–v, d.745–756). Nếu khoản vay trả nợ định kỳ áp dụng lãi suất thả nổi, CFU kết hợp đồng thời cả hai kỹ thuật: Lãi suất COF cơ sở lấy theo kỳ hạn tái định giá, trong khi Phần bù thanh khoản kỳ hạn được xác định dựa trên chênh lệch giữa lãi suất của kỳ hạn hiệu lực $WAT$ và lãi suất của kỳ hạn tái định giá:
$$\text{Phần bù thanh khoản kỳ hạn} = COF_{WAT} - COF_{\text{kỳ hạn tái định giá}}$$
(vab_ftp_methodology, Điều 6.2.e, d.758–770; vab_ftp_methodology, Điều 6.2.l, d.914–933). Trường hợp khoản vay có thời gian ân hạn trả gốc, việc dư nợ gốc duy trì 100% trong toàn bộ các kỳ đầu làm tăng trọng số thời gian $T_i$ trong tử số của công thức $WAT$; do đó, khoản vay có thời gian ân hạn sở hữu kỳ hạn hiệu lực $WAT$ dài hơn đáng kể và phải chịu mức phần bù thanh khoản kỳ hạn cao hơn so với khoản vay trả nợ gốc đều ngay từ kỳ đầu (vab_ftp_methodology, Điều 6.2.d.iii, d.748–754; Phụ lục 02.6, d.1600–1620).

Nhờ kỹ thuật bóc tách phần bù thanh khoản kỳ hạn kết hợp kỳ hạn hiệu lực $WAT$, mọi sự lệch pha giữa chu kỳ định giá lại lãi suất và kỳ hạn cam kết nguồn vốn đều được lượng hóa minh bạch bằng tiền tệ. Đơn vị kinh doanh được giải phóng hoàn toàn khỏi rủi ro thị trường để bảo toàn biên độ tín dụng thương mại, trong khi khối Treasury thu hồi đầy đủ chi phí bù đắp rủi ro tái tài trợ thanh khoản trên bảng cân đối kế toán, với toàn bộ các mức chênh lệch được cấu hình và tra cứu tự động hóa qua [[term-liquidity-premium-matrix-calibrates-two-dimensional-floating-rate-spreads]] (vab_ftp_methodology, Phụ lục 02.6, d.1590–1656). Nguyên lý bóc tách này đồng thời làm nền tảng toán học để bóc tách cấu phần định giá cho các hợp đồng tín dụng ưu đãi lãi suất giai đoạn đầu theo [[promotional-and-behavioral-loan-ftp-pricing-decomposes-hybrid-cash-flows]].

