---
title: "Yield Curve PCA Factors Link Curvature Convexity to Implied Rate Volatility"
type: concept
tags:
  - trading
  - curve-trading
  - pca
  - factor-analysis
  - implied-volatility
  - curvature
  - convexity
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Phân tích Thành phần Chính (Principal Component Analysis - PCA) là công cụ toán học tiêu chuẩn được sử dụng để bóc tách động học nội tại của đường cong lợi suất thành các nhân tố trực giao độc lập thay vì áp đặt các cấu trúc chênh lệch kỳ hạn định sẵn (fixed_income_during, Ch.31, Sec.31.2, d.142–159). Ba nhân tố thành phần chính đầu tiên (eigenvectors) giải thích tới hơn 99% tổng phương sai biến động hàng ngày của cấu trúc kỳ hạn trái phiếu chính phủ Mỹ và Đức:
1. Nhân tố 1 (Level / Mức độ): giải thích khoảng 80% đến 90% biến động, phản ánh sự dịch chuyển đồng thời của toàn bộ mặt bằng lợi suất gắn liền với điều chỉnh lãi suất chính sách của ngân hàng trung ương [[parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments]];
2. Nhân tố 2 (Slope / Độ dốc): phản ánh sự thay đổi độ nghiêng tương đối giữa đầu ngắn và đầu dài (Steepening hoặc Flattening), thường tương quan chặt chẽ với các pha chu kỳ kinh tế vĩ mô (bear-steepening, bull-flattening) [[steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks]];
3. Nhân tố 3 (Curvature / Độ cong): mô tả sự phân kỳ hiệu suất giữa vùng kỳ hạn trung tâm so với hai đầu mút, tương ứng chính xác với cấu trúc hình học của chiến lược Butterfly [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]].

Nhân tố thứ ba bộc lộ một liên kết kinh tế học sâu sắc giữa độ cong của đường cong lợi suất và độ biến động lãi suất ngụ ý (implied volatility) trên thị trường quyền chọn (fixed_income_during, Ch.31, Sec.31.2, d.184–193). Xét một vị thế Butterfly trung hòa rủi ro thời lượng với trạng thái bán khống chân thân (short bullet) và mua hai chân cánh (long wings): do cấu trúc kỳ hạn phân tán, vị thế này sở hữu độ lồi dương thuần túy (positive convexity). Khi mặt bằng lãi suất dịch chuyển theo bất kỳ hướng nào, việc tái cân bằng tỷ lệ phòng hộ theo thời gian sẽ tạo ra dòng tiền lãi lỗ P&L dương liên tục trước chi phí ma sát. Để loại trừ cơ hội kinh doanh chênh lệch giá, thị trường bắt buộc phải phản ánh mức lợi nhuận kỳ vọng từ độ lồi này vào chi phí nắm giữ (carry) của cấu trúc kỳ hạn thông qua hình dạng lồi tự nhiên: lợi suất của chân thân (bullet yield) phải cao hơn mức lợi suất nội suy tuyến tính giữa hai cánh (wings) (fixed_income_during, Ch.31, Sec.31.2, d.184).

Dữ liệu thực nghiệm xác nhận mối tương quan thuận giữa giá trị thực hóa của Nhân tố PCA 3 và chỉ số biến động quyền chọn trái phiếu kho bạc Mỹ CBOE VXTYN: khi kỳ vọng biến động lãi suất tăng cao, thị trường định giá độ lồi đắt hơn, làm gia tăng độ phồng (hump) của vùng trung tâm đường cong (fixed_income_during, Ch.31, Sec.31.2, d.184–192). Tuy nhiên, mối tương quan kinh tế tự nhiên này đã bị suy giảm đáng kể trong thập kỷ qua do các chương trình nới lỏng định lượng (QE) quy mô lớn và định hướng chính sách tương lai (Forward Guidance) của các ngân hàng trung ương lớn, vốn đã can thiệp thô bạo vào sự hình thành giá cả và đè nén độ biến động tự do của thị trường [[convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end]].

Mặc dù các mô hình đường cong tham số hóa như Nelson-Siegel và Nelson-Siegel-Svensson đã thiết kế sẵn các tham số $\beta$ để biểu diễn Level, Slope và Hump [[parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness]], việc sử dụng trực tiếp các tham số này để giao dịch gặp phải hai rào cản nghiêm trọng (fixed_income_during, Ch.31, Sec.31.2.1, d.208–214). Thứ nhất, tham số định hình vị trí $\lambda$ (hoặc $\tau$) của mô hình biến động rất mạnh theo thời gian, khiến vị trí đỉnh gù (hump location) liên tục trôi dạt dọc theo trục kỳ hạn và làm vô hiệu hóa các tỷ trọng giao dịch Butterfly cố định. Thứ hai, các tham số $\beta$ có tương quan phi tuyến tính cao với nhau qua thời gian, đòi hỏi quy trình tính toán độ nhạy cảm phức tạp hơn nhiều so với việc trích xuất các nhân tố PCA trực giao thuần túy từ chuỗi sai phân lợi suất par [[curve-trading-hierarchies-systematically-immunize-lower-order-risk-dimensions]].
