---
title: standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa
type: concept
tags: [banking, credit-risk, rwa, standardized-approach, basel-iii, regulation]
sources: [sbv_circular_14_2025]
status: draft
last_updated: 2026-09-26
---

Phương pháp tiêu chuẩn (Standardized Approach — SA) theo Thông tư 14/2025/TT-NHNN quy định quy tắc định lượng tổng tài sản có rủi ro tín dụng để tính [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]] đối với ngân hàng thương mại và chi nhánh ngân hàng nước ngoài (sbv_circular_14_2025, file TT14_1.md, Điều 8, d.276–322). Tổng tài sản có rủi ro tín dụng bao gồm hai cấu phần độc lập:

$$RWA = RWA_{CR} + RWA_{CCR}$$

Trong đó $RWA_{CR}$ là tổng tài sản có rủi ro tín dụng khách hàng và $RWA_{CCR}$ là tổng tài sản có rủi ro tín dụng đối tác phát sinh từ các giao dịch sản phẩm phái sinh đo lường theo [[counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure]], các giao dịch mua bán có kỳ hạn (repo và reverse repo) cùng thỏa thuận bù trừ ròng theo [[securities-financing-transactions-and-bilateral-netting-govern-counterparty-exposures]] theo hướng dẫn tại Phụ lục II (sbv_circular_14_2025, file TT14_1.md, Điều 8.1–8.4, d.278–321; file TT14_2.md, Phụ lục II, d.740–850). Các giao dịch đã tính rủi ro tín dụng đối tác được loại trừ khỏi danh mục tính rủi ro tín dụng khách hàng nhằm triệt tiêu nguy cơ tính trùng vốn yêu cầu.

Giá trị phơi nhiễm của một khoản phải đòi $E_i$ được ngân hàng đo lường bằng cách gộp số dư nợ gốc, lãi và phí phải thu nội bảng với giá trị quy đổi của cam kết ngoại bảng (sbv_circular_14_2025, file TT14_1.md, Điều 8.3, d.299–309):

$$E_i = E_{on, i} + E_{off, i} \times CCF_i$$

Mức độ rủi ro của phần ngoại bảng $E_{off, i}$ được kiểm soát thông qua [[regulatory-credit-conversion-factors-apportion-off-balance-sheet-contingent-liabilities]] theo từng bậc cam kết. Sau khi áp dụng các kỹ thuật [[credit-risk-mitigation-framework-recognizes-collateral-netting-guarantees-and-derivatives]], giá trị phơi nhiễm được điều chỉnh giảm còn $E_i^*$. Tổng tài sản có rủi ro tín dụng khách hàng sau đó được tính bằng cách khấu trừ dự phòng cụ thể $SP_i$ và nhân với hệ số rủi ro tín dụng tương ứng (sbv_circular_14_2025, file TT14_1.md, Điều 8.2, d.285–298):

$$RWA_{CR} = \sum_j E_j \times CRW_j + \sum_i (E_i^* - SP_i) \times CRW_i$$

Hệ số rủi ro tín dụng ($CRW$) được phân tầng chi tiết theo từng nhóm tài sản tại Điều 11–24, trong đó nổi bật là cơ chế [[loan-to-value-and-specialised-lending-criteria-differentiate-real-estate-risk-weights]] định giá hệ số rủi ro dựa trên tỷ số bảo đảm LTV và bản chất dòng tiền của từng dự án tài trợ. Ngoài vai trò xác định tỷ lệ an toàn vốn trực tiếp cho các ngân hàng thông thường, kết quả tính toán $RWA_{CR(SA)}$ còn đóng vai trò là mốc đối chuẩn sàn bắt buộc (Benchmark Floor) trong [[basel-output-floor-and-coverage-ratios-constrain-irb-capital-reductions]] để khống chế giới hạn giảm vốn của các mô hình xếp hạng nội bộ (sbv_circular_14_2025, file TT14_1.md, Điều 35, d.891–895).
