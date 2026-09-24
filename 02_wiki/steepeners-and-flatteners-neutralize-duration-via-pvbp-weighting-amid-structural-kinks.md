---
title: "Steepeners and Flatteners Neutralize Duration via PVBP Weighting Amid Structural Kinks"
type: concept
tags:
  - trading
  - curve-trading
  - steepeners
  - flatteners
  - pvbp-neutral
  - structural-kinks
  - jgb
sources: [fixed_income_during, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Chiến lược làm dốc (Steepeners) và làm phẳng (Flatteners) là hình thức giao dịch đường cong hai chân ($n=2$) cơ bản nhất, phản ánh kỳ vọng của nhà đầu tư về sự dịch chuyển tương đối giữa lợi suất kỳ hạn dài và lợi suất kỳ hạn ngắn dọc theo cấu trúc kỳ hạn (fixed_income_during, Ch.31, Sec.31.1.2, d.64–71). Trong quy ước thị trường phái sinh và trái phiếu quốc tế, trạng thái "long the curve" đồng nghĩa với việc mở vị thế làm dốc (Steepener — kỳ vọng đường cong dựng đứng hơn), trong khi "short the curve" tương đương với việc mở vị thế làm phẳng (Flattener — kỳ vọng chênh lệch kỳ hạn thu hẹp lại) [[curve-trading-hierarchies-systematically-immunize-lower-order-risk-dimensions]].

Để cô lập thuần túy rủi ro độ dốc và loại trừ rủi ro định hướng từ sự dịch chuyển song song của mặt bằng lãi suất, hai khối lượng danh nghĩa ($N_1, N_2$) của vị thế phải thỏa mãn điều kiện trung hòa rủi ro thời lượng tiền mặt (PVBP neutrality) (fixed_income_during, Ch.31, Sec.31.1.2, d.80–89):

$$N_1 \text{PVBP}_1 + N_2 \text{PVBP}_2 = 0$$

Khi xác định quy mô rủi ro tổng thể $R$ (tương đương với mức lãi lỗ P&L phát sinh khi chênh lệch lợi suất giữa hai chân dịch chuyển 1 điểm cơ bản), quy mô vị thế danh nghĩa cho chiến lược làm dốc (Steepener) được thiết lập với $N_1 > 0$ (mua kỳ hạn ngắn) và $N_2 < 0$ (bán kỳ hạn dài):

$$N_1 = \frac{R}{\text{PVBP}_1}, \quad N_2 = -\frac{R}{\text{PVBP}_2}$$

Ngược lại, chiến lược làm phẳng (Flattener) áp dụng cùng công thức với dấu đảo ngược ($N_1 < 0, N_2 > 0$). Trong quá trình nắm giữ, các nhà quản lý rủi ro phải đối mặt với hiện tượng trôi dạt rủi ro (risk drift): theo thời gian hướng về ngày đáo hạn, độ nhạy cảm PVBP của cả hai chân đều suy giảm, nhưng chân có kỳ hạn ngắn hơn sẽ có tốc độ suy giảm thời lượng tương đối nhanh hơn chân dài [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]]. Do đó, tỷ lệ phòng hộ ban đầu sẽ bị phá vỡ, đòi hỏi danh mục phải được tái cân bằng liên tục hoặc phải được định lượng bằng giá trị PVBP kỳ hạn (forward PVBP) phù hợp với chân trời nắm giữ dự kiến (fixed_income_during, Ch.31, Sec.31.1.2, d.90). Ngoài ra, chuỗi dữ liệu chênh lệch lợi suất chuẩn thường chịu các bước nhảy gián đoạn kỹ thuật do sự kiện thay đổi mã trái phiếu chuẩn phát hành mới (benchmark switch jump) [[par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities]], gây ra các tín hiệu giả mạo về sự làm dốc hoặc làm phẳng của đường cong (fixed_income_during, Ch.31, Sec.31.1.2, d.72–78).

Mặc dù Steepeners và Flatteners về mặt toán học là các cấu trúc giao dịch tuyến tính hoàn toàn, hành vi thị trường thực tế có thể tạo ra các đặc tính phi tuyến tính (non-linear behavior) có giá trị kinh tế lớn (fixed_income_during, Ch.31, Sec.31.1.2, d.98–101). Minh chứng kinh điển xuất hiện trên thị trường trái phiếu chính phủ Nhật Bản (JGB) trong mối quan hệ giữa lợi suất 10 năm và 30 năm giai đoạn 2010–2015: đồ thị phân tán bộc lộ một điểm gãy rõ nét (pivot point) tại ngưỡng lợi suất 2% của kỳ hạn 30 năm. Hiện tượng này bắt nguồn từ môi trường ưa thích quy định (preferred habitat) của các công ty bảo hiểm nhân thọ Nhật Bản: do các cam kết nghĩa vụ chi trả hợp đồng bảo hiểm quá khứ yêu cầu tỷ suất sinh lời tối thiểu cố định quanh 2%, các công ty bảo hiểm sẽ tung dòng tiền khổng lồ mua chặn đáy bất kỳ khi nào lợi suất 30 năm vượt ngưỡng 2% [[institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity]]. Lực cầu hấp thụ cưỡng bức này đã neo chặt đầu dài của đường cong, biến một chiến lược giao dịch tuyến tính đơn giản thành một vị thế có cấu trúc thanh toán bất đối xứng tương đương một quyền chọn (option-like payoff) tại vùng điểm gãy, mở ra cơ hội kinh doanh chênh lệch giá có tỷ lệ sinh lời trên rủi ro vượt trội trước khi bước sang các cấu trúc phức tạp hơn như Butterfly [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]].

Tại Chương 12, Moorad Choudhry bổ sung khung quản trị giao dịch thực chiến cho các chiến lược Steepeners và Flatteners, cụ thể hóa quy tắc cân bằng tỷ số BPV ($N_1 = N_2 \cdot BPV_2 / BPV_1$) để triệt tiêu hoàn toàn rủi ro định hướng bậc một (choudhry_analysing_yield_curve, Ch.12, d.4901–4925). Choudhry nhấn mạnh kỷ luật giao dịch bắt buộc phải phối hợp ba thành tố: (1) Mục tiêu chênh lệch chốt lời xác định, (2) Khung thời gian nắm giữ cố định (bắt buộc tất toán khi hết thời hạn dù chưa đạt mục tiêu), và (3) Ngưỡng dừng lỗ (stop-loss) kích hoạt chính xác tại 50% biên độ mục tiêu lợi nhuận khi spread đảo chiều ngược kỳ vọng [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]]. Đồng thời, điểm hòa vốn thực tế của toàn bộ vị thế chịu sự chi phối quyết định bởi chi phí tài trợ repo và rủi ro lãi suất đặc biệt (specialness) phát sinh từ chân bán khống [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]].
