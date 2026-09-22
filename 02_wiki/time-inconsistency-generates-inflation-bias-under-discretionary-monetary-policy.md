---
title: time-inconsistency-generates-inflation-bias-under-discretionary-monetary-policy
type: concept
tags:
  - time-inconsistency
  - inflation-bias
  - rules-versus-discretion
  - game-theory
  - social-welfare
sources: [cargill_central_bank_policy]
status: stable
last_updated: 2026-09-22
---

Vấn đề bất nhất thời gian (time inconsistency) là một bước phát triển và mở rộng có tính nền tảng của [[lucas-critique-invalidates-econometric-policy-evaluation-under-discretion|Phê phán Lucas]] trong lý thuyết trò chơi vĩ mô (khởi xướng bởi Finn Kydland và Edward Prescott năm 1977, Robert Barro và David Gordon năm 1983), mô tả tình trạng trong đó một chính sách được đánh giá là tối ưu tại thời điểm ngắn hạn lại tất yếu dẫn đến kết quả hạ tối ưu trong dài hạn (cargill_central_bank_policy, Ch.16, Time Inconsistency, d.4726–4727). Trong hoạt động điều hành tiền tệ, chính sách tùy nghi là nguồn cơn gốc rễ sinh ra vấn đề bất nhất thời gian, biến các [[central-bank|ngân hàng trung ương]] thành những thực thể luôn mang xu hướng thiên lệch lạm phát (inflation bias) cố hữu (d.4738).

Cơ chế động học này được Alex Cukierman (1986) mô hình hóa rõ nét thông qua một hàm phúc lợi xã hội ($SW$), trong đó tổn thất xã hội gia tăng theo bình phương lạm phát ($\pi^2$) và cải thiện khi có khoảng cách sản lượng dương so với [[potential-gdp-measures-productive-capacity-at-full-employment|sản lượng tiềm năng]] ($y^* = 5$) (d.4740–4744):
$$SW = -\pi^2 + 2 \cdot (y - y^*)$$
Khi ngân hàng trung ương có toàn quyền tùy nghi lựa chọn duy trì ổn định giá cả ($\pi = 0$) hoặc tạo lạm phát bất ngờ ($\pi = 1$), và công chúng hình thành kỳ vọng lạm phát tương ứng ($\pi^e = 0$ hoặc $\pi^e = 1$), ma trận tương tác sinh ra bốn kết cục ngắn hạn (d.4746–4752):
- Kết cục $(1,1)$: $\pi = 0, \pi^e = 0 \implies y = 5 \implies SW = 0$ (ổn định giá cả hoàn hảo).
- Kết cục $(1,2)$: $\pi = 1, \pi^e = 0 \implies y = 6 \implies SW = -1^2 + 2(6 - 5) = 1$ (ngân hàng trung ương đánh lừa được kỳ vọng, kích thích sản lượng vượt tiềm năng và đạt phúc lợi ngắn hạn tối đa).
- Kết cục $(2,1)$: $\pi = 0, \pi^e = 1 \implies y = 4 \implies SW = -0^2 + 2(4 - 5) = -2$ (ngân hàng trung ương siết tiền bất ngờ trong khi kỳ vọng cao, đẩy nền kinh tế vào suy thoái).
- Kết cục $(2,2)$: $\pi = 1, \pi^e = 1 \implies y = 5 \implies SW = -1^2 + 2(5 - 5) = -1$ (lạm phát cao đi kèm sản lượng quay về tiềm năng).

Trong ngắn hạn, đối mặt với tình thế tương tự trò chơi Song đề tù nhân (prisoner's dilemma), dù công chúng kỳ vọng thế nào, ngân hàng trung ương tùy nghi luôn có động cơ chiếm đoạt lợi ích ngắn hạn bằng cách bơm tiền tạo lạm phát (vì $1 > 0$ khi $\pi^e = 0$, và $-1 > -2$ khi $\pi^e = 1$) (d.4757). Tuy nhiên, trong dài hạn, công chúng có kỳ vọng hợp lý sẽ thấu hiểu xu hướng thiên lệch lạm phát này và nâng kỳ vọng lạm phát lên $\pi^e = 1$. Nền kinh tế bị giam cầm vĩnh viễn vào trạng thái cân bằng Nash hạ tối ưu tại điểm $(2,2)$: sản lượng thực tế không hề tăng thêm so với tiềm năng ($y = 5$), nhưng toàn xã hội phải gánh chịu mức phúc lợi sụt giảm ($SW = -1$ thay vì $SW = 0$) do lạm phát cao kéo dài (d.4759–4762).

Lý thuyết kinh tế lượng đề xuất bốn giải pháp thể chế để hóa giải bẫy bất nhất thời gian và thiên lệch lạm phát (d.4765–4766):
1. Ràng buộc theo quy tắc chính sách (rules-based policy): Buộc ngân hàng trung ương phải tuân thủ các quy tắc minh bạch như [[taylor-rule-formalizes-systematic-feedback-and-the-taylor-principle|quy tắc Taylor]] hoặc cam kết [[inflation-targeting-framework-anchors-expectations-through-transparent-commitment|khuôn khổ lạm phát mục tiêu]] để triệt tiêu quyền tùy nghi ngắn hạn.
2. Xây dựng uy tín thể chế (reputation): Tích lũy uy tín kiên định chống lạm phát qua nhiều chu kỳ để công chúng tin tưởng tuyệt đối vào cam kết ổn định giá cả.
3. Cơ chế hợp đồng thành tích (incentive contract): Ký hợp đồng gắn thù lao hoặc sự tồn tại của ban lãnh đạo ngân hàng trung ương với việc đạt mục tiêu ổn định giá cả.
4. Bổ nhiệm thống đốc bảo thủ (conservative central banker): Trao quyền điều hành cho những cá nhân có ác cảm cực đoan với lạm phát (theo mô hình Kenneth Rogoff) để thị trường tin rằng họ sẽ không bao giờ hy sinh giá cả vì việc làm ngắn hạn.

Trong thực tiễn, việc áp dụng các khuôn khổ quy tắc ràng buộc hoặc cơ chế thỏa hiệp như [[constrained-discretion-attempts-to-synthesize-rules-and-flexibility-in-central-banking|tùy nghi có kiềm chế]] là những nỗ lực thực tế nhất nhằm khắc phục vấn đề bất nhất thời gian trong các nền kinh tế phát triển.
