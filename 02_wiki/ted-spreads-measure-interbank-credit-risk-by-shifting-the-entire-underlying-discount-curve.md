---
title: ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve
type: concept
tags: [ted-spread, option-adjusted-spread, interbank-risk, discount-curve, eurodollar]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Chênh lệch TED lượng hóa rủi ro tín dụng và thanh khoản của hệ thống ngân hàng thương mại tư nhân so với nợ chính phủ phi rủi ro, xuất phát từ chênh lệch lịch sử giữa hợp đồng tương lai tín phiếu Kho bạc Mỹ kỳ hạn 13 tuần và hợp đồng tương lai Eurodollar 3 tháng (fixed_income_during, Ch.22, The TED spread, d.82). Về mặt cấu trúc định lượng, TED spread có sự tương đồng với chênh lệch điều chỉnh quyền chọn nhưng khác biệt căn bản so với mọi loại spread công cụ khác (fixed_income_during, Ch.22, The TED spread, d.82–84). Thay vì chỉ đo khoảng cách giữa các mức lợi suất hay cộng biên độ vào nhánh thả nổi, TED spread phản ánh biên độ dịch chuyển bắt buộc của toàn bộ đường cong chiết khấu để tái định giá một chứng khoán nhất định về mức giá thị trường (fixed_income_during, Ch.22, The TED spread, d.82–84).

Khi tín phiếu Kho bạc hủy niêm yết và khi mở rộng phân tích sang các thị trường ngoài Mỹ (nơi các hợp đồng tương lai Euribor hay Euroyen thiếu thanh khoản ở các dải kỳ hạn xa), các nhà phân tích không thể tính toán TED spread trực tiếp từ các chuỗi hợp đồng tương lai thị trường tiền tệ đơn lẻ (fixed_income_during, Ch.22, The TED spread, d.82–84). Thay vào đó, mô hình định lượng dịch chuyển trực tiếp các lãi suất kỳ hạn ngụ ý trong một mô hình thị trường, sau đó tái cấu trúc lại toàn bộ đường cong hệ số chiết khấu từ chuỗi lãi suất kỳ hạn đã điều chỉnh (fixed_income_during, Ch.22, The TED spread, d.84).

Phương pháp dịch chuyển đường cong này kết nối trực tiếp với các mô hình biểu diễn đường cong chiết khấu trong [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]], đồng thời tạo đối trọng với kỹ thuật cộng spread dòng tiền của [[z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves]] và cơ chế bóc tách rủi ro tài trợ repo trong [[bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing]]. Rủi ro tín dụng hệ thống ngân hàng hàm chứa trong mức chênh lệch TED phản ánh trực tiếp cơ chế hấp thụ tổn thất cưỡng chế theo luật định tại [[statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors]] và chịu sự chi phối của động lực dịch chuyển xếp hạng tín dụng liên ngân hàng theo [[rating-migration-matrices-resolve-the-maturity-paradox-and-reveal-corporate-versus-sovereign-risk-divergence]].
