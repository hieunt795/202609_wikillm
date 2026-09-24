---
title: negative-yield-to-maturity-implies-bond-market-prices-exceed-nominal-aggregate-cash-flows
type: concept
tags: [yield-curve, interest-rates, yield-to-maturity, bond-pricing, negative-yields, swiss-bonds]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Lợi suất đáo hạn âm (negative yield to maturity - negative YTM) là trạng thái cân bằng thị trường đặc thù của công cụ nợ có thu nhập cố định, tại đó giá thị trường hiện hành của trái phiếu vượt quá tổng danh nghĩa của toàn bộ các dòng tiền coupon và mệnh giá gốc mà nhà đầu tư sẽ nhận được trong suốt vòng đời còn lại của công cụ (choudhry_analysing_yield_curve, Ch.9, Sec. "The Yield to Maturity", d.3978–3986). Trong lý thuyết định giá trái phiếu truyền thống, mức lợi suất đáo hạn $y$ được xác định thông qua phương trình điều kiện phi trọng tài cân bằng giá thị trường $P$ với hiện giá của các dòng tiền:
$$P = \sum_{t=1}^T \frac{C_t}{(1+y)^t} + \frac{M}{(1+y)^T}$$
Trong đó $C_t$ là tiền lãi coupon định kỳ, $M$ là mệnh giá thanh toán khi đáo hạn, và $T$ là thời gian đáo hạn [[yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price]].

Wolfgang Marty phân định ba trạng thái nghiệm kinh tế của phương trình định giá này:
1. Khi $y > 0$: Giá thị trường nhỏ hơn tổng số học các dòng tiền ($P < \sum_{t=1}^T C_t + M$), phản ánh giá trị thời gian dương của tiền tệ trong môi trường lãi suất danh nghĩa thông thường.
2. Khi $y = 0$: Giá thị trường bằng đúng tổng số học của toàn bộ các dòng tiền danh nghĩa trong tương lai ($P = \sum_{t=1}^T C_t + M$).
3. Khi $y < 0$: Giá thị trường vượt quá tổng số học của toàn bộ các dòng tiền danh nghĩa ($P > \sum_{t=1}^T C_t + M$) (choudhry_analysing_yield_curve, Ch.9, d.3980).

Hệ quả kinh tế trực tiếp của trạng thái $P > \sum CF_t$ là một nhà đầu tư mua trái phiếu ở mức lợi suất âm và nắm giữ cho tới ngày đáo hạn sẽ nhận về tổng lượng tiền mặt danh nghĩa ít hơn số vốn đã bỏ ra mua ban đầu, đồng nghĩa với việc chấp nhận một mức tổng tỷ suất sinh lời danh nghĩa âm chắc chắn [[negative-interest-rates-distort-financial-intermediation-and-test-the-zero-lower-bound]]. Về mặt cấu trúc toán học, phương trình YTM là một phương trình đa thức bậc $T$ đối với biến số $(1+y)^{-1}$. Dù các nghiên cứu giải tích của Shestopaloff và Marty (2011) chỉ ra rằng phương trình này về mặt lý thuyết có thể có nhiều nghiệm thực và phức khác nhau, nhưng trong thực tiễn định giá tài chính, luôn tồn tại một nghiệm thực cục bộ duy nhất nằm lân cận điểm 0 được giải bằng các thuật toán lặp số học (như Newton-Raphson) (choudhry_analysing_yield_curve, Ch.9, d.3980, d.3994).

Trong kỷ nguyên hậu khủng hoảng tài chính 2008, hiện tượng lợi suất đáo hạn âm không còn là một hiện tượng lý thuyết cá biệt mà trở thành chuẩn mực giao dịch thực tế trên thị trường nợ công châu Âu. Dữ liệu từ Sở Giao dịch Chứng khoán Thụy Sĩ (SIX Exchange) cho thấy toàn bộ các kỳ hạn ngắn và trung hạn của trái phiếu chính phủ Thụy Sĩ (Eidgenossen) đều giao dịch ở mức YTM âm (choudhry_analysing_yield_curve, Ch.9, Example 9.2, d.3982–3986, Figure 9.5), tương tự như diễn biến của đường cong lợi suất trái phiếu chính phủ Đức (Bunds).

Động lực thúc đẩy các nhà đầu tư tổ chức tiếp tục mua các trái phiếu có lợi suất âm bắt nguồn từ bốn yếu tố cấu trúc:
- Chi phí bảo toàn vốn: Mức lợi suất âm nhẹ trên trái phiếu chính phủ phi rủi ro vẫn ít tốn kém hơn chi phí lưu kho, bảo hiểm tiền mặt vật lý hoặc mức lãi suất phạt tiền gửi qua đêm tại ngân hàng trung ương;
- Ràng buộc pháp lý: Các quy định an toàn vốn Basel III và tỷ số đảm bảo thanh khoản (LCR) bắt buộc các ngân hàng phải nắm giữ tài sản thanh khoản chất lượng cao (HQLA) bất chấp mức lợi suất danh nghĩa;
- Kỳ vọng tỷ giá: Nhà đầu tư nước ngoài chấp nhận lợi suất âm đối với đồng tiền trú ẩn an toàn (như CHF) để tìm kiếm lợi nhuận từ sự tăng giá của đồng nội tệ;
- Đầu cơ chênh lệch giá vốn: Kỳ vọng lãi suất chính sách tiếp tục bị cắt giảm sâu hơn cho phép nhà đầu tư bán lại trái phiếu trên thị trường thứ cấp để hiện thực hóa thặng dư vốn trước khi đáo hạn [[discount-factor-functions-exhibit-asymmetric-convexity-and-exceed-unity-in-negative-interest-rates]].

Sự hiện diện của các mức YTM âm đòi hỏi các nhà quản lý danh mục và bộ phận ALM ngân hàng phải cẩn trọng với các giả định kinh điển của mô hình [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]], đồng thời tích hợp các đường cong chiết khấu hai đường cong phù hợp trong định giá và phòng hộ phái sinh [[dual-curve-discounting-separates-rate-projection-from-collateralized-cash-flow-discounting]].
