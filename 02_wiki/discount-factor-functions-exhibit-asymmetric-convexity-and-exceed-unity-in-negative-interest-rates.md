---
title: discount-factor-functions-exhibit-asymmetric-convexity-and-exceed-unity-in-negative-interest-rates
type: concept
tags: [yield-curve, interest-rates, discount-factor, negative-interest-rates, financial-mathematics, compounding]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Hàm hệ số chiết khấu trong môi trường lãi suất âm (discount factor function in negative interest rate regimes) là sự mở rộng toán tài chính của hàm chuyển đổi giá trị thời gian của tiền khi lãi suất chiết khấu lùi xuống dưới mức 0%, làm đảo ngược các định đề chiết khấu truyền thống vốn mặc định giả định lãi suất luôn dương (choudhry_analysing_yield_curve, Ch.9, Sec. "The Discount Factor", d.3854–3882). Về mặt toán học, hàm hệ số chiết khấu $d(r, t)$ cho lãi suất $r$ và kỳ hạn $t$ được định nghĩa cho trường hợp ghép lãi rời rạc và ghép lãi liên tục:
$$d(r, t) = \frac{1}{(1+r)^t} = (1+r)^{-t} \quad \text{hoặc} \quad d(r, t) = e^{-rt}$$
Trong phân tích định lượng của Wolfgang Marty, miền xác định của hàm hệ số chiết khấu xuất hiện một điểm kỳ dị (singularity) tại $r = -1$, tại đó hệ số chiết khấu không xác định do mẫu số triệt tiêu về 0 (choudhry_analysing_yield_curve, Ch.9, d.3872).

Toàn bộ miền xác định thực của hàm $d(r, t)$ được phân rã thành ba vùng kinh tế riêng biệt:
1. Vùng $r \le -1$: Giá trị của hệ số chiết khấu trở nên vô nghĩa và bị loại trừ khỏi phạm vi ứng dụng kinh doanh tài chính.
2. Vùng $r > 0$: Trạng thái truyền thống quen thuộc, tại đó hệ số chiết khấu luôn nhỏ hơn 1 ($d(r, t) < 1$), phản ánh việc tiền tệ bị suy giảm giá trị theo thời gian và các khoản thanh toán tương lai có hiện giá thấp hơn mệnh giá danh nghĩa.
3. Vùng $-1 < r < 0$: Môi trường lãi suất âm thực tế, tại đó hệ số chiết khấu luôn lớn hơn 1 ($d(r, t) > 1$) và tiến tới vô hạn khi $r \to -1^+$ (choudhry_analysing_yield_curve, Ch.9, d.3872–3874). Khi $d(r, t) > 1$, một dòng tiền danh nghĩa nhận được trong tương lai lại có giá trị hiện tại lớn hơn chính giá trị danh nghĩa của nó hôm nay.

Đặc tính toán học cốt lõi của hàm chiết khấu được xác lập thông qua đạo hàm bậc nhất và bậc hai theo lãi suất:
$$\frac{d}{dr} d(r, t) = -t (1+r)^{-(t+1)} < 0$$
$$\frac{d^2}{dr^2} d(r, t) = t(t+1) (1+r)^{-(t+2)} > 0$$
Hai phương trình vi phân này chứng minh rằng hàm hệ số chiết khấu luôn nghịch biến đơn điệu và có độ lồi dương nghiêm ngặt ($\text{strictly convex}$) trên toàn bộ miền xác định $r > -1$ (choudhry_analysing_yield_curve, Ch.9, d.3876–3880). Do tính lồi dương nghiêm ngặt này, hàm chiết khấu thể hiện thuộc tính lồi bất đối xứng (asymmetric convexity): mức tăng giá (appreciation) của hệ số chiết khấu khi lãi suất chuyển sang mức âm luôn lớn hơn mức giảm giá (depreciation) của hệ số chiết khấu khi lãi suất chuyển sang mức dương với cùng một biên độ tuyệt đối $|\Delta r|$:
$$d(-\Delta r, t) - 1 > 1 - d(\Delta r, t)$$
Chẳng hạn với kỳ hạn 1 năm ($t=1$) và biên độ lãi suất $|\Delta r| = 5\%$, hệ số chiết khấu ở mức lãi suất âm $r = -0{,}05$ là $d(-0{,}05, 1) = \frac{1}{0{,}95} \approx 1{,}05263$ (tăng $+5{,}263\%$), trong khi hệ số chiết khấu ở mức lãi suất dương $r = +0{,}05$ là $d(+0{,}05, 1) = \frac{1}{1{,}05} \approx 0{,}95238$ (chỉ giảm $-4{,}762\%$) (choudhry_analysing_yield_curve, Ch.9, Table 9.1, d.3916–3929).

Tần suất ghép lãi trong môi trường lãi suất âm cũng tạo ra động thái kỹ thuật ngược chiều so với môi trường lãi suất dương: đối với lãi suất âm $r = -5\%$, ghép lãi hàng năm cho hệ số chiết khấu $1{,}05263$, ghép lãi bán niên giảm xuống $1{,}05194$, ghép lãi hàng quý giảm xuống $1{,}05160$, và ghép lãi liên tục hội tụ về cận dưới $e^{-(-0{,}05)} = e^{0{,}05} \approx 1{,}05127$ (choudhry_analysing_yield_curve, Ch.9, d.3931–3939). Việc hệ số chiết khấu vượt quá 1 đòi hỏi các mô hình định giá phái sinh [[dual-curve-discounting-separates-rate-projection-from-collateralized-cash-flow-discounting]] và các thuật toán khớp đường cong cấu trúc kỳ hạn [[vasicek-model-incorporates-mean-reversion-into-gaussian-dynamics-but-permits-negative-interest-rates]] phải cho phép nghiệm chiết khấu lớn hơn 1 mà không kích hoạt các điều kiện biên kiểm tra lỗi hệ thống. Hiện tượng này dẫn thẳng tới việc định giá các công cụ nợ có lợi suất đáo hạn âm [[negative-yield-to-maturity-implies-bond-market-prices-exceed-nominal-aggregate-cash-flows]], đặt ra những thách thức trực tiếp đối với công tác quản trị tài sản nợ - tài sản có (ALM) của hệ thống ngân hàng [[negative-interest-rates-distort-financial-intermediation-and-test-the-zero-lower-bound]].
