---
title: automatic-interest-rate-options-standardised-valuation-and-volatility-shocks
type: concept
tags: [banking, alm, irrbb, automatic-options, full-revaluation, volatility-shock, kao-metric, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Phương pháp định giá chuẩn hóa quyền chọn lãi suất tự động và cú sốc độ biến động (Automatic Interest Rate Options Standardised Valuation and Volatility Shocks) thiết lập quy trình tái định giá toàn diện (full revaluation) bắt buộc đối với toàn bộ các quyền chọn lãi suất tự động rõ ràng và ngầm định trong Khung đo lường chuẩn hóa IRRBB của Ủy ban Basel, thông qua việc áp dụng một cú sốc kép gồm dịch chuyển đường cong lợi suất và cú sốc tăng tương đối $+25\%$ đối với độ biến động ngầm định ($\Delta \sigma / \sigma = +25\%$) nhằm xác định phần bù rủi ro quyền chọn $KAO_{i,c}$ (bcbs_368, file d368.md, Section IV.5, d.739–766; Paragraph 130–131).

Các quyền chọn lãi suất tự động mang bản chất phi tuyến tính cực đoan. Khi lãi suất biến động lớn (như các kịch bản sốc $\pm 200$ bps của Basel), các phép xấp xỉ tuyến tính bậc một dựa trên thời lượng điều chỉnh (Modified Duration) hoặc độ lồi (Convexity) đều trở nên sai lệch nghiêm trọng. Do đó, Basel yêu cầu loại bỏ hoàn toàn các quyền chọn này khỏi quy trình phân bổ dòng tiền thông thường tại Giai đoạn 2 và chuyển sang Giai đoạn 4 để tính toán tái định giá giá trị hợp lý độc lập.

**Nhận diện các công cụ quyền chọn tự động trên sổ ngân hàng**

Theo quy chuẩn của Ủy ban Basel, danh mục quyền chọn lãi suất tự động bao gồm (Paragraph 130 & Footnote 24, 25, d.752–755):
- *Quyền chọn tự động rõ ràng (Explicit automatic options)*: Các hợp đồng phái sinh lãi suất giao dịch độc lập trên thị trường phi tập trung (OTC) hoặc sàn giao dịch, bao gồm trần lãi suất (caps), sàn lãi suất (floors), trần-sàn kết hợp (collars) và quyền chọn hợp đồng hoán đổi (swaptions).
- *Quyền chọn tự động ngầm định (Embedded automatic options)*: Các điều khoản quyền chọn được nhúng trực tiếp vào các hợp đồng tài chính cơ sở (host contracts), phổ biến nhất là trần lãi suất tối đa (caps) hoặc sàn lãi suất tối thiểu (floors) trong các hợp đồng cho vay thế chấp lãi suất thả nổi hoặc chứng khoán nợ thả nổi; trái phiếu có điều khoản mua lại trước hạn (callable bonds) hoặc trái phiếu có điều khoản bán lại (puttable bonds) do ngân hàng phát hành hoặc nắm giữ.
- *Quyền chọn hành vi của khách hàng bán buôn (Wholesale behavioural options)*: Toàn bộ các quyền chọn hành vi phát sinh trong giao dịch với đối tác bán buôn hoặc định chế tài chính (như quyền tất toán trước hạn khoản vay doanh nghiệp, quyền rút tiền gửi doanh nghiệp trước hạn) bắt buộc phải quy về nhóm quyền chọn tự động, bởi vì các đối tác này được giả định là các nhà đầu tư tinh vi và sẽ luôn thực hiện quyền chọn một cách triệt để ngay khi mang lại lợi ích tài chính (Footnote 24).

**Quy tắc bất đối xứng giữa quyền chọn bán (Sold) và quyền chọn mua (Bought)**

Khung chuẩn hóa thiết lập nguyên tắc xử lý bất đối xứng nhằm bảo đảm tính thận trọng tối cao (Paragraph 130):
- *Quyền chọn tự động đã bán (Sold automatic options)*: Bắt buộc phải đưa toàn bộ $100\%$ vào tính toán rủi ro. Ngân hàng đóng vai trò là bên bán quyền chọn chịu rủi ro không giới hạn khi lãi suất biến động ngược chiều.
- *Quyền chọn tự động đã mua (Bought automatic options)*: Ngân hàng được quyền lựa chọn một trong hai phương án:
  - *Phương án 1*: Đưa toàn bộ các quyền chọn mua vào tính toán để bù trừ giá trị với quyền chọn bán;
  - *Phương án 2*: Chỉ được phép đưa vào tính toán các quyền chọn mua được sử dụng với mục đích phòng hộ trực tiếp (hedging) cho các quyền chọn tự động đã bán. Nếu áp dụng phương án 2, mọi biến động giá trị thị trường của các quyền chọn mua còn lại (không dùng phòng hộ) đã được phản ánh vào vốn điều tiết (CET1, AT1 hoặc Vốn cấp 2) phải được cộng gộp bổ sung vào thước đo rủi ro tổng thể $KAO_{i,c}$ (Paragraph 131, d.765–766).

**Cú sốc kép chuẩn hóa và hàm giá trị quyền chọn**

Đối với từng quyền chọn bán $o$ theo đồng tiền $c$, giá trị thay đổi $\Delta FVAO_{i,c}^o$ dưới kịch bản sốc lãi suất $i$ được xác định thông qua phép trừ giữa giá trị quyền chọn sau sốc và giá trị quyền chọn tại ngày định giá hiện hành (Paragraph 130.1, d.742–750):

$$\Delta FVAO_{i,c}^o = V_o\left( R_{i,c}, \sigma_0 \times 1{,}25 \right) - V_o\left( R_{0,c}, \sigma_0 \right)$$

Trong đó:
- $V_o(\cdot)$ là giá trị của quyền chọn đối với người nắm giữ quyền chọn (option holder), được ước lượng bằng các mô hình định giá quyền chọn chuẩn mực (Black-76, Hull-White hoặc Black-Karasinski) đã được cơ quan giám sát phê chuẩn (Footnote 26);
- $R_{i,c}$ là đường cong lãi suất phi rủi ro của đồng tiền $c$ dưới kịch bản sốc lãi suất $i$ (Annex 2);
- $R_{0,c}$ là đường cong lãi suất phi rủi ro hiện hành tại ngày định giá;
- $\sigma_0$ là độ biến động ngầm định (implied volatility) hiện hành của lãi suất trên thị trường phái sinh;
- Yếu tố then chốt: **Độ biến động ngầm định bị áp đặt cú sốc tăng tương đối $+25\%$** ($\sigma_i = \sigma_0 \times 1{,}25$). Cú sốc này mô phỏng hiện tượng bùng nổ biến động thị trường (volatility spike) thường đi kèm với các biến cố sốc lãi suất vĩ mô, làm gia tăng mạnh giá trị thời gian (time value) của quyền chọn và đẩy chi phí bồi thường tiềm năng của bên bán quyền chọn lên mức cực đại.

Tương tự, đối với từng quyền chọn mua $q$ dùng cho mục đích phòng hộ, biến động giá trị $\Delta FVAO_{i,c}^q$ được xác định tương ứng:

$$\Delta FVAO_{i,c}^q = V_q\left( R_{i,c}, \sigma_0 \times 1{,}25 \right) - V_q\left( R_{0,c}, \sigma_0 \right)$$

**Thước đo rủi ro quyền chọn tự động $KAO_{i,c}$ và tích hợp EVE**

Tổng mức rủi ro quyền chọn lãi suất tự động đối với đồng tiền $c$ dưới kịch bản sốc $i$ ($KAO_{i,c}$) được tổng hợp theo công thức (Paragraph 130.3, d.759–764):

$$KAO_{i,c} = \sum_{o=1}^{n_c} \Delta FVAO_{i,c}^o - \sum_{q=1}^{m_c} \Delta FVAO_{i,c}^q$$

Trong đó $n_c$ là tổng số quyền chọn bán và $m_c$ là tổng số quyền chọn mua phòng hộ bằng đồng tiền $c$. Nếu tổng giá trị quyền chọn bán gia tăng vượt trội so với mức tăng của quyền chọn phòng hộ, $KAO_{i,c} > 0$ sẽ đóng vai trò là một khoản tổn thất vốn bổ sung trực tiếp (capital add-on).

Đại lượng $KAO_{i,c}$ sau đó được cộng gộp trực tiếp vào mức biến thiên giá trị kinh tế của dòng tiền cơ sở tại Giai đoạn 5 của [[irrbb-standardised-framework-five-stage-measurement-architecture]]:

$$\Delta EVE_{i,c} = EVE_{0,c}^{no} - EVE_{i,c}^{no} + KAO_{i,c}$$

phản ánh toàn diện cả rủi ro định giá lại thời lượng (duration/gap risk) lẫn rủi ro phi tuyến tính và rủi ro biến động ngầm định (vega risk) trong tổng thể thuật toán tại [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
