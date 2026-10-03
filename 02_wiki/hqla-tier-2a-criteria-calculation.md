---
title: hqla-tier-2a-criteria-calculation
type: concept
tags: [tt502026, alm, lcr, hqla, hqla-tier2a, liquidity]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

HQLA Cấp 2A là nhóm tài sản thanh khoản cao thứ hai, bao gồm trái phiếu ngân hàng và chính quyền địa phương, được tính vào LCR ở hệ số 85% (nghĩa là giá trị được ghi nhận = dư nợ × 85%), với giới hạn tổng dư nợ không vượt 40% của tổng HQLA (sbv_circular_22_final, Phụ lục I Phần A, d.831–860).

**Danh mục Cấp 2A bao gồm:**

1. **Trái phiếu phát hành bởi ngân hàng thương mại**: trái phiếu có kỳ hạn còn lại ≥ 6 tháng, mức xếp hạng tín dụng tối thiểu từ A– trở lên (theo BIS, Moody's, S&P hoặc tương đương).

2. **Trái phiếu phát hành bởi chính quyền địa phương (Local Authority Securities)**: trái phiếu phát hành bởi UBND cấp tỉnh, thành phố, hoặc tổ chức tự quản cấp địa phương, mức xếp hạng tối thiểu A–, không có điều khoản call giai đoạn ≤ 30 ngày.

3. **Nợ của Ngân hàng Phát triển**: nợ phát hành bởi các ngân hàng phát triển quốc tế (IBRD, ADB, EFTA, v.v.), mức xếp hạng tối thiểu A–.

**Tiêu chí nhập danh mục:**

- **Xếp hạng tín dụng**: tối thiểu A– tại thời điểm báo cáo. Nếu xếp hạng giảm xuống dưới A– (thậm chí BBB+), tài sản bị loại khỏi HQLA Cấp 2A và phải được reclassify sang Cấp 2B hoặc loại bỏ.

- **Kỳ hạn còn lại**: tối thiểu 6 tháng (cho trái phiếu ngân hàng); trái phiếu chính quyền địa phương không có yêu cầu kỳ hạn tối thiểu nhưng không được có điều khoản call ≤ 30 ngày.

- **Không ràng buộc**: tương tự Cấp 1, tài sản phải tự do không được sử dụng làm bảo đảm.

- **Thị trường giao dịch**: trái phiếu phải được giao dịch trên thị trường tiêu chuẩn (sàn chứng khoán HoSE, HNX, hoặc thị trường OTC có tính lỏng).

**Công thức tính giá trị HQLA Cấp 2A:**

$$\text{Giá trị HQLA Cấp 2A} = \sum (\text{Dư nợ tài sản 2A}) \times 85\%$$

$$\text{Với điều kiện: } \text{Giá trị HQLA Cấp 2A} \leq 40\% \times \text{Tổng HQLA}$$

Nếu tổng Cấp 2A vượt ngưỡng 40%, chỉ phần không vượt giới hạn được tính vào LCR; phần vượt bị loại bỏ hoàn toàn (sbv_circular_22_final, Phụ lục I Phần A, d.861–880).

**Ví dụ:** Ngân hàng có HQLA Cấp 1 = 1.000 tỷ, Cấp 2A = 600 tỷ. Tổng HQLA = 1.600 tỷ. Giới hạn Cấp 2A = 40% × 1.600 = 640 tỷ. Vì 600 < 640, toàn bộ 600 tỷ được tính: 600 × 85% = 510 tỷ đưa vào LCR.

**Xử lý downgrade xếp hạng:**

Nếu tài sản Cấp 2A bị downgrade dưới A– trong quá trình nắm giữ, ngân hàng phải loại bỏ nó khỏi Cấp 2A ngay trong báo cáo kỳ tiếp theo. Tài sản downgrade có thể được đưa sang Cấp 2B (nếu xếp hạng ≥ BBB–) hoặc loại bỏ hoàn toàn (sbv_circular_22_final, Phụ lục I Phần A, d.881–895).

[[lcr-hqla-definition-framework]] định nghĩa LCR. [[hqla-tier-1-criteria-formula]] chi tiết Cấp 1. [[hqla-tier-2b-criteria-haircut]] chi tiết Cấp 2B với xử lý haircut.
