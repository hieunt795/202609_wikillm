---
title: market-impact-of-collateral-framework-and-leverage-constraints
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, collateral, interest-rates, asset-pricing]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-21
---

Quy định về tài sản bảo đảm và tỷ lệ chiết khấu (haircuts) của ngân hàng trung ương có tác động lan toả mạnh mẽ lên định giá tài sản tài chính và chi phí vốn của nền kinh tế thực, biến khuôn khổ tài sản bảo đảm thành một công cụ chính sách tiền tệ thực chất (bindseil_monetary_policy, Ch.9, §9.4, d.1713–1814).

**Phí quyền hội đủ điều kiện (Eligibility premium) và vấn đề méo mó giá**: Tài sản được NHTW chấp nhận làm tài sản thế chấp luôn được giao dịch ở mức định giá cao hơn (lợi suất thấp hơn), phản ánh giá trị của quyền chọn có thể đổi thành thanh khoản NHTW bất kỳ lúc nào. Khi NHTW mở rộng danh mục chấp nhận, phí quyền của các tài sản đã đủ điều kiện trước đó giảm xuống (do tính khan hiếm giảm), trong khi giá tài sản mới được thêm vào tăng lên (d.1715). Tác động này không phải là méo mó thị trường (distortion) nếu NHTW áp dụng đúng nguyên tắc tương đương rủi ro và thu phí thẩm định; trái lại, việc chỉ chấp nhận trái phiếu chính phủ sẽ tạo ra đặc quyền quá mức và bị xem là một dạng kìm hãm tài chính (financial repression) nhằm ép các định chế tài chính tài trợ nợ công (d.1719–1720).

**Haircut như ràng buộc đòn bẩy hiệu lực — Mô hình Ashcraft, Garleanu & Pedersen (2011)**: Khi tài sản thế chấp bị ràng buộc, tỷ lệ chiết khấu $h(x)$ quy định giới hạn đòn bẩy tối đa mà ngân hàng có thể sử dụng để tài trợ cho tài sản $x \in [0, 1]$. Chi phí vốn hiệu lực $i(x)$ để tài trợ tài sản $x$ là bình quân gia quyền giữa chi phí vốn chủ sở hữu ngầm định ($i_e$) và lãi suất tái cấp vốn của NHTW ($i^*$):
$$i(x) = h(x) i_e + (1 - h(x)) i^*$$

Nếu hàm haircut có dạng hàm luỹ thừa $h(x) = x^\delta$, chi phí vốn bình quân của toàn nền kinh tế là:
$$i^\# = \frac{1}{\delta + 1} i_e + \frac{\delta}{\delta + 1} i^*$$

Mô hình này chứng minh điều kiện tiền tệ hiệu lực phụ thuộc đồng thời vào lãi suất chính sách $i^*$ và tham số haircut $\delta$. NHTW có thể đạt cùng một mức chi phí vốn vĩ mô (ví dụ 3%) bằng nhiều cặp tham số $(i^*, \delta)$ khác nhau (chẳng hạn lãi suất thấp kết hợp haircut chặt, hoặc lãi suất cao kết hợp haircut nới lỏng). Tuy nhiên, các lựa chọn này có tác động phân bổ rất khác nhau: chính sách haircut lỏng có lợi hơn cho các dự án và tài sản kém thanh khoản (d.1725–1735).

**Mô hình định giá chênh lệch lợi suất dựa trên xác suất cạn kiệt tài sản thế chấp**: Trong thực tế, các ngân hàng chỉ tái cấp vốn một phần nhỏ tài sản qua NHTW. Bindseil (2014, d.1763–1804) phát triển mô hình vi mô đo lường khoảng trống tài sản thế chấp (collateral gap — $CG$):
$$CG = \max(0, \text{nhu cầu tài trợ NHTW} - CVPH)$$

Khi ngân hàng đối mặt với các cú sốc rút tiền gửi $k$, kỳ vọng chi phí cạn kiệt tài sản thế chấp $Q = \int q(CG) f(k) dk$ (bao gồm chi phí vay khẩn cấp, bán tháo tài sản, hoặc vỡ nợ) sẽ tạo ra mức chênh lệch lợi suất (spread $s$) giữa tài sản có haircut thấp (như trái phiếu chính phủ) và tài sản có haircut cao (như trái phiếu doanh nghiệp):
$$\Delta s \le \Delta E(q(CG))$$

Chênh lệch lợi suất này càng lớn khi: (i) khoảng cách haircut $h_B - h_A$ càng rộng; (ii) độ biến động của các cú sốc thanh khoản $\sigma_k^2$ càng cao; và (iii) mức độ phụ thuộc cấu trúc của hệ thống ngân hàng vào thanh khoản NHTW càng lớn (d.1797). Các nghiên cứu gần đây (Koulischer & Struyven 2013; Bindseil 2013; Majnoni d'Intignano 2013) đều xác nhận việc nới lỏng chính sách tài sản bảo đảm của NHTW là biện pháp hữu hiệu giúp hạ nhiệt lãi suất thị trường và phá vỡ tình trạng đóng băng tín dụng, đặc biệt khi chính sách lãi suất bị chặn bởi [[one-directional-standing-facility-monetary-policy|lãi suất sàn danh nghĩa (ZLB)]].

Xem thêm: [[central-bank-collateral-framework-design-and-risk-control]], [[collateral-constraint-on-central-bank-credit]], [[collateral-pool-segregation-and-double-adverse-selection]], [[standing-facilities-in-monetary-policy-operations]].
