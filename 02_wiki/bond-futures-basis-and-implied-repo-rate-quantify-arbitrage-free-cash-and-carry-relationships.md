---
title: "Bond Futures Basis and Implied Repo Rate Quantify Arbitrage-Free Cash-and-Carry Relationships"
type: concept
tags:
  - derivatives
  - bond-futures
  - gross-basis
  - net-basis
  - implied-repo-rate
  - cash-and-carry-arbitrage
  - cheapest-to-deliver
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Mối quan hệ định giá phi trọng tài giữa trái phiếu chính phủ giao ngay và hợp đồng tương lai được lượng hóa thông qua bộ ba thước đo cơ bản: Chênh lệch giá gộp (Gross Basis), Chênh lệch giá thuần (Net Basis), và Lãi suất mua lại ngụ ý (Implied Repo Rate - IRR) (fixed_income_during, Ch.28, Sec.28.3.2–28.3.4, d.221–250). Chênh lệch giá gộp biểu thị sự khác biệt trực tiếp giữa giá giao ngay (spot clean price) của trái phiếu và giá hợp đồng tương lai đã nhân với hệ số chuyển đổi tương ứng [[conversion-factors-induce-duration-dependent-cheapest-to-deliver-biases-around-notional-coupons]]:

$$\text{Gross Basis} = \text{Spot Price} - (\text{Futures Price} \times \text{CF})$$

Vị thế kinh doanh mua chênh lệch giá (long basis trade) bao gồm việc mua trái phiếu giao ngay và bán khống hợp đồng tương lai. Lợi nhuận của vị thế này phụ thuộc vào chi phí nắm giữ (carry) bao gồm tiền lãi coupon nhận được trừ đi chi phí tài trợ repo để duy trì danh mục cho đến ngày chuyển giao hợp đồng tương lai [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]]. Chênh lệch giá thuần (Net Basis), hay còn gọi là chênh lệch giá có tính chi phí nắm giữ (basis at carry), loại trừ ảnh hưởng của chi phí tài trợ và tiền lãi coupon bằng cách so sánh giá kỳ hạn lý thuyết (forward price) của trái phiếu với giá hợp đồng tương lai quy đổi (fixed_income_during, Ch.28, Sec.28.3.2, d.235–252):

$$\text{Net Basis} = \text{Forward Price} - (\text{Futures Price} \times \text{CF}) = \text{Gross Basis} - \text{Carry}$$

Lãi suất mua lại ngụ ý (Implied Repo Rate - IRR) là mức lãi suất tài trợ repo hòa vốn lý thuyết làm cho Net Basis của một trái phiếu chính xác bằng không (fixed_income_during, Ch.28, Sec.28.3.3, d.253–268). Một nhà giao dịch kinh doanh chênh lệch giá tiền mặt - kỳ hạn (cash-and-carry arbitrage) sẽ mua trái phiếu giao ngay, tài trợ việc mua bằng hợp đồng repo kỳ hạn đến ngày giao nhận, đồng thời bán khống hợp đồng tương lai tương ứng. Nếu nhà giao dịch có thể vay vốn trên thị trường repo thực tế với mức lãi suất thấp hơn IRR của trái phiếu, giao dịch cash-and-carry sẽ khóa chặt mức lợi nhuận phi rủi ro danh nghĩa. Do đó, trong một thị trường repo đồng nhất không có hiện tượng định giá đặc thù (specials), trái phiếu mang lại IRR cao nhất cho người bán chính là trái phiếu rẻ nhất để giao nộp (Cheapest-to-Deliver - CTD) vì nó tối đa hóa tỷ suất sinh lời từ giao dịch bán giao nhận (fixed_income_during, Ch.28, Sec.28.3.3, d.260–272).

Tuy nhiên, tại thị trường trái phiếu chính phủ châu Âu (Eurex Bund/Bobl), quy tắc chọn CTD dựa trên IRR cao nhất có thể bị sai lệch do sự phân mảnh lãi suất repo của từng mã trái phiếu riêng lẻ [[on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures]]. Một trái phiếu có IRR cao nhưng lãi suất repo trên thị trường thực tế lại giao dịch ở mức lãi suất đặc thù (repo specials) rất thấp sẽ khiến chi phí tài trợ thực tế chênh lệch so với mặt bằng chung, buộc các nhà kinh doanh chênh lệch giá phải tính toán Net Basis thực tế dựa trên đường cong repo đặc thù của từng tài sản (fixed_income_during, Ch.28, Sec.28.3.3, d.265–275). Trong điều kiện bình thường, Net Basis lý thuyết của trái phiếu CTD luôn là một số dương phản ánh chi phí của quyền chọn giao nộp hoán đổi chất lượng [[quality-delivery-options-embed-negative-convexity-and-convexity-drag-in-bond-futures]]. Nếu Net Basis của CTD giảm xuống dưới 0, điều này báo hiệu sự suy giảm nghiêm trọng của cơ chế trọng tài hoặc sự xuất hiện của hiện tượng ép giá hợp đồng tương lai [[futures-squeezes-and-repo-scarcity-invert-net-basis-into-negative-territory]].

Trong hoạt động quản trị rủi ro lãi suất, các nhà giao dịch sử dụng bảng phân tích cơ sở (basis sheet) để xác định giá trị biến động giá theo một điểm cơ bản (Price Value of a Basis Point - PVBP hay DV01) của hợp đồng tương lai (fixed_income_during, Ch.28, Sec.28.3.4, d.270–279). Khi trạng thái CTD đã được xác lập rõ ràng và xác suất chuyển đổi CTD là không đáng kể, độ nhạy cảm rủi ro lãi suất của hợp đồng tương lai được xấp xỉ bằng độ nhạy cảm rủi ro của chính trái phiếu CTD chia cho hệ số chuyển đổi của nó:

$$\text{PVBP}_{\text{Future}} \approx \frac{\text{PVBP}_{\text{CTD}}}{\text{CF}_{\text{CTD}}}$$

Công thức này chứng minh rằng tỷ lệ phòng hộ (hedge ratio) đối với một danh mục trái phiếu CTD bằng chính hệ số chuyển đổi của nó, cho phép các định chế tài chính xác định chính xác số lượng hợp đồng tương lai cần bán để vô hiệu hóa rủi ro thời lượng của danh mục trái phiếu cơ sở (fixed_income_during, Ch.28, Sec.28.3.4, d.275–279). Khi áp dụng vào các chiến lược giá trị tương đối nâng cao, nếu kỳ hạn của trái phiếu lệch đáng kể so với CTD, các nhà giao dịch mở rộng sang kỹ thuật kẹp hai hợp đồng tương lai đa kỳ hạn tại [[bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging]].
