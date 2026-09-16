# Log

> Nhật ký append-only, mỗi operation đúng 1 mục. Định dạng và danh sách `<op>`: `00_schema.md` §12. Lấy 5 mục gần nhất: `grep "^## \[" log.md | tail -5`.
>
> Lý do các quyết định: `decisions.md`. Mục có giờ `00-00-00` là mục cũ không lưu giờ. Bản log đầy đủ trước khi rút gọn: `git show e2adb7a:log.md`.

## [2026-09-12:00-00-00] ingest | imf_macro_accounting Ch.2 cụm A — đại lượng hạch toán quốc gia
- 14 trang mới: khung SNA, value added, GDP (3 trang), GNI, GNDI, absorption, tiết kiệm quốc gia, 3 đồng nhất thức đối ngoại
- 6 stub: current-account-balance, depreciation, final-consumption, gross-investment, inflation, mps-material-product-system
- Còn lại: Ch.2 cụm B–G

## [2026-09-12:00-00-00] ingest | imf_macro_accounting Ch.2 cụm B + C — đo lường chuyển đổi, lạm phát
- Nâng 2 stub lên draft: mps-material-product-system, inflation
- 8 trang mới: 3 trang đo lường chuyển đổi, 5 trang lạm phát (lõi, quán tính, phân loại, cú sốc giá, Laspeyres/Paasche)
- Còn lại: Ch.2 cụm D–G

## [2026-09-12:00-00-00] ingest | imf_macro_accounting Ch.2 cụm D + E — lao động, chính sách giá và thu nhập
- 10 trang mới: real-wages, trần tăng lương, unemployment-rate, nairu, types-of-unemployment, price-liberalization, hội tụ giá, incomes-policy, 2 trang kiểm soát lương
- Còn lại: Ch.2 cụm F–G

## [2026-09-12:00-00-00] ingest | imf_macro_accounting Ch.2 cụm F + G — case Ba Lan, khung SNA chi tiết
- 12 trang mới: 6 case Ba Lan 1989–94, 6 trang khung SNA; system-of-national-accounts-sna thành hub
- Ch.2 xong 7/7 cụm; còn 4 stub

## [2026-09-12:00-00-00] ingest | imf_macro_accounting Ch.2 — bồi đắp, gỡ 4 stub
- 4 stub lên draft bằng vật liệu sẵn có trong Ch.2: final-consumption, gross-investment, depreciation, current-account-balance
- 1 trang mới: leakages-equal-injections-in-the-circular-flow; thêm backlink cho 9 trang
- Wiki: 51 trang, 0 stub, 0 link chết, 0 trang mồ côi

## [2026-09-14:00-00-00] schema | batch 7 issue audit
- Thêm: index §Sources, bản đồ chunk nguồn dài (§10), chú thích vị trí (§7.5), ngưỡng nguồn dài, `_inbox.md` (§11), tiêu chí lint *Nhiễu OCR*, trường `reviewed:` tuỳ chọn
- Nợ: 51 trang chưa có chú thích §7.5, không backfill

## [2026-09-14:00-00-00] schema | đính chính — trạng thái ingest chuyển sang 03_state/
- Hoàn nguyên ngoại lệ vừa khoét vào luật `01_sources/` bất biến; tạo `03_state/imf_macro_accounting.md`

## [2026-09-14:00-00-00] lint | 51 trang — audit Karpathy + Evergreen
- 4 lỗi: lệnh grep backlink sai; alias `[[a|b]]` chưa định nghĩa; 0/51 trang có chú thích §7.5; 16/37 tag chỉ dùng 1 lần
- 3 khoảng trống: chưa query lần nào; mọi trang kẹt ở `draft`; chưa có git
- Sạch: 0 link chết, 0 mồ côi, 0 heading, 51/51 title đúng quy ước, 0 lỗi OCR

## [2026-09-14:00-00-00] repo | publish — commit đầu cho github.com/hieunt795/202609_wikillm
- Không commit `01_sources/` (bản quyền IMF); bù bằng `03_state/_sources_manifest.md` (SHA-256), thêm `README.md`, `.gitignore`
- Người dùng tự push từ máy

## [2026-09-15:19-10-02] repo | rollback về e2adb7a (51 trang)
- Hoàn tác `34751e1` (ingest Ch.1 + Ch.3, 117 trang, cùng hook/skill mới); bản đó giữ ở tag `ch3-snapshot`
- 17 mục log của nhánh đó: `git show ch3-snapshot:log.md`

## [2026-09-15:19-17-18] lint | 51 trang — audit Karpathy + Evergreen trên e848dc1
- 8 lỗi tài liệu/công cụ (A1–A8), 6 vấn đề cơ chế (B1–B6)
- Báo cáo: `Claude outputs/audit-2026-09-15-e848dc1.md` (không commit)

## [2026-09-15:19-40-23] schema | batch xử lý audit e848dc1
- Hook lấy lại từ `ch3-snapshot` (`--all`, link chết, mồ côi); lint sửa lệnh grep, thêm 3 tiêu chí; thêm skill `promote`; ingest thêm bước 0 duyệt ý chính
- Schema: alias §6, ngôn ngữ title §3, không có trang tóm tắt nguồn §2, phân vai vòng đời §9, định dạng log §12; sửa 5 tham chiếu chết và ví dụ lỗi thời
- Log viết lại theo §12; thêm `decisions.md`; README, `.gitignore` (`Claude outputs/`)

## [2026-09-15:19-40-23] ingest | 5 stub từ nợ stub của audit
- Tạo: cpi, exchange-rate, hyperinflation, indexation, subsidies; chèn 17 link từ 14 trang cũ (không nâng `last_updated`)
- Bỏ `fiscal-deficit`: chỉ 1 trang nhắc thâm hụt ngân sách (ghi ở `_inbox.md`)
- Wiki: 56 trang (51 draft + 5 stub); `--all` sạch

## [2026-09-15:20-04-31] schema | cho phép model tự review
- Thêm cặp `reviewed` + `reviewed_by: user|model` (§1, §9); hook kiểm cặp trường; skill mới `/review`; op `review` vào §12
- Lý do: `decisions.md` mục "Cho phép model tự review trang"

## [2026-09-15:20-04-31] review | 5 trang hub
- Đạt, chỉ thêm chú thích: gndi
- Đã sửa claim theo nguồn: gdp (khấu hao làm GDP đánh giá cao *sản lượng*, không phải *năng lực tăng thêm*); production-income-… (bỏ "tín hiệu chất lượng thống kê" nguồn không nói, thêm sai số dồn vào thặng dư); the-saving-investment-gap-… (lý do tách khu vực viết lại theo nguồn); system-of-national-accounts-sna (bỏ "trong nước", "không gắn một trường phái")
- 5/5 trang có chú thích §7.5, `reviewed_by: model`; `--all` sạch

## [2026-09-15:20-17-49] schema | chuẩn bị ingest Ch.3
- Phục hồi §2 *ưu tiên lý luận trước tường thuật*; bản đồ chunk chia Ch.3 thành cụm A–E, bối cảnh Ba Lan và Exercises/phụ lục đánh bỏ qua
- Lý do: `decisions.md` mục "Ch.3 chỉ ingest phần lý luận"

## [2026-09-15:20-17-49] ingest | imf_macro_accounting Ch.3 cụm A — khung kế toán tài khoá GFS
- 11 trang mới: government-finance-statistics-gfs (hub), general-government, conventional-fiscal-deficit, cơ sở tiền mặt, nợ đọng, thu, viện trợ, cho vay ròng, tái cấp vốn ngân hàng, tư nhân hoá, quỹ ngoài ngân sách/đối ứng
- Nối sang Ch.2: 4 link mới từ trang cũ (không nâng last_updated); mục inbox stub fiscal-deficit đóng vì đã có conventional-fiscal-deficit
- Còn lại: Ch.3 cụm B–E

## [2026-09-15:20-23-39] ingest | imf_macro_accounting Ch.3 cụm B — thước đo và tài trợ thâm hụt
- 13 trang mới: 6 trang thước đo (S−I chính phủ, chọn thước đo, PSBR, cán cân thường xuyên, primary, operational), 5 trang tài trợ (hub + 4 kênh), seigniorage, trần thuế lạm phát
- 3 stub: central-bank, reserve-money, crowding-out; cập nhật payments-arrears-… (nợ đọng là tài trợ cưỡng ép)
- Còn lại: Ch.3 cụm C–E

## [2026-09-15:20-27-59] ingest | imf_macro_accounting Ch.3 cụm C — nợ công và tính bền vững
- 9 trang mới: fiscal-sustainability (hub), động học nợ, hai chế độ r−g, ổn định nợ, khả năng thanh toán, 3 chỉ số bền vững, nợ cao, Ricardian equivalence, nợ đọng chi tiêu
- 1 stub: real-interest-rate; thêm link từ 4 trang cụm B
- Còn lại: Ch.3 cụm D–E

## [2026-09-15:20-31-38] ingest | imf_macro_accounting Ch.3 cụm D — phân tích thu
- 6 trang mới: tăng thu chắp vá, tax-elasticity, độ nổi, độ trễ thu khi lạm phát cao, nỗ lực thuế, tanzi-diagnostic-test
- Nối sang cụm A–B (thu, thâm hụt, tài trợ nước ngoài, cán cân thường xuyên)
- Còn lại: Ch.3 cụm E

## [2026-09-15:20-36-05] ingest | imf_macro_accounting Ch.3 cụm E — phân tích chi; Ch.3 phần lý luận xong
- 12 trang mới (khung chi, 3 vấn đề chi, vai trò nhà nước, lương, bảo dưỡng, tiêu chí trợ cấp, đầu tư công, lưới an sinh, bán tài khoá, phong toả chi, tác động vĩ mô, vòng chi–lạm phát–thu); nâng stub subsidies; 1 stub public-goods
- Ch.3 tổng cộng 51 trang mới + 5 stub; 39/201 cạnh đi ra ngoài khối Ch.3 (bản snapshot: 29/386)
- Còn lại: Ch.1, Ch.4, Ch.5, Ch.6; Modern Money Mechanics

## [2026-09-15:23-44-16] review | 5 trang
- Đạt sau khi sửa: gross-national-saving, absorption, current-account-balance, the-private-sector-resource-gap-must-be-financed-by-other-sectors, inflation
- Claim sai/không có nguồn: tiết kiệm Ba Lan sụt "không phải do tiêu xài" (d.1206 nói có); đánh đổi mức sống/năng lực tương lai; tách khu vực là "cách duy nhất" chẩn đoán CAB; giá tương đối là "tín hiệu" CSTT không nên xử lý
- Giữ lại: không; ghi `_inbox.md` mâu thuẫn trong nguồn về tiết kiệm Ba Lan 1992 cho lượt cụm F

## [2026-09-15:23-49-06] review | 5 trang
- Đạt nguyên trạng (chỉ thêm chú thích): a-one-time-price-shock-becomes-inflation-only-if-monetary-policy-accommodates-it, current-account-deficit-means-absorption-exceeds-national-income
- Đạt sau khi sửa: gni (GDP đo theo "lãnh thổ" → nguồn nói theo cư trú; bỏ ý nợ/lao động nước ngoài làm lệch chẩn đoán); depreciation (bỏ ý sai lệch so sánh quốc tế; tách lý do dùng số gộp cho GDP và cho tiết kiệm); final-consumption (bỏ ý "không thể chọn riêng một vế")
- Giữ lại: không

## [2026-09-15:23-52-17] review | 5 trang
- Đạt sau khi sửa: gross-investment (bỏ "nén đầu tư khác bản chất nén tiêu dùng"), incomes-policy (thêm giả định tỷ trọng lương/GDP không đổi; bỏ "chỉ mua thời gian"), institutional-sectors-in-the-sna (sửa quan hệ nhân quả ROW), types-of-inflation (bỏ "mỗi nguyên nhân một công cụ"; "hầu hết" → "thường")
- Sửa bổ sung inflation (lượt trước bỏ sót câu "phân loại để chọn công cụ" không có nguồn)
- Giữ lại: measured-gdp-covers-only-what-markets-price — title không khớp nội dung, ghi `_inbox.md`

## [2026-09-15:23-56-40] review | 6 trang
- Đổi tên measured-gdp-covers-only-what-markets-price → measured-gdp-is-an-imperfect-gauge-of-output-and-welfare (người dùng chốt; 5 link + index cập nhật; mục inbox đóng), sửa câu mở đầu và "phải ước lượng" → "vẫn tính nhưng đo không chính xác"; đạt
- Đạt nguyên trạng: polands-output-collapse-1990-91-came-from-three-distinct-causes. Đạt sau khi sửa: a-real-output-index-… ("không phải chuyện thống kê thuần tuý"), gdp-deflator (bỏ "quan trọng nhất"; thêm điều kiện "trực tiếp, ngắn hạn" cho giá nhập khẩu), inertial-inflation-… (bỏ "thắt cầu phải trả giá bằng sản lượng"; "lập luận chính" → "lý do đầu tiên"), laspeyres-and-paasche-… (bỏ "không nên đọc con số đơn lẻ như sự thật")
- Giữ lại: không

## [2026-09-16:00-12-21] ingest | imf_macro_accounting Ch.2 cụm A1 (viết lại) — SNA, khu vực, đại lượng hạch toán
- Viết mới từ nguồn 12 trang (giữ title): SNA, value-added, final-consumption, gross-investment, depreciation, absorption, gdp, ba cách đo GDP, leakages, gni, gndi, gross-national-saving; 1 trang mới: macroeconomic-analysis-divides-the-economy-into-five-main-sectors
- 2 stub: macroeconomic-sectors, net-exports; bản đồ chunk: tách A1/A2, chuyển d.1011–1017 sang cụm C, B–G về `[ ]`
- Còn lại Ch.2: A2, B–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-18-49] ingest | imf_macro_accounting Ch.2 cụm A2 (viết lại) — đồng nhất thức đối ngoại, GDP thực, giới hạn đo GDP
- Viết mới từ nguồn 6 trang (giữ title): GNDI − A = CAB, S − I = CAB, khoảng chênh khu vực tư (nối macroeconomic-sectors), real-gdp, gdp-deflator (chưa gồm phần so với CPI), measured-gdp-…
- current-account-balance hạ draft → stub, chờ Ch.4 (decisions.md)
- Còn lại Ch.2: B–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-24-22] ingest | imf_macro_accounting Ch.2 cụm B (viết lại) — đo lường trong kinh tế chuyển đổi, MPS
- Viết mới từ nguồn 4 trang (giữ title): mps-material-product-system, transition-statistics-…, a-real-output-index-…, to-what-extent-was-polands-output-decline-1990-91-overstated
- 2 trang mới: mps-counts-only-output-of-the-material-sphere, converting-mps-net-material-product-to-gdp-requires-four-adjustments
- Còn lại Ch.2: C–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-28-45] ingest | imf_macro_accounting Ch.2 cụm C (viết lại) — lạm phát và chỉ số giá
- Viết mới từ nguồn 6 trang (giữ title): inflation, lạm phát lõi, cú tăng giá một lần, types-of-inflation, lạm phát quán tính, Laspeyres/Paasche
- Nâng cpi stub → draft; 1 trang cầu nối mới cpi-and-the-gdp-deflator-differ-…; cập nhật gdp-deflator trỏ sang trang cầu nối
- Còn lại Ch.2: D–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-31-56] ingest | imf_macro_accounting Ch.2 cụm D (viết lại) — lương thực, thất nghiệp
- Viết mới từ nguồn 5 trang (giữ title): real-wages, real-wage-growth-is-bounded-by-productivity-growth, unemployment-rate, nairu, types-of-unemployment
- 2 trang mới: discouraged-workers-make-the-unemployment-rate-understate-joblessness, full-employment-does-not-mean-zero-unemployment
- Còn lại Ch.2: E–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-35-38] ingest | imf_macro_accounting Ch.2 cụm E (viết lại) — chính sách giá và thu nhập
- Viết mới từ nguồn 5 trang (giữ title): price-liberalization, price-convergence-… (gộp tỷ giá thực d.1146), incomes-policy, designing-wage-controls-…, wage-controls-lose-effectiveness-… (thêm d.1224)
- 1 trang mới: open-trade-and-a-convertible-currency-…; 1 stub: soft-budget-constraint; nối lại trang case giá Ba Lan (tránh mồ côi)
- Còn lại Ch.2: F–G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-40-41] ingest | imf_macro_accounting Ch.2 cụm F (viết lại) — case Ba Lan 1989–94
- Viết mới từ nguồn 6 trang case (giữ title); 1 trang mới: polish-real-wages-stabilized-but-lagged-productivity-gains
- ⚠️ Conflict trên polish-national-saving-…: tiết kiệm 1992 (d.1206 so với d.1204 + Table 2.3 d.1407); đóng mục inbox tương ứng
- Còn lại Ch.2: G (bản gốc ở tag ch2-snapshot)

## [2026-09-16:00-46-02] ingest | imf_macro_accounting Ch.2 cụm G (viết lại) — khung SNA chi tiết; Ch.2 viết lại xong
- Viết mới từ nguồn 6 trang (giữ title); 2 trang mới: sna-transactions-are-goods-and-services-distributive-or-financial, polands-1992-sna-accounts-… (⚠️ Conflict d.1609 so với Table 2.3)
- Ch.2 viết lại xong 8/8 cụm; không còn trang thiếu chú thích §7.5 → đóng mục nợ trong inbox
- Còn lại: Ch.1, Ch.4, Ch.5, Ch.6; Modern Money Mechanics

## [2026-09-16:00-50-57] lint | 125 trang
- Bước 0 sạch; 2 Conflict (người dùng hoãn), 4 khái niệm chưa có trang, 1 cặp nghi trùng, 3 vi phạm title, 11 nợ stub; 0 OCR, stale, Atomic, mồ côi
- 101 trang đủ điều kiện stable (55 Ch.2, 46 Ch.3), chưa trang nào qua review; 2 mục inbox đề xuất xoá
- Báo cáo: Claude outputs/lint-2026-09-16.md

## [2026-09-16:00-58-12] schema | xử lý lint 2026-09-16 (phần không phải ingest)
- §8 luật 1: title phủ định hợp lệ (người dùng chốt, decisions.md); lint bỏ tiêu chí title phủ định; giữ nguyên 2 title phủ định
- Viết lại câu stub macroeconomic-sectors (tập trung tương tác); chèn 5 link (lưới an sinh ×2, soft-budget-constraint ×3), không nâng last_updated
- Inbox: xoá 2 mục; ghi chú conflict Ch.1 chuyển vào dòng Ch.1 của 03_state

## [2026-09-16:01-08-46] ingest | imf_macro_accounting — khái niệm từ lint 2026-09-16 (đa chương)
- 4 trang mới: balance-of-payments, state-owned-enterprises, aggregate-demand, nominal-anchor; nâng 6 stub lên draft: indexation, exchange-rate, crowding-out, real-interest-rate, public-goods, hyperinflation
- Vật liệu Ch.2–Ch.3, cộng trích lẻ có ghi rõ chương từ Ch.1, Ch.4, Ch.5, Ch.6 (ghi dải dòng vào 03_state); chèn 12 link tới trang mới (không nâng last_updated)
- Còn lại: Ch.1, Ch.4, Ch.5, Ch.6 (ingest trọn chương); Modern Money Mechanics; stub chờ: central-bank, reserve-money, net-exports, current-account-balance, macroeconomic-sectors, soft-budget-constraint

## [2026-09-16:08-17-02] ingest | imf_macro_accounting Ch.4 cụm A — khung khái niệm BOP
- 8 trang mới (double-entry, transfers, net-errors-and-omissions, flow-vs-stock, valuation, unit-of-account, NIIP, BPM5) + merge 3 trang (balance-of-payments, residency-in-the-sna, sna-accrual-double-entry)
- Ch.4 (158 KB) tự vượt ngưỡng nguồn dài, chia 6 cụm A–F trong `03_state/imf_macro_accounting.md`; cụm A xong
- Còn lại: cụm B (phân loại chuẩn BOP, d.3551–3648) → E (dự trữ), cụm F (case Ba Lan) tuỳ tình trạng minh chứng

## [2026-09-16:08-25-54] ingest | imf_macro_accounting Ch.4 cụm B — phân loại chuẩn BOP
- current-account-balance nâng stub→draft; 7 trang mới (tiêu chí phân loại, gộp/ròng, 4 nhóm tài khoản tài chính, dự trữ là flow không phải stock, giao dịch IMF, tài trợ ngoại lệ, chất lượng dữ liệu kinh tế chuyển đổi)
- Merge: balance-of-payments, balance-of-payments-manual-fifth-edition, transition-statistics-understate-private-sector-growth
- Còn lại Ch.4: cụm C (phân tích vị thế đối ngoại, d.3649–3829) → F (case Ba Lan)

## [2026-09-16:08-34-02] ingest | imf_macro_accounting Ch.4 cụm C — phân tích vị thế đối ngoại
- 12 trang mới: đường chia trên/dưới vạch, trade-balance, overall-balance, CAB=ΔFI+ΔRES, học thuyết Lawson, CA theo chế độ tỷ giá, solvency/sustainability vãng lai, cơ cấu thương mại, chiến lược hướng ngoại, trade bias (ERP), assessing-exchange-rate
- Merge: exchange-rate, current-account-deficit-means-absorption-exceeds-national-income
- Bỏ qua d.3816–3829 (Services/Income/Transfers chi tiết, ít giá trị mới) và bảng Ba Lan 4.3/4.4 (§2). Còn lại Ch.4: cụm D (nợ nước ngoài, FDI, d.3830–3938) → F

## [2026-09-16:08-36-45] schema | công thức trình bày bằng $$...$$, không lẫn văn xuôi
- 00_schema.md §7 luật 4: thêm quy ước đồng nhất thức/công thức dùng khối $$...$$ hoặc $...$, người dùng chốt
- Sửa 3 trang vừa ghi trong lượt Ch.4 cụm C: current-account-balance-equals-the-change-in-net-foreign-assets, trade-bias-is-measured-by-..., current-account-deficit-means-absorption-exceeds-national-income
- Ghi nợ vào _inbox.md: các trang công thức cũ (Ch.2/Ch.3) ghi trước quy ước này chưa được sửa

## [2026-09-16:08-47-16] ingest | imf_macro_accounting Ch.4 cụm D — tài khoản vốn/tài chính và nợ nước ngoài
- 8 trang mới: nguồn tài trợ CAB=FDI+NFB+ΔRES, chuỗi lựa chọn chính sách tài trợ thâm hụt, định nghĩa nợ gộp, phương trình động thái nợ (D_t=D_{t-1}+B_t-A_t), 3 tỷ số gánh nặng nợ, bền vững nợ nước ngoài (Box 4.9), FDI không tạo nợ (Box 4.10), động lực vốn chính phủ vs tư nhân
- Merge: functional-categories-of-the-financial-account, external-deficit-financing-is-limited-by-reserves-and-creditworthiness
- Còn lại Ch.4: cụm E (dự trữ và tài trợ, d.3939–4032) → cụm F (case Ba Lan, tuỳ minh chứng)

## [2026-09-16:08-52-23] ingest | imf_macro_accounting Ch.4 cụm E — dự trữ và tài trợ
- 6 trang mới: NFA hệ thống ngân hàng, dùng dự trữ tài trợ thâm hụt tạm thời, 4 rủi ro luồng vốn vào lớn (Box 4.11), dự trữ đủ phụ thuộc độ tin cậy chính sách (case Ba Lan 1991), công thức dự trữ/nhập khẩu, chỉ báo tổn thương tài chính sau Mexico 1994
- Merge: overall-balance-of-payments (định nghĩa đường chia trên/dưới vạch + cách tiếp cận tiền tệ), exceptional-financing-in-the-balance-of-payments (lý do xếp dưới vạch)
- Ch.4 cụm A–E xong. Còn cụm F (case Ba Lan BOP + tỷ giá zloty, d.4033–4076) — chỉ ingest nếu concept A–E còn thiếu minh chứng (§2)

## [2026-09-16:08-57-54] ingest | imf_macro_accounting Ch.4 cụm F — bỏ qua
- Bỏ qua case Ba Lan (BOP, tỷ giá zloty, d.4033–4076): tường thuật, concept A–E đã đủ minh chứng thực tế (case Ba Lan 1991 dự trữ, dữ liệu chuyển đổi), theo §2 ưu tiên lý luận trước tường thuật — người dùng chốt
- Ch.4 coi như xong toàn bộ (cụm A–E ingest, cụm F bỏ qua có ghi chú); index.md và 03_state cập nhật khớp

## [2026-09-16:08-57-54] schema | rà soát công thức/đồng nhất thức toàn wiki theo chuẩn $$...$$
- Sửa định dạng (không đổi nội dung/last_updated) cho 13 trang Ch.2–Ch.3 ghi trước quy ước: absorption, depreciation, gdp, gdp-deflator, gndi, gni, gross-national-saving, real-gdp, production-income-and-expenditure-approaches-yield-the-same-gdp, real-wage-growth-is-bounded-by-productivity-growth, the-saving-investment-gap-equals-the-current-account-balance, public-debt-dynamics-depend-on-the-primary-balance-seigniorage-and-the-interest-growth-gap, the-private-sector-resource-gap-must-be-financed-by-other-sectors, government-saving-investment-gap-approximates-the-overall-fiscal-deficit
- Sửa 1 trang Ch.4 (current-account-monitoring-depends-on-the-exchange-rate-regime)
- Xoá mục nợ tương ứng trong _inbox.md (đã xử lý xong). Hook --all sạch: 169 trang, 0 lỗi, 0 mồ côi

## [2026-09-16:09-16-27] review | Phân biệt đồng tiền định giá / đồng nội tệ trong cụm trang tỷ giá
Sửa 4 trang (unit-of-account-in-the-balance-of-payments, exchange-rate, current-account-monitoring-depends-on-the-exchange-rate-regime, overall-balance-of-payments) để nêu rõ CAB/ΔFI/ΔRES tính theo đồng tiền định giá (đơn vị BOP), không phải đồng nội tệ.
Quy ước ký hiệu $ (Box 5.8, Ch.5) chưa ingest nên chưa đưa vào; chỉ dựa trên d.3508 (Ch.4, đã ingest).

## [2026-09-16:09-26-16] ingest | Trích lẻ từ cụm F (Ch.4) và Ch.1: tốc độ trượt crawling peg, 5 bài học tỷ giá
1 trang mới: the-rate-of-crawl-under-a-crawling-peg-can-be-set-passively-or-actively (d.4067–4070).
Bổ sung bài học 2, 3, 5 (d.514–534, Ch.1) vào exchange-rate; cập nhật index.md và 03_state.

## [2026-09-16:09-39-53] ingest | Ch.5 — đọc toàn chương, tổ chức lại kế hoạch viết theo 4 trục
Đọc bài bản toàn Ch.5 (trừ Exercises). Thay bảng chunk tuần tự A–G bằng 4 batch viết theo chủ đề (W1 cấu trúc/đối tượng, W2 cân đối, W3 cơ chế, W4 đặc thù chuyển đổi + IMF).
Chưa ghi trang nào; 03_state/imf_macro_accounting.md ghi chi tiết dải dòng đã đọc và nội dung từng batch.

## [2026-09-16:09-48-03] ingest | imf_macro_accounting Ch.5 batch W1 — cấu trúc hệ thống tiền tệ
6 trang mới (3 tầng IFS, ngân hàng nhận tiền gửi, quy ước tồn kho/cơ sở tiền mặt, quy đổi tỷ giá cuối kỳ, hợp nhất khác tổng hợp, chức năng tiền, thang đo M1–L) + merge central-bank.
Stub mới: nonbank-financial-institutions, valuation-adjustments-...-of-stocks (link-forward cho W2). Còn W2, W3, W4.

## [2026-09-16:09-53-07] ingest | imf_macro_accounting Ch.5 batch W2 — đồng nhất thức tiền tệ và tỷ giá
7 trang mới (M2=NFA+NDC+OIN_b, liên kết khảo sát tiền tệ–BOP ΔNFA=CAB+ΔFI=-ΔRES, số nhân tiền, lý thuyết số lượng, cầu tiền, lý thuyết cầu tài sản, valuation adjustments Eₜ/VAd) + merge reserve-money + bổ sung real-interest-rate.
Cross-link ngược vào exchange-rate và current-account-monitoring-depends-on-the-exchange-rate-regime, đóng vòng đồng tiền định giá/nội tệ. Còn W3, W4.

## [2026-09-16:09-58-25] ingest | imf_macro_accounting Ch.5 batch W3 — cơ chế vận hành chính sách tiền tệ
7 trang mới: 5 công cụ điều tiết tiền cơ sở, kiểm soát không hoàn toàn, tỷ giá cố định/thả nổi và tự chủ tiền tệ, tiệt trùng + hội đồng tiền tệ, di chuyển vốn hoàn hảo, đô la hoá, đổi mới tài chính.
Cross-link vào real-interest-rate, monetizing-the-deficit-creates-high-powered-money-and-inflation. Còn W4.

## [2026-09-16:10-03-55] ingest | imf_macro_accounting Ch.5 batch W4 — kinh tế chuyển đổi + kỹ thuật IMF, hoàn tất Ch.5
7 trang mới: vòng quay tiền nhảy bậc, thiếu cạnh tranh ngân hàng/thị trường tài chính, nợ đọng liên doanh nghiệp, chính sách tiền tệ lệ thuộc ngân sách, quota/tranche/RPF, NPF=RPF-UFC=Q-H, case số liệu 4 bảng cân đối.
Case Ba Lan F2 (d.5136-5177) bỏ qua theo §2 (đã duyệt cùng batch). Ch.5 hoàn tất cả 4 batch W1-W4 (27 trang mới + 3 merge/bổ sung).

## [2026-09-16:10-19-43] ingest | imf_macro_accounting Ch.6 — flow of funds, hoàn tất chương
Đọc toàn chương (d.5588–5790), phần lớn nội dung ghép 7 cột bảng flow of funds vào các đồng nhất thức đã ingest ở Ch.2/3/4/5.
6 trang mới (cấu trúc ma trận, quy ước ghi sổ, bảng phân giải cột, phương pháp luận, twin deficits, cơ chế truyền dẫn thâm hụt) + 7 cross-link vào trang cũ. Exercises/bảng số liệu Ba Lan bỏ qua theo §2.

## [2026-09-16:10-30-48] ingest | imf_macro_accounting Ch.5 review — cấu trúc bảng cân đối thô
Đọc lại toàn bộ mục liên quan bảng cân đối trong Ch.5 và các trang wiki Ch.5/Ch.6 đã tạo.
3 trang mới: bảng cân đối thô Box 5.1 (nhà chức trách tiền tệ), Box 5.5 (DMB), quy ước ròng/gộp bất đối xứng giữa tín dụng chính phủ và DMB. Ch.6 không có nội dung bảng cân đối (chương flow, không phải stock).

## [2026-09-16:10-33-36] ingest | imf_macro_accounting rà soát toàn bộ Box Ch.5+Ch.6
Kiểm kê đầy đủ Box 5.1–5.10 và Box 6.1–6.4: tất cả đã có trong wiki, trừ Box 5.6/5.7 không trích xuất được từ nguồn (mất bảng khi OCR, không phải lỗ hổng ingest).
1 bổ sung: chi tiết dấu ở Box 6.3 (khoản vay nước ngoài ghi +200/-200 hai phía) vào trang cấu trúc ma trận flow of funds.

## [2026-09-16:10-40-29] ingest | imf_macro_accounting rà soát toàn bộ Table Ch.5+Ch.6
Table 5.1–5.7 và Table 6.2–6.6 (số liệu Ba Lan/Transitia) nằm trong Exercises đã bỏ qua theo §2; phần số liệu Table 6.6 bị lỗi OCR nặng nên không trích số.
1 trang mới từ chú thích Table 6.6 (rõ, không lỗi): cách dung hoà số liệu GFS/NIPA/BOP/tiền tệ khi dựng bảng flow of funds thật, minh chứng cụ thể cho quy ước chọn nguồn đã có.

## [2026-09-16:11-05-53] ingest | imf_macro_accounting Ch.5 bổ sung Box 5.2/5.6 + công thức 5.3–5.5
Tạo 2 trang mới: `the-analytical-monetary-authorities-balance-sheet-groups-items-into-nfa-nda-and-rm` (Box 5.2), `the-analytical-deposit-money-bank-balance-sheet-separates-required-from-excess-reserves` (Box 5.6). Cập nhật `reserve-money` (công thức 5.3, 5.4), `money-supply-equals-net-foreign-assets-plus-net-domestic-assets` (công thức 5.5 + 2 công thức tăng trưởng M2 không đánh số), cùng 3 trang liên quan (link ngược).
Đính chính ghi chú review trước đó về Box 5.6 (OCR không phải lỗ hổng thật) trong `03_state/imf_macro_accounting.md`. Box 5.7 xác nhận không có bảng T-account riêng trong nguồn.

## [2026-09-16:14-06-43] schema | thành phần có tên kinh tế riêng phải có trang wiki riêng (§5 amendment)
Người dùng chốt qua Box 2.1: mọi thành phần trong đồng nhất thức/bảng cân đối/box có tên kinh tế thật phải tách trang riêng, áp dụng hồi tố toàn wiki. Chi tiết: `00_schema.md` §5, `decisions.md`.
Batch 1 (Ch.2, Box 2.1): 11 trang mới + nâng `net-exports` stub→draft + link ngược 6 trang liên quan (gni, gndi, depreciation, final-consumption, production-income-expenditure). Ch.3–Ch.6 còn nợ, sẽ làm ở các lượt sau.

## [2026-09-16:07-21-14] ingest | backfill §5 Ch.3 — thành phần có tên kinh tế riêng (Batch 2)
Áp chính sách §5 (2026-09-16) hồi tố cho Ch.3 (tài khoá/GFS). 8 trang mới: `inflation-tax`, `pure-seigniorage` (phân rã seigniorage Box 3.1); `current-fiscal-deficit` (định nghĩa noun-phrase); `primary-gap`, `medium-term-tax-gap` (Box 3.4); `wages-and-salaries-expenditure`, `government-goods-and-services-expenditure`, `government-capital-expenditure` (4 hạng mục chi tiêu công). Cập nhật link ngược 5 trang liên quan + `index.md` + `03_state/imf_macro_accounting.md`. Quyết định phạm vi (không tách trang): 8 chỉ số Tanzi (Box 3.5), 3 thành phần lưới an sinh (Box 3.6), 3 loại bán tài khoá (Box 3.7) — liệt kê định tính, giữ nguyên trong trang đã có; $NFB_g$/$\Delta NDC_g$/$NB$, $S_g$/$I_g$ — đã có trang cơ chế tương ứng hoặc là ứng dụng khái niệm chung, không tạo trùng lặp. Hook `validate_wiki_page.py --all`: 230 trang, 0 vấn đề, 0 mồ côi.

## [2026-09-16:07-36-16] ingest | backfill §5 Ch.4 — thành phần có tên kinh tế riêng (Batch 3)
Áp chính sách §5 (2026-09-16) hồi tố cho Ch.4 (BOP), đọc lại Box 4.3 (bảng phân loại chuẩn, trước đây coi là "số liệu thô" và bỏ qua — thực ra là bảng cấu trúc có tên hạng mục). 7 trang mới: `goods-in-the-balance-of-payments`, `services-in-the-balance-of-payments`, `income-in-the-balance-of-payments` (tài khoản vãng lai); `capital-account-in-the-balance-of-payments`; `direct-investment`, `portfolio-investment`, `other-investment` (tài khoản tài chính). Cập nhật link ngược 5 trang + `index.md` + `03_state/imf_macro_accounting.md`. Quyết định phạm vi (không tách trang): 4 kỹ thuật exceptional financing (Box 4.4) và các khoản mục con của reserve assets — liệt kê định tính trong trang hub đã có. Hook `validate_wiki_page.py --all`: 237 trang, 0 vấn đề, 0 mồ côi.

## [2026-09-16:07-42-59] ingest | backfill §5 Ch.5 — thành phần có tên kinh tế riêng (Batch 4)
Rà lại bảng cân đối MA/DMB (Box 5.1/5.2/5.5/5.6) và công thức số nhân tiền để tìm khoản mục có tên kinh tế riêng + đủ nội dung phân tích tách trang. 3 trang mới: `required-reserves`, `excess-reserves` (dòng "Dự trữ" trên bảng phân tích DMB, số hạng r/r_d/r_t/r_e trong công thức số nhân tiền); `quasi-money` (QM, số hạng TD trong M2). Cập nhật link ngược 7 trang + `index.md` + `03_state`. Quyết định phạm vi: các khoản mục chi tiết còn lại của Box 5.1/5.2/5.5/5.6 (vàng, SDR, tín phiếu, tiền gửi theo công cụ...) không có elaboration riêng trong nguồn ngoài việc được nêu tên — giữ nguyên liệt kê trong 4 trang bảng cân đối đã có, không tách trang, cùng logic đã áp cho Box 3.5–3.7 (Ch.3) và reserve-assets sub-items (Ch.4). Ch.5 xong; Ch.6 (flow of funds) là chương cuối còn lại. Hook `validate_wiki_page.py --all`: 240 trang, 0 vấn đề, 0 mồ côi.

## [2026-09-16:07-44-33] review | backfill §5 Ch.6 — rà soát, không tạo trang mới (Batch 5, hoàn tất kế hoạch)
Đọc lại toàn bộ cấu trúc bảng flow of funds (7 cột, Box 6.1–6.4, Table 6.1) theo chính sách §5 (thành phần có tên kinh tế riêng phải có trang riêng). Kết luận: không có khoản mục mới cần tách trang — Ch.6 chỉ xếp lại các đồng nhất thức đã ingest từ Ch.2–5 vào một ma trận cột-khu vực, không tự tạo khoản mục mới; "twin deficits" (Box 6.1) đã có trang từ trước. Ghi rõ vào `03_state/imf_macro_accounting.md` để phân biệt "đã rà soát, không có gì" với "chưa rà soát". **Kế hoạch backfill §5 hoàn tất cho toàn bộ phạm vi đã ingest (Ch.2–Ch.6):** tổng cộng 5 batch, 26 trang mới (Ch.2: 11 + nâng 1 stub→draft, Ch.3: 8, Ch.4: 7, Ch.5: 3, Ch.6: 0).
