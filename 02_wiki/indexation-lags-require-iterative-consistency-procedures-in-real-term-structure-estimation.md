---
title: indexation-lags-require-iterative-consistency-procedures-in-real-term-structure-estimation
type: concept
tags: [inflation-linked-bonds, indexation-lag, real-term-structure, curve-fitting, cubic-spline, iterative-calibration]
sources: [choudhry_analysing_yield_curve]
status: draft
last_updated: 2026-09-28
---

Ước lượng cấu trúc kỳ hạn thực (real term structure estimation) đối mặt với rào cản kỹ thuật đặc thù do bản chất dòng tiền của trái phiếu liên kết lạm phát phụ thuộc vào chỉ số giá tiêu dùng nhưng lại chịu một độ trễ chỉ số hóa cố định (indexation lag) (choudhry_analysing_yield_curve, Ch.7, Index-Linked Bonds and Real Yields, d.3338; The Term Structure of Implied Forward Inflation Rates, d.3374).

Vì lý do kỹ thuật thu thập và công bố chỉ số giá của cơ quan thống kê quốc gia, các thị trường trái phiếu chính phủ đều áp dụng một khoảng thời gian trễ nhất định giữa thời điểm chốt chỉ số lạm phát và ngày chi trả dòng tiền (chẳng hạn 8 tháng đối với UK Index-Linked Gilts phát hành trước năm 2005, hoặc 3 tháng đối với các đợt phát hành sau 2005 và US TIPS) (choudhry_analysing_yield_curve, Ch.7, d.3338, d.3374, d.3412). Độ trễ này tạo ra nghịch lý phụ thuộc luẩn quẩn: để tính toán được lợi suất thực tế của trái phiếu từ giá thị trường quan sát được, người phân tích bắt buộc phải đưa vào một giả định về tỷ lệ lạm phát tương lai; tuy nhiên, mức lạm phát giả định này lại trực tiếp quyết định hình thái của đường cong lợi suất thực và đường cong lạm phát ngụ ý được ước lượng (choudhry_analysing_yield_curve, Ch.7, d.3374, d.3410).

Để xây dựng cấu trúc kỳ hạn thực từ giá thị trường, phương pháp khớp hàm chiết khấu của McCulloch (1971) được mở rộng áp dụng cho danh mục trái phiếu chỉ số hóa (choudhry_analysing_yield_curve, Ch.7, Fitting the Discount Function, d.3382–3403). Phương trình định giá trái phiếu truyền thống:
$$P_i = \sum_{t=1}^{T_i} C_i \cdot df(t) + M_i \cdot df(T_i)$$
được tham số hóa bằng cách biểu diễn hàm chiết khấu $df(t)$ thành tổ hợp tuyến tính của $k$ hàm cơ sở độc lập tuyến tính $f_j(t)$ (choudhry_analysing_yield_curve, Ch.7, Fitting the Discount Function, d.3390–3394):
$$df(t) = 1 + \sum_{j=1}^k a_j f_j(t)$$
Đối với trái phiếu liên kết lạm phát, theo Deacon và Derry (1994), phương trình định giá được hiệu chỉnh thông qua một hệ số tỷ lệ co giãn $\Delta_i$ xác định cho từng trái phiếu dựa trên tỷ số chỉ số giá bán lẻ (RPI) tại thời điểm dòng tiền so với chỉ số RPI cơ sở tại thời điểm phát hành (choudhry_analysing_yield_curve, Ch.7, Fitting the Discount Function, d.3394–3403):
$$\Delta_i = \frac{\text{RPI}_t}{\text{RPI}_{\text{base}, i}}$$
Do độ trễ quy định, $\text{RPI}_{\text{base}, i}$ được chốt tại thời điểm 8 tháng (hoặc 3 tháng) trước ngày phát hành (choudhry_analysing_yield_curve, Ch.7, d.3412). Đối với các dòng tiền tương lai vượt quá kỳ công bố dữ liệu RPI thực tế, giá trị $\text{RPI}_t$ được ngoại suy bằng cách kết hợp số liệu RPI mới nhất với quỹ đạo lạm phát giả định $\pi^e$ (choudhry_analysing_yield_curve, Ch.7, d.3402). Hệ số hồi quy $a_j$ được ước lượng bằng phương pháp bình phương tối thiểu có trọng số sau khi nhân hệ số co giãn $\Delta_i$ vào từng dòng tiền danh nghĩa kỳ vọng.

Sau khi khớp hàm chiết khấu thực, Bank of England và các chuyên gia định lượng áp dụng quy trình lặp nhất quán lạm phát để khử bỏ tính võ đoán của giả định ban đầu (choudhry_analysing_yield_curve, Ch.7, Deriving the Term Structure of Inflation Expectations, d.3406–3420):
1. Thiết lập giả định lạm phát phẳng ban đầu $\pi^e$ (thường là 3% hoặc 5%) để tính dòng tiền danh nghĩa dự phóng và xác định lợi suất thực tế ban đầu cho từng trái phiếu trong mẫu (choudhry_analysing_yield_curve, Ch.7, d.3410);
2. Sử dụng các mức lợi suất này để khớp hàm chiết khấu thực, từ đó suy ra đường cong lãi suất kỳ hạn thực tức thời $r(t)$ (choudhry_analysing_yield_curve, Ch.7, d.3410);
3. Trích xuất đường cong lạm phát kỳ hạn tức thời ngụ ý $i(t)$ bằng cách kết hợp đường cong kỳ hạn danh nghĩa $f(t)$ và kỳ hạn thực $r(t)$ qua đồng nhất thức Fisher (choudhry_analysing_yield_curve, Ch.7, d.3406–3410):
$$1 + f(t) = (1 + r(t))(1 + i(t)) \iff i(t) = \frac{1 + f(t)}{1 + r(t)} - 1$$
4. Chuyển đổi đường cong lạm phát kỳ hạn $i(t)$ thành đường cong lạm phát trung bình tích lũy $\bar{\pi}(t)$ ứng với kỳ hạn đáo hạn của từng trái phiếu (choudhry_analysing_yield_curve, Ch.7, d.3410–3418):
$$\bar{\pi}_m = \left[\prod_{k=1}^m (1 + i_k)\right]^{1/m} - 1$$
5. Thay thế giả định phẳng ban đầu bằng chính mức lạm phát trung bình $\bar{\pi}_m$ đặc thù cho từng trái phiếu, cập nhật lại hệ số co giãn $\Delta_i$ và tính toán lại toàn bộ dòng tiền cũng như lợi suất thực tế (choudhry_analysing_yield_curve, Ch.7, d.3420);
6. Lặp lại chu trình trên cho đến khi cấu trúc kỳ hạn lạm phát dùng làm đầu vào tính dòng tiền hội tụ hoàn toàn với cấu trúc kỳ hạn lạm phát suy ra từ đầu ra của mô hình (sai số tuyệt đối nhỏ hơn ngưỡng hội tụ định trước $\epsilon$) (choudhry_analysing_yield_curve, Ch.7, d.3420).

Song song với thách thức độ trễ, việc thị trường có số lượng mã trái phiếu liên kết lạm phát lưu hành rất hạn chế (chẳng hạn thị trường Anh vào tháng 12/1999 chỉ có 11 mã index-linked gilts) đặt ra ràng buộc nghiêm ngặt cho việc khớp đường cong (choudhry_analysing_yield_curve, Ch.7, Estimating the Real Term Structure, d.3374, d.3378). Các mô hình spline bậc ba (như phương pháp Schaefer 1981 hay biến thể McCulloch 1971) buộc phải cắt giảm số điểm nút xuống mức tối thiểu (thường chỉ 3 nút định hình 2 đoạn hàm bậc ba) nhằm triệt tiêu hiện tượng uốn lượn giả tạo (forward rate oscillation) và bảo đảm tính trơn nhẵn của cấu trúc kỳ hạn thực (choudhry_analysing_yield_curve, Ch.7, d.3370, d.3378).

Quy trình lặp này cấu thành điều kiện tiền đề để xây dựng [[real-yield-curves-reflect-real-cost-of-capital-and-fluctuate-with-economic-growth]] và [[implied-forward-inflation-curves-isolate-marginal-inflation-expectations-via-fisher-identity]], kế thừa nguyên lý khớp đường cong từ [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity]] và [[mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds]], đồng thời cung cấp giải pháp xử lý nhiễu vi mô cho [[breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise]].
