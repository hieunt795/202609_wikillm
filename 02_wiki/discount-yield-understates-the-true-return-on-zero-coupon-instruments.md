---
title: discount-yield-understates-the-true-return-on-zero-coupon-instruments
type: concept
tags: [interest-rates, money-market, treasury-bills, yield-to-maturity, discount-yield]
sources: [cargill_central_bank_policy]
status: draft
last_updated: 2026-09-21
---

Đối với các công cụ chiết khấu ngắn hạn trên [[financial-markets-are-divided-into-money-markets-and-capital-markets-by-maturity|thị trường tiền tệ]]—tiêu biểu là tín phiếu kho bạc (Treasury bills - T-bills) không chi trả lãi định kỳ (zero-coupon)—thực tiễn tài chính tồn tại song song hai thước đo: lợi suất đáo hạn (yield to maturity - YTM) và lợi suất chiết khấu ngân hàng (discount yield) (cargill_central_bank_policy, Ch.4, Yields on Money and Capital Market Instruments, d.1486–1503). Về mặt kỹ thuật định lượng, lợi suất chiết khấu luôn phản ánh thấp hơn tỷ suất sinh lời kinh tế thực tế của tài sản.

Sự phân kỳ này bắt nguồn từ công thức tính toán của hai phương pháp (cargill_central_bank_policy, Ch.4, d.1493–1502). [[yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price|Lợi suất đáo hạn YTM]] ($r$) đo lường tỷ lệ sinh lời thực tế trên số vốn nhà đầu tư thực chi ra để mua tài sản ($MP$) dựa trên năm lịch 365 ngày:

$$r = \frac{FV - MP}{MP} \times \frac{365}{m}$$

Trong khi đó, theo thông lệ kế toán ngân hàng truyền thống, lợi suất chiết khấu ($dr$) được tính bằng cách lấy phần chênh lệch chiết khấu chia cho mệnh giá danh nghĩa nhận về khi đáo hạn ($FV$) và quy chuẩn theo năm ước lệ 360 ngày:

$$dr = \frac{FV - MP}{FV} \times \frac{360}{m}$$

Có hai nguyên nhân có tính hệ thống khiến lợi suất chiết khấu $dr$ luôn thấp hơn $r$ một cách nhân tạo:
- Thứ nhất, mẫu số của $dr$ là mệnh giá $FV$, trong khi mẫu số của YTM là giá mua thị trường $MP$. Vì các công cụ chiết khấu luôn bán dưới mệnh giá ($FV > MP$), việc chia khoản lãi chiết khấu cho một cơ số vốn lớn hơn ($FV$) sẽ tự động làm co hẹp tỷ suất sinh lời danh nghĩa;
- Thứ hai, thừa số thời gian của $dr$ sử dụng năm 360 ngày thay vì 365 ngày thực tế, khiến tỷ lệ điều chỉnh theo năm của lợi suất chiết khấu bị thu nhỏ thêm một lượng tỷ lệ với $360/365$.

Ví dụ định lượng của Cargill chỉ ra rằng một tín phiếu kho bạc kỳ hạn 1 năm ($m = 365$) mệnh giá 1.000 USD được mua với giá 950 USD sẽ mang lại lợi suất đáo hạn thực tế là 5,26%, trong khi lợi suất chiết khấu công bố chỉ đạt 4,93% (hoặc 5,0% trên cơ sở 360 ngày) (cargill_central_bank_policy, Ch.4, d.1496, d.1502). Mặc dù các ấn phẩm tài chính lớn thường niêm yết song song cả hai thước đo, các nhà phân tích và hoạch định chính sách bắt buộc phải sử dụng YTM để phản ánh đúng chi phí cơ hội của vốn và định giá chính xác phần bù rủi ro trong hệ thống tài chính.
