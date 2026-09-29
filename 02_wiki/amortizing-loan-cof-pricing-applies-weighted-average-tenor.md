---
title: amortizing-loan-cof-pricing-applies-weighted-average-tenor
type: concept
tags: [alm, ftp, cof, amortizing-loans, wat, weighted-average-tenor, floating-rate, market-1]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Đối với các sản phẩm cho vay có lịch trình thanh toán nợ gốc chia thành nhiều kỳ định kỳ (amortizing loans) như cho vay mua nhà trả góp, cho vay mua ô tô hoặc cấp tín dụng trung dài hạn tài trợ dự án, dòng tiền hoàn vốn giảm dần theo thời gian làm cho kỳ hạn rủi ro thực tế của khoản vay ngắn hơn đáng kể so với kỳ hạn pháp lý cuối cùng của hợp đồng tín dụng (vab_ftp_methodology, Điều 6.2.d.i, d.744; Điều 6.2.e.i, d.760). Để phản ánh chính xác chi phí cam kết nguồn vốn nội bộ, Trung tâm Điều chuyển Vốn Nội bộ (CFU) áp dụng phương pháp Bình quân gia quyền (Weighted Average) nhằm lượng hóa Kỳ hạn hiệu lực (Weighted Average Tenor — WAT) của khoản vay (vab_ftp_methodology, Điều 6.2.d.iii, d.746–754):
$$WAT = \frac{\sum_{i=1}^N (P_i \times T_i)}{\sum_{i=1}^N P_i}$$
trong đó $N$ là tổng số kỳ trả nợ gốc theo lịch trình hợp đồng, $P_i$ là số dư gốc được thanh toán trong kỳ thứ $i$, và $T_i$ là số ngày thực tế tính từ ngày giải ngân ban đầu đến ngày thanh toán nợ gốc của kỳ thứ $i$ (vab_ftp_methodology, Điều 6.2.d.iii, d.752–754).

Khi khoản vay trả nợ gốc định kỳ áp dụng lãi suất cố định suốt đời hợp đồng, lãi suất COF cơ sở được xác định tương ứng trực tiếp với kỳ hạn hiệu lực $WAT$ căn cứ vào biểu COF Thị trường 1 tại ngày giải ngân và được áp dụng cố định trong suốt toàn bộ thời gian cho vay (vab_ftp_methodology, Điều 6.2.d.ii, d.745; Điều 6.2.d.iv, d.755). Do kỳ hạn hiệu lực đã hấp thụ trọn vẹn rủi ro kỳ hạn của dòng tiền trả dần, phần bù thanh khoản kỳ hạn của khoản vay trả góp lãi suất cố định được ấn định bằng 0% (vab_ftp_methodology, Điều 6.2.d.v, d.756).

Ngược lại, khi khoản vay trả nợ gốc định kỳ áp dụng lãi suất thả nổi, CFU kết hợp đồng thời phương pháp kỳ hạn hiệu lực $WAT$ với chu kỳ định giá lại lãi suất định kỳ (vab_ftp_methodology, Điều 6.2.e.ii–vi, d.761–770):
1. **Lãi suất COF cơ sở**: Xác định tương ứng với kỳ hạn tái định giá của khoản vay tại ngày giải ngân hoặc ngày điều chỉnh lãi suất gần nhất, áp dụng đến ngày điều chỉnh tiếp theo (vab_ftp_methodology, Điều 6.2.e.ii–iii, d.761–762);
2. **Phần bù thanh khoản kỳ hạn**: Được đo lường bằng mức chênh lệch giữa lãi suất của kỳ hạn hiệu lực $WAT$ và lãi suất của kỳ hạn tái định lại lãi suất tại thời điểm xác định giá:
$$\text{Phần bù thanh khoản kỳ hạn} = COF_{WAT} - COF_{\text{kỳ hạn tái định giá}}$$
Khoản phần bù này có hiệu lực cho đến ngày điều chỉnh lãi suất kế tiếp của hợp đồng tín dụng (vab_ftp_methodology, Điều 6.2.e.vi, d.769–770, d.780).

Quy tắc tính toán dựa trên $WAT$ này giải quyết dứt điểm nghịch lý lệch pha kỳ hạn theo [[matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch]], bổ trợ hoàn hảo cho cấu trúc bullet tại [[straight-term-bullet-loan-cof-pricing-decomposes-repricing-and-term-risk]], và được tự động hóa tra cứu thông qua ma trận hai chiều tại [[term-liquidity-premium-matrix-calibrates-two-dimensional-floating-rate-spreads]].
