---
title: risk-exposure-offbalance-commitments
type: concept
tags: [tt502026, alm, lev, risk-exposure, commitments]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

Trạng thái cam kít ngoại bảng (EOffB) được tính bằng cách nhân số dư cam kít ngoài bảng cân đối kế toán với hệ số chuyển đổi (CCF — Credit Conversion Factor) tương ứng, theo quy định tỷ lệ an toàn vốn hiện hành (sbv_circular_22_final, Phụ lục III, Mục II.3, d.1750–1751).

**Công thức tính trạng thái cam kít ngoại bảng:**

$$\text{EOffB} = \sum_i (\text{Eoff}_i \times \text{CCF}_i)$$

Trong đó:

- **Eoffi**: Số dư phần cam kít ngoại bảng của khoản phải đòi thứ i được xác định theo quy định tỷ lệ an toàn vốn hiện hành của Thống đốc NHNN.

- **CCFi**: Hệ số chuyển đổi của phần cam kít ngoại bảng của khoản phải đòi thứ i, cũng được xác định theo quy định tỷ lệ an toàn vốn. Hệ số này phản ánh khả năng cam kít sẽ được rút ra và trở thành khoản phải đòi thực tế (sbv_circular_22_final, Phụ lục III, Mục II.3, d.1751).

CCF thường dao động từ 0% (cam kít có khả năng bị hủy bỏ cao) đến 100% (cam kít chắc chắn sẽ được sử dụng), tùy vào loại cam kít và độ ổn định của khách hàng. Cơ chế này cho phép tính toán EM dựa trên rủi ro thực tế từ các cam kít, chứ không phải coi tất cả cam kít là nợ hiện thời.

[[risk-exposure-framework-definition]] định rõ EOffB trong công thức tổng trạng thái. [[risk-exposure-derivatives-replacement-cost]] trình bày phái sinh. [[risk-exposure-onbalance-assets]] chi tiết tài sản nội bảng.
