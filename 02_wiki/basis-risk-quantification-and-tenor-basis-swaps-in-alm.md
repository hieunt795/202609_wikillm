---
title: "Basis Risk Quantification and Tenor Basis Swaps in ALM"
tags:
  - concept
  - alm
  - irrbb
  - basis-risk
  - basis-swap
  - tenor-basis
  - bcbs-368
---

Rủi ro cơ sở (Basis Risk) trong IRRBB nảy sinh khi các tài sản và khoản nợ có cùng tần suất định giá lại nhưng được neo vào các chỉ số lãi suất tham chiếu khác nhau hoặc các dải kỳ hạn lãi suất khác nhau của cùng một chỉ số, đòi hỏi các kỹ thuật lượng hóa ma trận độ nhạy Basis DV01 và chiến lược trung hòa rủi ro thông qua các hợp đồng hoán đổi cơ sở (Tenor and Benchmark Basis Swaps) (bcbs_368, file d368.md, Section I, d.75–78; Principle 1, d.91–105; Annex 1.1.3 & 1.2.7, d.820–835, d.915–925).

**1. Phân loại và Bản chất Kinh tế của Rủi ro Cơ sở trong Sổ Ngân hàng**

Một sai lầm phổ biến trong ALM truyền thống là giả định rằng nếu ngân hàng duy trì trạng thái "khe hở kỳ hạn bằng không" (Zero Repricing Gap — tài sản và nợ cùng định giá lại sau $3$ tháng) thì rủi ro lãi suất đã được triệt tiêu hoàn toàn. Chuẩn mực BCBS 368 xác định rõ: Ngay cả khi kỳ hạn định giá lại khớp nhau hoàn hảo, ngân hàng vẫn đối mặt với rủi ro sụt giảm nghiêm trọng giá trị kinh tế và thu nhập lãi thuần do hai hình thái rủi ro cơ sở:

- **Benchmark Basis Risk (Rủi ro cơ sở giữa các chỉ số tham chiếu khác nhau):** Xảy ra khi tài sản và nợ neo vào các thị trường hoặc phân khúc thanh khoản khác nhau. Điển hình:
  - Các khoản cho vay thả nổi neo theo Lãi suất Cơ sở Khách hàng (Prime Rate / Base Lending Rate), trong khi nguồn vốn tài trợ liên ngân hàng neo theo Lãi suất phi rủi ro qua đêm (SOFR, SONIA, VNIBOR).
  - Tài sản neo theo lợi suất Trái phiếu Chính phủ ngắn hạn, trong khi chi phí huy động neo theo lãi suất chứng chỉ tiền gửi (CDs) hoặc lãi suất tiền gửi tiết kiệm dân cư.
  - Khi căng thẳng thị trường, chênh lệch (spread) giữa các chỉ số này mở rộng hoặc phân kỳ đột ngột, làm bốc hơi toàn bộ biên lãi của ngân hàng.
- **Tenor Basis Risk (Rủi ro cơ sở kỳ hạn tham chiếu):** Xảy ra khi tài sản và nợ cùng neo vào một họ chỉ số lãi suất thả nổi, nhưng với kỳ hạn thanh toán khác nhau. Ví dụ: Ngân hàng tài trợ cho khoản vay thả nổi neo theo lãi suất $3\text{M}$ (định giá lại mỗi quý) bằng nguồn vốn phát hành giấy tờ có giá neo theo lãi suất $1\text{M}$ (định giá lại mỗi tháng). Phần bù kỳ hạn ($3\text{M}-1\text{M}$ Basis Spread) không phải là một hằng số cố định mà biến động liên tục theo mức độ thắt chặt thanh khoản của hệ thống liên ngân hàng.

**2. Phương pháp Lượng hóa Ma trận Rủi ro Cơ sở**

Để đo lường chuẩn xác mức độ phơi nhiễm rủi ro cơ sở theo yêu cầu của Principle 1 và 4 của BCBS 368, hệ thống đo lường nội bộ (IMS) áp dụng ba kỹ thuật định lượng:

*Mô hình Hồi quy Lịch sử và Động thái Beta Cơ sở ($\beta_{\text{basis}}$):*
Ngân hàng ước lượng mối quan hệ đồng liên kết giữa biến động của lãi suất tài sản ($\Delta R_A$) và lãi suất nguồn vốn tài trợ ($\Delta R_L$):

$$\Delta R_A(t) = \alpha + \beta_{\text{basis}} \cdot \Delta R_L(t) + \epsilon(t)$$

Trong đó hệ số $\beta_{\text{basis}}$ thể hiện độ nhạy tương đối:
- Nếu $\beta_{\text{basis}} = 1$ và phần dư $\epsilon(t) \approx 0$, hai chỉ số dịch chuyển hoàn hảo cùng nhau, rủi ro cơ sở tiệt trừ.
- Nếu $\beta_{\text{basis}} < 1$ (hiện tượng phổ biến khi lãi suất huy động tăng nhanh hơn tốc độ điều chỉnh lãi suất cho vay cơ sở), ngân hàng chịu phơi nhiễm rủi ro cơ sở âm và biên lãi thuần sẽ bị co hẹp tức thì khi lãi suất toàn thị trường leo dốc.

*Thước đo Độ nhạy Điểm Cơ bản Cơ sở (Basis DV01):*
Basis DV01 đo lường sự biến động tuyệt đối của giá trị kinh tế ($\Delta EVE$) hoặc thu nhập lãi thuần ($\Delta NII$) khi khoảng cách chênh lệch giữa hai chỉ số tham chiếu mở rộng thêm 1 điểm cơ bản ($1 \text{ bp} = 0{,}01\%$):

$$\text{Basis DV01}_{A-L} = \frac{\Delta EVE}{\Delta (R_A - R_L)}$$

Ngân hàng xây dựng một ma trận Basis DV01 đa chiều trải rộng trên tất cả các cặp chỉ số tham chiếu trọng yếu ($SOFR \text{ vs } Prime$, $3\text{M} \text{ vs } 1\text{M}$, $6\text{M} \text{ vs } 3\text{M}$).

*Kịch bản Kiểm tra Áp lực Cơ sở Chuyên biệt (Dedicated Basis Stress Scenarios):*
Principle 4 bắt buộc ngân hàng không chỉ dựa vào các kịch bản sốc song song mà phải thiết kế các cú sốc phân kỳ cơ sở cực đoan (ví dụ: Cú sốc mở rộng spread giữa Libor/Euribor và OIS thêm $+100 \text{ bps}$ tương tự cuộc khủng hoảng tài chính toàn cầu 2008, hoặc kịch bản đóng băng thanh khoản thị trường tiền tệ).

**3. Kỹ thuật Phòng hộ thông qua Tenor và Benchmark Basis Swaps**

Để triệt tiêu rủi ro cơ sở tích lũy trên bảng cân đối, Treasury sử dụng các hợp đồng hoán đổi cơ sở chuyên biệt (Basis Swaps) trên thị trường phái sinh:

```
[BẢNG CÂN ĐỐI NỘI BẢNG]                 [HỢP ĐỒNG PHÁI SINH TENOR BASIS SWAP]
+-----------------------------+         +-------------------------------------+
| Tài sản: Nhận lãi suất 3M  |<------->| Trả lãi suất 3M                     |
| Nợ:     Trả lãi suất 1M     |<------->| Nhận lãi suất 1M + Tenor Spread     |
+-----------------------------+         +-------------------------------------+
                  ==> RỦI RO CƠ SỞ ĐƯỢC KHÓA CHẶT VÀ TRIỆT TIÊU
```

- **Tenor Basis Swap ($3\text{M} \text{ vs } 1\text{M}$):** Hai đối tác thỏa thuận định kỳ hoán đổi hai dòng tiền thả nổi trên cùng một mệnh giá danh nghĩa. Một bên trả lãi suất kỳ hạn $3\text{M}$, bên kia trả lãi suất kỳ hạn $1\text{M}$ cộng thêm một mức biên độ thỏa thuận (Quoted Basis Spread). Khi ký kết hợp đồng này song song với các vị thế nội bảng, Treasury khóa cứng phần chênh lệch chi phí vốn, loại bỏ hoàn toàn sự bất định của biến động spread giữa hai kỳ hạn.
- **Benchmark Basis Swap ($OIS \text{ vs } Benchmark$):** Hoán đổi giữa lãi suất phi rủi ro qua đêm dồn tích (Compounded OIS) và lãi suất huy động kỳ hạn ngắn. Giao dịch này giúp chuyển hóa toàn bộ các tài sản thả nổi phức tạp về một hệ quy chiếu chi phí vốn duy nhất là lãi suất phi rủi ro.

**4. Ràng buộc Giám sát và Chế tài Thanh tra theo BCBS 368**

Theo Principle 1 và Section IV.2 của chuẩn mực BCBS 368:
- **Cấm Bù trừ Ròng Tự động (No Automatic Netting):** Cơ quan giám sát nghiêm cấm các ngân hàng tự ý bù trừ các vị thế tài sản và nợ có cùng kỳ hạn định giá lại nếu chúng được định giá dựa trên các chỉ số tham chiếu khác nhau. Mọi phép bù trừ ròng trong bảng tính khe hở lãi suất hoặc mô hình EVE chỉ được chấp thuận nếu ngân hàng chứng minh bằng dữ liệu định lượng rằng hệ số tương quan lịch sử giữa hai chỉ số đạt tối thiểu $0{,}95$ liên tục trong 5 năm, kể cả trong các giai đoạn biến động thị trường căng thẳng nhất.
- **Hạn mức Khẩu vị Rủi ro Cơ sở Độc lập:** Ngân hàng phải thiết lập các hạn mức rủi ro cơ sở độc lập (Basis Risk Limits) tách rời khỏi hạn mức rủi ro khe hở thời gian. Bất kỳ sự vi phạm hạn mức Basis DV01 nào đều phải được kích hoạt quy trình báo cáo khẩn cấp lên ALCO ([[irrbb-risk-appetite-framework-establishes-multi-tiered-limits-and-escalation-protocols]]) và thực hiện tái cân bằng danh mục phái sinh ngay lập tức.
