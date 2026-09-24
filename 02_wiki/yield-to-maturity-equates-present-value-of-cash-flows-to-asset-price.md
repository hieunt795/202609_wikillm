---
title: yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price
type: concept
tags: [interest-rates, yield-to-maturity, bond-pricing, present-value, financial-mathematics]
sources: [cargill_central_bank_policy, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Trong kinh tế học tài chính, lợi suất đáo hạn (yield to maturity - YTM) được xem là thước đo chuẩn xác và có ý nghĩa kinh tế toàn diện nhất để đo lường lãi suất của một tài sản tài chính (cargill_central_bank_policy, Ch.4, Basic Technical Aspects of Interest Rates, d.1462–1464). YTM được định nghĩa là tỷ suất chiết khấu làm cân bằng tổng giá trị hiện tại của toàn bộ dòng tiền mà tài sản sinh ra trong tương lai với chi phí hiện tại để mua tài sản đó (tức giá thị trường của tài sản). Dưới góc độ đầu tư, YTM chính là tỷ suất sinh lời nội bộ (internal rate of return - IRR) của tài sản nếu người nắm giữ duy trì khoản đầu tư cho tới ngày đáo hạn.

Nguyên lý YTM dựa trên [[interest-rate-connects-the-present-to-the-future-through-time-value-of-money|giá trị thời gian của tiền]] và được áp dụng thống nhất cho mọi cấu trúc công cụ nợ và vốn trong nền kinh tế (cargill_central_bank_policy, Ch.4, d.1464–1481, d.1526–1565):
- Khoản vay đơn và tài khoản tiền gửi: Khoản vay được thanh toán một lần gồm gốc và lãi khi đáo hạn, trong đó YTM chính là lãi suất ghi trên hợp đồng tín dụng hoặc biểu lãi suất tiền gửi;
- Khoản vay thanh toán cố định (fixed-payment loan): Phổ biến trong vay mua ô tô và vay mua nhà trả góp, với số tiền trả nợ mỗi kỳ ($P$) là cố định, bao gồm phần gốc tăng dần và phần lãi giảm dần theo thời gian. Phương trình hiện giá $L = \sum_{t=1}^m \frac{P}{(1+r)^t}$ xác định YTM ($r$) từ quy mô khoản vay $L$ và kỳ hạn $m$;
- Trái phiếu trả lãi định kỳ (coupon bond): Giá thị trường ($MP$) bằng tổng hiện giá của các dòng tiền lãi coupon ($CP$) hàng năm cộng với hiện giá của mệnh giá gốc ($FV$) hoàn trả vào năm đáo hạn:

$$MP = \sum_{t=1}^m \frac{CP}{(1+r)^t} + \frac{FV}{(1+r)^m}$$

Mối quan hệ định giá này chỉ ra rằng: khi lợi suất thị trường $r$ bằng lãi suất coupon ($CP/FV$), trái phiếu giao dịch đúng mệnh giá (at par); khi lợi suất thị trường cao hơn lãi suất coupon, trái phiếu giao dịch dưới mệnh giá (bán chiết khấu - discount); và khi lợi suất thị trường thấp hơn lãi suất coupon, trái phiếu giao dịch trên mệnh giá (bán thặng dư - premium) (cargill_central_bank_policy, Ch.4, Table 4.1, d.1531–1533);
- Trái phiếu vĩnh cửu (consol) và Cổ phiếu (equities): Đối với trái phiếu không có kỳ hạn thanh toán gốc ($m = \infty$), công thức rút gọn thành $MP = CP / r \iff r = CP / MP$. Bằng cách mở rộng nguyên lý này sang cổ phiếu với dòng cổ tức dự kiến ($D$) chi trả vô hạn, tỷ suất sinh lời của cổ phiếu được xấp xỉ bằng tỷ số cổ tức trên giá thị trường: $r \approx D / MP$ (cargill_central_bank_policy, Ch.4, d.1536–1565).

Việc áp dụng nhất quán YTM giúp thị trường so sánh chuẩn mực lợi suất giữa các công cụ có cấu trúc dòng tiền hoàn toàn khác nhau, tránh được những sai lệch do các thước đo quy ước tạo ra như [[discount-yield-understates-the-true-return-on-zero-coupon-instruments|lợi suất chiết khấu]] của tín phiếu kho bạc, đồng thời là cơ sở để phân tích [[interest-rate-risk-increases-with-maturity-and-separates-total-return-from-yield|rủi ro lãi suất khi định giá tài sản tài chính]], dù bản thân công thức này chứa đựng khiếm khuyết khi [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates|giả định đường cong lợi suất phẳng và tái đầu tư đồng nhất]].

Trong kỷ nguyên hậu khủng hoảng tài chính 2008, Wolfgang Marty chỉ ra sự xuất hiện của trạng thái nghiệm đặc biệt: lợi suất đáo hạn âm ($r < 0$) (choudhry_analysing_yield_curve, Ch.9, d.3978–3986). Khi YTM rơi xuống dưới 0%, giá thị trường của trái phiếu vượt qua tổng số học không chiết khấu của toàn bộ các khoản coupon và mệnh giá gốc tương lai ($MP > \sum_{t=1}^m CP_t + FV$), đồng nghĩa với việc nhà đầu tư nhận về lượng tiền mặt danh nghĩa ít hơn chi phí vốn đã chi ra [[negative-yield-to-maturity-implies-bond-market-prices-exceed-nominal-aggregate-cash-flows]]. Mặc dù về mặt đại số phương trình YTM là một đa thức bậc cao có thể chứa nhiều nghiệm phức, trong thực tiễn định giá các thuật toán số học luôn xác định được một nghiệm thực duy nhất lân cận điểm 0, phản ánh trung thực trạng thái hệ số chiết khấu vượt quá 1 trong phân tích cấu trúc kỳ hạn [[discount-factor-functions-exhibit-asymmetric-convexity-and-exceed-unity-in-negative-interest-rates]].

