---
title: pre-acquisition-review-and-hedging-approval-governance-for-irrbb
type: concept
tags: [banking, alm, irrbb, new-product-review, hedging-governance, internal-controls, alco, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Quy trình thẩm định tiền khả thi đối với sản phẩm mới và cơ chế quản trị phê duyệt phòng hộ IRRBB (Pre-acquisition Review and Hedging Approval Governance) thiết lập các chốt chặn kiểm soát nội bộ bắt buộc theo Chuẩn mực BCBS 368 của Ủy ban Basel, nhằm ngăn chặn việc phát sinh rủi ro lãi suất ngoài tầm kiểm soát từ các cấu trúc hợp đồng mới và bảo đảm tính minh bạch, hiệu quả của các giao dịch phòng hộ phái sinh (bcbs_368, file d368.md, Principle 1, Paragraph 18, d.103; Principle 3, Paragraph 27, d.166–167; Principle 7, Paragraph 66, d.324–327).

Các cuộc khủng hoảng ngân hàng trong lịch sử đã chứng minh rằng các khoản lỗ lãi suất nặng nề nhất thường bắt nguồn từ các sản phẩm tài chính phức tạp có đính kèm các điều khoản quyền chọn ngầm định mà hệ thống quản trị rủi ro không nhận diện kịp thời, hoặc từ các chiến lược phòng hộ phái sinh thiếu kiểm soát gây phát sinh rủi ro cơ sở và rủi ro thanh khoản ký quỹ khổng lồ.

**1. Quy trình Thẩm định tiền khả thi trước khi ban hành sản phẩm mới (Pre-acquisition Review)**

Theo Nguyên tắc 1 và 3 của BCBS 368, trước khi giới thiệu bất kỳ sản phẩm, dịch vụ hoặc thực hiện các giao dịch kinh doanh mới nào có thể làm thay đổi đáng kể cấu trúc dòng tiền hoặc hồ sơ rủi ro lãi suất của sổ ngân hàng, ngân hàng bắt buộc phải vận hành quy trình thẩm định rủi ro tiền khả thi độc lập (Paragraph 18, d.103; Paragraph 27, d.166). Quy trình này bao gồm 5 nội dung kiểm soát bắt buộc:
1. *Nhận diện và bóc tách các điều khoản quyền chọn ngầm định (Embedded Options Identification)*:
   - Rà soát toàn diện các điều khoản hợp đồng để nhận diện các quyền chọn tự động ngầm định (như trần lãi suất cap, sàn lãi suất floor, điều khoản mua lại callable, điều khoản bán lại puttable) và các quyền chọn hành vi (quyền trả nợ trước hạn không bồi hoàn, cam kết giải ngân cố định, quyền rút tiền gửi có kỳ hạn sớm).
   - Xác định rõ liệu các quyền chọn này có thể bóc tách để đối xử chuẩn hóa hay phải chuyển sang định giá lại độc lập tại Giai đoạn 4 theo [[automatic-interest-rate-options-standardised-valuation-and-volatility-shocks]].
2. *Đánh giá rủi ro mô hình hành vi (Behavioural Model Risk Assessment)*:
   - Thẩm định tính khả thi của việc mô hình hóa hành vi khách hàng trong các môi trường lãi suất khác nhau, đặc biệt là sự biến đổi tốc độ trả nợ trước hạn hoặc tháo chạy tiền gửi khi lãi suất thị trường tăng dựng đứng hoặc rơi vào vùng âm.
3. *Đánh giá năng lực ghi nhận của Hệ thống đo lường nội bộ (IMS Data Capabilities)*:
   - Kiểm tra xem hạ tầng công nghệ thông tin và hệ thống IMS có khả năng trích xuất dữ liệu giao dịch ở cấp độ chi tiết (deal-level data), phân rã đúng ngày định giá lại và tự động ánh xạ dòng tiền vào lịch 19 dải kỳ hạn theo [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]] hay không.
4. *Mô phỏng tác động biên lên dung sai rủi ro EVE và NII (Marginal Impact Simulation)*:
   - Mô phỏng tác động biên của quy mô sản phẩm dự kiến lên mức sử dụng hạn mức $\Delta EVE$ và $\Delta NII$ của ngân hàng, biên độ an toàn trước ngưỡng $15\%$ Vốn cấp 1 trong Bài kiểm tra tổ chức ngoại lai SOT theo [[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]], và mức phân bổ vốn kinh tế ICAAP theo [[irrbb-capital-allocation-framework-differentiates-economic-capital-from-earnings-buffers]].
5. *Tích hợp định giá điều chuyển vốn nội bộ (FTP Integration)*:
   - Bắt buộc các đơn vị kinh doanh phải đưa đầy đủ chi phí rủi ro thời lượng, chi phí quyền chọn ngầm định và phần bù thanh khoản của sản phẩm mới vào biểu giá FTP nội bộ, ngăn ngừa hiện tượng kinh doanh trục lợi bằng cách phát triển các sản phẩm tiềm ẩn rủi ro lãi suất cao nhưng không bị tính chi phí vốn thích đáng.

**2. Cơ chế quản trị phê duyệt và giám sát chiến lược phòng hộ (Hedging Governance)**

Chiến lược phòng hộ phái sinh (Hedging) là công cụ trọng yếu để ALCO điều chỉnh trạng thái khe hở kỳ hạn và bảo vệ vốn tự có. Tuy nhiên, việc sử dụng các công cụ phái sinh lãi suất (như IRS, Swaptions, Caps/Floors, Futures) đòi hỏi một khuôn khổ quản trị đa tầng nghiêm ngặt (Principle 3, Paragraph 27; Principle 7, Paragraph 66):
- *Phân định thẩm quyền phê duyệt*:
  - **Hội đồng quản trị (Board of Directors)**: Phê duyệt chính sách phòng hộ tổng thể, danh mục các công cụ phái sinh được phép sử dụng, và hạn mức dung sai rủi ro tối đa cho toàn bộ hoạt động phòng hộ;
  - **Hội đồng ALCO và Ban điều hành**: Phê duyệt các chiến lược phòng hộ cụ thể (macro hedging cho toàn bảng cân đối hoặc micro hedging cho các danh mục tài sản/nợ cụ thể) trong phạm vi hạn mức ủy quyền, bảo đảm tuân thủ nguyên tắc cách ly độc lập giữa Tuyến 2 (Quản trị rủi ro) và Tuyến 1 (Treasury thực thi giao dịch).
- *Thẩm định các rủi ro phát sinh từ giao dịch phòng hộ*:
  - *Rủi ro cơ sở phòng hộ (Hedging Basis Risk)*: Đánh giá độ phân kỳ giữa chỉ số tham chiếu của hợp đồng phái sinh (ví dụ SOFR OIS) và lãi suất của tài sản cơ sở được phòng hộ (ví dụ Lãi suất cho vay cơ sở Prime Rate), phòng ngừa nguy cơ phòng hộ không hoàn hảo theo [[interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]];
  - *Rủi ro kế toán phòng hộ (Hedge Accounting Risk)*: Đánh giá khả năng đáp ứng các tiêu chí kiểm tra tính hiệu quả kế toán phòng hộ (effectiveness testing) theo chuẩn mực kế toán tài chính, nhằm tránh hiện tượng chênh lệch ghi nhận biến động giá trị hợp lý vào P&L;
  - *Rủi ro thanh khoản ký quỹ (Liquidity Margin Call Risk)*: Lượng hóa dòng tiền ký quỹ bổ sung (variation margin) tiềm tàng mà ngân hàng phải chi trả cho đối tác bù trừ trung tâm (CCP) hoặc ngân hàng đại lý khi lãi suất thị trường dịch chuyển đột ngột ngược chiều với vị thế phái sinh.

**3. Chế độ báo cáo hiệu quả phòng hộ định kỳ (Principle 7 Reporting)**

Định kỳ tối thiểu hàng quý (hoặc hàng tháng khi thị trường biến động mạnh), bộ phận quản trị rủi ro độc lập phải lập báo cáo chuyên đề về hoạt động phòng hộ gửi lên ALCO và Hội đồng quản trị (Paragraph 66, d.324–327):
- *Đo lường hiệu quả phòng hộ thực tế*: So sánh mức độ giảm thiểu rủi ro EVE và NII đạt được trong thực tế so với mục tiêu đề ra khi thiết lập giao dịch phòng hộ;
- *Phân tích chi phí - lợi ích*: Báo cáo chi phí trả lãi/phí giao dịch phái sinh so với lợi ích kinh tế bảo toàn biên lãi thuần;
- *Cảnh báo trạng thái lệch pha*: Nhận diện các trạng thái "thừa phòng hộ" (over-hedged) phát sinh khi tài sản cơ sở bị khách hàng trả nợ trước hạn (prepayment) nhanh hơn dự kiến hoặc khi tiền gửi bị rút trước hạn, buộc ALCO phải phê duyệt các phương án tái cân đối hoặc tất toán vị thế phái sinh kịp thời.

Khuôn khổ quản trị này liên kết trực tiếp với [[irrbb-board-and-senior-management-governance-framework-enforces-delegation-and-independence]], hỗ trợ việc thiết lập hạn mức tại [[irrbb-risk-appetite-framework-establishes-multi-tiered-limits-and-escalation-protocols]], và đáp ứng các yêu cầu thuyết minh định tính tại Bảng A Trụ cột 3 theo [[pillar-3-irrbb-qualitative-disclosure-standards-mandate-table-a-narratives]].
