---
title: prolonged-volatility-suppression-breeds-liquidity-fragility-and-var-shocks
type: concept
tags: [volatility, var-shock, asset-purchases, market-microstructure, liquidity-risk, market-makers]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Việc ngân hàng trung ương can thiệp nén biến động thị trường (volatility suppression) thông qua các chương trình mua tài sản hoặc định hướng chính sách có thể hỗ trợ tăng trưởng ngắn hạn, nhưng việc duy trì trạng thái biến động thấp kéo dài sẽ tích tụ rủi ro hệ thống và tạo tiền đề cho các cú sốc thanh khoản nghiêm trọng (fixed_income_during, Ch.8, Volatility, file -9, d.20; Ch.9, Lower Volatility, file -10, d.62).

Về mặt lý thuyết, biến động đóng vai trò là một cơ chế tự điều chỉnh thiết yếu của thị trường tài chính: nó vừa là chiếc phanh hãm các hành vi chấp nhận rủi ro và sử dụng đòn bẩy quá mức của các định chế tài chính, vừa tạo động lực kinh tế cho hoạt động tạo lập thị trường (market making) và quản trị rủi ro (fixed_income_during, Ch.8, Volatility, file -9, d.20). Khi ngân hàng trung ương can thiệp triệt tiêu biến động trong một thời gian dài, cấu trúc vi mô của thị trường bị suy thoái qua ba cơ chế đồng thời (fixed_income_during, Ch.9, Lower Volatility, file -10, d.62; Lessons from the initial BoJ quantitative easing, file -10, d.226):

1. *Gia tăng đòn bẩy tư nhân*: Để duy trì tỷ suất sinh lời mục tiêu trên cơ sở điều chỉnh rủi ro trong môi trường biên lợi nhuận thấp, các nhà đầu tư buộc phải gia tăng đòn bẩy tài chính (fixed_income_during, Ch.9, Lower Volatility, file -10, d.62).
2. *Thu hẹp năng lực tạo lập thị trường*: Sự suy giảm biến động và chênh lệch giá mua-bán (bid-ask spread) khiến các ngân hàng thương mại và đại lý sơ cấp cắt giảm phân bổ vốn cho các bàn giao dịch tạo lập thị trường, làm teo tóp đệm thanh khoản hấp thụ cú sốc của toàn hệ thống (fixed_income_during, Ch.9, Lower Volatility, file -10, d.62).
3. *Triệt tiêu các nhà giao dịch bán khống (short-sellers)*: Các đợt tăng giá trái phiếu đơn chiều kéo dài nhiều năm dưới sự bảo trợ của ngân hàng trung ương dần loại bỏ hoàn toàn các nhà giao dịch sẵn sàng mở vị thế bán khống (fixed_income_during, Ch.9, Lessons from the initial BoJ quantitative easing, file -10, d.226).

Khi một cú sốc ngoại sinh xuất hiện làm lợi suất đảo chiều tăng vọt, thị trường rơi vào trạng thái tê liệt: việc thiếu vắng các vị thế bán khống (vốn sẽ mua lại để đóng trạng thái và tạo lực đỡ sàn cho giá) khiến áp lực bán đè nặng lên các đại lý đang nắm giữ vị thế mua lớn (long positions) (fixed_income_during, Ch.9, Lessons from the initial BoJ quantitative easing, file -10, d.226). Sự gia tăng đột ngột của biến động làm tăng vọt yêu cầu vốn an toàn theo mô hình Giá trị chịu rủi ro (Value-at-Risk — VaR), buộc các thuật toán và nhà quản lý rủi ro phải kích hoạt lệnh bán tháo cắt lỗ tự động (stop-loss selling) (fixed_income_during, Ch.9, Lessons from the initial BoJ quantitative easing, file -10, d.226). Quá trình này kích hoạt vòng lặp phản hồi dương (positive feedback loop) đẩy lợi suất tăng phi mã và thổi bùng hiện tượng **VaR shock** (fixed_income_during, Ch.9, Lessons from the initial BoJ quantitative easing, file -10, d.226).

Bài học điển hình là cú sốc VaR shock mùa hè năm 2003 trên thị trường trái phiếu chính phủ Nhật Bản (JGB): sau nhiều năm BoJ nới lỏng tiền tệ và nén biến động, sự đảo chiều của lợi suất trái phiếu Mỹ đã kích hoạt làn sóng bán tháo dây chuyền tại Tokyo, đẩy lợi suất JGB tăng dựng đứng dù BoJ vẫn đang duy trì chương trình QE (fixed_income_during, Ch.9, Lessons from the initial BoJ quantitative easing, file -10, d.226). Cơ chế rủi ro nội sinh này tương đồng sâu sắc với [[endogenous-risk-and-upward-sloping-haircut-loss-curve|đường cong tổn thất haircut nội sinh]] và các động lực kích hoạt [[mechanics-of-liquidity-crises-and-feedback-loops|vòng xoáy khủng hoảng thanh khoản]].
