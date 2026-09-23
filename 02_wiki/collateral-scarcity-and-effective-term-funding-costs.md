---
title: collateral-scarcity-and-effective-term-funding-costs
type: concept
tags: [monetary, central-banking, collateral-framework, liquidity-risk, monetary-transmission]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-21
---

Sự khan hiếm tài sản bảo đảm và chi phí tài trợ kỳ hạn hiệu dụng (collateral scarcity and effective term funding costs) được Bindseil (2014, Ch.12, §12.1, d.2462–2642) mô hình hóa nhằm giải thích tại sao trong khủng hoảng tài chính, các điều kiện tiền tệ thực tế có thể bị thắt chặt nghiêm trọng ngay cả khi ngân hàng trung ương duy trì lãi suất điều hành không đổi.

**Cơ chế truyền dẫn từ đệm tài sản bảo đảm tới lãi suất cho vay thực tế**: Trong thời bình, ngân hàng thương mại luôn có đủ tài sản bảo đảm chất lượng cao để tiếp cận tín dụng NHTW với xác suất bằng 1, khiến chi phí tài trợ kỳ hạn 1 năm của ngân hàng bám sát lãi suất chính sách $i^*$. Khi quyết định cấp tín dụng cho nền kinh tế thực (doanh nghiệp, hộ gia đình), ngân hàng tính toán dựa trên chi phí tài trợ kỳ hạn kỳ vọng nhìn về phía trước (forward-looking expected term funding costs). Trong khủng hoảng, rủi ro cạn kiệt tài sản bảo đảm (collateral gap $CG > 0$) xuất hiện do hai lực đẩy đồng thời: (i) giá trị tài sản bảo đảm sau chiết khấu (CVPH - Collateral Value Post Haircut) sụt giảm mạnh vì tài sản bị hạ bậc xếp hạng tín nhiệm, giá thị trường lao dốc và NHTW chủ động nâng haircut phòng thủ; (ii) dòng tiền gửi bị rút đột ngột ($k$ biến động mạnh với độ lệch chuẩn $\sigma_k$ tăng vọt), đẩy nhu cầu vay mượn từ NHTW tăng cao vượt quá trần thế chấp khả dụng (bindseil_monetary_policy, Ch.12, §12.1, d.2488–2585).

**Mô hình chi phí tài trợ kỳ hạn 1 năm với ba trạng thái**: Giả định ngân hàng đối mặt với cú sốc rút tiền gửi $k \sim \mathcal{N}(0, \sigma_k^2)$ và biến động haircut $h = h_0 + \theta$ với $\theta \sim \mathcal{N}(0, \sigma_h^2)$. Chi phí tài trợ thực tế kỳ vọng $i^\#$ của ngân hàng là giá trị bình quân gia quyền của ba kịch bản (công thức 12.3 của Bindseil):
$$i^\# = P(CG > 0) \cdot i_{ELA} + P(\text{normal}) \cdot i^* + P(\text{excess}) \cdot i_D$$
Trong đó:
- $P(CG > 0)$ là xác suất ngân hàng cạn kiệt tài sản bảo đảm và phải tiếp cận hỗ trợ thanh khoản khẩn cấp (Emergency Liquidity Assistance - ELA) với chi phí trừng phạt $i_{ELA} > i^*$ (hoặc đối mặt với nguy cơ phá sản).
- $P(\text{normal}) = 1 - P(CG > 0) - P(\text{excess})$ là trạng thái bình thường khi ngân hàng vay đủ từ NHTW theo lãi suất chính sách $i^*$.
- $P(\text{excess})$ là xác suất dòng tiền gửi thặng dư chảy vào khiến ngân hàng rơi vào trạng thái thừa thanh khoản và phải gửi tại tiện ích tiền gửi với lãi suất sàn $i_D$.

**Phân tích 11 kịch bản can thiệp chính sách (Bảng 12.1)**: Mô phỏng số của Bindseil chỉ ra rằng:
- Khi bất định tăng lên ($\sigma_k$ tăng từ 1 lên 4 và $\sigma_h$ tăng từ 0.01 lên 0.2, Kịch bản II), xác suất chạm ngưỡng ELA $P(CG > 0)$ tăng vọt lên 24%, kéo chi phí tài trợ hiệu dụng $i^\#$ từ 4.00% vọt lên **5.43%**, gây hiệu ứng thắt chặt tiền tệ ngoài ý muốn.
- *Phản ứng bằng chính sách thông thường (Kịch bản III)*: NHTW có thể trung hòa cú sốc này bằng cách hạ lãi suất chính sách $i^*$ từ 4% xuống 2.12% và hạ $i_D$ về 0%, khôi phục $i^\#$ về đúng 4.00%. Tuy nhiên, phản ứng này đòi hỏi NHTW chưa chạm [[monetary-policy-transmission-breakdown-and-zero-lower-bound|giới hạn lãi suất zero (ZLB)]].
- *Phản ứng qua công cụ phi quy ước khi chạm ZLB (Kịch bản VIII–XI)*: Khi $\sigma_k$ tăng lên 6 và $i^\#$ vọt lên 5.64%, chính sách lãi suất đơn lẻ bị bất lực. NHTW phải kết hợp hạ lãi suất với:
  1. *Thu hẹp hành lang lãi suất (Kịch bản IX)*: Giảm độ rộng hành lang từ 200 bps xuống 166 bps.
  2. *Mua đứt chứng khoán (Outright purchases, Kịch bản X)*: Mua 2.5 đơn vị trái phiếu doanh nghiệp, bơm thanh khoản trực tiếp và giải phóng phụ thuộc vào tín dụng NHTW.
  3. *Nới lỏng khung tài sản bảo đảm (Kịch bản XI)*: Chủ động giảm haircut cơ sở $h_0$ từ 30% xuống 27%, mở rộng đệm CVPH cho hệ thống ngân hàng (bindseil_monetary_policy, Ch.12, §12.1, d.2608–2642).

**Ý nghĩa đối với chính sách tiền tệ trong khủng hoảng**: Khi ZLB bị chạm, việc nới lỏng [[central-bank-collateral-framework-design-and-risk-control|khung tài sản bảo đảm]] không còn đơn thuần là quyết định quản trị rủi ro vi mô, mà trở thành một công cụ chính sách tiền tệ vĩ mô thay thế kênh lãi suất để ngăn chặn vòng xoáy [[deflation|giảm phát]] và phá vỡ [[mechanics-of-liquidity-crises-and-feedback-loops|vòng xoáy thắt chặt tín dụng]].
