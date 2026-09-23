---
title: collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties
type: concept
tags: [repo-market, rehypothecation, systemic-risk, settlement-risk]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Tái thế chấp tài sản bảo đảm (rehypothecation) là việc bên nhận chứng khoán trong giao dịch repo tiếp tục sử dụng chính tài sản đó để thế chấp cho một giao dịch repo khác cho đến thời hạn phải hoàn trả, tạo nên các chuỗi giao dịch chuyển tiếp đa tầng trong hệ thống thanh khoản bán buôn (fixed_income_during, Ch.14, Rehypothecation, d.60).

Khi tất cả các giao dịch trong chuỗi đều thanh toán và đáo hạn đúng hạn, việc tái thế chấp giúp tối ưu hóa hiệu quả sử dụng vốn của các đại lý (fixed_income_during, Ch.14, Rehypothecation, d.60). Tuy nhiên, nếu một định chế trung gian trong chuỗi gặp sự cố vận hành hoặc mất khả năng thanh toán, nguy cơ chậm trễ chuyển giao chứng khoán sẽ lập tức lan truyền dây chuyền (cascading settlement delays) ngược trở lại các chủ sở hữu tài sản ban đầu (fixed_income_during, Ch.14, Rehypothecation, d.62). Các chủ thể cung ứng tài sản gốc thường hoàn toàn không nắm bắt được danh tính hay mức độ rủi ro tài chính của các bên trung gian nằm sâu trong chuỗi giao dịch (fixed_income_during, Ch.14, Rehypothecation, d.62).

Tình trạng hòa lẫn tài sản bảo đảm từ nhiều nguồn khác nhau tại các nút giao dịch trung gian khiến việc phân định quyền đòi nợ tài sản trở nên phức tạp khi xảy ra tranh chấp pháp lý (fixed_income_during, Ch.14, Rehypothecation, d.62). Cơ chế lây lan này khuếch đại tình trạng chậm trễ thanh toán tương tự như [[securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins|rủi ro thất bại giao nhận chứng khoán]]. Nhằm hạn chế rủi ro ách tắc chuỗi tái thế chấp, các định chế tài chính gia tăng sử dụng mô hình [[tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers|repo ba bên]] kết hợp với việc kiểm soát chặt chẽ [[repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk|tỷ lệ khấu trừ tài sản bảo đảm]].
