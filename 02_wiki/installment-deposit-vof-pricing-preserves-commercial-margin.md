---
title: installment-deposit-vof-pricing-preserves-commercial-margin
type: concept
tags: [alm, ftp, vof, installment-deposits, margin-preservation, deposits, market-1]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Đối với các sản phẩm tiền gửi tích lũy định kỳ (gửi góp), dòng tiền huy động phát sinh phân tán thành nhiều đợt nộp tiền định kỳ xuyên suốt kỳ hạn hợp đồng thay vì tập trung một lần tại ngày giải ngân ban đầu (vab_ftp_methodology, Điều 6.1.c.i, d.644). Đặc tính dòng tiền tích lũy dần này khiến chi phí lãi thực tế mà ngân hàng chi trả cho khách hàng gửi góp thường chênh lệch so với tiền gửi truyền thống, đòi hỏi phương pháp luận FTP phải thiết lập một kỹ thuật bù đắp biên độ thương mại (*margin preservation*) nhằm bảo đảm sự công bằng thù lao cho mạng lưới chi nhánh bán lẻ (vab_ftp_methodology, Điều 6.1.c.ii, d.645).

Trung tâm Điều chuyển Vốn Nội bộ (CFU) tính toán lãi suất mua vốn VOF cơ sở cho sản phẩm gửi góp bằng cách lấy lãi suất huy động thực tế của sản phẩm gửi góp cộng với mức chênh lệch biên độ quan sát được giữa giá VOF và lãi suất huy động của sản phẩm tiền gửi trả gốc cuối kỳ có cùng kỳ hạn (vab_ftp_methodology, Điều 6.1.c.ii, d.645):
$$VOF_{\text{gửi góp}} = \text{Lãi suất gửi góp} + \left( VOF_{\text{cuối kỳ}} - \text{Lãi suất}_{\text{cuối kỳ}} \right)$$
Ví dụ, khi khách hàng xác lập hợp đồng tiền gửi 12 tháng với số tiền cam kết 120 triệu đồng và nộp góp mỗi tháng 10 triệu đồng, CFU sẽ lấy lãi suất gửi góp 12 tháng cộng với phần chênh lệch giữa giá VOF 12 tháng và lãi suất tiền gửi trả cuối kỳ 12 tháng để xác định giá mua vốn cho tài khoản này (vab_ftp_methodology, Điều 6.1.c.ii, d.645).

Lãi suất VOF cơ sở tính theo công thức bù chênh lệch này được áp dụng cố định trong suốt thời gian gửi tiền của hợp đồng (vab_ftp_methodology, Điều 6.1.c.iii, d.646). Đồng thời, phần bù thanh khoản kỳ hạn được ấn định bằng 0% do toàn bộ hồ sơ thanh khoản đã được hấp thụ theo nguyên tắc của [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] (vab_ftp_methodology, Điều 6.1.c.iv, d.647). Quy tắc này kết nối chặt chẽ với cơ chế giá gốc của [[bullet-term-deposit-vof-pricing-locks-fixed-spread-at-origination]], giúp đơn vị kinh doanh bảo toàn trọn vẹn phần bù thù lao theo [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]] mà không bị ảnh hưởng tiêu cực bởi cấu trúc dòng tiền phân kỳ của sản phẩm tiết kiệm tích lũy.
