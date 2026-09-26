---
title: equity-endowment-effect-and-replicating-portfolio-in-alm
type: concept
tags: [banking, alm, irrbb, equity-endowment, replicating-portfolio, nii-vs-eve-tradeoff, structural-hedging, bcbs-368]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Hiệu ứng lợi suất thừa kế của vốn tự có và kỹ thuật danh mục mô phỏng (Equity Endowment Effect and Replicating Portfolio in ALM) phân tích bản chất cấu trúc của vốn chủ sở hữu và nguồn tiền gửi không kỳ hạn trong quản trị cân đối tài sản - nợ, làm rõ sự đánh đổi tất yếu (inherent trade-off) giữa việc ổn định thu nhập lãi thuần ($\Delta NII$) và ổn định giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) theo Chuẩn mực BCBS 368 của Ủy ban Basel (bcbs_368, file d368.md, Annex 1.3.4–3.5, d.970–987; Footnote 35, 38, 39).

Trong bảng cân đối ngân hàng, vốn chủ sở hữu kế toán là giá trị thặng dư ròng giữa tổng tài sản và tổng nợ phải trả ($E = A - L$). Về mặt tài chính, vốn tự có cấu thành một nguồn tài trợ cấu trúc (structural funding) cho một danh mục tài sản thặng dư mà ngân hàng hoàn toàn không phải chi trả chi phí lãi suất hợp đồng trực tiếp. Khả năng tạo ra dòng tiền lãi từ tài sản được tài trợ bởi nguồn vốn "miễn phí" này được gọi là **Lợi suất thừa kế của vốn tự có (Equity endowment return)** (Annex 1.3.5, d.982–987).

**Nhu cầu quản trị ổn định thu nhập và Danh mục mô phỏng (Replicating Portfolio)**

Mặc dù không có chi phí lãi suất hợp đồng, vốn chủ sở hữu đòi hỏi chi phí sử dụng vốn (cost of capital) dưới hình thức chi trả cổ tức cho cổ đông. Để ổn định tỷ suất lợi nhuận trên vốn (ROE) và chi trả cổ tức ổn định, ngân hàng có mục tiêu chiến lược là bảo vệ thu nhập phát sinh từ nguồn vốn tự có trước những biến động của lãi suất thị trường (Annex 1.3.5, d.984). Tương tự như vốn tự có, tiền gửi không kỳ hạn (NMDs) cũng là nguồn vốn chi phí thấp, không có ngày định giá lại hợp đồng xác định và có số dư ổn định lớn theo thời gian (Annex 1.3.4, d.972–974).

Để triệt tiêu biến động thu nhập phát sinh từ vốn tự có và tiền gửi không kỳ hạn lõi, bộ phận Quản trị Tài sản - Nợ (ALM) áp dụng **Kỹ thuật danh mục đầu tư mô phỏng (Replicating Portfolio technique)** (Footnote 38, d.1002):
- Ngân hàng xác định quy mô vốn tự có ròng hợp lệ (eligible net equity capital) bằng cách khấu trừ các tài sản phi sinh lời (như trụ sở, đất đai, tài sản cố định) và một phần vốn được giữ ngắn hạn làm đệm thanh khoản hấp thụ tổn thất (Footnote 39, d.1004).
- Ngân hàng giải ngân nguồn vốn này vào một danh mục tài sản sinh lời có lãi suất cố định kỳ hạn (như trái phiếu chính phủ hoặc hoán đổi lãi suất IRS nhận cố định) với cơ chế giải ngân và tái đầu tư cuốn chiếu liên tục (rolling reinvestment).
- *Ví dụ thực nghiệm Basel (Footnote 38)*: Một danh mục mô phỏng kỳ hạn 5 năm được vận hành bằng cách chia đều nguồn vốn thành $60$ phần bằng nhau; mỗi tháng, ngân hàng tái đầu tư $1/60$ tổng danh mục vào công cụ lãi suất cố định kỳ hạn 5 năm mới. Cơ chế này duy trì một danh mục có kỳ hạn bình quân gia quyền không đổi là $2{,}5$ năm và mang lại tỷ suất lợi nhuận bình quân động (moving average return) của lãi suất 5 năm, triệt tiêu hoàn toàn sự biến động ngắn hạn của lãi suất thị trường đối với thu nhập lãi thuần.

**Sự đánh đổi không thể dung hòa giữa ổn định NII và ổn định EVE**

Ủy ban Basel nhấn mạnh một nguyên lý nền tảng của quản trị ALM: **Ngân hàng không thể nào triệt tiêu đồng thời cả rủi ro giá trị kinh tế (EVE risk) lẫn rủi ro thu nhập (NII risk)** (Footnote 35, d.958). Sự đánh đổi này diễn ra như sau:
1. *Chiến lược tối đa hóa ổn định thu nhập*: Nếu mục tiêu của ngân hàng là khóa chặt thu nhập (zero earnings volatility), ngân hàng phải đầu tư toàn bộ vốn tự có vào các tài sản lãi suất cố định kỳ hạn dài (như trái phiếu chính phủ 10–20 năm). Khi đó, thu nhập lãi hàng năm được bảo đảm tuyệt đối; tuy nhiên, khi lãi suất thị trường tăng vọt, giá trị thị trường của danh mục tài sản dài hạn này sụt giảm thảm khốc, đẩy ngân hàng vào tình trạng sụt giảm giá trị kinh tế vốn chủ sở hữu ($\Delta EVE$) cực lớn.
2. *Chiến lược tối đa hóa ổn định giá trị kinh tế*: Nếu mục tiêu của ngân hàng là bảo toàn tuyệt đối giá trị kinh tế (zero EV risk), ngân hàng phải đầu tư toàn bộ vốn tự có vào thị trường tiền tệ qua đêm (overnight market). Khi đó, giá trị hiện tại của tài sản luôn bằng mệnh giá (reset to par), $\Delta EVE = 0$; tuy nhiên, thu nhập lãi thuần (NII) của ngân hàng sẽ biến động dữ dội và hoàn toàn phụ thuộc vào từng bước nhảy lãi suất điều hành của ngân hàng trung ương.

Do đó, vị thế phòng hộ cấu trúc cho thu nhập (structural hedge for NII) bản chất là việc chấp nhận một mức phơi nhiễm rủi ro giá trị kinh tế ($\Delta EVE$) có tính toán (Annex 1.2.3, d.932).

**Đối xử của Cơ quan Giám sát: Loại trừ vốn tự có trong tính toán EVE**

Trong quản trị nội bộ, ngân hàng có thể xây dựng mô hình *Giá trị kinh tế điều chỉnh theo thu nhập (Earnings-adjusted EV)* bằng cách gán thời lượng hành vi của danh mục mô phỏng cho vốn tự có (Annex 1.2.1, d.897; 1.4.2, d.1013).

Tuy nhiên, từ góc độ an toàn hệ thống và giám sát thận trọng, Ủy ban Basel xác lập nguyên tắc cứng rắn: **Trong các thước đo EVE chuẩn hóa và Bài kiểm tra tổ chức ngoại lai (SOT), vốn chủ sở hữu bắt buộc phải bị loại trừ hoàn toàn (Equity exclusion)** (Annex 1.4.2, d.1012; Principle 8 & 12). Lý do là vì trong các biến cố căng thẳng nghiêm trọng hoặc khi ngân hàng đối mặt với nguy cơ đổ vỡ, các khoản lỗ kinh tế trên tài sản sẽ trực tiếp ăn mòn lớp đệm vốn tự có; việc cho phép gán kỳ hạn hành vi cho vốn tự có để triệt tiêu thời lượng tài sản sẽ che giấu mức độ dễ bị tổn thương thực tế của hệ thống ngân hàng.

Nguyên lý này kết nối trực tiếp với [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]], định hình quy tắc loại trừ vốn trong [[delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion]], và chi phối cách phân bổ dòng tiền trong [[irrbb-standardised-framework-five-stage-measurement-architecture]].
