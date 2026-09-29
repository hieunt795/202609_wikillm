---
title: bullet-term-deposit-vof-pricing-locks-fixed-spread-at-origination
type: concept
tags: [alm, ftp, vof, deposits, bullet-deposits, market-1, nim-margin]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Trong cấu trúc điều chuyển vốn nội bộ Thị trường 1, sản phẩm tiền gửi có kỳ hạn thanh toán gốc một lần khi đáo hạn (bullet payment) với lãi suất cố định hoặc thả nổi được định giá mua vốn (VOF) dựa trên nguyên tắc khóa cố định biên độ tại thời điểm phát sinh giao dịch (vab_ftp_methodology, Điều 6.1.b, d.627–641). Trung tâm Điều chuyển Vốn Nội bộ (CFU) xác định lãi suất VOF cơ sở tương ứng trực tiếp với kỳ hạn gốc của khoản tiền gửi căn cứ vào biểu lãi suất VOF Thị trường 1 ban hành có hiệu lực tại ngày khách hàng mở tài khoản gửi tiền (vab_ftp_methodology, Điều 6.1.b.ii, d.630). Mức lãi suất VOF cơ sở này được áp dụng cố định trong suốt thời gian tồn tại của khoản tiền gửi, bất kể lãi suất huy động thực tế trả cho khách hàng biến động theo loại hình cố định hay thả nổi (vab_ftp_methodology, Điều 6.1.b.iii, d.638).

Do rủi ro thanh khoản kỳ hạn của nguồn tiền gửi có kỳ hạn đã được tích hợp trọn vẹn vào cấu trúc đường cong mua vốn chuẩn theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]], CFU ấn định phần bù thanh khoản kỳ hạn của sản phẩm tiền gửi trả cuối kỳ bằng 0% trong suốt thời hạn gửi tiền (vab_ftp_methodology, Điều 6.1.b.iv, d.639). Để thúc đẩy mạng lưới chi nhánh mở rộng quy mô huy động vốn bán lẻ, đơn vị kinh doanh được hưởng thêm cấu phần hỗ trợ huy động ($Margin$) phân bổ từ chỉ tiêu kế hoạch kinh doanh theo [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]] (vab_ftp_methodology, Điều 6.1.b.v, d.640). Trường hợp khoản tiền gửi có kỳ hạn thực tế không trùng khớp với các mốc chuẩn trên biểu ban hành, hệ thống FTP tự động tính toán lãi suất bằng phương pháp nội suy hoặc ngoại suy tuyến tính giữa hai kỳ hạn chuẩn liền kề căn cứ trên số ngày thực tế của năm tài chính (vab_ftp_methodology, Điều 6.1.a, d.623–625).

Cơ chế khóa giá cố định này cô lập hoàn toàn các chi nhánh huy động khỏi rủi ro lãi suất thị trường, giao toàn bộ trách nhiệm quản trị tái tài trợ cho khối Treasury theo [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]]. Tuy nhiên, nếu khách hàng đơn phương kích hoạt quyền chọn rút vốn trước ngày đáo hạn theo thỏa thuận hợp đồng, toàn bộ mức lãi suất VOF cố định cùng thù lao Margin đã thanh toán sẽ bị hủy bỏ và tái định giá theo quy tắc phạt rút sớm của [[early-deposit-redemption-ftp-penalty-resets-vof-to-demand-rate]].
