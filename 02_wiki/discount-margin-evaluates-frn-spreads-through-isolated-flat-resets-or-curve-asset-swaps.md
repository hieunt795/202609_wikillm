---
title: discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps
type: concept
tags: [floating-rate-notes, valuation, yield-curve]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Trái phiếu thả nổi không sở hữu dòng tiền cố định nên các nhà phân tích không thể áp dụng công thức lợi suất đáo hạn thông thường mà phải sử dụng thước đo biên độ chiết khấu (fixed_income_during, Ch.17, Discount Margin, d.86–95). Biên độ chiết khấu đại diện cho phần bù lãi suất cộng thêm vào chỉ số tham chiếu nhằm đưa hiện giá của các dòng coupon và gốc tương lai về đúng mức giá thị trường của trái phiếu (fixed_income_during, Ch.17, Discount Margin, d.90–95). Theo quy ước tính toán biệt lập phổ biến trên thị trường, nhà đầu tư giải phương trình phi tuyến dưới giả định rằng mọi lần chốt lãi suất trong tương lai sẽ giữ nguyên ở mức lãi suất hiện hành và mức lãi suất kỳ hạn con (fixed_income_during, Ch.17, Discount Margin, d.96–109).

Quy ước biệt lập này có khiếm khuyết lớn là hoàn toàn không phản ánh sự thay đổi độ dốc của đường cong lãi suất kỳ hạn, khiến việc so sánh biên độ chiết khấu giữa các trái phiếu có thời gian đáo hạn khác nhau trở nên thiếu chuẩn xác (fixed_income_during, Ch.17, Discount Margin, d.110–111). Trái lại, phương pháp tiếp cận dựa trên đường cong chiết khấu của hợp đồng hoán đổi tài sản tích hợp đầy đủ cấu trúc kỳ hạn, phản ánh chính xác sự sụt giảm hiện giá của các dòng tiền xa khi đường cong lợi suất dốc lên (fixed_income_during, Ch.17, Discount Margin, d.90–95, 110–111). Phương pháp hoán đổi tài sản này kế thừa trực tiếp cơ chế bóc tách rủi ro thời lượng và cam kết vốn bảng cân đối được phân tích trong [[par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks]], đồng thời phân biệt với giải pháp phòng hộ bằng hoán đổi nội suy tại [[interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision]]. Giới hạn phương pháp luận này có nét tương đồng với giả định tái đầu tư phẳng của lợi suất đáo hạn trong [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]], đồng thời là cơ sở bổ trợ để kiểm tra tính năng bình ổn giá tại [[floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread]].
