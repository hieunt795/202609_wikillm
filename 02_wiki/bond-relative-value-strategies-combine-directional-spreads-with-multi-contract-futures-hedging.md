---
title: bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging
type: concept
tags:
  - trading
  - bond-trading
  - relative-value
  - basis-trade
  - futures-hedging
  - spread-widener
  - spread-tightener
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Các chiến lược giá trị tương đối trái phiếu (bond relative value strategies) là các cấu trúc giao dịch được thiết lập nhằm thu lợi nhuận từ sự hội tụ hoặc phân kỳ giá cả giữa các trái phiếu cụ thể mà không chịu rủi ro định hướng từ sự dịch chuyển của toàn bộ mặt bằng lãi suất [[bond-relative-value-metrics-select-reference-curves-aligned-with-instrument-hedging-practices]]. Chiến lược cơ bản nhất là nới rộng chênh lệch (Spread Widener) và thu hẹp chênh lệch (Spread Tightener) so với đường cong tham chiếu (fixed_income_during, Ch.32, Sec.32.2.1, d.34–47). Theo quy ước vị thế nhất quán theo rủi ro trái phiếu, chiến lược Spread Widener bao gồm việc bán khống trái phiếu và nhận lãi suất cố định trên đường cong hoán đổi (thực hiện qua asset swap hoặc swap nội suy), phản ánh kỳ vọng trái phiếu sẽ kém hiệu quả hơn so với đường cong; ngược lại, Spread Tightener bao gồm việc mua trái phiếu và trả lãi suất cố định trên đường cong swap. Đối với các nhà quản lý quỹ theo chỉ số chuẩn (benchmark index tracking), chiến lược Spread Widener tương đương với việc hạ tỷ trọng (underweight) trái phiếu đó trong danh mục, còn Spread Tightener tương đương với việc nâng tỷ trọng (overweight).

Khi muốn tối ưu hóa chi phí vốn và tận dụng thanh khoản vượt trội, các nhà giao dịch thay thế việc giao dịch hoán đổi bằng hợp đồng tương lai để thực hiện giao dịch chênh lệch giá cơ sở (Basis Trade) (fixed_income_during, Ch.32, Sec.32.2.2, d.48–67). Trong một vị thế Short Basis, nhà giao dịch bán khống trái phiếu giao ngay và mua hợp đồng tương lai với tỷ trọng trung hòa rủi ro thời lượng ($N_B \text{PVBP}_B + N_F \text{PVBP}_F = 0$) [[bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships]]. Do vị thế được miễn nhiễm hoàn toàn rủi ro thời lượng (DV01-neutral), các đại lý tạo lập thị trường có thể chào giá với mức chênh lệch bid-offer cực mỏng.

Tuy nhiên, nếu kỳ hạn của trái phiếu lệch đáng kể so với kỳ hạn của trái phiếu rẻ nhất để giao nộp (CTD) của hợp đồng tương lai, giao dịch sẽ bị phơi nhiễm trước rủi ro độ dốc của đường cong lợi suất [[steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks]]. Để triệt tiêu rủi ro này, các nhà giao dịch áp dụng kỹ thuật kẹp hai hợp đồng tương lai đa kỳ hạn (two-contract futures hedge) theo mô hình khoảng cách kỳ hạn tuyến tính (fixed_income_during, Ch.32, Sec.32.2.2, d.62–67):

$$\frac{N_{F1} \text{PVBP}_{F1}}{|m_B - m_{F2}|} = \frac{N_{F2} \text{PVBP}_{F2}}{|m_B - m_{F1}|}$$

Hợp đồng tương lai có kỳ hạn CTD nằm gần trái phiếu hơn sẽ được phân bổ tỷ trọng rủi ro cao hơn, hình thành một thế kẹp Butterfly trung hòa rủi ro đường cong hoàn chỉnh [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]].

Khi thực hiện giao dịch chênh lệch giữa hai trái phiếu tiền mặt có kỳ hạn cách xa nhau (Bond Spread), vị thế sẽ chịu rủi ro làm dốc hoặc làm phẳng của đường cong chung (fixed_income_during, Ch.32, Sec.32.2.3–32.2.4, d.68–99). Nhằm cô lập thuần túy rủi ro định giá tương đối của hai trái phiếu, nhà giao dịch thiết lập cấu trúc chênh lệch trái phiếu có phòng hộ đường cong (curve-hedged bond spread) bằng cách kết hợp hai trái phiếu với hai hợp đồng tương lai (hoặc hai trái phiếu chuẩn on-the-run thanh khoản cao). Cấu trúc bốn chân này đòi hỏi giải hệ ba phương trình độc lập để vừa triệt tiêu rủi ro thời lượng tổng thể, vừa bảo đảm rủi ro độ dốc trên cặp trái phiếu được triệt tiêu chính xác bằng rủi ro độ dốc đối ứng trên cặp hợp đồng tương lai (fixed_income_during, Ch.32, Sec.32.2.4, d.92–95).

Mặc dù việc bổ sung các công cụ phái sinh giúp vô hiệu hóa rủi ro vĩ mô, nhà giao dịch luôn phải ý thức về rủi ro cơ sở tồn dư (residual basis risk), chẳng hạn như việc dùng hợp đồng tương lai Bund của Đức để phòng hộ chênh lệch trái phiếu chính phủ Hà Lan vẫn tiềm ẩn rủi ro phân kỳ độ dốc giữa hai quốc gia (fixed_income_during, Ch.32, Sec.32.2.4, d.96–98). Trong quản trị giao dịch chủ động, tính đơn giản luôn là một phẩm chất tối thượng (simplicity is a virtue): một cấu trúc giao dịch bị thiết kế quá phức tạp với quá nhiều chân hợp đồng sẽ đòi hỏi chi phí tái cân bằng khổng lồ và làm mờ nhạt khả năng bóc tách hiệu quả đóng góp danh mục (performance attribution) [[fixed-income-trade-governance-balances-probabilistic-stop-loss-and-epistemological-consistency]].
