---
title: ftp-coordinates-asset-liability-structure-with-risk-adjusted-margin-allocation
type: analysis
tags: [alm, ftp, balance-sheet-structure, asset-liability-mismatch, margin-attribution, steering]
sources: [tata_bank_alm]
status: draft
last_updated: 2026-09-28
---

Cấu trúc tài sản – nợ (asset-liability structure) của một ngân hàng và cơ chế phân bổ biên lợi nhuận thông qua định giá chuyển giao vốn nội bộ (FTP) không thể tách rời: FTP là công cụ không chỉ để **phân bổ lợi nhuận đa mục tiêu** mà còn để **điều hướng cấu trúc cân đối** theo chiến lược của ngân hàng. Hai khía cạnh này tương tác trong một vòng phản hồi liên tục.

Từ góc độ [[the-typical-deposit-money-bank-balance-sheet-groups-assets-by-counterparty-and-liabilities-by-instrument]], cấu trúc tài sản – nợ được xác định bởi **kỳ hạn và loại khách hàng**: tiền gửi không kỳ hạn (CASA) từ khách hàng lẻ, tiền gửi kỳ hạn từ doanh nghiệp, khoản vay ngắn hạn cho vay dài hạn, v.v. Tuy nhiên, cấu trúc này không phải là tự nhiên — nó là kết quả của những quyết định chiến lược về **chi phí vốn huy động** và **lợi suất tài sản**. Từ góc độ [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]], **FTP curve quyết định ai được khuyến khích và ai bị "phạt"**: nếu FTP mua vốn (VOF) cao, bộ phận huy động tiền gửi được thưởng lớn → tiền gửi sẽ tăng; nếu FTP bán vốn (COF) cao, bộ phận cho vay được thưởng lớn → khối lượng cho vay sẽ tăng.

Cơ chế này thể hiện rõ ở [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]]: NII kế hoạch của ngân hàng phải được phân rã (decompose) thành hai phần — một phần cho bộ phận huy động ($n_1$%) và một phần cho bộ phận cho vay ($n_2$%) — dựa trên chiến lược kinh doanh. Nếu ngân hàng muốn tăng khối tiền gửi (ví dụ để cải thiện LCR), ALCO sẽ tăng $n_1$ → hỗ trợ huy động (margin) tăng → bộ phận huy động được thêm động lực. Ngược lại, nếu ngân hàng cần tăng cho vay để tuân thủ LDR, $n_2$ sẽ tăng → margin cho vay tăng.

Tại sâu hơn, [[ftp-curve-decomposition-separates-pure-interest-rate-risk-from-liquidity-premium]] giải thích tại sao chi phí vốn phải có **kỳ hạn khác nhau**: CoF(2 năm) > CoF(1 năm) bởi vì khi một khoản cho vay 2 năm được tài trợ bằng tiền gửi 1 năm, Treasury phải chịu hai rủi ro — rủi ro thanh khoản (tiền gửi hết thời hạn phải tái huy động) và rủi ro lãi suất (lãi suất có thể tăng lúc tái huy động, làm xâm thực NIM) (tata_bank_alm, Ch.2, 2.3.4, d.1629–1633). Bù đắp cho hai rủi ro này là **structural contribution** — phần lợi nhuận lớn hơn dành cho Treasury. Nếu cấu trúc bảng cân đối thay đổi (ví dụ: giảm tiền gửi dài hạn, tăng tiền gửi ngắn hạn), structural contribution có thể tăng vì mismatch tăng, từ đó FTP curve phải dốc hơn (tata_bank_alm, Ch.2, 2.3.5, d.1639–1661).

Kết quả là cấu trúc bảng cân đối và FTP curve là hai mặt của cùng một vấn đề: **cấu trúc xác định rủi ro, FTP giảm thiểu rủi ro + phân bổ lợi nhuận.** Khi [[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions|ALM team điều hướng cấu trúc 4 chiều kích]], FTP team phải thích ứng FTP curve để phản ánh chi phí thực tế; ngược lại, khi FTP được điều chỉnh để steering business lines, cấu trúc bảng cân đối sẽ dần thay đổi theo hành vi của các bộ phận. Sự tương tác này cũng được kiểm soát bởi [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] — những quy định buộc FTP phải reflect thêm những chi phí không nhìn thấy (HQLA buffer cost, NSFR compliance cost), từ đó làm thay đổi incentive của mỗi business line đối với cấu trúc bảng cân đối mà họ tạo ra.

Trong thực hành ALM tiên tiến ([[holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage]]), ngân hàng tích hợp hai công cụ này thành một hệ thống feedback duy nhất: FTP curve không chỉ là công cụ định giá mà là **steering lever** để đạt tới cấu trúc bảng cân đối mục tiêu theo chiến lược vốn.
