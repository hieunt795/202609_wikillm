---
title: yield-curve-interpolation-and-discounting-mechanics-in-alm
type: concept
tags: [banking, alm, irrbb, yield-curve, interpolation, discounting-mechanics, zero-coupon, nirp, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Cơ chế nội suy và chiết khấu đường cong lợi suất trong ALM (Yield Curve Interpolation and Discounting Mechanics in ALM) thiết lập các kỹ thuật toán học chuẩn tắc theo Chuẩn mực BCBS 368 của Ủy ban Basel để chuyển đổi các điểm quan sát thị trường rời rạc thành một đường cong zero-coupon phi rủi ro liên tục, áp dụng hệ số chiết khấu lãi kép liên tục $DF(t_k) = \exp(-R(t_k) \cdot t_k)$ cho 19 dải kỳ hạn, và xử lý kỹ thuật đối với môi trường lãi suất âm (NIRP) khi đường cong sau sốc chạm sàn pháp định (bcbs_368, file d368.md, Section IV.6, d.771–786; Annex 2, d.1072–1111).

Độ chính xác của các thước đo giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) phụ thuộc hoàn toàn vào hai yếu tố: độ chính xác của việc phân rã dòng tiền định giá lại danh nghĩa ($CF(t_k)$) và tính chuẩn xác của đường cong lãi suất chiết khấu ($R(t_k)$) (Annex 1.4.2, d.1021). Sai số trong kỹ thuật nội suy đường cong có thể làm bóp méo kết quả tính toán EVE và dẫn đến việc đánh giá sai lệch vị thế rủi ro của ngân hàng.

**1. Xây dựng đường cong Zero-Coupon phi rủi ro từ thị trường rời rạc**

Trên thị trường tài chính, lãi suất phi rủi ro không thể quan sát được liên tục tại mọi thời điểm mà chỉ tồn tại dưới dạng các mức lãi suất niêm yết tại các kỳ hạn chuẩn có thanh khoản cao (Pillar tenors: qua đêm, 1M, 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 15Y, 20Y, 30Y) từ các công cụ thị trường tiền tệ và phái sinh (tiền gửi liên ngân hàng, hợp đồng tương lai lãi suất, và hoán đổi chỉ số qua đêm OIS / Secured Swaps) (Footnote 29, d.785).

Để xác định tỷ lệ chiết khấu cho các tọa độ điểm giữa của 19 dải kỳ hạn ($t_k \in \{0{,}0028; 0{,}0417; \dots; 25{,}0\}$ năm theo Bảng 1), ngân hàng phải thực hiện quy trình bóc tách lãi suất zero-coupon (Bootstrapping) kết hợp với các kỹ thuật nội suy toán học (Interpolation methods):
- *Nội suy tuyến tính tỷ lệ zero (Linear interpolation on zero rates)*:
  Phương pháp đơn giản nhất, nối các điểm zero-coupon quan sát liền kề bằng các đoạn thẳng. Mặc dù dễ triển khai, phương pháp này làm cho đường cong lãi suất kỳ hạn tương lai (forward curve) bị gián đoạn từng khúc (step function), tạo ra các bước nhảy lãi suất phi thực tế tại các điểm mốc kỳ hạn.
- *Nội suy Cubic Spline / Monotone Convex Spline*:
  Sử dụng các đa thức bậc ba cục bộ để tạo ra một đường cong zero-coupon trơn tru (smooth), bảo đảm tính liên tục của cả đạo hàm bậc một (thời lượng) và đạo hàm bậc hai (độ lồi). Kỹ thuật này triệt tiêu các bước nhảy bất thường của forward rates, là chuẩn mực được nhiều hệ thống ALM tiên tiến áp dụng.
- *Mô hình tham số Nelson-Siegel và Svensson (NSS)*:
  Mô hình hóa toàn bộ cấu trúc kỳ hạn thông qua hàm toán học phi tuyến biểu diễn 4 thành tố kinh tế vĩ mô: mức độ cao (level $\beta_0$), độ dốc (slope $\beta_1$), độ cong ngắn hạn (curvature $\beta_2$) và độ cong trung hạn (curvature $\beta_3$):
  $$R(t) = \beta_0 + \beta_1 \frac{1 - e^{-t/\tau_1}}{t/\tau_1} + \beta_2 \left( \frac{1 - e^{-t/\tau_1}}{t/\tau_1} - e^{-t/\tau_1} \right) + \beta_3 \left( \frac{1 - e^{-t/\tau_2}}{t/\tau_2} - e^{-t/\tau_2} \right)$$
  Mô hình NSS đem lại sự ổn định cấu trúc vượt trội khi ngoại suy các kỳ hạn rất dài (như dải $t_{19} = 25$ năm).

**2. Công thức chiết khấu lãi kép liên tục của Basel (Continuous Discounting)**

Khung chuẩn hóa BCBS 368 cưỡng chế áp dụng thống nhất công thức chiết khấu lãi kép liên tục đối với mọi dòng tiền định giá lại ròng $CF_{i,c}(t_k)$ (Section IV.6, Paragraph 132.2, d.771–776):

$$DF_{i,c}(t_k) = \exp\left( - R_{i,c}(t_k) \cdot t_k \right) = e^{-R_{i,c}(t_k) \cdot t_k}$$

Trong đó:
- $t_k$ là tọa độ điểm giữa tính bằng năm của dải kỳ hạn $k$ quy định tại Bảng 1;
- $R_{i,c}(t_k)$ là lãi suất zero-coupon phi rủi ro liên tục của đồng tiền $c$ sau cú sốc lãi suất $i$ tại kỳ hạn $t_k$:
  $$R_{i,c}(t_k) = R_{0,c}(t_k) + \Delta R_{i,c}(t_k)$$
  với $R_{0,c}(t_k)$ là lãi suất zero hiện hành và $\Delta R_{i,c}(t_k)$ là mức dịch chuyển của đường cong dưới 6 kịch bản sốc của Annex 2 (như Parallel, Steepener, Flattener).

*Quy tắc nhất quán về biên độ thương mại (Commercial Margin Consistency)*:
- Nếu dòng tiền $CF_{i,c}(t_k)$ đã được ngân hàng khấu trừ biên độ thương mại và spread tín dụng $\rightarrow$ tỷ lệ chiết khấu $R_{i,c}(t_k)$ bắt buộc phải là lãi suất zero-coupon phi rủi ro thuần túy;
- Nếu dòng tiền $CF_{i,c}(t_k)$ giữ nguyên biên độ thương mại $\rightarrow$ tỷ lệ chiết khấu $R_{i,c}(t_k)$ bắt buộc phải được cộng thêm biên độ thương mại và spread tương ứng. Việc sử dụng đường cong phi rủi ro thuần túy để chiết khấu dòng tiền có chứa biên độ thương mại bị nghiêm cấm vì sẽ phóng đại giá trị hiện tại của tài sản một cách sai lệch.

**3. Xử lý kỹ thuật trong môi trường lãi suất âm (Negative Interest Rate Environment - NIRP)**

Trong các giai đoạn kinh tế áp dụng chính sách lãi suất âm (như Ngân hàng Trung ương Châu Âu ECB, Ngân hàng Quốc gia Thụy Sĩ SNB, Ngân hàng Trung ương Nhật Bản BOJ), các cú sốc giảm lãi suất (Parallel down, Short rate down, Steepener) đẩy lãi suất sau sốc xuống sâu trong vùng âm ($R_{i,c}(t_k) < 0$).

Tình trạng này dẫn đến các hệ quả toán học đặc thù:
- *Hệ số chiết khấu lớn hơn 1*: Khi $R_{i,c}(t_k) = -|R| < 0$, hệ số chiết khấu trở thành:
  $$DF_{i,c}(t_k) = \exp\left( -(-|R|) \cdot t_k \right) = \exp\left( |R| \cdot t_k \right) > 1{,}0$$
  Dòng tiền 1 đồng nhận được tại kỳ hạn 20 năm trong tương lai sẽ có giá trị hiện tại lớn hơn 1 đồng danh nghĩa ngày hôm nay, phản ánh chi phí cơ hội âm (người nắm giữ tiền mặt phải trả phí lưu trữ).
- *Cơ chế sàn lãi suất sau sốc (Post-shock rate floors)*:
  Để ngăn chặn hiện tượng lãi suất sau sốc rơi tự do xuống các mức âm phi thực tế (chẳng hạn $-5\%$ hay $-10\%$) làm bùng nổ giá trị hiện tại của các dòng tiền dài hạn, Ủy ban Basel trao quyền cho cơ quan giám sát quốc gia áp đặt mức sàn đối với lãi suất sau sốc (Annex 2, d.1098 & Footnote 46):
  $$R_{i,c}^{\text{post-shock}}(t_k) = \max\left( \text{Floor}_c, R_{0,c}(t_k) + \Delta R_{i,c}(t_k) \right)$$
  với điều kiện tiên quyết: **Mức sàn giám sát $\text{Floor}_c$ không được lớn hơn $0\%$** (nghĩa là cơ quan quản lý được phép đặt sàn $0\%$, $-0{,}5\%$ hoặc $-1{,}0\%$, nhưng tuyệt đối không được đặt sàn dương như $+1{,}0\%$ để làm giảm giả tạo mức độ sốc giảm lãi suất).

Cơ chế nội suy và chiết khấu này là mắt xích toán học trung tâm kết nối [[six-standardised-interest-rate-shock-scenarios-and-mathematical-formulations]] và [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]] vào thuật toán tính toán tổng thể tại [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
