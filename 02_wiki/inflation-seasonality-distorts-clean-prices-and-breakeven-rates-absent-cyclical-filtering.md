---
title: inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering
type: concept
tags: [inflation-seasonality, clean-price, breakeven-inflation, seasonal-filtering, tips]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Các chỉ số giá tiêu dùng bộc lộ tính mùa vụ rất mạnh, với biên độ dao động định kỳ có thể tương đương hoặc vượt quá xu hướng lạm phát cơ bản, tiêu biểu như chỉ số CPI tại Nhật Bản hoặc các tiểu chỉ số du lịch, nghỉ dưỡng và năng lượng sưởi ấm tại Đức (fixed_income_during, Ch.23, Inflation Seasonality, d.142–148, 162). Sự biến động mùa vụ này xuất phát từ các chiến dịch giảm giá bán lẻ, các dịp lễ chuyển dịch và chu kỳ thời tiết (fixed_income_during, Ch.23, Inflation Seasonality, d.148).

Do lãi suất ngắn hạn trên thị trường tiền tệ không tồn tại tính mùa vụ tương ứng, giá sạch của trái phiếu liên kết lạm phát bắt buộc phải biến động nghịch chiều để hấp thụ tính mùa vụ của tỷ số chỉ số, đảm bảo lợi suất kỳ vọng ngắn hạn cân bằng với lãi suất thị trường tiền tệ (fixed_income_during, Ch.23, Inflation Seasonality, d.164–168). Sự điều chỉnh này làm cho giá sạch và lợi suất thực tính toán của trái phiếu biến thiên theo chu kỳ lịch biểu trong năm (fixed_income_during, Ch.23, Inflation Seasonality, d.168–170).

Khi nhà đầu tư tính toán tỷ lệ lạm phát hòa vốn giữa ngày tất toán và ngày đáo hạn, tính mùa vụ gây ra sự sai lệch nếu khoảng thời gian này không phải là một số nguyên năm (fixed_income_during, Ch.23, Breakeven Inflation, d.232–236). Việc tất toán vào tháng có chỉ số CPI mùa vụ thấp sẽ đẩy lạm phát hòa vốn tính toán lên cao, trong khi đáo hạn vào tháng có CPI mùa vụ thấp sẽ đè nén lạm phát hòa vốn xuống dưới xu hướng thực tế (fixed_income_during, Ch.23, Breakeven Inflation, d.232–248). Nếu không áp dụng các bộ lọc chu kỳ chuyên sâu, các mô hình định lượng sẽ ngộ nhận sai lệch mùa vụ thành cơ hội kinh doanh chênh lệch giá, dẫn đến việc đánh giá sai lệch tương đối giữa các trái phiếu có tháng đáo hạn khác nhau như phân tích trong [[comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves]]. Sai số mùa vụ này cũng là nguyên nhân gây nhiễu cho việc ước lượng kỳ vọng lạm phát tại [[breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise]].
