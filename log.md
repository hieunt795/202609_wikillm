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
