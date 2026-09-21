---
title: optimal-width-of-the-interest-rate-corridor
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, corridor, interest-rates, money-market]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

Độ rộng tối ưu của hành lang lãi suất (optimal width of the interest rate corridor) là bài toán đánh đổi trung tâm trong thiết kế [[interest-rate-corridor-symmetric-approach|hành lang lãi suất đối xứng]] của ngân hàng trung ương (bindseil_monetary_policy, Ch.6, §6.2, d.1242–1312).

**Đánh đổi cốt lõi giữa ổn định lãi suất và hoạt động thị trường**: NHTW đối mặt với xung đột mục tiêu cơ bản: (i) kiểm soát và ổn định lãi suất qua đêm: hành lang càng hẹp, biên độ dao động tối đa của lãi suất càng nhỏ, phương sai lãi suất càng thấp; (ii) duy trì thanh khoản thị trường liên ngân hàng và kỷ luật thị trường: hành lang đủ rộng tạo động lực kinh tế (spread penalty) để các ngân hàng tự tìm đến nhau vay mượn bù trừ thanh khoản thay vì ỷ lại vào bảng cân đối của NHTW.

**Tại sao không đặt độ rộng hành lang bằng 0?**: Nếu mục tiêu duy nhất là kiểm soát lãi suất thị trường, NHTW có thể đặt lãi suất cho vay bằng lãi suất tiền gửi ($i_B = i_D$, độ rộng bằng 0) để triệt tiêu hoàn toàn biến động lãi suất (Berentsen, Galli & Monnet 2010). Tuy nhiên, khi có chi phí giao dịch liên ngân hàng ($C_{MM} > 0$), hành lang bằng 0 sẽ triệt tiêu hoàn toàn giao dịch liên ngân hàng:
- *Mất kỷ luật thị trường*: Giao dịch song phương trên thị trường OTC buộc các ngân hàng phải thẩm định rủi ro tín dụng của đối tác ("peer monitoring"), ngăn chặn hành vi chấp nhận rủi ro quá mức (Hoerova & Monnet 2010).
- *Mất tín hiệu thị trường*: Thị trường liên ngân hàng phân tầng tín dụng (credit tiering) và chênh lệch rủi ro (credit spread) cung cấp tín hiệu cảnh báo sớm vô giá về stress tài chính cho nhà làm chính sách (Allen 2002).
- *Phình to bảng cân đối NHTW*: Khi thị trường tư nhân bị triệt tiêu, NHTW buộc phải đứng ra làm trung gian cho toàn bộ các dòng vốn bù trừ, gánh chịu toàn bộ rủi ro tín dụng phân phối trong hệ thống (Mitlid & Vesterlund 2001; xem thêm [[relative-vs-absolute-central-bank-intermediation]]).

**Mô hình Bindseil & Jablecki (2011b)**: Mô hình hoá cơ chế vi mô của đánh đổi này trong hệ thống 2 ngân hàng với tài khoản khép kín (d.1262–1312). Trình tự mỗi ngày gồm: (i) sáng: NHTW OMO sao cho cung dự trữ kỳ vọng $S = B$; (ii) sốc thanh khoản 1: sốc tổng thể $2d_1$ cùng sốc phân phối tiền gửi $k$; (iii) trưa: phiên giao dịch liên ngân hàng với chi phí $C_{MM}$, ngân hàng giao dịch khối lượng $y$ chừng nào $|MV_1 - MV_2| > C_{MM}$; (iv) chiều: sốc tổng thể $2d_2$; (v) cuối ngày: tiếp cận standing facilities để đạt dự trữ bắt buộc (0). Khi chi phí giao dịch $C_{MM} > 0$ và hành lang quá hẹp, hai ngân hàng không bù trừ hết sốc $k$, dẫn tới *tiếp cận hai chiều (two-sided recourse)*: một bên vay borrowing facility và bên kia gửi deposit facility. Hiện tượng này làm phình chiều dài bảng cân đối NHTW vượt khỏi mức cấu trúc tối thiểu; khối lượng phình thêm nghịch đảo với doanh số giao dịch liên ngân hàng. Do khối lượng giao dịch $E(y)$ là hàm lõm theo độ rộng hành lang còn độ biến động lãi suất là hàm lồi, hàm phúc lợi của NHTW luôn dẫn đến giá trị nội biên tối ưu (interior optimum) — không quá hẹp cũng không quá rộng (d.1305).

**Lựa chọn thực tiễn của các ngân hàng trung ương**: Bank of Canada (1995) đặt hành lang 50 bp giữa overdraft rate và surplus rate; với bid-ask liên ngân hàng dưới 1/8% (12.5 bp), spread 50 bp đủ tạo động lực thương lượng thị trường và giữ mức sử dụng standing facilities tối thiểu (d.1246–1248). Sveriges Riksbank (2001) từng áp dụng hành lang 150 bp rồi cân nhắc thu hẹp vì nhận thấy 150 bp rộng hơn cần thiết (d.1250–1252). Eurosystem trước 2008 áp dụng hành lang 200 bp ($\pm 100$ bp quanh lãi suất MRO), sau đó thu hẹp tạm thời xuống 100 bp mùa thu 2008 trước khi chuyển sang [[one-directional-standing-facility-monetary-policy|hệ thống sàn/surplus]] với full allotment.

**Vai trò của độ rộng hành lang trong khủng hoảng**: Khi thị trường liên ngân hàng đóng băng ($C_{MM} > C_{COR}$), Bindseil & Jablecki (2011a) chỉ ra rằng độ rộng hành lang chuyển từ tham số vận hành trung tính thành một công cụ chính sách tiền tệ chủ động. Thu hẹp hành lang giúp hạ trực tiếp lãi suất cho vay thực tế đối với doanh nghiệp và giải tỏa chi phí trung gian tuyệt đối qua bảng cân đối NHTW (xem chi tiết tại [[narrowing-interest-rate-corridor-and-absolute-central-bank-intermediation]]; bindseil_monetary_policy, Ch.13, §13.1, d.2885–3024).

Xem thêm: [[interest-rate-corridor-symmetric-approach]], [[standing-facilities-in-monetary-policy-operations]], [[three-techniques-to-control-short-term-interest-rates]], [[taralac-facility-target-rate-limited-access]].
