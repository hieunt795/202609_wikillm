---
title: central-bank-risk-taking-and-liquidity-support-trade-off
type: concept
tags: [monetary, central-banking, lolr, risk-management, efficient-frontier, collateral-framework]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

Sự đánh đổi giữa chấp nhận rủi ro của NHTW và hỗ trợ thanh khoản hệ thống (central bank risk-taking and liquidity support trade-off) được Bindseil (2014, Ch.15, §15.1, d.3445–3490) mô hình hóa như bài toán tối ưu hóa phúc lợi xã hội trên đường biên hiệu quả, giải quyết mâu thuẫn giữa nguyên tắc bảo toàn vốn của NHTW và sự ổn định của hệ thống tài chính trong khủng hoảng.

**Bốn trường phái quan điểm về quản trị rủi ro NHTW trong khủng hoảng**:
Khi khủng hoảng nổ ra, các ngân hàng bị siết chặt đồng thời về thanh khoản và khả năng thanh toán. NHTW đối mặt với câu hỏi: cần chấp nhận gia tăng rủi ro tài chính đến mức nào để bảo vệ hệ thống?
1. *Nguyên lý quán tính (Inertia principle)*: Giữ nguyên vẹn khuôn khổ tài sản bảo đảm và các tiêu chuẩn kiểm soát rủi ro như thời bình (Bagehot). Lợi ích: giúp ngân hàng thương mại lập kế hoạch dự phòng thanh khoản tin cậy, tránh việc NHTW phải đánh giá lại các bài toán rủi ro phức tạp trong tâm bão hoảng loạn.
2. *Chủ động chấp nhận rủi ro bổ sung (Active additional risk-taking)*: Buiter & Sibert (2007) lập luận rằng trong khủng hoảng, lợi ích xã hội biên (marginal social return) của việc NHTW gánh vác rủi ro tăng vọt. NHTW bắt buộc phải đưa rủi ro tín dụng lên bảng cân đối của mình; nếu chỉ chăm chăm giữ an toàn tài chính cho riêng mình thì NHTW là "người phục vụ tồi của lợi ích công cộng".
3. *Kế hoạch dũng cảm là kế hoạch an toàn duy nhất (Only the brave plan is the safe plan)*: Dựa trên nguyên lý rủi ro nội sinh của Bagehot, việc NHTW hành động quyết liệt bơm thanh khoản sẽ dập tắt khủng hoảng hệ thống, từ đó làm giảm (chứ không phải tăng) tổn thất tài chính thực tế của chính NHTW.
4. *Bảo vệ an toàn tín dụng trên hết (Ensure above all credit-risk protection)*: Cho rằng NHTW không có chuyên môn và nhiệm vụ gánh chịu rủi ro tín dụng lớn, nên khi rủi ro thị trường tăng, NHTW phải nâng haircut và siết chặt điều kiện để tự bảo vệ mình (bindseil_monetary_policy, Ch.15, §15.1, d.3449–3454).

**Mô hình hóa đường biên hiệu quả và hàm phúc lợi (Hình 15.1)**:
- Gọi $L(F, \Omega)$ là mức độ an toàn thanh khoản của hệ thống ngân hàng (xác suất bình quân duy trì được khả năng thanh toán), với $L$ tăng theo độ nới lỏng của khuôn khổ $F$ và giảm theo cường độ khủng hoảng $\Omega$.
- Gọi $R(F, \Omega)$ là tổng rủi ro tài chính của NHTW (đo lường qua Expected Loss, VaR hoặc Expected Shortfall), với $R$ tăng theo $\Omega$ và thông thường tăng theo độ mở của $F$.
- Véc-tơ khuôn khổ chính sách $F = \{F_1, F_2, \dots, F_n\}$ gồm các tham số: danh mục tài sản thế chấp đủ điều kiện, tỷ lệ chiết khấu (haircuts), xu hướng mua đứt chứng khoán và phổ kỳ hạn OMOs. Hai điểm mốc cực đoan:
  * *Khuôn khổ nới lỏng nhất*: Chấp nhận toàn bộ tài sản ngân hàng theo giá trị hợp lý (fair value), cam kết mọi ngân hàng có vốn dương ($E > 0$) sẽ không bao giờ bị vỡ nợ vì thanh khoản.
  * *Khuôn khổ thắt chặt nhất*: Chỉ giao dịch với trái phiếu chính phủ phi rủi ro (AAA), không cấp quyền tiếp cận tự do cho ngân hàng.
- Hàm phúc lợi xã hội của NHTW là $W(R, L)$, giảm theo rủi ro $R$ và tăng theo thanh khoản $L$.
- Tại mỗi cường độ khủng hoảng $\Omega_1 > \Omega_0$, tồn tại một **đường biên hiệu quả (efficient frontier)** biểu diễn mức thanh khoản $L$ tối đa đạt được tương ứng với từng mức rủi ro $R$. Điểm tối ưu chính sách $(R^*, L^*)$ là tiếp điểm giữa đường biên hiệu quả và đường bàng quan phúc lợi (indifference curve).

**Sự bất khả thi của trạng thái quán tính tuyệt đối**: Bindseil chứng minh rằng khi khủng hoảng xảy ra ($\Omega$ chuyển từ $\Omega_0$ sang $\Omega_1$), nếu NHTW giữ nguyên hoàn toàn khuôn khổ cũ $F^*(\Omega_0)$ (trạng thái quán tính), tọa độ rủi ro - thanh khoản $(R(F^*(\Omega_0), \Omega_1), L(F^*(\Omega_0), \Omega_1))$ hầu như không bao giờ nằm trên đường biên hiệu quả mới. NHTW bắt buộc phải tái hiệu chỉnh véc-tơ $F^*(\Omega_1)$ để thích ứng với trạng thái cân bằng mới, phân bổ tối ưu giữa mức độ bảo vệ an toàn bảng cân đối của mình và sự cứu trợ thanh khoản cho nền kinh tế (bindseil_monetary_policy, Ch.15, §15.1, d.3472–3490). Mối quan hệ giữa hai biến số này dẫn trực tiếp tới hiện tượng [[endogenous-risk-and-upward-sloping-haircut-loss-curve|rủi ro nội sinh và đường cong tổn thất dốc lên]].
