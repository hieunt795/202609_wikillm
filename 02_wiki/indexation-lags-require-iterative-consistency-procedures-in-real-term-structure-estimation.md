---
title: indexation-lags-require-iterative-consistency-procedures-in-real-term-structure-estimation
type: concept
tags: [inflation-linked-bonds, indexation-lag, real-term-structure, curve-fitting, cubic-spline, iterative-calibration]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Ước lượng cấu trúc kỳ hạn thực (real term structure estimation) đối mặt với rào cản kỹ thuật đặc thù do bản chất dòng tiền của trái phiếu liên kết lạm phát phụ thuộc vào chỉ số giá tiêu dùng nhưng lại chịu một độ trễ chỉ số hóa cố định (indexation lag) (choudhry_analysing_yield_curve, Ch.7, Index-Linked Bonds and Real Yields, d.3338; The Term Structure of Implied Forward Inflation Rates, d.3374).

Vì lý do kỹ thuật thu thập và công bố chỉ số giá của cơ quan thống kê quốc gia, các thị trường trái phiếu chính phủ đều áp dụng một khoảng thời gian trễ nhất định giữa thời điểm chốt chỉ số lạm phát và ngày chi trả dòng tiền (chẳng hạn 8 tháng đối với UK Index-Linked Gilts phát hành trước năm 2005, hoặc 3 tháng đối với các đợt phát hành sau 2005 và US TIPS) (choudhry_analysing_yield_curve, Ch.7, d.3338, d.3374, d.3412). Độ trễ này tạo ra nghịch lý phụ thuộc luẩn quẩn: để tính toán được lợi suất thực tế của trái phiếu từ giá thị trường quan sát được, người phân tích bắt buộc phải đưa vào một giả định về tỷ lệ lạm phát tương lai; tuy nhiên, mức lạm phát giả định này lại trực tiếp quyết định hình thái của đường cong lợi suất thực và đường cong lạm phát ngụ ý được ước lượng (choudhry_analysing_yield_curve, Ch.7, d.3374, d.3410).

Để phá vỡ vòng lặp phụ thuộc này, Bank of England và các chuyên gia định lượng áp dụng quy trình lặp nhất quán lạm phát (iterative consistency procedure) (choudhry_analysing_yield_curve, Ch.7, Deriving the Term Structure of Inflation Expectations, d.3410–3420):
1. Thiết lập một giả định lạm phát phẳng ban đầu (thường là 3% hoặc 5%) để tính toán sơ bộ dòng tiền danh nghĩa kỳ vọng và xác định lợi suất thực tế ban đầu cho từng trái phiếu trong mẫu (choudhry_analysing_yield_curve, Ch.7, d.3410);
2. Sử dụng các mức lợi suất này để khớp hàm chiết khấu hoặc đường cong lợi suất thực, từ đó suy ra đường cong lãi suất kỳ hạn thực tức thời $f_{\text{real}}(t,T)$ (choudhry_analysing_yield_curve, Ch.7, d.3410);
3. Kết hợp đường cong kỳ hạn thực với đường cong kỳ hạn danh nghĩa qua đồng nhất thức Fisher để trích xuất đường cong lạm phát kỳ hạn ngụ ý ban đầu $\pi_{\text{fwd}}(t,T)$ (choudhry_analysing_yield_curve, Ch.7, d.3410);
4. Tích phân đường cong forward inflation để tính toán đường cong lạm phát trung bình gộp ứng với từng kỳ hạn đáo hạn cụ thể của các trái phiếu trong mẫu (choudhry_analysing_yield_curve, Ch.7, d.3414–3418);
5. Thay thế giả định lạm phát phẳng ban đầu bằng chính các mức lạm phát ngụ ý mới trích xuất cho từng trái phiếu, và tính toán lại toàn bộ lợi suất thực tế (choudhry_analysing_yield_curve, Ch.7, d.3420);
6. Lặp lại chu trình trên cho đến khi cấu trúc kỳ hạn lạm phát dùng làm đầu vào tính dòng tiền trùng khớp hoàn toàn với cấu trúc kỳ hạn lạm phát suy diễn ở đầu ra, đạt trạng thái hội tụ nhất quán nội tại (choudhry_analysing_yield_curve, Ch.7, d.3420).

Song song với thách thức độ trễ, việc thị trường có số lượng mã trái phiếu liên kết lạm phát lưu hành rất hạn chế (chẳng hạn thị trường Anh vào tháng 12/1999 chỉ có 11 mã index-linked gilts) đặt ra ràng buộc nghiêm ngặt cho việc khớp đường cong (choudhry_analysing_yield_curve, Ch.7, Estimating the Real Term Structure, d.3374, d.3378). Các mô hình spline bậc ba (như phương pháp Schaefer 1981 hay biến thể McCulloch 1971) buộc phải cắt giảm số điểm nút xuống mức tối thiểu (thường chỉ 3 nút định hình 2 đoạn hàm bậc ba) nhằm triệt tiêu hiện tượng uốn lượn giả tạo (forward rate oscillation) và bảo đảm tính trơn nhẵn của cấu trúc kỳ hạn thực (choudhry_analysing_yield_curve, Ch.7, d.3370, d.3378).

Quy trình lặp này cấu thành điều kiện tiền đề để xây dựng [[real-yield-curves-reflect-real-cost-of-capital-and-fluctuate-with-economic-growth]] và [[implied-forward-inflation-curves-isolate-marginal-inflation-expectations-via-fisher-identity]], kế thừa nguyên lý khớp đường cong từ [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity]] và [[mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds]], đồng thời cung cấp giải pháp xử lý nhiễu vi mô cho [[breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise]].
