---
title: embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap
type: concept
tags: [alm, irrbb, embedded-options, behavioral-modeling, eba-guidelines, model-risk]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]
drives: [economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows]
related: [non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles, replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches, contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]
---

ALM cần xét cả hai loại quyền chọn lãi suất: quyền chọn tự động (*automatic options*) và quyền chọn hành vi (*behavioral options*), còn gọi là quyền chọn gắn trong sản phẩm (*embedded options*) (tata_bank_alm, Ch.2, Embedded Options, d.1821). Quyền chọn tự động được thực hiện theo quy tắc, như trần lãi suất (cap), sàn lãi suất (floor) và swaption (tata_bank_alm, Ch.2, Embedded Options, d.1821). Quyền chọn hành vi cho khách hàng quyền tự quyết về dòng tiền: đóng một tài khoản hoặc chấm dứt quan hệ với ngân hàng, rút tiền khỏi tài khoản tiền gửi thanh toán (*deposit redemption option*), trả khoản vay thế chấp sớm hơn kế hoạch (*prepayment option*), dùng thấu chi, và cả nộp đơn phá sản (*default option*) (tata_bank_alm, Ch.2, Embedded Options, d.1823).

Quyền chọn hành vi có thể tồn tại cả ở sản phẩm có kỳ hạn hợp đồng, như khoản vay lãi suất thả nổi và khoản vay thế chấp tiêu dùng (tata_bank_alm, Ch.2, Embedded Options, d.1825). Chúng có thể rút ngắn kỳ hạn kỳ vọng so với hợp đồng, nên tác động đáng kể tới thước đo [[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows|giá trị kinh tế của vốn chủ sở hữu (EVE)]] và thu nhập lãi thuần (NII) (tata_bank_alm, Ch.2, Embedded Options, d.1827); đây là phần hành vi của [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options|rủi ro quyền chọn]]. Để dự báo dòng tiền của một giao dịch khách hàng, ngân hàng cần mô hình hóa hành vi khách hàng (tata_bank_alm, Ch.2, Embedded Options, d.1831). Giả định đơn giản là một tỷ lệ cố định $p$ khách hàng trả trước khoản vay, rút từ quan sát thực nghiệm; mô hình sát thực tế hơn cho $p$ là hàm của môi trường lãi suất tại ngày trả trước, và khi đó dòng tiền của khoản vay thay đổi theo mức lãi suất (tata_bank_alm, Ch.2, Embedded Options, d.1831).

Lý thuyết định giá quyền chọn chuẩn giả định quyền chọn tự động được thực hiện một cách duy lý: người giữ không thực hiện một quyền chọn mua đang out-of-the-money, vì giá phải trả cho tài sản cơ sở khi đó cao hơn giá thị trường (tata_bank_alm, Ch.2, Embedded Options, d.1843). Quyền chọn hành vi có thể không được thực hiện tối ưu, một phần do yếu tố nhân khẩu như qua đời, ly hôn hoặc đổi việc (tata_bank_alm, Ch.2, Embedded Options, d.1843). Ví dụ của nguồn: một khoản vay thế chấp được trả trước dù lãi suất hợp đồng thấp hơn nhiều so với lãi suất thị trường, vì người vay ly hôn và phải bán nhà; ngân hàng được lợi từ việc quyền chọn được thực hiện dù đang ở vị thế bán quyền chọn (tata_bank_alm, Ch.2, Embedded Options, d.1843).

Mô hình chỉ tốt bằng giả định của nó: giả định sai có thể làm kết quả lệch xa thực tế, và nguồn mô tả tác động của rủi ro mô hình (*model risk*) là có thể rất lớn (tata_bank_alm, Ch.2, Embedded Options, d.1837). Nguồn nêu ngân hàng dùng mô hình dựa trên kỳ quan sát đủ dài, rà soát và cập nhật định kỳ (tata_bank_alm, Ch.2, Embedded Options, d.1837). Hướng dẫn của Cơ quan Ngân hàng Châu Âu (EBA) giới hạn biên độ của một số giả định để tránh kết luận vô nghĩa (tata_bank_alm, Ch.2, Embedded Options, d.1837):
> Ngày định giá lại theo hành vi giả định đối với tiền gửi bán lẻ, tiền gửi bán buôn từ khách hàng phi tài chính và tiền gửi vận hành (...) không có ngày định giá lại cụ thể (tiền gửi không kỳ hạn) cần được giới hạn ở ngày định giá lại bình quân gia quyền tối đa 5 năm (tata_bank_alm, Ch.2, Embedded Options, d.1839).

Trần 5 năm áp vào kỳ định giá lại hành vi của tiền gửi không kỳ hạn, loại sản phẩm được mô tả ở trang [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]] và được mô hình hóa bằng danh mục tái tạo ở trang [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]]. Việc đưa chi phí của quyền chọn gắn trong sản phẩm vào giá vốn nội bộ nằm ở trang [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]].
