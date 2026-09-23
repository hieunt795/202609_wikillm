---
title: "Conversion Factors Induce Duration-Dependent Cheapest-to-Deliver Biases Around Notional Coupons"
type: concept
tags:
  - derivatives
  - bond-futures
  - conversion-factor
  - cheapest-to-deliver
  - duration-bias
  - notional-coupon
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Hệ số chuyển đổi (Conversion Factor - CF) là công cụ toán học được các sở giao dịch phái sinh thiết lập nhằm chuẩn hóa giá trị của nhiều loại trái phiếu chính phủ có kỳ hạn và lãi suất danh nghĩa (coupon) khác nhau trong cùng một giỏ giao nhận hợp đồng tương lai (fixed_income_during, Ch.28, Sec.28.3.1, d.147–170). Khi hợp đồng tương lai bước vào quy trình giao nhận vật chất, số tiền thực tế mà bên mua phải thanh toán cho bên bán (được gọi là giá hóa đơn - invoice price) được xác định thông qua việc nhân giá khớp lệnh hợp đồng tương lai với hệ số chuyển đổi của trái phiếu cụ thể được chuyển giao, sau đó cộng thêm phần tiền lãi tích dồn phát sinh [[clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement]]:

$$\text{Invoice Price} = \text{Futures Price} \times \text{CF} + \text{Accrued Interest}$$

Về mặt định giá lý thuyết, hệ số chuyển đổi của một trái phiếu tương đương với giá sạch (clean price) của chính trái phiếu đó nếu nó được giao dịch tại mức lợi suất đáo hạn đúng bằng mức coupon danh nghĩa quy định của hợp đồng (notional coupon, thông thường là 6% tại Mỹ, Anh và khu vực đồng Euro) vào ngày giao nhận đầu tiên của tháng giao dịch (fixed_income_during, Ch.28, Sec.28.3.1, d.165–185). Do hệ số chuyển đổi cố định mức chiết khấu dòng tiền ở 6% trong suốt vòng đời của hợp đồng, sự chênh lệch giữa lợi suất giao dịch thực tế trên thị trường ($y$) và mức coupon danh nghĩa ($c_n = 6\%$) tạo ra một thiên kiến toán học có hệ thống chi phối việc xác định trái phiếu rẻ nhất để giao nộp (Cheapest-to-Deliver - CTD) [[physical-delivery-bond-futures-deter-market-manipulation-through-post-settlement-inventory-exposure]].

Thiên kiến lựa chọn CTD phụ thuộc trực tiếp vào mối quan hệ giữa lợi suất thị trường và mức coupon danh nghĩa thông qua độ nhạy cảm thời lượng (duration bias) (fixed_income_during, Ch.28, Sec.28.3.1, d.186–215). Khi lợi suất thị trường giảm sâu xuống dưới mức coupon danh nghĩa ($y < 6\%$), hệ số chuyển đổi định giá thấp hơn tương đối giá trị thị trường thực tế của các trái phiếu có thời lượng dài; do đó, các trái phiếu có thời lượng thấp nhất (lowest duration) — tức các trái phiếu có kỳ hạn còn lại ngắn nhất trong giỏ giao nhận hoặc có lãi suất coupon cao nhất — sẽ có mức giá điều chỉnh theo CF rẻ nhất và trở thành trái phiếu rẻ nhất để giao nộp [[bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships]]. Ngược lại, trong môi trường lợi suất thị trường tăng cao hơn mức coupon danh nghĩa ($y > 6\%$), hệ số chuyển đổi định giá cao hơn giá trị thực tế của các dòng tiền kỳ hạn dài; kết quả là các trái phiếu có thời lượng cao nhất (highest duration) — tức các trái phiếu có kỳ hạn dài nhất hoặc coupon thấp nhất — sẽ trở thành CTD (fixed_income_during, Ch.28, Sec.28.3.1, d.198–220).

Sự dịch chuyển CTD giữa các trái phiếu có thời lượng khác nhau khi đường cong lợi suất thay đổi trao cho bên bán một quyền chọn hoán đổi tài sản có giá trị kinh tế lớn, trực tiếp định hình tính chất lồi âm của hợp đồng tương lai [[quality-delivery-options-embed-negative-convexity-and-convexity-drag-in-bond-futures]]. Khi một đợt phát hành trái phiếu chính phủ mới diễn ra trước ngày đáo hạn của hợp đồng, việc trái phiếu mới có đủ điều kiện gia nhập giỏ giao nhận hay không sẽ làm thay đổi cấu trúc thời lượng của toàn bộ giỏ (fixed_income_during, Ch.28, Sec.28.9, d.493–501). Nếu trái phiếu mới phát hành có mức thời lượng rơi đúng vào vùng lợi thế cạnh tranh của môi trường lợi suất hiện hành, trái phiếu đó có thể lập tức trở thành CTD mới, làm dịch chuyển tức thời độ nhạy cảm rủi ro lãi suất của hợp đồng tương lai và làm thay đổi tỷ lệ đảo vị thế giữa các kỳ hạn hợp đồng [[futures-rolls-maintain-interest-rate-hedges-via-pvbp-neutral-roll-ratios-below-parity]].
