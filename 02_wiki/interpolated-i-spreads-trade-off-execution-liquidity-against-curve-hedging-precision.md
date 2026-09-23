---
title: interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision
type: concept
tags: [i-spread, swap-spread, hedging, liquidity, fixed-income-derivatives]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Chênh lệch hoán đổi nội suy (I-spread) là mức chênh lệch giữa lợi suất của một trái phiếu và lãi suất hoán đổi chuẩn được nội suy tại đúng kỳ hạn của trái phiếu đó trên đường cong swap (fixed_income_during, Ch.22, I-spreads, d.76). Khác với asset swap spread được xác định ở nhánh thả nổi, I-spread được tính toán hoàn toàn ở nhánh cố định, tuân theo quy ước đếm ngày và tần suất ghép lãi cố định của thị trường swap (fixed_income_during, Ch.22, I-spreads, d.76). Khi ngày đáo hạn của trái phiếu không trùng khớp với các kỳ hạn hoán đổi chuẩn, thị trường áp dụng quy ước kỳ coupon đầu tiên ngắn cho cả hai nhánh cố định và thả nổi của hợp đồng swap nội suy (fixed_income_during, Ch.22, I-spreads, d.76).

Ưu thế của I-spread là tính thanh khoản và tốc độ thực thi cao, đặc biệt phù hợp cho các chiến lược phòng hộ rủi ro lãi suất ngắn hạn (fixed_income_during, Ch.22, I-spreads, d.78). Do các hợp đồng swap sử dụng là các swap ngang giá tại thời điểm khởi tạo, các bên giao dịch có thể định giá tức thì mà không phải đối mặt với các cam kết ràng buộc vốn trả trước trên bảng cân đối kế toán như trong par-par asset swap (fixed_income_during, Ch.22, I-spreads, d.78).

Tuy nhiên, I-spread bộc lộ sự đánh đổi cố hữu giữa tính thanh khoản thực thi và độ chính xác phòng hộ (fixed_income_during, Ch.22, I-spreads, d.78). Sự khác biệt về cấu trúc coupon và tần suất thanh toán dòng tiền giữa trái phiếu và hợp đồng swap chuẩn khiến mối quan hệ giá trị giữa hai công cụ bị lệch pha khi đường cong lợi suất có các biến động lớn (fixed_income_during, Ch.22, I-spreads, d.78). Do đó, nhà quản trị rủi ro phải cân nhắc giữa việc chấp nhận chi phí bảng cân đối để đạt độ chính xác phòng hộ cao qua [[par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks]] hay tối ưu hóa tốc độ luân chuyển danh mục qua I-spread. Cơ chế này cũng bổ trợ cho việc đánh giá vị thế tương đối trên đường cong kết hợp cùng [[par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities]]. Trong thực tiễn định giá và giao dịch giá trị tương đối, I-spread đóng vai trò thước đo chuẩn hóa cho trái phiếu doanh nghiệp và trái phiếu có bảo đảm theo [[bond-relative-value-metrics-select-reference-curves-aligned-with-instrument-hedging-practices]], đồng thời làm cơ sở xác lập các vị thế spread kết hợp phòng hộ hợp đồng tương lai theo [[bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging]].
