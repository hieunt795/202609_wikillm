---
title: zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp
type: concept
tags: [alm, zero-lower-bound, nirp, rigid-deposits, margin-compression, negative-rates]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Kỷ nguyên chính sách lãi suất âm (Negative Interest Rate Policy — NIRP), được Ngân hàng Trung ương Châu Âu (ECB) kích hoạt từ ngày 05/06/2014 khi hạ lãi suất tiền gửi cơ sở (*deposit facility*) xuống -0,10% và kéo dài suốt 8 năm, đã phá vỡ tiên đề căn bản của lý thuyết tài chính truyền thống vốn giả định lãi suất phân phối log-normal với xác suất âm bằng 0 (tata_bank_alm, Ch.3, Negative Interest Rates, d.2419). Trong khi các giao dịch định chế bán buôn liên ngân hàng (như hợp đồng phái sinh chuẩn hóa ISDA Negative Interest Protocol hay thị trường Repo) thích ứng dễ dàng với lãi suất âm, hoạt động ngân hàng bán lẻ lại va chạm trực diện với **sàn lãi suất 0% (Zero Lower Bound / 0% Interest Rate Floor)** (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2423–2425; tata_bank_alm, Ch.3, Notes, d.2510).

Đối với các khoản tiền gửi của khách hàng cá nhân bán lẻ, việc áp dụng lãi suất âm bị ngăn cản nghiêm ngặt bởi luật bảo vệ người tiêu dùng hoặc bởi nguy cơ đánh mất quan hệ khách hàng (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2425). Do đó, mức lãi suất thực tế trả cho người gửi tiền không còn tuân theo công thức thả nổi $r_I \pm x$ mà bị chặn cứng tại mức $\max(r_I \pm x; 0\%)$ (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2425). Sàn lãi suất 0% này biến thành một quyền chọn hành vi ngầm định nằm sâu trong trạng thái sinh lời (*deep in-the-money*), cho phép người dân từ chối bị phạt lãi suất âm (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2427).

Hiện tượng này tạo ra hệ quả kinh tế vĩ mô sâu sắc: tiền gửi thanh toán bán lẻ không bị tính lãi âm bất ngờ trở thành một kênh tài sản trú ẩn hấp dẫn vượt trội so với các công cụ thu nhập cố định ngắn hạn khác (tata_bank_alm, Ch.3, Economic Implications, d.2443; tata_bank_alm, Ch.3, Notes, d.2513). Dòng tiền ồ ạt chảy vào các tài khoản thanh toán, hình thành nên khối **"tiền gửi cứng nhắc" (Rigid Deposits)** — được Grandi và Guille (2023) định nghĩa là các khoản tiền gửi có lãi suất hoàn toàn trơ lỳ, không thể co giãn giảm thêm khi lãi suất thị trường xuyên thủng mốc 0% (tata_bank_alm, Ch.3, Economic Implications, d.2443; tata_bank_alm, Ch.3, Notes, d.2515).

Nghiên cứu của Demiralp, Eisenschmidt và Vlassopoulos (2021) chứng minh rằng NIRP vận hành hoàn toàn khác biệt so với các đợt cắt giảm lãi suất thông thường (tata_bank_alm, Ch.3, Economic Implications, d.2445): do tiền mặt giấy (*banknotes*) tồn tại như một kho lưu trữ giá trị với lợi suất cố định bằng 0%, các ngân hàng không thể chuyển chi phí vốn âm sang người gửi tiền bán lẻ; trong khi đó, lợi suất sinh lời từ các tài sản nợ (trái phiếu, tín dụng) liên tục suy giảm theo lãi suất chính sách, dẫn đến **sự xói mòn nghiêm trọng của biên trung gian tài chính (*declining intermediation margins*)** (tata_bank_alm, Ch.3, Economic Implications, d.2445).

Để bảo vệ lợi nhuận trong kỷ nguyên lãi suất âm, các ngân hàng phụ thuộc tiền gửi buộc phải phản ứng thông qua ba chiến lược tái cơ cấu bảng cân đối (tata_bank_alm, Ch.3, Economic Implications, d.2447):
1. Dịch chuyển cơ cấu tài sản sang các công cụ rủi ro cao hơn để tìm kiếm lợi suất (*reach for yield*);
2. Tăng mạnh biên độ lãi suất đối với các khoản vay mới nhằm bù đắp phần biên tiền gửi đã mất;
3. Đẩy mạnh các nguồn thu từ phí dịch vụ và hoa hồng giao dịch phi tín dụng.

Về mặt pháp lý, phán quyết bước ngoặt của Tòa án Tối cao Liên bang Đức (Bundesgerichtshof — BGH 2023 XI ZR 544/21) đã làm rõ rằng lãi suất cho vay không thể âm, bởi bản chất cốt lõi của hợp đồng tín dụng đòi hỏi tiền vay phải sinh lợi cho bên cho vay, tạo ra một sàn 0% ngầm định bảo vệ ngân hàng trên kênh tài sản (tata_bank_alm, Ch.3, Notes, d.2519). 

Cơ chế sàn 0% tạo ra sự biến dạng phức tạp được lượng hóa qua [[coupon-floors-and-indicator-floors-induce-asymmetric-nii-exposures-in-negative-rates]], bóp méo việc định giá [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]], làm suy sụp hệ số deposit beta theo [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]], thách thức năng lực điều hành của [[bank-specific-alm-tailors-balance-sheet-governance-to-business-models-and-regional-habitats]], và gieo mầm cho những tổn thương nặng nề khi môi trường đảo chiều sang [[rapid-rate-tightening-exposes-duration-gaps-and-asymmetric-prepayment-speeds]]. Đồng thời, để mô phỏng chính xác các cú sốc lãi suất âm mà không bóp méo dòng tiền chiết khấu dài hạn, cơ quan giám sát đã chuẩn hóa giới hạn chặn dưới của đường cong lợi suất thành [[maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb]].
