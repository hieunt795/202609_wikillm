---
title: upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields
type: concept
tags: [yield-curve, forward-rate, zero-rate, par-yield, term-structure]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Trên một đường cong dốc lên, cấu trúc toán học của các kỳ hạn chiết khấu bắt buộc đường cong lãi suất kỳ hạn tức thời (overnight forward curve) phải nằm trên đường cong lãi suất zero (spot curve), và đường cong lãi suất zero phải nằm trên đường cong lợi suất ngang giá (par curve) (fixed_income_during, Ch.21, Carry and Roll-Down, d.12–14). Mối quan hệ thứ bậc này chỉ đảo ngược tại các phân khúc đường cong dốc xuống, tiêu biểu như ở đoạn cực ngắn khi thị trường kỳ vọng ngân hàng trung ương sắp hạ lãi suất điều hành (fixed_income_during, Ch.21, Carry and Roll-Down, d.12, 18).

Cơ chế quy định thứ bậc này xuất phát từ bản chất bình quân của các biểu diễn cấu trúc kỳ hạn (fixed_income_during, Ch.21, Carry and Roll-Down, d.14). Lãi suất zero kỳ hạn $t$ phản ánh mức lãi suất cố định mang lại hệ số chiết khấu tương đương với việc dồn tích lãi suất qua đêm biến đổi liên tục trong suốt kỳ hạn $t$ (fixed_income_during, Ch.21, Carry and Roll-Down, d.14). Khi đường cong dốc lên, lãi suất qua đêm tăng dần theo thời gian đáo hạn. Do lãi suất zero là giá trị bình quân của các lãi suất qua đêm đó, các mức lãi suất kỳ hạn ở thời điểm tương lai xa hơn bắt buộc phải cao hơn giá trị bình quân để nâng mức trung bình đi lên (fixed_income_during, Ch.21, Carry and Roll-Down, d.14). Theo cùng nguyên lý, đường cong par curve thể hiện mức coupon bình quân của một danh mục các trái phiếu zero-coupon có các kỳ hạn trung gian. Do các trái phiếu zero-coupon ở kỳ hạn ngắn hơn có lợi suất thấp hơn, mức coupon bình quân của danh mục bắt buộc phải thấp hơn lãi suất zero tại chính điểm đáo hạn cuối cùng (fixed_income_during, Ch.21, Carry and Roll-Down, d.14).

Trật tự phân tầng này kết nối trực tiếp với các mô hình chuyển đổi trong [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], đồng thời tạo nền tảng cho việc lượng hóa [[holding-period-return-combines-carry-and-roll-down-quantified-by-break-even-yield-buffers|lợi suất kỳ hạn nắm giữ qua cấu phần carry và roll-down]]. Khi nhà đầu tư sử dụng đường cong kỳ hạn làm chỉ báo định giá, forward rate phản ánh tỷ suất sinh lời biên nếu giữ vốn đầu tư thêm một ngày trong điều kiện hình dạng đường cong không thay đổi (fixed_income_during, Ch.21, Carry and Roll-Down, d.16).
