---
title: collateral-constraint-on-central-bank-credit
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, collateral, liquidity]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-21
---

Khả năng vay của ngân hàng từ ngân hàng trung ương bị giới hạn bởi lượng và chất của tài sản thế chấp đủ điều kiện (eligible collateral). Giới hạn này phát sinh từ bốn nguồn: (i) điều kiện eligible hạn chế (loại trừ tài sản kém thanh khoản, thiếu minh bạch, hoặc dưới mức chất lượng tín dụng tối thiểu); (ii) định giá bảo thủ (để tránh định giá quá cao); (iii) haircut — NHTW chỉ cho vay một tỷ lệ nhỏ hơn 100% giá trị tài sản để bù rủi ro giá trị giảm trong thời gian thanh lý; (iv) giới hạn định lượng để kiểm soát rủi ro tập trung (bindseil_monetary_policy, Ch.2, §2.3, d.547).

Với véc-tơ tỷ lệ chiết khấu $H = \{h_1, h_2, \dots, h_n\}$, tổng hạn mức vay tái cấp vốn tối đa của ngân hàng là giá trị tài sản thế chấp sau chiết khấu (Collateral Value Post-Haircut — $CVPH$): $CVPH = \sum a_i (1 - h_i)$. Dư nợ vay NHTW không thể vượt quá $CVPH$, tức $\sum a_i - D + RR \le CVPH$. Trên mô hình liên tục với tài sản xếp hạng theo độ rủi ro $x \in [0, 1]$, hàm haircut luỹ thừa $h(x) = x^\delta$ cho thấy giá trị $CVPH = \delta / (\delta + 1)$. Tại Eurosystem, với tổng tài sản ngân hàng khoảng 32 nghìn tỷ EUR và $CVPH$ khoảng 5 nghìn tỷ EUR, tham số $\delta \approx 0.2$ (tỷ lệ chiết khấu bình quân lên tới 84% tổng tài sản ngân hàng), nghĩa là chỉ khoảng 16% tài sản ngân hàng có thể chuyển đổi thành thanh khoản NHTW (bindseil_monetary_policy, Ch.9, §9.1, d.1605–1620).

Sự khan hiếm tài sản thế chấp là điều tất yếu trong hệ thống tài chính bởi hai lý do: (i) NHTW không thể cho vay không tài sản bảo đảm (unsecured lending) do không thể quản trị rủi ro tín dụng từng ngân hàng dưới mức lãi suất chính sách đồng nhất; (ii) ngay cả khi có công nghệ định giá hoàn hảo, tính bất đối xứng lãi/lỗ khi thanh lý tài sản đối tác vỡ nợ (phần thặng dư phải trả lại cho người quản lý tài sản, phần thâm hụt NHTW tự gánh chịu) buộc NHTW luôn phải duy trì haircut (d.1631–1635).

Ràng buộc collateral giới hạn [[relative-vs-absolute-central-bank-intermediation|trung gian tương đối]]: khi ngân hàng thiếu thanh khoản đã cạn kiệt tài sản thế chấp đủ điều kiện, thị trường liên ngân hàng không còn có thể được bù trừ qua bảng cân đối NHTW. Các khía cạnh chuyên sâu của khuôn khổ tài sản bảo đảm bao gồm:
- Quy trình thiết kế 5 bước và các kỹ thuật quản trị rủi ro (hạn mức, định giá hàng ngày, hiệu chuẩn haircut theo biến động giá): [[central-bank-collateral-framework-design-and-risk-control]].
- Tác động lên định giá tài sản thị trường, phí quyền và vai trò haircut như ràng buộc đòn bẩy vĩ mô: [[market-impact-of-collateral-framework-and-leverage-constraints]].
- Hiện tượng lựa chọn đối nghịch kép (Double Gresham's Law) và chiến lược phân tách rổ tài sản: [[collateral-pool-segregation-and-double-adverse-selection]].
- Tác động thắt chặt điều kiện tiền tệ và gia tăng chi phí tài trợ kỳ hạn hiệu dụng khi xuất hiện rủi ro cạn kiệt collateral: [[collateral-scarcity-and-effective-term-funding-costs]].
- Hệ quả thứ cấp hóa chủ nợ không bảo đảm và đẩy vọt tỷ lệ tổn thất khi vỡ nợ (LGD) do phong tỏa tài sản: [[asset-encumbrance-and-subordination-of-unsecured-creditors]].
- Giải pháp hoán đổi collateral thanh khoản mà không làm phình to bảng cân đối NHTW: [[securities-lending-programmes-and-central-bank-collateral-swaps]].
