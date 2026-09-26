---
title: interest-rate-theoretical-decomposition-and-csrbb-boundary
type: concept
tags: [banking, alm, irrbb, csrbb, interest-rate-components, credit-spread, risk-free-rate, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Mô hình phân rã lý thuyết 5 thành tố cấu thành lãi suất (Interest Rate Theoretical Decomposition) theo Chuẩn mực BCBS 368 của Ủy ban Basel thiết lập cơ sở lý luận tài chính vi mô để bóc tách một mức lãi suất tài sản hoặc chi phí nợ thành các lớp bù đắp rủi ro độc lập, qua đó xác lập ranh giới pháp lý phân định rủi ro lãi suất trên sổ ngân hàng (IRRBB) và rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB) (bcbs_368, file d368.md, Annex 1.1.3–1.4, d.830–862; Figure 1).

Trong thực tiễn quản trị rủi ro ngân hàng, lãi suất được hình thành từ nhiều cấu phần giá trị đan xen mà ranh giới giữa chúng rất khó bóc tách định lượng. Để thiết lập khung giám sát nhất quán, Ủy ban Basel xác định mọi mức lãi suất sinh lời trên tài sản hoặc chi phí trả lãi trên nợ phải trả về mặt lý thuyết đều được cấu thành từ 5 thành tố cơ bản (Paragraph 1.3, d.832–839):

**Năm thành tố lý thuyết cấu thành lãi suất**

1. *Lãi suất phi rủi ro (The risk-free rate)*: Khối xây dựng nền tảng (fundamental building block) của mọi mức lãi suất, đại diện cho mức lợi suất kỳ vọng thuần túy mà một nhà đầu tư yêu cầu từ một khoản đầu tư hoàn toàn không có rủi ro tín dụng và không có rủi ro thanh khoản cho một kỳ hạn xác định (ví dụ đường cong lợi suất hoán đổi chỉ số qua đêm OIS hoặc trái phiếu chính phủ phi rủi ro tối cao).
2. *Phần bù thời lượng thị trường (Market duration spread)*: Công cụ có thời lượng (duration) càng dài thì độ nhạy cảm của giá trị hiện tại trước những biến động lãi suất thị trường càng lớn. Để bù đắp cho sự không chắc chắn của dòng tiền tương lai và mức độ biến động giá (price volatility), thị trường đòi hỏi một khoản phần bù gia tăng trên lãi suất phi rủi ro cho rủi ro thời lượng.
3. *Phần bù thanh khoản thị trường (Market liquidity spread)*: Ngay cả khi công cụ tài chính hoàn toàn không có rủi ro vỡ nợ, mức lãi suất vẫn phải chứa đựng một phần bù thanh khoản đại diện cho khẩu vị thị trường chung và mức độ sẵn có của các bên mua/bán sẵn sàng giao dịch, phản ánh chi phí chuyển đổi công cụ thành tiền mặt nhanh chóng mà không gây tổn thất giá.
4. *Phần bù rủi ro tín dụng thị trường chung (General market credit spread)*: Khoản phần bù chênh lệch lợi suất mà các thành viên thị trường yêu cầu đối với một mức chất lượng tín dụng nhất định trên thị trường (ví dụ mức lợi suất chênh lệch mà một công cụ nợ do tổ chức phát hành xếp hạng AA phải trả cao hơn so với tài sản phi rủi ro cùng kỳ hạn). Đây là phần bù tín dụng mang tính hệ thống, tách biệt hoàn toàn với rủi ro của từng con nợ riêng lẻ.
5. *Phần bù rủi ro tín dụng đặc thù (Idiosyncratic credit spread)*: Phản ánh rủi ro vỡ nợ cụ thể gắn liền với hồ sơ tín dụng của từng khách hàng vay riêng biệt (chịu ảnh hưởng bởi năng lực tài chính, xếp hạng tín dụng nội bộ, lĩnh vực ngành nghề và vị trí địa lý) cũng như các đặc tính hợp đồng của công cụ nợ (tài sản bảo đảm, thứ bậc hoàn trả).

**Cấu trúc lãi suất thực tế trong cho vay thương mại**

Trong khi 5 thành tố trên có thể dễ dàng nhận diện và định giá độc lập trên các công cụ nợ giao dịch trên thị trường (như trái phiếu thanh khoản), đối với các khoản tín dụng khách hàng truyền thống, lãi suất thường được hình thành thông qua hai cấu phần tổng hợp (Annex 1.1.3, d.840–845):
- *Chi phí vốn huy động nội bộ (Funding rate)* hoặc *Lãi suất tham chiếu (Reference rate) cộng Biên độ vốn (Funding margin)*: Phản ánh chi phí vốn hòa trộn nội bộ của ngân hàng thông qua cơ chế định giá điều chuyển vốn nội bộ (FTP), hoặc được neo theo các chỉ số tham chiếu thị trường bên ngoài (như SOFR, Euribor, VNIBOR). Cấu phần này tích hợp lãi suất phi rủi ro, phần bù thời lượng, phần bù thanh khoản và một phần credit spread thị trường chung. Sự phân kỳ giữa chi phí huy động thực tế và lãi suất tham chiếu là nguồn gốc trực tiếp sinh ra [[interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]].
- *Biên độ thương mại / Biên độ tín dụng (Commercial margin / Credit margin)*: Là phần biên độ cộng thêm được quy định cụ thể trong hợp đồng hoặc do ngân hàng ấn định toàn quyền (administered rate) nhằm bù đắp rủi ro tín dụng đặc thù của khách hàng và đem lại lợi nhuận mục tiêu cho ngân hàng.

**Ranh giới pháp lý phân định giữa IRRBB và CSRBB**

Ủy ban Basel phân định rõ ràng ranh giới pháp lý và phạm vi điều tiết giữa hai loại hình rủi ro (Annex 1.1.3–1.4, d.846–862; Figure 1):
- **Phạm vi của Rủi ro Lãi suất Sổ Ngân hàng (IRRBB)**: Bao hàm toàn bộ các biến động phát sinh từ sự thay đổi của (i) Lãi suất phi rủi ro; (ii) Phần bù thời lượng thị trường; (iii) Lãi suất tham chiếu thị trường; và (iv) Biên độ vốn huy động (funding margin). IRRBB tập trung đo lường tác động của sự dịch chuyển hình dạng, độ dốc và độ cao của các đường cong lợi suất lên giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) và thu nhập lãi thuần ($\Delta NII$).
- **Phạm vi của Rủi ro Chênh lệch Tín dụng Sổ Ngân hàng (CSRBB)**: Được định nghĩa là toàn bộ rủi ro biến động chênh lệch giá (spread risk) trên tài sản và nợ phải trả của các công cụ có rủi ro tín dụng phát sinh từ (i) Sự thay đổi của Phần bù thanh khoản thị trường; và (ii) Sự thay đổi của Phần bù rủi ro tín dụng thị trường chung (Annex 1.1.4, d.859–860). CSRBB bắt nguồn từ sự biến đổi trong nhận thức thị trường về chất lượng tín dụng của một nhóm tài sản hoặc tính thanh khoản chung của thị trường.

Quy định Basel nhấn mạnh nguyên tắc loại trừ cốt lõi: **CSRBB không bao gồm rủi ro tín dụng đặc thù (idiosyncratic credit spread) và không bao gồm rủi ro vỡ nợ dự kiến hoặc rủi ro nhảy vỡ nợ (jump-to-default risk)** (Annex 1.1.4, d.859). Các rủi ro vỡ nợ này thuộc phạm vi quản trị riêng biệt của Khuôn khổ Rủi ro Tín dụng Trụ cột 1 (Credit Risk Framework).

Mô hình phân rã lý thuyết này kết nối trực tiếp với [[credit-spread-risk-in-the-banking-book-csrbb]], đồng thời cung cấp căn cứ để xác định đường cong chiết khấu lãi suất phi rủi ro và quy tắc khấu trừ biên độ thương mại trong [[standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule]] và [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
