---
title: standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule
type: concept
tags: [banking, alm, irrbb, cash-flow-bucketing, repricing-schedule, time-buckets, bcbs-368, eve-discounting]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Lịch 19 dải kỳ hạn định giá lại chuẩn hóa (The nineteen-bucket maturity schedule) thiết lập cấu trúc phân tầng thời gian thống nhất bắt buộc trong Khung đo lường chuẩn hóa IRRBB của Ủy ban Basel, yêu cầu ngân hàng ánh xạ toàn bộ dòng tiền định giá lại danh nghĩa tương lai của các tài sản, nợ phải trả và cam kết ngoại bảng nhạy cảm với lãi suất nhằm định lượng biến thiên giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) (bcbs_368, file d368.md, Section IV.2.1, d.559–596; Paragraph 101–104).

Khung 19 dải kỳ hạn được thiết kế với độ phân giải cao tại các kỳ hạn ngắn và trung hạn nhằm kiểm soát chặt chẽ rủi ro định giá lại nội dải (intra-bucket mismatch risk), triệt tiêu giả định sai lệch rằng các dòng tiền phát sinh tại các thời điểm khác nhau trong cùng một khoảng thời gian có thể bù trừ hoàn hảo cho nhau (bcbs_368, file d368.md, Footnote 27, d.781).

**Phạm vi ghi nhận và nguyên tắc loại trừ công cụ tài chính**

Ngân hàng phải phóng chiếu toàn bộ dòng tiền định giá lại danh nghĩa phát sinh từ mọi hợp đồng tài chính nhạy cảm với lãi suất trên sổ ngân hàng theo từng đồng tiền riêng biệt (Paragraph 101):
- *Tài sản nhạy cảm lãi suất*: Bao gồm mọi tài sản sinh lời, ngoại trừ các tài sản bị khấu trừ trực tiếp khỏi Vốn cổ phần phổ thông Cấp 1 (CET1) theo chuẩn Basel III, và loại trừ hoàn toàn tài sản cố định hữu hình/vô hình (bất động sản, máy móc) cùng các khoản đầu tư vốn cổ phần (equity exposures) trên sổ ngân hàng.
- *Nợ phải trả nhạy cảm lãi suất*: Bao gồm mọi nghĩa vụ nợ, tiền gửi của khách hàng, kể cả tiền gửi không chịu lãi suất (non-remunerated deposits), nhưng loại trừ hoàn toàn vốn tự có Cấp 1 (CET1 capital).
- *Cam kết ngoại bảng*: Bao gồm các hợp đồng phái sinh lãi suất (hoán đổi IRS, kỳ hạn FRA, tương lai futures) và các cam kết cấp tín dụng/thanh khoản có điều kiện.

**Bảng chuẩn 19 dải kỳ hạn và tọa độ điểm giữa (Time bucket midpoints $t_k$)**

Các dòng tiền được phân bổ theo ngày định giá lại vào 19 khoảng kỳ hạn ($k \in \{1,\dots,19\}$) hoặc gắn trực tiếp vào tọa độ điểm giữa danh nghĩa của dải kỳ hạn ($t_k$ tính bằng năm) theo Bảng 1 chuẩn hóa của Basel (bcbs_368, file d368.md, Table 1, d.589–596):

| Nhóm kỳ hạn | Chỉ số $k$ | Khoảng kỳ hạn định giá lại ($t_{CF}$) | Tọa độ điểm giữa $t_k$ (năm) | Ghi chú quy chuẩn |
|---|---|---|---|---|
| **Lãi suất ngắn hạn (Short-term rates)** | $k=1$ | Qua đêm (Overnight) | $t_1 = 0{,}0028$ năm | Tương đương $1/365$ ngày |
| | $k=2$ | Qua đêm $< t_{CF} \le 1$ tháng | $t_2 = 0{,}0417$ năm | Trung bình 0,5 tháng |
| | $k=3$ | $1$ tháng $< t_{CF} \le 3$ tháng | $t_3 = 0{,}1667$ năm | Trung bình 2 tháng |
| | $k=4$ | $3$ tháng $< t_{CF} \le 6$ tháng | $t_4 = 0{,}3750$ năm | Trung bình 4,5 tháng |
| | $k=5$ | $6$ tháng $< t_{CF} \le 9$ tháng | $t_5 = 0{,}6250$ năm | Trung bình 7,5 tháng |
| | $k=6$ | $9$ tháng $< t_{CF} \le 1$ năm | $t_6 = 0{,}8750$ năm | Trung bình 10,5 tháng |
| | $k=7$ | $1$ năm $< t_{CF} \le 1{,}5$ năm | $t_7 = 1{,}2500$ năm | Điểm giữa 1,25 năm |
| | $k=8$ | $1{,}5$ năm $< t_{CF} \le 2$ năm | $t_8 = 1{,}7500$ năm | Điểm giữa 1,75 năm |
| **Lãi suất trung hạn (Medium-term rates)** | $k=9$ | $2$ năm $< t_{CF} \le 3$ năm | $t_9 = 2{,}5000$ năm | Điểm giữa 2,5 năm |
| | $k=10$ | $3$ năm $< t_{CF} \le 4$ năm | $t_{10} = 3{,}5000$ năm | Điểm giữa 3,5 năm |
| | $k=11$ | $4$ năm $< t_{CF} \le 5$ năm | $t_{11} = 4{,}5000$ năm | Điểm giữa 4,5 năm |
| | $k=12$ | $5$ năm $< t_{CF} \le 6$ năm | $t_{12} = 5{,}5000$ năm | Điểm giữa 5,5 năm |
| | $k=13$ | $6$ năm $< t_{CF} \le 7$ năm | $t_{13} = 6{,}5000$ năm | Điểm giữa 6,5 năm |
| **Lãi suất dài hạn (Long-term rates)** | $k=14$ | $7$ năm $< t_{CF} \le 8$ năm | $t_{14} = 7{,}5000$ năm | Điểm giữa 7,5 năm |
| | $k=15$ | $8$ năm $< t_{CF} \le 9$ năm | $t_{15} = 8{,}5000$ năm | Điểm giữa 8,5 năm |
| | $k=16$ | $9$ năm $< t_{CF} \le 10$ năm | $t_{16} = 9{,}5000$ năm | Điểm giữa 9,5 năm |
| | $k=17$ | $10$ năm $< t_{CF} \le 15$ năm | $t_{17} = 12{,}5000$ năm | Điểm giữa 12,5 năm |
| | $k=18$ | $15$ năm $< t_{CF} \le 20$ năm | $t_{18} = 17{,}5000$ năm | Điểm giữa 17,5 năm |
| | $k=19$ | $t_{CF} > 20$ năm | $t_{19} = 25{,}0000$ năm | Điểm giả định 25 năm |

Khi ngân hàng lựa chọn phương án phân bổ vào điểm giữa ($t_k$), các dòng tiền rơi vào giữa hai điểm giữa liền kề bắt buộc phải được chia nhỏ (splitting up) giữa hai điểm giữa đó theo tỷ trọng thời gian tương ứng nhằm bảo toàn hoàn hảo kỳ hạn thực tế của dòng tiền (Paragraph 101).

**Định nghĩa và quy tắc bóc tách dòng tiền định giá lại danh nghĩa ($CF(k)$)**

Một dòng tiền định giá lại danh nghĩa $CF(k)$ được Ủy ban Basel cấu thành từ 3 thành tố hợp đồng (bcbs_368, file d368.md, Paragraph 102, d.569–585):
1. *Dòng tiền hoàn trả nợ gốc (Repayment of principal)*: Phát sinh tại ngày đáo hạn hợp đồng (contractual maturity) hoặc theo lịch trình trả nợ định kỳ (amortisation schedule).
2. *Dòng tiền định giá lại nợ gốc (Repricing of principal)*: Xảy ra tại ngày sớm nhất mà ngân hàng hoặc đối tác có quyền đơn phương thay đổi lãi suất hợp đồng, hoặc ngày mà lãi suất của công cụ thả nổi tự động thay đổi theo chỉ số chuẩn tham chiếu bên ngoài.
3. *Dòng tiền thanh toán lãi coupon (Interest payment)*: Phát sinh trên phần nợ gốc chưa được hoàn trả hoặc chưa được định giá lại. Quy định Basel nhấn mạnh nguyên tắc kỹ thuật cốt lõi: phần bù biên độ (spread component) của lãi suất không bị định giá lại bắt buộc phải được phân bổ liên tục cho đến ngày đáo hạn hợp đồng cuối cùng của nợ gốc, bất kể phần nợ gốc cơ sở đã bị định giá lại hay chưa (Paragraph 102 & 104).

**Quy tắc xử lý công cụ thả nổi và biên độ thương mại**

- *Công cụ lãi suất thả nổi (Floating rate positions)*: Toàn bộ nợ gốc được ấn định dồn vào dải kỳ hạn rơi vào ngày định giá lại kế tiếp (first reset date), với giả định giá trị thị trường của nợ gốc sẽ hoàn trả về mệnh giá (reset to par). Sau ngày tái thiết lập đầu tiên này, không còn dòng tiền nợ gốc nào được phân bổ vào các dải kỳ hạn sau, ngoại trừ phần biên độ lãi suất cố định (spread) được duy trì đến kỳ hạn cuối (Paragraph 104 & 106).
- *Khấu trừ biên độ thương mại (Commercial margins deduction)*: Ngân hàng có quyền lựa chọn khấu trừ biên độ thương mại và các thành tố spread khác khỏi dòng tiền định giá lại danh nghĩa theo một phương pháp luận thận trọng, minh bạch và nhất quán (Paragraph 103). Nếu khấu trừ biên độ thương mại, dòng tiền chỉ phản ánh cấu phần lãi suất phi rủi ro và bắt buộc phải chiết khấu bằng đường cong zero-coupon phi rủi ro thuần túy; nếu giữ lại biên độ thương mại, đường cong chiết khấu phải được cộng thêm biên độ thương mại tương ứng (Paragraph 132.2 & Footnote 29).

Cấu trúc phân bổ 19 dải kỳ hạn này đóng vai trò là nền tảng kỹ thuật cho toàn bộ chu trình tính toán của [[irrbb-standardised-framework-five-stage-measurement-architecture]], tương thích chặt chẽ với quy tắc phân tầng tiền gửi không kỳ hạn tại [[standardised-nmd-categorisation-and-core-deposit-caps-framework]] và làm đầu vào trực tiếp cho thuật toán chiết khấu giá trị kinh tế tại [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
