---
title: tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage
type: concept
tags: [alm, crypto, defi, deposits, liquidity-risk]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Tiền gửi được mã hóa (*deposit tokens*) kết hợp cùng các hợp đồng thông minh (*smart contracts*) trên công nghệ sổ cái phân tán (DLT) và tài chính phi tập trung (DeFi) cho phép người gửi tiền thiết lập cơ chế kinh doanh chênh lệch lãi suất (*interest rate arbitrage*) tự động hóa hoàn toàn, triệt tiêu độ trễ hành vi truyền thống và tạo ra thách thức lớn đối với công tác mô hình hóa thanh khoản và ALM (tata_bank_alm, Ch.6, §6.2, d.3141–3148).

Trong kiến trúc ngân hàng truyền thống, tiền gửi không kỳ hạn duy trì được tính ổn định thanh khoản và thời lượng kéo dài nhờ vào sự thiếu nhạy cảm tức thời của khách hàng trước các biến động lãi suất thị trường. Ngay cả khi lãi suất điều hành tăng mạnh, nhiều người gửi tiền vẫn duy trì số dư tài khoản vãng lai vì sự tiện ích thanh toán và chi phí tìm kiếm địa chỉ gửi tiền sinh lời cao hơn (tata_bank_alm, Ch.6, §6.2, d.3147). Tuy nhiên, khi các định chế tài chính phát hành tiền gửi mã hóa—phiên bản số hóa của tiền gửi ngân hàng thương mại được ghi nhận trên sổ cái blockchain để lưu ký và giao dịch qua ví kỹ thuật số—ranh giới giữa tài khoản thanh toán và công cụ đầu tư thị trường tiền tệ bị xóa nhòa (tata_bank_alm, Ch.6, §6.2, d.3147, d.3221).

Sự kết hợp giữa token tiền gửi và hợp đồng thông minh cho phép người gửi tiền cá nhân và tổ chức "lập trình sẵn" (*pre-program*) các thuật toán tự động thực thi giao dịch chuyển nhượng vốn. Khách hàng có thể cài đặt điều kiện: nếu ngân hàng thương mại không điều chỉnh tăng lãi suất tiền gửi tương ứng với mức chênh lệch tham chiếu thị trường (*market spread*), hợp đồng thông minh sẽ tự động chuyển nhượng token tiền gửi cho bên thứ ba trên mạng lưới P2P hoặc rút cạn vốn ngay lập tức về một quỹ thị trường tiền tệ hoặc nền tảng sinh lời cao hơn (tata_bank_alm, Ch.6, §6.2, d.3147, d.3222–3223). Cơ chế này loại bỏ hoàn toàn yếu tố quán tính tâm lý con người, biến rủi ro rút tiền chậm truyền thống thành rủi ro rút vốn thuật toán tức thời (*algorithmic deposit run*).

Tình huống này đặt ra thách thức nghiêm trọng cho mô hình hóa ALM vì hầu hết các công cụ DeFi và tài sản mã hóa chưa từng trải qua một chu kỳ tài chính - kinh tế hoàn chỉnh (*full financial cycle*), dẫn đến sự thiếu hụt dữ liệu lịch sử để hiệu chỉnh các tham số hành vi rút tiền sớm hay kỳ hạn thực tế (tata_bank_alm, Ch.6, §6.2, d.3145). Đối với các ngân hàng đóng vai trò nhà cung cấp dịch vụ tài sản mã hóa (CASPs) hoặc huy động vốn qua trái phiếu số (*crypto bonds*), giả định rằng tiền gửi mã hóa sẽ có hành vi kết dính như tiền gửi truyền thống là một sai lầm nghiêm trọng trong quản trị rủi ro thanh khoản ([[liquidity-risk]]) và cân đối thời lượng bảng cân đối. Hiện tượng này thúc đẩy quá trình [[fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]] và đòi hỏi các công cụ [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]] để giám sát luồng thanh khoản thời gian thực.

Xem thêm: [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]], [[fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]], [[liquidity-risk]], [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]].
