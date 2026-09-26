---
title: "IRRBB Model Governance and Independent Three-Tier Validation Framework"
tags:
  - concept
  - alm
  - irrbb
  - model-governance
  - model-validation
  - model-risk
  - bcbs-368
---

Khung quản trị mô hình và kiểm định độc lập ba tầng (Three-Tier Model Validation Framework) theo Nguyên tắc 6 của BCBS 368 là cơ chế kiểm soát bắt buộc nhằm triệt tiêu rủi ro mô hình trong việc lượng hóa IRRBB, đòi hỏi quy trình đánh giá toàn diện tách biệt giữa đơn vị phát triển mô hình, đơn vị kiểm định độc lập và kiểm toán nội bộ trên ba trụ cột: Tính đúng đắn về mặt lý thuyết, Kiểm tra quy trình thực thi và Phân tích kết quả thực tế (bcbs_368, file d368.md, Principle 6, d.279–313).

**1. Bản chất của Rủi ro Mô hình trong Hệ thống Quản trị IRRBB**

Hệ thống đo lường nội bộ IRRBB (Internal Measurement Systems - IMS) tại các ngân hàng hiện đại là một tập hợp các mô hình toán học và hành vi cực kỳ phức tạp:
- Mô hình phân rã và ước lượng tỷ lệ tiền gửi lõi (core deposits) cùng hệ số điều chỉnh lãi suất (pass-through beta) của tiền gửi không kỳ hạn NMDs ([[non-maturity-deposit-behavioural-modelling-governs-core-and-non-core-segmentation-under-irrbb]]).
- Mô hình xác suất trả nợ trước hạn (CPR) cho các khoản vay thế chấp bán lẻ cố định và mô hình rút tiền gửi tiết kiệm trước hạn (TDRR) ([[customer-behavioural-optionalities-govern-loan-prepayments-and-early-deposit-redemptions]]).
- Các thuật toán nội suy đường cong lợi suất spline và mô hình định giá quyền chọn tự động ([[automatic-interest-rate-options-standardised-valuation-and-volatility-shocks]]).

Rủi ro mô hình (Model Risk) nảy sinh khi:
1. Mô hình có sai sót căn bản trong nền tảng lý thuyết hoặc thuật toán toán học.
2. Dữ liệu đầu vào bị sai lệch hoặc không đầy đủ.
3. Ban điều hành lạm dụng mô hình ngoài phạm vi thiết kế, hoặc cố tình hiệu chỉnh các giả định hành vi lạc quan quá mức để "bóp méo" làm giảm nhẹ chỉ số sụt giảm vốn trong bài kiểm tra ngoại lai ([[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]]).

Hậu quả của rủi ro mô hình trong IRRBB là ngân hàng tích lũy các khoản lỗ ngầm khổng lồ trên vốn chủ sở hữu mà hệ thống cảnh báo sớm không thể phát hiện trước khi khủng hoảng thanh khoản bùng phát.

**2. Khung Kiểm định Độc lập Ba Trụ cột (Three Pillars of Validation)**

Principle 6 quy định bất kỳ mô hình IRRBB nào trước khi đưa vào áp dụng chính thức và định kỳ hàng năm phải vượt qua quy trình kiểm định độc lập dựa trên ba trụ cột kỹ thuật:

```
+-----------------------------------------------------------------------------------+
|                        BA TRỤ CỘT KIỂM ĐỊNH MÔ HÌNH IRRBB                         |
+-----------------------------------------------------------------------------------+
        |                                   |                                   |
        v                                   v                                   v
[TRỤ CỘT 1: LÝ THUYẾT]             [TRỤ CỘT 2: THỰC THI]             [TRỤ CỘT 3: KẾT QUẢ]
- Cơ sở kinh tế & toán học         - Tính toàn vẹn dữ liệu (lineage) - Backtesting dự báo NII
- Tính hợp lý của giả định hành vi - Mã nguồn & thuật toán phần mềm   - Đối chuẩn mô hình thách thức
- Kiểm tra điều kiện biên (NIRP)   - Độ chính xác chia dải kỳ hạn     - Phân tích độ nhạy tham số
```

*Trụ cột 1: Đánh giá Tính đúng đắn về mặt Lý thuyết (Conceptual Soundness)*
- Thẩm định logic kinh tế lượng và nền tảng toán học của mô hình. Kiểm tra tính chặt chẽ của các biến giải thích (ví dụ: biến vĩ mô GDP, tỷ lệ thất nghiệp, chênh lệch lãi suất thị trường trong mô hình CPR).
- Đánh giá tính thận trọng của các giả định hành vi, đặc biệt là sự tuân thủ các trần khống chế giám sát (như trần kỳ hạn 5 năm cho tiền gửi bán lẻ giao dịch theo Section IV.3).
- Kiểm tra hành vi của mô hình tại các vùng biên cực trị, chẳng hạn như khi lãi suất danh nghĩa rơi vào vùng âm (Negative Interest Rate Policy - NIRP) hoặc khi đường cong đảo ngược sâu.

*Trụ cột 2: Kiểm định Quy trình Thực thi và Tính Toàn vẹn Dữ liệu (Process Verification)*
- Kiểm tra tính toàn vẹn và nguồn gốc dữ liệu (data lineage & reconciliation): Đối chiếu dữ liệu đầu vào giữa hệ thống Core Banking, hệ thống Front-office Treasury và kho dữ liệu ALM để đảm bảo không có giao dịch bị bỏ sót hoặc trùng lặp.
- Rà soát mã nguồn lập trình (code review) và thuật toán phân bổ dòng tiền: Đảm bảo quy tắc phân chia 19 dải kỳ hạn (slotting criteria) được thực hiện nhất quán, tách bạch chính xác giữa dòng tiền gốc và dòng tiền lãi.

*Trụ cột 3: Phân tích Kết quả Thực tế, Backtesting và Benchmarking (Outcomes Analysis)*
- **Kiểm định dự báo (Backtesting):** Định kỳ so sánh thu nhập lãi thuần thực tế ($NII_{\text{actual}}$) với mức thu nhập lãi thuần dự báo ($NII_{\text{forecast}}$) từ mô hình tại kỳ trước. Bóc tách các nguyên nhân sai lệch: do sai số mô hình, do biến động lãi suất thị trường bất ngờ, hay do quy mô bảng cân đối kế toán tăng trưởng khác kế hoạch.
- **Mô hình Thách thức (Challenger Models / Benchmarking):** Chạy song song mô hình nội bộ với các mô hình chuẩn mực độc lập hoặc Khung chuẩn hóa của Basel ([[irrbb-standardised-framework-five-stage-measurement-architecture]]) để đánh giá độ lệch chuẩn.
- **Phân tích Độ nhạy Tham số (Sensitivity Analysis):** Stress test chính các tham số của mô hình (ví dụ: tăng tốc độ rút tiền gửi NMDs thêm $20\%$, giảm tỷ lệ trả nợ trước hạn CPR đi $30\%$) để đo lường mức độ dễ bị tổn thương của $\Delta EVE$ và $\Delta NII$ trước sự sai lệch tham số.

**3. Cơ cấu Quản trị Ba Tuyến Phòng thủ (Three Lines of Defence)**

Một khung quản trị mô hình IRRBB hiệu quả đòi hỏi sự phân định trách nhiệm rõ ràng:
- **Tuyến 1 (First Line - Đơn vị Phát triển & Vận hành):** Bộ phận ALM / Treasury Analytics chịu trách nhiệm xây dựng mô hình, thu thập dữ liệu, chạy mô phỏng hàng tháng, duy trì Danh mục Mô hình (Model Inventory) và lập Hồ sơ Kỹ thuật Mô hình (Model Technical Documentation) chi tiết.
- **Tuyến 2 (Second Line - Đơn vị Kiểm định Độc lập):** Bộ phận Quản trị Rủi ro Mô hình (Model Risk Management - MRM) hoặc Quản trị Rủi ro Thị trường. Đơn vị này hoàn toàn độc lập về mặt nhân sự và báo cáo đối với Tuyến 1. MRM có thẩm quyền phê duyệt, từ chối, hoặc áp đặt hạn mức đệm an toàn bổ sung (model overlays / capital add-ons) đối với các mô hình chưa đạt độ tin cậy tuyệt đối.
- **Tuyến 3 (Third Line - Kiểm toán Nội bộ):** Thực hiện kiểm toán độc lập định kỳ hàng năm toàn bộ quy trình quản trị mô hình, đánh giá tính tuân thủ chính sách thay đổi mô hình (Model Change Policy), và kiểm tra tính khách quan của Tuyến 2.

**4. Quản trị Mô hình do Bên Thứ ba Cung cấp (Vendor Models)**

BCBS 368 Principle 6 nhấn mạnh một nguyên tắc mang tính pháp lý: Việc sử dụng phần mềm thương mại từ các nhà cung cấp bên ngoài (Vendor Models) không làm giảm bớt trách nhiệm giải trình của Hội đồng Quản trị và Ban điều hành.
- Ngân hàng tuyệt đối không được đối xử với mô hình của nhà cung cấp như một chiếc "hộp đen" (black box).
- Ngân hàng phải yêu cầu nhà cung cấp cung cấp đầy đủ tài liệu giải thích thuật toán, giả định toán học và mã nguồn cốt lõi.
- Đơn vị Tuyến 2 phải tự thực hiện kiểm định độc lập trên dữ liệu danh mục thực tế của ngân hàng và chứng minh được rằng việc hiệu chuẩn tham số của nhà cung cấp hoàn toàn phù hợp với hành vi khách hàng và môi trường pháp lý sở tại.
