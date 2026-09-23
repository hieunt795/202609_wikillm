---
title: ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding
type: concept
tags: [ccp, clearing, risk-management, margin-requirements]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Thác bảo vệ của đối tác bù trừ trung tâm (CCP protection waterfall) là chuỗi các tầng phòng vệ tài chính và nghĩa vụ pháp lý được thiết lập theo thứ tự ưu tiên nhằm bảo vệ CCP khỏi nguy cơ mất khả năng thanh toán khi có thành viên bù trừ vỡ nợ (fixed_income_during, Ch.12, Direct Clearing, d.48). Tầng bảo vệ đầu tiên là ký quỹ biến đổi (Variation Margin - VM) bắt buộc thanh toán bằng tiền mặt hàng ngày, xóa sạch mọi khoản lãi lỗ chưa thực hiện và đưa trạng thái rủi ro mở của vị thế về mức 0 (fixed_income_during, Ch.12, Direct Clearing, d.34, d.42). Tầng thứ hai là ký quỹ ban đầu (Initial Margin - IM), được định cỡ theo công thức $\rho \sqrt{t}$ để hấp thụ các biến động giá bất lợi trong khoảng thời gian $t$ ngày cần thiết nhằm đóng vị thế của thành viên vi phạm; khoản này chấp nhận tài sản thế chấp phi tiền mặt (fixed_income_during, Ch.12, Direct Clearing, d.38–40).

Khi thành viên bù trừ vỡ nợ nội bộ do không nộp đủ tiền ký quỹ hoặc vỡ nợ pháp lý bên ngoài, tài sản ký quỹ IM của chính thành viên đó được thanh lý đầu tiên để thanh toán tiền VM cho các thành viên còn lại (fixed_income_during, Ch.12, Direct Clearing, d.52–54). Nếu nguồn ký quỹ IM bị cạn kiệt trong các phiên đấu thầu thanh lý vị thế, CCP kích hoạt tầng thứ ba là quỹ vỡ nợ tương hỗ (default fund) được đóng góp trước bởi toàn bộ các thành viên bù trừ (fixed_income_during, Ch.12, Direct Clearing, d.56). Tầng thứ tư là nghĩa vụ bỏ thầu bắt buộc (bidding obligations): CCP yêu cầu các thành viên còn sống sót phải tham gia đấu thầu tiếp nhận danh mục tài sản của bên phá sản (fixed_income_during, Ch.12, Direct Clearing, d.56). 

Nhằm hạn chế tình trạng các thành viên cố tình bỏ giá thấp để đẩy lỗ cho quỹ chung, quy chế bù trừ ràng buộc nghĩa vụ đóng góp bù đắp quỹ vỡ nợ (replenishment obligation) tỷ lệ nghịch với mức giá đấu thầu mà thành viên đưa ra (fixed_income_during, Ch.12, Direct Clearing, d.60). Cấu trúc tầng này giúp [[central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk|đối tác bù trừ trung tâm]] đứng vững trước các cú sốc phá sản lớn, nhưng đồng thời tạo ra các khoản nợ tiềm tàng phức tạp và chi phí vốn cho các định chế tài chính thành viên, làm nền tảng tính toán [[xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices|các khoản điều chỉnh định giá vốn và ký quỹ xVA]].
