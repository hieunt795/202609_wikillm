---
title: standardised-delta-eve-calculation-and-multi-currency-aggregation-rules
type: concept
tags: [banking, alm, irrbb, delta-eve, discount-factors, multi-currency-aggregation, standardised-framework, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Thuật toán tính toán $\Delta EVE$ chuẩn hóa và quy tắc tổng hợp đa tiền tệ (Standardised Delta EVE Calculation and Multi-Currency Aggregation Rules) thiết lập hệ thống công thức toán học chiết khấu dòng tiền liên tục, tích hợp phần bù rủi ro quyền chọn tự động ($KAO_{i,c}$) và cơ chế tổng hợp rủi ro giữa các đồng tiền trọng yếu trong Khung đo lường chuẩn hóa IRRBB của Ủy ban Basel nhằm xác định mức sụt giảm giá trị kinh tế tối đa của vốn chủ sở hữu ($\Delta EVE_{\text{standardised}}$) (bcbs_368, file d368.md, Section IV.6, d.767–800; Paragraph 132).

Thuật toán chuẩn hóa là giai đoạn tổng hợp cuối cùng (Giai đoạn 3, 4 và 5 của Khung chuẩn hóa), nơi toàn bộ dữ liệu dòng tiền định giá lại từ 19 dải kỳ hạn, các tham số hành vi NMDs, CPR, TDRR và định giá quyền chọn tự động được quy đổi thành một con số tổn thất giá trị kinh tế duy nhất mang tính so sánh tuyệt đối giữa các ngân hàng.

**1. Bù trừ dòng tiền ròng nội dải và phạm vi đồng tiền trọng yếu**

Quy trình tính toán được thực hiện độc lập cho từng đồng tiền trọng yếu (material currencies) — được định nghĩa là các đồng tiền chiếm từ **$5\%$ trở lên** tổng tài sản hoặc tổng nợ phải trả trên sổ ngân hàng (Paragraph 132, d.769–770):
- Tại mỗi dải kỳ hạn $k \in \{1,\dots,19\}$ với tọa độ điểm giữa $t_k$, toàn bộ các dòng tiền định giá lại danh nghĩa dương (dòng tiền thu từ tài sản) và âm (dòng tiền chi trả nợ) phát sinh dưới kịch bản sốc $i$ được bù trừ hoàn hảo để tạo thành dòng tiền định giá lại ròng duy nhất (Paragraph 132.1, d.770–771):

$$CF_{i,c}(t_k) = \sum \text{Dòng tiền tài sản}_{i,c}(t_k) - \sum \text{Dòng tiền nợ}_{i,c}(t_k) + \sum \text{Dòng tiền phái sinh ròng}_{i,c}(t_k)$$

- Các phần dòng tiền bị triệt tiêu thông qua bù trừ được loại bỏ khỏi tính toán. Dòng tiền ròng $CF_{i,c}(t_k)$ có thể mang giá trị dương (trạng thái trường / long position) hoặc âm (trạng thái đoản / short position).

**2. Hệ số chiết khấu liên tục và xác định $EVE$ cơ sở loại trừ quyền chọn**

Dòng tiền ròng tại mỗi điểm giữa $t_k$ được chiết khấu về giá trị hiện tại thông qua hệ số chiết khấu lãi kép liên tục (Continuously compounded discount factor) (Paragraph 132.2, d.771–776):

$$DF_{i,c}(t_k) = \exp\left( - R_{i,c}(t_k) \cdot t_k \right)$$

Trong đó:
- $t_k$ là tọa độ thời gian tính bằng năm của điểm giữa dải kỳ hạn $k$ quy định tại Bảng 1 (ví dụ $t_1 = 0{,}0028$, $t_6 = 0{,}875$, $t_{19} = 25{,}0$);
- $R_{i,c}(t_k)$ là lãi suất zero-coupon phi rủi ro liên tục tương ứng với kỳ hạn $t_k$ theo đồng tiền $c$ dưới kịch bản sốc lãi suất $i$ quy định tại Annex 2 (với $i=0$ đại diện cho đường cong lãi suất phi rủi ro hiện hành tại ngày định giá);
- *Nguyên tắc nhất quán về biên độ thương mại*: Đường cong chiết khấu phải đại diện cho lãi suất zero-coupon phi rủi ro (như đường cong hoán đổi lãi suất có bảo đảm OIS/Secured swap curve - Footnote 29). Nếu ngân hàng giữ lại biên độ thương mại và các thành tố spread trong dòng tiền, đường cong chiết khấu $R_{i,c}(t_k)$ bắt buộc phải được cộng thêm biên độ thương mại và spread tương ứng nhằm bảo đảm tính nhất quán tài chính (Paragraph 132.2).

Giá trị kinh tế của vốn chủ sở hữu loại trừ quyền chọn tự động dưới kịch bản $i$ ($EVE_{i,c}^{no}$) được tính bằng tổng giá trị hiện tại của các dòng tiền ròng trên toàn bộ 19 dải kỳ hạn (Paragraph 132.3, d.777–780):

$$EVE_{i,c}^{no} = \sum_{k=1}^{19} CF_{i,c}(t_k) \cdot DF_{i,c}(t_k) = \sum_{k=1}^{19} CF_{i,c}(t_k) \cdot \exp\left( - R_{i,c}(t_k) \cdot t_k \right)$$

Tại trạng thái ban đầu ($i=0$), giá trị kinh tế hiện hành được xác định tương tự:

$$EVE_{0,c}^{no} = \sum_{k=1}^{19} CF_{0,c}(t_k) \cdot \exp\left( - R_{0,c}(t_k) \cdot t_k \right)$$

**3. Tích hợp phần bù rủi ro quyền chọn tự động $KAO_{i,c}$**

Biến thiên toàn phần của giá trị kinh tế vốn chủ sở hữu theo đồng tiền $c$ dưới kịch bản sốc $i$ ($\Delta EVE_{i,c}$) được xác định bằng cách lấy mức sụt giảm giá trị hiện tại của dòng tiền cơ sở cộng gộp với phần bù tổn thất quyền chọn tự động $KAO_{i,c}$ từ Giai đoạn 4 (Paragraph 132.4, d.789–794):

$$\Delta EVE_{i,c} = EVE_{0,c}^{no} - EVE_{i,c}^{no} + KAO_{i,c}$$

Trong đó $KAO_{i,c} = \sum_{o} \Delta FVAO_{i,c}^o - \sum_{q} \Delta FVAO_{i,c}^q$ đại diện cho tổn thất phát sinh từ việc tái định giá toàn diện các quyền chọn bán và quyền chọn mua phòng hộ dưới cú sốc đường cong lãi suất và cú sốc tăng tương đối $+25\%$ độ biến động ngầm định ($\Delta \sigma / \sigma = +25\%$) theo [[automatic-interest-rate-options-standardised-valuation-and-volatility-shocks]].
- Một giá trị $\Delta EVE_{i,c} > 0$ biểu thị **mức sụt giảm (loss)** trong giá trị kinh tế của vốn chủ sở hữu;
- Một giá trị $\Delta EVE_{i,c} < 0$ biểu thị **mức gia tăng (gain)** trong giá trị kinh tế.

**4. Quy tắc tổng hợp đa tiền tệ (Multi-currency aggregation rules)**

Ủy ban Basel thiết lập quy tắc tổng hợp chuẩn tắc trên toàn bộ các đồng tiền cho từng kịch bản sốc lãi suất $i$ (Paragraph 132.5, d.795–798):

$$\Delta EVE_i = \max\left( 0, \sum_{c} \Delta EVE_{i,c} \right)$$

Quy tắc chuẩn tắc này cho phép bù trừ giữa các đồng tiền có mức tăng giá trị ($\Delta EVE_{i,c_1} < 0$) với các đồng tiền chịu tổn thất ($\Delta EVE_{i,c_2} > 0$) trong cùng một kịch bản sốc vĩ mô toàn cầu $i$, nhưng nếu tổng thể toàn ngân hàng ghi nhận mức tăng ròng thì tổn thất chung của kịch bản đó được ấn định bằng $0$ (ngân hàng không được ghi nhận lãi vào vốn rủi ro).

*Thẩm quyền giám sát thận trọng quốc gia (National Supervisory Discretion)*:
Để phòng ngừa hiện tượng đứt gãy tương quan chéo (cross-currency correlation breakdown) trong khủng hoảng, cơ quan giám sát quốc gia có toàn quyền pháp lý áp đặt phương pháp tổng hợp bảo thủ không cho phép bù trừ quyền lợi giữa các đồng tiền (Footnote 30, d.799):

$$\Delta EVE_i = \sum_{c} \max\left( 0, \Delta EVE_{i,c} \right)$$

Theo quy tắc thận trọng này, mọi khoản lãi phát sinh tại các đồng tiền riêng lẻ đều bị triệt tiêu về $0$, và tổng rủi ro của ngân hàng dưới kịch bản $i$ là tổng số học tuyệt đối của các khoản sụt giảm vốn trên mọi đồng tiền có tổn thất.

**5. Xác định thước đo rủi ro EVE chuẩn hóa tối đa**

Thước đo rủi ro EVE chuẩn hóa tổng thể ($\Delta EVE_{\text{standardised}}$) của ngân hàng được xác định bằng tổn thất lớn nhất trên toàn bộ 6 kịch bản sốc lãi suất chuẩn hóa của Annex 2 (Paragraph 132.5, d.795–798):

$$\Delta EVE_{\text{standardised}} = \max_{i \in \{1,\dots,6\}} \Delta EVE_i$$

Chỉ số $\Delta EVE_{\text{standardised}}$ này là căn cứ tối cao để:
1. Đối chiếu với ngưỡng $15\%$ Vốn cấp 1 trong Bài kiểm tra tổ chức ngoại lai giám sát theo [[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]];
2. Kích hoạt 4 chế tài can thiệp sớm của cơ quan giám sát theo [[supervisory-remedial-actions-mandate-exposure-reduction-capital-add-ons-and-parameter-constraints]];
3. Công bố thông tin bắt buộc tại Bảng B Trụ cột 3 theo [[pillar-3-irrbb-quantitative-disclosure-standards-mandate-table-b-metrics]].
