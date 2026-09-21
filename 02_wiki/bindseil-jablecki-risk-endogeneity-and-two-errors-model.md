---
title: bindseil-jablecki-risk-endogeneity-and-two-errors-model
type: concept
tags: [monetary, central-banking, lolr, endogenous-risk, collateral-framework, welfare-optimization]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

Mô hình cấu trúc rủi ro nội sinh và bài toán hai loại sai lầm của Bindseil & Jablecki (2013) được trình bày tại Bindseil (2014, Ch.15, §15.2, d.3533–3606) nhằm hình thức hóa mối quan hệ giữa chính sách tỷ lệ chiết khấu (haircut) của NHTW, hiệu quả kinh tế vĩ mô và rủi ro thua lỗ tài chính của chính NHTW qua hai chu kỳ kinh tế.

**Cấu trúc tài khoản tài chính và trình tự thời gian hai kỳ (Hình 15.5)**:
Hệ thống kinh tế gồm hộ gia đình (tài sản ròng $E = 200$, tiền mặt $B = 40$, tiền gửi $D = 54$, vốn cổ phần doanh nghiệp $P = 4$ và vốn ngân hàng $Q = 2$), hai ngân hàng thương mại và hai doanh nghiệp sản xuất độc lập. Mỗi ngân hàng tài trợ độc quyền cho một doanh nghiệp.
- *Kỳ 1*:
  1. *Cú sốc khả năng thanh toán (Solvency shock)*: Hai doanh nghiệp chịu cú sốc giá trị tài sản thực tế $\eta_1, \eta_2 \sim \mathcal{N}(0, \sigma_\eta^2)$.
  2. *Cú sốc thanh khoản (Liquidity shock)*: Người gửi tiền dịch chuyển số dư từ ngân hàng 2 sang ngân hàng 1 theo tín hiệu $k = \theta + (\eta_1 - \eta_2)$, trong đó $\theta \sim \mathcal{N}(0, \sigma_\theta^2)$ là yếu tố nhiễu thông tin (noise).
  3. *Ràng buộc tái cấp vốn NHTW*: Ngân hàng cầm cố toàn bộ tài sản cho NHTW; hạn mức vay mượn tối đa sau chiết khấu là $(1-h)(B+D+Q)/2$. Với dữ liệu danh mục, haircut tối đa khả thi là $h \le 60\%$.
  4. *Đổ vỡ do thanh khoản và chi phí vỡ nợ*: Nếu dòng tiền rút $k$ vượt quá hạn mức bảo đảm sau haircut, ngân hàng vỡ nợ $\implies$ doanh nghiệp phụ thuộc không thể đảo nợ và vỡ nợ dây chuyền (tín dụng bị bóp nghẹt) $\implies$ tài sản thực của doanh nghiệp bị phá hủy một lượng $x$ do chi phí thanh lý và gián đoạn tổ chức.
- *Kỳ 2*:
  5. *Độ trễ và phục hồi kinh tế*: Các doanh nghiệp và ngân hàng sống sót tiếp tục vận hành với cú sốc $\eta$ lặp lại (tính bền vững của hiệu quả kinh doanh). Doanh nghiệp vỡ nợ được tái cấu trúc dưới ban quản trị mới và nhận một cú sốc ngẫu nhiên mới.
  6. *Thước đo phúc lợi*: Tổng giá trị tài sản thực của nền kinh tế tại cuối kỳ 2.

**Bài toán hai loại sai lầm của NHTW (The Two Errors)**:
NHTW không có thông tin hoàn hảo về khả năng thanh toán của từng doanh nghiệp, mà chỉ có thể điều chỉnh tỷ lệ chiết khấu $h$ để tối thiểu hóa chi phí kỳ vọng của hai loại sai lầm:
- *Sai lầm loại 1 (Error 1 - Thanh lý non ngân hàng tốt)*: Để một ngân hàng có dự án kinh doanh bền vững trong dài hạn bị phá sản thuần túy vì cú sốc thanh khoản ngẫu nhiên $k$, phá hủy vốn tổ chức và gánh chịu chi phí vỡ nợ $x$.
- *Sai lầm loại 2 (Error 2 - Nuôi dưỡng ngân hàng xác sống)*: Cung cấp thanh khoản quá dễ dãi ($h \to 0$) cho một ngân hàng thực chất đã mất khả năng thanh toán, cho phép doanh nghiệp hoạt động kém hiệu quả tiếp tục tồn tại và lãng phí nguồn lực xã hội trong kỳ 2 (zombie lending).

**Kết quả mô phỏng và hàm ý chính sách (Hình 15.6 & 15.7)**:
- *Tác động của độ nhiễu thông tin thanh khoản ($\sigma_\theta$)*: Khi thị trường vận hành bình thường (nhiễu $\sigma_\theta$ thấp), dòng tiền rút $k$ phản ánh chính xác sự yếu kém thực chất của bên vay. Khi đó, mức haircut tối ưu $h^*$ cao hơn nhằm chủ động loại bỏ các doanh nghiệp yếu kém.
- *Tác động mang tính quyết định của chi phí vỡ nợ ($x$ và LGD)*:
  * Khi chi phí vỡ nợ bằng 0 ($x = 0$, hệ thống có khả năng tái cơ cấu không ma sát): Haircut tối ưu xã hội là 60% và tổn thất kỳ vọng của NHTW giảm đơn điệu theo $h$. NHTW có thể hành xử như một nhà đầu tư nhỏ lẻ thông thường.
  * Khi chi phí vỡ nợ cao ($x = 15$ hoặc $25$, tương đương tổn thất khi vỡ nợ $LGD \ge 60\%$, đặc trưng của khủng hoảng hệ thống): Sự hủy hoại tài sản thực $x$ lấn át hoàn toàn lợi ích của việc thanh lý các dự án xấu. Đường cong tổn thất kỳ vọng của NHTW **biến đổi thành dạng chữ U hoặc dốc đứng lên trời khi $h$ tăng cao**. Haircut khắt khe đẩy đối tác vào vỡ nợ hàng loạt, phá hủy chính giá trị tài sản bảo đảm của NHTW và làm tổn thất của NHTW tăng vọt.

**Kết luận thực tiễn**: Trong khủng hoảng tài chính toàn diện, khi chi phí vỡ nợ xã hội $x$ cực lớn và tín hiệu thị trường bị nhiễu loạn, quyết định **hạ tỷ lệ chiết khấu $h$ và mở rộng tối đa đệm tài sản bảo đảm sau chiết khấu ($CVPH$)** là lựa chọn tối ưu duy nhất — vừa tối đa hóa phúc lợi kinh tế vĩ mô, vừa bảo vệ an toàn bảng cân đối của chính NHTW theo đúng [[lender-of-last-resort-foundations-and-bagehot-principles|nguyên lý Bagehot]].
