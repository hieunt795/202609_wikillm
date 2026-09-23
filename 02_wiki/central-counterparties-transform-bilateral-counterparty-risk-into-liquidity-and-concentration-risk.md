---
title: central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk
type: concept
tags: [clearing, ccp, systemic-risk, financial-infrastructure]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Đối tác bù trừ trung tâm (Central Counterparty - CCP) thu gọn $n(n-1)/2$ mối quan hệ bù trừ song phương tiềm tàng giữa $n$ thành viên thị trường thành đúng $n$ mối quan hệ trực tiếp với một định chế trung tâm duy nhất thông qua cơ chế chuyển nhượng giao dịch (give-up) (fixed_income_during, Ch.12, Direct Clearing, d.10–14). Quá trình này giúp nâng cao hiệu quả vận hành và mở rộng khả năng đối trừ đa phương vượt bậc so với [[multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures|bù trừ song phương hoặc đa phương nội bộ ngân hàng]] (fixed_income_during, Ch.12, Direct Clearing, d.10).

Tuy nhiên, sự hiện diện của CCP không làm triệt tiêu rủi ro tín dụng đối tác của toàn thị trường, mà chuyển hóa rủi ro tín dụng song phương thành rủi ro thanh khoản của các thành viên bù trừ và rủi ro sụp đổ tập trung mang tính hệ thống (fixed_income_during, Ch.12, Direct Clearing, d.18, d.34). Để bảo đảm khả năng thanh toán, CCP yêu cầu các thành viên nộp ký quỹ biến đổi (Variation Margin - VM) bằng tiền mặt hàng ngày để tái lập giá trị rủi ro mở về 0, biến nguy cơ mất vốn dài hạn thành áp lực huy động tiền mặt khẩn cấp trong ngắn hạn (fixed_income_during, Ch.12, Direct Clearing, d.34). Rủi ro thanh khoản này được phòng vệ nhiều lớp thông qua [[ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding|thác bảo vệ rủi ro của CCP]] bao gồm ký quỹ ban đầu và quỹ vỡ nợ tương hỗ.

Cấu trúc bù trừ gián tiếp làm lộ rõ sự đánh đổi thông tin và phân bổ rủi ro thanh khoản (fixed_income_during, Ch.12, Indirect Clearing, d.70–100). Trong mô hình bù trừ đại lý (agency clearing) thống trị tại Mỹ, CCP ký hợp đồng trực tiếp với khách hàng cuối và nắm rõ vị thế của bên thụ hưởng tối hậu, hỗ trợ kiểm tra sức chịu đựng (stress test) chính xác (fixed_income_during, Ch.12, Indirect Clearing, d.76–80). Ngược lại, mô hình bù trừ tự doanh (principal clearing) phổ biến tại châu Âu và Nhật Bản đặt thành viên bù trừ đứng giữa làm đối tác duy nhất, khiến CCP không nhận diện được mức độ tập trung rủi ro của một khách hàng lớn chia lệnh qua nhiều đại lý khác nhau (fixed_income_during, Ch.12, Indirect Clearing, d.86–90). Các chi phí phát sinh từ việc tuân thủ ký quỹ tại CCP trở thành căn cứ tham chiếu cho [[xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices|các khoản điều chỉnh định giá xVA]].
