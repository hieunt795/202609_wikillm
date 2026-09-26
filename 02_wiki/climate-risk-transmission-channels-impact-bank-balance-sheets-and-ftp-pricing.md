---
title: climate-risk-transmission-channels-impact-bank-balance-sheets-and-ftp-pricing
type: concept
tags: [alm, climate-risk, esg, ftp, regulation, stress-testing]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Quản lý rủi ro khí hậu (*climate risk management* hay *carbon risk*) đang phát triển từ các vấn đề truyền thông đạo đức ban đầu (chống tẩy xanh—*greenwashing*) thành cấu phần cốt lõi trong quản trị ALM, tác động trực tiếp lên cấu trúc bảng cân đối ngân hàng thông qua 4 kênh truyền dẫn và đòi hỏi cơ chế định giá phụ phí khí hậu (*Climate FTP add-on*) trong hệ thống định giá chuyển vốn nội bộ (tata_bank_alm, Ch.6, §6.4, d.3169–3189).

Rủi ro khí hậu—bao gồm rủi ro vật lý (*physical risk* như bão lũ, hạn hán, sóng nhiệt cực đoan) và rủi ro chuyển đổi (*transition risk* phát sinh từ lộ trình phi carbon hóa theo Thỏa thuận Paris)—ảnh hưởng đến bảng cân đối và vốn tự có của ngân hàng qua 4 kênh truyền dẫn cơ bản (tata_bank_alm, Ch.6, §6.4, d.3175–3181):
1. **Kênh rủi ro tín dụng đối tác (*counterparty credit risk channel*)**: Khách hàng vay vốn và đối tác thị trường vốn bị suy giảm chất lượng tín dụng do thiệt hại tài sản hoặc chi phí tuân thủ phát thải gia tăng, ảnh hưởng trực tiếp đến dòng tiền thu hồi nợ và dự phòng rủi ro.
2. **Kênh huy động vốn (*funding channel*)**: Mức độ rủi ro khí hậu cảm nhận của thị trường ảnh hưởng đến khả năng phát hành trái phiếu và chi phí huy động vốn bán buôn của ngân hàng trên thị trường liên ngân hàng và thị trường vốn nợ.
3. **Kênh danh mục đầu tư (*investment channel*)**: Lợi suất và giá trị thị trường của danh mục chứng khoán chịu ảnh hưởng tiêu cực trước các sự kiện khí hậu cực đoan hoặc suy thoái của các ngành công nghiệp thâm dụng carbon.
4. **Kênh quy chế giám sát (*regulatory channel*)**: Các yêu cầu duy trì đệm vốn và đệm thanh khoản bổ sung từ cơ quan giám sát làm gia tăng chi phí vốn quy định (*regulatory cost of capital*).

Một trong những ứng dụng quan trọng nhất của ALM trong tương lai là tích hợp rủi ro khí hậu vào quy trình [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]]. Các thảm họa khí hậu thường kéo theo những thay đổi hành vi bất lợi của khách hàng (chậm thanh toán gốc lãi, tăng cường rút tiền gửi, hoặc đột ngột rút hết hạn mức tín dụng dự phòng). Do đó, Treasury thiết lập một khoản phụ phí khí hậu chuyên biệt (*Climate Risk Add-on*) bổ sung vào [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]] tương tự cơ chế [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]] nhằm áp mức phí phạt đối với những mảng kinh doanh tập trung phát thải cao hoặc nằm tại các vùng địa lý dễ bị tổn thương thiên tai (tata_bank_alm, Ch.6, §6.4, d.3182). Cơ chế định giá này liên kết trực tiếp với điểm số ESG và cường độ phát thải carbon của danh mục vay, gia tăng phụ phí COF cho các ngành công nghiệp thâm dụng carbon nhằm bù đắp rủi ro tín dụng ngầm và định hướng phân bổ nguồn lực bền vững theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] (tata_bank_alm, Ch.6, §6.4, d.3182–3189).

Về mặt giám sát pháp lý, Ngân hàng Trung ương Châu Âu (ECB) đã thúc đẩy quyết liệt việc lượng hóa rủi ro này. Cuộc kiểm tra sức ép rủi ro khí hậu năm 2022 của ECB (ECB Climate Risk Stress Test) trên hơn 100 ngân hàng lớn (Significant Institutions) chỉ ra rằng hầu hết các tổ chức chưa tích hợp thỏa đáng rủi ro khí hậu vào các mô hình nội bộ và khung kiểm tra sức ép (tata_bank_alm, Ch.6, §6.4, d.3184, d.3241–3242). Trong Hướng dẫn Mô hình Nội bộ năm 2024 (ECB Guide to Internal Models), ECB yêu cầu các ngân hàng bắt buộc phải đánh giá tính trọng yếu của các nhân tố rủi ro môi trường - khí hậu trong toàn bộ vòng đời mô hình và tích hợp chúng vào các mô hình nội bộ được phê duyệt tính vốn tự có đối với rủi ro tín dụng và rủi ro thị trường (tata_bank_alm, Ch.6, §6.4, d.3186–3188, d.3243).
