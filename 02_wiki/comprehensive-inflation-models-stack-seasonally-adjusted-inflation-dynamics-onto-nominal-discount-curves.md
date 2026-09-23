---
title: comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves
type: concept
tags: [inflation-modelling, composite-curve, real-discount-factor, spline-fitting, quantitative-finance]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Để định giá các công cụ liên kết lạm phát trong bối cảnh tính mùa vụ và các cú sốc thuế làm sai lệch các chỉ số đơn giản, các nhà định lượng xây dựng mô hình đường cong chiết khấu thực toàn diện theo nguyên lý mô hình phức hợp (fixed_income_during, Ch.23, Comprehensive Inflation Modelling, d.284–296, 326). Kiến trúc mô hình phân tầng bắt đầu từ đường cong hệ số chiết khấu danh nghĩa được khớp bằng spline tham số, sau đó xếp chồng một mô hình động học lạm phát hội tụ kết hợp với các hệ số điều chỉnh mùa vụ để trích xuất đường cong chiết khấu thực (fixed_income_during, Ch.23, Comprehensive Inflation Modelling, d.286–296, 318–326).

Mô hình lạm phát hai tham số cho phép đường lạm phát kỳ vọng hội tụ dần từ mức hiện hành về mức cân bằng dài hạn, giúp phản ánh các bước nhảy chỉ số giá do điều chỉnh thuế tiêu thụ hoặc các cú sốc giá năng lượng ngắn hạn (fixed_income_during, Ch.23, Comprehensive Inflation Modelling, d.292–296, 306).

Việc áp dụng mô hình chiết khấu thực có hiệu chỉnh mùa vụ giúp thu hẹp độ phân tán sai số của các trái phiếu TIPS thực tế, loại bỏ sự ngộ nhận về định giá đắt rẻ giữa các trái phiếu có tháng đáo hạn khác nhau (fixed_income_during, Ch.23, Comprehensive Inflation Modelling, d.336). Ngoài ra, khi so sánh ước lượng lạm phát dài hạn từ mô hình trái phiếu với tỷ suất hoán đổi lạm phát kỳ hạn xa, độ phân tán trung bình khoảng 15 điểm cơ bản chỉ ra một hành lang phi kinh doanh chênh lệch giá rộng khoảng 30 điểm cơ bản, phản ánh chi phí sử dụng bảng cân đối kế toán để lưu kho vị thế hoán đổi tài sản (fixed_income_during, Ch.23, Inflation Models and Expectations, d.346). Cấu trúc mô hình phân tầng này kế thừa phương pháp luận tách đường cong từ [[composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition]], khắc phục các sai lệch định giá được nhận diện trong [[inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering]], và cung cấp cơ sở vững chắc cho các phép đo z-spread tại [[z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves]].
