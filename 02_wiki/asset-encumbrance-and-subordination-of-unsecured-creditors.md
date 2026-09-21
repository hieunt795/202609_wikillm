---
title: asset-encumbrance-and-subordination-of-unsecured-creditors
type: concept
tags: [monetary, central-banking, asset-encumbrance, collateral-framework, credit-risk]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

Vấn đề ràng buộc tài sản và sự thứ cấp hóa các chủ nợ không bảo đảm (asset encumbrance problem and subordination of unsecured creditors) được Bindseil (2014, Ch.12, §12.3, d.2699–2772) phân tích nhằm vạch rõ mặt trái của việc ngân hàng thương mại phụ thuộc quy mô lớn vào tái cấp vốn có bảo đảm từ ngân hàng trung ương.

**Bản chất của hiện tượng ràng buộc tài sản (asset encumbrance)**: Khi thị trường liên ngân hàng và thị trường vốn không bảo đảm đóng băng, các ngân hàng thương mại (đặc biệt tại các nước ngoại vi Eurozone như Tây Ban Nha, Bồ Đào Nha, Ireland, Hy Lạp giai đoạn 2011–2012) buộc phải thế chấp phần lớn tài sản chất lượng trên bảng cân đối kế toán để vay vốn từ NHTW hoặc phát hành trái phiếu có bảo đảm (covered bonds) (Fitch Ratings, 2013). Khi một tài sản bị đem đi cầm cố cho NHTW, nó trở thành "tài sản bị ràng buộc" (encumbered asset) và được ưu tiên tuyệt đối để thanh toán cho NHTW trong trường hợp phá sản, nằm ngoài tầm với của các chủ nợ không bảo đảm và người gửi tiền thông thường (bindseil_monetary_policy, Ch.12, §12.3, d.2720–2724).

**Mô hình hóa tổn thất khi vỡ nợ của chủ nợ không bảo đảm**: Xét bảng cân đối kế toán ngân hàng có quy mô tổng tài sản là 1, vốn chủ sở hữu $E$, tiền gửi và nợ không bảo đảm $D$, và tín dụng tái cấp vốn từ NHTW là $1 - D - E$. Giả sử trong trường hợp vỡ nợ do mất khả năng thanh toán (xác suất $\Phi(-E/\sigma_\epsilon)$), tỷ lệ tổn thất cơ sở khi thanh lý tài sản là $LGD = 50\%$ (tương đương tỷ lệ thu hồi $rr = 1 - LGD = 50\%$).
- Do NHTW áp dụng tỷ lệ chiết khấu bình quân $\bar{h} > 0$ trên danh mục thế chấp theo hàm lũy thừa $h(x) = x^\delta$, để vay được khoản vốn $1 - D - E$, ngân hàng phải cầm cố một khối lượng tài sản $C$ lớn hơn nhiều so với giá trị khoản vay:
$$C = \frac{1 - D - E}{1 - \bar{h}} > 1 - D - E$$
- Khi vỡ nợ xảy ra, NHTW thu giữ toàn bộ khối tài sản $C$. Khối tài sản còn lại để thanh toán cho các chủ nợ không bảo đảm $D$ chỉ là:
$$\text{Tài sản còn lại} = rr(1 - E) - C$$
- Từ đó, tỷ lệ thu hồi hiệu dụng $rr^\#$ và tỷ lệ tổn thất hiệu dụng $LGD^\#$ của các chủ nợ không bảo đảm bị đội lên theo công thức 12.8 của Bindseil:
$$LGD^\# = 1 - \frac{rr(1 - E) - C}{D}$$

**Hiệu ứng thứ cấp hóa và vòng xoáy loại trừ thị trường (Bảng 12.3)**:
- *Khi mức phụ thuộc NHTW là 10% ($D = 0.8, E = 0.1$)*: Nếu haircut rất chặt chẽ ($\delta = 0.1 \implies \bar{h} \approx 72\%$), ngân hàng phải thế chấp tới $C = 0.36$ tài sản để vay $0.10$ vốn. Tỷ lệ tổn thất $LGD^\#$ của người gửi tiền vọt từ mức chuẩn 50% lên **66%**, đẩy phần bù rủi ro lãi suất tăng thêm 32 bps.
- *Khi mức phụ thuộc NHTW là 20% ($D = 0.7, E = 0.1$)*: Với cùng mức chiết khấu trên, khối lượng tài sản bị phong tỏa lên tới $C = 0.88$ (chiếm 88% toàn bộ tài sản ngân hàng). Khi vỡ nợ, người gửi tiền và chủ nợ không bảo đảm mất trắng gần như toàn bộ (**$LGD^\# = 99\%$**), và phần bù lãi suất đòi hỏi tăng thêm 98 bps (bindseil_monetary_policy, Ch.12, §12.3, d.2751–2769).
- *Hiệu ứng kép từ giảm giá trị định giá*: Trong thực tế khủng hoảng nợ công Eurozone, tài sản thế chấp bị giảm giá trị định giá thị trường trầm trọng (trái phiếu chính phủ Bồ Đào Nha bị định giá dưới 50%, Hy Lạp dưới 20%), tương đương với việc gánh thêm một tầng haircut bổ sung, đẩy $C$ lên mức kịch trần bảng cân đối.

**Hệ quả đối với ổn định tài chính**: Sự gia tăng asset encumbrance tạo ra một hiệu ứng phụ nguy hiểm: việc NHTW càng bảo vệ an toàn cho bảng cân đối của mình bằng haircut cao thì càng làm trầm trọng hóa sự thứ cấp hóa (structural subordination) của các chủ nợ tư nhân. Điều này khiến các nhà đầu tư bán buôn và người gửi tiền hoảng sợ rút vốn, kích hoạt [[bank-runs-investor-strikes-and-multiple-equilibria|đình công đảo nợ và rút tiền hàng loạt]], đẩy ngân hàng lún sâu hơn vào [[relative-vs-absolute-central-bank-intermediation|trung gian tuyệt đối của NHTW]].
