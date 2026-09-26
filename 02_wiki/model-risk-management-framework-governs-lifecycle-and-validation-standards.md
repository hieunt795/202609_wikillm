---
title: model-risk-management-framework-governs-lifecycle-and-validation-standards
type: concept
tags: [banking, model-risk, model-governance, model-validation, irb, three-lines-of-defense, regulation]
sources: [sbv_circular_83_2025]
status: stable
last_updated: 2026-09-26
---

Khung quản lý rủi ro mô hình (Model Risk Management - MRM) theo quy chuẩn kiểm soát nội bộ ngành ngân hàng thiết lập cơ chế giám sát toàn diện đối với toàn bộ chu kỳ sống của các mô hình định lượng tài chính, nhằm kiểm soát các sai lệch phát sinh từ dữ liệu đầu vào không đầy đủ, giả định kỹ thuật không phù hợp, lỗi thuật toán hoặc việc lạm dụng/áp dụng sai kết quả mô hình trong việc ra quyết định kinh doanh và lượng hóa an toàn vốn (sbv_circular_83_2025, file TT83.md, Điều 56–58, d.956–993).

**1. Phân loại mức độ rủi ro mô hình và danh mục quản lý bắt buộc**

Ngân hàng phải thiết lập và duy trì danh mục toàn bộ các mô hình cần quản lý theo quy định nội bộ, định kỳ xếp hạng và phân loại thành mô hình có rủi ro cao, trung bình hoặc thấp dựa trên các tiêu chí kỹ thuật:
- Tính trọng yếu (materiality): Mức độ ảnh hưởng của kết quả mô hình đến bảng cân đối kế toán, mức vốn yêu cầu, chỉ tiêu an toàn vốn và quyết định kinh doanh cốt lõi.
- Tính phức tạp (complexity): Cấu trúc thuật toán, giả định toán học, mức độ phi tuyến tính hoặc khả năng tự thích ứng (như các mô hình học máy/trí tuệ nhân tạo).
- Mục đích sử dụng (purpose): Ứng dụng trong định hạng tín dụng nội bộ, trích lập dự phòng rủi ro tín dụng, định giá tài sản tài chính, quản trị rủi ro thanh khoản hoặc kiểm tra sức chịu đựng vốn (ICAAP).
- Chất lượng mô hình (quality): Độ ổn định lịch sử, tần suất xuất hiện ngoại lệ và tính sẵn sàng của dữ liệu hiệu chuẩn.
- **Quy định bắt buộc đối với phương pháp IRB**: Kể từ thời điểm ngân hàng bắt đầu thực hiện giai đoạn chuyển đổi sang phương pháp xếp hạng nội bộ (Internal Ratings-Based - IRB) theo quy định an toàn vốn của Ngân hàng Nhà nước, tất cả các mô hình được sử dụng trong phương pháp IRB (như PD, LGD, EAD theo [[irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility]]) bắt buộc phải được phân loại và quản trị theo cấp độ **mô hình có rủi ro cao** (sbv_circular_83_2025, file TT83.md, Điều 56.1, d.956).

**2. Quản trị vòng đời mô hình năm giai đoạn (Model Lifecycle Governance)**

Đối với các mô hình do ngân hàng tự phát triển nội bộ hoặc thuê ngoài phát triển, quy trình quản trị rủi ro phải bao quát đầy đủ 5 giai đoạn vòng đời kỹ thuật:
- **Giai đoạn xây dựng (Development)**: Xác định rõ ràng mục đích sử dụng, phạm vi ứng dụng dự kiến; đánh giá nghiêm ngặt chất lượng dữ liệu đầu vào (tính chính xác, tính đầy đủ, tính đại diện thống kê và chiều dài chuỗi thời gian) theo quy định nội bộ (sbv_circular_83_2025, file TT83.md, Điều 56.4.a, d.960).
- **Giai đoạn triển khai (Implementation & UAT)**: Tiến hành kiểm thử chấp nhận người dùng (User Acceptance Testing - UAT), đối chiếu kết quả tích hợp trên hệ thống CNTT lõi với thuật toán đã phê duyệt. Bất kỳ sự khác biệt hoặc điều chỉnh mã nguồn nào so với kết quả xây dựng ban đầu đều phải được cấp có thẩm quyền phê duyệt lại và lưu giữ đầy đủ trong hồ sơ mô hình (sbv_circular_83_2025, file TT83.md, Điều 56.4.b, d.961).
- **Giai đoạn sử dụng và kiểm soát ghi đè (Usage & Override Governance)**: Đảm bảo mô hình được vận hành nghiêm ngặt trong phạm vi thiết kế. Thiết lập cơ chế kiểm soát việc ghi đè (override) dữ liệu đầu vào hoặc kết quả đầu ra (khi chuyên viên phân tích hoặc cấp quản lý bỏ qua, thay đổi hoặc đảo ngược kết quả tính toán tự động): phải quy định rõ điều kiện được ghi đè, thẩm quyền phê duyệt ghi đè, lưu vết kiểm toán và định kỳ đánh giá tính khách quan của các trường hợp ghi đè để phát hiện thiên vị chủ quan; xử lý kịp thời các phản hồi từ bộ phận kinh doanh sử dụng (sbv_circular_83_2025, file TT83.md, Điều 56.4.c, d.962–966).
- **Giai đoạn theo dõi và giám sát (Monitoring)**: Đo lường liên tục tính hiệu quả thực tế của mô hình trong vận hành kinh doanh, giám sát độ ổn định dân số mẫu (Population Stability Index - PSI) và chất lượng phân loại/dự báo theo thời gian thực (sbv_circular_83_2025, file TT83.md, Điều 56.4.d, d.967).
- **Giai đoạn kiểm định mô hình (Model Validation)**: Thực hiện kiểm định độc lập bao gồm 3 mốc bắt buộc:
  1. Kiểm định trước khi đưa vào sử dụng chính thức (Initial Validation).
  2. Kiểm định khi có thay đổi trọng yếu về thuật toán, giả định hoặc biến số kinh tế vĩ mô (Material Change Validation).
  3. Kiểm định định kỳ tối thiểu hằng năm (Periodic Annual Validation).
  Báo cáo kiểm định phải đánh giá cụ thể mức độ đáp ứng mục tiêu ban đầu và hiệu quả sử dụng thực tế (sbv_circular_83_2025, file TT83.md, Điều 56.4.đ, d.968).

**3. Cơ chế ba tuyến bảo vệ chuyên biệt trong quản lý rủi ro mô hình**

Quy định chuẩn hóa sự phân lập độc lập giữa 3 tuyến phòng thủ theo [[three-lines-of-defense-framework-enforces-banking-internal-control-and-risk-oversight]] để loại bỏ xung đột lợi ích giữa phát triển và thẩm định (sbv_circular_83_2025, file TT83.md, Điều 56.7, d.973–976):
- **Tuyến 1 (First Line)**: Bộ phận hoặc cá nhân trực tiếp xây dựng mô hình (Model Developers), triển khai kỹ thuật, người dùng vận hành mô hình (Model Users); chịu trách nhiệm nhận dạng rủi ro ban đầu, áp dụng các biện pháp kiểm soát vận hành và giám sát chất lượng dữ liệu.
- **Tuyến 2 (Second Line)**: Bộ phận kiểm định mô hình độc lập (Independent Model Validation Unit), bộ phận xây dựng chính sách quản lý rủi ro mô hình; chịu trách nhiệm đánh giá lại cơ sở toán học, kiểm tra tính vững (robustness), thực hiện kiểm thử nghịch đảo/stress test mô hình, theo dõi và kiểm soát rủi ro toàn ngân hàng, đảm bảo tuân thủ pháp lý. Tuyến 2 hoàn toàn độc lập về cơ cấu tổ chức và nhân sự với Tuyến 1.
- **Tuyến 3 (Third Line)**: Bộ phận kiểm toán nội bộ độc lập trực thuộc Ban kiểm soát theo [[risk-based-internal-audit-framework-enforces-third-line-oversight-and-governance]]; thực hiện kiểm toán định kỳ tính hiệu lực của khung quản lý rủi ro mô hình và kiểm tra sự tuân thủ các chuẩn mực kiểm định của Tuyến 2.

**4. Quản lý mô hình mua ngoài, mô hình chuyển giao từ ngân hàng mẹ và hồ sơ mô hình**

Trường hợp ngân hàng sử dụng mô hình mua từ nhà cung cấp giải pháp bên ngoài hoặc tiếp nhận từ ngân hàng mẹ (đối với chi nhánh ngân hàng nước ngoài và ngân hàng con có vốn nước ngoài), ngân hàng không được xem mô hình là "hộp đen" bất khả xâm phạm. Ngân hàng bắt buộc phải:
- Yêu cầu bên bán hoặc ngân hàng mẹ cung cấp đầy đủ tài liệu kỹ thuật, giả định toán học, cấu trúc dữ liệu và phương pháp kiểm thử để phục vụ công tác đánh giá độc lập (sbv_circular_83_2025, file TT83.md, Điều 56.5.a, d.970).
- Thực hiện đánh giá hiệu quả sử dụng thực tế và tính tương thích của mô hình với đặc thù danh mục tài sản và môi trường kinh tế Việt Nam (sbv_circular_83_2025, file TT83.md, Điều 56.5.b, d.971; liên kết [[model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity]]).
- Quản lý hồ sơ mô hình (Model Inventory & Documentation): Lập và lưu trữ tập trung hồ sơ mô hình hoàn chỉnh cho tất cả các mô hình có rủi ro cao và trung bình, bao gồm các mô hình đang vận hành, mô hình đang điều chỉnh và cả các mô hình đã ngừng sử dụng (sbv_circular_83_2025, file TT83.md, Điều 56.6, d.972).

**5. Chế độ báo cáo nội bộ và lộ trình chuyển tiếp**

Định kỳ tối thiểu hằng năm hoặc đột xuất, ngân hàng phải lập báo cáo rủi ro mô hình trình Hội đồng quản trị/Hội đồng thành viên và Tổng giám đốc, bao quát: danh mục mô hình phân loại rủi ro (cao, trung bình, thấp), danh mục mô hình thay đổi/ngừng sử dụng, kết quả kiểm định độc lập, các kiến nghị khắc phục (remedial actions) và tình hình thực hiện kiến nghị của kiểm toán nội bộ hoặc cơ quan thanh tra (sbv_circular_83_2025, file TT83.md, Điều 58, d.983–993; Phụ lục II.II.7, d.1407–1416).
- **Lộ trình thực hiện**: Ngân hàng chuyển đổi sang phương pháp IRB trước ngày 01/07/2026 phải áp dụng đầy đủ quy định quản lý rủi ro mô hình đối với mô hình IRB ngay từ ngày 01/07/2026. Tất cả các ngân hàng thương mại còn lại phải hoàn thành việc thiết lập và vận hành toàn diện khung quản trị rủi ro mô hình cho toàn bộ danh mục mô hình chậm nhất kể từ ngày 01/01/2028 (sbv_circular_83_2025, file TT83.md, Điều 74.3, d.1237–1240).

Xem thêm: [[irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility]], [[three-lines-of-defense-framework-enforces-banking-internal-control-and-risk-oversight]], [[model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity]], [[risk-based-internal-audit-framework-enforces-third-line-oversight-and-governance]], [[icaap-framework-determines-economic-capital-and-target-capital-under-stress]].
