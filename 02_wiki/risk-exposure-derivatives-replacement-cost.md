---
title: risk-exposure-derivatives-replacement-cost
type: concept
tags: [tt502026, alm, lev, risk-exposure, derivatives]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

Trạng thái giao dịch phái sinh (ED) được tính bằng công thức kết hợp hai thành phần: chi phí thay thế (RC — Replacement Cost) và giá trị tương lai rủi ro (PFE — Potential Future Exposure). Công thức này áp dụng cho tất cả giao dịch sản phẩm phái sinh mà ngân hàng thực hiện (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1719).

**Công thức tính trạng thái phái sinh:**

$$\text{ED}_i = \text{RC}_i + \text{PFE}_i$$

Trong đó:

- **RCi** (chi phí thay thế giao dịch thứ i): Giá trị thị trường của giao dịch sau khi trừ giá trị bù trừ hai bên đủ điều kiện, được tính bằng công thức RC = max(V − CVMr + CVMp, 0), với:
  - V = giá trị thị trường giao dịch phái sinh;
  - CVMr = ký quỹ tiền mặt ngân hàng nhận từ đối tác;
  - CVMp = ký quỹ tiền mặt ngân hàng phải trả cho đối tác.
  
  Công thức này đảm bảo RC không bao giờ âm (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1730–1738).

- **PFEi** (giá trị tương lai rủi ro giao dịch thứ i): Được xác định theo quy định tỷ lệ an toàn vốn hiện hành, đại diện cho khả năng giá trị giao dịch tăng lên trong tương lai nếu đối tác vỡ nợ (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1729).

**Bù trừ hai bên (bilateral netting):** Ngân hàng được phép thỏa thuận bù trừ hai bên nếu hợp đồng không chứa điều kiện cho phép khách hàng chỉ phải thanh toán một phần hoặc không thanh toán cho ngân hàng (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1739). Điều kiện này bảo vệ quyền lợi ngân hàng trong trường hợp khủng hoảng thị trường.

**Tài sản bảo đảm cung cấp (Collateral):** Khi ngân hàng cung cấp tài sản bảo đảm cho đối tác, tài sản này được tính vào EM như tài sản nội bảng, nếu cung cấp tài sản bảo đảm đó đã làm giảm giá trị tài sản trên báo cáo tình hình tài chính theo chuẩn mực kế toán hiện hành (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1740).

**Ký quỹ tiền mặt (Cash variation margin):** Phần ký quỹ biến động bằng tiền mặt được trao đổi giữa các đối tác có thể được coi là một dạng thanh toán trước khi đến hạn (pre-settlement payment) khi đáp ứng điều kiện tại Điều 25 Thông tư (sbv_circular_22_final, Phụ lục III, Mục II.2, d.1742). Điều kiện này cho phép ngân hàng khấu trừ ký quỹ nhận được khỏi RC.

[[risk-exposure-framework-definition]] định rõ ED trong công thức tổng trạng thái. [[risk-exposure-onbalance-assets]] trình bày cách xử lý tài sản nội bảng. [[risk-exposure-offbalance-commitments]] chi tiết các cam kít ngoại bảng.
