---
title: hqla-tier-2b-criteria-haircut
type: concept
tags: [tt502026, alm, lcr, hqla, hqla-tier2b, liquidity]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

HQLA Cấp 2B là nhóm tài sản thanh khoản thấp nhất trong HQLA, bao gồm cổ phiếu, RMBS (Residential Mortgage-Backed Securities), và trái phiếu công ty, được tính vào LCR ở hệ số 50–75% tùy loại, với giới hạn tổng dư nợ không vượt 15% của tổng HQLA (sbv_circular_22_final, Phụ lục I Phần A, d.896–930).

**Danh mục Cấp 2B bao gồm:**

1. **Cổ phiếu (Equities)**: cổ phiếu của công ty không phải tổ chức tài chính, niêm yết trên sàn chứng khoán (HoSE, HNX), thuộc chỉ số cổ phiếu chính (VN30, HNX30), với yêu cầu độ lỏng cao (khối lượng giao dịch trung bình ≥ 2 triệu cổ phiếu/ngày).

2. **RMBS (Residential Mortgage-Backed Securities)**: chứng chỉ được bảo đảm bởi danh mục khoản vay mua nhà ở, với điều kiện: (a) LTV (Loan-to-Value) không vượt 80% tại thời điểm phát hành, (b) kỳ hạn gốc ≤ 40 năm, (c) không có điều khoản call ≤ 30 ngày.

3. **Trái phiếu công ty (Corporate Bonds)**: trái phiếu phát hành bởi doanh nghiệp phi tài chính, mức xếp hạng tối thiểu BBB–, kỳ hạn còn lại ≥ 6 tháng.

**Tiêu chí nhập danh mục:**

- **Xếp hạng tín dụng**: tối thiểu BBB– (cho trái phiếu công ty); cổ phiếu không yêu cầu xếp hạng nhưng phải thuộc chỉ số chính; RMBS phải đủ điều kiện LTV/kỳ hạn.

- **Độ lỏng**: cổ phiếu phải giao dịch hằng ngày trên sàn với khối lượng không quá nhỏ; RMBS phải được giao dịch trên thị trường thứ cấp; trái phiếu công ty phải có bid-ask spread ≤ 50 bps (basis points).

- **Không ràng buộc**: tương tự các cấp trước.

- **Giới hạn chiếm tỷ lệ**: mỗi cổ phiếu không được vượt 10% của HQLA (để tránh tập trung quá cao trong một chứng chỉ).

**Công thức tính giá trị HQLA Cấp 2B với Haircut:**

$$\text{Giá trị HQLA Cấp 2B} = \sum [(\text{Dư nợ tài sản 2B}) \times \text{Hệ số} \times (1 - \text{Haircut})]$$

**Bảng hệ số và haircut:**

| Loại tài sản | Hệ số | Haircut | Hệ số cuối cùng |
|---|---|---|---|
| RMBS đủ điều kiện | 75% | 25% | 56.25% |
| Cổ phiếu chỉ số | 50% | 35% | 32.5% |
| Trái phiếu công ty (BBB–) | 50% | 30% | 35% |

$$\text{Với điều kiện: } \text{Giá trị HQLA Cấp 2B} \leq 15\% \times \text{Tổng HQLA}$$

Haircut được áp dụng để phản ánh rủi ro thị trường (price volatility) của tài sản, đặc biệt là cổ phiếu có tính biến động cao. Ví dụ: cổ phiếu VN30 bị giảm trừ 35% giá trị, có nghĩa nếu ngân hàng nắm giữ cổ phiếu trị giá 100 tỷ, chỉ 32.5 tỷ được tính vào HQLA (sbv_circular_22_final, Phụ lục I Phần A, d.931–955).

**Ví dụ tính toán:** Ngân hàng có HQLA Cấp 1 = 1.000 tỷ, Cấp 2A = 500 tỷ (đã tính 85%), Cấp 2B = 200 tỷ cổ phiếu + 100 tỷ RMBS. Tổng HQLA sơ bộ = 1.500 tỷ. Giới hạn Cấp 2B = 15% × 1.500 = 225 tỷ. Giá trị Cấp 2B: (200 × 32.5%) + (100 × 56.25%) = 65 + 56.25 = 121.25 tỷ < 225 tỷ → toàn bộ được tính.

[[lcr-hqla-definition-framework]] định nghĩa LCR. [[hqla-tier-1-criteria-formula]] chi tiết Cấp 1. [[hqla-tier-2a-criteria-calculation]] chi tiết Cấp 2A.
