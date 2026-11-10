---
title: tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage
type: concept
tags: [alm, crypto, defi, deposits, liquidity-risk]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]
drives: [non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles, liquidity-risk]
related: [deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]
---

Tài chính phi tập trung (DeFi) nhằm thay các bên trung tâm của thị trường bằng một mạng các thực thể phi tập trung; ví dụ nổi bật là công nghệ sổ cái phân tán (DLT), lưu thông tin bằng các bản sao số lặp lại ở nhiều nơi như trong blockchain (tata_bank_alm, Ch.6, §6.2, d.3143). Hầu như chưa công cụ nào dựa trên DeFi đi qua trọn một chu kỳ tài chính, nên thiếu dữ liệu lịch sử để hiệu chuẩn mô hình quản trị rủi ro và ALM về hành vi khách hàng như trả trước, rút trước hạn hoặc đổi nhà cung cấp dịch vụ (tata_bank_alm, Ch.6, §6.2, d.3145). Token tiền gửi (*deposit token*) tương đương tiền gửi ngân hàng thương mại hiện có nhưng được ghi trên blockchain, nhờ đó chuyển được từ ví số của người bán sang ví số của người mua (tata_bank_alm, Ch.6, §6.2, d.3221).

Nguồn minh hoạ bằng tiền gửi không kỳ hạn, loại sản phẩm ở trang [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]]. Khi lãi suất tăng mà ngân hàng chưa nâng lãi suất tiền gửi, một phần tiền gửi thanh toán bị rút, còn một số khách hàng không phản ứng ngay; hành vi tiền gửi vì vậy không co giãn hoàn toàn theo lãi suất, và kỳ hạn hành vi của các khoản vốn qua đêm này có thể được mô hình hóa dài hơn nhiều so với kỳ hạn hợp đồng (tata_bank_alm, Ch.6, §6.2, d.3147). Nếu ngân hàng phát hành token tiền gửi, người dùng có thể dùng hợp đồng thông minh, tức thuật toán theo quy tắc tự thực hiện giao dịch trên blockchain, để tự động chuyển tiền gửi theo các quy tắc có đầu vào là lãi suất (tata_bank_alm, Ch.6, §6.2, d.3147) (tata_bank_alm, Ch.6, §6.2, d.3222). Khách hàng bán lẻ có thể "lập trình sẵn" để tiền gửi số được bán cho bên thứ ba khi lãi suất tiền gửi kém hấp dẫn, và bên thứ ba nhiều khả năng rút tiền khỏi ngân hàng; nguồn cho rằng giả định hành vi nền tiền gửi giữ nguyên sau khi token hóa là ngây thơ (tata_bank_alm, Ch.6, §6.2, d.3147). Chú thích của nguồn thêm rằng khách hàng có thể tìm ngân hàng có chênh lệch thấp nhất giữa lãi suất tiền gửi và lãi suất thị trường rồi chuyển tiền theo (tata_bank_alm, Ch.6, §6.2, d.3223).

Ví dụ này là một trường hợp của thay đổi hành vi do FinTech ở trang [[fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]]. Tiền gửi rời ngân hàng nhanh hơn là một nguồn của [[liquidity-risk|rủi ro thanh khoản]]. Trang [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]] ghi hướng dùng dữ liệu ở cấp từng khách hàng để đoán trước việc rút tiền.
