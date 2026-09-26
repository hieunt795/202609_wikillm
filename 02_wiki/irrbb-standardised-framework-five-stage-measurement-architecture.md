---
title: irrbb-standardised-framework-five-stage-measurement-architecture
type: concept
tags: [banking, alm, irrbb, standardised-framework, eve, bcbs-368, regulatory-capital, interest-rate-shocks]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Khung đo lường chuẩn hóa rủi ro lãi suất trên sổ ngân hàng (IRRBB Standardised Framework) thiết lập quy trình tính toán 5 giai đoạn (five-stage measurement architecture) mang tính định lượng chuẩn tắc nhằm đo lường mức độ sụt giảm giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) dưới 6 kịch bản sốc lãi suất giám sát, đóng vai trò là khuôn khổ dự phòng bắt buộc do cơ quan giám sát chỉ định hoặc do ngân hàng chủ động lựa chọn áp dụng (bcbs_368, file d368.md, Section IV.1, d.536–556; Paragraph 99–100).

Khung chuẩn hóa được Ủy ban Basel ban hành nhằm khắc phục tính thiếu so sánh và rủi ro mô hình tiềm ẩn trong các hệ thống đo lường nội bộ (IMS) của các tổ chức tín dụng. Không giống như phương pháp nội bộ cho phép ngân hàng tự do đặt giả định hành vi, Khung chuẩn hóa quy định cứng nhắc các quy tắc phân nhóm công cụ tài chính, trần tham số hóa hành vi khách hàng, quy tắc slotting 19 dải kỳ hạn và thuật toán tổng hợp rủi ro đa tiền tệ.

**Giai đoạn 1: Phân loại vị thế sổ ngân hàng theo khả năng chuẩn hóa (Stage 1 - Categorisation of positions)**

Toàn bộ các tài sản, nợ phải trả và cam kết ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng (loại trừ tài sản cố định, đầu tư cổ phần và các khoản khấu trừ Vốn cấp 1 CET1) được phân bổ vào 3 nhóm nghiệp vụ dựa trên tính chất hợp đồng và mức độ chuẩn hóa (bcbs_368, file d368.md, Section IV.1–2.2, d.543–545, d.601–617; Paragraph 100, 105–109):
- *Nhóm đáp ứng chuẩn hóa (Amenable to standardisation)*: Bao gồm các công cụ có dòng tiền hợp đồng xác định chắc chắn (khoản vay lãi suất cố định không có rủi ro trả nợ trước hạn, chứng khoán nợ coupon cố định, tiền gửi có kỳ hạn không có quyền rút trước hạn) hoặc công cụ lãi suất thả nổi thuần túy tự động định giá lại theo chỉ số tham chiếu thị trường. Đối với các công cụ có đính kèm quyền chọn lãi suất tự động (như trần sàn cap/floor trong hợp đồng vay thế chấp thả nổi, hoặc trái phiếu có điều khoản mua lại callable bonds), quyền chọn ngầm định phải được bóc tách riêng (stripped out) sang Giai đoạn 4, phần hợp đồng cơ sở (host contract) tiếp tục được giữ lại ở nhóm đáp ứng chuẩn hóa (bcbs_368, file d368.md, Paragraph 107 & Footnote 14, 15, d.573–574, 608, 626).
- *Nhóm kém đáp ứng chuẩn hóa (Less amenable to standardisation)*: Bao gồm các quyền chọn lãi suất tự động rõ ràng (explicit automatic interest rate options như swaptions, caps, floors độc lập) và các quyền chọn ngầm định đã bóc tách từ các hợp đồng cơ sở. Các vị thế này bị loại khỏi quy trình slotting dòng tiền thông thường và chuyển sang định giá lại độc lập tại Giai đoạn 4.
- *Nhóm không đáp ứng chuẩn hóa (Not amenable to standardisation)*: Bao gồm 3 danh mục sản phẩm mang tính chất quyền chọn hành vi phi tuyến tính của khách hàng bán lẻ: (i) Tiền gửi không kỳ hạn (NMDs); (ii) Khoản vay lãi suất cố định chịu rủi ro trả nợ trước hạn không bồi hoàn (prepayment risk); và (iii) Tiền gửi có kỳ hạn chịu rủi ro rút tiền trước hạn (early redemption risk) (bcbs_368, file d368.md, Paragraph 109, d.616). Các vị thế hành vi của khách hàng bán buôn không được xếp vào nhóm này mà bắt buộc phải coi là quyền chọn tự động bất lợi nhất.

**Giai đoạn 2: Phân bổ dòng tiền định giá lại danh nghĩa vào 19 dải kỳ hạn (Stage 2 - Cash flow slotting)**

Mọi dòng tiền định giá lại danh nghĩa ($CF(k)$ hoặc $CF(t_k)$) — bao gồm hoàn trả nợ gốc, định giá lại gốc và các khoản thanh toán lãi coupon — được ánh xạ vào lịch 19 dải kỳ hạn chuẩn hóa (Table 1) từ dải qua đêm ($0{,}0028$ năm) đến trên 20 năm ($25$ năm) (bcbs_368, file d368.md, Section IV.2.1, d.559–596; Paragraph 101–104):
- *Vị thế cố định và thả nổi thuần*: Dòng tiền cố định phân bổ vào dải kỳ hạn theo ngày đáo hạn hợp đồng; công cụ thả nổi được phân bổ toàn bộ nợ gốc vào dải kỳ hạn rơi vào ngày định giá lại kế tiếp (next repricing date), phản ánh việc giá trị thị trường của nợ gốc được tái thiết lập về mệnh giá (par value) (bcbs_368, file d368.md, Paragraph 106, d.603–607).
- *Xử lý tiền gửi không kỳ hạn (NMDs)*: Dựa trên chuỗi số liệu 10 năm, ngân hàng bóc tách thành phần phi lõi (non-core) ấn định hoàn toàn vào dải qua đêm ($k=1$), và phần lõi (core) được phân bổ vào các dải kỳ hạn tuân thủ trần tỷ trọng tối đa ($90\%$ cho bán lẻ giao dịch, $70\%$ cho bán lẻ phi giao dịch, $50\%$ cho bán buôn) và trần kỳ hạn bình quân tối đa ($5$ năm, $4{,}5$ năm, $4$ năm) theo Bảng 2 chuẩn hóa (bcbs_368, file d368.md, Section IV.3, d.618–652).
- *Mô hình hóa quyền chọn hành vi bán lẻ*: Tỷ lệ trả nợ trước hạn ($CPR_{i,c}^p$) và tỷ lệ rút tiền gửi sớm ($TDRR_{i,c}^p$) được điều chỉnh theo kịch bản sốc lãi suất thông qua hệ số nhân chuẩn hóa $\gamma_i$ (Bảng 3) và $u_i$ (Bảng 4). Dòng tiền rút trước hạn của tiền gửi có kỳ hạn bị dồn toàn bộ vào dải qua đêm (bcbs_368, file d368.md, Section IV.4, d.653–738).
- *Tách biên thương mại*: Ngân hàng có quyền lựa chọn khấu trừ biên độ thương mại (commercial margin/spread) khỏi dòng tiền định giá lại theo phương pháp nhất quán và minh bạch.

**Giai đoạn 3: Xác định biến thiên EVE theo từng đồng tiền (Stage 3 - Determination of Delta EVE per currency)**

Tại mỗi dải kỳ hạn $k \in \{1,\dots,19\}$, toàn bộ dòng tiền thu và dòng tiền chi được bù trừ ròng để tạo thành dòng tiền định giá lại ròng $CF_{i,c}(t_k)$. Dòng tiền ròng được chiết khấu theo công thức lãi kép liên tục bằng đường cong lãi suất phi rủi ro sau sốc $R_{i,c}(t_k)$ (hoặc đường cong phi rủi ro cộng spread nếu dòng tiền bao gồm biên thương mại) để xác định giá trị kinh tế của vốn chủ sở hữu loại trừ quyền chọn tự động ($EVE_{i,c}^{no}$) (bcbs_368, file d368.md, Section IV.6, d.769–786; Paragraph 132):

$$EVE_{i,c}^{no} = \sum_{k=1}^{19} CF_{i,c}(t_k) \cdot \exp\left( - R_{i,c}(t_k) \cdot t_k \right)$$

Mức sụt giảm giá trị kinh tế cơ sở cho từng đồng tiền trọng yếu (chiếm trên $5\%$ tổng tài sản hoặc nợ sổ ngân hàng) được đo lường qua chênh lệch so với đường cong hiện hành: $\Delta EVE_{i,c}^{no} = EVE_{0,c}^{no} - EVE_{i,c}^{no}$ dưới 6 kịch bản sốc lãi suất chuẩn hóa (Parallel up, Parallel down, Steepener, Flattener, Short rate up, Short rate down) quy định tại Annex 2.

**Giai đoạn 4: Tính toán phần bù rủi ro quyền chọn tự động (Stage 4 - Add-ons for automatic interest rate options)**

Các quyền chọn lãi suất tự động bán (sold options) và quyền chọn mua dùng cho phòng hộ (bought hedging options) phải trải qua quy trình tái định giá toàn diện (full revaluation) dưới từng kịch bản sốc lãi suất $i$ kết hợp với một cú sốc gia tăng tương đối $+25\%$ đối với độ biến động ngầm định ($\Delta \sigma / \sigma = +25\%$) (bcbs_368, file d368.md, Section IV.5, d.739–766; Paragraph 130):

$$KAO_{i,c} = \sum_{o=1}^{n_c} \Delta FVAO_{i,c}^o - \sum_{q=1}^{m_c} \Delta FVAO_{i,c}^q$$

Trong đó $\Delta FVAO_{i,c}^o$ là biến động giá trị của quyền chọn bán đối với chủ sở hữu quyền chọn giữa trạng thái sốc kép $(R_{i,c}, 1{,}25 \cdot \sigma_0)$ và trạng thái đường cong ban đầu $(R_{0,c}, \sigma_0)$. Biến số $KAO_{i,c}$ lượng hóa rủi ro phi tuyến tính và rủi ro biến động (vega risk) mà các phép xấp xỉ thời lượng (duration-based approximations) không thể phản ánh.

**Giai đoạn 5: Tổng hợp rủi ro đa tiền tệ và xác định thước đo tổn thất EVE tối đa (Stage 5 - IRRBB EVE aggregation)**

Biến thiên tổng thể của giá trị kinh tế cho từng đồng tiền $c$ dưới kịch bản sốc $i$ được xác định bằng cách cộng gộp tổn thất dòng tiền ròng và phần bù rủi ro quyền chọn (bcbs_368, file d368.md, Section IV.6, d.789–799; Paragraph 132.4–5):

$$\Delta EVE_{i,c} = EVE_{0,c}^{no} - EVE_{i,c}^{no} + KAO_{i,c}$$

Tổn thất trên toàn bộ các đồng tiền được tổng hợp theo nguyên tắc chuẩn tắc của Basel:

$$\Delta EVE_i = \max\left( 0, \sum_{c} \Delta EVE_{i,c} \right) \quad \text{hoặc quy tắc bảo thủ giám sát:} \quad \Delta EVE_i = \sum_{c} \max\left( 0, \Delta EVE_{i,c} \right)$$

Đại lượng rủi ro EVE chuẩn hóa cuối cùng của ngân hàng ($\Delta EVE_{\text{standardised}}$) là mức sụt giảm giá trị kinh tế lớn nhất trên toàn bộ 6 kịch bản sốc lãi suất:

$$\Delta EVE_{\text{standardised}} = \max_{i \in \{1,\dots,6\}} \Delta EVE_i$$

Kết quả tính toán này được sử dụng trực tiếp để đối chiếu với Bài kiểm tra tổ chức ngoại lai giám sát (Supervisory Outlier Test - ngưỡng $15\%$ Vốn cấp 1 theo Principle 12), công bố thông tin minh bạch tại Bảng B Trụ cột 3, và làm căn cứ áp đặt đệm vốn bổ sung Trụ cột 2 nếu hệ thống đo lường nội bộ của ngân hàng không đạt chuẩn.

Quy trình 5 giai đoạn này liên kết trực tiếp với các chuẩn mực kỹ thuật chi tiết: [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]] lượng hóa việc phân bổ dòng tiền Giai đoạn 2, [[standardised-nmd-categorisation-and-core-deposit-caps-framework]] khống chế tham số tiền gửi không kỳ hạn, [[standardised-loan-prepayment-modelling-and-cpr-multipliers]] và [[standardised-term-deposit-early-redemption-risk-and-tdrr-scalars]] mô hình hóa hành vi khách hàng, [[automatic-interest-rate-options-standardised-valuation-and-volatility-shocks]] định hình Giai đoạn 4, và [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]] hoàn thiện thuật toán tổng hợp Giai đoạn 5.
