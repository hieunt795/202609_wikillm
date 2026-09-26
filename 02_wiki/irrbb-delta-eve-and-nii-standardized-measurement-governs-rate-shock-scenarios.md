---
title: irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios
type: concept
tags: [banking, alm, irrbb, delta-eve, delta-nii, interest-rate-shocks, bcbs-d578, cash-flow-discounting, regulation]
sources: [sbv_circular_83_2025, bcbs_368]
status: stable
last_updated: 2026-09-26
---

Phương pháp đo lường chuẩn hóa rủi ro lãi suất trên sổ ngân hàng (Interest Rate Risk in the Banking Book - IRRBB Standardised Measurement) thiết lập thuật toán định lượng độ nhạy kép của toàn bộ bảng cân đối tài chính ngân hàng thông qua hai thước đo bổ trợ: Thay đổi giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) và Thay đổi thu nhập lãi thuần ($\Delta NII$) dưới các kịch bản sốc lãi suất đồng bộ (sbv_circular_83_2025, file TT83.md, Điều 53–55, d.926–954; Phụ lục V, d.1564–1844; nguyên bản chuẩn tắc quốc tế tại bcbs_368, file d368.md, Section IV, d.536–800, Paragraph 99–132). Khung chuẩn hóa này vận hành theo quy trình 5 giai đoạn chặt chẽ được phân tích tại [[irrbb-standardised-framework-five-stage-measurement-architecture]].

**1. Phân nhóm tài sản, nợ phải trả và ngoại bảng nhạy cảm lãi suất**

Quy trình lượng hóa $\Delta EVE$ bắt đầu từ việc rà soát và phân loại các công cụ tài chính nhạy cảm lãi suất thành 3 nhóm kỹ thuật theo mức độ chuẩn hóa (sbv_circular_83_2025, file TT83.md, Phụ lục V.A.I, d.1574–1597):
- **Khoản mục loại trừ**: Tài sản cố định, các khoản đầu tư vốn chủ sở hữu trên sổ ngân hàng (Equity exposures in the banking book) và các khoản giảm trừ khỏi Vốn lõi Cấp 1 (CET1) không được tính vào tài sản nhạy cảm lãi suất. Ngược lại, tiền gửi không hưởng lãi (Non-remunerated deposits) bắt buộc phải đưa vào nợ phải trả nhạy cảm lãi suất.
- **Nhóm 1 - Đáp ứng đủ tiêu chuẩn (Amenable to standardisation)**: Bao gồm các tài sản, nợ và ngoại bảng có lãi suất cố định hoặc lãi suất thả nổi thuần túy. Đối với các hợp đồng có đính kèm quyền chọn lãi suất (embedded options), ngân hàng bóc tách riêng phần quyền chọn sang nhóm 2 và chỉ giữ phần dòng tiền cơ sở tại nhóm 1.
- **Nhóm 2 - Chưa đáp ứng đủ tiêu chuẩn (Less amenable to standardisation)**: Bao gồm các quyền chọn lãi suất tự động (Automatic interest rate options - ví dụ như trần/sàn lãi suất cap/floor, swaptions). Dòng tiền của nhóm này không phân bổ vào thang kỳ hạn chuẩn mà được định giá riêng biệt bằng mô hình định giá quyền chọn ($KAO_{i,c}$).
- **Nhóm 3 - Không đáp ứng đủ tiêu chuẩn (Not amenable to standardisation)**: Bao gồm 3 cấu phần mang tính chất rủi ro hành vi của khách hàng đòi hỏi mô hình hóa phi tuyến tính:
  1. Tiền gửi không kỳ hạn (Non-Maturity Deposits - NMDs);
  2. Khoản cho vay lãi suất cố định có rủi ro trả nợ trước hạn (Fixed rate loans subject to prepayment risk);
  3. Khoản tiền gửi có kỳ hạn có rủi ro rút trước hạn (Term deposits subject to early redemption risk).

**2. Khung 19 thang kỳ hạn chuẩn và mô hình hóa tiền gửi không kỳ hạn (NMDs)**

Dòng tiền định giá lại danh nghĩa trong tương lai (Notional repricing cash flows - gồm trả gốc, lãi và định giá lại lãi suất) được phân bổ vào 19 thang kỳ hạn chuẩn hóa hoặc điểm giữa của thang kỳ hạn ($t_k$) từ qua đêm (0,0028 năm) đến trên 20 năm (25 năm). Khi phân bổ vào điểm giữa thang kỳ hạn, ngân hàng thực hiện chia nhỏ (splitting up) dòng tiền giữa hai điểm giữa liền kề để bảo toàn kỳ hạn bình quân (sbv_circular_83_2025, file TT83.md, Phụ lục V.A.II, d.1598–1638).

Đối với tiền gửi không kỳ hạn (NMDs), ngân hàng phân tách thành NMDs cá nhân (tài khoản giao dịch vs. tài khoản không giao dịch) và NMDs tổ chức. Dựa trên chuỗi dữ liệu lịch sử, ngân hàng tách thành NMDs không ổn định (phân bổ ngay vào thang kỳ hạn qua đêm) và NMDs ổn định. Từ NMDs ổn định, ngân hàng xác định **NMDs lõi (Core deposits)** - phần tiền gửi gần như không bị định giá lại ngay cả khi lãi suất thị trường biến động mạnh. Tỷ trọng và kỳ hạn trung bình của NMDs lõi bị khống chế nghiêm ngặt bởi các mức trần kỹ thuật (sbv_circular_83_2025, file TT83.md, Phụ lục V.A.II.3.a, d.1639–1660):
- **Cá nhân - Tài khoản giao dịch**: Tỷ trọng NMDs lõi tối đa **90%** tổng NMDs giao dịch cá nhân; Kỳ hạn trung bình trần tối đa **5,0 năm**.
- **Cá nhân - Tài khoản không giao dịch**: Tỷ trọng NMDs lõi tối đa **70%**; Kỳ hạn trung bình trần tối đa **4,5 năm**.
- **Tổ chức**: Tỷ trọng NMDs lõi tối đa **50%** tổng NMDs tổ chức; Kỳ hạn trung bình trần tối đa **4,0 năm**.

**3. Mô hình hóa rủi ro hành vi khách hàng: Trả trước (CPR) và Rút trước hạn (TDRR)**

Hành vi tài chính của khách hàng cá nhân được mô hình hóa động theo từng kịch bản cú sốc lãi suất $i$ thông qua các hệ số nhân tác động lên tỷ lệ cơ sở (sbv_circular_83_2025, file TT83.md, Phụ lục V.A.II.3.b–c, d.1661–1718):
- **Tỷ lệ trả trước hạn có điều kiện (Conditional Prepayment Rate - CPR)** của danh mục cho vay cá nhân lãi suất cố định:

$$CPR_{i,c}^p = CPR_{0,c}^p \times \gamma_i$$

Hệ số nhân $\gamma_i$: Khi lãi suất thị trường tăng (kịch bản tăng song song, dốc, tăng ngắn hạn), động lực trả nợ trước hạn để tái tài trợ giảm đi $\rightarrow \gamma_i = 0{,}8$. Khi lãi suất thị trường giảm (kịch bản giảm song song, phẳng, giảm ngắn hạn), người vay có xu hướng trả nợ trước hạn để vay mới lãi suất thấp hơn $\rightarrow \gamma_i = 1{,}2$.
- **Tỷ lệ rút tiền gửi trước hạn (Term Deposit Redemption Ratio - TDRR)** của khách hàng cá nhân:

$$TDRR_{i,c}^p = TDRR_{0,c}^p \times u_i$$

Hệ số nhân $u_i$: Khi lãi suất thị trường tăng (kịch bản tăng song song, phẳng, tăng ngắn hạn), người gửi tiền có xu hướng tất toán sớm để gửi lại kỳ hạn mới với lãi suất cao hơn $\rightarrow u_i = 1{,}2$. Khi lãi suất giảm $\rightarrow u_i = 0{,}8$.

**4. Sáu kịch bản sốc lãi suất chuẩn Basel (BCBS D578) và thuật toán chiết khấu $\Delta EVE$**

Để lượng hóa $\Delta EVE$, ngân hàng áp dụng 6 kịch bản sốc lãi suất theo chuẩn mực hiệu chỉnh BCBS D578 (sbv_circular_83_2025, file TT83.md, Phụ lục V.A.III, d.1719–1768; Phụ lục V.C, d.1775–1844):
1. **Tăng song song (Parallel shock up)**: Dịch chuyển lên toàn bộ đường cong lợi suất.
2. **Giảm song song (Parallel shock down)**: Dịch chuyển xuống toàn bộ đường cong lợi suất.
3. **Cú sốc dốc (Steepener shock)**: Giảm lãi suất ngắn hạn và tăng lãi suất dài hạn: $\Delta R_{steepener,c}(t_k) = -0{,}65 \cdot |\Delta R_{short,c}(t_k)| + 0{,}9 \cdot |\Delta R_{long,c}(t_k)|$.
4. **Cú sốc phẳng (Flattener shock)**: Tăng lãi suất ngắn hạn và giảm lãi suất dài hạn: $\Delta R_{flattener,c}(t_k) = 0{,}8 \cdot |\Delta R_{short,c}(t_k)| - 0{,}6 \cdot |\Delta R_{long,c}(t_k)|$.
5. **Tăng lãi suất ngắn hạn (Short rates shock up)**: $\Delta R_{short\_up,c}(t_k) = \bar{R}_{short,c} \cdot e^{-t_k / 4}$.
6. **Giảm lãi suất ngắn hạn (Short rates shock down)**: $\Delta R_{short\_down,c}(t_k) = -\bar{R}_{short,c} \cdot e^{-t_k / 4}$.

Tham số sốc lãi suất chuẩn đối với các đồng tiền chính được quy định tại Bảng 5 Phụ lục V (ví dụ USD: Song song 200 bps, Ngắn hạn 300 bps, Dài hạn 150 bps; EUR: Song song 200 bps, Ngắn hạn 250 bps, Dài hạn 100 bps). Đối với VND và các đồng tiền chưa quy định, ngân hàng tính toán từ chuỗi lãi suất lịch sử bình quân 16 năm nhân với hệ số cú sốc toàn cầu cơ sở ($\alpha_{parallel} = 60\%$, $\alpha_{short} = 85\%$, $\alpha_{long} = 40\%$) với sàn tối thiểu 100 bps và trần tương ứng 400 bps (song song), 500 bps (ngắn hạn), 300 bps (dài hạn).

Dòng tiền ròng $CF_{i,c}(t_k)$ tại mỗi điểm giữa kỳ hạn được chiết khấu theo hệ số chiết khấu lãi kép liên tục (Continuously compounded discount factor) dựa trên lãi suất phi rủi ro sau sốc $R_{i,c}(t_k)$:

$$df_{i,c}(t_k) = \exp\left( -R_{i,c}(t_k) \cdot t_k \right)$$

Giá trị kinh tế ròng của vốn chủ sở hữu theo kịch bản $i$ cho đồng tiền $c$ được tính: $EVE_{i,c}^{nao} = \sum_k CF_{i,c}(t_k) \cdot df_{i,c}(t_k)$. Mức sụt giảm giá trị vốn chủ sở hữu: $\Delta EVE_{i,c} = EVE_{0,c}^{nao} - EVE_{i,c}^{nao} + KAO_{i,c}$.

Tổng rủi ro $\Delta EVE$ toàn hàng là mức suy giảm vốn lớn nhất trong số 6 kịch bản sau khi cộng gộp các khoản giảm dương trên tất cả các đồng tiền:

$$\Delta EVE = \max_{i} \left( \sum_{c} \max(0, \Delta EVE_{i,c}) \right)$$

**5. Đo lường $\Delta NII$ và lộ trình tuân thủ hai chỉ tiêu**

Song song với thước đo dài hạn $\Delta EVE$, ngân hàng đo lường Thay đổi thu nhập lãi thuần ($\Delta NII$) trong khung thời gian 01 năm dưới giả định cấu trúc bảng cân đối kế toán không đổi (Constant balance sheet). $\Delta NII$ được kiểm tra qua 2 kịch bản (Tăng song song và Giảm song song); rủi ro $\Delta NII$ là mức suy giảm thu nhập lãi thuần lớn nhất giữa hai kịch bản này (sbv_circular_83_2025, file TT83.md, Phụ lục V.B, d.1769–1774; liên kết [[irrbb-supervisory-framework-measures-eve-and-nii-sensitivity-across-interest-rate-shocks]]).

- **Lộ trình áp dụng**: Từ ngày 01/07/2026 đến ngày 31/12/2027, ngân hàng được quyền lựa chọn đo lường và xác định hạn mức IRRBB theo chỉ tiêu $\Delta NII$ hoặc $\Delta EVE$. Chậm nhất kể từ ngày **01/01/2028**, tất cả các ngân hàng bắt buộc phải vận hành đo lường, thiết lập hạn mức và thực hiện kiểm tra sức chịu đựng IRRBB đồng thời theo cả hai chỉ tiêu $\Delta NII$ và $\Delta EVE$, đồng thời tích hợp $\Delta EVE$ vào công thức tính vốn kinh tế $RWA_{IRRBB}$ thuộc quy trình ICAAP theo [[icaap-framework-determines-economic-capital-and-target-capital-under-stress]] (sbv_circular_83_2025, file TT83.md, Điều 74.4, d.1242–1245).

Xem thêm: [[irrbb-standardised-framework-five-stage-measurement-architecture]], [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]], [[standardised-nmd-categorisation-and-core-deposit-caps-framework]], [[standardised-loan-prepayment-modelling-and-cpr-multipliers]], [[standardised-term-deposit-early-redemption-risk-and-tdrr-scalars]], [[automatic-interest-rate-options-standardised-valuation-and-volatility-shocks]], [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]], [[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]], [[pillar-3-irrbb-quantitative-disclosure-standards-mandate-table-b-metrics]].
