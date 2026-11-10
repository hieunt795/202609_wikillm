---
title: non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles
type: concept
tags: [alm, irrbb, non-maturity-products, liquidity-risk, administered-rates]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governed_by: [replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]
drives: [interest-rate-risk-in-the-banking-book-irrbb, liquidity-risk]
driven_by: [fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities, tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage]
related: [non-maturity-deposit-modelling-runs-from-behavioural-options-through-replicating-portfolios-to-unstable-deposit-betas, sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models, embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]
---

Sản phẩm không kỳ hạn (Non-maturity Products — NMP) là các vị thế tài sản hoặc nợ phải trả trên bảng cân đối kế toán mà kỳ hạn hành vi thực tế (*behavioral maturity*) khác với kỳ hạn hợp đồng (*contractual maturity*), hoặc hoàn toàn không có kỳ hạn đáo hạn xác định theo hợp đồng (tata_bank_alm, Ch.2, Non-maturity Products, d.1786). Mặc dù mang tên "không kỳ hạn", các công cụ này trên thực tế vẫn sẽ đáo hạn và tiêu hao dần theo thời gian; điểm cốt lõi là thời điểm đáo hạn không được ấn định trước tại ngày mở tài khoản, hoặc khách hàng nắm giữ quyền chọn đơn phương thay đổi quy mô dòng tiền (tata_bank_alm, Ch.2, Non-maturity Products, d.1786). Trên bảng cân đối, NMP bao gồm hai nhóm chính: bên tài sản là các khoản vay mua nhà thế chấp chịu rủi ro trả nợ trước hạn (*prepayment risk*); bên nguồn vốn là các khoản tiền gửi không kỳ hạn (Non-maturity Deposits — NMDs) như tiền gửi thanh toán (*sight deposits*) và tiền gửi tiết kiệm rút tiền linh hoạt (*savings deposits*) (tata_bank_alm, Ch.2, Examples of Non-maturity Products, d.1790–1792).

Nguồn xếp việc mô hình hóa NMP vào nhóm việc khó nhất khi đo rủi ro lãi suất, tức đầu vào của [[interest-rate-risk-in-the-banking-book-irrbb]] (tata_bank_alm, Ch.2, Non-maturity Products, d.1786). Mỗi sản phẩm được mô tả bằng hai hồ sơ, hồ sơ thanh khoản (*liquidity profile*, gắn với [[liquidity-risk]]) và hồ sơ lãi suất (*interest rate profile*) (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1796):
1. **Hồ sơ thanh khoản**: vòng đời kỳ vọng của sản phẩm và cách khối lượng thay đổi theo thời gian;
2. **Hồ sơ lãi suất**: tần suất định giá lại (*reset frequency*) và lãi suất tham chiếu khi định giá lại (*reset reference rate* hay *indicator rate*).

Thông thường lãi suất tham chiếu có cùng kỳ hạn với kỳ hạn hợp đồng của công cụ, và khi đó hai hồ sơ trùng nhau (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1796). Khi thời gian tới kỳ định giá lại khác kỳ hạn hợp đồng, hai hồ sơ không còn trùng nhau (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1798). Nguồn lấy ví dụ một khoản vay lãi suất thả nổi 5 năm theo EURIBOR 12 tháng: công cụ thả nổi có giá trị bằng mệnh giá tại kỳ định giá lại kế tiếp nếu bỏ qua thay đổi rủi ro tín dụng, nên hồ sơ lãi suất là 1 năm; ngân hàng vẫn phải cấp thanh khoản tới khi đáo hạn, nên hồ sơ thanh khoản là 5 năm (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1798).

Một số sản phẩm như tiền gửi thanh toán (*sight deposits*) không có thỏa thuận hợp đồng về cả kỳ hạn lẫn lãi suất tham chiếu (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1800). Thiếu điều khoản về kỳ hạn thì ngân hàng không biết trước chính xác hồ sơ thanh khoản (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1810). Các sản phẩm này thường có lãi suất chỉ định (*administered rate*): ngân hàng có quyền tự đổi lãi suất trả cho người gửi, có trường hợp kèm thời hạn báo trước, nên ngân hàng cũng không biết trước chính xác hồ sơ lãi suất (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1810). Lãi suất chỉ định chỉ liên hệ lỏng với lãi suất thị trường (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1810); điểm này được trình bày ở trang [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]].

Nguồn nêu bốn khung ước lượng hồ sơ lãi suất và hồ sơ thanh khoản của NMP (tata_bank_alm, Ch.2, Liquidity and Interest Rate Profile, d.1812–1817):
1. **Mô hình chênh lệch đã điều chỉnh quyền chọn (option-adjusted spread, OAS)**: ước lượng giá trị các quyền chọn gắn trong sản phẩm bằng lý thuyết định giá quyền chọn chuẩn; các quyền chọn này được mô tả ở trang [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]];
2. **Mô hình tái tạo (replicating models)**: tái tạo sản phẩm bằng một danh mục gồm chủ yếu các công cụ tài chính thanh khoản và giao dịch được, sao cho diễn biến khối lượng và lãi suất của danh mục xấp xỉ hành vi kỳ vọng của sản phẩm, theo trang [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]];
3. **Mô hình vòng đời (lifecycle models)**: dùng quan sát lịch sử về khách hàng (loại khách hàng, ngày mở tài khoản, lãi suất ban đầu) để giải thích ảnh hưởng của chúng lên kỳ hạn kỳ vọng, khối lượng và lãi suất của sản phẩm;
4. **Mô hình ARIMA**: dựa trên quan sát lịch sử về khối lượng và lãi suất.

Nguồn nêu hành vi của khách hàng dùng các đổi mới FinTech buộc ngân hàng xem lại khung ALM, nhất là các mô hình quyền chọn gắn trong NMD (tata_bank_alm, Ch.6, §6.1, d.3137); trang [[fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]] trình bày tác động này. Ví dụ của nguồn là token tiền gửi trên blockchain: khách hàng có thể dùng hợp đồng thông minh lập trình sẵn việc bán tiền gửi khi lãi suất tiền gửi kém hấp dẫn, và bên mua nhiều khả năng rút tiền khỏi ngân hàng (tata_bank_alm, Ch.6, §6.2, d.3147). Nguồn cho rằng ngân hàng không thể giả định hành vi của nền tiền gửi giữ nguyên khi tiền gửi được token hóa (tata_bank_alm, Ch.6, §6.2, d.3147); cơ chế này nằm ở trang [[tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage]]. Trang [[non-maturity-deposit-modelling-runs-from-behavioural-options-through-replicating-portfolios-to-unstable-deposit-betas]] đặt sản phẩm không kỳ hạn vào toàn cảnh của nhóm trang về tiền gửi và mô hình hành vi.
