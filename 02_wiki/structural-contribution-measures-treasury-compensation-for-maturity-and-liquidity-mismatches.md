---
title: structural-contribution-measures-treasury-compensation-for-maturity-and-liquidity-mismatches
type: analysis
tags: [ftp, structural-contribution, treasury, alm, margin-attribution, asset-liability-mismatch, liquidity-risk, interest-rate-risk]
sources: [tata_bank_alm, vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Đóng góp cấu trúc (Structural Contribution) là phần lợi nhuận mà khối Nguồn vốn trung tâm (Treasury) nhận được để bù đắp cho việc chịu các rủi ro khi bảng cân đối không cân khớp hoàn toàn giữa tài sản dài hạn và nguồn vốn ngắn hạn — đây không phải biên lợi nhuận kinh doanh của bộ phận huy động hay cho vay, mà là **chi phí cấu trúc** (cost of the structure itself) mà Treasury phải quản lý. Khái niệm này xuất hiện từ ba góc nhìn khác nhau nhưng đều cùng chỉ một thực tế kinh tế: từ góc [[cost-of-funds-in-alm-establishes-internal-hurdle-rate-for-business-margin-allocation]], structural contribution là phần chênh lệch trong đường cong CoF giữa các kỳ hạn (CoF(2Y) > CoF(1Y)), phản ánh chi phí tái tài trợ khi tài sản dài hạn được tài trợ bằng vốn ngắn hạn (tata_bank_alm, Ch.2, 2.3.2 Cost of Funds, d.1630–1637).

Từ góc [[planned-nim-allocation-determines-ftp-deposit-mobilization-margins]], structural contribution được gọi là khoản bù đắp cho Treasury vì chịu hai rủi ro cơ bản khi giữ vị thế mismatched: (1) **rủi ro thanh khoản** — khi tiền gửi ngắn hạn roll hết nhưng tài sản dài hạn vẫn còn, Treasury phải tái huy động với lãi suất có thể cao hơn hoặc gặp khủng hoảng thanh khoản, (2) **rủi ro lãi suất** — khi lãi suất tăng lúc tái huy động, phần chênh lệch lãi suất có thể xâm xói lợi nhuận ròng từ vị thế ban đầu (tata_bank_alm, Ch.2, 2.3.4, d.1629–1633). Cả hai rủi ro này đều là hậu quả của cấu trúc bảng cân đối, không phải từ hoạt động kinh doanh cốt lõi của các bộ phận huy động hay cho vay.

Từ góc [[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]], structural contribution là biến động giữa ba yếu tố: (1) cấu trúc kỳ hạn của bảng cân đối xác định độ lớn của mismatch, (2) FTP curve phản ánh chi phí của mismatch đó, (3) hành vi của các bộ phận kinh doanh — khi [[ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation|FTP được điều chỉnh để steering]], structural contribution thay đổi tương ứng để tạo động lực kinh tế chính xác mà ALM cần, nhưng mức độ thay đổi phản ánh những giả định về hành vi sản phẩm chứ không phải chi phí thực tế của Treasury (tata_bank_alm, Ch.2, 2.3.7, d.1692–1695; vab_ftp_methodology, Điều 4.2.2, d.285–320).

Hiểu rõ structural contribution giúp phân biệt ba khái niệm dễ lẫn lộn: **business margin** (lợi nhuận kinh doanh thuần từ hoạt động huy động/cho vay), **funding cost** (chi phí thực tế của vốn trên thị trường bán buôn), và **structural cost** (chi phí từ cấu trúc cân đối không khớp). Khi một trang báo cáo lợi nhuận bộ phận, phần structural contribution không thuộc về bộ phận đó — nó được dành riêng cho Treasury, và sự biến động của nó theo thời gian phản ánh sự thay đổi trong cấu trúc bảng cân đối, không phải hiệu quả kinh doanh tốt hay xấu của bộ phận.
