# Index

> Mục lục trang wiki theo chủ đề. Cập nhật mỗi khi có trang mới (xem `.claude/skills/ingest/SKILL.md` bước 6).

## Sources

Trạng thái ingest từng nguồn trong `01_sources/`. **Cập nhật mỗi lượt ingest**, kể cả lượt không tạo trang mới (`ingest/SKILL.md` bước 6). Bảng này chỉ tóm tắt ở cấp nguồn — tiến độ theo chunk của nguồn dài nằm trong `03_state/<tên_nguồn>.md` (`00_schema.md` §10), và đó mới là nguồn sự thật khi cần biết chi tiết "còn lại phần nào".

| Nguồn | Phân loại | Trạng thái | Phần còn lại | State file |
|---|---|---|---|---|
| `imf_macro_accounting` | Nguồn dài (829 KB / 6.065 dòng) | **Đang ingest dở** | Ch.2 và Ch.4 đã xong (Ch.4 tự vượt ngưỡng nguồn dài — 158 KB — nên chia 6 cụm A–F; cụm A–E ingest 2026-09-16, cụm F case Ba Lan bỏ qua vì §2 ưu tiên lý luận trước tường thuật, các concept đã đủ minh chứng — 1 khái niệm tổng quát trong cụm F (tốc độ trượt crawling peg) vẫn được trích ra riêng 2026-09-16). Chưa ingest: Ch.1 (tổng quan chuyển đổi Ba Lan, dù đã trích lẻ nhiều đoạn). Ch.6 (flow of funds) xong 2026-09-16 — phần lớn là gắn 7 cột của bảng flow of funds vào các đồng nhất thức đã ingest ở Ch.2/3/4/5, cộng 6 trang mới về cấu trúc ma trận, quy ước ghi sổ, twin deficits, cơ chế truyền dẫn thâm hụt tài khoá; Exercises và các bảng số liệu Ba Lan sau đó (d.5790+, gồm Table 6.2 đã trích lẻ trước) bỏ qua theo §2. Ch.5 (tiền tệ) xong cả 4 batch (W1–W4) 2026-09-16; case Ba Lan cụ thể (F2, Background for Monetary Analysis) bỏ qua theo §2 — khái niệm liên quan (vòng quay, đô la hoá, lãi suất thực âm) đã bao phủ tổng quát ở W3/W4. Ch.3 phần lý luận xong (cụm A–E), bỏ qua bối cảnh Ba Lan và Exercises (§2) | `03_state/imf_macro_accounting.md` |
| `Modern Money Mechanics` | Nguồn ngắn (83 KB / 721 dòng) | **Chưa ingest** | Toàn bộ — dưới ngưỡng nguồn dài nên ingest trọn 1 lượt, không cần file trạng thái (§10) | — |

## Trang wiki theo chủ đề

**Khung hạch toán**
- [[system-of-national-accounts-sna]] — khung kế toán quốc tế, hub của toàn bộ chuỗi đại lượng
- [[sna-sequence-of-accounts]] — sáu tài khoản nối nhau qua balancing item
- [[institutional-sectors-in-the-sna]] — năm khu vực thể chế cộng phần còn lại của thế giới
- [[sna-records-transactions-on-an-accrual-basis-with-double-entry]] — quy ước ghi nhận
- [[sna-transactions-are-goods-and-services-distributive-or-financial]] — ba loại giao dịch và tồn lượng
- [[residency-in-the-sna-follows-the-centre-of-economic-interest]] — ai là đơn vị cư trú
- [[valuation-in-the-sna]] — giá cơ bản, giá người sản xuất, giá người mua
- [[the-1993-sna-added-balance-sheets-and-fuller-income-accounts]] — khác biệt so với bản 1968
- [[mps-material-product-system]] — khung hạch toán của kinh tế kế hoạch
- [[mps-counts-only-output-of-the-material-sphere]] — MPS loại dịch vụ phi vật chất
- [[converting-mps-net-material-product-to-gdp-requires-four-adjustments]] — quy NMP về GDP
- [[macroeconomic-analysis-divides-the-economy-into-five-main-sectors]] — năm khu vực phân tích và vai trò của từng khu vực

**Đại lượng sản lượng**
- [[value-added]] — giá trị thực sự tạo thêm, đơn vị nền của mọi phép đo sản lượng
- [[gdp]] — tổng value added theo nguyên tắc cư trú
- [[production-income-and-expenditure-approaches-yield-the-same-gdp]] — ba cách đo, một con số
- [[compensation-of-employees]] — W, cấu phần thù lao lao động trong GDP cách thu nhập
- [[operating-surplus]] — OS, thặng dư hoạt động gộp doanh nghiệp, gồm cả khấu hao
- [[taxes-less-subsidies-on-products]] — TSP, cấu phần thứ ba của GDP cách thu nhập
- [[net-domestic-product]] — NDP = GDP − D
- [[measured-gdp-is-an-imperfect-gauge-of-output-and-welfare]] — GDP đo sản xuất và phúc lợi chưa chuẩn ở đâu, vì sao

**Giá và sản lượng thực**
- [[real-gdp]] — sản lượng theo giá cố định
- [[gdp-deflator]] — chỉ số giá của toàn bộ sản lượng
- [[cpi]] — chỉ số giá rổ hàng tiêu dùng, dạng Laspeyres
- [[cpi-and-the-gdp-deflator-differ-in-coverage-import-prices-and-weights]] — ba khác biệt giữa CPI và deflator
- [[laspeyres-and-paasche-indexes-bracket-true-inflation]] — quyền số cố định và quyền số hiện hành lệch hai phía

**Lạm phát**
- [[inflation]] — tăng giá chung kéo dài, phân biệt với giá tương đối
- [[types-of-inflation]] — do chính sách, chi phí đẩy, cầu kéo, quán tính
- [[core-inflation-strips-out-one-time-price-level-jumps]] — tốc độ nền so với con số đo được
- [[a-one-time-price-shock-becomes-inflation-only-if-monetary-policy-accommodates-it]] — điều kiện tiền tệ
- [[inertial-inflation-persists-because-it-is-written-into-contracts]] — vì sao quán tính tự duy trì
- [[indexation]] — điều chỉnh khoản danh nghĩa theo lạm phát; kênh duy trì quán tính
- [[hyperinflation]] — định nghĩa Cagan, ba đặc điểm, Ba Lan 1989

**Đại lượng thu nhập và sử dụng**
- [[gni]] — thu nhập người cư trú kiếm được
- [[net-factor-income-from-abroad]] — Y_f, khoản cộng từ GDP ra GNI
- [[gndi]] — thu nhập khả dụng để tiêu hoặc để dành
- [[net-current-transfers]] — TR_f, khoản cộng từ GNI ra GNDI
- [[net-national-disposable-income]] — NNDI = GNDI − D
- [[absorption]] — tổng cầu nội địa (C + I)
- [[aggregate-demand]] — cầu với hàng trong nước, gồm xuất khẩu ròng
- [[gross-national-saving]] — phần dư sau tiêu dùng
- [[final-consumption]] — phần hộ gia đình và chính phủ sử dụng, đối lập với tiêu dùng trung gian
- [[private-consumption]] — CP, cấu phần tư nhân của C (Box 2.1)
- [[general-government-consumption]] — CG, cấu phần chính phủ của C (Box 2.1)
- [[gross-investment]] — bổ sung vốn vật chất, không phải mua tài sản tài chính
- [[depreciation]] — đại lượng tách mọi cặp gộp/ròng
- [[exports-of-goods-and-nonfactor-services]] — X, cấu phần GDP cách chi tiêu
- [[imports-of-goods-and-nonfactor-services]] — M, cấu phần GDP cách chi tiêu (trừ ra)
- [[net-exports]] — X − M, khác trade-balance ở Ch.4 vì gồm cả dịch vụ
- [[leakages-equal-injections-in-the-circular-flow]] — dòng luân chuyển nối các khu vực, rò rỉ bằng bơm vào

**Đồng nhất thức đối ngoại**
- [[balance-of-payments]] — báo cáo giao dịch với phần còn lại của thế giới
- [[current-account-balance]] — xuất khẩu trừ nhập khẩu, cộng thu nhập nhân tố ròng và chuyển nhượng vãng lai ròng
- [[current-account-deficit-means-absorption-exceeds-national-income]] — GNDI − A = CAB
- [[the-saving-investment-gap-equals-the-current-account-balance]] — S − I = CAB
- [[the-private-sector-resource-gap-must-be-financed-by-other-sectors]] — ràng buộc ngân sách ở cấp khu vực

**Cán cân thanh toán — khung khái niệm (Ch.4 cụm A)**
- [[double-entry-accounting-in-the-balance-of-payments]] — quy ước nợ/có, giao dịch thực vs tài chính
- [[transfers-in-the-balance-of-payments]] — chuyển nhượng vãng lai vs vốn
- [[net-errors-and-omissions]] — khoản mục cân bằng khi dữ liệu không khớp
- [[balance-of-payments-flows-differ-from-international-investment-position-stocks]] — dòng chảy vs tồn kho
- [[valuation-in-the-balance-of-payments]] — giá thị trường, hàng đổi hàng, fob/cif
- [[unit-of-account-in-the-balance-of-payments]] — quy đổi về ngoại tệ ổn định
- [[net-international-investment-position]] — tài sản trừ nợ đối ngoại tại một thời điểm
- [[balance-of-payments-manual-fifth-edition]] — BPM5, khác biệt với BPM4

**Cán cân thanh toán — phân loại chuẩn (Ch.4 cụm B)**
- [[criteria-for-selecting-standard-balance-of-payments-components]] — 4 tiêu chí chọn thành phần chuẩn
- [[current-account-entries-are-recorded-gross-while-capital-and-financial-account-entries-are-net]] — gộp vs ròng
- [[goods-in-the-balance-of-payments]] — hạng mục hàng hóa của tài khoản vãng lai
- [[services-in-the-balance-of-payments]] — vận tải, du lịch, dịch vụ chính phủ, khác
- [[income-in-the-balance-of-payments]] — thù lao người lao động, thu nhập đầu tư
- [[capital-account-in-the-balance-of-payments]] — chuyển nhượng vốn + tài sản phi tài chính không do sản xuất
- [[functional-categories-of-the-financial-account]] — hub 4 nhóm: FDI, portfolio, other investment, reserve assets
- [[direct-investment]] — vốn cổ phần, lợi nhuận tái đầu tư, vốn khác
- [[portfolio-investment]] — chứng khoán nợ/cổ phần dài hạn, công cụ thị trường tiền tệ, phái sinh
- [[other-investment]] — tín dụng thương mại, vay mượn, tín dụng IMF
- [[reserve-assets-in-the-balance-of-payments-are-flows-not-stocks]] — tại sao dự trữ vẫn là biến động
- [[how-imf-transactions-affect-the-balance-of-payments]] — 3 loại giao dịch với IMF
- [[exceptional-financing-in-the-balance-of-payments]] — tái cơ cấu, nợ quá hạn, xóa nợ, debt-equity swap
- [[balance-of-payments-data-quality-problems-in-transition-economies]] — nguồn yếu, ghi thiếu, khó định giá

**Cán cân thanh toán — phân tích vị thế đối ngoại (Ch.4 cụm C)**
- [[above-the-line-and-below-the-line-determine-a-balance-of-payments-surplus-or-deficit]] — cách vẽ đường chia sinh ra thặng dư/thâm hụt
- [[trade-balance]] — cán cân thương mại, chỉ báo sớm cho cán cân vãng lai
- [[overall-balance-of-payments]] — CAB + vốn/tài chính phi tài trợ
- [[current-account-balance-equals-the-change-in-net-foreign-assets]] — CAB + ΔFI + ΔRES = 0
- [[the-lawson-doctrine-that-private-current-account-deficits-need-no-policy-response-is-not-valid]] — vì sao thâm hụt tư nhân vẫn cần theo dõi
- [[current-account-monitoring-depends-on-the-exchange-rate-regime]] — peg vs float quyết định ΔRES hay ΔFI hấp thụ cú sốc
- [[the-rate-of-crawl-under-a-crawling-peg-can-be-set-passively-or-actively]] — trượt bị động theo lạm phát hay chủ động đánh đổi cạnh tranh
- [[solvency-and-sustainability-of-the-current-account]] — PV thặng dư tương lai vs tiếp diễn chính sách hiện hành
- [[analyzing-changes-in-the-structure-of-trade]] — cơ cấu mặt hàng và địa lý của thương mại
- [[outward-oriented-trade-strategies-are-associated-with-successful-exporters]] — chiến lược trung lập và 4 yếu tố khuyến khích xuất khẩu
- [[trade-bias-is-measured-by-the-ratio-of-effective-protection-for-importables-to-exportables]] — tb = ERP(nhập)/ERP(xuất)
- [[assessing-the-appropriateness-of-the-exchange-rate]] — 4 chỉ báo: tỷ giá thực, dự trữ, vãng lai, thị trường song song

**Cán cân thanh toán — tài khoản vốn/tài chính và nợ nước ngoài (Ch.4 cụm D)**
- [[sources-of-current-account-financing-are-fdi-net-borrowing-and-reserve-changes]] — CAB + FDI + NFB + ΔRES ≡ 0
- [[financing-a-current-account-deficit-forces-a-sequence-of-policy-choices]] — thu hút vốn → vay → rút dự trữ → điều chỉnh ép buộc
- [[gross-external-debt-is-defined-by-contractual-and-disbursed-obligations]] — nợ hợp đồng, đã giải ngân
- [[debt-dynamics-equation-links-the-stock-of-external-debt-to-disbursements-and-amortization]] — D_t = D_(t-1) + B_t − A_t
- [[indicators-of-external-debt-burden]] — 3 tỷ số + ngưỡng World Bank
- [[sustainability-of-external-debt]] — Box 4.9, khác solvency vãng lai và khác "viability"
- [[foreign-direct-investment-is-non-debt-creating]] — Box 4.10, chuyển giao công nghệ
- [[government-and-private-capital-flows-have-different-determinants]] — ngân sách vs lợi suất/niềm tin

**Cán cân thanh toán — dự trữ và tài trợ (Ch.4 cụm E)**
- [[net-foreign-assets-of-the-banking-system]] — dự trữ gộp không luôn phản ánh mất cân đối
- [[using-reserve-assets-to-finance-a-deficit-depends-on-whether-it-is-temporary]] — tạm thời thì dùng dự trữ, dai dẳng thì phải điều chỉnh
- [[capital-inflow-surges-pose-four-macroeconomic-management-risks]] — Box 4.11, đảo chiều/lạm phát/lên giá/bùng tiêu dùng
- [[reserve-adequacy-depends-more-on-policy-credibility-than-on-the-exchange-rate-regime]] — case Ba Lan 1991
- [[reserves-to-imports-ratio-measures-reserve-adequacy]] — quy tắc 3 tháng nhập khẩu
- [[reserve-adequacy-indicators-shifted-toward-financial-vulnerability-after-the-1994-mexico-crisis]] — tỷ số cung tiền/dự trữ, kỳ hạn nợ, độ mở

**Lao động và tiền lương**
- [[unemployment-rate]] — cách đo và các sai lệch của nó
- [[discouraged-workers-make-the-unemployment-rate-understate-joblessness]] — người bỏ tìm việc rơi khỏi cả tử lẫn mẫu
- [[full-employment-does-not-mean-zero-unemployment]] — toàn dụng là mức việc làm tối ưu
- [[types-of-unemployment]] — thời vụ, ma sát, chu kỳ, cơ cấu, trá hình
- [[nairu]] — mức thất nghiệp tương thích với lạm phát ổn định
- [[real-wages]] — sức mua của lương, phân biệt với thu nhập thực
- [[real-wage-growth-is-bounded-by-productivity-growth]] — trần dài hạn của tăng lương

**Chính sách giá và thu nhập**
- [[price-liberalization]] — lợi ích và điều kiện đi kèm
- [[exchange-rate]] — giá bị méo, neo danh nghĩa, chịu tác động của tài trợ thâm hụt
- [[nominal-anchor]] — biến danh nghĩa được cố định để neo kỳ vọng lạm phát
- [[open-trade-and-a-convertible-currency-are-the-fastest-route-to-rational-relative-prices]] — giá hợp lý bám giá thế giới
- [[price-convergence-keeps-pressure-on-inflation-through-the-transition]] — vì sao áp lực giá kéo dài, tỷ giá thực tăng
- [[incomes-policy]] — ba cách tiếp cận và lý do dùng
- [[designing-wage-controls-means-choosing-a-norm-indexation-coverage-and-enforcement]] — bốn bước thiết kế
- [[wage-controls-lose-effectiveness-rapidly-after-a-short-period]] — vì sao chỉ nên tạm thời

**Đo lường trong kinh tế chuyển đổi**
- [[transition-statistics-understate-private-sector-growth]] — sai lệch ở khâu bao phủ
- [[a-real-output-index-needs-prices-that-reflect-relative-scarcity]] — sai lệch ở khâu định giá

**Case: Ba Lan 1989–1994**
- [[polands-output-collapse-1990-91-came-from-three-distinct-causes]] — vĩ mô, thể chế, đo lường
- [[to-what-extent-was-polands-output-decline-1990-91-overstated]] — câu hỏi còn để ngỏ
- [[polands-recovery-from-1992-was-led-by-consumption-then-exports]] — phục hồi 1992–94
- [[polish-national-saving-fell-sharply-at-the-onset-of-transition]] — tiết kiệm rơi mạnh; ⚠️ nguồn mâu thuẫn về năm 1992
- [[polish-price-liberalization-left-inflation-stuck-at-30-percent]] — thả giá và lạm phát nền
- [[polands-excess-wage-tax-popiwek-was-discontinued-after-five-years]] — kiểm soát lương trên thực tế
- [[polish-real-wages-stabilized-but-lagged-productivity-gains]] — lương thực hồi nhẹ, tụt sau năng suất
- [[polands-1992-sna-accounts-show-government-dissaving-and-household-saving]] — tài khoản SNA 1992 theo khu vực; ⚠️ nguồn mâu thuẫn về tiết kiệm gộp
- [[polish-unemployment-rose-from-near-zero-to-16-percent-in-four-years]] — từ thất nghiệp trá hình sang công khai

**Khung kế toán tài khoá (GFS)**
- [[government-finance-statistics-gfs]] — khung thống kê tài chính chính phủ của IMF, hub của cụm
- [[general-government]] — các cấp chính quyền, public sector, hợp nhất, ranh giới với khu vực tiền tệ
- [[extrabudgetary-and-counterpart-funds-distort-the-measured-fiscal-position]] — hai nguồn méo số liệu tài khoá
- [[gfs-records-government-transactions-on-a-cash-basis]] — tiền mặt thay vì dồn tích, và vì sao
- [[payments-arrears-split-the-cash-deficit-from-the-accrual-deficit]] — nợ đọng làm hai con số thâm hụt lệch nhau
- [[government-revenue-is-a-receipt-that-creates-no-repayment-obligation]] — thu, thuế, thu ngoài thuế, lợi nhuận NHTW
- [[grants-are-better-treated-as-financing-in-fiscal-analysis]] — viện trợ không bền nên đặt dưới dòng
- [[government-net-lending-is-classed-as-expenditure-because-its-motive-is-policy]] — cho vay vì chính sách, nợ bảo lãnh
- [[bank-recapitalization-enters-the-gfs-deficit-only-through-interest]] — nhận nợ phi tiền mặt
- [[privatization-receipts-are-an-asset-exchange-not-deficit-reduction]] — giảm thâm hụt một lần là ảo
- [[conventional-fiscal-deficit]] — định nghĩa và hai hạn chế
- [[state-owned-enterprises]] — doanh nghiệp công trong GFS và trong chuyển đổi

**Đo thâm hụt tài khoá**
- [[government-saving-investment-gap-approximates-the-overall-fiscal-deficit]] — ràng buộc ngân sách của khu vực chính phủ và ba nguồn lấp
- [[the-right-fiscal-deficit-measure-depends-on-the-question-asked]] — bốn yếu tố chọn thước đo
- [[public-sector-borrowing-requirement]] — thước đo rộng nhất
- [[current-fiscal-deficit]] — thu thường xuyên trừ chi thường xuyên
- [[current-fiscal-deficit-rests-on-an-arbitrary-capital-current-split]] — vì sao cán cân thường xuyên ít hữu ích
- [[primary-deficit]] — chính sách tuỳ nghi hiện tại và nợ
- [[operational-deficit]] — tách phần lãi bù lạm phát

**Tài trợ thâm hụt**
- [[each-way-of-financing-a-deficit-carries-its-own-macroeconomic-imbalance]] — hub: bốn cách, bốn mất cân đối
- [[monetizing-the-deficit-creates-high-powered-money-and-inflation]] — vay ngân hàng trung ương
- [[government-borrowing-from-commercial-banks-either-monetizes-or-crowds-out]] — tùy ngân hàng trung ương có nới dự trữ
- [[nonbank-deficit-financing-postpones-inflation-but-raises-future-debt-costs]] — trái phiếu trong nước
- [[external-deficit-financing-is-limited-by-reserves-and-creditworthiness]] — vay nước ngoài, rút dự trữ
- [[crowding-out]] — chi tiêu, vay công lấn chi tiêu tư qua lãi suất
- [[seigniorage]] — nguồn thu từ phát hành tiền, tách thành phần thuần và thuế lạm phát
- [[pure-seigniorage]] — thành phần đến từ tăng trưởng thực/cầu tiền dịch chuyển
- [[inflation-tax]] — thành phần đến từ lạm phát nhân số dư tiền thực
- [[inflation-tax-revenue-peaks-because-high-inflation-shrinks-its-base]] — đường chữ U ngược

**Nợ công và tính bền vững**
- [[fiscal-sustainability]] — hub: định nghĩa đồng thuận, ổn định nợ và khả năng thanh toán
- [[real-interest-rate]] — lãi suất trừ lạm phát kỳ vọng; biến trung tâm của bền vững nợ
- [[high-debt-ratios-raise-real-interest-rates-and-erode-market-confidence]] — nợ cao tốn kém rồi mất bền
- [[public-debt-dynamics-depend-on-the-primary-balance-seigniorage-and-the-interest-growth-gap]] — phương trình động học nợ
- [[when-interest-exceeds-growth-a-permanent-primary-deficit-cannot-exceed-seigniorage]] — hai chế độ r > g và r < g
- [[stabilizing-the-debt-ratio-caps-the-deficit-at-debt-times-nominal-growth]] — mục tiêu ngân sách để ổn định nợ
- [[government-solvency-is-a-forward-looking-balance-sheet]] — ràng buộc liên thời gian, tài sản ròng
- [[fiscal-sustainability-indicators-measure-the-adjustment-needed]] — hub ba chỉ số
- [[primary-gap]] — PDV cân đối cơ bản ổn định nợ trừ cân đối thực tế
- [[medium-term-tax-gap]] — điều chỉnh tỷ lệ thuế cần để ổn định nợ
- [[ricardian-equivalence]] — vay nợ là thuế hoãn lại? bằng chứng yếu
- [[expenditure-arrears-raise-the-cost-of-providing-government-services]] — nợ đọng chi tiêu

**Phân tích thu**
- [[ad-hoc-revenue-increases-build-distortionary-tax-systems-that-still-underyield]] — tăng thu chắp vá
- [[tax-elasticity]] — số thu tăng theo GDP khi hệ thống thuế giữ nguyên
- [[tax-buoyancy-exceeds-elasticity-when-discretionary-changes-raise-revenue]] — độ nổi so với độ co giãn
- [[collection-lags-erode-real-tax-revenue-under-high-inflation]] — độ trễ thu khi lạm phát cao
- [[tax-effort-compares-revenue-with-taxable-capacity-not-gdp]] — nỗ lực thuế và năng lực thuế
- [[tanzi-diagnostic-test]] — tám kiểm tra năng suất thu

**Phân tích chi**
- [[public-expenditure-analysis-rests-on-five-elements]] — khung đánh giá mức và cơ cấu chi
- [[public-goods]] — tiêu dùng tập thể, thị trường không cung ứng
- [[public-spending-poses-three-problems-level-efficiency-and-mix]] — mức, hiệu quả, cơ cấu; vĩ mô và cấu trúc
- [[low-public-spending-ratios-can-reflect-weak-financing-capacity-not-a-small-state]] — vai trò nhà nước
- [[civil-service-pay-policy-shapes-government-spending-efficiency]] — lương công vụ
- [[underspending-on-operations-and-maintenance-erodes-existing-capital]] — vận hành và bảo dưỡng
- [[wages-and-salaries-expenditure]] — chi lương công chức
- [[government-goods-and-services-expenditure]] — chi phí hành chính, vận hành
- [[government-capital-expenditure]] — đầu tư công có tính sản xuất
- [[subsidies]] — định nghĩa, bảy dạng, công khai và ngầm
- [[effective-subsidies-are-targeted-temporary-transparent-and-budget-financed]] — năm tiêu chí đánh giá trợ cấp
- [[public-investment-should-complement-rather-than-compete-with-markets]] — chi đầu tư
- [[social-safety-nets-trade-targeting-against-work-incentives]] — lưới an sinh
- [[quasi-fiscal-operations]] — hoạt động bán tài khoá của ngân hàng trung ương và ngân hàng công
- [[sequestering-expenditures-is-an-emergency-cut-that-distorts-allocation]] — phong toả chi
- [[public-expenditure-raises-supply-in-the-long-run-but-crowds-out-private-spending]] — tác động vĩ mô
- [[in-transition-economies-extra-spending-can-worsen-financing-through-inflation]] — vòng chi – lạm phát – thu

**Stub — khái niệm đã có tên, chờ nội dung**
- [[macroeconomic-sectors]] — các khu vực vĩ mô và tương tác giữa chúng
- [[soft-budget-constraint]] — ràng buộc ngân sách doanh nghiệp lách được nhờ nhà nước, ngân hàng
- [[nonbank-financial-institutions]] — tầng thứ ba của thống kê tài chính IFS

**Ch.5 — cấu trúc hệ thống tiền tệ và nhà chức trách tiền tệ (batch W1)**
- [[financial-statistics-are-organized-in-three-tiers-from-institutional-balance-sheets-to-the-financial-survey]] — bảng cân đối riêng → khảo sát tiền tệ → khảo sát tài chính
- [[central-bank]] — nhà chức trách tiền tệ: định nghĩa chức năng, vai trò, người cho vay cuối cùng
- [[deposit-money-banks]] — 4 vai trò, dự trữ phân đoạn, cầu dự trữ
- [[monetary-statistics-are-stock-data-recorded-on-a-cash-basis]] — tồn kho, cơ sở tiền mặt
- [[foreign-currency-items-in-monetary-statistics-are-converted-at-the-end-period-exchange-rate]] — tỷ giá cuối kỳ cho tồn kho, khác BOP
- [[consolidation-nets-out-inter-entity-claims-unlike-aggregation]] — hợp nhất triệt tiêu khoản mục liên thực thể
- [[money-serves-as-a-medium-of-exchange-store-of-value-and-unit-of-account]] — ba chức năng của tiền
- [[money-aggregates-form-a-nested-hierarchy-from-narrow-money-to-broad-liquidity]] — M1 ⊂ M2 ⊂ M3 ⊂ M4 ⊂ L
- [[quasi-money]] — QM, tiền gửi có kỳ hạn/tiết kiệm, số hạng TD trong M2
- [[the-typical-monetary-authorities-balance-sheet-itemizes-foreign-assets-and-shows-reserve-money-by-holder]] — bảng cân đối thô Box 5.1, trước khi rút gọn thành đồng nhất thức RM
- [[the-analytical-monetary-authorities-balance-sheet-groups-items-into-nfa-nda-and-rm]] — bảng phân tích gọn Box 5.2, lớp trung gian giữa Box 5.1 và đồng nhất thức RM
- [[the-typical-deposit-money-bank-balance-sheet-groups-assets-by-counterparty-and-liabilities-by-instrument]] — bảng cân đối thô Box 5.5, tài sản theo đối tác/nợ theo công cụ
- [[the-analytical-deposit-money-bank-balance-sheet-separates-required-from-excess-reserves]] — bảng phân tích gọn Box 5.6, dự trữ bắt buộc/vượt mức
- [[required-reserves]] — r, r_d, r_t; dòng Required trên bảng phân tích DMB
- [[excess-reserves]] — r_e; lựa chọn của DMB, không phải chỉ tiêu chính sách
- [[monetary-accounts-net-claims-on-government-but-keep-claims-on-deposit-money-banks-gross]] — vì sao tín dụng cho chính phủ bị trừ tiền gửi còn tín dụng cho DMB thì không

**Ch.5 — cân đối: đồng nhất thức tiền tệ, cầu tiền, tỷ giá (batch W2)**
- [[reserve-money]] — RM ≡ NFA*+NCG*+CDMB*+CPS*+OIN*
- [[money-supply-equals-net-foreign-assets-plus-net-domestic-assets]] — M2 = NFA + NDC + OIN_b
- [[change-in-net-foreign-assets-links-the-monetary-survey-to-the-balance-of-payments]] — ΔNFA = CAB + ΔFI = -ΔRES, cách tiếp cận tiền tệ với BOP
- [[the-money-multiplier-links-reserve-money-to-the-money-supply]] — mm = (c+1)/(c+r)
- [[the-quantity-theory-links-money-velocity-prices-and-output]] — MV = PY
- [[demand-for-money-is-a-demand-for-real-balances-driven-by-income-and-opportunity-cost]] — cầu số dư tiền thực
- [[assets-are-held-based-on-expected-return-risk-and-liquidity]] — lợi suất, rủi ro, thanh khoản
- [[real-interest-rate]] — Rᵣ ≈ Rₙ − Pₑ (đã bổ sung Ch.5)
- [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks]] — Eₜ, VAd (Box 5.8)

**Ch.5 — cơ chế vận hành chính sách tiền tệ (batch W3)**
- [[monetary-authorities-influence-reserve-money-through-five-direct-instruments]] — can thiệp ngoại hối, thị trường mở, tài trợ thâm hụt, chiết khấu, dự trữ bắt buộc
- [[monetary-authorities-control-over-reserve-money-is-incomplete]] — NFA và NCG một phần nằm ngoài tầm chính sách
- [[fixed-exchange-rates-make-the-money-supply-endogenous-while-floating-rates-restore-monetary-control]] — cố định = nội sinh, thả nổi = toàn quyền
- [[sterilization-offsets-fx-intervention-but-only-temporarily]] — tiệt trùng và giới hạn, hội đồng tiền tệ
- [[perfect-capital-mobility-with-a-fixed-exchange-rate-strips-monetary-policy-of-independence]] — lãi suất trong nước bị ép về mức thế giới
- [[currency-substitution-undermines-monetary-control]] — đô la hoá
- [[financial-innovation-blurs-the-boundary-of-money]] — đổi mới tài chính, đánh đổi liên quan/kiểm soát

**Ch.5 — đặc thù kinh tế chuyển đổi + kỹ thuật IMF (batch W4)**
- [[transition-economies-experience-large-discrete-jumps-in-money-velocity]] — vòng quay tiền nhảy bậc, phục hồi chậm
- [[underdeveloped-banking-competition-and-financial-markets-limit-indirect-monetary-control-in-transition-economies]] — vì sao công cụ gián tiếp khó dùng
- [[interenterprise-arrears-substitute-for-bank-credit-when-budget-constraints-are-not-hardened]] — nợ đọng liên doanh nghiệp
- [[high-government-financing-needs-subordinate-monetary-policy-to-fiscal-needs]] — chính sách tiền tệ lệ thuộc ngân sách
- [[imf-quota-and-credit-tranches-determine-a-members-reserve-position-in-the-fund]] — quota, hạn mức tín dụng, RPF
- [[quota-payment-and-reserve-tranche-drawdowns-leave-net-foreign-assets-unchanged-while-credit-tranche-purchases-do-not]] — NPF = RPF - UFC = Q - H
- [[a-worked-example-shows-how-monetary-authorities-dmb-and-nbfi-balance-sheets-reconcile-into-the-financial-survey]] — case số liệu 4 bảng cân đối khớp nhau

**Ch.6 — flow of funds: ghép các cân đối khu vực vào một ma trận**
- [[the-flow-of-funds-table-is-a-zero-sum-quadruple-entry-matrix]] — cấu trúc cột-khu vực/hàng-giao dịch, tính chất tổng-bằng-0
- [[flow-of-funds-recording-conventions-govern-coverage-source-selection-and-sign]] — phạm vi, chọn nguồn, quy ước ngân hàng/đối ngoại, quy ước dấu
- [[the-flow-of-funds-table-decomposes-the-economy-wide-identity-into-sector-columns]] — 7 cột của bảng ứng với các đồng nhất thức đã ingest
- [[the-flow-of-funds-approach-treats-sectoral-balances-as-constraints-unlike-market-equilibrium-models]] — khác biệt phương pháp luận với cân bằng thị trường
- [[twin-deficits-describes-the-co-movement-of-the-fiscal-and-current-account-balances]] — vì sao thâm hụt ngân sách và thâm hụt vãng lai không di chuyển cùng chiều một cách tất yếu
- [[fiscal-imbalance-transmits-differently-to-the-private-sector-depending-on-how-it-is-financed]] — tài trợ bằng thuế so với bằng tín dụng ngân hàng trung ương tác động khác nhau tới khu vực tư và cán cân vãng lai
- [[a-real-flow-of-funds-table-must-reconcile-gfs-nipa-and-bop-data-recorded-on-different-bases]] — dựng bảng thật từ Table 6.6 (Ba Lan) đòi hỏi tính lại chỉ tiêu để dung hoà cơ sở ghi nhận khác nhau giữa các hệ thống nguồn
