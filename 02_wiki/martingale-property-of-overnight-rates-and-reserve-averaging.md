---
title: martingale-property-of-overnight-rates-and-reserve-averaging
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, interest-rates, money-market]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

**Martingale property của lãi suất qua đêm**: Trong phiên giao dịch bất kỳ, kỳ vọng lãi suất ở phiên tiếp theo bằng lãi suất hiện tại — $E(i_{t+1} | I_t) = i_t$. Đây là hệ quả tất yếu của arbitrage: nếu $i_1 > E(i_2)$, toàn bộ ngân hàng sẽ cho vay ở phiên 1 và vay ở phiên 2, đẩy $i_1$ xuống và $i_2$ lên cho đến khi bằng nhau. Ngược lại nếu $i_1 < E(i_2)$ tất cả đảo chiều. Cân bằng duy nhất là martingale (bindseil_monetary_policy, Ch.5, §5.1, d.1192–1196).

**Hệ quả cho thời điểm OMO trong ngày**: Bindseil mô hình hoá một ngày có 3 phiên giao dịch và 3 shock autonomous factors. Khi NHTW thực hiện OMO sớm (buổi sáng), lãi suất phiên 1 bằng midpoint corridor, nhưng biến động tăng dần ở các phiên sau khi shock materialized. Khi OMO thực hiện giữa ngày (trung hoà shock sáng), lãi suất ổn định hơn — chỉ phiên cuối mới biến động. Thực hiện OMO cuối ngày = ổn định tối đa nhưng phi thực tế. Bank of Canada thực hiện OMO lúc giữa ngày chính xác vì lý do này (bindseil_monetary_policy, Ch.5, §5.1, d.1143–1175).

Quan sát quan trọng từ mô hình: mức độ volatility tuyệt đối của shock autonomous factors **không ảnh hưởng** tới volatility lãi suất — shock lớn hơn cũng làm tăng uncertainty cuối ngày tương ứng, hai hiệu ứng triệt tiêu nhau. Điều quan trọng là **profile theo thời gian** của volatility: nếu shock tăng dần trong ngày, lãi suất sẽ ổn định (vì uncertainty cuối ngày lớn kéo lãi suất về midpoint); nếu shock giảm dần, lãi suất sẽ biến động nhiều hơn (bindseil_monetary_policy, Ch.5, §5.1, d.1175).

**Reserve averaging qua nhiều ngày**: Mô hình 3 phiên giao dịch trong 1 ngày tương đương hoàn toàn với kỳ duy trì dự trữ (reserve maintenance period) 3 ngày có averaging — miễn là không có ràng buộc không thâm hụt cuối ngày. Ngân hàng thực hiện inter-temporal arbitrage qua toàn bộ kỳ duy trì giống như arbitrage giữa các phiên trong ngày → martingale property áp dụng xuyên suốt kỳ duy trì (bindseil_monetary_policy, Ch.5, §5.2, d.1200–1206).

Trong thực tế, martingale property bị vi phạm nhẹ vì: ràng buộc không thâm hụt cuối ngày, chi phí giao dịch, giới hạn giao dịch liên ngân hàng, và "window dressing" của ngân hàng. Perez Quiros & Rodriguez (2006) tìm thấy xu hướng lãi suất tăng nhẹ cuối kỳ duy trì: ngân hàng ưa hoàn thành RR muộn để giữ linh hoạt xử lý shock — nhưng hiệu ứng này hầu như biến mất ở euro area do tổng RR cao hơn (bindseil_monetary_policy, Ch.5, §5.2, d.1212). Kết nối: [[interest-rate-corridor-symmetric-approach]], [[autonomous-factors-of-central-bank-balance-sheet]].
