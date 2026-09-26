---
title: standardised-term-deposit-early-redemption-risk-and-tdrr-scalars
type: concept
tags: [banking, alm, irrbb, early-redemption-risk, tdrr, term-deposits, behavioural-modelling, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Đo lường rủi ro rút tiền gửi có kỳ hạn trước hạn chuẩn hóa và hệ số vô hướng TDRR (Standardised Term Deposit Early Redemption Risk and TDRR Scalars) thiết lập quy tắc pháp lý và thuật toán định lượng hành vi rút vốn trước ngày đáo hạn hợp đồng của người gửi tiền cá nhân trong Khung đo lường chuẩn hóa IRRBB của Ủy ban Basel, thông qua việc điều chỉnh tỷ lệ rút tiền trước hạn cơ sở ($TDRR_{0,c}^p$) bằng ma trận hệ số vô hướng theo kịch bản ($u_i$) (bcbs_368, file d368.md, Section IV.4, d.704–738; Paragraph 125–129; Table 4).

Rủi ro rút tiền gửi có kỳ hạn trước hạn (early redemption risk) cấu thành một vị thế quyền chọn bán (put option) mà ngân hàng đã cấp ngầm định cho khách hàng. Về mặt kinh tế, ngân hàng thường sử dụng nguồn tiền gửi có kỳ hạn cố định để tài trợ và phòng hộ cho các tài sản sinh lời có kỳ hạn tương ứng. Khi lãi suất thị trường tăng vọt, người gửi tiền có động lực tài chính mạnh mẽ để đơn phương phá vỡ hợp đồng, rút tiền trước hạn nhằm tái đầu tư vào các sản phẩm tiền gửi hoặc công cụ nợ mới có lãi suất cao hơn, làm sụp đổ cấu trúc phòng hộ kỳ hạn và phơi bày ngân hàng trước chi phí tái tài trợ đắt đỏ.

**Tiêu chuẩn pháp lý và kinh tế phân loại tiền gửi có kỳ hạn**

Theo quy định nghiêm ngặt của Ủy ban Basel, một khoản tiền gửi có kỳ hạn chỉ được phép coi là nợ phải trả lãi suất cố định thuần túy (và được phân bổ dòng tiền định giá lại theo đúng ngày đáo hạn hợp đồng) nếu ngân hàng chứng minh thỏa mãn ít nhất một trong hai điều kiện sau (Paragraph 125, d.706–710):
1. *Điều kiện pháp lý*: Người gửi tiền không có bất kỳ quyền pháp lý nào được rút tiền trước ngày đáo hạn hợp đồng; hoặc
2. *Điều kiện kinh tế*: Việc rút tiền trước hạn bị áp đặt một chế tài phạt tài chính đáng kể (significant penalty), bảo đảm bù đắp tối thiểu toàn bộ khoản chênh lệch lãi suất mất mát giữa ngày rút thực tế và ngày đáo hạn hợp đồng, cộng với toàn bộ chi phí kinh tế phát sinh từ việc phá vỡ hợp đồng của ngân hàng (Footnote 23, d.715).

Nếu hợp đồng tiền gửi áp dụng biểu phí phạt đơn giản (chẳng hạn chỉ phạt một tỷ lệ phần trăm trên lãi tích lũy hoặc hạ lãi suất về mức không kỳ hạn nhưng không đủ bù đắp chi phí kinh tế tái tài trợ của ngân hàng) hoặc khách hàng có quyền rút tiền tự do, hợp đồng đó đương nhiên bị kết luận là mang rủi ro rút trước hạn (Paragraph 126). Đối với khách hàng bán buôn, nếu không đáp ứng hai tiêu chuẩn trên, ngân hàng bắt buộc phải giả định đối tác sẽ luôn thực hiện quyền rút tiền theo kịch bản gây bất lợi tài chính tối đa cho ngân hàng, và vị thế này phải chuyển sang Giai đoạn 4 để định giá như quyền chọn tự động.

**Hàm toán học TDRR và ma trận hệ số vô hướng kịch bản (Table 4)**

Đối với danh mục tiền gửi bán lẻ chịu rủi ro rút trước hạn, Khung chuẩn hóa quy định quy trình định lượng theo 2 bước (Paragraph 127–128):
1. *Xác định TDRR cơ sở ($TDRR_{0,c}^p$)*: Ngân hàng ước lượng hoặc cơ quan giám sát chỉ định tỷ lệ rút tiền gửi trước hạn cơ sở áp dụng cho từng danh mục tiền gửi đồng nhất $p$ theo đồng tiền $c$ dưới mặt bằng lãi suất hiện hành.
2. *Hiệu chỉnh TDRR theo 6 kịch bản sốc lãi suất*: Tỷ lệ rút tiền gửi trước hạn áp dụng cho kịch bản sốc $i$ được tính bằng cách nhân tỷ lệ cơ sở với hệ số vô hướng $u_i$ (Paragraph 128, d.717–721):

$$TDRR_{i,c}^p = TDRR_{0,c}^p \times u_i$$

Hệ số vô hướng $u_i$ được quy định tại Bảng 4 của Chuẩn mực BCBS 368 (bcbs_368, file d368.md, Table 4, d.723–732):

| Kịch bản sốc lãi suất ($i$) | Tên kịch bản (Annex 2) | Hệ số vô hướng $u_i$ | Diễn giải cơ chế hành vi tài chính |
|---|---|---|---|
| **$i = 1$** | Tăng song song (Parallel up) | **$1{,}2$** | Mặt bằng lãi suất huy động mới tăng vọt $\rightarrow$ Chi phí cơ hội tăng cao kích thích rút sớm $\rightarrow$ TDRR tăng $20\%$. |
| **$i = 2$** | Giảm song song (Parallel down) | **$0{,}8$** | Lãi suất huy động mới sụt giảm $\rightarrow$ Khoản tiền gửi cũ giữ mức lãi suất hấp dẫn $\rightarrow$ TDRR giảm $20\%$. |
| **$i = 3$** | Cú sốc dốc (Steepener) | **$0{,}8$** | Lãi suất ngắn hạn giảm $\rightarrow$ Động lực rút tiền gửi ngắn hạn để gửi lại không đáng kể $\rightarrow$ TDRR giảm $20\%$. |
| **$i = 4$** | Cú sốc phẳng (Flattener) | **$1{,}2$** | Lãi suất ngắn hạn tăng cao $\rightarrow$ Người gửi tiền rút sớm để gửi ngắn hạn hưởng lợi suất mới $\rightarrow$ TDRR tăng $20\%$. |
| **$i = 5$** | Tăng ngắn hạn (Short rate up) | **$1{,}2$** | Lãi suất ngắn hạn tăng dựng đứng $\rightarrow$ Khách hàng ồ ạt tất toán hợp đồng cũ để gửi lại $\rightarrow$ TDRR tăng $20\%$. |
| **$i = 6$** | Giảm ngắn hạn (Short rate down) | **$0{,}8$** | Lãi suất ngắn hạn giảm mạnh $\rightarrow$ Người gửi tiền kiên quyết nắm giữ hợp đồng đến đáo hạn $\rightarrow$ TDRR giảm $20\%$. |

**Quy tắc slotting dồn về dải qua đêm và điều chỉnh dòng tiền**

Khung chuẩn hóa thiết lập cơ chế xử lý dòng tiền rút trước hạn mang tính thận trọng tối đa (Paragraph 127 & 129, d.711, 733–737):
- *Dồn toàn bộ phần rút trước hạn vào dải qua đêm*: Dòng tiền định giá lại tương ứng với phần tiền gửi dự kiến bị rút sớm dưới kịch bản sốc $i$ được gom toàn bộ và ấn định vào dải kỳ hạn ngắn nhất (Overnight time bucket $k=1$, $t_1 = 0{,}0028$ năm):

$$TD_{i,c}^p(k=1) = TD_{0,c}^p \times TDRR_{i,c}^p$$

Trong đó $TD_{0,c}^p$ là tổng số dư danh nghĩa của danh mục tiền gửi có kỳ hạn loại $p$. Việc ấn định này phản ánh thực tế ngân hàng phải chi trả thanh khoản ngay lập tức hoặc phải tái định giá phần nợ này theo mức lãi suất qua đêm sau sốc.
- *Điều chỉnh giảm số dư tại các dải kỳ hạn hợp đồng*: Số dư nợ gốc danh nghĩa và dòng tiền lãi dự kiến tại dải kỳ hạn hợp đồng tương ứng ($k > 1$) được điều chỉnh giảm theo tỷ lệ:

$$TD_{i,c}^p(k) = TD_{0,c}^p(k) \times \left( 1 - TDRR_{i,c}^p \right)$$

Quy trình rút ngắn thời lượng nợ này làm trầm trọng thêm chênh lệch kỳ hạn định giá lại (repricing gap), trực tiếp làm gia tăng mức độ sụt giảm giá trị kinh tế của vốn chủ sở hữu trong Giai đoạn 3 của [[irrbb-standardised-framework-five-stage-measurement-architecture]] và cấu thành một mắt xích cốt lõi trong thuật toán tổng hợp tại [[standardised-delta-eve-calculation-and-multi-currency-aggregation-rules]].
