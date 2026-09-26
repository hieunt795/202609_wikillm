---
title: counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure
type: concept
tags: [banking, ccr, counterparty-credit-risk, derivatives, pfe, replacement-cost, regulation]
sources: [sbv_circular_14_2025]
status: stable
last_updated: 2026-09-26
---

Khuôn khổ đo lường rủi ro tín dụng đối tác (Counterparty Credit Risk - CCR) đối với các giao dịch phái sinh theo Thông tư 14/2025/TT-NHNN định lượng tổn thất tiềm tàng phát sinh khi đối tác giao dịch vỡ nợ trước thời điểm thanh toán dứt điểm dòng tiền của hợp đồng (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 1–4, d.740–783). Khác với rủi ro tín dụng truyền thống của các khoản cho vay thông thường (nơi bên vay luôn nợ ngân hàng một giá trị danh nghĩa xác định), phơi nhiễm trong các giao dịch sản phẩm phái sinh mang tính chất hai chiều và biến động phi tuyến tính theo thời gian phụ thuộc vào giá trị thị trường của các tài sản tài chính cơ sở. Ngân hàng chỉ gánh chịu rủi ro tín dụng đối tác khi hợp đồng phái sinh đang ở trạng thái có lãi (In-the-Money), tức giá trị thị trường thay thế của hợp đồng mang dấu dương.

Tài sản có tính theo rủi ro tín dụng đối tác của giao dịch phái sinh thứ $j$ ($RWA_{CCRj}$) được xác định dựa trên mức phơi nhiễm khi đối tác vỡ nợ nhân với hệ số rủi ro tín dụng của đối tác ($CRW$) (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4, d.740–743):

$$RWA_{CCRj} = \max(RC_j + PFE_j - C_j, 0) \times CRW$$

Trong đó mức phơi nhiễm gộp được phân tách thành hai thành phần kinh tế độc lập: Chi phí thay thế hiện tại ($RC_j$) và Giá trị tương lai trạng thái rủi ro ($PFE_j$), sau đó giảm trừ giá trị tài sản bảo đảm hợp lệ ($C_j$).

Chi phí thay thế hiện tại ($RC_j$ - Current Replacement Cost) phản ánh tổn thất kinh tế tức thời mà ngân hàng phải gánh chịu nếu đối tác tuyên bố vỡ nợ ngay tại thời điểm định giá (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.a, d.746). Đại lượng này được xác định theo giá trị thị trường (Mark-to-Market) của giao dịch thay thế tương đương; nếu giá trị thị trường âm (ngân hàng đang ở vị thế nợ đối tác), $RC_j$ được gán bằng 0 do ngân hàng không phải chịu rủi ro tín dụng khi đối tác vỡ nợ.

Giá trị tương lai trạng thái rủi ro ($PFE_j$ - Potential Future Exposure) lượng hóa mức tăng phơi nhiễm tiềm năng trong khoảng thời gian từ thời điểm hiện tại cho đến khi hợp đồng đáo hạn do biến động thị trường bất lợi (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.b, d.747–759). $PFE_j$ được tính bằng tích số giữa giá trị vốn gốc danh nghĩa của hợp đồng với chỉ số tăng thêm quy định (Add-on factor):

$$PFE_j = \text{Vốn danh nghĩa} \times \text{Hệ số Add-on}$$

Hệ số Add-on được Ngân hàng Nhà nước chuẩn hóa thông qua ma trận hai chiều dựa trên tính chất biến động của loại tài sản tài chính cơ sở và thời hạn hiệu lực còn lại của hợp đồng (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.b, d.749–759):
- **Phái sinh lãi suất**: Áp dụng mức Add-on $0{,}0\%$ cho kỳ hạn $\le 1$ năm; $0{,}5\%$ cho kỳ hạn từ trên 1 đến 5 năm; và $1{,}5\%$ cho kỳ hạn trên 5 năm. Riêng đối với sản phẩm hoán đổi lãi suất thả nổi/thả nổi một đồng tiền (Basis Swap), Thông tư miễn trừ tính $PFE_j$ ($PFE = 0$) và chỉ tính rủi ro theo chi phí thay thế $RC_j$ do hai vế thả nổi tự triệt tiêu phần lớn rủi ro trôi dạt giá trị dài hạn (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.b.(v), d.766).
- **Phái sinh ngoại hối và vàng tiêu chuẩn**: Áp dụng mức $1{,}0\%$ ($\le 1$ năm); $5{,}0\%$ (1–5 năm); và $7{,}5\%$ ($> 5$ năm).
- **Phái sinh cổ phiếu và chứng chỉ quỹ**: Áp dụng mức $6{,}0\%$ ($\le 1$ năm); $8{,}0\%$ (1–5 năm); và $10{,}0\%$ ($> 5$ năm).
- **Kim loại quý (trừ vàng)**: Áp dụng mức $7{,}0\%$ cho kỳ hạn đến 5 năm và $8{,}0\%$ cho kỳ hạn trên 5 năm.
- **Hàng hóa khác**: Chịu biên độ biến động lớn nhất với Add-on từ $10{,}0\%$ ($\le 1$ năm), $12{,}0\%$ (1–5 năm) đến $15{,}0\%$ ($> 5$ năm).
- **Phái sinh tín dụng** (Hợp đồng hoán đổi tổng lợi nhuận TRS và Hợp đồng hoán đổi vỡ nợ tín dụng CDS): Áp dụng mức Add-on cố định $5{,}0\%$ nếu tài sản tham chiếu có xếp hạng tín nhiệm đầu tư (Baa/BBB trở lên), và áp dụng mức $10{,}0\%$ nếu tài sản tham chiếu không đủ chuẩn đầu tư (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.b.(vi), d.767–780).

Tài sản bảo đảm nhận về ($C_j$) chỉ được khấu trừ vào phơi nhiễm khi đáp ứng đầy đủ điều kiện hợp lệ và phải áp dụng chiết khấu biến động giá ($H_c$) cùng chiết khấu độ lệch tiền tệ $H_{fx} = 8\%$ (sbv_circular_14_2025, file TT14_2.md, Phụ lục II Mục 4.c, d.781).

Đại lượng $RWA_{CCR}$ phái sinh được hợp nhất vào tổng tài sản có rủi ro tín dụng tại [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]], phối hợp với kỹ thuật giảm thiểu rủi ro tại [[credit-risk-mitigation-framework-recognizes-collateral-netting-guarantees-and-derivatives]], và chi phối trực tiếp tỷ lệ an toàn vốn tổng thể theo [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]].
