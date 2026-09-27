---
title: early-deposit-redemption-ftp-penalty-resets-vof-to-demand-rate
type: concept
tags: [alm, ftp, vof, early-redemption, embedded-options, deposit-penalties, market-1]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-27
---

Hành vi đơn phương rút tiền gửi có kỳ hạn trước ngày đáo hạn của khách hàng tạo ra rủi ro thanh khoản và rủi ro tái đầu tư đáng kể cho ngân hàng, làm phá vỡ kỳ hạn cam kết nguồn vốn ban đầu và buộc ngân hàng phải áp dụng cơ chế chế tài định giá điều chuyển vốn nội bộ (VOF) (vab_ftp_methodology, Điều 6.3.a, d.954–956). Để loại trừ động cơ tư lợi của các chi nhánh huy động và phản ánh đúng bản chất kinh tế của dòng tiền thực tế, phương pháp luận FTP thiết lập cơ chế tái định giá và truy thu thù lao tài chính ngay tại thời điểm biến cố rút vốn phát sinh (vab_ftp_methodology, Điều 6.3.a, d.957–961).

Khi khách hàng tất toán khoản tiền gửi trước hạn, Trung tâm Điều chuyển Vốn Nội bộ (CFU) lập tức chấm dứt hiệu lực của mức lãi suất VOF có kỳ hạn đã ấn định ban đầu và xác định lại lãi suất VOF cơ sở đối với khoản tiền gửi căn cứ trên lãi suất VOF không kỳ hạn thông thường có hiệu lực tại thời điểm rút vốn, áp dụng cho toàn bộ khoảng thời gian khách hàng thực gửi (vab_ftp_methodology, Điều 6.3.a.i–ii, d.958–960). Đồng thời, CFU kích hoạt quy trình phạt rút trước hạn đối với đơn vị kinh doanh bằng cách truy thu toàn bộ khoản hỗ trợ huy động ($Margin$) đã tạm chi trả và khấu trừ toàn bộ khoản chênh lệch giữa giá VOF kỳ hạn ban đầu với lãi suất không kỳ hạn mà khách hàng thực nhận (vab_ftp_methodology, Điều 6.1.b.vi, d.641; Điều 8.1.b, d.1035–1037).

Cơ chế tái lập giá này triệt tiêu hoàn toàn khả năng đơn vị kinh doanh ghi nhận lợi nhuận ảo từ các khoản tiền gửi kỳ hạn dài nhưng bị rút sớm, củng cố tính tôn ti của hợp đồng tiền gửi theo [[bullet-term-deposit-vof-pricing-locks-fixed-spread-at-origination]] và quy tắc tái tính toán giá chuyển nhượng tại [[contractual-amendment-ftp-repricing-rules-govern-loan-and-deposit-restructuring]]. Ở cấp độ toàn hệ thống, rủi ro rút tiền gửi trước hạn được tích hợp vào khuôn khổ phụ phí thanh khoản dự phòng tại [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]] và đối chiếu với mô hình tỷ lệ rút sớm cơ sở $TDRR$ theo chuẩn mực Basel III tại [[standardised-term-deposit-early-redemption-risk-and-tdrr-scalars]].
