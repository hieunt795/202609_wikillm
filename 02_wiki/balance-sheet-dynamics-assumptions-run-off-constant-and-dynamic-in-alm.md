---
title: balance-sheet-dynamics-assumptions-run-off-constant-and-dynamic-in-alm
type: concept
tags: [alm, irrbb, balance-sheet, eve, nii, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Ba giả định động thái bảng cân đối kế toán — Bảng cân đối thu hồi chạy cạn (Run-off balance sheet), Bảng cân đối quy mô không đổi (Constant balance sheet), và Bảng cân đối biến động động (Dynamic balance sheet) — tạo thành ba hệ quy chiếu phân tích cốt lõi trong ALM và [[interest-rate-risk-in-the-banking-book-irrbb]], trong đó chuẩn mực BCBS 368 bắt buộc áp dụng Run-off cho phép đo Giá trị Kinh tế của Vốn tự có ($\Delta EVE$) và Constant cho phép đo Thu nhập Lãi thuần ($\Delta NII$), đồng thời hạn chế Dynamic cho mục đích lập kế hoạch kinh doanh nội bộ (bcbs_368, file d368.md, Section I, d.80–90; Section II.1 Principle 4, d.180–210; Annex 1.3, d.920–970).

**1. Bảng cân đối Thu hồi Chạy cạn (Run-off / Static Balance Sheet)**

Bảng cân đối thu hồi chạy cạn đóng băng toàn bộ vị thế tài sản, nợ và ngoại bảng hiện hữu tại thời điểm phân tích $T_0$. Trong suốt chân trời dự báo:
- Mọi dòng tiền gốc và lãi khi đáo hạn sẽ chạy cạn dần (run off) và biến mất khỏi bảng cân đối.
- Tuyệt đối không phát sinh bất kỳ khoản giải ngân cho vay mới, không huy động thêm tiền gửi, và không tái tục các hợp đồng đã đến hạn.
- Số dư bảng cân đối kế toán suy giảm liên tục theo hàm số thời gian cho đến khi toàn bộ dòng tiền của hợp đồng dài nhất kết thúc.

*Ứng dụng chuẩn mực theo BCBS 368:*
Theo Principle 8 (Bảng B công bố Trụ cột 3), Section IV.6 và [[delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion]], giả định Run-off là yêu cầu pháp lý bắt buộc cho việc tính toán $\Delta EVE$. Cơ sở lý luận giám sát xác định rằng Giá trị Kinh tế của Vốn tự có ([[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows]]) là thước đo giá trị thanh lý ròng (run-off liquidation value) của các cam kết hợp đồng hiện tại. Việc cho phép đưa các dòng tiền kinh doanh tương lai hoặc giả định tái đầu tư vào phép đo EVE sẽ tạo ra sự tùy tiện chủ quan, làm sai lệch bản chất đo lường rủi ro cấu trúc bảng cân đối tích lũy từ quá khứ, tương tự như đã phân định ở [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]].

**2. Bảng cân đối Quy mô Không đổi (Constant Balance Sheet)**

Bảng cân đối quy mô không đổi duy trì một trạng thái cân bằng tĩnh về quy mô và cấu trúc danh mục trong suốt chân trời đo lường (thông thường là 12 tháng):
- Khi bất kỳ tài sản hoặc khoản nợ nào đáo hạn hoặc được thanh toán trước hạn, nó sẽ được tái tục ngay lập tức bằng một hợp đồng mới có cùng tính chất.
- Hợp đồng thay thế có cùng kỳ hạn gốc, cùng phân loại khách hàng, cùng loại tiền tệ và cùng biên độ thương mại (commercial margin/spread) so với lãi suất chuẩn thị trường tại thời điểm tái tục.
- Tổng tài sản, tổng nguồn vốn và tỷ trọng cơ cấu giữa các dải kỳ hạn và sản phẩm được bảo toàn nguyên vẹn ($TotalAssets_t = TotalAssets_0$).

*Ứng dụng chuẩn mực theo BCBS 368:*
Theo Principle 8 và [[delta-nii-regulatory-calculation-rules-mandate-constant-balance-sheet-and-rolling-horizon]], giả định Constant là tiêu chuẩn giám sát bắt buộc khi tính toán biến thiên thu nhập lãi thuần ($\Delta NII$) dưới 6 kịch bản sốc chuẩn hóa. Phép đo NII đặt trong giả định hoạt động liên tục (going-concern perspective). Việc cố định quy mô bảng cân đối cho phép cơ quan thanh tra bóc tách thuần túy tác động của cú sốc lãi suất thị trường lên thu nhập lãi biên mà không bị pha tạp bởi dự báo tăng trưởng quy mô kinh doanh hoặc sự suy giảm giả tạo do chạy cạn dòng tiền.

**3. Bảng cân đối Biến động Động (Dynamic Balance Sheet)**

Bảng cân đối biến động động giải phóng toàn bộ các ràng buộc cố định để mô phỏng tương lai của ngân hàng sát thực tế kinh doanh nhất:
- Tích hợp kế hoạch tăng trưởng tín dụng và huy động vốn theo chiến lược kinh doanh đa năm đã được phê duyệt.
- Mô hình hóa sự thay đổi cơ cấu sản phẩm (product mix shift) dưới tác động của môi trường kinh tế (ví dụ: khách hàng chuyển từ tiền gửi không kỳ hạn CASA sang tiền gửi có kỳ hạn khi lãi suất huy động tăng cao).
- Tích hợp các phản ứng hành động quản trị chủ động của Ban điều hành và Hội đồng ALCO (management actions), chẳng hạn như thay đổi biểu lãi suất niêm yết, thắt chặt tiêu chuẩn cấp tín dụng, hoặc thực hiện các hợp đồng hoán đổi lãi suất mới để tái cân bằng trạng thái rủi ro.

*Yêu cầu Quản trị và Giám sát theo BCBS 368:*
Theo Principle 4 (đoạn 190–210), mô hình Dynamic Balance Sheet được khuyến khích sử dụng trong quy trình tự đánh giá mức độ đủ vốn nội bộ ([[icaap-framework-determines-economic-capital-and-target-capital-under-stress]]) và kế hoạch ngân sách tài chính. Tuy nhiên, Basel 368 đặt ra các rào cản kiểm soát nghiêm ngặt:
- Ngân hàng không được phép sử dụng kết quả Dynamic Balance Sheet để thay thế hoặc làm giảm nhẹ các chỉ số cảnh báo theo chuẩn Run-off và Constant trong báo cáo Trụ cột 3 hoặc Bài kiểm tra ngoại lai ([[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]]).
- Mọi hành động can thiệp quản trị dự kiến (management actions) phải chứng minh được tính khả thi về mặt vận hành và thanh khoản thị trường dưới điều kiện stress, đồng thời phải được thẩm định độc lập bởi bộ phận Quản trị Rủi ro Mô hình.

**4. Ma trận So sánh Kỹ thuật giữa Ba Giả định Bảng Cân đối**

| Tiêu chí So sánh | Bảng Cân đối Thu hồi (Run-off) | Bảng Cân đối Không đổi (Constant) | Bảng Cân đối Biến động (Dynamic) |
|---|---|---|---|
| **Chân trời Phân tích** | Toàn bộ dòng tiền còn lại (đến 30–50 năm) | Ngắn hạn (12 tháng đến 3 năm) | Đa năm theo kế hoạch vốn (3–5 năm) |
| **Xử lý Dòng tiền Đáo hạn** | Chạy cạn dần, biến mất khỏi sổ sách | Tái tục ngay vị thế tương đương cùng kỳ hạn/margin | Tái đầu tư theo định hướng kinh doanh tương lai |
| **Biên độ Thương mại (Margin)** | Không phát sinh khoản mới | Cố định spread so với lãi suất chuẩn mới | Biến động theo cung cầu thị trường và cạnh tranh |
| **Quy mô Bảng Cân đối** | Suy giảm liên tục về 0 | Bất biến ($TotalAssets_t = Const$) | Tăng trưởng hoặc thu hẹp theo chiến lược |
| **Hành vi Quản trị (ALCO)** | Bị vô hiệu hóa hoàn toàn | Bị vô hiệu hóa hoàn toàn | Được tích hợp có kiểm định khả thi |
| **Vai trò Pháp lý BCBS 368** | **Bắt buộc** cho $\Delta EVE$ Trụ cột 2 & 3 | **Bắt buộc** cho $\Delta NII$ Trụ cột 3 | Cho phép trong ICAAP & Stress test nội bộ |
| **Độ phức tạp Mô hình** | Thấp đến trung bình | Trung bình | Rất cao, phụ thuộc nhiều giả định chủ quan |
