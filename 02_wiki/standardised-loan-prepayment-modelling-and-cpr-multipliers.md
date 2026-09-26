---
title: standardised-loan-prepayment-modelling-and-cpr-multipliers
type: concept
tags: [banking, alm, irrbb, prepayment-risk, cpr, fixed-rate-loans, behavioural-modelling, bcbs-368]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Mô hình hóa trả nợ trước hạn chuẩn hóa và hệ số nhân CPR (Standardised Loan Prepayment Modelling and CPR Multipliers) thiết lập phương pháp luận định lượng hành vi trả nợ trước hạn của khách hàng cá nhân đối với các khoản cho vay lãi suất cố định trong Khung đo lường chuẩn hóa IRRBB của Ủy ban Basel, thông qua việc điều chỉnh tỷ lệ trả trước có điều kiện cơ sở ($CPR_{0,c}^p$) bằng ma trận hệ số nhân kịch bản ($\gamma_i$) (bcbs_368, file d368.md, Section IV.4, d.653–703; Paragraph 116–124; Table 3).

Rủi ro trả nợ trước hạn (prepayment risk) là một trong những dạng thức quyền chọn hành vi khách hàng nguy hiểm nhất đối với bảng cân đối của ngân hàng. Đặc tính bất đối xứng này tạo ra độ lồi âm (negative convexity) cho danh mục cho vay cố định: khi lãi suất thị trường giảm, người vay có xu hướng tất toán hợp đồng sớm để tìm kiếm nguồn tài trợ mới với lãi suất thấp hơn (buộc ngân hàng phải tái đầu tư dòng vốn thu hồi vào tài sản có lợi suất thấp); ngược lại, khi lãi suất thị trường tăng, người vay trì hoãn việc trả nợ, khiến thời lượng thực tế của khoản vay bị kéo dài (extension risk) ngay tại thời điểm mà giá trị hiện tại của tài sản bị chiết khấu nặng nề nhất.

**Phạm vi áp dụng và khái niệm trả nợ trước hạn không bồi hoàn**

Ủy ban Basel phân định nghiêm ngặt phạm vi áp dụng của mô hình hành vi trả nợ trước hạn chuẩn hóa (Paragraph 116 & 120):
- *Chỉ áp dụng cho đối tượng khách hàng bán lẻ (Retail customers)*: Các quyền chọn hành vi của khách hàng bán buôn (wholesale counterparties) không được áp dụng mô hình này mà bắt buộc phải bị bóc tách và đối xử như quyền chọn tự động (automatic interest rate options) tại Giai đoạn 4 với giả định khách hàng sẽ luôn hành động một cách tối ưu tài chính nhất gây thiệt hại tối đa cho ngân hàng (Paragraph 116 & Footnote 19, d.661).
- *Khoản cho vay chịu rủi ro trả nợ trước hạn không bồi hoàn (Uncompensated prepayments)*: Mô hình chuẩn hóa bắt buộc áp dụng cho các sản phẩm tín dụng lãi suất cố định mà ngân hàng không thu phí phạt đền bù chi phí kinh tế thực tế của việc tất toán trước hạn, hoặc chỉ áp dụng mức phí phạt mang tính tượng trưng hay chỉ phạt đối với phần trả trước vượt một ngưỡng tỷ lệ nhất định (Paragraph 120). Nếu hợp đồng vay có điều khoản phạt kinh tế toàn diện bù đắp đủ tổn thất lãi tái đầu tư và chi phí phá vỡ hợp đồng, ngân hàng được phép coi là tài sản cố định chuẩn hóa thuần túy.

**Hàm toán học CPR và ma trận hệ số nhân kịch bản (Table 3)**

Quy trình chuẩn hóa vận hành theo 2 bước:
1. *Xác định CPR cơ sở ($CPR_{0,c}^p$)*: Ngân hàng ước lượng hoặc cơ quan giám sát chỉ định tỷ lệ trả nợ trước hạn có điều kiện hàng năm cơ sở cho từng danh mục sản phẩm tín dụng đồng nhất $p$ bằng đồng tiền $c$ dưới cấu trúc kỳ hạn lãi suất hiện hành (Paragraph 121). CPR cơ sở có thể là một hằng số cố định hoặc biến thiên theo độ tuổi (seasoning) của khoản vay qua từng dải kỳ hạn $k$ ($CPR_{0,c}^p(k)$) (Footnote 21, d.685).
2. *Hiệu chỉnh CPR theo 6 kịch bản sốc lãi suất*: Tỷ lệ trả trước có điều kiện $CPR_{i,c}^p$ áp dụng cho kịch bản sốc $i$ được tính bằng cách nhân CPR cơ sở với hệ số nhân kịch bản $\gamma_i$ (Paragraph 122–123):

$$CPR_{i,c}^p = CPR_{0,c}^p \times \gamma_i$$

Hệ số nhân kịch bản $\gamma_i$ được quy định tại Bảng 3 của Chuẩn mực BCBS 368 (bcbs_368, file d368.md, Table 3, d.687–697):

| Kịch bản sốc lãi suất ($i$) | Tên kịch bản (Annex 2) | Hệ số nhân kịch bản $\gamma_i$ | Diễn giải cơ chế hành vi tài chính |
|---|---|---|---|
| **$i = 1$** | Tăng song song (Parallel up) | **$0{,}8$** | Mặt bằng lãi suất tăng toàn diện $\rightarrow$ Chi phí vay mới đắt đỏ $\rightarrow$ Động lực tái tài trợ giảm mạnh $\rightarrow$ CPR giảm $20\%$. |
| **$i = 2$** | Giảm song song (Parallel down) | **$1{,}2$** | Mặt bằng lãi suất giảm sâu $\rightarrow$ Động lực tất toán để vay mới lãi suất thấp tăng vọt $\rightarrow$ CPR tăng $20\%$. |
| **$i = 3$** | Cú sốc dốc (Steepener) | **$0{,}8$** | Lãi suất dài hạn tăng cao $\rightarrow$ Tái tài trợ khoản vay trung dài hạn không có lợi $\rightarrow$ CPR giảm $20\%$. |
| **$i = 4$** | Cú sốc phẳng (Flattener) | **$1{,}2$** | Lãi suất dài hạn hạ thấp tương đối $\rightarrow$ Khách hàng có xu hướng chốt lãi suất dài hạn thấp $\rightarrow$ CPR tăng $20\%$. |
| **$i = 5$** | Tăng ngắn hạn (Short rate up) | **$0{,}8$** | Chi phí thanh khoản ngắn hạn tăng $\rightarrow$ Ngân sách chi tiêu thắt chặt $\rightarrow$ Tốc độ trả nợ sớm suy giảm $\rightarrow$ CPR giảm $20\%$. |
| **$i = 6$** | Giảm ngắn hạn (Short rate down) | **$1{,}2$** | Chi phí tài trợ rẻ đi $\rightarrow$ Thanh khoản dồi dào kích thích tất toán trước hạn $\rightarrow$ CPR tăng $20\%$. |

**Thuật toán phân rã dòng tiền và cập nhật số dư qua 19 dải kỳ hạn**

Dòng tiền định giá lại danh nghĩa tại mỗi dải kỳ hạn $k \in \{1,\dots,19\}$ được cấu thành từ hai bộ phận: dòng tiền trả nợ theo hợp đồng (đã điều chỉnh theo tốc độ suy giảm số dư) và dòng tiền trả nợ trước hạn thực tế (Paragraph 124, d.698–703):

$$CF_{i,c}^p(k) = CF_{i,c}^S(k) + CPR_{i,c}^p \cdot N_{i,c}^p(k-1)$$

Trong đó:
- $CF_{i,c}^S(k)$ là dòng tiền trả nợ gốc và lãi theo hợp đồng cơ sở trong dải kỳ hạn $k$;
- $N_{i,c}^p(k-1)$ là số dư nợ danh nghĩa còn lại của danh mục tại thời điểm kết thúc dải kỳ hạn $k-1$;
- $CPR_{i,c}^p \cdot N_{i,c}^p(k-1)$ là lượng nợ gốc được trả trước không bồi hoàn, phát sinh và được ghi nhận toàn bộ vào dải kỳ hạn $k$.

Số dư nợ danh nghĩa chuyển tiếp sang dải kỳ hạn tiếp theo được cập nhật suy giảm tương ứng:

$$N_{i,c}^p(k) = N_{i,c}^p(k-1) - \text{Gốc theo hợp đồng}_k - \left( CPR_{i,c}^p \cdot N_{i,c}^p(k-1) \right)$$

Quy trình điều chỉnh động này làm thay đổi phân bổ dòng tiền trên trục thời gian của 19 dải kỳ hạn tại [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]], cấu thành dữ liệu đầu vào không thể thiếu cho giai đoạn chiết khấu giá trị kinh tế tại [[irrbb-standardised-framework-five-stage-measurement-architecture]] và [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
