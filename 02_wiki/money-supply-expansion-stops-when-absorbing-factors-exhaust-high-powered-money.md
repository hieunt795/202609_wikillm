---
title: money-supply-expansion-stops-when-absorbing-factors-exhaust-high-powered-money
type: concept
tags:
  - money-supply
  - base-money
  - money-multiplier
  - absorbing-factors
  - bank-reserves
sources: [cargill_central_bank_policy]
status: stable
last_updated: 2026-09-22
---

Quá trình cung tiền trong [[modern-monetary-system-functions-as-an-inverted-pyramid|hệ thống tiền tệ kim tự tháp ngược]] vận hành dựa trên sự tương tác giữa quyết định bơm tiền của ngân hàng trung ương và phản ứng của hệ thống ngân hàng thương mại cùng công chúng. Để làm rõ bản chất động học này, Thomas F. Cargill đặt ra hai câu hỏi định hình toàn bộ cơ chế mở rộng tiền tệ (cargill_central_bank_policy, Ch.12, Part 2: The Money Supply Process in More Detail, d.3783–3788):
- *Điều gì kích hoạt quá trình?* Quá trình cung tiền luôn bắt đầu từ sự thay đổi trong lượng [[reserve-money|tiền cơ sở]] ($\Delta H$) do ngân hàng trung ương chủ động tạo lập thông qua [[central-banks-create-base-money-out-of-thin-air-through-open-market-operations|nghiệp vụ thị trường mở]] hoặc cung cấp thanh khoản tái cấp vốn.
- *Điều gì làm dừng quá trình?* Quá trình tạo tiền và mở rộng tín dụng chỉ dừng lại khi toàn bộ lượng tiền cơ sở ban đầu $\Delta H$ bị hấp thụ hoàn toàn bởi các yếu tố hấp thụ (absorbing factors), khiến cho trong hệ thống không còn bất kỳ lượng dự trữ khả dụng nào để tiếp tục hỗ trợ cho các khoản vay mới.

Điểm cân bằng kết thúc quá trình được xác định chính xác qua phương trình các yếu tố hấp thụ:
$$\Delta H = rr \cdot \Delta T + \Delta C + \Delta E$$
trong đó ba yếu tố hấp thụ tiền cơ sở gồm có (cargill_central_bank_policy, Ch.12, Part 2: The Money Supply Process in More Detail, d.3789–3794):
1. Gia tăng [[required-reserves|dự trữ bắt buộc]] ($rr \cdot \Delta T$): lượng tiền cơ sở bị phong tỏa theo quy định pháp lý khi tiền gửi giao dịch ($T$) mở rộng với tỷ lệ dự trữ bắt buộc $rr$.
2. Gia tăng tiền mặt do công chúng nắm giữ ($\Delta C$): khi thu nhập và tiền gửi tăng lên, người dân rút một phần tiền gửi thành tiền mặt lưu thông ngoài ngân hàng (rò rỉ tiền mặt).
3. Gia tăng [[excess-reserves|dự trữ vượt mức]] tự nguyện ($\Delta E$): các tổ chức tín dụng giữ lại một phần dự trữ để phòng ngừa rủi ro thanh khoản thay vì đem toàn bộ đi cấp tín dụng.

Về mặt tổ chức thị trường, có sự khác biệt căn bản giữa một định chế nhận tiền gửi độc quyền (monopoly depository institution) và một hệ thống đa ngân hàng cạnh tranh (multiple depository institutions) dù kết quả mở rộng cung tiền cuối cùng là tương đương nhau (cargill_central_bank_policy, Ch.12, Dropping the First Restriction, d.3693–3696):
- Trong mô hình độc quyền, ngân hàng duy nhất có thể lập tức cấp một khoản vay lớn gấp nhiều lần lượng dự trữ mới mà không lo sợ rủi ro mất thanh khoản, bởi vì toàn bộ số tiền người vay chi trả cho đối tác cuối cùng cũng sẽ được gửi lại vào chính các chi nhánh của ngân hàng đó (d.3663–3689).
- Ngược lại, trong hệ thống đa ngân hàng thực tế, một ngân hàng riêng lẻ không bao giờ dám cho vay vượt quá lượng dự trữ vượt mức hiện có ($\Delta E$), bởi vì khi người vay chi tiêu tiền bằng séc hoặc chuyển khoản, ngân hàng nhận tiền của bên thụ hưởng sẽ đòi thanh toán bù trừ, buộc ngân hàng gốc phải chuyển giao dự trữ tương ứng qua tài khoản tại ngân hàng trung ương (d.3695–3711). Tuy nhiên, số dự trữ chuyển dịch sang ngân hàng thứ hai lại trở thành nguồn dự trữ vượt mức mới cho ngân hàng đó tiếp tục cho vay, tạo ra chuỗi phân phối tín dụng phân tán qua nhiều tầng nấc (d.3712–3769).

Cơ chế hấp thụ này chứng minh rằng [[the-money-multiplier-links-reserve-money-to-the-money-supply|số nhân tiền]] không phải là một hằng số máy móc, mà là sự phản chiếu tổng hòa các hành vi kinh tế của cả ba bên: ngân hàng trung ương (quy định $rr$), công chúng (lựa chọn tỷ lệ nắm giữ tiền mặt) và các ngân hàng thương mại (lựa chọn tỷ lệ đệm an toàn dự trữ vượt mức).

Để thấy rõ phương pháp vận hành bằng số học cụ thể, Cargill xây dựng mô hình minh họa quá trình cung tiền với các tỷ lệ hành vi định sẵn (cargill_central_bank_policy, Ch.12, An mustration of the Money Supply Process, d.3885–3944):
- Giả định các tỷ lệ hành vi nền tảng:
  1. Hộ gia đình mong muốn giữ 0,25 USD tiền mặt cho mỗi 1 USD tiền gửi giao dịch: $k = C / T = 0{,}25$.
  2. Tỷ lệ dự trữ bắt buộc theo luật định đối với tiền gửi giao dịch là 10%: $rr = 0{,}10$.
  3. Các tổ chức nhận tiền gửi mong muốn giữ 0,05 USD dự trữ vượt mức cho mỗi 1 USD nợ tiền gửi giao dịch: $e = ER / T = 0{,}05$.
  4. Hộ gia đình mong muốn giữ 0,50 USD trong các quỹ thị trường tiền tệ (MMF) cho mỗi 1 USD tiền gửi giao dịch: $m = MMF / T = 0{,}50$.
- Các số nhân thành phần được tính toán từ các tỷ lệ trên với mẫu số chung $(rr + k + e) = 0{,}10 + 0{,}25 + 0{,}05 = 0{,}40$:
  - Số nhân tiền gửi giao dịch: $TM = \frac{1}{rr + k + e} = \frac{1}{0{,}40} = 2{,}5$.
  - Số nhân tiền mặt: $CM = \frac{k}{rr + k + e} = \frac{0{,}25}{0{,}40} = 0{,}625$.
  - Số nhân dự trữ vượt mức: $ERM = \frac{e}{rr + k + e} = \frac{0{,}05}{0{,}40} = 0{,}125$.
  - Số nhân tiền M1: $M1M = \frac{1 + k}{rr + k + e} = \frac{1{,}25}{0{,}40} = 3{,}125$.
  - Số nhân quỹ thị trường tiền tệ: $MMFM = \frac{m}{rr + k + e} = \frac{0{,}50}{0{,}40} = 1{,}25$.
  - Số nhân tiền M2: $M2M = \frac{1 + k + m}{rr + k + e} = \frac{1 + 0{,}25 + 0{,}50}{0{,}40} = 4{,}375$.
- Khi ngân hàng trung ương bơm một lượng tiền cơ sở ban đầu $\Delta H = 1.000\text{ USD}$, các cấu phần tiền tệ và các yếu tố hấp thụ biến đổi chính xác theo các số nhân:
  - Tiền gửi giao dịch mở rộng: $\Delta T = TM \cdot \Delta H = 2{,}5 \times 1.000 = 2.500\text{ USD}$.
  - Yếu tố hấp thụ 1 (dự trữ bắt buộc tăng): $\Delta RR = rr \cdot \Delta T = 0{,}10 \times 2.500 = 250\text{ USD}$.
  - Yếu tố hấp thụ 2 (tiền mặt lưu thông tăng): $\Delta C = k \cdot \Delta T = CM \cdot \Delta H = 0{,}625 \times 1.000 = 625\text{ USD}$.
  - Yếu tố hấp thụ 3 (dự trữ vượt mức tăng): $\Delta ER = e \cdot \Delta T = ERM \cdot \Delta H = 0{,}125 \times 1.000 = 125\text{ USD}$.
  - Tổng các yếu tố hấp thụ: $\sum = \Delta RR + \Delta C + \Delta ER = 250 + 625 + 125 = 1.000\text{ USD} = \Delta H$.
  - Khối tiền mở rộng tương ứng: $\Delta M1 = M1M \cdot \Delta H = 3{,}125 \times 1.000 = 3.125\text{ USD}$ (chính bằng $\Delta T + \Delta C = 2.500 + 625$), tiền quỹ thị trường tiền tệ $\Delta MMF = 1{,}25 \times 1.000 = 1.250\text{ USD}$, và tổng cung tiền $\Delta M2 = 4{,}375 \times 1.000 = 4.375\text{ USD}$.

Minh họa số học này chứng minh định lý căn bản: quá trình tạo tiền dừng lại chính xác tại điểm tổng các yếu tố hấp thụ triệt tiêu toàn bộ lượng tiền cơ sở ban đầu do ngân hàng trung ương bơm vào. Việc mở rộng sang các công cụ không chịu dự trữ bắt buộc như quỹ thị trường tiền tệ làm tăng tổng cung tiền M2 nhưng không làm thay đổi phương trình hấp thụ tiền cơ sở vì MMF không bị trói buộc bởi tỷ lệ dự trữ bắt buộc (cargill_central_bank_policy, Ch.12, An mustration of the Money Supply Process, d.3885–3944).
