---
title: interest-rate-shock-calibration-methodology-global-scalars-and-caps-floors
type: concept
tags: [banking, alm, irrbb, shock-calibration, global-scalars, caps-and-floors, basel-derivation, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Phương pháp luận hiệu chuẩn sốc lãi suất, tham số toàn cầu và hệ thống trần-sàn (Interest Rate Shock Calibration Methodology Global Scalars and Caps Floors) thiết lập quy trình tính toán 2 bước chuẩn hóa của Ủy ban Basel để xác định độ lớn của các cú sốc lãi suất theo từng đồng tiền từ chuỗi số liệu lịch sử 16 năm, kết hợp với các hệ số nhân toàn cầu cơ sở và hệ thống trần-sàn giám sát pháp định (bcbs_368, file d368.md, Annex 2, d.1112–1207; Table 1–4).

Để bảo đảm tính so sánh quốc tế và tạo lập một sân chơi bình đẳng (level playing field) giữa các ngân hàng hoạt động đa quốc gia, Ủy ban Basel từ bỏ phương pháp áp đặt một mức sốc tùy tiện duy nhất (như mức sốc phẳng $\pm 200$ bps của Basel 2004) mà thay bằng thuật toán định lượng dựa trên bằng chứng thực nghiệm phản ánh trung thực môi trường lãi suất đặc thù của từng khu vực pháp lý.

**Bước 1: Xây dựng chuỗi dữ liệu 16 năm và xác định lãi suất bình quân địa phương**

Ủy ban Basel thu thập chuỗi dữ liệu chu kỳ lãi suất hàng ngày trong giai đoạn 16 năm kéo dài từ ngày **03/01/2000 đến ngày 31/12/2015** cho từng đồng tiền riêng biệt (Annex 2 Step 1, d.1118–1121):
- Mức lãi suất bình quân của từng đồng tiền được tính bằng trung bình cộng của toàn bộ các quan sát lãi suất hàng ngày trải rộng trên **9 dải kỳ hạn đại diện**: 3 tháng, 6 tháng, 1 năm, 2 năm, 5 năm, 7 năm, 10 năm, 15 năm và 20 năm.
- Kết quả lãi suất bình quân lịch sử của các đồng tiền chủ chốt được quy định tại Bảng 2 của Annex 2 (bcbs_368, file d368.md, Table 2, d.1122–1167):
  - Nhóm lãi suất thấp: Yên Nhật (JPY) $89$ bps ($0{,}89\%$), Franc Thụy Sĩ (CHF) $183$ bps ($1{,}83\%$), Đô la Singapore (SGD) $230$ bps;
  - Nhóm lãi suất trung bình: Euro (EUR) $300$ bps ($3{,}00\%$), Đô la Mỹ (USD) $329$ bps ($3{,}29\%$), Bảng Anh (GBP) $375$ bps, Đô la Canada (CAD) $341$ bps, Đô la Úc (AUD) $517$ bps;
  - Nhóm thị trường mới nổi / lãi suất cao: Rand Nam Phi (ZAR) $867$ bps, Real Brazil (BRL) $1.153$ bps, Lira Thổ Nhĩ Kỳ (TRY) $1.494$ bps, Peso Argentina (ARS) $3.363$ bps.

**Bước 2: Áp dụng bộ tham số sốc toàn cầu cơ sở (Baseline Global Shock Parameters)**

Từ chuỗi phân phối lợi suất toàn cầu, Ủy ban Basel xác định các hệ số sốc toàn cầu cơ sở $\bar{\alpha}_j$ bằng cách lấy bình quân gia quyền của các tham số sốc trên tất cả các đồng tiền (Annex 2 Step 2, Table 3, d.1168–1176):

| Phân đoạn đường cong | Ký hiệu tham số | Trọng số sốc toàn cầu cơ sở ($\bar{\alpha}_j$) |
|---|---|---|
| **Cú sốc song song (Parallel)** | $\bar{\alpha}_{\text{parallel}}$ | **$60\%$** |
| **Cú sốc lãi suất ngắn hạn (Short rate)** | $\bar{\alpha}_{\text{short}}$ | **$85\%$** |
| **Cú sốc lãi suất dài hạn (Long rate)** | $\bar{\alpha}_{\text{long}}$ | **$40\%$** |

Lấy lãi suất dài hạn bình quân lịch sử của từng đồng tiền nhân với bộ ba tham số toàn cầu này sẽ cho ra biên độ cú sốc chưa điều chỉnh (Bảng 4, d.1179–1192). Ví dụ đối với đồng USD:
- Cú sốc song song sơ bộ: $329 \text{ bps} \times 60\% = 197$ bps;
- Cú sốc ngắn hạn sơ bộ: $329 \text{ bps} \times 85\% = 279$ bps;
- Cú sốc dài hạn sơ bộ: $329 \text{ bps} \times 40\% = 131$ bps.

**Hệ thống trần và sàn pháp định giám sát (Prudential Caps and Floors)**

Ủy ban Basel nhận định rằng việc áp dụng thuần túy phép nhân tỷ lệ sẽ dẫn đến hai khiếm khuyết nguy hiểm: (i) Tạo ra mức sốc quá nhỏ đối với các đồng tiền có lãi suất danh nghĩa thấp (như JPY hoặc CHF), khiến bài kiểm tra áp lực mất đi tính răn đe; và (ii) Tạo ra mức sốc quá lớn phi thực tế đối với các nền kinh tế đang phát triển hoặc có lạm phát cao (như ARS, TRY, BRL) làm méo mó kết quả đo lường (Annex 2, d.1193–1204).

Để thiết lập tính thận trọng tối thiểu và bảo đảm khả năng thanh khoản hoạt động, Basel quy định hệ thống trần-sàn nghiêm ngặt (d.1193–1200):
- **Sàn tối thiểu tuyệt đối (The Floor)**: **$100$ bps** ($1{,}0\%$) cho tất cả các kịch bản và mọi đồng tiền. Không một đồng tiền nào trên thế giới được phép áp dụng mức sốc thấp hơn 100 bps. Cơ quan giám sát quốc gia có quyền áp đặt mức sàn cao hơn đối với đồng nội tệ của mình (National Discretion).
- **Hệ thống trần tối đa biến đổi (Variable Caps $\Delta \bar{R}_j^{\text{cap}}$)**:
  - Trần cú sốc song song: $\Delta \bar{R}_{\text{parallel}}^{\text{cap}} = \mathbf{400 \text{ bps}}$;
  - Trần cú sốc ngắn hạn: $\Delta \bar{R}_{\text{short}}^{\text{cap}} = \mathbf{500 \text{ bps}}$;
  - Trần cú sốc dài hạn: $\Delta \bar{R}_{\text{long}}^{\text{cap}} = \mathbf{300 \text{ bps}}$.

Công thức toán học xác định biên độ sốc chính thức $\Delta \bar{R}_{j,c}$ cho kịch bản $j \in \{\text{parallel}, \text{short}, \text{long}\}$ theo đồng tiền $c$ được chuẩn hóa (Annex 2, d.1195–1200):

$$\Delta \bar{R}_{j,c} = \min\left( \Delta \bar{R}_j^{\text{cap}}, \max\left( 100 \text{ bps}, \bar{\alpha}_j \cdot \text{Lãi suất bình quân}_c \right) \right)$$

Sau khi áp dụng trần-sàn và làm tròn theo bước nhảy $50$ bps, Basel ban hành Bảng 1 chuẩn hóa chính thức (như USD: 200/300/150 bps; EUR: 200/250/100 bps; JPY: 100/100/100 bps do chạm sàn 100 bps; ARS/BRL: chạm trần 400/500/300 bps).

Đối với các kịch bản sốc xoay (Steepener và Flattener), biến động tại dải kỳ hạn ngắn nhất ($t_1$) không được vượt quá trần $500$ bps và tại dải kỳ hạn dài nhất ($t_K$) không được vượt quá trần $300$ bps (Footnote 45, d.1203).

**Ứng dụng đối với các đồng tiền nội tệ và Chu kỳ tái hiệu chuẩn**

Đối với các đồng tiền không nằm trong danh sách Bảng 1 của BCBS 368 (chẳng hạn như Đồng Việt Nam - VND được quy định tại Thông tư 83/2025/TT-NHNN Phụ lục V), cơ quan quản lý tiền tệ quốc gia áp dụng chính xác thuật toán 2 bước này: thu thập chuỗi lãi suất lịch sử địa phương trong 16 năm, nhân với bộ ba hệ số toàn cầu cơ sở ($60\%$, $85\%$, $40\%$) và áp dụng sàn $100$ bps cùng hệ thống trần $(400, 500, 300)$ bps để xác định biên độ sốc chuẩn mực cho đồng nội tệ.

Ủy ban Basel cam kết thực hiện tái hiệu chuẩn định kỳ (Recalibration) toàn bộ bảng tham số sốc tối thiểu **5 năm một lần** nhằm cập nhật kịp thời các biến đổi cơ cấu trong môi trường kinh tế vĩ mô toàn cầu (Annex 2, d.1114).

Khuôn khổ hiệu chuẩn này liên kết trực tiếp với [[six-standardised-interest-rate-shock-scenarios-and-mathematical-formulations]], cung cấp tham số cốt lõi cho [[irrbb-standardised-framework-five-stage-measurement-architecture]] và làm cơ sở vận hành [[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]].
