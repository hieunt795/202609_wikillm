---
title: hqla-adjustments-encumbrance-repo-unwinding
type: concept
tags: [tt502026, alm, lcr, hqla, encumbrance, repo]
sources: [sbv_circular_22_final]
status: draft
last_updated: 2026-09-30
---

HQLA bị ràng buộc (encumbered) hoặc được sử dụng trong giao dịch repo cần được điều chỉnh giá trị hoặc loại bỏ khỏi LCR, tùy thuộc vào mức độ cam kết và kỳ hạn giao dịch (sbv_circular_22_final, Phụ lục I Phần A, d.851–895).

**Nguyên tắc ràng buộc (Encumbrance):**

Tài sản được xem là ràng buộc khi nó được sử dụng làm bảo đảm cho một cam kít khác, bao gồm: (1) thế chấp cho khoản cấp tín dụng, (2) bảo đảm cho giao dịch repo/reverse repo, (3) bảo đảm cho hợp đồng phái sinh, (4) bảo đảm cho các cam kít bán ngoài bảng. Nếu tài sản bị ràng buộc một phần (ví dụ 40% là bảo đảm, 60% tự do), chỉ phần tự do được tính vào HQLA (sbv_circular_22_final, Phụ lục I Phần A, d.856–865).

**Công thức tính phần HQLA tự do:**

$$\text{HQLA tự do} = \text{Dư nợ tài sản} \times (1 - \text{Tỷ lệ ràng buộc})$$

**Ví dụ:** Ngân hàng nắm giữ trái phiếu CP trị giá 500 tỷ, trong đó 200 tỷ được thế chấp cho một khoản vay từ NHNN (tỷ lệ ràng buộc = 200/500 = 40%). Phần HQLA tính được = 500 × (1 − 40%) = 300 tỷ.

**Xử lý giao dịch Repo (Repurchase Agreement):**

Nếu ngân hàng vay tiền bằng cách thế chấp HQLA (repo), tài sản đó vẫn được tính vào HQLA nếu kỳ hạn repo ≤ 30 ngày và ngân hàng có quyền hoàn lại tiền trong 30 ngày. Nếu kỳ hạn > 30 ngày, tài sản được loại bỏ khỏi HQLA hoàn toàn (sbv_circular_22_final, Phụ lục I Phần A, d.866–880).

**Công thức xử lý Repo:**

$$\text{HQLA (repo)} = \begin{cases}
\text{Dư nợ tài sản} \times \text{Hệ số} & \text{nếu kỳ hạn repo} \leq 30 \text{ ngày} \\
0 & \text{nếu kỳ hạn repo} > 30 \text{ ngày}
\end{cases}$$

**Đảo ngược Repo (Reverse Repo):**

Khi ngân hàng cho vay tiền bằng cách nhận tài sản làm bảo đảm (reverse repo), tài sản nhận được có thể được tính vào HQLA nếu: (1) tài sản đó có chất lượng từ Cấp 1 trở lên, (2) kỳ hạn reverse repo ≤ 30 ngày, (3) ngân hàng có quyền yêu cầu hoàn lại tiền trước 30 ngày. Khi ngân hàng lưu giữ tài sản reverse repo, nó phải được tính vào HQLA sau khi trừ đi giá trị tiền phải trả lại theo hợp đồng (sbv_circular_22_final, Phụ lục I Phần A, d.881–895).

**Công thức Reverse Repo:**

$$\text{HQLA (reverse repo)} = \text{Giá trị tài sản nhận} - \text{Khoản tiền phải trả lại} - \text{Haircut}$$

Haircut áp dụng nếu tài sản nhận là Cấp 2B (ví dụ: tài sản RMBS nhận được = 1.000 tỷ, tiền phải trả = 980 tỷ, haircut 25% = 0 tỷ → HQLA = 1.000 − 980 − 0 = 20 tỷ).

**Điều chỉnh rủi ro thị trường (Valuation):**

Nếu giá trị thị trường của HQLA giảm đáng kể (ví dụ: cổ phiếu giảm > 35% trong một ngày), ngân hàng phải điều chỉnh giá trị HQLA xuống để phản ánh rủi ro thực tế. Trường hợp tài sản bị downgrade xếp hạng, nó phải được reclassify sang cấp thấp hơn hoặc loại bỏ (sbv_circular_22_final, Phụ lục I Phần A, d.896–920).

[[lcr-hqla-definition-framework]] định nghĩa LCR tổng quan. [[hqla-tier-1-criteria-formula]], [[hqla-tier-2a-criteria-calculation]], [[hqla-tier-2b-criteria-haircut]] chi tiết từng cấp tài sản.
