---
title: bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance
type: concept
tags: [yield-curve, relative-value, spread-trading, bpv-weighting, dv01, risk-management, stop-loss]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Giao dịch spread trên đường cong lợi suất (yield spread trading) là chiến lược kinh doanh thu nhập cố định phi định hướng (market non-directional trading), được thiết kế để loại bỏ hoàn toàn rủi ro thị trường bậc một (first-order market-directional risk) và chỉ thu lợi nhuận từ sự thay đổi tương đối của độ chênh lệch lợi suất giữa các phân đoạn kỳ hạn (choudhry_analysing_yield_curve, Ch.12, Sec. "Yield Spread Trades", "Bond Spread Weighting" & "Types of Bond Spreads", d.4899–4940). Trong thực tế thị trường, không tồn tại mối liên hệ giải tích tất yếu nào giữa hướng dịch chuyển của mặt bằng lãi suất chung và sự thay đổi hình thái đường cong: đường cong có thể dốc lên (steepen) hoặc phẳng đi (flatten) trong cả môi trường lãi suất tăng lẫn lãi suất giảm (choudhry_analysing_yield_curve, Ch.12, d.4901).

Để triệt tiêu rủi ro định hướng khi xây dựng một vị thế spread (chẳng hạn chiến lược làm phẳng đường cong giữa kỳ hạn 2 năm và 10 năm bằng cách bán khống trái phiếu 2 năm và mua trái phiếu 10 năm), khối lượng giao dịch giữa hai chân phải được điều chỉnh tỷ lệ nghịch với giá trị một điểm cơ bản (Basis Point Value - BPV hoặc Dollar Value of a Basis Point - DV01):
$$N_1 \cdot BPV_1 = N_2 \cdot BPV_2 \implies N_1 = N_2 \cdot \frac{BPV_2}{BPV_1}$$
Trong đó $BPV_i = P_i \cdot MD_i \cdot 0.0001$ đo lường mức thay đổi thị giá tuyệt đối của trái phiếu thứ $i$ khi lợi suất dịch chuyển 1 điểm cơ bản ($0.01\%$). Việc cân bằng tỷ trọng theo BPV bảo đảm khi mặt bằng lãi suất dịch chuyển song song, mức lãi/lỗ trên chân mua và chân bán sẽ tự động triệt tiêu lẫn nhau [[parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments]], giữ cho danh mục miễn nhiễm trước các biến động vĩ mô tổng thể.

Tuy nhiên, Moorad Choudhry lưu ý rằng chỉ số BPV bắt nguồn từ thước đo Modified Duration mang bản chất xấp xỉ tuyến tính bậc một. Khi xảy ra các cú sốc lãi suất lớn hoặc dải biến động mạnh, sự chênh lệch độ lồi (convexity differential) giữa hai trái phiếu có kỳ hạn cách xa nhau sẽ bộc lộ rõ rệt ($\Delta P \approx -BPV \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2$), làm lệch tỷ lệ cân bằng BPV ban đầu và sinh ra rủi ro định hướng dư thừa. Do đó, nhà kinh doanh buộc phải thường xuyên giám sát và tái cân bằng tỷ trọng vị thế trong các giai đoạn thị trường biến động cao (choudhry_analysing_yield_curve, Ch.12, d.4908).

Hiệu quả thực thi của giao dịch spread đòi hỏi việc tuân thủ một khung quản trị kỷ luật giao dịch chặt chẽ gồm ba yếu tố cốt lõi:
1. Xác lập mục tiêu chênh lệch (target spread): Định lượng cụ thể mức chênh lệch kỳ vọng để thực hiện chốt lời (ví dụ từ mức 59.7 điểm cơ bản thu hẹp về 50 điểm cơ bản). Nếu chênh lệch đạt mục tiêu sớm hơn dự kiến, kỷ luật giao dịch đòi hỏi phải hiện thực hóa lợi nhuận ngay lập tức thay vì suy đoán tiếp diễn.
2. Chân trời thời gian cố định (fixed time horizon): Áp đặt một khung thời gian tối đa để kiểm nghiệm giả thuyết đầu tư (ví dụ 3 tuần). Nếu hết thời hạn này mà chênh lệch vẫn chưa đạt mục tiêu, vị thế bắt buộc phải được tất toán (unwind) để giải phóng hạn mức vốn và ngăn ngừa rủi ro chôn vốn.
3. Ngưỡng cắt lỗ nghiêm ngặt (strict stop-loss rule): Choudhry thiết lập quy tắc cắt lỗ chuẩn mực tại đúng 50% biên độ mục tiêu lợi nhuận khi thị trường đi ngược kỳ vọng (choudhry_analysing_yield_curve, Ch.12, d.4924–4925). Ví dụ, nếu mục tiêu lợi nhuận kỳ vọng là 9.7 điểm cơ bản (từ 59.7 về 50.0), điểm dừng lỗ sẽ được kích hoạt dứt khoát khi chênh lệch nới rộng thêm 4.8 điểm cơ bản lên mức 64.5 điểm cơ bản.

Khung kỷ luật này ngăn ngừa hiện tượng duy ý chí nắm giữ vị thế lỗ chờ hồi phục trong kinh doanh giá trị tương đối, liên kết chặt chẽ với việc quản trị chi phí tài trợ repo [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]], phương pháp bóc tách thặng dư cục bộ [[excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions]], và các chiến lược giao dịch độ cong phức hợp [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]].
