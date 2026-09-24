---
title: endogenous-risk-and-upward-sloping-haircut-loss-curve
type: concept
tags: [monetary, central-banking, lolr, endogenous-risk, haircuts, collateral-framework, bank-runs]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-21
---

Rủi ro nội sinh và đường cong tổn thất dốc lên theo tỷ lệ chiết khấu (endogenous risk and upward-sloping haircut-loss curve) được Bindseil (2014, Ch.15, §15.2, d.3491–3532) chứng minh toán học như bằng chứng bác bỏ quan niệm quản trị rủi ro cơ học, hiện thực hóa nguyên lý kinh điển của Walter Bagehot rằng đối với ngân hàng trung ương, "kế hoạch dũng cảm là kế hoạch an toàn duy nhất".

**Nhà đầu tư nguyên tử và rủi ro ngoại sinh thông thường (Hình 15.2)**: Đối với một nhà đầu tư nhỏ lẻ (atomistic lender) trên thị trường repo tư nhân, hành vi áp đặt tỷ lệ chiết khấu (haircut $h$) của họ không làm thay đổi giá thị trường của tài sản hay xác suất vỡ nợ của đối tác (rủi ro mang tính ngoại sinh). Khi đó, xác suất chịu tổn thất của bên cho vay trong trường hợp đối tác vỡ nợ là:
$$P(\text{Loss}) = 1 - \Phi(h\%)$$
(với $\Phi$ là hàm phân phối chuẩn tích lũy của biến động giá tài sản). Mọi thước đo rủi ro (xác suất lỗ, tổn thất kỳ vọng - Expected Loss, Value-at-Risk) đều là **hàm nghịch biến đơn điệu (downward-sloping)** theo $h$. Haircut càng cao, nhà đầu tư càng an toàn.

**NHTW và tính chất nội sinh của rủi ro trong trò chơi rút tiền (Hình 15.3 & 15.4)**: NHTW không phải là một chủ thể vi mô, mà quy mô tín dụng của nó quyết định sự sống còn của toàn hệ thống.
Xét ngân hàng có cấu trúc tài sản gồm: tài sản luôn thanh khoản $\Lambda(2+E)$, tài sản bán thanh khoản $\Pi(2+E)$ và tài sản phi thanh khoản $(1-\Pi-\Lambda)(2+E)$, với tiền gửi bán lẻ là 2, vốn chủ sở hữu $E$, chi phí vỡ nợ là $C > E$. Thanh khoản tối đa mà ngân hàng có thể tạo ra khi bị rút tiền là:
$$L = (\Lambda + \Pi)(2+E) + (1-h)(1-\Lambda-\Pi)(2+E)$$
Điều kiện để duy trì [[bank-runs-investor-strikes-and-multiple-equilibria|cân bằng không rút tiền duy nhất (unique No-Run equilibrium)]] là $L \ge 1$.
- *Trong thời bình*: Với $\Lambda = 0$, $\Pi = 0.4$, haircut NHTW $h = 0.6$, vốn $E = 0$, tổng thanh khoản tạo được là $L = 0.4 \times 2 + (1-0.6) \times 0.6 \times 2 = 0.8 + 0.48 = 1.28 \ge 1$, hệ thống hoàn toàn ổn định.
- *Khi khủng hoảng nổ ra*: Tài sản $\Pi$ mất tính thanh khoản ($\Pi = 0$). Thanh khoản ngân hàng tạo ra từ việc thế chấp tài sản còn lại cho NHTW chỉ còn:
$$L = (1-0.6) \times 2 = 0.8 < 1$$
Điều kiện $L \ge 1$ bị vi phạm. Hệ thống lập tức xuất hiện hai trạng thái cân bằng, trong đó cân bằng rút tiền hoảng loạn (bank run) xảy ra với xác suất 50%. Khi cuộc tháo chạy diễn ra, ngân hàng buộc phải thanh lý non tài sản, giá trị tài sản sụt giảm 75%. Dư nợ vay NHTW tại thời điểm sụp đổ là 0.8 và toàn bộ tài sản ngân hàng đã bị cầm cố cho NHTW. NHTW chỉ thu hồi được $0.5$ trên tổng số $0.8$ dư nợ (tỷ lệ thu hồi 62.5%), chịu khoản lỗ trực tiếp là $0.3$ đơn vị.
- *Nghịch lý Bagehot - Giảm haircut để giảm rủi ro*: Nếu trong tâm bão khủng hoảng, NHTW hành động dũng cảm bằng cách **giảm tỷ lệ chiết khấu từ $h = 0.6$ xuống $h = 0.5$**, khả năng huy động vốn của ngân hàng tăng lên:
$$L = (1-0.5) \times 2 = 1.0 \ge 1$$
Điều kiện ổn định được khôi phục trọn vẹn, cân bằng tháo chạy bị triệt tiêu hoàn toàn. Ngân hàng tiếp tục hoạt động, và tổn thất kỳ vọng của NHTW **giảm từ 0.15 xuống bằng 0**.

**Đường cong tổn thất dốc lên (Upward-sloping risk curve)**: Đồ thị hàm tổn thất của NHTW trong khủng hoảng (Hình 15.4) trở thành **đường dốc lên (upward-sloping)** theo tỷ lệ chiết khấu: việc NHTW tăng haircut mang tính phòng thủ vi mô lại chính là nguyên nhân trực tiếp kích hoạt sự đổ vỡ của đối tác và hủy hoại giá trị của khối tài sản thế chấp, đẩy tổn thất thực tế của chính NHTW tăng vọt. Sự phụ thuộc nội sinh này là nền tảng để Bindseil & Jablecki (2013) xây dựng [[bindseil-jablecki-risk-endogeneity-and-two-errors-model|mô hình cấu trúc đánh đổi hai loại sai lầm]].
