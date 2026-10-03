---
title: hqla-calculation-table-example
type: concept
tags: [tt502026, alm, lcr, hqla, calculation, template]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

Bảng tính HQLA được dùng để ghi nhận toàn bộ tài sản thanh khoản cao mà ngân hàng nắm giữ, phân loại theo cấp, áp dụng hệ số và haircut, rồi tổng hợp thành giá trị HQLA cuối cùng (sbv_circular_22_final, Phụ lục I Phần A, d.921–955).

**Cấu trúc bảng 7 cột:**

| (1) Mục | (2) Danh mục tài sản | (3) Dư nợ | (4) Hệ số thanh khoản | (5) Giá trị sau nhân | (6) Haircut / Điều chỉnh | (7) Giá trị cuối cùng |
|---|---|---|---|---|---|---|
| 1.1 | Tiền mặt VNĐ | 50 | 100% | 50 | 0% | 50 |
| 1.2 | Trái phiếu CP VNĐ | 600 | 100% | 600 | 0% | 600 |
| 1.3 | Nợ NHNN | 200 | 100% | 200 | 0% | 200 |
| **1. Cấp 1 tổng** | | **850** | | **850** | | **850** |
| 2.1 | Trái phiếu ngân hàng (xếp hạng A–) | 300 | 85% | 255 | 0% | 255 |
| 2.2 | Trái phiếu địa phương | 200 | 85% | 170 | 0% | 170 |
| **2. Cấp 2A tổng** | | **500** | | **425** | | **425** |
| | **Giới hạn Cấp 2A (40% Tổng HQLA)** | | | | | **Được tính: 425 ✓** |
| 3.1 | RMBS đủ điều kiện | 150 | 75% | 112.5 | 25% | 84.4 |
| 3.2 | Cổ phiếu VN30 | 100 | 50% | 50 | 35% | 32.5 |
| 3.3 | Trái phiếu công ty (BBB–) | 80 | 50% | 40 | 30% | 28 |
| **3. Cấp 2B tổng** | | **330** | | **202.5** | | **144.9** |
| | **Giới hạn Cấp 2B (15% Tổng HQLA)** | | | | | **Được tính: 144.9 ✓** |
| | | | | | | |
| **HQLA Tổng Cộng** | | **1.680** | | **1.477.5** | | **1.469.9** |

**Giải thích chi tiết:**

**Cột (1) — Mục:** Sắp xếp theo cấp (1 = Cấp 1, 2 = Cấp 2A, 3 = Cấp 2B), các mục con được đánh số thập phân (1.1, 1.2, v.v.).

**Cột (2) — Danh mục tài sản:** Tên ghi chép rõ loại tài sản, xếp hạng (nếu có), kỳ hạn còn lại.

**Cột (3) — Dư nợ:** Giá trị sổ sách hoặc giá trị thị trường tại ngày báo cáo, tính bằng tỷ VNĐ (hoặc ngoại tệ nếu tính LCR ngoại tệ riêng).

**Cột (4) — Hệ số thanh khoản:** Hệ số tương ứng với cấp (100% Cấp 1, 85% Cấp 2A, 50–75% Cấp 2B).

**Cột (5) — Giá trị sau nhân:** Cột (3) × Cột (4). Ví dụ: 300 × 85% = 255.

**Cột (6) — Haircut / Điều chỉnh:** Giảm trừ thêm nếu là Cấp 2B hoặc tài sản bị ràng buộc. Ví dụ: RMBS 75% × (1 − 25%) = 56.25%, cổ phiếu 50% × (1 − 35%) = 32.5%.

**Cột (7) — Giá trị cuối cùng:** Cột (5) × (1 − Cột (6)). Ví dụ: 112.5 × (1 − 25%) = 84.4.

**Kiểm tra giới hạn:**

- Cấp 2A ≤ 40% × Tổng HQLA: 425 ≤ 40% × 1.469.9 = 587.96 ✓ (đạt)
- Cấp 2B ≤ 15% × Tổng HQLA: 144.9 ≤ 15% × 1.469.9 = 220.5 ✓ (đạt)

Nếu vượt giới hạn, chỉ phần không vượt được tính; phần vượt bị loại bỏ hoàn toàn (sbv_circular_22_final, Phụ lục I Phần A, d.921–940).

**Lưu ý:**

- Bảng này được ghi hàng ngày (hoặc định kỳ) để theo dõi sự thay đổi HQLA.
- Bất kỳ thay đổi xếp hạng, downgrade, hoặc ràng buộc đều phải được cập nhật ngay.
- Giá trị cuối cùng được cộng lại để tính Tổng HQLA, dùng trong công thức LCR.

[[lcr-hqla-definition-framework]] định nghĩa LCR công thức. [[cash-outflow-rates-by-deposit-and-liability-type]] định rõ dòng tiền ra cần bao phủ.