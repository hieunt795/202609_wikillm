---
title: delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles
type: concept
tags: [settlement, payment-systems, clearing, counterparty-risk]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Cơ chế chuyển giao đồng thời với thanh toán (Delivery versus Payment - DvP) loại bỏ hoàn toàn rủi ro Herstatt (rủi ro thanh toán) bằng cách ràng buộc việc chuyển giao quyền sở hữu chứng khoán chỉ có hiệu lực pháp lý khi luồng tiền thanh toán tương ứng được chuyển giao đồng thời (fixed_income_during, Ch.11, Settlement Mechanisms, d.258–260). Rủi ro Herstatt phát sinh trong phương thức thanh toán độc lập truyền thống, khi một bên hoàn tất việc bàn giao tài sản nhưng đối tác mất khả năng thanh toán trước khi chuyển giao phần đối ứng, khiến bên thực hiện nghĩa vụ trước trở thành chủ nợ không có bảo đảm (fixed_income_during, Ch.11, Settlement Mechanisms, d.258).

Để triệt tiêu rủi ro tín dụng đối tác, các định chế trung gian ủy thác đáng tin cậy (như ngân hàng CLS trong giao dịch ngoại hối hoặc các tổ chức CSD quốc tế trong thị trường trái phiếu) đóng vai trò tài khoản ký quỹ trung gian, chỉ giải tỏa và hạch toán tài sản khi cả hai bên đã nộp đủ tiền và chứng khoán vào tài khoản giám sát (fixed_income_during, Ch.11, Settlement Mechanisms, d.260). Nhằm giảm thiểu chi phí vốn phát sinh từ việc phải lưu trữ tài sản nhàn rỗi tại tổ chức trung gian, quy trình DvP trên thị trường trái phiếu được vận hành theo các chu kỳ thanh toán bù trừ định kỳ (settlement cycles) vào các khung giờ cố định trong ngày giao dịch (fixed_income_during, Ch.11, Settlement Mechanisms, d.262). Tại mỗi chu kỳ, hệ thống trung gian khớp lệnh và đối trừ toàn bộ các giao dịch đang chờ xử lý, tạo ra lợi ích bù trừ ròng đáng kể về mặt thanh khoản tương tự như [[multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures|nguyên lý bù trừ đa phương liên ngân hàng]] (fixed_income_during, Ch.11, Settlement Mechanisms, d.262).

Quy ước thanh toán cuốn chiếu T+2 chuẩn hóa chu kỳ luân chuyển vốn, cân bằng giữa yêu cầu rút ngắn thời gian chịu rủi ro tín dụng và thời gian cần thiết để các bên đối chiếu sai sót tác nghiệp (fixed_income_during, Ch.11, Settlement Conventions, d.272–274). Hạ tầng DvP vận hành đồng bộ với mạng lưới [[book-entry-securities-centralize-ownership-via-global-notes-and-csds|lưu ký chứng khoán ghi sổ tập trung]], làm cơ sở kỹ thuật để các định chế tài chính kết nối vào các hệ thống quản trị rủi ro của [[central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk|đối tác bù trừ trung tâm (CCP)]].
