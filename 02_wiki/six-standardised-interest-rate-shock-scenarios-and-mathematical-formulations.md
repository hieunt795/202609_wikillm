---
title: six-standardised-interest-rate-shock-scenarios-and-mathematical-formulations
type: concept
tags: [banking, alm, irrbb, shock-scenarios, yield-curve-shocks, steepener, flattener, mathematical-formulation, bcbs-368]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Hệ thống 6 kịch bản sốc lãi suất chuẩn hóa và công thức toán học định hình (Six Standardised Interest Rate Shock Scenarios and Mathematical Formulations) thiết lập các thuật toán tham số hóa sự biến dạng của đường cong lợi suất phi rủi ro trên trục thời gian kỳ hạn ($t_k$) theo Chuẩn mực BCBS 368 của Ủy ban Basel, kết hợp giữa các cú sốc dịch chuyển song song (parallel shifts) và các cú sốc phi song song (rotational and short-rate shocks) nhằm kiểm tra áp lực toàn diện đối với giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) (bcbs_368, file d368.md, Annex 2, d.1043–1111).

Nhằm khắc phục nhược điểm của các kịch bản sốc phẳng truyền thống vốn bỏ sót rủi ro tái định giá phi song song và rủi ro đường cong, Basel quy định 6 kịch bản sốc chuẩn hóa bắt buộc áp dụng cho mọi đồng tiền có vị thế trọng yếu (chiếm trên $5\%$ tài sản hoặc nợ sổ ngân hàng).

**1. Các hàm định hình suy giảm kỳ hạn (Shaping Scalars)**

Tác động của các cú sốc phi song song tại điểm giữa của từng dải kỳ hạn $t_k$ ($k \in \{1,\dots,19\}$, tính bằng năm) được điều tiết bởi hai hàm số mũ chuẩn hóa (Annex 2.ii–iii, d.1080–1090):
- *Hệ số định hình cú sốc ngắn hạn ($S_{\text{short}}(t_k)$)*: Có giá trị lớn nhất ($=1$) tại kỳ hạn ngắn nhất và suy giảm dần tiệm cận về $0$ khi kỳ hạn kéo dài về cuối đường cong (Footnote 43, d.1108):

$$S_{\text{short}}(t_k) = \exp\left( -\frac{t_k}{x} \right) = \exp\left( -\frac{t_k}{4} \right)$$

Tham số $x=4$ ở mẫu số quy định tốc độ phân rã (decay rate) của cú sốc ngắn hạn trên đường cong lợi suất.
- *Hệ số định hình cú sốc dài hạn ($S_{\text{long}}(t_k)$)*: Có giá trị bằng $0$ tại kỳ hạn qua đêm và tăng dần tiệm cận về $1$ tại kỳ hạn dài nhất:

$$S_{\text{long}}(t_k) = 1 - S_{\text{short}}(t_k) = 1 - \exp\left( -\frac{t_k}{4} \right)$$

**2. Công thức toán học của 6 kịch bản sốc chuẩn hóa**

Đối với mỗi đồng tiền $c$, mức độ dịch chuyển của đường cong lãi suất phi rủi ro $\Delta R_{i,c}(t_k)$ tại điểm giữa kỳ hạn $t_k$ dưới 6 kịch bản sốc được xác định chính xác theo các công thức chuẩn tắc sau (Annex 2.i–iv, d.1076–1097):

1. **Kịch bản 1: Tăng song song (Parallel shock up)**:
   $$\Delta R_{\text{parallel\_up}, c}(t_k) = +\Delta \bar{R}_{\text{parallel}, c}$$
2. **Kịch bản 2: Giảm song song (Parallel shock down)**:
   $$\Delta R_{\text{parallel\_down}, c}(t_k) = -\Delta \bar{R}_{\text{parallel}, c}$$
3. **Kịch bản 3: Tăng lãi suất ngắn hạn (Short rate shock up)**:
   $$\Delta R_{\text{short\_up}, c}(t_k) = +\Delta \bar{R}_{\text{short}, c} \cdot S_{\text{short}}(t_k) = +\Delta \bar{R}_{\text{short}, c} \cdot \exp\left( -\frac{t_k}{4} \right)$$
4. **Kịch bản 4: Giảm lãi suất ngắn hạn (Short rate shock down)**:
   $$\Delta R_{\text{short\_down}, c}(t_k) = -\Delta \bar{R}_{\text{short}, c} \cdot S_{\text{short}}(t_k) = -\Delta \bar{R}_{\text{short}, c} \cdot \exp\left( -\frac{t_k}{4} \right)$$
5. **Kịch bản 5: Cú sốc dốc (Steepener shock)**:
   Lãi suất ngắn hạn hạ thấp trong khi lãi suất dài hạn tăng vọt, làm gia tăng tối đa độ dốc của đường cong lợi suất:
   $$\Delta R_{\text{steepener}, c}(t_k) = -0{,}65 \cdot \left| \Delta R_{\text{short}, c}(t_k) \right| + 0{,}90 \cdot \left| \Delta R_{\text{long}, c}(t_k) \right|$$
   $$\Delta R_{\text{steepener}, c}(t_k) = -0{,}65 \cdot \Delta \bar{R}_{\text{short}, c} \cdot \exp\left( -\frac{t_k}{4} \right) + 0{,}90 \cdot \Delta \bar{R}_{\text{long}, c} \cdot \left[ 1 - \exp\left( -\frac{t_k}{4} \right) \right]$$
6. **Kịch bản 6: Cú sốc phẳng (Flattener shock)**:
   Lãi suất ngắn hạn tăng dựng đứng trong khi lãi suất dài hạn hạ thấp, làm phẳng hoặc đảo ngược đường cong lợi suất:
   $$\Delta R_{\text{flattener}, c}(t_k) = +0{,}80 \cdot \left| \Delta R_{\text{short}, c}(t_k) \right| - 0{,}60 \cdot \left| \Delta R_{\text{long}, c}(t_k) \right|$$
   $$\Delta R_{\text{flattener}, c}(t_k) = +0{,}80 \cdot \Delta \bar{R}_{\text{short}, c} \cdot \exp\left( -\frac{t_k}{4} \right) - 0{,}60 \cdot \Delta \bar{R}_{\text{long}, c} \cdot \left[ 1 - \exp\left( -\frac{t_k}{4} \right) \right]$$

**3. Ma trận biên độ sốc chuẩn theo từng đồng tiền (Table 1 Calibration)**

Biên độ cú sốc tức thời đối với lãi suất phi rủi ro ($\Delta \bar{R}_{\text{parallel}, c}$, $\Delta \bar{R}_{\text{short}, c}$, $\Delta \bar{R}_{\text{long}, c}$) được Ủy ban Basel hiệu chuẩn dựa trên chuỗi dữ liệu lịch sử 16 năm cho các đồng tiền chủ chốt (bcbs_368, file d368.md, Annex 2, Table 1, d.1060–1071):

| Đồng tiền | Ký hiệu | Cú sốc Song song ($\Delta \bar{R}_{\text{parallel}}$) | Cú sốc Ngắn hạn ($\Delta \bar{R}_{\text{short}}$) | Cú sốc Dài hạn ($\Delta \bar{R}_{\text{long}}$) |
|---|---|---|---|---|
| **Đô la Mỹ** | USD | **$200$ bps** | **$300$ bps** | **$150$ bps** |
| **Đồng Euro** | EUR | **$200$ bps** | **$250$ bps** | **$100$ bps** |
| **Yên Nhật** | JPY | **$100$ bps** | **$100$ bps** | **$100$ bps** |
| **Bảng Anh** | GBP | **$250$ bps** | **$300$ bps** | **$150$ bps** |
| **Franc Thụy Sĩ** | CHF | **$100$ bps** | **$150$ bps** | **$100$ bps** |
| **Đô la Úc** | AUD | **$300$ bps** | **$450$ bps** | **$200$ bps** |
| **Đô la Canada** | CAD | **$200$ bps** | **$300$ bps** | **$150$ bps** |
| **Nhân dân tệ** | CNY | **$250$ bps** | **$300$ bps** | **$150$ bps** |
| **Đô la Hồng Kông**| HKD | **$200$ bps** | **$250$ bps** | **$100$ bps** |
| **Đô la Singapore**| SGD | **$150$ bps** | **$200$ bps** | **$100$ bps** |

**4. Ví dụ minh họa định lượng chuẩn xác theo Ủy ban Basel (Annex 2 Examples)**

Để bảo đảm việc triển khai thuật toán không bị sai lệch, Basel cung cấp ví dụ định chuẩn tại dải kỳ hạn trung hạn $k=10$ với tọa độ điểm giữa $t_{10} = 3{,}5$ năm (kỳ hạn 3 năm đến 4 năm) (Annex 2 Examples, d.1102–1107):
- Tính toán hệ số định hình:
  $$S_{\text{short}}(3{,}5) = \exp\left( -\frac{3{,}5}{4} \right) = \exp(-0{,}875) = 0{,}417$$
  $$S_{\text{long}}(3{,}5) = 1 - 0{,}417 = 0{,}583$$
- Giả định áp dụng cho đồng Yên Nhật (JPY) với $\Delta \bar{R}_{\text{short}} = 100$ bps và $\Delta \bar{R}_{\text{long}} = 100$ bps:
  - *Tác động cú sốc Short rate up*: $\Delta R(3{,}5) = +100 \text{ bps} \times 0{,}417 = +41{,}7$ bps;
  - *Tác động cú sốc Steepener*:
    $$\Delta R(3{,}5) = -0{,}65 \cdot (100 \times 0{,}417) + 0{,}90 \cdot (100 \times 0{,}583) = -27{,}1 \text{ bps} + 52{,}5 \text{ bps} = \mathbf{+25{,}4 \text{ bps}}$$
  - *Tác động cú sốc Flattener*:
    $$\Delta R(3{,}5) = +0{,}80 \cdot (100 \times 0{,}417) - 0{,}60 \cdot (100 \times 0{,}583) = +33{,}4 \text{ bps} - 35{,}0 \text{ bps} = \mathbf{-1{,}6 \text{ bps}}$$

**5. Sàn lãi suất sau sốc (Post-shock rate floors)**

Cơ quan giám sát quốc gia có toàn quyền pháp lý (national discretion) áp đặt mức sàn đối với lãi suất sau sốc dưới 6 kịch bản trên, với điều kiện mức sàn này **không được lớn hơn $0\%$** (Annex 2, d.1098 & Footnote 46, d.1205). Quy định này cho phép phản ánh môi trường lãi suất âm thực tế (như trường hợp EUR, CHF, JPY) nhưng ngăn chặn hiện tượng áp đặt sàn dương giả tạo làm sai lệch kết quả đo lường độ nhạy cảm của bảng cân đối.

Hệ thống công thức chuẩn hóa này cung cấp biến số lãi suất chiết khấu đầu vào $R_{i,c}(t_k)$ cho [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]], điều khiển các hệ số nhân hành vi trong [[standardised-loan-prepayment-modelling-and-cpr-multipliers]] và [[standardised-term-deposit-early-redemption-risk-and-tdrr-scalars]], và tích hợp trực tiếp vào thuật toán chiết khấu giá trị kinh tế tại [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
