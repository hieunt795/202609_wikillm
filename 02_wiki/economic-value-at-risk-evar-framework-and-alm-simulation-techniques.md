---
title: economic-value-at-risk-evar-framework-and-alm-simulation-techniques
type: concept
tags: [banking, alm, irrbb, evar, monte-carlo, historical-simulation, earnings-simulation, pv01, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Khuôn khổ Giá trị kinh tế chịu rủi ro và các kỹ thuật mô phỏng ALM (Economic Value at Risk EVaR Framework and ALM Simulation Techniques) tổng hợp hệ thống các công cụ định lượng rủi ro lãi suất trên sổ ngân hàng theo Chuẩn mực BCBS 368 của Ủy ban Basel, bao gồm phân tích khe hở định giá lại (PV01/Duration), Giá trị kinh tế của vốn chủ sở hữu (EVE), Giá trị kinh tế chịu rủi ro (EVaR) và mô phỏng thu nhập động (dynamic earnings simulation) (bcbs_368, file d368.md, Annex 1.4, d.988–1042).

Mỗi kỹ thuật định lượng sở hữu những ưu thế và giới hạn kỹ thuật riêng biệt trong việc nhận diện các dạng thức rủi ro phụ của IRRBB (Gap risk, Basis risk, Option risk). Do đó, Ủy ban Basel khuyến nghị các ngân hàng phải vận hành phối hợp đa thước đo nhằm đạt được bức tranh rủi ro toàn diện và khách quan (Annex 1.4.2, d.1006).

**1. Phân tích khe hở định giá lại và độ nhạy điểm cơ bản (PV01 / Modified Duration)**

Phân tích khe hở định giá lại (Repricing Gap analysis) là kỹ thuật định lượng truyền thống, phân bổ toàn bộ tài sản, nợ phải trả và ngoại bảng nhạy cảm với lãi suất vào các dải kỳ hạn định sẵn theo ngày định giá lại kế tiếp. Khe hở ròng ($Gap_k = Asset_k - Liability_k$) tại mỗi dải kỳ hạn được nhân với một bước nhảy lãi suất giả định để ước lượng sự thay đổi của thu nhập lãi thuần hoặc giá trị hiện tại (Annex 1.4.2, d.1008):
- *Chỉ số PV01 (Present Value of a Basis Point)*: Đo lường biến động giá trị hiện tại của bảng cân đối khi lãi suất dịch chuyển 01 điểm cơ bản ($0{,}01\%$).
- *Thời lượng điều chỉnh (Modified Duration)*: Biểu thị mức độ biến động phần trăm của giá trị tài chính trước một bước dịch chuyển song song cận biên của đường cong lợi suất (ví dụ 100 bps) (Footnote 40, d.1019).
- *Giới hạn kỹ thuật cốt lõi*: Phân tích Gap và Modified Duration chỉ phản ánh các bước dịch chuyển nhỏ, giả định đường cong dịch chuyển song song tuyệt đối, và giả định sai lệch rằng toàn bộ các vị thế trong cùng một dải kỳ hạn sẽ định giá lại đồng thời tại cùng một thời điểm, bỏ qua hoàn toàn rủi ro không khớp kỳ hạn nội dải (intra-bucket mismatch) và rủi ro cơ sở (basis risk).

**2. Thước đo Giá trị kinh tế của vốn chủ sở hữu (EVE)**

EVE đo lường mức sụt giảm giá trị hiện tại ròng của toàn bộ dòng tiền hiện hữu trên sổ ngân hàng khi chịu các cú sốc lãi suất lớn và các kịch bản căng thẳng (Annex 1.4.2, d.1010–1025). Khác với các mô hình tuyến tính, EVE chuẩn tắc đòi hỏi:
- Tái định giá toàn diện (full revaluation) đối với toàn bộ các quyền chọn lãi suất tự động;
- Tích hợp các hàm hành vi phi tuyến tính của khách hàng (trả nợ trước hạn CPR, rút tiền gửi sớm TDRR và phân tầng NMDs);
- Phân định rõ ràng giữa thước đo chuẩn tắc *Loại trừ vốn tự có (EVE measure)* dùng cho giám sát và thước đo *Điều chỉnh theo thu nhập (Earnings-adjusted EV)* dùng cho quản trị nội bộ.

**3. Khuôn khổ Giá trị kinh tế chịu rủi ro (EVaR)**

Giá trị kinh tế chịu rủi ro (Economic Value at Risk - EVaR) đo lường mức sụt giảm giá trị thị trường tối đa dự kiến của sổ ngân hàng (và của vốn tự có) trong điều kiện thị trường bình thường, tại một khoảng thời gian nắm giữ xác định (holding period / time horizon) và tương ứng với một độ tin cậy thống kê cho trước (ví dụ $99\%$ trong 1 năm) (Annex 1.4.2, d.1027–1030). Khung EVaR được xây dựng thông qua 3 phương pháp luận chính:
1. *Mô phỏng lịch sử (Historical simulation)*: Tái định giá toàn bộ bảng cân đối tài chính dựa trên các chuỗi biến động lãi suất thực tế quan sát được trong quá khứ. Phương pháp này không đòi hỏi giả định phân phối chuẩn nhưng mang tính chất nhìn lại quá khứ (backward-looking) và dễ bỏ sót các biến cố cực đoan chưa từng xảy ra trong chuỗi dữ liệu.
2. *Phương pháp ma trận phương sai - hiệp phương sai (Variance-Covariance approach)*: Ước lượng độ biến động của từng kỳ hạn và ma trận tương quan chéo giữa các điểm kỳ hạn trên đường cong lợi suất để tính toán độ phân tán giá trị của danh mục (Footnote 41, d.1037). Phương pháp này tính toán nhanh chóng nhưng bắt buộc phải giả định phân phối chuẩn của lợi suất, đánh giá thấp nghiêm trọng rủi ro đuôi (tail risk) và không thể xử lý chính xác tính phi tuyến của các sản phẩm có quyền chọn.
3. *Mô phỏng Monte Carlo (Monte Carlo simulation)*: Sử dụng các mô hình cấu trúc kỳ hạn lãi suất ngẫu nhiên (như mô hình 1 yếu tố hoặc 2 yếu tố Hull-White, Black-Karasinski) để tạo ra hàng nghìn đường đi lãi suất tương lai khả dĩ. Phương pháp này xử lý xuất sắc các cấu trúc quyền chọn phức tạp và rủi ro hành vi phụ thuộc đường đi (path-dependent options), nhưng đòi hỏi năng lực công nghệ và tài nguyên tính toán khổng lồ.
- *Giới hạn cơ bản của EVaR (Annex 1.4.2, d.1029)*: EVaR được thiết kế cho các điều kiện thị trường thông thường nên không phản ánh đầy đủ rủi ro mất mát trong các biến cố khủng hoảng (tail events), do đó EVaR chỉ đóng vai trò bổ trợ và không thể thay thế cho các kịch bản kiểm tra áp lực sốc lãi suất (stress testing).

**4. Kỹ thuật mô phỏng thu nhập động (Dynamic Earnings Simulation)**

Song song với việc đo lường giá trị kinh tế, ngân hàng áp dụng kỹ thuật mô phỏng thu nhập để lượng hóa mức độ biến động của thu nhập lãi thuần ($\Delta NII$) và tổng thu nhập hoạt động trong chân trời ngắn và trung hạn (thường từ 1 đến 3 năm, tối đa 5 năm) dưới góc nhìn hoạt động liên tục (going-concern perspective) (Annex 1.4.3, d.1033–1042):
- Kỹ thuật mô phỏng so sánh thu nhập kỳ vọng giữa *Kịch bản cơ sở (Base case scenario)* — phản ánh kế hoạch kinh doanh và dự báo vĩ mô tốt nhất của ngân hàng — với các kịch bản sốc lãi suất căng thẳng.
- Ba trạng thái mô hình hóa bảng cân đối được áp dụng tùy theo mức độ phức tạp:
  - *Bảng cân đối run-off*: Các tài sản và nợ hiện hữu tự suy giảm và đáo hạn mà không được thay thế;
  - *Bảng cân đối không đổi (Constant balance sheet)*: Duy trì quy mô và cơ cấu danh mục cố định thông qua việc thay thế đối ứng cùng loại các khoản mục đáo hạn;
  - *Bảng cân đối động (Dynamic balance sheet)*: Mô hình toàn diện nhất, phản ánh các kỳ vọng kinh doanh mới, sự thay đổi trong hành vi khách hàng và các phản ứng điều hành chủ động của ALCO trước môi trường lãi suất mới.

Hệ thống kỹ thuật này kết nối chặt chẽ với [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]], cung cấp nền tảng toán học cho các quy tắc tính toán tại [[delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion]] và [[delta-nii-regulatory-calculation-rules-mandate-constant-balance-sheet-and-rolling-horizon]].
