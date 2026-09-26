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

## [2026-09-16:22-14-49] lint | 240 trang
- Bước 0 sạch; Conflict 2 (hoãn); Atomic 1 (exchange-rate); title 3; nợ stub 3/3; khái niệm chưa có trang 9; 4 cặp SNA–BOP thiếu link; OCR/mồ côi/link chết/inbox 0
- Đủ điều kiện stable: 188 trang (0 đã review); 46 trang draft backlink < 2
- Báo cáo: Claude outputs/lint-2026-09-16-240.md

## [2026-09-16:22-21-29] schema | xử lý lint 240 trang — đổi tên 4 trang
- analyzing-changes-in-the-structure-of-trade → trade-data-by-commodity-and-partner-separates-structural-from-temporary-trade-shocks; assessing-the-appropriateness-of-the-exchange-rate → exchange-rate-appropriateness-is-judged-by-four-indicator-groups-none-sufficient-alone
- macroeconomic-sectors → sectoral-interactions; the-1993-sna-added-balance-sheets-and-fuller-income-accounts → the-1993-sna-revised-the-1968-system-in-five-ways
- 11 link + index cập nhật, không nâng last_updated; --all sạch

## [2026-09-16:22-23-41] promote | 188 trang lên stable
- Danh sách "Đủ điều kiện stable" của lint 240 trang, người dùng duyệt và chọn bỏ qua /review; Ch.2 71 · Ch.3 60 · Ch.4 27 · Ch.5 26 · Ch.6 4 (chi tiết: Claude outputs/lint-2026-09-16-240.md §9)
- Loại: 0 (kiểm lại điều kiện ngay trước khi ghi; the-1993-sna-… theo tên mới)
- --all sạch trước và sau; không đổi last_updated, không đặt reviewed

## [2026-09-16:22-31-41] ingest | imf_macro_accounting — xử lý lint 240 trang, lượt A (đa chương)
- 5 trang mới: case tỷ giá Ba Lan (tách từ exchange-rate), real-exchange-rate, monetary-policy, fiscal-policy, international-monetary-fund-imf; nâng 3 stub lên draft: sectoral-interactions, soft-budget-constraint, nonbank-financial-institutions; exchange-rate bỏ đoạn Ba Lan
- Chèn 7 link từ trang cũ tới trang mới (không nâng last_updated); index + 03_state + decisions cập nhật; --all sạch (245 trang)
- Còn lại: lượt B (thành phần tiền tệ Ch.5), C (dự trữ/IMF/tài trợ đặc biệt), D (Box 3.5–3.7)

## [2026-09-16:22-35-56] ingest | imf_macro_accounting Ch.5 — xử lý lint 240 trang, lượt B (thành phần tiền tệ §5)
- 10 trang mới: currency-in-circulation, demand-deposits, narrow-money-m1, net-domestic-assets, net-domestic-credit, net-credit-to-government, credit-to-the-private-sector, claims-on-deposit-money-banks, other-items-net, foreign-currency-deposits
- Chèn 16 link từ trang cũ (không nâng last_updated); index + 03_state cập nhật; --all sạch (255 trang)
- Còn lại: lượt C (dự trữ/IMF/tài trợ đặc biệt), lượt D (Box 3.5–3.7)

## [2026-09-16:22-39-53] ingest | imf_macro_accounting Ch.4–5 — xử lý lint 240 trang, lượt C (dự trữ, IMF, tài trợ đặc biệt §5)
- 11 trang mới: foreign-exchange-reserve-assets, monetary-gold, special-drawing-rights-sdr, reserve-position-in-the-imf, use-of-imf-credit, government-deposits, treasury-bills, debt-rescheduling, arrears-on-external-debt-servicing, debt-forgiveness, debt-equity-swaps
- Chèn 16 link từ trang cũ (không nâng last_updated); index + 03_state cập nhật; --all sạch (266 trang)
- Còn lại: lượt D (Box 3.5 Tanzi, 3.6 lưới an sinh, 3.7 bán tài khoá)

## [2026-09-16:22-44-45] ingest | imf_macro_accounting Ch.3 — xử lý lint 240 trang, lượt D (Box 3.5–3.7 §5)
- 14 trang mới: 8 chỉ số Tanzi; targeted-commodity-subsidies-and-cash-compensation, social-security-arrangements, unemployment-benefits-and-public-works; exchange-rate-subsidies, credit-subsidies, exchange-rate-guarantees-and-other-contingent-liabilities
- Chèn 15 link từ trang cũ (không nâng last_updated); trích lẻ d.2551, d.2590–2596 từ chunk bối cảnh Ba Lan; index + 03_state cập nhật; --all sạch (280 trang)
- Còn lại: lượt E (hình thức trợ cấp)

## [2026-09-16:22-46-15] ingest | imf_macro_accounting Ch.3 — xử lý lint 240 trang, lượt E (hình thức trợ cấp §5)
- 6 trang mới: cash-grant-subsidies, tax-subsidies, in-kind-subsidies, procurement-subsidies, regulatory-subsidies, implicit-subsidies; tanzi-erosion-index thêm ví dụ thuế doanh thu Ba Lan (d.2571–2573)
- Chèn 9 link từ trang cũ (không nâng last_updated); index + 03_state cập nhật; --all sạch (286 trang)
- Kế hoạch tách trang thành phần §5 không ngoại lệ hoàn tất

## [2026-09-16:22-50-46] lint | 286 trang
- Bước 0 sạch; Conflict 2 (hoãn); Atomic 1 (case tỷ giá Ba Lan); trùng lặp một phần 1 (subsidies/implicit-subsidies); khái niệm chưa có trang 4; title/stub/OCR/inbox/mồ côi/link chết 0
- Đủ điều kiện stable: 53 trang (0 đã review); 41 trang draft backlink < 2
- Báo cáo: Claude outputs/lint-2026-09-16-286.md

## [2026-09-16:22-55-15] ingest | imf_macro_accounting — xử lý lint 286 trang (tách trang, bỏ trùng)
- Tách 5 bài học chính sách khỏi case tỷ giá Ba Lan thành polands-exchange-rate-experience-yields-five-policy-lessons (Ch.1 d.514–534); exchange-rate cập nhật link
- subsidies: rút đoạn trợ cấp ngầm còn 1 câu + link implicit-subsidies; stable → draft, last_updated 2026-09-16
- index cập nhật; --all sạch (287 trang)

## [2026-09-16:22-55-16] promote | 53 trang lên stable
- Danh sách "Đủ điều kiện stable" của lint 286 trang; người dùng duyệt, bỏ qua /review (38 trang mới từ lượt A–E)
- Loại: 0; --all sạch trước và sau; hiện 240 stable / 47 draft

## [2026-09-16:22-58-04] ingest | imf_macro_accounting Ch.2/4/5 — xử lý lint 286 trang, 5 khái niệm mới
- 5 trang mới: exchange-rate-regimes, devaluation, foreign-exchange-intervention, open-market-operations, discount-window
- Chèn 13 link từ trang cũ (không nâng last_updated); index + 03_state cập nhật; --all sạch (292 trang)
- Công cụ trực tiếp thứ 4, 5 đã có trang (monetizing-the-deficit-…, required-reserves)

## [2026-09-16:23-00-01] lint | 292 trang
- Bước 0 sạch; Conflict 2 (hoãn); khái niệm chưa có trang 3; Atomic/title/trùng lặp/stub/OCR/inbox/mồ côi/link chết 0
- Đủ điều kiện stable: 12 trang (0 đã review); 38 trang draft backlink < 2
- Báo cáo: Claude outputs/lint-2026-09-16-292.md

## [2026-09-16:23-01-21] promote | 12 trang lên stable
- Danh sách "Đủ điều kiện stable" của lint 292 trang; người dùng duyệt, bỏ qua /review
- Loại: 0; --all sạch trước và sau; hiện 252 stable / 40 draft

## [2026-09-16:23-04-25] ingest | imf_macro_accounting Ch.3–6 — xử lý lint 292 trang, 3 khái niệm mới
- 3 trang mới: capital-flight, financial-programming, currency-board
- Chèn 9 link từ trang cũ (không nâng last_updated); index + 03_state cập nhật; --all sạch (295 trang)

## [2026-09-17:18-07-56] repo | reset main về 38d3381 (bản cuối ngày 2026-09-16)
- Bỏ khỏi local 9 commit ngày 2026-09-17 (6287ec9 → b1ba033: audit skill, ingest Bindseil + Capitalism and Freedom, trường school); vẫn còn trong reflog
- Wiki về 295 trang, 03_state còn 2 file; origin/main (9c7daaa) chưa đổi — local behind 6

## [2026-09-17:19-08-08] schema | batch audit v2 (cấu trúc + skill)
- Skill review → review-node (sửa YAML); ingest/lint/promote/query sửa theo B2–B13, áp writing-style; agents.md gộp vào CLAUDE.md; schema 30 → 21 KB, lý do dời sang decisions.md
- Hook thêm --backlinks/--ocr/--stub-debt/--inbox-debt/--verify-sources/--now, nguồn dài đọc từ bản kê; bản kê + index §Sources đủ 10 nguồn; 03_state/fixed_income_during.md
- 01_sources: file OCR IMF khôi phục CRLF (khớp SHA), _source_note.md chuyển ra và xoá (người dùng duyệt); --all sạch 295 trang, --verify-sources 0 lệch

## [2026-09-17:19-08-08] repo | commit batch audit v2
- Đính chính mục repo trước: origin/main đã được force-push về 812200a, không còn 9c7daaa; các commit ngày 2026-09-17 chỉ còn trong reflog cục bộ
- Commit cục bộ, chưa push

## [2026-09-17:19-23-19] schema | evals vòng 1 cho query và review-node
- Thêm .claude/skills/{query,review-node}/evals/evals.json (5 prompt, assertion kiểm được bằng script); chạy trên bản sao, wiki thật không đổi
- Pass rate bản mới 100% so với bản cũ 92%; kết quả: Claude outputs/eval-review-query-review-node-iter1.html
- Hook: không in traceback khi pipe bị đóng sớm (--backlinks | head)

## [2026-09-17:19-37-25] review | 1 trang
- Đã sửa: reserve-money (stable → draft, reviewed_by: model), áp bản đối chiếu của eval vòng 1 sau khi kiểm lại nguồn d.4584–4675
- Claim sai: "ghi gộp" gắn nhầm CPS* (thuộc CDMB*); CPS* thiếu phạm vi (d.4614); "bốn" → năm khoản mục (5.1); phép phân rã 5.3–5.4 bị gán cho financial programming (bỏ link); chú thích định nghĩa RM d.4593–4609 → d.4618
- Giữ lại: không; _inbox thêm 1 mục cho chú thích sai ở central-bank

## [2026-09-17:23-52-03] schema | tối ưu description query + review-node
- review-node: thêm bước ghi _inbox khi trang khác mắc cùng lỗi; description viết lại theo ý định "check trang với nguồn" (trigger 15/20 → 19/20 trên bộ 20 câu, 3 lượt/câu)
- query: description thêm ý "tìm, liệt kê các trang về một khái niệm" (19/20 → 20/20)
- Bộ câu test ở máy cloud, chưa lưu vào repo

## [2026-09-18:23-02-43] schema | thêm công cụ ghi câu hỏi theo yêu cầu
- Chính thức hoá `.claude/tools/log_questions.py`: chạy thủ công, phân loại bằng rule cục bộ, deduplicate và append JSONL
- Dữ liệu mặc định: `.claude/local/question-logger/questions.jsonl`; không gọi LLM

## [2026-09-18:23-13-37] schema | mở rộng question logger ra toàn dự án
- Không truyền `--input`: quét toàn bộ Codex session có `cwd` hoặc workspace root thuộc repo hiện tại; vẫn giữ chế độ một file
- Lần chạy đầu toàn dự án: 22 chat, 157 prompt; lần chạy lại ghi thêm 0 record

## [2026-09-21:18-48-48] ingest | bindseil_monetary_policy Introduction + Ch.1–2
- Tạo 7 trang mới (separation-principle, operational-target, monetary-policy-instruments-three-tools, central-bank-financial-accounts-model, relative-vs-absolute-intermediation, collateral-constraint, autonomous-factors, liquidity-deficit-banking-system); merge Bindseil vào 3 trang stable (monetary-policy, open-market-operations, discount-window → draft)
- Dựng 03_state/bindseil_monetary_policy.md với bản đồ chunk đầy đủ (17 chunk)
- Còn lại: Ch.3–18 (chi tiết ở state file)

## [2026-09-21:18-53-09] ingest | bindseil_monetary_policy Ch.3
- 2 trang mới: overnight-rate-is-the-natural-operational-target-of-monetary-policy, reserve-position-doctrine-rise-and-fall-at-the-fed
- Merge Ch.3 §3.1 taxonomy (explicit/implicit, quantity/rate, one/many) vào operational-target-of-monetary-policy
- Còn lại: Ch.4–18

## [2026-09-21:18-57-27] ingest | bindseil_monetary_policy Ch.4
- 3 trang mới: three-techniques-to-control-short-term-interest-rates (hub), one-directional-standing-facility-monetary-policy, interest-rate-corridor-symmetric-approach
- Còn lại: Ch.5–18

## [2026-09-21:19-01-55] ingest | bindseil_monetary_policy Ch.5
- 1 trang mới: martingale-property-of-overnight-rates-and-reserve-averaging
- Link từ three-techniques-to-control-short-term-interest-rates sang trang martingale
- Còn lại: Ch.6–18

## [2026-09-21:19-05-18] ingest | bindseil_monetary_policy Ch.6
- 3 trang mới: standing-facilities-in-monetary-policy-operations, optimal-width-of-the-interest-rate-corridor, taralac-facility-target-rate-limited-access
- Cập nhật cross-links tại: discount-window, monetary-policy-instruments-three-tools, interest-rate-corridor-symmetric-approach, three-techniques-to-control-short-term-interest-rates
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.7–18

## [2026-09-21:19-07-06] ingest | bindseil_monetary_policy Ch.7
- 3 trang mới: outright-vs-credit-open-market-operations, tender-procedures-for-credit-open-market-operations, liquidity-absorbing-open-market-operations
- Làm giàu trang open-market-operations với góc nhìn lịch sử và phân loại của Bindseil Ch.7
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.8–18

## [2026-09-21:19-09-02] ingest | bindseil_monetary_policy Ch.8
- 2 trang mới: functions-of-reserve-requirements-in-monetary-policy, reserve-requirement-system-specifications-and-averaging
- Làm giàu trang required-reserves (chuyển sang draft, thêm nguồn bindseil, giải cấu trúc số nhân tiền tệ và phân tích chi phí tín dụng/hạn chế collateral)
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.9–18

## [2026-09-21:19-11-06] ingest | bindseil_monetary_policy Ch.9
- 3 trang mới: central-bank-collateral-framework-design-and-risk-control, market-impact-of-collateral-framework-and-leverage-constraints, collateral-pool-segregation-and-double-adverse-selection
- Làm giàu trang collateral-constraint-on-central-bank-credit với công thức CVPH, hàm haircut luỹ thừa và lý do khan hiếm tài sản thế chấp tất yếu
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.10–18

## [2026-09-21:19-12-48] ingest | bindseil_monetary_policy Ch.10
- 2 trang mới: optimal-monetary-policy-operations-frameworks-in-normal-times (hub), comparative-central-bank-operational-frameworks-normal-times
- Kết nối separation-principle-of-monetary-policy với khuôn khổ tối ưu trong thời bình
- Hoàn thành toàn bộ Phần I (Part I: Monetary Policy Operations in Normal Times, Ch.1–10) của Bindseil
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.11–18 (Phần II: Khủng hoảng thanh khoản và người cho vay cuối cùng)

## [2026-09-21:19-37-00] ingest | bindseil_monetary_policy Ch.11
- 3 trang mới: mechanics-of-liquidity-crises-and-feedback-loops, bank-runs-investor-strikes-and-multiple-equilibria, monetary-policy-transmission-breakdown-and-zero-lower-bound
- Bổ sung đứt gãy truyền dẫn, quy tắc Wicksell mở rộng R = i + j + k và ma trận mục tiêu đa chiều (I*, Q*) vào separation-principle-of-monetary-policy và operational-target-of-monetary-policy; bổ sung stigma và nghịch lý minh bạch vào discount-window
- Mở đầu Phần II (Part II: Monetary Policy Operations in Times of Crisis and the LOLR); wiki đạt 325 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.12–18

## [2026-09-21:19-39-00] ingest | bindseil_monetary_policy Ch.12
- 4 trang mới: collateral-scarcity-and-effective-term-funding-costs, effective-corridor-asymmetry-and-stigma-in-overnight-rates, asset-encumbrance-and-subordination-of-unsecured-creditors, securities-lending-programmes-and-central-bank-collateral-swaps
- Bổ sung phân tích phá vỡ tính đối xứng do rủi ro cạn kiệt collateral và stigma vào interest-rate-corridor-symmetric-approach; bổ sung các kênh tác động Ch.12 vào collateral-constraint-on-central-bank-credit
- Wiki đạt 329 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.13–18

## [2026-09-21:19-41-00] ingest | bindseil_monetary_policy Ch.13
- 4 trang mới: narrowing-interest-rate-corridor-and-absolute-central-bank-intermediation, fixed-rate-full-allotment-and-maturity-lengthening-in-crisis, seven-channels-of-central-bank-asset-purchase-programmes, dangers-of-ultra-accommodating-monetary-policy-and-the-wicksellian-counter-defense
- Bổ sung vai trò thu hẹp hành lang trong khủng hoảng vào optimal-width-of-the-interest-rate-corridor; bổ sung trung gian tuyệt đối và hình thái bảng cân đối vào relative-vs-absolute-central-bank-intermediation; bổ sung chuyển đổi OMOs khủng hoảng vào open-market-operations
- Wiki đạt 333 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.14–18

## [2026-09-21:19-44-00] ingest | bindseil_monetary_policy Ch.14
- 3 trang mới: lender-of-last-resort-foundations-and-bagehot-principles, central-bank-inertia-and-active-crisis-lolr-measures, emergency-liquidity-assistance-framework-and-constructive-ambiguity
- Bổ sung phân định standing facility vs ELA vào standing-facilities-in-monetary-policy-operations; bổ sung các kênh LOLR và ELA vào discount-window
- Wiki đạt 336 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.15–18

## [2026-09-21:19-46-00] ingest | bindseil_monetary_policy Ch.15
- 3 trang mới: central-bank-risk-taking-and-liquidity-support-trade-off, endogenous-risk-and-upward-sloping-haircut-loss-curve, bindseil-jablecki-risk-endogeneity-and-two-errors-model
- Làm giàu trang central-bank-collateral-framework-design-and-risk-control với cơ chế tính nội sinh của rủi ro và hàm mục tiêu hai sai lầm
- Wiki đạt 339 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.16–18

## [2026-09-21:19-49-00] ingest | bindseil_monetary_policy Ch.16
- 3 trang mới: lender-of-last-resort-moral-hazard-and-liquidity-externalities, liquidity-regulation-and-central-bank-operations-arbitrage, surcharges-for-over-proportional-reliance-on-the-central-bank
- Bổ sung rủi ro đạo đức và quy định thanh khoản vào lender-of-last-resort-foundations-and-bagehot-principles; bổ sung kinh doanh chênh lệch pháp lý LCR vào relative-vs-absolute-central-bank-intermediation
- Wiki đạt 342 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.17–18

## [2026-09-21:19-52-00] ingest | bindseil_monetary_policy Ch.17
- 3 trang mới: international-lender-of-last-resort-and-dual-liquidity-crises, central-bank-fx-swap-lines-and-cross-border-liquidity, target2-balances-and-balance-of-payments-mechanics
- Làm giàu trang international-monetary-fund-imf với vai trò định chế neo giữ ILOLR hóa giải rủi ro đạo đức và rủi ro tín dụng đối ngoại
- Wiki đạt 345 trang, 0 lỗi, 0 mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md
- Còn lại: Ch.18 (kết thúc nguồn sách)

## [2026-09-21:19-54-00] ingest | bindseil_monetary_policy Ch.18 (Hoàn tất toàn bộ nguồn sách)
- 2 trang mới: optimal-monetary-policy-operations-frameworks-in-crisis-times (hub tổng hợp toàn bộ Phần II Khủng hoảng), exit-strategies-from-non-conventional-monetary-policy
- Làm giàu trang optimal-monetary-policy-operations-frameworks-in-normal-times và liquidity-absorbing-open-market-operations
- Hoàn tất 100% việc tiếp nhận toàn bộ cuốn sách Ulrich Bindseil (2014, 4.474 dòng, 18 chương)
- Toàn bộ wiki đạt 347 trang, 0 trang lỗi, 0 trang mồ côi
- Cập nhật index.md và state file bindseil_monetary_policy.md

## [2026-09-21:20-18-50] ingest | cargill_central_bank_policy Ch.1 — The Financial and Monetary Regime
- 9 trang mới: financial-and-monetary-regime, real-and-financial-sectors-interact-..., potential-gdp-..., gdp-gap-..., natural-rate-of-unemployment-..., u6-unemployment-rate-..., okuns-law-..., a-well-functioning-financial-..., government-policy-failure-...; cập nhật liên kết 6 trang cũ
- Khởi dựng 03_state/cargill_central_bank_policy.md (17 chương); cập nhật _sources_manifest.md và index.md §Sources; wiki đạt 356 trang, 0 lỗi, 0 mồ côi
- Còn lại: Ch.2–17

## [2026-09-21:20-26-30] ingest | cargill_central_bank_policy Ch.2 — Basic Concepts Regarding Money
- 8 trang mới: money-is-a-market-innovation-..., money-is-the-only-one-hundred-percent-liquid-asset, credit-cards-are-liabilities-..., consumer-price-index-has-four-sources-of-upward-bias, cpi-upward-bias-expands-government-deficits-..., monetary-standards-evolved-..., modern-monetary-system-functions-as-an-inverted-pyramid, money-is-non-neutral-...
- Cập nhật 5 trang: money-serves-as-a-medium-..., the-quantity-theory-..., cpi, narrow-money-m1, quasi-money; cập nhật state file và index.md; wiki đạt 364 trang, 0 lỗi, 0 mồ côi; còn lại Ch.3–17

## [2026-09-21:20-32-59] ingest | cargill_central_bank_policy Ch.3 — The Financial System and Flow of Funds
- 6 trang mới: flow-of-funds-fundamental-equation-..., economic-sectors-are-classified-..., financial-system-transfers-funds-..., direct-financial-markets-fail-small-participants-..., financial-markets-are-divided-into-money-markets-..., financial-institutions-operate-as-balanced-budget-...
- Cập nhật 4 trang: deposit-money-banks, nonbank-financial-institutions, the-flow-of-funds-table-is-a-zero-sum-..., financial-and-monetary-regime; cập nhật state file và index.md; wiki đạt 370 trang, 0 lỗi, 0 mồ côi; còn lại Ch.4–17

## [2026-09-21:20-41-30] ingest | cargill_central_bank_policy Ch.4 — Interest Rates in the Financial System
- 6 trang mới: interest-rate-connects-the-present-..., interest-rates-in-indirect-finance-..., interest-rate-ceilings-distort-credit-..., yield-to-maturity-equates-present-value-..., discount-yield-understates-the-true-return-..., interest-rate-risk-increases-with-maturity-...
- Cập nhật 4 trang: real-and-financial-sectors-interact-..., financial-system-transfers-funds-..., government-policy-failure-..., financial-markets-are-divided-into-money-markets-...; cập nhật state file và index.md; wiki đạt 376 trang, 0 lỗi, 0 mồ côi; còn lại Ch.5–17

## [2026-09-21:20-47-47] ingest | cargill_central_bank_policy Ch.5 — The Level of Interest Rates
- 7 trang mới: loanable-funds-framework-..., interest-rates-move-procyclically-..., debt-monetization-creates-conflict-..., fisher-effect-shifts-nominal-..., expected-inflation-is-measured-..., negative-interest-rates-distort-..., monetary-expansion-lowers-interest-rates-...
- Cập nhật 5 trang: real-interest-rate, crowding-out, monetizing-the-deficit-..., real-and-financial-sectors-interact-..., monetary-policy-transmission-breakdown-...; cập nhật state file và index.md; wiki đạt 383 trang, 0 lỗi, 0 mồ côi; còn lại Ch.6–17

## [2026-09-21:20-54-13] ingest | cargill_central_bank_policy Ch.6 — The Structure of Interest Rates
- 8 trang mới: interest-rate-structure-is-determined-..., default-risk-premium-widens-..., liquidity-premium-compensates-..., tax-exemption-lowers-municipal-..., pure-expectations-hypothesis-..., liquidity-premium-hypothesis-..., segmented-markets-hypothesis-..., yield-curve-functions-as-a-rorschach-...
- Cập nhật 5 trang: loanable-funds-framework-..., interest-rate-risk-increases-..., financial-markets-are-divided-into-money-markets-..., fisher-effect-shifts-nominal-..., interest-rates-move-procyclically-...; cập nhật state file và index.md; wiki đạt 391 trang, 0 lỗi, 0 mồ côi; còn lại Ch.7–17

## [2026-09-21:21-04-47] ingest | cargill_central_bank_policy Ch.7–9 — International Dimensions, Role of Government, Regulation & Supervision
- 13 trang mới: statement-of-international-transactions-..., exchange-rate-determination-balances-..., real-interest-rate-increases-appreciate-..., internal-external-balance-links-..., greshams-law-and-uniform-coinage-..., government-safety-net-solves-..., government-credit-allocation-subsidies-..., public-choice-theory-explains-..., supervision-differs-from-regulation-..., prompt-corrective-action-establishes-..., risk-based-capital-requirements-aim-..., supervisory-stress-testing-provides-..., macroprudential-regulation-bridges-...
- Cập nhật 5 trang: central-bank, government-policy-failure-..., financial-and-monetary-regime, lender-of-last-resort-foundations-..., exchange-rate-regimes; cập nhật state file và index.md; wiki đạt 404 trang, 0 lỗi, 0 mồ côi; còn lại Ch.10–17

## [2026-09-21:22-53-06] lint | 404 trang
- 0 lỗi schema/mồ côi/link chết, 2 conflict tồn đọng, 0 nợ stub, 0 nợ inbox, 11 khái niệm đề xuất tạo stub
- 120 trang draft đủ điều kiện lên stable (outlink >= 1, backlink >= 2, không conflict)
- Báo cáo chi tiết: Claude outputs/lint-2026-09-21-404.md

## [2026-09-21:23-03-55] ingest | tạo 11 stub từ kết quả lint 404 trang
- Tạo 11 stub concept: money-supply, foreign-exchange-reserves, repurchase-agreement, moral-hazard, yield-curve, deflation, sterilization, non-performing-loans, currency-swap, quantitative-easing, credit-spread
- Cập nhật liên kết từ 14 trang liên quan và bổ sung vào index.md; wiki đạt 415 trang, 0 lỗi, 0 mồ côi

## [2026-09-22:21-07-15] ingest | cargill_central_bank_policy Ch.10 — A Short History of the U.S. Financial and Monetary Regime in Transition
- 4 trang mới: regulatory-market-dialectic-drives-financial-regime-evolution, dual-banking-system-emerged-as-a-market-innovation-around-taxation, savings-and-loan-collapse-manifested-interest-rate-risk-and-disintermediation, us-financial-deregulation-eliminated-great-depression-era-competitive-barriers; cập nhật 3 trang
- Cập nhật 03_state/cargill_central_bank_policy.md và 02_wiki/index.md; wiki đạt 419 trang, 0 lỗi, 0 mồ côi
- Còn lại: Ch.11–17 (cargill_central_bank_policy)

## [2026-09-22:21-21-03] ingest | cargill_central_bank_policy Ch.11 — The Five Steps and Step 1: Institutional Design
- 5 trang mới: five-step-framework-structures-central-bank-policy-analysis, central-banks-are-necessarily-public-institutions-despite-private-ownership-fictions, de-jure-central-bank-independence-diverges-from-de-facto-policy-autonomy, central-bank-transparency-anchors-public-expectations-across-five-dimensions, institutional-structure-of-the-federal-reserve-concentrates-power-in-the-board-and-fomc
- Cập nhật 3 trang: central-bank, debt-monetization-creates-conflict-between-fiscal-deficits-and-central-bank-independence, public-choice-theory-explains-regulatory-capture-and-monetary-politicization
- Cập nhật 03_state/cargill_central_bank_policy.md và 02_wiki/index.md; wiki đạt 424 trang, 0 lỗi, 0 mồ côi; còn lại Ch.12–17

## [2026-09-22:21-25-51] ingest | cargill_central_bank_policy Ch.12 — Central Banks, Base Money and the Money Supply
- 5 trang mới: central-banks-create-base-money-out-of-thin-air-through-open-market-operations, money-supply-expansion-stops-when-absorbing-factors-exhaust-high-powered-money, currency-deposit-ratio-reflects-opportunity-costs-and-underground-economy-incentives, central-bank-controls-the-monetary-base-but-cannot-predictably-control-the-money-supply, money-multiplier-collapsed-post-2008-due-to-interest-on-excess-reserves-and-bank-risk-aversion
- Cập nhật 3 trang: the-money-multiplier-links-reserve-money-to-the-money-supply, modern-monetary-system-functions-as-an-inverted-pyramid, autonomous-factors-of-central-bank-balance-sheet
- Cập nhật 03_state/cargill_central_bank_policy.md và 02_wiki/index.md; wiki đạt 429 trang, 0 lỗi, 0 mồ côi; còn lại Ch.13–17

## [2026-09-22:21-31-49] ingest | cargill_central_bank_policy Ch.13 — Tools of Monetary Policy and Policy Instruments
- 4 trang mới: selective-credit-controls-decayed-due-to-fungibility-and-regulatory-circumvention, forward-guidance-evolved-from-moral-suasion-as-conditional-transparent-commitment, central-banks-cannot-simultaneously-target-money-supply-and-interest-rates, interest-rate-targeting-dominates-monetary-aggregates-due-to-measurement-and-control-limits
- Cập nhật 4 trang: open-market-operations, loanable-funds-framework-determines-equilibrium-interest-rate-and-bond-price, central-bank-transparency-anchors-public-expectations-across-five-dimensions, us-financial-deregulation-eliminated-great-depression-era-competitive-barriers
## [2026-09-22:21-38-52] ingest | cargill_central_bank_policy Ch.14 — Step 4: The Central Bank Model of the Economy
- 4 trang mới: macroeconomic-models-provide-road-map-for-central-bank-policy-transmission, natural-rate-hypothesis-invalidates-the-permanent-phillips-curve-tradeoff, aggregate-supply-and-demand-framework-synthesizes-short-run-nonneutrality-and-long-run-neutrality, macroeconomic-schools-diverge-on-market-stability-and-rules-versus-discretion
- Cập nhật 3 trang cũ: natural-rate-of-unemployment-equals-frictional-plus-structural-unemployment, money-is-non-neutral-in-the-short-run-but-neutral-in-the-long-run, potential-gdp-measures-productive-capacity-at-full-employment; cập nhật state file và index.md
- Wiki đạt 437 trang, 0 lỗi, 0 mồ côi; còn lại: Ch.15–17 (cargill_central_bank_policy)

## [2026-09-22:21-46-41] ingest | cargill_central_bank_policy Ch.15 — Step 5: Final Policy Targets
- 4 trang mới: price-stability-is-defined-by-low-and-stable-inflation-rather-than-zero-percent, monetary-policy-lags-can-render-countercyclical-stabilization-destabilizing, inflation-targeting-framework-anchors-expectations-through-transparent-commitment, federal-reserve-dual-mandate-creates-inflation-bias-and-time-inconsistency
- Cập nhật 3 trang cũ: central-bank, consumer-price-index-has-four-sources-of-upward-bias, five-step-framework-structures-central-bank-policy-analysis; cập nhật state file và index.md
- Wiki đạt 441 trang, 0 lỗi, 0 mồ côi; còn lại: Ch.16–17 (cargill_central_bank_policy)

## [2026-09-22:21-59-35] ingest | cargill_central_bank_policy Ch.16–17 (Hoàn tất 100% nguồn sách)
- 10 trang mới: Ch.16 (monetary-policy-tactics-..., taylor-rule-..., lucas-critique-..., time-inconsistency-..., constrained-discretion-...) và Ch.17 (great-depression-monetary-contraction-..., accord-of-nineteen-fifty-one-..., great-inflation-originated-..., great-moderation-benefited-..., great-recession-stemmed-...)
- Cập nhật 6 trang liên quan: open-market-operations, macroeconomic-schools-..., five-step-framework-..., government-policy-failure-..., government-safety-net-..., de-jure-central-bank-independence-...; cập nhật 03_state/cargill_central_bank_policy.md (17/17 chương - 100%) và 02_wiki/index.md
- Hook kiểm định validate_wiki_page.py --all: 451 trang quét, 0 lỗi, 0 mồ côi. Hoàn tất toàn bộ nguồn cargill_central_bank_policy!

## [2026-09-22:22-06-04] lint | 451 trang
- 0 lỗi schema/mồ côi/link chết, 2 conflict tồn đọng, 11 nợ stub, 0 nợ inbox, 9 khái niệm đề xuất tạo stub
- 147 trang draft đủ điều kiện lên stable (outlink >= 1, backlink >= 2, không conflict)
- Báo cáo chi tiết: Claude outputs/lint-2026-09-22-451.md

## [2026-09-22:22-12-31] promote | 147 trang lên stable
- Nâng 147 trang draft đủ điều kiện (outlink >= 1, backlink >= 2, không conflict) theo danh sách người dùng duyệt từ lint 451 trang lên stable
- 52 trang draft còn lại giữ nguyên (50 trang backlink = 1, 2 trang đang gắn nhãn ⚠️ Conflict); không đổi last_updated, không chạm thân bài
- Wiki hiện đạt: 388 stable, 52 draft, 11 stub; hook validate_wiki_page.py --all sạch (451 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-22:22-20-45] ingest | tạo 9 stub từ kết quả lint 451 trang & triage inbox
- Tạo 9 stub concept: nominal-interest-rate, interbank-market, financial-intermediation, deposit-insurance, liquidity-risk, adverse-selection, asset-bubble, asymmetric-information, reverse-repurchase-agreement
- Triage _inbox.md: sửa trích dẫn d.4584 trong central-bank và làm sạch inbox; cập nhật liên kết từ 10 trang liên quan và bổ sung vào index.md
- Wiki đạt 460 trang (388 stable, 52 draft, 20 stub); hook validate_wiki_page.py --all quét 460 trang, 0 lỗi, 0 mồ côi

## [2026-09-22:22-42-24] lint | 460 trang
- 0 lỗi schema/mồ côi/link chết, 2 conflict tồn đọng, 0 nợ stub (20 stub hiện hành), 0 nợ inbox (0 mục tồn)
- 0 trang draft đủ điều kiện lên stable (toàn bộ 147 trang trước đó đã promote; 50 trang backlink = 1, 2 trang conflict)
- Báo cáo chi tiết: Claude outputs/lint-2026-09-22-460.md

## [2026-09-22:23-04-38] ingest | clippings Cụm 1 ALM và Bảng cân đối ngân hàng VN
- 7 trang mới: alm-balance-sheet-balancing-progresses-through-four-operational-dimensions, cash-flow-balancing-resolves-immediate-payment-obligations-against-excess-reserve-opportunity-cost, maturity-balancing-manages-liquidity-duration-to-mitigate-rollover-and-repricing-risks, behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales, vietnams-banking-system-exhibits-structural-dichotomy-between-tt1-and-tt2, multiple-balance-sheet-mismatches-compound-banking-systemic-risk, tt1-deposit-rate-stickiness-prevents-interbank-liquidity-from-lowering-lending-rates
- Cập nhật 3 trang liên quan: interbank-market, liquidity-risk, deposit-money-banks; đăng ký source id clippings vào 03_state/_sources_manifest.md (82 file) và tạo 03_state/clippings.md, cập nhật 02_wiki/index.md
- Phần còn lại: Cụm 1 (các bài SBV/vàng còn lại) và Cụm 2–6 (chi tiết ở 03_state/clippings.md); hook validate_wiki_page.py --all quét 467 trang, 0 lỗi, 0 mồ côi

## [2026-09-22:23-13-05] ingest | clippings Cụm 1 Đợt 2 (Hoàn tất 100% Cụm 1 ALM & Ngân hàng VN)
- 6 trang mới: active-spot-foreign-exchange-intervention-injects-primary-liquidity-directly-into-banking-system, central-bank-interest-rate-corridor-requires-separate-facilities-for-interbank-and-credit-markets, central-banks-prioritize-public-policy-mandates-over-accounting-profitability, domestic-gold-pricing-diverges-from-international-benchmarks-due-to-structural-liquidity-constraints, banks-fundamentally-rely-on-short-term-liabilities-to-finance-long-term-capital-formation, treasury-deposits-at-commercial-banks-provide-temporary-liquidity-without-easing-structural-funding-gaps
- Cập nhật 4 trang liên quan: financial-intermediation, sterilization, central-banks-are-necessarily-public-institutions-despite-private-ownership-fictions, multiple-balance-sheet-mismatches-compound-banking-systemic-risk; cập nhật 03_state/clippings.md (100% Cụm 1 hoàn tất) và 02_wiki/index.md
- Phần còn lại: Cụm 2–6 (chi tiết ở state file); hook validate_wiki_page.py --all: 473 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:09-28-36] ingest | clippings Cụm 2 Điều hành Fed, Repo & Nợ công Kho bạc (Hoàn tất 100%)
- 8 trang mới: treasury-repo-market-operates-through-three-distinct-client-segments, repo-rate-spikes-transmit-to-federal-funds-rate-via-fhlb-arbitrage, quantitative-tightening-differs-from-quantitative-easing-through-balance-sheet-asymmetry, persistent-fiscal-deficits-operate-as-a-monetary-force-expanding-private-balance-sheets, bank-absorption-of-sovereign-debt-is-governed-by-a-regulatory-triangle, sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand, treasury-buybacks-function-as-debt-management-rather-than-monetary-yield-curve-control, central-banks-face-policy-reaction-traps-when-energy-supply-shocks-elevate-headline-inflation
- Nâng 3 stub lên draft: repurchase-agreement, reverse-repurchase-agreement, quantitative-easing; cập nhật liên kết 5 trang cũ: risk-based-capital-requirements-..., supervisory-stress-testing-..., interbank-market, core-inflation-..., expected-inflation-...; cập nhật 03_state/clippings.md (100% Cụm 2) và index.md
- Phần còn lại: Cụm 3–6 (chi tiết ở 03_state/clippings.md); hook validate_wiki_page.py --all: 481 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:09-37-29] ingest | clippings Cụm 3 Lạm phát phi tuyến & Vĩ mô toàn cầu (Hoàn tất 100%)
- 4 trang mới: supply-chain-disruptions-propagate-nonlinearly-through-input-output-cascades, producer-price-stage-differential-signals-systemic-supply-chain-inflation-cascades, sovereign-bond-term-premia-rise-from-fiscal-burdens-independently-of-inflation-expectations, global-risk-appetite-reallocates-across-sectors-under-surging-sovereign-yields
- Cập nhật 2 chiều 5 trang: core-inflation-strips-out-one-time-price-level-jumps, central-banks-face-policy-reaction-traps-when-energy-supply-shocks-elevate-headline-inflation, expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads, sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand, cpi; cập nhật 03_state/clippings.md (100% Cụm 3) và index.md
- Phần còn lại: Cụm 4–6 (chi tiết ở 03_state/clippings.md); hook validate_wiki_page.py --all: 485 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:09-41-47] ingest | clippings Cụm 4 Thị trường ngoại hối châu Á, Tỷ giá & Carry Trade (Hoàn tất 100%)
- 5 trang mới: industrial-overcapacity-drives-transition-from-supply-funding-to-productive-buyer-funding, conditional-cny-carry-trade-finances-global-real-absorption-without-capital-account-liberalization, japan-net-international-creditor-position-anchors-global-jpy-carry-trade, sovereign-fx-intervention-integrates-fima-repo-facility-to-prevent-treasury-market-dislocation, commodity-import-energy-shocks-transmit-directly-into-offshore-dollar-funding-stresses
- Cập nhật 2 chiều 4 trang: repurchase-agreement, quantitative-easing, sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand, exchange-rate; cập nhật 03_state/clippings.md (100% Cụm 4) và index.md
- Phần còn lại: Cụm 5–6 (chi tiết ở 03_state/clippings.md); hook validate_wiki_page.py --all: 490 trang quét, 0 lỗi, 0 mồ côi
## [2026-09-23:09-49-03] ingest | clippings Cụm 5 Hàm phản ứng NHTW, Forward Guidance & Định giá thị trường (Hoàn tất 100%)
- 5 trang mới: reaction-function-guidance-replaces-calendar-path-with-conditional-market-pricing, asymmetric-monetary-reaction-functions-generate-ratchet-effects-on-real-rates, absence-of-policy-roadmaps-anchors-markets-to-high-frequency-data-noise, financial-market-duration-repricing-executes-monetary-tightening-on-central-banks-behalf, persistent-policy-rate-holds-compound-sovereign-bond-duration-and-refinancing-risks
- Cập nhật 2 chiều 5 trang: forward-guidance-evolved-from-moral-suasion-as-conditional-transparent-commitment, taylor-rule-formalizes-systematic-feedback-and-the-taylor-principle, real-interest-rate, central-banks-face-policy-reaction-traps-when-energy-supply-shocks-elevate-headline-inflation, sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand; cập nhật 03_state/clippings.md (100% Cụm 5) và index.md
- Phần còn lại: Cụm 6 (chi tiết ở 03_state/clippings.md); hook validate_wiki_page.py --all: 495 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:09-59-10] ingest | clippings Cụm 6 Phương pháp luận, Tín dụng tư nhân & Nợ công (Hoàn tất 100% clippings)
- 6 trang mới: top-down-macro-analysis-fails-without-bottom-up-microstructure-and-capital-allocation, private-credit-selective-defaults-obscure-systemic-banking-fragility, sovereign-debt-refinancing-dependency-constrains-monetary-policy-horizons, offshore-foreign-currency-debt-pricing-diverges-from-domestic-benchmarks, endogenous-systemic-liquidity-circulation-distorts-accounting-equations-via-balance-sheet-resonance, technological-automation-shifts-scarcity-from-commodity-production-to-relational-sectors
- Nâng 2 stub lên draft: financial-intermediation, liquidity-risk; cập nhật 2 chiều 4 trang: sovereign-bond-term-premia-..., vietnams-banking-system-..., alm-balance-sheet-..., measured-gdp-...; cập nhật 03_state/clippings.md (100% Cụm 6) và index.md
- Hoàn tất 100% toàn bộ nguồn clippings (82 file, 6 cụm, 33 trang wiki mới, 5 stub nâng cấp); hook validate_wiki_page.py --all: 501 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:10-18-30] ingest | fixed_income_during Ch.1–2 (Mở đầu & Tiền tệ, tín dụng)
- 8 trang mới: fixed-income-instruments, securities-differ-from-bilateral-contracts-..., modern-credit-markets-shift-lenders-..., statutory-welfare-entitlements-..., four-key-attributes-distinguish-cash-..., seigniorage-and-transaction-costs-create-a-price-band-..., lex-monetae-grants-sovereign-currency-authority-..., fiat-money-removes-the-commodity-reserve-straightjacket-...; 1 stub mới: dollarization
- Cập nhật 5 trang liên quan: money-serves-as-a-medium-of-exchange-..., seigniorage, monetary-standards-evolved-from-commodity-money-to-fiat-credit-money, trade-balance, social-safety-nets-...; cập nhật 03_state/fixed_income_during.md (Ch.1–2 [x]) và 02_wiki/index.md
- Phần còn lại: Ch.3–39 (chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 510 trang quét, 0 lỗi, 0 mồ côi
## [2026-09-23:11-04-53] ingest | fixed_income_during Ch.3–6 (Giai đoạn 1 của Part One)
- 6 trang mới: commercial-banks-create-inside-money-by-extending-credit, multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures, commercial-bills-and-cheques-represent-claims-on-money-rather-than-money-itself, bill-discounting-and-rediscounting-provide-dual-recourse-liquidity-to-the-banking-system, narrow-banking-mandates-one-hundred-percent-reserve-backing-eliminating-private-credit-money, price-level-targeting-commits-to-offset-past-inflation-deviations-unlike-inflation-targeting
- Cập nhật 2 chiều 4 trang: central-bank, discount-window, inflation-targeting-framework-anchors-expectations-through-transparent-commitment, bill-discounting-and-rediscounting-provide-dual-recourse-liquidity-to-the-banking-system; cập nhật 03_state/fixed_income_during.md (Ch.3–6 [x]) và 02_wiki/index.md
## [2026-09-23:11-38-36] ingest | fixed_income_during Ch.7–9 (Hoàn tất 100% Part One: Preliminaries)
- 6 trang mới: delphic-versus-odyssean-forward-guidance-delineates-forecast-contingency-from-unconditional-commitment, large-scale-asset-purchases-expand-inside-money-and-lengthen-commercial-bank-balance-sheets, helicopter-money-materializes-through-sovereign-debt-rollover-and-seigniorage-remittance, index-tracking-asset-purchases-distort-free-float-liquidity-due-to-forced-holders, prolonged-volatility-suppression-breeds-liquidity-fragility-and-var-shocks, central-bank-output-legitimacy-cannot-substitute-for-input-legitimacy-under-treaty-constraints
- Cập nhật 2 chiều 6 trang: outright-vs-credit-open-market-operations, forward-guidance-evolved-from-moral-suasion-..., central-bank-collateral-framework-design-and-risk-control, securities-lending-programmes-and-central-bank-collateral-swaps, negative-interest-rates-distort-financial-intermediation-..., quantitative-easing, central-bank; cập nhật 03_state/fixed_income_during.md (Ch.7–9 [x]) và index.md
- Hoàn tất 100% Part One (Ch.1–9); phần còn lại: Part Two — Cash Instruments (Ch.10–22, chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 522 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:13-33-43] ingest | fixed_income_during Ch.10–12 (Part Two: Cash Instruments, Giao dịch & Bù trừ trung tâm)
- 9 trang mới: book-entry-securities-centralize-ownership-via-global-notes-and-csds, schuldschein-avoids-mark-to-market-accounting-through-transfer-restrictions, fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities, competitive-dealer-inquiries-incur-information-leakage-and-winners-curse, delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles, securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins, central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk, ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding, xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices
- Cập nhật 2 chiều 2 trang: securities-differ-from-bilateral-contracts-by-transferability-without-counterparty-consent, multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures; cập nhật 03_state/fixed_income_during.md (Ch.10–12 [x]) và 02_wiki/index.md
- Phần còn lại: Part Two tiếp theo (Ch.13–22) và Part Three–Eight (chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 531 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:13-47-15] ingest | fixed_income_during Ch.13–14 (Part Two: Thị trường tiền tệ & Thị trường Repo)
- 8 trang mới: commercial-paper-and-short-term-instruments-compete-as-near-money, overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume, lagged-compounded-overnight-rates-lack-term-risk-premia-and-delay-policy-transmission, futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows, general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing, repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk, collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties, tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers
- Cập nhật 2 chiều 3 trang: repurchase-agreement, securities-lending-programmes-and-central-bank-collateral-swaps, xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices; cập nhật 03_state/fixed_income_during.md (Ch.13–14 [x]) và 02_wiki/index.md
- Phần còn lại: Part Two tiếp theo (Ch.15–22) và Part Three–Eight (chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 539 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:14-01-33] ingest | fixed_income_during Ch.15–17 (Part Two: Định giá trái phiếu, Rủi ro lãi suất & FRN)
- 12 trang mới: turn-premium-reflects-year-end-balance-sheet-constraints-rather-than-policy-rate-expectations, joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause, dutch-and-american-auctions-differentiate-dealer-bidding-incentives-through-the-winners-curse, clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement, yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates, modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases, bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons, bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing, floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread, rfr-compounded-in-arrears-notes-require-observation-lags-and-synthetic-term-rates-to-quote-accrued-interest, discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps, constant-maturity-floaters-fail-par-reset-due-to-coupon-and-discount-tenor-mismatch
- Cập nhật 2 chiều 6 trang: fixed-income-instruments, yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price, general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing, overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume, competitive-dealer-inquiries-incur-information-leakage-and-winners-curse, central-bank-output-legitimacy-cannot-substitute-for-input-legitimacy-under-treaty-constraints; cập nhật 03_state/fixed_income_during.md (Ch.15–17 [x]) và 02_wiki/index.md
- Phần còn lại: Part Two tiếp theo (Ch.18–22) và Part Three–Eight (chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 551 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:14-18-31] ingest | fixed_income_during Ch.18–20 (Part Two: Thanh khoản thị trường, Mô hình đường cong & Phân tích cấu trúc kỳ hạn)
- 12 trang mới: microscopic-versus-macroscopic-market-liquidity-separates-trade-breadth-from-balance-sheet-depth, clobs-and-otc-market-making-differentiate-search-costs-from-information-leakage, spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias, on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures, yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields, bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles, parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness, composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition, dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches, parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments, convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end, institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity
- Cập nhật 2 chiều 4 trang: fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities, bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons, modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases, financial-market-duration-repricing-executes-monetary-tightening-on-central-banks-behalf; cập nhật 03_state/fixed_income_during.md (Ch.18–20 [x]) và 02_wiki/index.md
- Phần còn lại: Part Two tiếp theo (Ch.21–22) và Part Three–Eight (chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 563 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:14-30-50] ingest | fixed_income_during Ch.21–22 (Hoàn tất 100% Part Two: Carry, Roll-Down & Chênh lệch đường cong lợi suất)
- 7 trang mới: upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields, holding-period-return-combines-carry-and-roll-down-quantified-by-break-even-yield-buffers, z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves, par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities, par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks, interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision, ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve
- Cập nhật 2 chiều 4 trang: bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing, yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields, spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias, discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps; cập nhật 03_state/fixed_income_during.md (100% Part Two xong) và 02_wiki/index.md
- Hoàn tất 100% Part Two (Ch.10–22); phần còn lại: Part Three–Eight (Ch.23–39, chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 570 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:14-40-07] ingest | fixed_income_during Ch.23 (Hoàn tất 100% Part Three: Trái phiếu liên kết lạm phát & Định giá TIPS)
- 7 trang mới: capital-indexed-tips-structure-operates-as-a-synthetic-foreign-currency-investment, sovereign-inflation-linked-issuance-hedges-tax-creep-and-extracts-the-inflation-risk-premium, cpi-rebasing-and-ex-tobacco-conventions-prevent-index-distortions-in-inflation-linked-debt, inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering, breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise, real-short-rates-and-inflation-forecasts-determine-the-arbitrage-free-carry-of-inflation-linked-bonds, comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves
- Cập nhật 2 chiều 5 trang: expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads, composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition, z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves, bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing, cpi; cập nhật 03_state/fixed_income_during.md (100% Part Three xong) và 02_wiki/index.md
- Hoàn tất 100% Part Three (Ch.23); phần còn lại: Part Four–Eight (Ch.24–39, chi tiết ở 03_state/fixed_income_during.md); hook validate_wiki_page.py --all: 577 trang quét, 0 lỗi, 0 mồ côi

## [2026-09-23:14-52-10] ingest | fixed_income_during Ch.24 (Part Four: Rủi ro tín dụng, Thứ bậc nợ & Xếp hạng tín nhiệm)
- 7 trang mới: default-insolvency-and-bankruptcy-differentiate-covenant-breaches-cash-shortfalls-and-terminal-liquidation, debt-acceleration-and-cross-default-clauses-prevent-time-subordination-in-multi-creditor-structures, statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors, sovereign-debt-operates-as-a-repeat-game-devoid-of-judicial-liquidation-and-enforceable-seniority, collective-action-clauses-resolve-creditor-coordination-failures-and-neutralize-hold-out-vultures, credit-ratings-represent-ordinal-ranking-scales-distorted-by-the-issuer-pays-conflict-and-curse-of-the-commons, rating-migration-matrices-resolve-the-maturity-paradox-and-reveal-corporate-versus-sovereign-risk-divergence
- Cập nhật 2 chiều 5 trang: private-credit-selective-defaults-obscure-systemic-banking-fragility, joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause, market-impact-of-collateral-framework-and-leverage-constraints, par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks, ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve; cập nhật 03_state/fixed_income_during.md (Ch.24 [x]) và 02_wiki/index.md
- Phần còn lại: Part Four tiếp theo (Ch.25–27: Covered Bonds, ABS, RMBS) và Part Five–Eight (Ch.28–39, chi tiết ở 03_state/fixed_income_during.md)

## [2026-09-23:15-02-15] ingest | fixed_income_during Ch.25–27 (Hoàn tất 100% Part Four: Covered Bonds, ABS & RMBS)
- 8 trang mới: covered-bonds-combine-on-balance-sheet-dual-recourse-with-insolvency-ring-fencing, overcollateralization-optimizes-covered-bond-spreads-against-unsecured-asset-encumbrance, danish-balance-principle-links-mortgage-origination-to-bond-pricing-through-delivery-and-prepayment-options, asset-backed-securitization-achieves-bankruptcy-remoteness-via-true-sale-and-non-recourse-spvs, tranching-mechanics-partition-collateral-losses-into-equity-mezzanine-and-senior-option-profiles, mortgage-prepayments-combine-demographic-attrition-economic-refinancing-and-burn-out-effects, rmbs-negative-convexity-arises-from-embedded-borrower-prepayment-options-and-wal-extension, tba-market-mechanics-and-dollar-rolls-manage-mortgage-origination-uncertainty
- Cập nhật 2 chiều 5 trang: statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors, debt-acceleration-and-cross-default-clauses-prevent-time-subordination-in-multi-creditor-structures, bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons, institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity, market-impact-of-collateral-framework-and-leverage-constraints; cập nhật 03_state/fixed_income_during.md (100% Part Four xong) và 02_wiki/index.md
- Hoàn tất 100% Part Four (Ch.24–27); phần còn lại: Part Five–Eight (Ch.28–39, chi tiết ở 03_state/fixed_income_during.md)

## [2026-09-23:15-08-30] ingest | fixed_income_during Ch.28 (Part Five: Hợp đồng tương lai trái phiếu chính phủ & Kinh doanh chênh lệch giá Basis)
- 9 trang mới: physical-delivery-bond-futures-deter-market-manipulation-through-post-settlement-inventory-exposure, bond-futures-market-microstructure-differentiates-clearing-netting-and-cftc-trader-categories, conversion-factors-induce-duration-dependent-cheapest-to-deliver-biases-around-notional-coupons, bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships, quality-delivery-options-embed-negative-convexity-and-convexity-drag-in-bond-futures, futures-rolls-maintain-interest-rate-hedges-via-pvbp-neutral-roll-ratios-below-parity, futures-delivery-windows-confer-timing-options-governed-by-carry-sign-and-repo-fails-risk, futures-squeezes-and-repo-scarcity-invert-net-basis-into-negative-territory, cash-settled-bond-futures-and-exchange-for-physical-substitute-delivery-with-swap-or-yield-baskets
- Cập nhật 2 chiều 5 trang: on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures, general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing, repo-rate-spikes-transmit-to-federal-funds-rate-via-fhlb-arbitrage, futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows, clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement; cập nhật 03_state/fixed_income_during.md (Ch.28 [x]) và 02_wiki/index.md
- Phần còn lại: Part Five tiếp theo (Ch.29: Swaps) và Part Six–Eight (Ch.30–39, chi tiết ở 03_state/fixed_income_during.md)

## [2026-09-23:15-16-45] ingest | fixed_income_during Ch.29 (Hoàn tất 100% Part Five: Hợp đồng hoán đổi lãi suất, Nén giao dịch & Vi cấu trúc Swaps)
- 3 trang mới: plain-vanilla-interest-rate-swaps-trade-pure-risk-and-resolve-preferred-habitat-friction, swap-rate-term-structures-diverge-from-bank-bond-yields-due-to-panel-survivorship-bias, multilateral-trade-compression-and-re-couponing-deflate-gross-notional-and-margin-drag
- Cập nhật 2 chiều 4 trang: institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity, par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities, par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks, xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices; cập nhật 03_state/fixed_income_during.md (100% Part Five xong: Ch.28–29) và 02_wiki/index.md
- Hoàn tất 100% Part Five (Ch.28–29); phần còn lại: Part Six–Eight (Ch.30–39, chi tiết ở 03_state/fixed_income_during.md)

## [2026-09-23:15-30-00] ingest | fixed_income_during Ch.30–32 (Hoàn tất 100% Part Six: Giao dịch đường cong & Giá trị tương đối trái phiếu)
- 8 trang mới: fixed-income-trade-governance-balances-probabilistic-stop-loss-and-epistemological-consistency, statistical-arbitrage-in-fixed-income-forfeits-initial-trend-movements-against-fundamental-dislocations, curve-trading-hierarchies-systematically-immunize-lower-order-risk-dimensions, steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks, butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions, yield-curve-pca-factors-link-curvature-convexity-to-implied-rate-volatility, bond-relative-value-metrics-select-reference-curves-aligned-with-instrument-hedging-practices, bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging
- Cập nhật 2 chiều 5 trang: spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias, institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity, bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships, par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities, interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision; cập nhật 03_state/fixed_income_during.md (100% Part Six xong: Ch.30–32) và 02_wiki/index.md
- Hoàn tất 100% Part Six (Ch.30–32); phần còn lại: Part Seven (Ch.33–38: Portfolio Management) và Part Eight (Ch.39: Global Markets)

## [2026-09-23:15-36-00] ingest | fixed_income_during Ch.33–38 (Hoàn tất 100% Part Seven: Quản trị rủi ro danh mục, Phòng hộ & Tái cân bằng)
- 12 trang mới: pca-generalised-regression-resolves-bidirectional-noise-asymmetry-in-fixed-income, pca-eigenvalue-herfindahl-index-measures-yield-curve-complexity-and-hedging-breadth, bond-index-construction-balances-ex-ante-replicability-and-liquidity-frictions, cross-market-settlement-conventions-induce-repo-funding-mismatches-in-global-indices, risk-neutral-portfolios-face-duration-aging-convexity-and-cross-gamma-instability, long-only-fixed-income-portfolios-cannot-achieve-complete-risk-neutrality, partial-index-replication-optimizes-tracking-error-against-cash-drag-and-turnover-costs, yield-curve-model-hedges-immunize-state-variable-sensitivities-via-linear-systems, mean-variance-optimisation-fails-in-fixed-income-due-to-finite-maturity-and-covariance-instability, dimension-reduction-via-asset-classes-and-pca-stabilizes-mean-variance-matrix-inversion, portfolio-rebalancing-strategies-embed-implicit-assumptions-on-asset-return-autocorrelation, multi-currency-portfolio-rebalancing-distorts-asset-allocation-under-exchange-rate-shocks
- Cập nhật 2 chiều 5 trang: modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases, bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons, curve-trading-hierarchies-systematically-immunize-lower-order-risk-dimensions, statistical-arbitrage-in-fixed-income-forfeits-initial-trend-movements-against-fundamental-dislocations, institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity; cập nhật 03_state/fixed_income_during.md (100% Part Seven xong: Ch.33–38) và 02_wiki/index.md
- Hoàn tất 100% Part Seven (Ch.33–38); phần còn lại: Part Eight (Ch.39: Selected Global Bond Markets)

## [2026-09-23:15-42-00] ingest | fixed_income_during Ch.39 (Hoàn tất 100% Part Eight & Hoàn thành toàn bộ sách nguồn Alexander Düring)
- 6 trang mới: euro-area-sovereign-debt-integration-relied-on-redenomination-and-reconventioning, sovereign-debt-maturity-trade-offs-balance-rate-volatility-against-refinancing-stability, sovereign-exchange-auctions-and-liquidity-facilities-mitigate-redemption-profile-clumping, sovereign-floating-rate-debt-matches-retail-banking-assets-amid-benchmark-transitions, funded-pension-systems-anchor-ultra-long-sovereign-yield-curves-the-uk-gilt-case, treasury-bill-maturity-clustering-functions-as-a-barometer-for-government-shutdown-risks
- Cập nhật 2 chiều 5 trang: clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement, floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread, institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity, sovereign-debt-refinancing-dependency-constrains-monetary-policy-horizons, turn-premium-reflects-year-end-balance-sheet-constraints-rather-than-policy-rate-expectations; cập nhật 03_state/fixed_income_during.md (42/42 file - 100% hoàn thành) và 02_wiki/index.md
- Hoàn tất 100% toàn bộ nguồn sách Alexander Düring (Fixed Income Trading and Risk Management, 39 chương, 7.300 dòng nguồn, 8 phần)

## [2026-09-23:16-06-36] query | quan hệ giữa các sector macro (phân tích netting private sector)
- 1 trang analysis mới: the-imf-private-sector-column-nets-household-surplus-against-enterprise-deficit — bảng 7-cột IMF gộp hộ gia đình/doanh nghiệp vào 1 cột trong khi ma trận 5-cột Cargill tách riêng, có thể che dòng vốn nội bộ
- Backlink từ the-private-sector-resource-gap-must-be-financed-by-other-sectors (không nâng last_updated); index.md cập nhật; --all sạch (631 trang)

## [2026-09-23:16-12-41] schema | query lượt đắt luôn gọi --backlinks cho trang cốt lõi
- query/SKILL.md bước 3: thêm gọi `validate_wiki_page.py --backlinks <trang>` cho mỗi trang trực tiếp liên quan, không chỉ đi outlink; triage bằng tên file như lượt rẻ
- Lý do: backlink 2 chiều chỉ đảm bảo từ lượt ingest tạo/sửa trang, không đảm bảo trang cũ; decisions.md ghi chi tiết

## [2026-09-23:16-26-24] schema | query — 3 kỷ luật mượn từ deep-research
- query/SKILL.md: bước 3 cap 1 vòng mở rộng outlink/backlinks; bước 2 hỏi làm rõ khi thuật ngữ Việt→Anh mơ hồ; bước 5 dedup `grep type: analysis` trước khi tạo trang mới
- Lý do: đối chiếu kiến trúc thật của anthropic-skills:deep-research; không mượn fan-out subagent vì đụng luật cấm auto-spawn; decisions.md ghi chi tiết

## [2026-09-23:18-03-30] ingest | imf_macro_accounting Ch.5 backfill F1 — tách trang gộp, 4/7 khó khăn kinh tế chuyển đổi
- Đọc lại "Monetary Analysis in Transition Economies: Some Special Issues" (d.5100–5132): 4/7 khó khăn đã có nhưng gộp chung 1 trang vi phạm §5 Atomic. Xoá trang gộp, tách 4 trang mới + stub `monobank` + nâng `non-performing-loans` stub→draft
- Sửa backlink ở 9 trang liên quan (3 trang trỏ tới trang cũ + 6 trang bổ sung link ngược); index.md mục lục Ch.5 cập nhật
- `--all` sạch (635 trang, 0 vấn đề, 0 mồ côi); Ch.1 vẫn là phần duy nhất chưa ingest của nguồn này

## [2026-09-23:18-17-07] lint | 635 trang
- Lỗi: 2 Conflict tồn đọng (không đổi), 15 nợ stub (16 stub, `monobank` chưa tính), 24 báo giả OCR, 0 stale, 0 vi phạm Atomic/title, 0 mồ côi/link chết
- 153 trang draft đủ điều kiện `stable` (backlink ≥ 2, hết Conflict); báo cáo: `Claude outputs/lint-2026-09-23-635.md`

## [2026-09-23:18-28-44] lint | 635 trang — mở rộng mục 3 và mục 5 theo yêu cầu
- Mục 3 quét toàn bộ 635 trang (không chỉ cụm mới nhất): thêm 14 khái niệm ứng viên (Fed, ECB, ALM, ZLB, PVBP, MMF, ABS, LCR, primary dealer, term premium, bid-ask spread, RWA, NIM, open interest, TAF, LDR)
- Mục 5 đối chiếu có cấu trúc 635 title (42 cặp trùng ≥4 từ khoá, đọc 9 cặp nghi ngờ nhất) — 0 trùng lặp thật; tự phát hiện và sửa lỗi regex (`\|` sai cú pháp) từng báo nhầm 2 trang đã tồn tại là thiếu
- Báo cáo cập nhật cùng file `Claude outputs/lint-2026-09-23-635.md`

## [2026-09-23:18-42-34] promote | 153 trang lên stable
- Nâng 153 trang draft đủ điều kiện (outlink >= 1, backlink >= 2, không conflict) theo danh sách người dùng duyệt từ lint 635 trang lên stable
- 87 trang draft còn lại giữ nguyên (85 trang backlink = 1, 2 trang đang gắn nhãn ⚠️ Conflict); không đổi last_updated, không chạm thân bài
- Wiki hiện đạt: 532 stable, 87 draft, 16 stub; hook validate_wiki_page.py --all sạch (635 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-23:18-47-03] review | 5 trang
- Đạt đối chiếu nguồn gốc: central-bank (sửa dải dòng Ch.15 d.4514–4537 → d.4682–4713 về dual mandate/time inconsistency), deposit-money-banks, gdp, conventional-fiscal-deficit, subsidies
- Cả 5 trang đều gắn reviewed: 2026-09-23 và reviewed_by: model; không đổi last_updated do claim không đổi
- Giữ lại: không; validate_wiki_page.py --all sạch (635 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-23:19-16-02] ingest | tata_bank_alm Ch.1 — Introduction
- 9 trang mới: interest-rate-risk-in-the-banking-book-irrbb (hub), economic-value-and-earnings-perspectives-complement-each-other-in-alm, 3 cấu phần IRRBB (gap-risk, basis-risk, option-risk), credit-spread-risk-in-the-banking-book-csrbb, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital, banks-predominantly-hedge-duration-mismatches-on-balance-sheet-rather-than-via-derivatives, key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts; cập nhật 2 trang (alm-balance-sheet-balancing-..., modified-duration-and-pvbp-...)
- Khởi tạo 03_state/tata_bank_alm.md (bản đồ chunk Ch.1–6), cập nhật _sources_manifest.md và 02_wiki/index.md; 0 stub mới, 0 mồ côi, 0 link chết
- Còn lại: Ch.2–6 (chi tiết theo chunk ở state file)

## [2026-09-23:19-24-00] ingest | tata_bank_alm Ch.2 cụm A — Economic Value & Earnings Measures
- 9 trang mới: economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows, repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date, duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base, net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations, balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views, interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves, earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights, receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk, monitoring-market-value-changes-outside-nii-horizon-prevents-deferred-interest-rate-losses; cập nhật 3 trang (economic-value-and-earnings-perspectives-complement-each-other-in-alm, interest-rate-gap-risk-stems-from-repricing-timing-mismatches, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.2 cụm A xong) và 02_wiki/index.md; tổng 654 trang wiki, 0 mồ côi, 0 link chết
- Còn lại: Ch.2 cụm B–C; Ch.3–6 (chi tiết theo chunk ở state file)

## [2026-09-23:19-30-00] ingest | tata_bank_alm Ch.2 cụm B — Funds Transfer Pricing (FTP)
- 7 trang mới: funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks (hub), matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions, funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads, ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation, regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp, funds-transfer-pricing-contrasts-with-derivatives-funding-value-adjustments, contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons; cập nhật 3 trang (xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices, liquidity-risk, alm-balance-sheet-balancing-progresses-through-four-operational-dimensions)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.2 cụm B xong) và 02_wiki/index.md; tổng 661 trang wiki, 0 mồ côi, 0 link chết
## [2026-09-23:19-38-00] ingest | tata_bank_alm Ch.2 cụm C — Non-maturity Products & Replicating Model
- 7 trang mới: non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles, embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap, replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches, rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates, replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates, dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates, sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models; cập nhật 3 trang (interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options, behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales, funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.2 cụm C xong) và 02_wiki/index.md; tổng 667 trang wiki, 0 mồ côi, 0 link chết
- Còn lại: Ch.3–6 (chi tiết theo chunk ở state file)
## [2026-09-23:19-37-46] schema | /research — sửa theo audit + eval 3 case
- Viết lại research/SKILL.md (1 cổng duyệt gộp, schema theo nhánh, đọc theo mục, nguồn nhiều file, nhánh Conflict/inbox); đồng bộ CLAUDE.md, query description, rules/project-records.md
- Sửa grep tag YAML nhiều dòng ở research + query (60/661 trang bị bỏ sót)
- Eval dry-run 3 case × 2 bản: 9/9 cả hai; repo không bị ghi; chi tiết ở decisions.md

## [2026-09-23:19-48-00] ingest | tata_bank_alm Ch.3 — Bank ALM in Practice
- 7 trang mới: bank-specific-alm-tailors-balance-sheet-governance-to-business-models-and-regional-habitats, net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons, behavioral-alm-models-customer-irrbb-optionality-and-asymmetric-interbank-competition, holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage, zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp, coupon-floors-and-indicator-floors-induce-asymmetric-nii-exposures-in-negative-rates, rapid-rate-tightening-exposes-duration-gaps-and-asymmetric-prepayment-speeds; cập nhật 3 trang (alm-balance-sheet-balancing-progresses-through-four-operational-dimensions, net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.3 xong) và 02_wiki/index.md; tổng 674 trang wiki, 0 mồ côi, 0 link chết
- Còn lại: Ch.4–6 (chi tiết theo chunk ở state file)

## [2026-09-23:20-00-00] ingest | tata_bank_alm Ch.4 — Case Study: The Collapse of Silicon Valley Bank
- 6 trang mới: silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs (case), held-to-maturity-gaap-accounting-masks-unrealized-economic-value-losses-in-banking-books, unhedged-interest-rate-swap-unwinding-magnifies-balance-sheet-vulnerability-for-short-term-pnl, svb-three-year-duration-gap-breached-supervisory-outlier-thresholds-absent-deposit-modeling-manipulation, regulatory-arbitrage-via-deposit-duration-assumptions-distorts-supervisory-irrbb-compliance, supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb; cập nhật 3 trang (duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital, economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.4 xong) và 02_wiki/index.md; tổng 680 trang wiki, 0 mồ côi, 0 link chết
- Còn lại: Ch.5–6 (chi tiết theo chunk ở state file)

## [2026-09-23:20-10-00] ingest | tata_bank_alm Ch.5 — Update on Regulatory and Supervisory Changes to IRRBB
- 6 trang mới: multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards, eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement, simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks, maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb, simultaneous-compliance-problem-constrains-fixed-rate-allocation-under-dual-sot-limits, supervisory-irrbb-reporting-mandates-five-standardized-templates-under-eu-2024-855; cập nhật 5 trang cũ (supervisory-outlier-test-..., monitoring-market-value-changes-..., economic-value-and-earnings-..., interest-rate-risk-in-the-banking-book-irrbb, zero-lower-bound-interest-rate-floors-...)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.5 xong) và 02_wiki/index.md; tổng 686 trang wiki, 0 mồ côi, 0 link chết, mọi trang mới đều >= 2 backlinks
- Còn lại: Ch.6 — The Future of ALM (d.3109–3269)

## [2026-09-23:20-16-00] ingest | tata_bank_alm Ch.6 — The Future of ALM
- 6 trang mới: fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities, tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage, deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering, model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity, climate-risk-transmission-channels-impact-bank-balance-sheets-and-ftp-pricing, granular-customer-segmentation-enhances-behavioral-modeling-of-banking-book-optionality; cập nhật 5 trang cũ (funds-transfer-pricing-..., contingency-liquidity-..., non-maturity-products-..., behavioral-alm-models-..., holistic-alm-elevates-...)
- Cập nhật 03_state/tata_bank_alm.md (đánh dấu Ch.6 và toàn bộ nguồn xong 100%) và 02_wiki/index.md; tổng 692 trang wiki, 0 mồ côi, 0 link chết, mọi trang mới đều >= 2 backlinks
- Nguồn tata_bank_alm hoàn tất toàn diện 6/6 chương

## [2026-09-23:20-28-32] lint | 692 trang
- 0 lỗi hook validate_wiki_page.py --all; 0 mồ côi; 182/182 file nguồn khớp; 16 nợ stub; 2 conflict cũ tồn đọng
- 60 trang draft đủ điều kiện stable (outlink >= 1, backlink >= 2, không conflict); 86 trang draft giữ nguyên
- Báo cáo: Claude outputs/lint-2026-09-23-692.md

## [2026-09-23:20-32-11] promote | 60 trang lên stable
- Nâng 60 trang draft đủ điều kiện (outlink >= 1, backlink >= 2, không conflict) theo danh sách người dùng duyệt từ lint 692 trang lên stable
- 86 trang draft còn lại giữ nguyên (84 trang backlink = 1, 2 trang đang gắn nhãn ⚠️ Conflict); không đổi last_updated, không chạm thân bài
- Wiki hiện đạt: 590 stable, 86 draft, 16 stub; hook validate_wiki_page.py --all sạch (692 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-23:21-28-24] research | bảng cân đối của MAs (money authorities)
- Cluster 10 trang; enrich 5 trang
- 8 claim mới ở 5 trang, 5 liên kết, 1 analysis; hook sạch 693 trang
- Báo cáo: Claude outputs/research-2026-09-23-monetary-authorities-balance-sheet.md

## [2026-09-23:21-50-00] lint | audit thuật ngữ sterilization và writing-style
- Xóa bỏ triệt để thuật ngữ dịch sai "tiệt trùng (sterilization)" ở 8 trang wiki, 1 state file và index.md, chuẩn hóa thành "nghiệp vụ trung hòa (sterilization)" / "can thiệp trung hòa"
- Quét và chuẩn hóa văn phong theo project skill writing-style trên toàn bộ wiki: sửa 8 trang vi phạm B2 (từ ngữ cực đoan/bạo lực), 9 trang vi phạm H1 ("đóng vai trò là" -> "là"), 5 trang vi phạm E4 & B1 (ẩn dụ "bốc hơi" & cụm "dẫn đến hệ quả là"), 5 trang vi phạm I4 (filler "nhìn chung")
- Không nâng last_updated theo §7.5; hook validate_wiki_page.py --all sạch 0 lỗi; 0 match cho "tiệt trùng" và các cụm từ cấm
- Báo cáo: Claude outputs/audit-2026-09-23-thuat-ngu-writing-style.md

## [2026-09-24:11-26-00] ingest | choudhry_analysing_yield_curve Ch.1 — The Yield Curve
- 7 trang mới: coupon-bias-induces-relative-yield-distortions-along-ytm-curves, par-yield-curve-derives-required-coupons-for-at-par-debt-issuance, implied-forward-rates-function-as-hedge-rates-rather-than-accurate-market-forecasts, local-expectations-hypothesis-resolves-jensens-inequality-under-risk-neutrality, humped-yield-curves-reflect-peaked-interest-rate-expectations-or-maturity-habitat-imbalances, cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity, collateralized-clearing-and-hedging-demand-drive-interest-rate-swaps-below-sovereign-yields
- Nâng 1 stub: yield-curve; cập nhật 6 trang liên quan: pure-expectations-hypothesis-..., liquidity-premium-hypothesis-..., yield-to-maturity-assumes-..., yield-curve-representations-..., institutional-preferred-habitats-..., swap-rate-term-structures-...; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 701 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.2–13 (choudhry_analysing_yield_curve)

## [2026-09-24:11-55-00] ingest | choudhry_analysing_yield_curve Ch.2 — A Further Look at Spot and Forward Rates
- 4 trang mới: instantaneous-forward-curves-lead-spot-curve-inflections-and-peak-earlier, arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures, mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds, term-structure-modeling-bifurcates-into-short-rate-diffusion-and-forward-rate-hjm-frameworks
- Cập nhật 4 trang: upward-sloping-yield-curves-..., bootstrapping-and-reverse-bootstrapping-..., yield-to-maturity-assumes-..., yield-curve-representations-...; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 705 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.3–13 (choudhry_analysing_yield_curve)

## [2026-09-24:13-10-00] ingest | choudhry_analysing_yield_curve Ch.3 — Interest Rate Modelling I: Primer on Basic Concepts
- 4 trang mới: ornstein-uhlenbeck-mean-reversion-prevents-infinite-drift-in-short-rate-diffusion, itos-lemma-transforms-short-rate-stochastic-dynamics-into-bond-pricing-pdes, one-factor-term-structure-models-force-perfect-yield-correlation-across-maturities, markov-property-reduces-contingent-claim-valuation-to-single-state-pdes
- Cập nhật 3 trang: parallel-yield-curve-shifts-..., term-structure-modeling-bifurcates-..., key-rate-duration-isolates-...; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 709 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.4–13 (choudhry_analysing_yield_curve)

## [2026-09-24:13-18-00] ingest | choudhry_analysing_yield_curve Ch.4 — Interest Rate Modelling II: The Dynamic of Asset Prices
- 4 trang mới: geometric-brownian-motion-ensures-strictly-positive-asset-prices-via-multiplicative-increments, itos-lemma-derives-the-lognormal-asset-price-distribution-via-convexity-drag-correction, bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics, pull-to-par-effect-forces-bond-price-volatility-to-decay-deterministically-to-zero-at-maturity
- Cập nhật 2 trang: arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures, convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 713 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.5–13 (choudhry_analysing_yield_curve)

## [2026-09-24:13-28-00] ingest | choudhry_analysing_yield_curve Ch.5 — Interest Rate Models I
- 5 trang mới: equilibrium-models-generate-term-structures-from-macro-assumptions-while-arbitrage-free-models-calibrate-to-market-prices, vasicek-model-incorporates-mean-reversion-into-gaussian-dynamics-but-permits-negative-interest-rates, cox-ingersoll-ross-model-scales-volatility-by-the-square-root-of-rates-to-preclude-negative-yields, hull-white-model-extends-vasicek-via-time-dependent-drift-to-match-the-initial-yield-curve, black-derman-toy-model-imposes-lognormal-short-rate-dynamics-on-arbitrage-free-binomial-trees
- Cập nhật 3 trang: term-structure-modeling-bifurcates-..., one-factor-term-structure-models-force-..., ornstein-uhlenbeck-mean-reversion-prevents-...; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 718 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.6–13 (choudhry_analysing_yield_curve)

## [2026-09-24:13-36-00] ingest | choudhry_analysing_yield_curve Ch.6 — Interest Rate Models II
- 5 trang mới: heath-jarrow-morton-framework-locks-forward-rate-drift-strictly-to-volatility-structures, libor-market-models-bridge-hjm-to-observable-discrete-forward-rates-and-black-76-swaption-pricing, jump-diffusion-interest-rate-models-capture-abrupt-policy-rate-shocks-via-poisson-processes, relative-value-trading-mandates-equilibrium-models-while-derivative-market-making-requires-arbitrage-free-models, multi-factor-term-structure-models-are-demanded-by-cross-rate-correlation-and-volatility-smiles
- Cập nhật 3 trang: term-structure-modeling-bifurcates-..., one-factor-term-structure-models-force-..., statistical-arbitrage-in-fixed-income-...; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 723 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.7–13 (choudhry_analysing_yield_curve)

## [2026-09-24:13-44-00] ingest | choudhry_analysing_yield_curve Ch.7 — The Index-Linked Bond Yield Curve
- 3 trang mới: real-yield-curves-reflect-real-cost-of-capital-and-fluctuate-with-economic-growth, implied-forward-inflation-curves-isolate-marginal-inflation-expectations-via-fisher-identity, indexation-lags-require-iterative-consistency-procedures-in-real-term-structure-estimation
- Cập nhật 3 trang: real-interest-rate, breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise, expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 726 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.8–13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-00-00] ingest | choudhry_analysing_yield_curve Ch.8 — Yield Curve Analytics in the Post-2008 Era
- 4 trang mới: dual-curve-discounting-separates-rate-projection-from-collateralized-cash-flow-discounting, credit-support-annex-discounting-incorporates-cheapest-to-deliver-collateral-optionality, derivatives-funding-valuation-adjustments-apply-bank-internal-cost-of-funds-directly-to-expected-exposure, cross-currency-basis-and-quanto-adjustments-align-internal-funding-curves-across-currencies
- Cập nhật 3 trang: plain-vanilla-interest-rate-swaps-trade-pure-risk-and-resolve-preferred-habitat-friction, liquidity-premium-compensates-for-secondary-market-depth-and-transaction-costs, multilateral-trade-compression-and-re-couponing-deflate-gross-notional-and-margin-drag; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 730 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.9–13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-04-00] ingest | choudhry_analysing_yield_curve Ch.9 — Negative Interest Rate Analytics
- 2 trang mới: discount-factor-functions-exhibit-asymmetric-convexity-and-exceed-unity-in-negative-interest-rates, negative-yield-to-maturity-implies-bond-market-prices-exceed-nominal-aggregate-cash-flows
- Cập nhật 2 trang: yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price, negative-interest-rates-distort-financial-intermediation-and-test-the-zero-lower-bound; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 732 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.10–13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-08-00] ingest | choudhry_analysing_yield_curve Ch.10 — Estimating and Fitting the Yield Curve I
- 3 trang mới: nelson-siegel-and-svensson-models-fit-parsimonious-forward-curves-with-asymptotic-long-rate-stability, b-splines-and-regression-splines-transform-piecewise-polynomial-curve-fitting-into-linear-least-squares, forward-rate-oscillation-reveals-magnified-fitting-errors-and-disqualifies-linear-interpolation
- Cập nhật 3 trang: cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity, parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness, mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 735 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.11–13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-18-00] ingest | choudhry_analysing_yield_curve Ch.11 — Estimating and Fitting the Yield Curve II
- 3 trang mới: variable-roughness-penalty-splines-balance-short-end-flexibility-and-long-end-smoothness, anderson-sleath-model-weights-fitting-errors-by-inverse-modified-duration, exponential-splines-linearize-discount-functions-via-asymptotic-maturity-transforms
- Cập nhật 3 trang: parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness, nelson-siegel-and-svensson-models-fit-parsimonious-forward-curves-with-asymptotic-long-rate-stability, mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 738 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.12–13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-26-00] ingest | choudhry_analysing_yield_curve Ch.12 — Yield Curves and Relative Value
- 3 trang mới: excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions, bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance, repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades
- Cập nhật 3 trang: coupon-bias-induces-relative-yield-distortions-along-ytm-curves, steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks, general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Tổng 741 trang wiki, 0 lỗi, 0 mồ côi; còn lại: Ch.13 (choudhry_analysing_yield_curve)

## [2026-09-24:14-31-00] ingest | choudhry_analysing_yield_curve Ch.13 — Identifying Relative Value in the US Treasury Market
- 3 trang mới: ancillary-yield-curves-expand-benchmark-definitions-via-strict-irr-admissibility, geometric-programming-optimizes-continuous-discount-curves-under-bounded-uncertainty, ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets
- Cập nhật 3 trang: butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions, dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches, repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades; cập nhật 03_state/choudhry_analysing_yield_curve.md và index.md
- Nguồn choudhry_analysing_yield_curve hoàn tất 100% (Ch.1–13 xong; Appendix & Index bỏ qua theo §2); tổng 744 trang wiki, 0 lỗi, 0 mồ côi

## [2026-09-24:15-28-46] review | 5 trang
- Đạt đối chiếu nguồn gốc: exchange-rate (bổ sung clippings vào sources), monetizing-the-deficit-creates-high-powered-money-and-inflation, financial-and-monetary-regime, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital, current-account-balance (thêm chú thích §7.5 Ch.2 d.797–815)
- Cả 5 trang đều gắn reviewed: 2026-09-24 và reviewed_by: model; không đổi last_updated do claim không đổi; sửa 4 link chết tồn đọng ở Ch.10–11
- Giữ lại: không; validate_wiki_page.py --all sạch (744 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-24:15-41-26] review | 5 trang
- Đạt đối chiếu nguồn gốc: potential-gdp-measures-productive-capacity-at-full-employment, alm-balance-sheet-balancing-progresses-through-four-operational-dimensions, financial-system-transfers-funds-through-direct-and-indirect-channels, bank-runs-investor-strikes-and-multiple-equilibria, discount-window
- Cả 5 trang đều gắn reviewed: 2026-09-24 và reviewed_by: model; không đổi last_updated do claim không đổi
- Giữ lại: không; validate_wiki_page.py --all sạch (744 trang quét, 0 lỗi, 0 mồ côi)

## [2026-09-24:15-58-27] lint | 744 trang
- 0 lỗi hook validate_wiki_page.py --all; 0 mồ côi; 182/182 file nguồn khớp; 15 nợ stub; 2 conflict cũ tồn đọng
- 73 trang draft đủ điều kiện stable (outlink >= 1, backlink >= 2, không conflict); 84 trang draft giữ nguyên
- Báo cáo: Claude outputs/lint-2026-09-24-744.md

## [2026-09-24:16-10-00] schema | triage _inbox.md và chuẩn hóa chú thích During, Ch.28
- Cập nhật 03_state/_sources_manifest.md: cargill_central_bank_policy hoàn tất 100%
- Sửa dải dòng chú thích §7.5 Ch.28 (bond futures) ở 2 trang; ghi nhận chuẩn hóa định dạng chú thích During vào decisions.md
- Dọn sạch 3 mục trong _inbox.md (0 nợ inbox); validate_wiki_page.py --verify-sources và --all đạt 100%

## [2026-09-24:16-26-42] promote | 73 trang lên stable
- Nâng 73 trang draft đủ điều kiện (báo cáo lint-2026-09-24-744.md) lên stable; không đổi last_updated, không đụng thân bài
- 84 trang draft giữ nguyên (82 trang backlink = 1, 2 trang conflict); 0 trang bị loại trong lượt
- validate_wiki_page.py --all sạch (744 trang quét, 0 lỗi, 0 mồ côi; hiện có 645 stable, 84 draft, 15 stub)

## [2026-09-24:21-40-00] ingest | imf_macro_accounting Ch.5 — overhaul Batch 1 (Cấu trúc + Đối tượng)
- Viết lại toàn diện 9 trang theo chuẩn schema/writing-style hiện tại: monetary-statistics-are-stock-data-recorded-on-a-cash-basis, foreign-currency-items-in-monetary-statistics-are-converted-at-the-end-period-exchange-rate, consolidation-of-monetary-authorities-and-dmb-accounts-eliminates-internal-claims-to-determine-broad-money, monetary-accounts-net-claims-on-government-but-keep-claims-on-deposit-money-banks-gross, the-typical-monetary-authorities-balance-sheet-itemizes-foreign-assets-and-shows-reserve-money-by-holder, the-analytical-monetary-authorities-balance-sheet-groups-items-into-nfa-nda-and-rm, the-analytical-deposit-money-bank-balance-sheet-separates-required-from-excess-reserves, narrow-money-m1, quasi-money.
- Sửa lỗi hook `--all` bằng cách gán `type` frontmatter và chèn thêm `[[wikilink]]` liên kết nội bộ.
- Cập nhật 03_state/imf_macro_accounting.md; validate_wiki_page.py --all đạt 100% (744 trang quét, 0 lỗi, 0 mồ côi).

## [2026-09-24:21-45-00] ingest | imf_macro_accounting Ch.5 — overhaul Batch 2 (Cân đối / Đồng nhất thức)
- Rà soát và cập nhật 8 trang thuộc nhóm phương trình/cân đối nền tảng: reserve-money, money-supply-equals-net-foreign-assets-plus-net-domestic-assets, change-in-net-foreign-assets-links-the-monetary-survey-to-the-balance-of-payments, the-money-multiplier-links-reserve-money-to-the-money-supply, the-quantity-theory-links-money-velocity-prices-and-output, demand-for-money-is-a-demand-for-real-balances-driven-by-income-and-opportunity-cost, real-interest-rate, valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks.
- Sửa lỗi định dạng công thức toán học (`$$...$$` và `$ ... $`) trong một số file bị rớt lại từ đợt kiểm tra quy định format toán học.


## [2026-09-24:21-50-00] ingest | imf_macro_accounting Ch.5 — overhaul Batch 3 (Cơ chế)
- Rà soát và cập nhật 7 trang cơ chế điều hành chính sách tiền tệ: monetary-authorities-influence-reserve-money-through-five-direct-instruments, monetary-authorities-control-over-reserve-money-is-incomplete, sterilization-offsets-fx-intervention-but-only-temporarily, fixed-exchange-rates-make-the-money-supply-endogenous-while-floating-rates-restore-monetary-control, perfect-capital-mobility-with-a-fixed-exchange-rate-strips-monetary-policy-of-independence, currency-substitution-undermines-monetary-control, financial-innovation-blurs-the-boundary-of-money.
- Nâng cấp stub dollarization lên draft và liên kết bổ sung nguồn imf_macro_accounting.
- Cập nhật 03_state/imf_macro_accounting.md; validate_wiki_page.py --all tiếp tục đạt 100% sạch (744 trang quét).

## [2026-09-24:22-00-00] ingest | imf_macro_accounting Ch.5 — overhaul Batch 4 (Đặc thù chuyển đổi & Kỹ thuật IMF) — hoàn tất Ch.5
- Rà soát toàn bộ 13 trang thuộc cụm đặc thù kinh tế chuyển đổi (F1) và giao dịch IMF / Case 3 tầng IFS (Appendix): lack-of-bank-competition-in-transition-economies-forces-nonprice-credit-rationing, absence-of-money-and-financial-markets-precludes-open-market-operations-in-early-transition, old-fixed-rate-loans-and-weak-financial-discipline-complicate-interest-rate-liberalization, wide-deposit-lending-spread-in-transition-economies-reflects-four-cost-factors, interenterprise-arrears-substitute-for-bank-credit-when-budget-constraints-are-not-hardened, transition-economies-experience-large-discrete-jumps-in-money-velocity, high-government-financing-needs-subordinate-monetary-policy-to-fiscal-needs, imf-quota-and-credit-tranches-determine-a-members-reserve-position-in-the-fund, quota-payment-and-reserve-tranche-drawdowns-leave-net-foreign-assets-unchanged-while-credit-tranche-purchases-do-not, a-worked-example-shows-how-monetary-authorities-dmb-and-nbfi-balance-sheets-reconcile-into-the-financial-survey, hyperinflation, monobank, non-performing-loans.
- Bổ sung liên kết mạng từ the-quantity-theory-links-money-velocity-prices-and-output sang transition-economies-experience-large-discrete-jumps-in-money-velocity; nâng transition-economies-experience-large-discrete-jumps-in-money-velocity từ draft lên stable (đạt đủ backlink >= 2, 0 conflict).
- Cập nhật last_updated: 2026-09-24 và hoàn tất 100% đợt đại tu toàn diện 4 Batch của Chương 5 IMF Macroeconomic Accounting.
- Cập nhật 03_state/imf_macro_accounting.md; validate_wiki_page.py --all đạt 100% sạch (744 trang quét, 0 lỗi, 0 mồ côi).

## [2026-09-24:22-21-55] research | stock và flow — quan hệ động học
- Cluster 13 trang (người dùng duyệt vượt giới hạn 10); enrich 4 trang: 8 claim mới (IMF Ch.4, Cargill Ch.3), 6 link, 1 analysis mới; 3 trang stable → draft
- 4 mục _inbox chờ /review-node (d.3470, d.1149, diễn giải lãi ở debt-dynamics, link/locator monetary-statistics)
- Báo cáo: Claude outputs/research-2026-09-24-stock-flow.md

## [2026-09-24:22-27-12] review | 5 trang
- Sửa claim sai (đặt reviewed model): balance-of-payments-flows-differ-… (hai tồn kho là dự trữ và nợ nước ngoài, d.3470); flow-of-funds-fundamental-… ("tiết kiệm lũy kế" → tiết kiệm của kỳ; bỏ "hữu hình"); debt-dynamics-… (lý do vắng số hạng lãi, d.3875)
- monetary-statistics-… (bỏ GFS, link dời chỗ, locator); foreign-currency-items-… (bỏ gán tỷ giá bình quân cho BOP, thêm điều kiện OIN d.4873, bỏ câu tiền cơ sở); 2 trang stable → draft
- Không trang nào bị giữ lại; 1 mục _inbox mới: locator Box 5.8 lệch ở valuation-adjustments-… và trang analysis stock-flow

## [2026-09-24:22-31-00] review | 2 trang
- Sửa claim sai (đặt reviewed model): valuation-adjustments-… (thêm nhóm thay đổi khác d.4843, giả định minh hoạ d.4853, locator VAd d.4845–4871, OIN d.4873; bỏ "đầy đủ nhất trong nguồn"); stock-flow analysis (locator VAd, thêm d.2339 no-Ponzi, bỏ xếp lãi nhập gốc vào Other)
- valuation-adjustments-… stable → draft; không trang nào bị giữ lại; mục _inbox locator Box 5.8 đã xử lý, xoá

## [2026-09-24:22-33-34] research | NDA (Net Domestic Assets)
- Cluster 12 trang (10 core + 2 bổ sung theo người dùng); enrich 5 trang: 5 claim mới (IMF Ch.5), 5 link nội bộ; 5 trang stable → draft
- Làm rõ cơ chế trần NDA (NDA ceiling), vai trò kinh tế vĩ mô NCG/CPS, hàm phản ứng lạm phát, triệt tiêu nội bộ CDMB* và kỹ thuật tỷ giá cố định OIN
- Báo cáo: Claude outputs/research-2026-09-24-nda.md

## [2026-09-24:22-49-31] research | NDC (Net Domestic Credit)
- Cluster 13 trang (gỡ hạn mức theo yêu cầu người dùng); enrich 6 trang: 6 claim mới (IMF Ch.3, Ch.5; Cargill Ch.13), 6 link nội bộ; 5 trang stable → draft
- Làm rõ cơ chế hấp thụ nợ công qua dự trữ dư thừa, bóp méo phân bổ tín dụng, né tránh trần NDC qua nợ đọng liên doanh nghiệp và chuyển từ kiểm soát chọn lọc sang trần tổng lượng
- Báo cáo: Claude outputs/research-2026-09-24-ndc.md

## [2026-09-24:22-59-53] research | OINs (Other Items Net)
- Cluster 10 trang; enrich 5 trang: 8 claim mới (IMF Ch.5), 5 link nội bộ; 2 trang stable → draft
- Làm rõ cấu phần OIN* và OIN_d (vốn, quỹ, lãi/lỗ, SDR, float), dấu kế toán nợ/tài sản, cơ chế hấp thu tái định giá VAd và đối chiếu 3 tầng IFS
- Báo cáo: Claude outputs/research-2026-09-24-oins.md

## [2026-09-24:23-10-20] research | net-credit-to-government
- Cluster 14 trang (vượt trần 10 theo yêu cầu người dùng); enrich 4 trang: 6 claim mới (IMF Ch.3, Ch.5), 6 link; government-deposits stable → draft
- 5 mục _inbox.md chờ /review-node; case Ba Lan Ch.5 d.5147–5177 dừng vì chưa [x]
- Báo cáo: Claude outputs/research-2026-09-24-net-credit-to-government.md

## [2026-09-24:23-14-41] review | 5 trang
- Đạt sau sửa (reviewed_by: model): net-credit-to-government (đoạn 2 viết lại theo d.4835/d.2209, sửa chú thích d.5142, bổ sung chú thích), net-domestic-credit (đoạn 2 nói quá d.4837), government-borrowing-… (bỏ claim dự trữ dư thừa không có trong nguồn, sửa lý do link), high-government-financing-needs-… (bỏ đoạn 2 không có trong nguồn), fiscal-imbalance-… (dải dòng d.5769–5772 → d.5786–5788, bỏ "luôn nới lỏng")
- Giữ lại: không; 1 mục _inbox.md cho credit-to-the-private-sector (sai tên mục ở chú thích d.5142)

## [2026-09-24:23-25-04] research | thống nhất ký hiệu NCG
- Quy ước: $NCG^*$ cấp nhà chức trách tiền tệ, $NCG$ cấp hệ thống ngân hàng; $NDCG$ trong công thức M2 đổi thành $NCG$ (ghi chú ký hiệu gốc); giữ $\Delta NDC_g$ trong đồng nhất thức tài trợ khu vực, thêm câu nối
- 5 trang: net-credit-to-government (câu quy ước), net-domestic-credit, money-supply-… (stable → draft, bỏ câu rào đón về NDCG), government-borrowing-…, government-saving-investment-gap-… (chỉ thêm link)

## [2026-09-24:23-41-36] research | bảng cân đối nhà chức trách tiền tệ
- Cluster 17 trang (vượt trần 10 theo yêu cầu người dùng); enrich 4 trang: 7 claim mới (IMF, Bindseil, Cargill), 7 link, 1 analysis (neo chính sách quyết định NFA có là nhân tố tự định); typical, central-bank, autonomous-factors stable → draft
- 7 mục _inbox.md chờ /review-node
- Báo cáo: Claude outputs/research-2026-09-24-monetary-authorities-balance-sheet.md

## [2026-09-24:23-46-32] review | 5 trang
- Đã sửa, đặt reviewed_by: model: the-analytical-… (OIN* ngược chiều d.4624; "mỗi nguồn gốc ứng một công cụ" sai: dự trữ bắt buộc qua bên nợ), sterilization-capacity-… (đọc sai Bindseil, công thức Cargill không giải mã được trong md, d.5065–5070 → d.5060–5062), claims-on-DMB (ghép cặp hợp nhất sai), monetary-accounts-net-… (bỏ "khu vực tư gộp" và lý do tự thêm, bổ sung lý do 2 d.4612), consolidation-of-… (bỏ lý do tính trùng, sửa link M2)
- 3 trang stable → draft; 2 mục _inbox.md mới (locator sterilization-offsets; title/type 4 trang cho lint)

## [2026-09-24:23-51-01] review | 4 trang
- Đã sửa, đặt reviewed_by: model: the-typical-… (danh mục Box 5.1, bỏ "định chế phi tài chính"), credit-to-the-private-sector (bỏ "động lực chủ yếu của NDA", sửa d.4837 nói quá, bỏ mốc 1991–94, sửa tên mục d.5142), central-bank (Bank of Ireland không "tư nhân", HKMA không "ủy thác in", đoạn giám sát viết lại theo d.2600–2602, nhiệm vụ kép theo d.4690–4708, sửa 4 chú thích lệch dòng)
- Đạt, chỉ sửa chú thích: sterilization-offsets-… (d.5065–5070 → d.5062, d.5071–5083 → d.5082)

## [2026-09-25:09-18-05] ingest | imf_macro_accounting Ch.6 — viết lại (Flow of Funds)
- 4 trang mới: reading-the-flow-of-funds-by-rows-…, government-disposable-income, private-disposable-income, external-imbalance-is-diagnosed-…; viết lại 4 trang (sector-columns + Box 6.4, recording-conventions, a-real-flow-of-funds sửa claim chú thích 4, constraints); chỉ thêm link/locator 3 trang
- Không stub mới; --all sạch (750 trang, 0 vấn đề, 0 mồ côi)
- Ch.6 xong; phần còn lại của nguồn: Ch.1 (xem state file)

## [2026-09-25:09-25-37] review | 5 trang
- Đã sửa và đặt reviewed_by: model cho cả 5 trang. government-disposable-income: bỏ claim "C_g ở Ch.3 gồm chuyển nhượng và lãi" (d.2073 không nói) và câu "hai cách tính cho cùng một khoảng chênh". private-disposable-income: bỏ vế "gồm hộ gia đình lẫn doanh nghiệp". reading-by-rows: bỏ "phần lớn".
- external-imbalance: link CAB=ΔNFA gán sai phạm vi (đồng nhất thức bao cả ba nguồn tài trợ); bỏ "hay cả hai". sector-columns: sửa mâu thuẫn với d.5776 (bảng có chỉ ra khu vực mất cân đối), thêm locator d.5594, d.5673
- Còn chờ review từ lượt ingest Ch.6: a-real-flow-of-funds, recording-conventions, constraints

## [2026-09-25:09-38-21] ingest | imf_macro_accounting Ch.2 B1 (A1+A2, d.607–934) — đối chiếu lại
- 6 trang mới: gross-output, intermediate-consumption, net-investment, gross-domestic-saving, nominal-gdp, underground-economy
- Sửa claim, về draft: net-domestic-product, compensation-of-employees, real-gdp, gdp, net-exports, measured-gdp-…; thêm locator 7 trang
- Còn B2 (d.935–1058), B3 (d.1059–1241), B4 (d.1524–1650)

## [2026-09-25:09-43-19] ingest | imf_macro_accounting Ch.2 B2 (B+C, d.935–1058) — đối chiếu lại
- 10 trang mới: net-material-product, gross-material-product, laspeyres-price-index, paasche-price-index, wholesale-price-index, producer-price-index, sauerbeck-index, policy-induced-inflation, cost-push-inflation, demand-pull-inflation
- core-inflation-… về draft (2 câu không nguồn IMF → câu trỏ); 14 trang khác khớp nguồn; 2 mục mới ở _inbox
- Còn B3 (d.1059–1241), B4 (d.1524–1650)

## [2026-09-25:09-45-53] review | 5 trang
- Đạt: gdp (thêm locator d.656), gndi
- Sửa, về draft: reserve-money (bỏ diễn giải trọng số không có trong nguồn, d.4647–4651); reserve-assets-… (chú thích 5 ở d.3597 không phải d.3591; câu tách NFA hệ thống ngân hàng gán lý do sai → theo d.3975–3977); cpi (2 câu không nguồn → câu trỏ; locator Boskin d.932–936)
- Gỡ mục cpi khỏi _inbox (đã xử lý)

## [2026-09-25:09-48-40] review | 5 trang (ingest lại Ch.2, lượt 1/5)
- Đạt: real-gdp (tách câu nối chấm phẩy, không đổi claim), core-inflation-… (thêm locator Pricing Policies d.1134–1144 cho ý tự do hóa giá), measured-gdp-…, net-exports, laspeyres-price-index (thêm locator Paasche d.1015)
- Không có claim sai; còn 17 trang từ luồng ingest lại Ch.2 chờ review

## [2026-09-25:09-54-11] lint | 766 trang
- Máy: 0 lỗi trang, 0 mồ côi; 1 file nguồn chưa kê (Clippings/Term premia); 25 OCR đều báo giả. Tay: 2 conflict tồn, 5 vi phạm title/type, 1 cặp trùng (foreign-exchange-reserves), 14 nợ stub, 2 khái niệm chưa có trang (broad-money, velocity), 0 stale
- Inbox: 14/16 mục đề xuất xoá (đã xử lý ở review 24/9); 58 trang đủ điều kiện stable (28 đã review, 30 chưa)
- Báo cáo: Claude outputs/lint-2026-09-25-766.md

## [2026-09-25:10-02-03] schema | xử lý lint 2026-09-25 (766 trang)
- Title: 29 trang Title Case → đúng tên file; 5 trang Ch.5 analysis một nguồn → concept; đổi tên to-what-extent-…-1990-91-… → to-what-extent-was-polands-early-transition-output-decline-overstated (sửa 5 link + ví dụ §8 schema)
- Trang mới: broad-money (draft, Ch.5 d.4713–5144), velocity-of-money (stub); inbox xoá 16/16 mục đã xử lý; decisions.md + ingest/SKILL.md: ngoại lệ stale cho ingest lại dạng đối chiếu, quy ước title
- Không xử lý: foreign-exchange-reserves không phải trùng (nghĩa dự trữ quốc tế, rộng hơn cấu phần FX), giữ lại; 14 nợ stub chờ /research; 2 conflict chờ B3–B4; --all 768 trang sạch

## [2026-09-25:10-17-17] research | quasi-fiscal mechanics: 8 concept + 1 analysis
- Tạo: 9 trang mới (8 concept pages kênh mechanics + 1 analysis page tổng hợp); update quasi-fiscal-operations + index.md §quasi-fiscal-mechanics
- Validation: 777 trang, 0 lỗi, 0 mồ côi; analysis page đã có backlink từ quasi-fiscal-operations
- Phạm vi: tám kênh mechanics từ phát hành tiền cơ sở → bù trừ NFA-NDA; synthesis không nhét thêm claim mới từ nguồn


## [2026-09-25:10-21-45] research | macro-accounting mechanics: foundation page
- Tạo: 1 trang concept "macro-accounting-mechanics-explains-how-transactions-create-distortion-in-reported-deficits" (bridge note giữa quasi-fiscal-operations và 8 kênh chi tiết)
- Nội dung: Giải thích ba nguyên lý kế toán (kép, consolidation, nhân tiền) và cơ chế che giấu thâm hụt từ đó
- Update: quasi-fiscal-operations.md (thêm link) + index.md (thêm vào danh mục quasi-fiscal-mechanics)
- Validation: 778 trang, 0 lỗi, 0 mồ côi

## [2026-09-25:11-45-50] research | quasi-fiscal (công cụ QFO + hub)
- Cluster 8 trang; enrich 3 trang
- 6 claim mới ở 3 trang (quasi-fiscal-operations, credit-subsidies về draft), 4 link; 1 mục inbox (primary-liquidity lệch d.4653)
- Báo cáo: Claude outputs/research-2026-09-25-quasi-fiscal.md

## [2026-09-25:11-54-22] research | cơ chế trợ cấp tỷ giá
- Cluster 8 trang; enrich 4 trang
- 8 claim mới ở 4 trang (cả 4 stable → draft), 1 link; 1 mục inbox (unit-of-account câu không nguồn)
- Báo cáo: Claude outputs/research-2026-09-25-exchange-rate-subsidies.md

## [2026-09-25:12-37-19] review | 1 trang
- Đã sửa: unit-of-account-in-the-balance-of-payments (bỏ cảnh báo "đọc sai chiều" và câu hai bút toán lệch — không có trong d.3508/d.3510); reviewed_by: model
- Ghi inbox: exchange-rate dòng 13 mắc cùng claim không nguồn (d.3508)

## [2026-09-25:12-45-41] review | 4 trang
- Đã sửa: exchange-rate (bỏ cảnh báo d.3508 không nguồn; clippings chỉ nói Nhật, thêm d.22–24; stable → draft), primary-liquidity-injection (policy-controlled lệch d.4653; thuật ngữ không có trong nguồn; nhân tiền về d.4707), quasi-fiscal-operations (bỏ "không phải ý định lừa dối"; câu PSBR theo d.2107), analysis 8 kênh (thêm locator, bỏ seigniorage, bù trừ tự động, RM↑50; ví dụ r = 10% ghi là minh hoạ)
- Cả 4 trang reviewed_by: model; inbox thêm 4 trang thành phần có locator sai hoặc claim không nguồn

## [2026-09-25:12-55-41] research | chế độ tỷ giá
- Cluster 16 trang (vượt giới hạn 10 theo chỉ định người dùng); enrich 5 trang
- 7 claim mới ở 5 trang, 7 link; 3 trang stable → draft; enrich trang Ba Lan dừng vì Ch.1 [ ]; 2 mục inbox
- Báo cáo: Claude outputs/research-2026-09-25-exchange-rate-regimes.md

## [2026-09-25:12-59-16] lint | 16 trang (cluster chế độ tỷ giá)
- 0 lỗi máy/mồ côi/conflict/OCR; trùng lặp 2, khái niệm chưa có trang 2, Atomic 1, title 1, nợ stub 1; verify-sources: 1 file Clippings chưa kê
- 5 trang đủ điều kiện stable; triage 9 mục inbox (3 xoá, 6 gộp)
- Báo cáo: Claude outputs/lint-2026-09-25-16.md

## [2026-09-25:13-04-51] ingest | imf_macro_accounting + cargill_central_bank_policy — dọn nợ lint cluster tỷ giá
- sterilization stub → draft (IMF d.3969, d.5060–5062, d.5082; Cargill d.3979); 2 stub mới: managed-float, parallel-foreign-exchange-market
- 13 link chèn vào câu có sẵn (7 managed-float, 6 parallel-…; bỏ underground-economy vì "chợ đen" ở đó là kinh tế ngầm)
- Không đổi phần nguồn còn lại; state 2 nguồn + index §Sources đã cập nhật

## [2026-09-26:09-53-45] ingest | ftp_transmission_analysis
- 3 trang mới: ftp-transmission-channels-steer-bank-balance-sheet-risks, ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc, balance-sheet-optimization-models-calibrate-ftp-as-a-control-variable
- 3 trang cập nhật (stable → draft): funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks, regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp, matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions; 0 stub mới
- Nguồn hoàn tất 100%; kê thêm nguồn dài vab_ftp_methodology (chưa ingest, state file đã dựng); index §Sources + bản kê đã cập nhật

## [2026-09-26:09-58-27] ingest | vab_ftp_methodology d.1–530
- 5 trang mới: vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu, vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing, ftp-base-curve-construction-contrasts-vnd-historical-cost-with-usd-market-benchmarks, regulatory-deposit-insurance-and-statutory-reserves-apportion-into-market-1-cof, planned-nim-allocation-determines-ftp-deposit-mobilization-margins
- 2 trang cập nhật (stable → draft): funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads, ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation; 0 stub mới
- Phần còn lại: Điều 5–15 & Phụ lục (d.531–2118); state file + index §Sources đã cập nhật
## [2026-09-26:10-04-30] ingest | vab_ftp_methodology d.531–983
- 5 trang mới: ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital, contingent-liquidity-charge-prices-undrawn-credit-commitments, deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles, matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch, promotional-and-behavioral-loan-ftp-pricing-decomposes-hybrid-cash-flows
- 4 trang cập nhật: contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons (stable → draft), ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc, funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads, vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing; 0 stub mới
- Phần còn lại: Điều 7–15 & Phụ lục (d.984–2118); state file + index §Sources đã cập nhật

## [2026-09-26:10-09-24] ingest | vab_ftp_methodology d.984–1255
- 5 trang mới: interbank-market-2-ftp-curve-construction-relies-on-peer-quotes-and-vnibor, treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers, contractual-amendment-ftp-repricing-rules-govern-loan-and-deposit-restructuring, non-earning-asset-and-nostro-vostro-ftp-treatment-precludes-double-counting, ftp-reporting-architecture-synthesizes-multi-dimensional-nii-and-nim-performance
- 3 trang cập nhật: vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu, matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions, vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing; 0 stub mới
- Phần còn lại: Phụ lục 01–06 & Mẫu biểu (d.1256–2118); state file + index §Sources đã cập nhật

## [2026-09-26:10-14-43] ingest | vab_ftp_methodology d.1256–2118
- 3 trang mới: term-liquidity-premium-matrix-calibrates-two-dimensional-floating-rate-spreads, two-tier-ftp-operational-workflows-govern-market-1-and-market-2-cycles, interbank-tenor-ladder-and-deal-ticket-standardization-enforce-internal-treasury-transfers
- 2 trang cập nhật: matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch, treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers; 0 stub mới
- Nguồn hoàn tất 100%; state file + index §Sources đã cập nhật

## [2026-09-26:10-23-44] ingest | sbv_circular_14_2025 TT14_1 d.1–798
- 5 trang mới: three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds, standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa, regulatory-credit-conversion-factors-apportion-off-balance-sheet-contingent-liabilities, loan-to-value-and-specialised-lending-criteria-differentiate-real-estate-risk-weights, credit-risk-mitigation-framework-recognizes-collateral-netting-guarantees-and-derivatives
- 3 trang cập nhật: contingent-liquidity-charge-prices-undrawn-credit-commitments, ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc, regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp; 0 stub mới
- Phần còn lại: TT14_1 d.799–1583 (Chương III IRB) và TT14_2; state file + index §Sources đã cập nhật

## [2026-09-26:10-29-33] ingest | sbv_circular_14_2025 TT14_1 d.799–1583
- 5 trang mới: basel-output-floor-and-coverage-ratios-constrain-irb-capital-reductions, regulatory-default-definition-and-multi-tier-portfolio-segmentation-anchor-irb-models, asymptotic-single-risk-factor-model-derives-corporate-irb-risk-weighted-assets, retail-irb-portfolio-risk-weights-calibrate-mortgage-revolving-and-other-retail-correlations, expected-loss-and-provisioning-shortfall-mechanics-adjust-regulatory-capital
- 3 trang cập nhật: three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds, standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa, ftp-credit-spread-and-capital-charge-operationalize-deal-level-raroc; 0 stub mới
- Hoàn tất 100% file TT14_1.md; phần còn lại: TT14_2 (d.1–1788); state file + index §Sources đã cập nhật

## [2026-09-26:10-35-30] ingest | sbv_circular_14_2025 TT14_2 d.1–750
- 5 trang mới: irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility, standardized-measurement-approach-and-internal-loss-multiplier-govern-operational-risk-capital, trading-book-and-banking-book-boundary-enforces-market-risk-containment, market-risk-capital-requirements-aggregate-interest-equity-fx-and-commodity-charges, subordinated-debt-amortization-and-eligibility-criteria-govern-tier-2-capital
- 3 trang cập nhật: three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds, regulatory-default-definition-and-multi-tier-portfolio-segmentation-anchor-irb-models, treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers; 0 stub mới
- Phần còn lại: TT14_2 d.751–1788 (Chunk 4: Phụ lục II–VIII); state file + index §Sources đã cập nhật

## [2026-09-26:10-39-30] ingest | sbv_circular_14_2025 TT14_2 d.751–1788
- 3 trang mới: counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure, securities-financing-transactions-and-bilateral-netting-govern-counterparty-exposures, supervisory-approval-and-technical-documentation-standards-govern-irb-rollout
- 3 trang cập nhật: standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa, credit-risk-mitigation-framework-recognizes-collateral-netting-guarantees-and-derivatives, irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility; 0 stub mới
- Nguồn hoàn tất 100% (cả 4/4 chunk); state file + index §Sources đã cập nhật

## [2026-09-26:10-50-45] ingest | sbv_circular_83_2025 TT83 d.1–352
- 4 trang mới: three-lines-of-defense-framework-enforces-banking-internal-control-and-risk-oversight, senior-management-oversight-and-conflict-of-interest-containment-anchor-banking-governance, credit-underwriting-and-approval-controls-enforce-operational-independence, proprietary-trading-internal-controls-mandate-front-middle-back-office-segregation
- 3 trang cập nhật: irb-governance-use-test-and-validation-standards-anchor-internal-ratings-credibility, trading-book-and-banking-book-boundary-enforces-market-risk-containment, treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers; 0 stub mới
- Phần còn lại: Chunk 2 (d.353–955) & Chunk 3 (d.956–1928); state file + index §Sources đã cập nhật

## [2026-09-26:10-56-15] ingest | sbv_circular_83_2025 TT83 d.353–955
- 5 trang mới: risk-appetite-framework-and-capital-targets-anchor-multi-year-risk-strategy, credit-risk-governance-mandates-portfolio-limits-and-problem-credit-containment, liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans, operational-risk-management-framework-mandates-rcsa-kri-and-loss-event-databases, irrbb-supervisory-framework-measures-eve-and-nii-sensitivity-across-interest-rate-shocks
- 5 trang cập nhật: interest-rate-risk-in-the-banking-book-irrbb, contingent-liquidity-charge-prices-undrawn-credit-commitments, standardized-measurement-approach-and-internal-loss-multiplier-govern-operational-risk-capital, three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds, credit-underwriting-and-approval-controls-enforce-operational-independence; 0 stub mới
- Phần còn lại: Chunk 3 (d.956–1928); state file + index §Sources đã cập nhật

## [2026-09-26:11-04-00] ingest | sbv_circular_83_2025 TT83 d.956–1928
- 4 trang mới: model-risk-management-framework-governs-lifecycle-and-validation-standards, icaap-framework-determines-economic-capital-and-target-capital-under-stress, irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios, risk-based-internal-audit-framework-enforces-third-line-oversight-and-governance
- 5 trang cập nhật: model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity, ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital, multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards, three-lines-of-defense-framework-enforces-banking-internal-control-and-risk-oversight, irrbb-supervisory-framework-measures-eve-and-nii-sensitivity-across-interest-rate-shocks; 0 stub mới
- Nguồn hoàn tất 100% (cả 3/3 chunk, 13 trang concept mới); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:11-20-00] ingest | sbv_draft_circular_replace_22 d.1–406
- 4 trang mới: basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion, loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity, equity-and-corporate-bond-financing-limits-curb-speculative-credit-allocation, statutory-capital-real-value-and-remedial-mechanisms-govern-bank-solvency
- 3 trang cập nhật: credit-underwriting-and-approval-controls-enforce-operational-independence, deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles, three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds; 0 stub mới
- Phần còn lại: Chunk 2 (d.407–872), Chunk 3 (d.873–1713) & Chunk 4 (d.1714–2009); state file + index §Sources đã cập nhật

## [2026-09-26:11-25-00] ingest | sbv_draft_circular_replace_22 d.407–872
- 4 trang mới: basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers, basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability, sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk, regulatory-liquidity-transition-rules-govern-dual-track-migration-from-mtll-to-lcr-nsfr
- 3 trang cập nhật: regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp, liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans, deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles; 0 stub mới
- Phần còn lại: Chunk 3 (d.873–1713) & Chunk 4 (d.1714–2009); state file + index §Sources đã cập nhật

## [2026-09-26:11-30-00] ingest | sbv_draft_circular_replace_22 d.873–1713
- 4 trang mới: hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers, retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows, contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments, contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement
- 3 trang cập nhật: basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers, contingent-liquidity-charge-prices-undrawn-credit-commitments, regulatory-credit-conversion-factors-apportion-off-balance-sheet-contingent-liabilities; 0 stub mới
- Phần còn lại: Chunk 4 (d.1714–2009); state file + index §Sources đã cập nhật

## [2026-09-26:11-35-00] ingest | sbv_draft_circular_replace_22 d.1714–2009
- 3 trang mới: asf-and-rsf-factor-matrices-calibrate-nsfr-structural-funding-requirements, leverage-ratio-exposure-measure-aggregates-on-balance-derivatives-and-off-balance-commitments, pillar-3-liquidity-disclosure-standards-mandate-qualitative-and-quantitative-market-transparency
- 3 trang cập nhật: basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability, basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion, liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans; 0 stub mới
- Nguồn hoàn tất 100% (cả 4/4 chunk, 15 trang concept mới); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:15-35-00] ingest | bcbs_144 d.1–182
- 3 trang mới: bcbs-sound-principles-establish-foundational-liquidity-risk-management-and-supervisory-mandates, board-approved-liquidity-risk-tolerance-aligns-business-strategy-with-stress-survival-horizons, internal-liquidity-cost-allocation-mandates-deal-level-ftp-for-on-and-off-balance-activities
- 3 trang cập nhật: funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks, liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans, risk-appetite-framework-and-capital-targets-anchor-multi-year-risk-strategy; 0 stub mới
- Phần còn lại: Chunk 2 (d.183–371), Chunk 3 (d.372–539) & Chunk 4 (d.540–641); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:15-46-00] ingest | bcbs_144 d.183–371
- 4 trang mới: prospective-cash-flow-forecasting-and-funding-gap-analysis-model-liquidity-stickiness, contingent-liquidity-risk-framework-mandates-asymmetric-spv-treatment-and-commitment-modeling, early-warning-indicators-and-mismatch-limits-operationalize-proactive-liquidity-monitoring, funding-diversification-and-market-access-testing-mitigate-wholesale-refinancing-freezes
- 3 trang cập nhật: liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans, contingent-liquidity-charge-prices-undrawn-credit-commitments, loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity; 0 stub mới
- Phần còn lại: Chunk 3 (d.372–539) & Chunk 4 (d.540–641); state file + index §Sources đã cập nhật

## [2026-09-26:15-50-00] ingest | bcbs_144 d.372–539
- 5 trang mới: intraday-liquidity-risk-management-mandates-real-time-monitoring-and-priority-sequencing, collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions, multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning, contingency-funding-plan-establishes-crisis-governance-and-operational-escalation-frameworks, unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits
- 3 trang cập nhật: liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans, hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers, senior-management-oversight-and-conflict-of-interest-containment-anchor-banking-governance; 0 stub mới
- Phần còn lại: Chunk 4 (d.540–641); state file + index §Sources đã cập nhật

## [2026-09-26:15-54-00] ingest | bcbs_144 d.540–641
- 4 trang mới: liquidity-risk-public-disclosure-standards-mandate-qualitative-and-quantitative-market-transcipline, supervisory-liquidity-review-process-evaluates-governance-stress-testing-and-cushion-adequacy, supervisory-early-remedial-actions-mandate-liquidity-gap-reductions-and-capital-add-ons, cross-border-supervisory-cooperation-and-crisis-information-sharing-contain-contagion
- 3 trang cập nhật: pillar-3-liquidity-disclosure-standards-mandate-qualitative-and-quantitative-market-transparency, icaap-framework-determines-economic-capital-and-target-capital-under-stress, statutory-capital-real-value-and-remedial-mechanisms-govern-bank-solvency; 0 stub mới
- Nguồn hoàn tất 100% (cả 4/4 chunk, 16 trang concept mới); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-05-00] ingest | bcbs_238 d.1–371
- 6 trang mới: basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability, hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification, hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control, hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers, hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions, alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits
- 3 trang cập nhật: hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers, basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers, unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits; 0 stub mới
- Phần còn lại: Chunk 2 (d.372–570), Chunk 3 (d.571–676) & Chunk 4 (d.677–1263); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-15-00] ingest | bcbs_238 d.372–570
- 5 trang mới: basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds, operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness, unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk, secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles, contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns
- 2 trang cập nhật: retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows, contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments; 0 stub mới
- Phần còn lại: Chunk 3 (d.571–676) & Chunk 4 (d.677–1263); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-25-00] ingest | bcbs_238 d.571–676
- 3 trang mới: basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer, secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk, consolidated-lcr-cross-border-framework-regulates-home-host-discretion-and-trapped-liquidity
- 2 trang cập nhật: contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement, basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers; 0 stub mới
- Phần còn lại: Chunk 4 (d.677–1263); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-35-00] ingest | bcbs_238 d.677–1263
- 3 trang mới: basel-iii-liquidity-risk-monitoring-tools-complement-contractual-and-market-oversight, alternative-liquidity-approaches-eligibility-assessment-principles-and-governance, basel-iii-lcr-master-factor-matrix-and-comprehensive-calibration-architecture
- 2 trang cập nhật: alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits, early-warning-indicators-and-mismatch-limits-operationalize-proactive-liquidity-monitoring; 0 stub mới
- Nguồn hoàn tất 100% (cả 4/4 chunk, 17 trang concept mới); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-46-00] ingest | bcbs_368 d.1–327
- 8 trang mới: irrbb-board-and-senior-management-governance-framework-enforces-delegation-and-independence, irrbb-risk-appetite-framework-establishes-multi-tiered-limits-and-escalation-protocols, irrbb-stress-testing-architecture-integrates-multi-tier-scenarios-and-reverse-stress-testing, non-maturity-deposit-behavioural-modelling-governs-core-and-non-core-segmentation-under-irrbb, customer-behavioural-optionalities-govern-loan-prepayments-and-early-deposit-redemptions, irrbb-internal-measurement-systems-mandate-three-pillar-model-risk-validation, irrbb-multi-currency-aggregation-governs-cross-currency-interest-rate-correlations, irrbb-capital-adequacy-and-business-alignment-integrate-into-icaap-framework
- 7 trang cập nhật: interest-rate-risk-in-the-banking-book-irrbb, credit-spread-risk-in-the-banking-book-csrbb, interest-rate-gap-risk-stems-from-repricing-timing-mismatches, interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options, economic-value-and-earnings-perspectives-complement-each-other-in-alm, balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views; 0 stub mới
- Phần còn lại: Chunk 2 (d.328–615), Chunk 3 (d.536–800) & Chunk 4 (d.801–1207); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-52-00] ingest | bcbs_368 d.328–615
- 8 trang mới: pillar-3-irrbb-qualitative-disclosure-standards-mandate-table-a-narratives, pillar-3-irrbb-quantitative-disclosure-standards-mandate-table-b-metrics, delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion, delta-nii-regulatory-calculation-rules-mandate-constant-balance-sheet-and-rolling-horizon, irrbb-capital-allocation-framework-differentiates-economic-capital-from-earnings-buffers, supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold, supervisory-remedial-actions-mandate-exposure-reduction-capital-add-ons-and-parameter-constraints, supervisory-review-process-srep-enforces-peer-benchmarking-and-cross-border-cooperation-for-irrbb
- 4 trang cập nhật: supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital, economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows, icaap-framework-determines-economic-capital-and-target-capital-under-stress, multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards; 0 stub mới
- Phần còn lại: Chunk 3 (d.536–800) & Chunk 4 (d.801–1207); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:16-58-00] ingest | bcbs_368 d.536–800
- 7 trang mới: irrbb-standardised-framework-five-stage-measurement-architecture, standardised-repricing-cash-flow-bucketing-and-nineteen-tenor-schedule, standardised-nmd-categorisation-and-core-deposit-caps-framework, standardised-loan-prepayment-modelling-and-cpr-multipliers, standardised-term-deposit-early-redemption-risk-and-tdrr-scalars, automatic-interest-rate-options-standardised-valuation-and-volatility-shocks, standardised-delta-eve-calculation-and-multi-currency-aggregation-rules
- 4 trang cập nhật: irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios, interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options, customer-behavioural-optionalities-govern-loan-prepayments-and-early-deposit-redemptions, non-maturity-deposit-behavioural-modelling-governs-core-and-non-core-segmentation-under-irrbb; 0 stub mới
- Phần còn lại: Chunk 4 (d.801–1207); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:17-03-00] ingest | bcbs_368 d.801–1207
- 5 trang mới: interest-rate-theoretical-decomposition-and-csrbb-boundary, equity-endowment-effect-and-replicating-portfolio-in-alm, economic-value-at-risk-evar-framework-and-alm-simulation-techniques, six-standardised-interest-rate-shock-scenarios-and-mathematical-formulations, interest-rate-shock-calibration-methodology-global-scalars-and-caps-floors
- 3 trang cập nhật: interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks, credit-spread-risk-in-the-banking-book-csrbb, economic-value-and-earnings-perspectives-complement-each-other-in-alm; 0 stub mới
- Nguồn hoàn tất 100% (cả 4/4 chunk, 28 concept mới, 18 lượt cập nhật); state file + manifest + index §Sources đã cập nhật

## [2026-09-26:17-13-00] ingest | bcbs_368 đợt mở rộng chuyên sâu vi mô (12 concept kỹ thuật định lượng & quản trị vi mô)
- 12 trang concept chuyên sâu mới: accounting-treatment-of-banking-book-amortised-cost-versus-fair-value-under-irrbb, replicating-portfolio-optimization-methodology-for-nmds-and-equity, pre-acquisition-review-and-hedging-approval-governance-for-irrbb, trapped-capital-and-cross-border-transferability-constraints-under-irrbb, reverse-stress-testing-quantitative-and-qualitative-mechanisms-for-irrbb, yield-curve-interpolation-and-discounting-mechanics-in-alm, effective-duration-and-effective-convexity-for-banking-book-optionalities, balance-sheet-dynamics-assumptions-run-off-constant-and-dynamic-in-alm, funds-transfer-pricing-as-an-irrbb-risk-transfer-and-steering-mechanism, irrbb-model-governance-and-independent-three-tier-validation-framework, macro-hedging-and-micro-hedging-strategies-in-the-banking-book, basis-risk-quantification-and-tenor-basis-swaps-in-alm
- Tổng cộng nguồn bcbs_368 tạo mới 40 concept và 18 lượt cập nhật trang hiện hữu; tổng số trang concept wiki đạt 930 trang; cập nhật 02_wiki/index.md và 03_state/bcbs_368.md

## [2026-09-26:19-33-55] research | FTP Đợt 1 — nền tảng & phân bổ chi phí thanh khoản
- Cluster 10 trang; enrich 4 trang
- 7 claim mới ở 4 trang, 5 liên kết bổ sung, 4 mục ghi _inbox.md; 0 analysis mới
- Báo cáo: Claude outputs/research-2026-09-26-ftp-batch1.md
## [2026-09-26:19-41-22] research | FTP Đợt 2 — cấu trúc VOF/COF TT1 & TT2 và tác nghiệp tại VN
- Cluster 8 trang; enrich 4 trang
- 6 claim mới ở 3 trang, 4 liên kết bổ sung, 5 mục ghi _inbox.md; 0 analysis mới
- Báo cáo: Claude outputs/research-2026-09-26-ftp-batch2.md

## [2026-09-26:19-48-29] research | FTP Đợt 3 — sản phẩm phức tạp & rủi ro hành vi
- Cluster 8 trang; enrich 7 trang
- 11 claim mới ở 7 trang, 6 liên kết bổ sung, 0 mục ghi _inbox.md (đã dọn dẹp trực tiếp); 0 analysis mới
- Báo cáo: Claude outputs/research-2026-09-26-ftp-batch3.md

## [2026-09-26:19-55-22] research | FTP Đợt 4 — điều hướng ALCO, tối ưu bảng cân đối, RAROC/Vốn, FVA & rủi ro mới nổi
- Cluster 8 trang; enrich 8 trang
- 8 claim mới ở 8 trang, 6 liên kết bổ sung, 0 mục ghi _inbox.md (đã dọn dẹp trực tiếp); 0 analysis mới
- Báo cáo: Claude outputs/research-2026-09-26-ftp-batch4.md



