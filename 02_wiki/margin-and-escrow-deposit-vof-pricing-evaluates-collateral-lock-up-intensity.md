---
title: margin-and-escrow-deposit-vof-pricing-evaluates-collateral-lock-up-intensity
type: concept
tags: [alm, ftp, vof, margin-deposits, escrow, collateral, market-1]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Tiền gửi ký quỹ phát sinh từ các nghĩa vụ ràng buộc pháp lý chặt chẽ giữa khách hàng với ngân hàng nhằm bảo đảm thực hiện các nghĩa vụ liên quan đến tài sản có, bao gồm tiền gửi ký quỹ thực hiện giao dịch phái sinh tiền tệ và ký quỹ duy trì điều kiện kinh doanh trong các ngành nghề đặc thù có điều kiện như kinh doanh bảo hiểm, bán hàng đa cấp hoặc cho thuê lại lao động (vab_ftp_methodology, Điều 6.1.d.ii, d.689–690). Bản chất của số dư ký quỹ là bị phong tỏa tạm thời nhưng có thể giải tỏa khi nghĩa vụ bảo đảm chấm dứt, đặt ra yêu cầu đánh giá mức độ ràng buộc thanh khoản thực tế khi định giá mua vốn (VOF) (vab_ftp_methodology, Điều 6.1.d.ii, d.691–693).

Phương pháp luận FTP thiết lập hai phương án tiếp cận định giá VOF cơ sở đối với các tài khoản ký quỹ (vab_ftp_methodology, Điều 6.1.d.ii, d.691–696):
1. **Phương án xem như tiền gửi không kỳ hạn**: Khi tài khoản ký quỹ có biến động thường xuyên hoặc thời gian phong tỏa không xác định trước, CFU định giá VOF cơ sở tương tự như sản phẩm tiền gửi không kỳ hạn theo [[non-maturity-deposit-vof-pricing-combines-redemption-curve-and-regulatory-floor]], với mức lãi suất mua vốn được hệ thống cập nhật tự động hàng ngày (vab_ftp_methodology, Điều 6.1.d.ii, d.692, d.695);
2. **Phương án đối ứng kỳ hạn cam kết**: Khi hợp đồng ký quỹ xác định rõ thời hạn phong tỏa pháp lý và chi phí trả lãi cho khách hàng tương đương tiền gửi có kỳ hạn, ngân hàng áp dụng cơ chế FTP có kỳ hạn tương ứng với thời gian phong tỏa cam kết, với lãi suất VOF cơ sở được giữ cố định trong suốt kỳ hạn hiệu lực của thỏa thuận (vab_ftp_methodology, Điều 6.1.d.ii, d.693, d.696).

Trong cả hai phương án định giá, phần bù thanh khoản kỳ hạn của tiền gửi ký quỹ đều được ấn định bằng 0% trong suốt thời gian giao dịch (vab_ftp_methodology, Điều 6.1.d.ii, d.697). Khác với tiền gửi không kỳ hạn thông thường, các đơn vị kinh doanh huy động tiền gửi ký quỹ được hưởng cấu phần hỗ trợ huy động ($Margin$) phân bổ từ kế hoạch kinh doanh theo [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]] (vab_ftp_methodology, Điều 6.1.d.ii, d.698). Cơ chế này kết hợp tính kỷ luật của đường cong hai vế tại [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] với yêu cầu khuyến khích mạng lưới chi nhánh thu hút các tài khoản phong tỏa pháp lý có tính bám dính cao.
