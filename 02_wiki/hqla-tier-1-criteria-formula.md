---
title: hqla-tier-1-criteria-formula
type: concept
tags: [tt502026, alm, lcr, hqla, hqla-tier1, liquidity]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

HQLA Cấp 1 là nhóm tài sản có tính thanh khoản cao nhất, không áp dụng giới hạn tổng dư nợ, và được tính vào HQLA ở hệ số 100%, nghĩa là toàn bộ giá trị tài sản được ghi nhận không bị giảm trừ (sbv_circular_22_final, Phụ lục I Phần A, d.811–830).

**Danh mục Cấp 1 bao gồm:**

1. **Tiền mặt**: toàn bộ tiền VNĐ và ngoại tệ gửi tại NHNN, ngân hàng khác hoặc nắm giữ trong quầy.

2. **Trái phiếu chính phủ (Government Securities)**: trái phiếu phát hành bởi Chính phủ Việt Nam, không có điều khoản call (không được phát hành bởi NHNN), mức xếp hạng tín dụng không thấp hơn mức xếp hạng quốc gia Việt Nam tại thời điểm báo cáo.

3. **Nợ của Ngân hàng Nhà nước**: tiền gửi tại NHNN, nợ phát hành bởi NHNN, hoặc các khoản tín dụng được cấp bởi NHNN dành cho các ngân hàng thương mại.

**Tiêu chí nhập danh mục:**

Để được ghi nhận là HQLA Cấp 1, tài sản phải thỏa mãn đồng thời các điều kiện sau:

- **Tính thanh khoản**: có thể chuyển đổi thành tiền mặt hoặc được NHNN chấp nhận làm bảo đảm cho khoản cấp tín dụng trong vòng 30 ngày mà không yêu cầu phải bán với lỗ.
- **Không ràng buộc**: tài sản không được sử dụng làm bảo đảm cho bất kỳ cam kít khác (trừ các trường hợp được pháp luật cho phép như bảo đảm cho hoạt động thanh toán, giao dịch repo).
- **Không có nợ**: tài sản không mang ghi chú nợ hoặc tranh chấp quyền sở hữu.
- **Được công nhận bởi các thị trường tiêu chuẩn**: tiền hoặc trái phiếu chính phủ được giao dịch công khai trên thị trường và có độ lỏng cao.

**Công thức tính giá trị HQLA Cấp 1:**

$$\text{Giá trị HQLA Cấp 1} = (\text{Tiền mặt} + \text{Trái phiếu CP} + \text{Nợ NHNN}) \times 100\%$$

Không áp dụng haircut hay điều chỉnh khác; toàn bộ dư nợ được tính vào LCR. Tuy nhiên, nếu tài sản bị ràng buộc (một phần), chỉ phần không ràng buộc được tính (sbv_circular_22_final, Phụ lục I Phần A, d.831–850).

**Xử lý ràng buộc và repo:**

Nếu ngân hàng vay tiền bằng cách thế chấp tài sản Cấp 1 (repo), tài sản đó vẫn được tính vào HQLA Cấp 1 nếu kỳ hạn repo ≤ 30 ngày. Nếu kỳ hạn > 30 ngày, tài sản được tính vào HQLA Cấp 1 chỉ khi có quyền hoàn trả tài sản trước 30 ngày (sbv_circular_22_final, Phụ lục I Phần A, d.851–880).

[[lcr-hqla-definition-framework]] định nghĩa LCR tổng quan. [[hqla-tier-2a-criteria-calculation]] và [[hqla-tier-2b-criteria-haircut]] chi tiết các cấp khác. [[hqla-adjustments-encumbrance-repo-unwinding]] quy định xử lý ràng buộc và đảo ngược giao dịch repo.
