---
title: "Effective Duration and Effective Convexity for Banking Book Optionalities"
tags:
  - concept
  - alm
  - irrbb
  - duration
  - convexity
  - embedded-options
  - bcbs-368
---

Độ thời lượng hiệu dụng (Effective Duration - $ED$) và Độ lồi hiệu dụng (Effective Convexity - $EC$) là các thước đo độ nhạy lãi suất bậc một và bậc hai bắt buộc phải áp dụng cho các vị thế trên sổ ngân hàng có chứa quyền chọn ngầm định hoặc hành vi khách hàng, do các công thức giải tích Macaulay Duration và Modified Duration hoàn toàn mất hiệu lực khi dòng tiền dự kiến biến động phi tuyến tính theo sự dịch chuyển của đường cong lợi suất (bcbs_368, file d368.md, Annex 1.2.2, d.840–880).

**1. Sự đổ vỡ của Macaulay và Modified Duration trong Sổ Ngân hàng**

Trong tài chính định lượng truyền thống, Macaulay Duration ($D_{\text{Mac}}$) và Modified Duration ($D_{\text{Mod}}$) được xác định trên giả định tiên quyết rằng dòng tiền danh nghĩa $\{CF_t\}$ tại các mốc thời gian $t$ là bất biến trước lãi suất thị trường $y$:

$$D_{\text{Mac}} = \frac{\sum_{t=1}^N t \cdot CF_t \cdot (1+y)^{-t}}{P}$$

$$D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1+y} = -\frac{1}{P} \frac{dP}{dy}$$

Tuy nhiên, hầu hết các cấu phần trọng yếu trên sổ ngân hàng đều gắn liền với quyền chọn ngầm định (embedded options) hoặc hành vi khách hàng (behavioural optionalities):
- Người vay mua nhà thế chấp có quyền trả nợ trước hạn không bị phạt hoặc chịu phí phạt rất thấp khi lãi suất thị trường giảm (loan prepayment option).
- Khách hàng cá nhân gửi tiền tiết kiệm có kỳ hạn có quyền rút vốn trước hạn bất cứ lúc nào (early deposit redemption option) khi lãi suất tăng cao để tìm kiếm lợi suất hấp dẫn hơn.
- Các hợp đồng cho vay thả nổi thường kèm điều khoản trần lãi suất (caps) hoặc sàn lãi suất (floors).
- Các khoản tiền gửi không kỳ hạn ([[non-maturity-deposit-behavioural-modelling-governs-core-and-non-core-segmentation-under-irrbb]]) có tốc độ phân rã và mức độ điều chỉnh lãi suất (pass-through beta) thay đổi mạnh theo chu kỳ lãi suất.

Khi lãi suất biến động, đạo hàm toàn phần của giá trị kinh tế theo lãi suất phải xét đến sự thay đổi của chính dòng tiền ($\frac{\partial CF_t}{\partial y} \neq 0$):

$$\frac{dP}{dy} = \sum_{t=1}^N \left[ \frac{\partial CF_t}{\partial y} (1+y)^{-t} - t \cdot CF_t (1+y)^{-(t+1)} \right]$$

Công thức Modified Duration thông thường đã bỏ qua hoàn toàn thành phần đạo hàm dòng tiền $\sum_{t=1}^N \frac{\partial CF_t}{\partial y} (1+y)^{-t}$. Sai số này dẫn đến việc ước lượng sai nghiêm trọng độ nhạy lãi suất, thậm chí sai cả chiều biến động giá trị kinh tế của danh mục.

**2. Công thức Toán học của Effective Duration (ED)**

Để phản ánh chính xác tác động của việc dòng tiền bị thay đổi bởi hành vi khách hàng, Effective Duration không sử dụng công thức vi phân giải tích mà sử dụng phương pháp sai phân hữu hạn (finite difference) thông qua tái định giá toàn diện hai chiều:

$$ED = -\frac{P_+ - P_-}{2 \cdot P_0 \cdot \Delta y} = \frac{P_- - P_+}{2 \cdot P_0 \cdot \Delta y}$$

Trong đó:
- $P_0$: Giá trị hiện tại thuần (base present value) của công cụ hoặc danh mục tại đường cong lợi suất cơ sở.
- $P_+$: Giá trị kinh tế của công cụ khi đường cong lợi suất dịch chuyển song song lên một biên độ $+\Delta y$. Tại mức lãi suất cao hơn này, mô hình hành vi tái tính toán lại toàn bộ dòng tiền $CF_t^{(+)}$ (ví dụ: tốc độ trả nợ trước hạn CPR giảm xuống, tỷ lệ rút tiền gửi trước hạn TDRR tăng lên).
- $P_-$: Giá trị kinh tế của công cụ khi đường cong lợi suất dịch chuyển song song xuống một biên độ $-\Delta y$. Toàn bộ dòng tiền được tái dự báo thành $CF_t^{(-)}$ (ví dụ: CPR tăng vọt do khách hàng tái tài trợ khoản vay, TDRR giảm do lãi suất ngoài thị trường kém hấp dẫn).
- $\Delta y$: Biên độ sốc lãi suất biên (thường được chuẩn hóa từ $10 \text{ bps}$ đến $50 \text{ bps}$, tức $0{,}0010$ đến $0{,}0050$) đủ nhỏ để hạn chế sai số bậc cao nhưng đủ lớn để tránh sai số làm tròn số học.

**3. Công thức Toán học của Effective Convexity (EC) và Hiện tượng Độ lồi âm**

Effective Convexity đo lường đạo hàm bậc hai của hàm giá trị kinh tế theo lãi suất, thể hiện tốc độ thay đổi của độ thời lượng hiệu dụng khi lãi suất dịch chuyển:

$$EC = \frac{P_+ + P_- - 2P_0}{P_0 \cdot (\Delta y)^2}$$

Sự biến động giá trị kinh tế tương đối ($\Delta P / P_0$) được xấp xỉ hóa bậc hai theo chuỗi Taylor:

$$\frac{\Delta P}{P_0} \approx -ED \cdot \Delta y + \frac{1}{2} EC \cdot (\Delta y)^2$$

Bản chất độ lồi mang ý nghĩa sống còn trong ALM:
- **Độ lồi dương ($EC > 0$)**: Điển hình ở các trái phiếu vani không quyền chọn. Khi lãi suất giảm, giá trị tài sản tăng nhanh hơn tốc độ suy giảm khi lãi suất tăng cùng một biên độ. Đây là trạng thái đệm rủi ro tự nhiên có lợi cho ngân hàng.
- **Độ lồi âm ($EC < 0$ - Negative Convexity)**: Xuất hiện phổ biến ở các danh mục cho vay bán lẻ cố định và trái phiếu có quyền chọn mua lại (callable bonds). Khi lãi suất giảm sâu, làn sóng trả nợ trước hạn tăng đột biến khiến tài sản bị hoàn vốn sớm đúng lúc ngân hàng phải tái đầu tư ở mức lãi suất rất thấp; giá trị tài sản bị chặn cứng bởi giá trị danh nghĩa trả trước ($P_-$ bị khống chế trần). Ngược lại, khi lãi suất tăng cao, khách hàng giữ chặt khoản vay lãi suất thấp, kỳ hạn dòng tiền bị kéo dài ra (extension risk), làm $P_+$ sụt giảm thê thảm. Kết quả là $P_+ + P_- < 2P_0$, dẫn tới $EC < 0$. Khi độ lồi âm, ngân hàng chịu tổn thất giá trị kinh tế kép ở cả hai chiều lãi suất.

**4. Mở rộng Key Rate Effective Duration (KRED)**

Khi đường cong lợi suất xoay trục hoặc uốn cong (non-parallel shifts) theo các kịch bản Steepener và Flattener của [[six-standardised-interest-rate-shock-scenarios-and-mathematical-formulations]], việc sử dụng một thước đo $ED$ duy nhất không phản ánh được rủi ro định hình (shaping risk). Ngân hàng triển khai ma trận Key Rate Effective Duration ($KRED_m$) cho $M$ dải kỳ hạn chuẩn hóa:

$$KRED_m = \frac{P_{-, m} - P_{+, m}}{2 \cdot P_0 \cdot \Delta y_m}$$

Trong đó $P_{+, m}$ và $P_{-, m}$ là giá trị kinh tế được tính lại khi chỉ có lãi suất tại điểm kỳ hạn $m$ bị sốc $\pm \Delta y_m$, trong khi các điểm kỳ hạn khác được nội suy giữ cố định. Tổng các độ thời lượng hiệu dụng từng phần xấp xỉ bằng $ED$ tổng thể:

$$ED \approx \sum_{m=1}^M KRED_m$$

**5. Chuẩn mực Giám sát BCBS 368 và Thực hành Quản trị ALCO**

Theo nguyên tắc Principle 4, 5 và Phụ lục Annex 1 của chuẩn mực BCBS 368:
- Các ngân hàng có danh mục tài sản/nợ chứa đựng quyền chọn ngầm định trọng yếu bắt buộc phải xây dựng hệ thống định giá động (dynamic valuation engines) có khả năng tính toán $ED$ và $EC$ cho từng danh mục sản phẩm.
- Nghiêm cấm việc áp dụng máy móc Modified Duration từ các phần mềm kế toán hoặc hệ thống core banking truyền thống vào việc tính toán rủi ro giá trị kinh tế của vốn tự có ([[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows]]).
- Khung giới hạn khẩu vị rủi ro ([[irrbb-risk-appetite-framework-establishes-multi-tiered-limits-and-escalation-protocols]]) của ALCO phải thiết lập hạn mức độ lồi âm tối đa cho phép. Các trạng thái độ lồi âm vượt ngưỡng phải được phòng hộ chủ động bằng các công cụ phái sinh bất đối xứng (như mua payer swaptions hoặc mua interest rate caps/floors) nhằm tái lập độ lồi dương cho bảng cân đối.
