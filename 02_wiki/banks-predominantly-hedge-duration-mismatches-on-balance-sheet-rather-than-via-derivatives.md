---
title: banks-predominantly-hedge-duration-mismatches-on-balance-sheet-rather-than-via-derivatives
type: analysis
tags: [alm, duration, hedging, interest-rate-swaps, commercial-banking]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
related: [maturity-balancing-manages-liquidity-duration-to-mitigate-rollover-and-repricing-risks, alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]
---

Phái sinh có thể được dùng để phòng hộ vi mô (*micro hedge*) cho một vị thế riêng lẻ trên bảng cân đối: một chân của swap tái tạo dòng tiền của vị thế theo chiều ngược lại, chân kia trả lãi suất thả nổi cộng hoặc trừ một biên (tata_bank_alm, Ch.1, Instruments Used in ALM, d.565). Ví dụ của nguồn là một khoản vay khách hàng lãi suất cố định 5 năm được phòng hộ bằng một hoán đổi lãi suất cố định lấy thả nổi, gọi là asset swap (tata_bank_alm, Ch.1, Instruments Used in ALM, d.565). Vị thế được phòng hộ có thể nằm ở bên tài sản hoặc bên nợ (tata_bank_alm, Ch.1, Instruments Used in ALM, d.565).

Nguồn ghi nhận, với nhận xét là điều này hơi bất ngờ, rằng quy mô vị thế hoán đổi lãi suất ròng của các ngân hàng tương đối không đáng kể so với quy mô hoạt động và các vị thế rủi ro của họ (tata_bank_alm, Ch.1, Instruments Used in ALM, d.567). Thay vì dùng swap, các ngân hàng có vẻ bù các khoản lệch duration bằng vị thế nội bảng (tata_bank_alm, Ch.1, Instruments Used in ALM, d.567). Nhận định này dựa trên nghiên cứu của McPhail, Schnabl và Tuckman (2024) về việc ngân hàng có phòng hộ bằng hoán đổi lãi suất hay không (tata_bank_alm, Ch.1, Notes, d.800).

Nguồn nêu hai điều kiện đi kèm việc dùng phái sinh. Chiến lược ALM có phái sinh cần chuyên môn đáng kể của tổ chức, và một giao dịch phòng hộ không thành có thể gây hại hơn việc không phòng hộ; hướng dẫn giám sát yêu cầu tổ chức chứng minh mình hiểu hệ quả của việc phòng hộ bằng phái sinh lãi suất (tata_bank_alm, Ch.1, Instruments Used in ALM, d.569–575). Về kế toán, khi đủ điều kiện kế toán phòng hộ (*hedge accounting*), phái sinh đã được chứng minh là phòng hộ không phải ghi vào lãi lỗ như thông thường; để đủ điều kiện, ngân hàng phải chứng minh phòng hộ có hiệu quả, với hồi quy giữa thay đổi giá trị của hai phía nằm trong khoảng 80% đến 125% (tata_bank_alm, Ch.1, Notes, d.772).

Việc chỉnh kỳ hạn bằng chính các vị thế nội bảng là nội dung của trang [[maturity-balancing-manages-liquidity-duration-to-mitigate-rollover-and-repricing-risks]], và chuỗi các bước cân đối bảng cân đối nằm ở trang [[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]].
