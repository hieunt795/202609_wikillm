---
title: collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties
type: concept
tags: [repo-market, rehypothecation, systemic-risk, settlement-risk]
sources: [fixed_income_during, basel_lcr]
status: stable
last_updated: 2026-09-23
related: [customer-short-positions-are-treated-as-secured-funding-because-the-customer-controls-them, downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade]
---

Tái thế chấp tài sản bảo đảm (rehypothecation) là việc bên nhận chứng khoán trong giao dịch repo tiếp tục sử dụng chính tài sản đó để thế chấp cho một giao dịch repo khác cho đến thời hạn phải hoàn trả, tạo nên các chuỗi giao dịch chuyển tiếp đa tầng trong hệ thống thanh khoản bán buôn (fixed_income_during, Ch.14, Rehypothecation, d.60).

Khi tất cả các giao dịch trong chuỗi đều thanh toán và đáo hạn đúng hạn, việc tái thế chấp giúp tối ưu hóa hiệu quả sử dụng vốn của các đại lý (fixed_income_during, Ch.14, Rehypothecation, d.60). Tuy nhiên, nếu một định chế trung gian trong chuỗi gặp sự cố vận hành hoặc mất khả năng thanh toán, nguy cơ chậm trễ chuyển giao chứng khoán sẽ lập tức lan truyền dây chuyền (cascading settlement delays) ngược trở lại các chủ sở hữu tài sản ban đầu (fixed_income_during, Ch.14, Rehypothecation, d.62). Các chủ thể cung ứng tài sản gốc thường hoàn toàn không nắm bắt được danh tính hay mức độ rủi ro tài chính của các bên trung gian nằm sâu trong chuỗi giao dịch (fixed_income_during, Ch.14, Rehypothecation, d.62).

Tình trạng hòa lẫn tài sản bảo đảm từ nhiều nguồn khác nhau tại các nút giao dịch trung gian khiến việc phân định quyền đòi nợ tài sản trở nên phức tạp khi xảy ra tranh chấp pháp lý (fixed_income_during, Ch.14, Rehypothecation, d.62). Cơ chế lây lan này khuếch đại tình trạng chậm trễ thanh toán tương tự như [[securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins|rủi ro thất bại giao nhận chứng khoán]]. Nhằm hạn chế rủi ro ách tắc chuỗi tái thế chấp, các định chế tài chính gia tăng sử dụng mô hình [[tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers|repo ba bên]] kết hợp với việc kiểm soát chặt chẽ [[repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk|tỷ lệ khấu trừ tài sản bảo đảm]]. LCR tính tới tái thế chấp ở hai chỗ: vị thế bán khống của khách hàng, ở trang [[customer-short-positions-are-treated-as-secured-funding-because-the-customer-controls-them]] (basel_lcr, LCR40, Secured funding run-off, 40.46 chú thích, d.923), và điều khoản hạ xếp hạng, ở trang [[downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade]] (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.51, d.973).
