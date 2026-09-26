---
title: macro-hedging-and-micro-hedging-strategies-in-the-banking-book
type: concept
tags: [alm, irrbb, hedging, macro-hedge, micro-hedge, derivatives, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Chiến lược phòng hộ vi mô (Micro-hedging) và phòng hộ vĩ mô (Macro-hedging / Portfolio hedging) là hai phương pháp tiếp cận cốt lõi trong ALM nhằm giảm thiểu phơi nhiễm rủi ro lãi suất trên sổ ngân hàng, trong đó phòng hộ vi mô gắn kết từng công cụ phái sinh riêng lẻ với từng tài sản/nợ cụ thể, còn phòng hộ vĩ mô trung hòa trạng thái nhạy cảm lãi suất tổng hợp (Net Repricing Gap hoặc DV01) của toàn bộ bảng cân đối kế toán (bcbs_368, file d368.md, Principle 3, d.160–168; Principle 7, d.314–327; Annex 1.2.7, d.910–930).

**1. Chiến lược Phòng hộ Vi mô (Micro-Hedging)**

Phòng hộ vi mô thiết lập mối quan hệ bảo hiểm rủi ro trực tiếp $1:1$ giữa một công cụ tài chính cụ thể trên sổ ngân hàng và một công cụ phái sinh ngoài thị trường:
- **Trường hợp áp dụng:** Thường được áp dụng cho các giao dịch đơn lẻ có quy mô danh nghĩa lớn, kỳ hạn dài và cấu trúc dòng tiền cố định rõ ràng. Ví dụ: Khi ngân hàng phát hành một đợt trái phiếu kỳ hạn 10 năm với lãi suất cố định $7{,}0\%$ ra thị trường công chúng, để tránh rủi ro chi phí vốn bị neo cao khi lãi suất thị trường giảm, Treasury thực hiện ngay một hợp đồng Hoán đổi Lãi suất (Payer/Receiver Interest Rate Swap - IRS) với quy mô và lịch trình dòng tiền hoàn toàn khớp với đợt trái phiếu, hoán đổi lãi suất cố định $7{,}0\%$ sang lãi suất thả nổi $3\text{M SOFR} + \text{Spread}$.
- **Ưu điểm Kế toán:** Mối quan hệ $1:1$ rõ ràng giúp ngân hàng dễ dàng đáp ứng các điều kiện khắt khe của Kế toán Phòng hộ (Hedge Accounting under IFRS 9 / IAS 39 - Fair Value Hedge), bám sát nguyên tắc tại [[accounting-treatment-of-banking-book-amortised-cost-versus-fair-value-under-irrbb]]. Sự biến động giá trị hợp lý của công cụ phái sinh sẽ bù trừ trực tiếp với sự biến động giá trị của công cụ nợ trên Báo cáo Kết quả Kinh doanh (P&L), triệt tiêu sự biến động giả tạo của lợi nhuận kế toán.
- **Hạn chế:** Phòng hộ vi mô cực kỳ tốn kém chi phí giao dịch, phân mảnh dòng tiền, làm tiêu hao hạn mức tín dụng đối tác (counterparty limits) và yêu cầu ký quỹ tài sản bảo đảm (margin requirements) lớn. Quan trọng nhất, phòng hộ vi mô hoàn toàn bất lực trong việc xử lý rủi ro cấu trúc nảy sinh từ hàng triệu giao dịch bán lẻ nhỏ lẻ có chứa quyền chọn hành vi (như NMDs và các khoản vay mua nhà).

**2. Chiến lược Phòng hộ Vĩ mô (Macro-Hedging / Portfolio Hedging)**

Thay vì phòng hộ từng tài khoản riêng lẻ, phòng hộ vĩ mô nhìn nhận ngân hàng như một danh mục hợp nhất toàn diện:
- **Cơ chế Vận hành:** Hệ thống ALM tổng hợp toàn bộ dòng tiền định giá lại từ tất cả các nhánh kinh doanh, áp dụng mô hình hành vi để phân bổ NMDs và tính toán dòng tiền trả trước của các khoản vay. Từ đó, Treasury xác định Trạng thái Khe hở Lãi suất Ròng (Net Repricing Gap) hoặc Độ nhạy Điểm Cơ bản Ròng (Net DV01) trên từng dải kỳ hạn, phối hợp với [[funds-transfer-pricing-as-an-irrbb-risk-transfer-and-steering-mechanism]].
- **Tận dụng Bù trừ Tự nhiên (Natural Netting):** Trước khi bước ra thị trường liên ngân hàng, các dòng tiền ngược chiều tự triệt tiêu lẫn nhau. Ví dụ: Rủi ro lãi suất dài hạn của danh mục cho vay mua nhà cố định được bù trừ tự nhiên bởi tính chất cố định dài hạn của nguồn vốn tiền gửi không kỳ hạn lõi (Core NMDs) theo mô hình danh mục mô phỏng ([[replicating-portfolio-optimization-methodology-for-nmds-and-equity]]).
- **Giao dịch Phái sinh Tập trung:** Treasury chỉ bước ra thị trường phái sinh để thực hiện một số ít các giao dịch hoán đổi lãi suất quy mô lớn (Macro Swaps), hợp đồng tương lai trái phiếu chính phủ (Bond Futures) hoặc hợp đồng Swaption nhằm đưa độ nhạy ròng của toàn ngân hàng về mức mục tiêu do ALCO đề ra.
- **Xung đột Kế toán (The Accounting Dilemma):** Chuẩn mực kế toán quốc tế IFRS 9 không hoàn toàn hỗ trợ kế toán phòng hộ cho danh mục mở biến động động (dynamic macro hedging). Do đó, các hợp đồng phái sinh macro thường bị hạch toán theo giá trị hợp lý qua lãi lỗ (FVTPL). Điều này dẫn đến nghịch lý: Về mặt kinh tế, bảng cân đối đã được phòng hộ an toàn tuyệt đối trước biến động lãi suất; nhưng về mặt kế toán, P&L hàng quý có thể bị biến động mạnh do lãi/lỗ phái sinh chưa thực hiện.

**3. Các Công cụ Phái sinh Cốt lõi và Chiến thuật Phòng hộ**

Theo Annex 1 của BCBS 368, ngân hàng triển khai danh mục công cụ phái sinh đa dạng để quản trị các trạng thái rủi ro:

| Công cụ Phái sinh | Mục tiêu Phòng hộ trong ALM | Trạng thái Bảng Cân đối được Phòng hộ |
|---|---|---|
| **Payer Interest Rate Swap** (Trả cố định, Nhận thả nổi) | Phòng hộ rủi ro lãi suất thị trường tăng cao làm sụt giảm thu nhập lãi thuần hoặc giảm giá trị tài sản cố định dài hạn | Danh mục tài sản cố định dài hạn vượt trội nguồn vốn cố định (Asset Sensitive to rate hikes) |
| **Receiver Interest Rate Swap** (Nhận cố định, Trả thả nổi) | Phòng hộ rủi ro lãi suất giảm sâu làm sụt giảm lợi suất tái đầu tư | Danh mục nguồn vốn cố định dài hạn hoặc chi phí huy động bị chặn sàn không thể giảm theo tài sản |
| **Amortising IRS** | Khớp lịch trình trả nợ gốc giảm dần | Danh mục cho vay trả góp mua nhà hoặc tài trợ dự án |
| **Payer / Receiver Swaptions** | Phòng hộ rủi ro phi tuyến tính, bảo hiểm trước hiện tượng độ lồi âm ([[effective-duration-and-effective-convexity-for-banking-book-optionalities]]) | Danh mục cho vay thế chấp có quyền trả nợ trước hạn cao khi lãi suất đảo chiều |
| **Basis Swaps (Tenor / Benchmark)** | Trung hòa rủi ro chênh lệch biên độ giữa các chỉ số lãi suất tham chiếu | Tài sản thả nổi theo SOFR nhưng nguồn vốn tài trợ thả nổi theo Fed Funds hoặc EURIBOR, quản trị theo [[basis-risk-quantification-and-tenor-basis-swaps-in-alm]] |

**4. Khung Quản trị và Giám sát theo Chuẩn mực BCBS 368**

Theo Principle 3 và Principle 7 của BCBS 368 và quy trình tại [[pre-acquisition-review-and-hedging-approval-governance-for-irrbb]]:
- **Phê duyệt Chiến lược của HĐQT:** HĐQT và ALCO phải phê duyệt rõ ràng ranh giới giữa hoạt động phòng hộ rủi ro thực chất (bona fide hedging) và hoạt động đầu cơ trạng thái (speculative positioning). Nghiêm cấm Treasury sử dụng danh nghĩa phòng hộ macro để thực hiện các trạng thái cược định hướng thị trường vượt khẩu vị rủi ro.
- **Đánh giá Tính Hiệu quả Phòng hộ (Hedging Effectiveness):** Định kỳ tối thiểu hàng quý, Treasury phải báo cáo cho ALCO mức độ hiệu quả của các hợp đồng phòng hộ. Phân tích chi tiết phần rủi ro không hoàn hảo (ineffectiveness) phát sinh do sự sai lệch giữa giả định hành vi khách hàng và thực tế dòng tiền.
- **Quản trị Rủi ro Tái cân bằng Động (Dynamic Rebalancing Costs):** Trong phòng hộ macro, khi hành vi khách hàng thay đổi theo chu kỳ kinh tế (ví dụ: tốc độ rút tiền gửi tăng lên), trạng thái ròng của bảng cân đối bị trôi dạt (drift). Treasury phải liên tục tái cân bằng danh mục phái sinh, và chi phí giao dịch phát sinh từ việc unwind hoặc bổ sung hợp đồng swap mới phải được tích hợp đầy đủ vào hệ thống đo lường hiệu quả kinh doanh.
