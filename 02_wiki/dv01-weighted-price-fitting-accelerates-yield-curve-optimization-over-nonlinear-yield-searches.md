---
title: dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches
type: concept
tags: [yield-curve, quantitative-finance, optimization, numerical-methods]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Quy trình khớp đường cong lợi suất tham số đòi hỏi việc xác định bộ tham số tối ưu nhằm cực tiểu hóa hàm sai số giữa dữ liệu thị trường và giá trị mô hình (fixed_income_during, Ch.19, Fitting Curve Models, d.319–325). Phương pháp tiếp cận truyền thống dựa trên hàm mục tiêu sai số lợi suất gặp rào cản chi phí tính toán lớn do phải thực hiện các thuật toán tìm nghiệm phi tuyến lặp đi lặp lại để chuyển đổi giá bẩn của từng trái phiếu thành lợi suất đáo hạn tương ứng (fixed_income_during, Ch.19, Fitting Curve Models, d.325–336).

Nhằm nâng cao hiệu suất xử lý, các hệ thống định giá lượng hóa hiện đại sử dụng phép xấp xỉ tuyến tính chuyển đổi sai lệch lợi suất thành sai lệch giá có trọng số DV01 (fixed_income_during, Ch.19, Fitting Curve Models, d.332–336). Nhờ việc giá bẩn mô hình có thể tính toán nhanh chóng thông qua tích vô hướng giữa dòng tiền tương lai và hệ số chiết khấu, giải thuật tối ưu hóa trọng số DV01 đạt tốc độ xử lý nhanh hơn nhiều bậc độ lớn mà vẫn đảm bảo độ tin cậy tương đương về mặt kinh tế (fixed_income_during, Ch.19, Fitting Curve Models, d.336). Dù vậy, các kỹ thuật loại bỏ điểm dữ liệu ngoại lai tự động cần được kiểm soát chặt chẽ để tránh làm thay đổi cấu trúc mẫu quan sát qua các phiên giao dịch liên tiếp (fixed_income_during, Ch.19, Fitting Curve Models, d.338–341). Kỹ thuật này kế thừa trực tiếp thước đo độ nhạy giá tại [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]], dựa trên quy ước tính toán giá bẩn trong [[clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement]], và là công cụ bổ trợ đắc lực cho các mô hình tại [[parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness]] cũng như giải thuật [[bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles]].
