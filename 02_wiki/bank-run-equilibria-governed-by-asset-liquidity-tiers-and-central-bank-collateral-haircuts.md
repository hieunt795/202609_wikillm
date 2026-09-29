---
title: bank-run-equilibria-governed-by-asset-liquidity-tiers-and-central-bank-collateral-haircuts
type: concept
tags: [monetary, central-banking, bank-runs, multiple-equilibria, collateral-haircuts, liquidity-tiers, lolr]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-29
---

Cân bằng tháo chạy tiền gửi theo các tầng thanh khoản tài sản và tỷ lệ chiết khấu của ngân hàng trung ương (bank run equilibria governed by asset liquidity tiers and central bank collateral haircuts) được Ulrich Bindseil mô hình hóa nhằm nội sinh hóa dòng tiền gửi và làm rõ vai trò giải cứu của chính sách tài sản thế chấp trong khủng hoảng ngân hàng (bindseil_monetary_policy, d.2773–2822). Thay vì đưa ra các giả định ngoại sinh về biến động tiền gửi, mô hình thiết lập mối liên kết toán học giữa cấu trúc thanh khoản tài sản nội bảng của ngân hàng thương mại, tỷ lệ chiết khấu (haircut $h$) của ngân hàng trung ương (NHTW), và sự chuyển dịch giữa trạng thái cân bằng ổn định và cân bằng sụp đổ hoảng loạn.

Cấu trúc bảng cân đối kế toán của ngân hàng được phân rã thành ba tầng tài sản có độ thanh khoản khác nhau (bindseil_monetary_policy, d.2777–2787):
1. Tài sản luôn thanh khoản (tỷ trọng $\Lambda \ge 0$): Có thể bán ngay lập tức trên thị trường mà không chịu bất kỳ khoản lỗ nào (zero price discount).
2. Tài sản bán thanh khoản (tỷ trọng $\Pi \ge 0$ với $\Lambda + \Pi \le 1$): Hoàn toàn thanh khoản trong điều kiện thị trường bình thường, nhưng sẽ đóng băng và không thể thanh lý khi khủng hoảng nổ ra.
3. Tài sản phi thanh khoản (tỷ trọng $1 - \Lambda - \Pi$): Các khoản vay dài hạn hoặc tài sản đặc thù, hoàn toàn không thể bán trên thị trường trong ngắn hạn.

Tổng quy mô tài sản của ngân hàng là $2 + E$, trong đó nguồn vốn gồm 2 đơn vị tiền gửi bán lẻ không kỳ hạn (mỗi người gửi 1 đơn vị tiền gửi), 0 đơn vị tín dụng từ NHTW và $E$ đơn vị vốn chủ sở hữu (bindseil_monetary_policy, d.2780–2788). NHTW áp đặt tỷ lệ chiết khấu đồng nhất $h$ lên toàn bộ các tài sản thế chấp, cho phép ngân hàng có tiềm năng vay tối đa từ NHTW là $(1 - h)$ lần giá trị tài sản chưa bán.

Khả năng tạo thanh khoản tối đa của ngân hàng khi đối mặt với rút tiền ($L$) và điều kiện cân bằng duy nhất không tháo chạy (bindseil_monetary_policy, d.2795–2801):
- Trong thời bình, khi tài sản bán thanh khoản $\Pi$ vẫn thanh khoản trọn vẹn, tổng thanh khoản ngân hàng huy động được bằng cách bán tài sản thanh khoản và thế chấp tài sản còn lại cho NHTW là:
  $$L = (\Lambda + \Pi)(2 + E) + (1 - h)(1 - \Lambda - \Pi)(2 + E)$$
- Để triệt tiêu hoàn toàn động cơ rút tiền hoảng loạn và duy trì **cân bằng duy nhất không có tháo chạy (unique no-run equilibrium)**, thanh khoản khả dụng $L$ phải đủ để chi trả trọn vẹn cho ít nhất một người gửi tiền rút vốn ($L \ge 1$). Khi đó, người gửi tiền còn lại biết chắc ngân hàng vẫn sống sót và không có lý do để tháo chạy.
- Từ điều kiện $L \ge 1$, ngưỡng vốn chủ sở hữu tối thiểu mà ngân hàng bắt buộc phải duy trì ($E^*$) được xác định bởi phương trình:
  $$E^* = \frac{1}{1 - h + h(\Lambda + \Pi)} - 2$$
Ngưỡng vốn $E^*$ là hàm đồng biến theo tỷ lệ chiết khấu $h$ (haircut càng khắt khe, ngân hàng càng cần nhiều vốn) và là hàm nghịch biến theo tỷ trọng tài sản thanh khoản $\Lambda + \Pi$ (bindseil_monetary_policy, d.2801).

Cơ chế bùng phát đa cân bằng khi khủng hoảng và thắt chặt tiền tệ cưỡng bức (bindseil_monetary_policy, d.2803–2818):
- Xét ví dụ chuẩn tắc với tỷ lệ chiết khấu thông thường của ECB $h = 0{,}8$, $\Lambda = 20\%$, $\Pi = 20\%$. Trong thời bình ($\Lambda + \Pi = 0{,}4$), thanh khoản khả dụng khi ngân hàng không có vốn ($E = 0$) là:
  $$L = 0{,}4 \times 2 + (1 - 0{,}8) \times 0{,}6 \times 2 = 0{,}8 + 0{,}24 = 1{,}04 \ge 1$$
  Do $L \ge 1$, ngân hàng không cần bất kỳ đệm vốn tự có nào ($E^* = 0$) để bảo vệ tính thanh khoản, và chi phí tài trợ bình quân bằng đúng lãi suất tiền gửi (bằng lãi suất chính sách của NHTW).
- Khi khủng hoảng nổ ra bất ngờ, thị trường tài sản $\Pi$ đóng băng ($\Pi = 0$). Thanh khoản khả dụng lập tức sụp đổ xuống:
  $$L = 0{,}2 \times 2 + (1 - 0{,}8) \times 0{,}8 \times 2 = 0{,}4 + 0{,}32 = 0{,}72 < 1$$
  Điều kiện $L \ge 1$ bị phá vỡ hoàn toàn. Hệ thống lập tức rơi vào trạng thái [[bank-runs-investor-strikes-and-multiple-equilibria|đa cân bằng (multiple equilibria)]], xuất hiện một cân bằng hoảng loạn nơi cả hai người gửi tiền đồng loạt tháo chạy và đẩy ngân hàng vào vỡ nợ.
- Để tự cứu và tái lập cân bằng duy nhất an toàn trong môi trường tài sản kém thanh khoản, ngân hàng buộc phải nâng vốn chủ sở hữu lên ngưỡng tối thiểu:
  $$E \ge E^* = \frac{1}{1 - 0{,}8 + 0{,}8 \times 0{,}2} - 2 = \frac{1}{0{,}36} - 2 \approx 0{,}8$$
  Áp lực phải huy động thêm 0,8 đơn vị vốn tự có đắt đỏ trong cơn hoảng loạn khiến chi phí vốn bình quân của ngân hàng tăng vọt. Ngân hàng buộc phải tăng mạnh lãi suất cho vay và siết chặt hạn mức tín dụng đối với nền kinh tế thực, gây ra một cú sốc thắt chặt tiền tệ nghiêm trọng.

Sự can thiệp hóa giải của Ngân hàng Trung ương: Bindseil chỉ ra rằng NHTW có thể vô hiệu hóa hoàn toàn cú sốc này bằng cách **chủ động hạ mức chiết khấu bình quân từ $h = 80\%$ xuống $h = 60\%$** (bindseil_monetary_policy, d.2819). Khi $h = 0{,}6$, ngưỡng vốn tối thiểu trở thành:
$$E^* = \frac{1}{1 - 0{,}6 + 0{,}6 \times 0{,}2} - 2 = \frac{1}{0{,}52} - 2 \approx 1{,}92 - 2 < 0 \implies E^* = 0$$
Trạng thái ổn định không tháo chạy được khôi phục trọn vẹn mà không ép ngân hàng phải tăng vốn trong hoảng loạn. Mặc dù việc hạ haircut trong khủng hoảng có thể làm phát sinh rủi ro đạo đức nếu được thị trường dự đoán trước, Chapman và cộng sự (2010) cũng như Diamond & Rajan (2012) khẳng định rằng một đợt cắt giảm haircut bất ngờ và tạm thời mang lại cải thiện phúc lợi xã hội vượt trội nhờ chặn đứng vòng xoáy bán tháo thanh lý tài sản. Kết nối mở rộng: [[collateral-scarcity-and-effective-term-funding-costs]], [[securities-lending-programmes-and-central-bank-collateral-swaps]], [[lender-of-last-resort-foundations-and-bagehot-principles]].
