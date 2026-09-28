---
title: haircuts-as-effective-leverage-constraints-and-zero-lower-bound-transmission
type: concept
tags: [monetary, central-banking, collateral-framework, haircuts, leverage-constraints, zero-lower-bound, wicksellian-rate]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-28
---

Tỷ lệ chiết khấu tài sản bảo đảm như trần đòn bẩy hiệu dụng và cơ chế truyền dẫn tiền tệ tại chặn dưới lãi suất bằng không (haircuts as effective leverage constraints and zero lower bound transmission) được Ulrich Bindseil hình thức hóa toán học nhằm giải thích vai trò của chính sách tài sản thế chấp khi công cụ lãi suất truyền thống bị vô hiệu hóa (bindseil_monetary_policy, d.2466–2485). Dựa trên mô hình của Ashcraft và cộng sự (2011), tỷ lệ chiết khấu (haircut $h$) mà ngân hàng trung ương (NHTW) áp đặt lên tài sản thế chấp đóng vai trò ấn định trần đòn bẩy tối đa mà hệ thống ngân hàng có thể huy động thông qua các nghiệp vụ vay mượn từ NHTW.

Khi tài sản của hệ thống tài chính được tài trợ kết hợp giữa vốn chủ sở hữu và nguồn vốn vay mượn có bảo đảm từ NHTW, chi phí tài trợ bình quân của nền kinh tế ($i^\#$) được xác định bằng bình quân gia quyền giữa chi phí ngầm định của vốn tự có ($i_e$ - shadow cost of equity) và lãi suất tái cấp vốn của NHTW ($i^*$):
$$i^\# = h \cdot i_e + (1 - h) \cdot i^*$$
Giả định phổ tài sản khả dụng là một chuỗi liên tục $x \in [0, 1]$ được sắp xếp theo trật tự thanh khoản tăng dần, và hàm chiết khấu tuân theo quy luật lũy thừa $h(x) = x^\delta$ với tham số độ cong $\delta > 0$ (bindseil_monetary_policy, d.2468). Khi đó, tỷ lệ chiết khấu bình quân toàn hệ thống là $\frac{1}{\delta + 1}$ và tiềm năng vay vốn sau chiết khấu (central bank borrowing potential - $CVPH$) là $\frac{\delta}{\delta + 1}$. Phương trình chi phí tài trợ vốn bình quân trở thành:
$$i^\# = \frac{1}{\delta + 1} i_e + \frac{\delta}{\delta + 1} i^*$$

Trong trạng thái cân bằng vĩ mô theo lý thuyết Wicksell, để nền kinh tế không bị rơi vào áp lực lạm phát hay giảm phát, chi phí tài trợ vốn danh nghĩa mục tiêu $i^\#$ phải bằng lãi suất thực tự nhiên $r$ (lợi suất hoàn vốn tự nhiên của tư bản) cộng với lạm phát kỳ vọng $E(\pi)$, tức là $i^\# = r + E(\pi)$ (bindseil_monetary_policy, d.2468). Từ đó, mức lãi suất tái cấp vốn trung hòa của NHTW ($i^*$) được thiết lập theo phương trình:
$$i^* = \frac{r + E(\pi) - \frac{1}{\delta^* + 1} i_e}{\frac{\delta^*}{\delta^* + 1}}$$
trong đó $\delta^*$ là tham số chiết khấu tối ưu được xác định thuần túy dựa trên các nguyên tắc quản trị rủi ro tài chính của NHTW trong thời bình (bindseil_monetary_policy, d.2472).

Mô hình này làm sáng tỏ sự bế tắc của chính sách tiền tệ truyền thống khi nền kinh tế chạm chặn dưới lãi suất bằng 0 ([[monetary-policy-transmission-breakdown-and-zero-lower-bound|Zero Lower Bound - ZLB]]) (bindseil_monetary_policy, d.2478). Giả định trong trạng thái bình thường, lạm phát kỳ vọng $E(\pi) = 2\%$, chi phí vốn chủ sở hữu $i_e = 10\%$, và tham số chiết khấu chuẩn tắc là $\delta^* = 1$ (tương ứng tỷ lệ chiết khấu bình quân là $50\%$).
- Khi lãi suất thực tự nhiên $r = 4\%$, mức lãi suất điều hành tối ưu của NHTW là:
  $$i^* = \frac{4\% + 2\% - 0{,}5 \times 10\%}{0{,}5} = \frac{6\% - 5\%}{0{,}5} = 2\%$$
- Giả sử một cú sốc vĩ mô tiêu cực làm lãi suất tự nhiên sụp đổ xuống $r = 2\%$. Để duy trì lập trường tiền tệ trung hòa, lãi suất danh nghĩa mục tiêu cần thiết phải là:
  $$i^* = \frac{2\% + 2\% - 0{,}5 \times 10\%}{0{,}5} = \frac{4\% - 5\%}{0{,}5} = -2\%$$
Do vướng rào cản kỹ thuật ZLB ($i^* \ge 0$), NHTW không thể cắt giảm lãi suất xuống mức âm $-2\%$. Nếu NHTW chỉ hạ lãi suất điều hành về kịch sàn $0\%$, chi phí tài trợ bình quân của nền kinh tế vẫn kẹt ở mức $i^\# = 0{,}5 \times 10\% + 0{,}5 \times 0\% = 5\%$, cao hơn đáng kể so với mức trung hòa $r + E(\pi) = 4\%$. Sự thắt chặt tiền tệ cưỡng bức này sẽ đẩy nền kinh tế rơi vào vòng xoáy giảm phát và đình trệ.

Lối thoát chính sách phi quy ước qua công cụ tài sản bảo đảm: Bindseil chứng minh rằng khi chạm ZLB, NHTW buộc phải từ bỏ nguyên tắc xác định chiết khấu thuần túy theo khẩu vị rủi ro tài chính để đưa tham số chiết khấu trở thành một công cụ kích thích tiền tệ chủ động (bindseil_monetary_policy, d.2478). Bằng cách chủ động nới lỏng khuôn khổ tài sản bảo đảm — nâng tham số $\delta$ từ $\delta^* = 1$ lên $\delta = 5$ (làm tỷ lệ chiết khấu bình quân giảm từ $50\%$ xuống chỉ còn $1/6 \approx 16{,}7\%$, mở rộng đòn bẩy tái cấp vốn lên $5/6 \approx 83{,}3\%$) — NHTW kéo giảm chi phí tài trợ bình quân $i^\#$ của toàn hệ thống và khôi phục lập trường tiền tệ trung hòa ở mức lãi suất điều hành dương $i^* = 1\%$ mà không cần phá vỡ rào cản ZLB (bindseil_monetary_policy, d.2478–2480). Kết nối mở rộng: [[collateral-scarcity-and-effective-term-funding-costs]], [[market-impact-of-collateral-framework-and-leverage-constraints]], [[central-bank-collateral-framework-design-and-risk-control]].
