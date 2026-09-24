# Index

> Mục lục trang wiki theo chủ đề. Cập nhật mỗi khi có trang mới (xem `.claude/skills/ingest/SKILL.md` bước 6).

## Sources

Trạng thái ingest từng nguồn trong `01_sources/`. **Cập nhật mỗi lượt ingest**, kể cả lượt không tạo trang mới (`ingest/SKILL.md` bước 6). Bảng này chỉ tóm tắt ở cấp nguồn — tiến độ theo chunk của nguồn dài nằm trong `03_state/<tên_nguồn>.md` (`00_schema.md` §10), và đó mới là nguồn sự thật khi cần biết chi tiết "còn lại phần nào".

| Nguồn | Phân loại | Trạng thái | Phần còn lại | State file |
|---|---|---|---|---|
| `imf_macro_accounting` | Nguồn dài (849 KB / 6.065 dòng) | **Đang ingest dở** | Ch.1; Ch.2–6 xong (chi tiết theo chunk ở state file) | `03_state/imf_macro_accounting.md` |
| `Modern Money Mechanics` | Nguồn ngắn (85 KB / 721 dòng) | **Chưa ingest** | Toàn bộ, ingest trọn 1 lượt | — |
| `capitalism_and_freedom` | Nguồn dài (565 KB / 2.055 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |
| `bindseil_monetary_policy` | Nguồn dài (1.155 KB / 4.473 dòng) | **Hoàn tất 100%** | Toàn bộ Ch.1–18 xong (chi tiết ở state file) | `03_state/bindseil_monetary_policy.md` |
| `cargill_central_bank_policy` | Nguồn dài (1.206 KB / 5.623 dòng) | **Hoàn tất 100%** | Toàn bộ Ch.1–17 xong (chi tiết ở state file) | `03_state/cargill_central_bank_policy.md` |
| `choudhry_principles_of_banking` | Nguồn dài (2.664 KB / 14.955 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |
| `choudhry_analysing_yield_curve` | Nguồn dài (703 KB / 6.177 dòng) | **Hoàn tất 100%** | Toàn bộ Ch.1–13 xong (chi tiết ở state file) | `03_state/choudhry_analysing_yield_curve.md` |
| `choudhry_fixed_income_markets` | Nguồn dài (1.941 KB / 15.414 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |
| `fixed_income_during` | Nguồn dài (42 file, 1.112 KB / 7.300 dòng) | **Hoàn tất 100%** | Toàn bộ Ch.1–39 xong (chi tiết ở state file) | `03_state/fixed_income_during.md` |
| `tata_bank_alm` | Nguồn dài (450 KB / 3.345 dòng) | **Hoàn tất 100%** | Toàn bộ Ch.1–6 xong (chi tiết ở state file) | `03_state/tata_bank_alm.md` |
| `clippings` | Nguồn dài (82 file, 882 KB / 6.684 dòng) | **Hoàn tất 100%** | Toàn bộ 6 cụm (82 file) xong (chi tiết ở state file) | `03_state/clippings.md` |

Khoá ở cột *Nguồn* là source id (`03_state/_sources_manifest.md`). Ô *Phần còn lại* chỉ ghi một câu; diễn biến từng lượt nằm ở `log.md`, tiến độ theo chunk nằm ở state file.

## Trang wiki theo chủ đề

**Khung hạch toán**
- [[system-of-national-accounts-sna]] — khung kế toán quốc tế, hub của toàn bộ chuỗi đại lượng
- [[sna-sequence-of-accounts]] — sáu tài khoản nối nhau qua balancing item
- [[institutional-sectors-in-the-sna]] — năm khu vực thể chế cộng phần còn lại của thế giới
- [[sna-records-transactions-on-an-accrual-basis-with-double-entry]] — quy ước ghi nhận
- [[sna-transactions-are-goods-and-services-distributive-or-financial]] — ba loại giao dịch và tồn lượng
- [[residency-in-the-sna-follows-the-centre-of-economic-interest]] — ai là đơn vị cư trú
- [[valuation-in-the-sna]] — giá cơ bản, giá người sản xuất, giá người mua
- [[the-1993-sna-revised-the-1968-system-in-five-ways]] — khác biệt so với bản 1968
- [[mps-material-product-system]] — khung hạch toán của kinh tế kế hoạch
- [[mps-counts-only-output-of-the-material-sphere]] — MPS loại dịch vụ phi vật chất
- [[converting-mps-net-material-product-to-gdp-requires-four-adjustments]] — quy NMP về GDP
- [[macroeconomic-analysis-divides-the-economy-into-five-main-sectors]] — năm khu vực phân tích và vai trò của từng khu vực
- [[sectoral-interactions]] — giao dịch thu–chi của mỗi khu vực sinh giao dịch tài chính với khu vực khác; $(S_p-I_p)+(S_g-I_g)=CAB$

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
- [[potential-gdp-measures-productive-capacity-at-full-employment]] — sản lượng tối đa khi toàn dụng lao động với công nghệ và cấu trúc hiện có
- [[gdp-gap-measures-deviation-of-actual-output-from-potential]] — (Y − Y*)/Y*, chỉ báo vị thế chu kỳ kinh doanh
- [[okuns-law-relates-the-gdp-gap-to-the-unemployment-gap]] — liên kết khoảng cách GDP với khoảng cách thất nghiệp
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
- [[deflation]] — giảm phát: mức giá chung sụt giảm liên tục, tỷ lệ lạm phát âm

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
- [[stocks-accumulate-transaction-flows-plus-revaluation-and-other-changes-and-feed-back-into-future-flows]] — *(analysis)* stock = stock kỳ trước + giao dịch + định giá lại + thay đổi khác; stock sinh flow kỳ sau
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
- [[trade-data-by-commodity-and-partner-separates-structural-from-temporary-trade-shocks]] — cơ cấu mặt hàng và địa lý của thương mại
- [[outward-oriented-trade-strategies-are-associated-with-successful-exporters]] — chiến lược trung lập và 4 yếu tố khuyến khích xuất khẩu
- [[trade-bias-is-measured-by-the-ratio-of-effective-protection-for-importables-to-exportables]] — tb = ERP(nhập)/ERP(xuất)
- [[exchange-rate-appropriateness-is-judged-by-four-indicator-groups-none-sufficient-alone]] — 4 chỉ báo: tỷ giá thực, dự trữ, vãng lai, thị trường song song

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
- [[reserve-adequacy-indicators-shifted-toward-financial-vulnerability-after-the-1994-mexico-crisis]] — Guidotti-Greenspan, nợ ngắn hạn, tỷ số cung tiền/dự trữ, kỳ hạn nợ, độ mở
- [[foreign-exchange-reserves]] — dự trữ ngoại hối: tài sản ngoại tệ do NHTW nắm giữ để can thiệp và hỗ trợ tỷ giá
- [[capital-flight]] — vốn chuyển ra khi mất lòng tin; rủi ro khi dự trữ sắp cạn, kể cả dưới thả nổi có quản lý

**Tài sản dự trữ, giao dịch với IMF, tài trợ đặc biệt — thành phần (§5, lượt C)**
- [[foreign-exchange-reserve-assets]] — tiền mặt, tiền gửi, chứng khoán ngoại tệ; dự trữ gộp không đo quy mô mất cân đối
- [[monetary-gold]] — vàng dự trữ; vàng phi tiền tệ là hàng hoá; tiền tệ hoá vàng không ghi dòng
- [[special-drawing-rights-sdr]] — tài sản dự trữ do IMF tạo; phân bổ mới chỉ đổi tồn lượng (BPM5), làm NFA tăng
- [[reserve-position-in-the-imf]] — phần quota nộp bằng dự trữ và nội tệ IMF đã dùng; nộp quota không đổi NFA
- [[use-of-imf-credit]] — mua ngoại tệ của IMF; "đầu tư khác, khoản vay" trong BOP, nợ đối ngoại của MA
- [[government-deposits]] — trừ vào tín dụng cho chính phủ, không tính vào tiền dự trữ
- [[treasury-bills]] — khoản mục tín dụng cho chính phủ; công cụ của nghiệp vụ thị trường mở
- [[debt-rescheduling]] — hoãn trả nợ bằng hợp đồng mới; chi phối tài khoản vốn Ba Lan 1991–93
- [[arrears-on-external-debt-servicing]] — lãi/gốc quá hạn; lãi quá hạn ghi như trả bằng vay ngắn hạn
- [[debt-forgiveness]] — chủ nợ chính thức huỷ nợ; chuyển nhượng trong tài khoản vốn
- [[debt-equity-swaps]] — đổi khoản nợ lấy vốn cổ phần của người không cư trú; đầu tư trực tiếp đặc biệt

**Lao động và tiền lương**
- [[unemployment-rate]] — cách đo và các sai lệch của nó
- [[u6-unemployment-rate-captures-discouraged-and-underemployed-workers]] — thước đo thất nghiệp mở rộng tích hợp lao động nản chí và bán thời gian bắt buộc
- [[discouraged-workers-make-the-unemployment-rate-understate-joblessness]] — người bỏ tìm việc rơi khỏi cả tử lẫn mẫu
- [[full-employment-does-not-mean-zero-unemployment]] — toàn dụng là mức việc làm tối ưu
- [[natural-rate-of-unemployment-equals-frictional-plus-structural-unemployment]] — mức thất nghiệp tự nhiên bằng cọ xát cộng cơ cấu khi GDP gap = 0
- [[types-of-unemployment]] — thời vụ, ma sát, chu kỳ, cơ cấu, trá hình
- [[nairu]] — mức thất nghiệp tương thích với lạm phát ổn định
- [[real-wages]] — sức mua của lương, phân biệt với thu nhập thực
- [[real-wage-growth-is-bounded-by-productivity-growth]] — trần dài hạn của tăng lương

**Chính sách giá và thu nhập**
- [[price-liberalization]] — lợi ích và điều kiện đi kèm
- [[exchange-rate]] — giá bị méo, neo danh nghĩa, chịu tác động của tài trợ thâm hụt
- [[real-exchange-rate]] — tỷ giá danh nghĩa điều chỉnh theo chi phí lao động đơn vị/giá tương đối; thước đo sức cạnh tranh
- [[exchange-rate-regimes]] — cố định, rổ tiền, trượt công bố trước, thả nổi có quản lý, thả nổi; quyết định mức tự chủ tiền tệ
- [[devaluation]] — hạ giá trị chính thức của nội tệ; tăng giá một lần; cần khi thâm hụt vãng lai không tài trợ được
- [[currency-board]] — tiền dự trữ chỉ phát hành khi có đủ ngoại tệ; không trung hoà được; Estonia, Lithuania
- [[nominal-anchor]] — biến danh nghĩa được cố định để neo kỳ vọng lạm phát
- [[open-trade-and-a-convertible-currency-are-the-fastest-route-to-rational-relative-prices]] — giá hợp lý bám giá thế giới
- [[price-convergence-keeps-pressure-on-inflation-through-the-transition]] — vì sao áp lực giá kéo dài, tỷ giá thực tăng
- [[incomes-policy]] — ba cách tiếp cận và lý do dùng
- [[designing-wage-controls-means-choosing-a-norm-indexation-coverage-and-enforcement]] — bốn bước thiết kế
- [[wage-controls-lose-effectiveness-rapidly-after-a-short-period]] — vì sao chỉ nên tạm thời
- [[soft-budget-constraint]] — doanh nghiệp lách ràng buộc ngân sách nhờ chính phủ/ngân hàng; tự do hoá giá là điều kiện cứng hoá

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
- [[polands-exchange-rate-path-from-dollar-peg-to-managed-float-balanced-disinflation-and-competitiveness]] — bốn chế độ tỷ giá 1990–95
- [[polands-exchange-rate-experience-yields-five-policy-lessons]] — năm bài học chính sách tỷ giá rút từ kinh nghiệm Ba Lan

**Chính sách vĩ mô và tổ chức quốc tế**
- [[monetary-policy]] — nhà chức trách tiền tệ điều tiết tiền qua tiền dự trữ; tự chủ phụ thuộc chế độ tỷ giá và nhu cầu tài trợ của chính phủ
- [[fiscal-policy]] — thuế, chi tiêu công, vay nợ; tác động trực tiếp lên tổng cầu
- [[international-monetary-fund-imf]] — bên cho vay, bên tạo SDR, bên ban hành chuẩn thống kê (BPM5, GFS, IFS)

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
- [[tanzi-concentration-index]] — Tanzi 1: số thu đến từ ít sắc thuế, ít thuế suất
- [[tanzi-dispersion-index]] — Tanzi 2: ít hoặc không có sắc thuế thu ít mà phiền hà
- [[tanzi-erosion-index]] — Tanzi 3: cơ sở thuế thực tế sát cơ sở tiềm năng
- [[tanzi-collection-lags-index]] — Tanzi 4: nộp thuế không trễ; quan trọng khi lạm phát cao
- [[tanzi-specificity-index]] — Tanzi 5: ít sắc thuế theo mức cố định; gắn với độ co giãn
- [[tanzi-objectivity-index]] — Tanzi 6: thuế đánh trên cơ sở đo được khách quan
- [[tanzi-enforcement-index]] — Tanzi 7: hệ thống được thực thi đầy đủ, hiệu quả
- [[tanzi-cost-of-collection-index]] — Tanzi 8: chi phí thu thuế thấp nhất có thể

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
- [[targeted-commodity-subsidies-and-cash-compensation]] — lưới an sinh 1: giữ sức mua lương thực cơ bản khi lạm phát
- [[social-security-arrangements]] — lưới an sinh 2: lương hưu, tàn tật, nuôi con; hệ thống hưu trí Ba Lan
- [[unemployment-benefits-and-public-works]] — lưới an sinh 3: trợ cấp thất nghiệp Ba Lan 12 tháng, 36% lương bình quân
- [[exchange-rate-subsidies]] — trợ cấp qua tỷ giá; hoạt động bán tài khoá
- [[credit-subsidies]] — cho vay dưới lãi suất chính phủ, có bảo lãnh; hoạt động bán tài khoá
- [[exchange-rate-guarantees-and-other-contingent-liabilities]] — nghĩa vụ chưa có nguồn/tiềm tàng; hoạt động bán tài khoá
- [[cash-grant-subsidies]] — trợ cấp tiền mặt; hình thức minh bạch nhất
- [[tax-subsidies]] — giảm nghĩa vụ thuế cụ thể
- [[in-kind-subsidies]] — cung ứng dưới giá thị trường; giá năng lượng thấp gây lãng phí
- [[procurement-subsidies]] — chính phủ mua trên giá thị trường
- [[regulatory-subsidies]] — trả ngầm qua quy định làm đổi giá hoặc quyền tiếp cận thị trường
- [[implicit-subsidies]] — trợ cấp không hiện ra trong ngân sách; khó kiểm soát hơn trợ cấp công khai

**Ch.5 — cấu trúc hệ thống tiền tệ và nhà chức trách tiền tệ (batch W1)**
- [[financial-statistics-are-organized-in-three-tiers-from-institutional-balance-sheets-to-the-financial-survey]] — bảng cân đối riêng → khảo sát tiền tệ → khảo sát tài chính
- [[central-bank]] — nhà chức trách tiền tệ: định nghĩa chức năng, vai trò, người cho vay cuối cùng
- [[nonbank-financial-institutions]] — bảo hiểm, quỹ tương hỗ, hưu trí, quỹ thị trường tiền tệ; tầng thứ ba của IFS
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
- [[consolidation-of-monetary-authorities-and-dmb-accounts-eliminates-internal-claims-to-determine-broad-money]] — *(analysis)* hợp nhất MA và DMB loại trừ trái quyền nội bộ, chuyển RM thành M2 qua số nhân và đối ứng NFA/NDA
- [[change-in-net-foreign-assets-links-the-monetary-survey-to-the-balance-of-payments]] — ΔNFA = CAB + ΔFI = -ΔRES, cách tiếp cận tiền tệ với BOP
- [[the-money-multiplier-links-reserve-money-to-the-money-supply]] — mm = (c+1)/(c+r)
- [[the-quantity-theory-links-money-velocity-prices-and-output]] — MV = PY
- [[demand-for-money-is-a-demand-for-real-balances-driven-by-income-and-opportunity-cost]] — cầu số dư tiền thực
- [[assets-are-held-based-on-expected-return-risk-and-liquidity]] — lợi suất, rủi ro, thanh khoản
- [[real-interest-rate]] — Rᵣ ≈ Rₙ − Pₑ (đã bổ sung Ch.5)
- [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks]] — Eₜ, VAd (Box 5.8)

**Ch.5 — thành phần của các đồng nhất thức tiền tệ (§5, lượt B)**
- [[currency-in-circulation]] — CY, tiền mặt ngoài ngân hàng; khác tiền đã phát hành; tham số $c$ của số nhân
- [[demand-deposits]] — DD, rút ngay; mẫu số của các tỷ lệ trong số nhân tiền
- [[narrow-money-m1]] — $M1 = CY + DD$; $M2 = M1 + QM$
- [[net-domestic-assets]] — NDA; $M2 = NFA + NDA$, $NDA = NDC + OIN_b$
- [[net-domestic-credit]] — NDC; tín dụng ròng cho chính phủ cộng tín dụng cho khu vực khác
- [[net-credit-to-government]] — NCG, ghi ròng tiền gửi chính phủ; phần tạo tiền mạnh
- [[credit-to-the-private-sector]] — CPS; nhỏ ở ngân hàng trung ương, dấu hiệu lấn át ở Ba Lan
- [[claims-on-deposit-money-banks]] — CDMB, ghi gộp; lãi suất chiết khấu là công cụ chính sách
- [[other-items-net]] — OIN, nhóm còn lại; chứa điều chỉnh định giá tỷ giá và đối ứng phân bổ SDR
- [[foreign-currency-deposits]] — FC; thước đo đô la hoá, thuộc M2

**Ch.5 — cơ chế vận hành chính sách tiền tệ (batch W3)**
- [[monetary-authorities-influence-reserve-money-through-five-direct-instruments]] — can thiệp ngoại hối, thị trường mở, tài trợ thâm hụt, chiết khấu, dự trữ bắt buộc
- [[monetary-authorities-control-over-reserve-money-is-incomplete]] — NFA và NCG một phần nằm ngoài tầm chính sách
- [[fixed-exchange-rates-make-the-money-supply-endogenous-while-floating-rates-restore-monetary-control]] — cố định = nội sinh, thả nổi = toàn quyền
- [[sterilization-offsets-fx-intervention-but-only-temporarily]] — nghiệp vụ trung hòa và giới hạn, hội đồng tiền tệ
- [[central-bank-balance-sheet-sterilization-capacity-depends-on-financial-market-depth-and-institutional-independence]] — *(analysis)* năng lực trung hòa bảng cân đối: đối chiếu quan điểm kiểm soát tiền cơ sở tuyệt đối (Cargill, Bindseil) với quyền kiểm soát không hoàn toàn do thị trường nông và sức ép tài khóa (IMF)
- [[perfect-capital-mobility-with-a-fixed-exchange-rate-strips-monetary-policy-of-independence]] — lãi suất trong nước bị ép về mức thế giới
- [[currency-substitution-undermines-monetary-control]] — đô la hoá
- [[financial-innovation-blurs-the-boundary-of-money]] — đổi mới tài chính, đánh đổi liên quan/kiểm soát
- [[foreign-exchange-intervention]] — mua bán ngoại tệ làm tài sản đối ngoại và tiền dự trữ đổi cùng chiều
- [[open-market-operations]] — mua bán giấy tờ có giá của chính phủ; công cụ trung hoà can thiệp ngoại hối
- [[discount-window]] — tín dụng của ngân hàng trung ương cho ngân hàng; lãi suất chiết khấu báo hiệu lập trường chính sách

**Ch.5 — đặc thù kinh tế chuyển đổi + kỹ thuật IMF (batch W4)**
- [[transition-economies-experience-large-discrete-jumps-in-money-velocity]] — vòng quay tiền nhảy bậc, phục hồi chậm
- [[lack-of-bank-competition-in-transition-economies-forces-nonprice-credit-rationing]] — di sản monobank, đấu giá phân bổ tín dụng, tín dụng ưu đãi
- [[absence-of-money-and-financial-markets-precludes-open-market-operations-in-early-transition]] — vì sao OMO không dùng được giai đoạn đầu
- [[old-fixed-rate-loans-and-weak-financial-discipline-complicate-interest-rate-liberalization]] — dư nợ cũ lãi suất thấp cản trở tự do hoá
- [[wide-deposit-lending-spread-in-transition-economies-reflects-four-cost-factors]] — 4 nguyên nhân chênh lệch lãi suất huy động-cho vay
- [[monobank]] — hệ thống ngân hàng độc quyền thời kế hoạch hoá tập trung
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
- [[financial-programming]] — gói chính sách định lượng, phối hợp; khung IMF dựa trên phân biệt tiền nguồn gốc trong nước/đối ngoại
- [[the-imf-private-sector-column-nets-household-surplus-against-enterprise-deficit]] — *(analysis)* cột khu vực tư 7-cột của IMF gộp hộ gia đình/doanh nghiệp, có thể che dòng vốn nội bộ mà ma trận 5-cột tách biệt của Cargill mới thấy

**Vận hành chính sách tiền tệ (Bindseil — Intro + Ch.1–2)**
- [[separation-principle-of-monetary-policy]] — phân ly giữa monetary macroeconomics và monetary policy implementation trong thời bình; sụp đổ trong khủng hoảng
- [[operational-target-of-monetary-policy]] — 4 điều kiện của mục tiêu vận hành; tại sao lãi suất ngắn hạn là lựa chọn chuẩn
- [[monetary-policy-instruments-three-tools]] — hub 3 công cụ: open market ops, standing facilities, reserve requirements
- [[central-bank-financial-accounts-model]] — phương pháp hệ thống tài khoản khép kín 4 khu vực để mô hình hoá monetary policy operations
- [[relative-vs-absolute-central-bank-intermediation]] — khi nào bảng cân đối NHTW nở; phân biệt trung gian tương đối và tuyệt đối
- [[collateral-constraint-on-central-bank-credit]] — haircut và eligibility giới hạn tổng tín dụng NHTW có thể cung cấp
- [[autonomous-factors-of-central-bank-balance-sheet]] — các mục ngoài kiểm soát của vận hành: tiền giấy, tiền gửi chính phủ, dự trữ ngoại hối
- [[liquidity-deficit-of-the-banking-system]] — original vs post-outright deficit; chỉ số leanness của NHTW

**Vận hành chính sách tiền tệ (Bindseil — Ch.3)**
- [[overnight-rate-is-the-natural-operational-target-of-monetary-policy]] — tại sao overnight là kỳ hạn tối ưu; Fisher equation; bẫy kỳ hạn dài
- [[reserve-position-doctrine-rise-and-fall-at-the-fed]] — lịch sử 70 năm kiểm soát định lượng tại Fed (1920–1990); 6 giai đoạn; lý do thất bại

**Vận hành chính sách tiền tệ (Bindseil — Ch.4)**
- [[three-techniques-to-control-short-term-interest-rates]] — hub: 3 kỹ thuật cơ bản kiểm soát lãi suất ngắn hạn
- [[one-directional-standing-facility-monetary-policy]] — structural deficit (Reichsbank) vs structural surplus (Fed post-2009)
- [[interest-rate-corridor-symmetric-approach]] — symmetric corridor, full allotment; ECB/BoE trước và trong khủng hoảng

**Vận hành chính sách tiền tệ (Bindseil — Ch.5)**
- [[martingale-property-of-overnight-rates-and-reserve-averaging]] — tại sao overnight rate là martingale; timing OMO trong ngày; reserve averaging qua kỳ duy trì

**Vận hành chính sách tiền tệ (Bindseil — Ch.6)**
- [[standing-facilities-in-monetary-policy-operations]] — 3 loại standing facilities (discount, Lombard, deposit); tách biệt với ELA; bác bỏ real bills doctrine
- [[optimal-width-of-the-interest-rate-corridor]] — đánh đổi ổn định lãi suất vs duy trì thanh khoản liên ngân hàng; mô hình Bindseil-Jablecki (2011b)
- [[taralac-facility-target-rate-limited-access]] — công cụ đệm thanh khoản Taralac neo lãi suất tại target mà không cần OMO hàng ngày

**Vận hành chính sách tiền tệ (Bindseil — Ch.7)**
- [[outright-vs-credit-open-market-operations]] — mua đứt vs cho vay tái cấp vốn; danh mục SOMA của Fed vs Eurosystem; kiểm soát đường cong lợi suất
- [[tender-procedures-for-credit-open-market-operations]] — đấu thầu fixed-rate vs variable-rate (English/Dutch); hiện tượng overbidding; ma trận tự động vs tuỳ ý
- [[liquidity-absorbing-open-market-operations]] — xử lý thặng dư thanh khoản (ngoại hối EMEs vs QE); 4 công cụ hút dự trữ dư và phổ thanh khoản tài sản
- [[repurchase-agreement]] — hợp đồng mua lại (repo): công cụ vay nợ ngắn hạn có bảo đảm bằng chứng khoán

**Vận hành chính sách tiền tệ (Bindseil — Ch.8)**
- [[functions-of-reserve-requirements-in-monetary-policy]] — 6 chức năng lịch sử và hiện đại; giải cấu trúc số nhân tiền tệ; đệm thanh khoản và thuế ngầm
- [[reserve-requirement-system-specifications-and-averaging]] — quy chuẩn kỳ tính toán (contemporaneous vs lagged); cơ chế bình quân hoá; cải cách 2004 của ECB

**Vận hành chính sách tiền tệ (Bindseil — Ch.9)**
- [[central-bank-collateral-framework-design-and-risk-control]] — quy trình thiết kế 5 bước và điểm cắt tối ưu xã hội; 3 kỹ thuật kiểm soát rủi ro (hạn mức, định giá/ký quỹ, haircuts)
- [[market-impact-of-collateral-framework-and-leverage-constraints]] — phí quyền và định giá tài sản; mô hình Ashcraft et al. (2011) coi haircut là công cụ CSTT vĩ mô; mô hình collateral gap
- [[collateral-pool-segregation-and-double-adverse-selection]] — quy luật Gresham kép trong tín dụng NHTW; 4 giải pháp ứng phó; so sánh Fed (TAF), BoE (asset swap) và Eurosystem

**Vận hành chính sách tiền tệ (Bindseil — Ch.10)**
- [[optimal-monetary-policy-operations-frameworks-in-normal-times]] — hub: 8 tiêu chuẩn khuôn khổ tối ưu; 3 mô hình khả thi trong thời bình; đồng thuận thực tiễn và 2 tranh luận chưa ngã ngũ
- [[comparative-central-bank-operational-frameworks-normal-times]] — khảo sát thực nghiệm 4 NHTW (Australia, BoE, ECB, Fed); sự tách biệt giữa kiểm soát lãi suất qua đêm và độ biến động lãi suất 3 tháng

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.11)**
- [[mechanics-of-liquidity-crises-and-feedback-loops]] — cơ chế vi mô khủng hoảng thanh khoản: lựa chọn đối nghịch Flannery, trò chơi tích trữ thanh khoản, vòng xoáy haircut VaR và bán tháo Cifuentes
- [[bank-runs-investor-strikes-and-multiple-equilibria]] — đa cân bằng và rút vốn: mô hình Diamond-Dybvig 3 trạng thái, nghịch lý minh bạch thông tin, đình công đảo nợ bán buôn và khủng hoảng nợ công Eurozone
- [[monetary-policy-transmission-breakdown-and-zero-lower-bound]] — đứt gãy truyền dẫn: bóc tách R = i + j + k, quy tắc Wicksell mở rộng, cái bẫy ZLB và sự sụp đổ của nguyên tắc phân tách với ma trận (I*, Q*)

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.12)**
- [[collateral-scarcity-and-effective-term-funding-costs]] — khan hiếm tài sản bảo đảm và chi phí tài trợ kỳ hạn 1 năm; công thức 3 trạng thái; phản ứng chính sách khi chạm ZLB
- [[effective-corridor-asymmetry-and-stigma-in-overnight-rates]] — tính phi đối xứng hiệu dụng của hành lang lãi suất; cú sốc ngày 9/8/2007; 4 nguồn phi đối xứng và hội chứng kỳ thị (stigma)
- [[asset-encumbrance-and-subordination-of-unsecured-creditors]] — vấn đề ràng buộc tài sản thế chấp; thứ cấp hóa chủ nợ không bảo đảm; công thức LGD# và phần bù rủi ro tại ngoại vi Eurozone
- [[securities-lending-programmes-and-central-bank-collateral-swaps]] — cơ chế hoán đổi collateral và cho vay chứng khoán; giữ trung hòa lượng dự trữ; Fed TSLF và BoE SLS/DWF

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.13)**
- [[narrowing-interest-rate-corridor-and-absolute-central-bank-intermediation]] — thu hẹp hành lang lãi suất; mô hình Bindseil & Jablecki 3 phân đoạn; vai trò công cụ CSTT phi quy ước hạ chi phí trung gian
- [[fixed-rate-full-allotment-and-maturity-lengthening-in-crisis]] — chuyển đổi credit OMOs: cơ chế phân bổ toàn bộ (FRFA), kéo dài kỳ hạn tới 3 năm (LTROs), và các chương trình tài trợ gắn mục tiêu tín dụng (FLS, LSP)
- [[seven-channels-of-central-bank-asset-purchase-programmes]] — 7 kênh tác động của mua đứt tài sản (QE/LSAP/Credit Easing); so sánh Bernanke vs BoJ; hiệu ứng nén lợi suất thực nghiệm
- [[dangers-of-ultra-accommodating-monetary-policy-and-the-wicksellian-counter-defense]] — tranh luận chính sách: 4 hiểm họa theo BIS (doanh nghiệp xác sống, nén biên lợi nhuận, tìm kiếm lợi suất) vs phản biện Wicksell; 2 hình thái bảng cân đối khủng hoảng
- [[quantitative-easing]] — nới lỏng định lượng (QE): mua tài sản dài hạn quy mô lớn khi lãi suất chạm sàn zero

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.14)**
- [[lender-of-last-resort-foundations-and-bagehot-principles]] — nền tảng lý thuyết LOLR: di sản Harman và Bagehot (nguyên lý quán tính và tính nội sinh của rủi ro); 6 cơ sở kinh tế học hiện đại
- [[central-bank-inertia-and-active-crisis-lolr-measures]] — kích hoạt LOLR tự động qua quán tính; rủi ro vỡ nợ kép tăng 1000 lần; 6 biện pháp can thiệp chủ động vượt ngoài quán tính
- [[emergency-liquidity-assistance-framework-and-constructive-ambiguity]] — hỗ trợ thanh khoản khẩn cấp (ELA): 7 khác biệt so với tín dụng chuẩn; mô hình HKMA và sự mập mờ mang tính xây dựng

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.15)**
- [[central-bank-risk-taking-and-liquidity-support-trade-off]] — đánh đổi giữa rủi ro tài chính và hỗ trợ thanh khoản; 4 trường phái quan điểm; mô hình đường biên hiệu quả và hàm phúc lợi W(R, L)
- [[endogenous-risk-and-upward-sloping-haircut-loss-curve]] — rủi ro nội sinh và đường cong tổn thất dốc lên theo haircut; tại sao hạ haircut từ 60% xuống 50% giúp triệt tiêu rủi ro vỡ nợ; minh chứng cho kế hoạch dũng cảm của Bagehot
- [[bindseil-jablecki-risk-endogeneity-and-two-errors-model]] — mô hình động 2 kỳ Bindseil & Jablecki: đánh đổi giữa sai lầm loại 1 (thanh lý non dự án tốt) và sai lầm loại 2 (nuôi dưỡng ngân hàng xác sống); tác động của độ nhiễu và chi phí vỡ nợ

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.16)**
- [[lender-of-last-resort-moral-hazard-and-liquidity-externalities]] — rủi ro đạo đức của LOLR và 2 ngoại tác hệ thống (bán tháo tài sản và liên kết mạng lưới); giới hạn của cứu trợ thanh khoản thuần túy
- [[liquidity-regulation-and-central-bank-operations-arbitrage]] — quy chuẩn thanh khoản Basel III (LCR); chỉ số khoảng cách tới mất thanh khoản (DTI); kinh doanh chênh lệch pháp lý qua trung gian NHTW tuyệt đối và tương đối
- [[surcharges-for-over-proportional-reliance-on-the-central-bank]] — cơ chế phụ thu lãi suất theo mức độ phụ thuộc quá tỷ lệ; mô hình Bindseil với vùng đệm miễn trừ; 2 kịch bản định chuẩn thời bình vs khủng hoảng

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.17)**
- [[international-lender-of-last-resort-and-dual-liquidity-crises]] — người cho vay cuối cùng quốc tế (ILOLR); khủng hoảng tỷ giá cố định, cạn kiệt dự trữ và mô hình đình công nhà đầu tư; vai trò trung gian có điều kiện của IMF
- [[central-bank-fx-swap-lines-and-cross-border-liquidity]] — mạng lưới hoán đổi ngoại hối liên NHTW (FX swap lines); lợi thế thể chế của NHTW sở tại (Bernanke 2008); bài học định giá hạ thấp để ngăn ngừa kỳ thị (stigma)
- [[target2-balances-and-balance-of-payments-mechanics]] — số dư TARGET2 trong Eurosystem; đồng nhất thức hạch toán giữa thâm hụt vãng lai (CUR) và tháo chạy vốn (CAP); vai trò chốt chặn thanh khoản tự động của liên minh tiền tệ
- [[currency-swap]] — hoán đổi ngoại tệ: thỏa thuận trao đổi tiền tệ kèm cam kết đảo ngược theo tỷ giá định trước

**Vận hành chính sách tiền tệ trong khủng hoảng (Bindseil — Ch.18)**
- [[optimal-monetary-policy-operations-frameworks-in-crisis-times]] — hub: tổng hợp khuôn khổ vận hành tối ưu trong khủng hoảng; 11 bài học và nguyên tắc chuẩn tắc từ thực tiễn; sự chuyển biến từ kỹ thuật sang nghệ thuật
- [[exit-strategies-from-non-conventional-monetary-policy]] — chiến lược thoái lui khỏi các chính sách phi quy ước; vấn đề ý chí chính trị vs năng lực kỹ thuật; nguyên tắc chiếc kim duy nhất trên la bàn

**Chế độ tài chính và chính sách tiền tệ (Cargill — Ch.1)**
- [[financial-and-monetary-regime]] — khung 3 trụ cột (hệ thống tài chính, giám sát chính phủ, NHTW) với 5 chức năng bất biến
- [[real-and-financial-sectors-interact-through-loanable-funds-and-interest-rates]] — tương tác phản hồi hai chiều qua quỹ cho vay và lãi suất
- [[a-well-functioning-financial-and-monetary-regime-is-necessary-but-not-sufficient-for-stability]] — điều kiện cần nhưng không đủ cho tăng trưởng và ổn định
- [[government-policy-failure-is-as-critical-as-market-failure-in-financial-crises]] — sai lầm chính sách của chính phủ và NHTW là căn nguyên ngang bằng hoặc vượt trội thất bại thị trường

**Khái niệm cơ bản về tiền tệ (Cargill — Ch.2)**
- [[money-is-a-market-innovation-to-overcome-barter-inefficiencies]] — tiền tệ là sáng kiến thị trường phi tập trung giải quyết sự bất tiện của hàng-đổi-hàng
- [[money-is-the-only-one-hundred-percent-liquid-asset]] — tiền là tài sản duy nhất có thanh khoản 100%; vị trí các tài sản trên phổ thanh khoản
- [[credit-cards-are-liabilities-and-not-part-of-the-money-supply]] — thẻ tín dụng là nghĩa vụ nợ ngắn hạn, không phải tiền tệ hay một phần của cung tiền
- [[money-supply]] — cung tiền: tổng lượng tiền tệ trong nền kinh tế, phân cấp từ tiền hẹp đến tiền rộng
- [[consumer-price-index-has-four-sources-of-upward-bias]] — 4 nguồn thiên lệch hệ thống của CPI thổi phồng lạm phát 1,1%/năm theo Ủy ban Boskin
- [[cpi-upward-bias-expands-government-deficits-through-automatic-indexation]] — tác động tài khóa kép của thiên lệch CPI làm phình to thâm hụt ngân sách qua COLA và thuế
- [[monetary-standards-evolved-from-commodity-money-to-fiat-credit-money]] — 3 giai đoạn tiến hóa chuẩn tiền tệ từ hàng hóa, quy đổi kim loại đến tiền pháp định
- [[modern-monetary-system-functions-as-an-inverted-pyramid]] — hệ thống tiền tệ vận hành như kim tự tháp ngược dựa trên niềm tin với chân đế hẹp là tiền cơ sở
- [[money-is-non-neutral-in-the-short-run-but-neutral-in-the-long-run]] — tiền tệ phi trung lập trong ngắn hạn do giá cứng nhắc nhưng trung lập hoàn toàn trong dài hạn

**Hệ thống tài chính và luồng vốn (Cargill — Ch.3)**
- [[flow-of-funds-fundamental-equation-links-real-and-financial-decisions]] — phương trình cơ bản (S - I) = (L - B) gắn kết quyết định kinh tế thực và tài chính
- [[economic-sectors-are-classified-into-surplus-deficit-and-balanced-units]] — 3 lăng kính phân loại khu vực thành đơn vị thặng dư, thâm hụt và cân bằng
- [[financial-system-transfers-funds-through-direct-and-indirect-channels]] — 2 kênh tài trợ: tài chính trực tiếp không bảng cân đối duy trì vs tài chính gián tiếp qua định chế
- [[direct-financial-markets-fail-small-participants-due-to-risk-return-tradeoff-asymmetry]] — thị trường trực tiếp thất bại với chủ thể nhỏ do bất đối xứng đường cong RR2 vs RR1
- [[financial-markets-are-divided-into-money-markets-and-capital-markets-by-maturity]] — thị trường tiền tệ (<=1 năm) vs thị trường vốn (>1 năm); công cụ và thanh khoản
- [[financial-institutions-operate-as-balanced-budget-entities-in-the-flow-of-funds]] — định chế tài chính là thực thể ngân sách cân bằng (S ~ I, B ~ L), đóng vai trò ống dẫn vốn

**Lãi suất trong hệ thống tài chính (Cargill — Ch.4)**
- [[interest-rate-connects-the-present-to-the-future-through-time-value-of-money]] — lãi suất là cơ chế kết nối hiện tại và tương lai thông qua giá trị thời gian của tiền; sự phân biệt giữa lãi suất danh nghĩa và thực
- [[interest-rates-in-indirect-finance-are-administered-with-a-lag-behind-market-rates]] — lãi suất ấn định của ngân hàng phản ứng có độ trễ trước biến động thị trường mở do chi phí giao dịch, hợp đồng ngầm và quy định
- [[interest-rate-ceilings-distort-credit-allocation-and-induce-disintermediation]] — trần lãi suất (Quy định Q) gây hiện tượng phi trung gian hóa tài chính (disintermediation) và phân bổ tín dụng phi hiệu quả
- [[yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price]] — lợi suất đáo hạn (YTM) là chuẩn mực đo lường chiết khấu dòng tiền chuẩn xác nhất theo phương pháp nội suy
- [[discount-yield-understates-the-true-return-on-zero-coupon-instruments]] — lợi suất chiết khấu đánh giá thấp tỷ suất sinh lời thực tế của công cụ chiết khấu do mẫu số mệnh giá và quy ước 360 ngày
- [[interest-rate-risk-increases-with-maturity-and-separates-total-return-from-yield]] — rủi ro lãi suất gia tăng theo kỳ hạn và tách biệt tỷ suất sinh lời tổng thể khỏi lợi suất đáo hạn danh nghĩa

**Mặt bằng lãi suất (Cargill — Ch.5)**
- [[loanable-funds-framework-determines-equilibrium-interest-rate-and-bond-price]] — khung quỹ cho vay xác định lãi suất cân bằng và giá trái phiếu; ưu thế thể chế so với ưa thích thanh khoản
- [[interest-rates-move-procyclically-due-to-asymmetric-business-cycle-shifts-in-loanable-funds]] — lãi suất biến động đồng chu kỳ do dịch chuyển bất đối xứng của cầu quỹ lấn át cung quỹ trong mở rộng kinh tế
- [[debt-monetization-creates-conflict-between-fiscal-deficits-and-central-bank-independence]] — thâm hụt tài khóa gây chèn lấn và áp lực tiền tệ hóa nợ công; cơ sở đòi hỏi tính độc lập của ngân hàng trung ương
- [[fisher-effect-shifts-nominal-interest-rates-one-to-one-with-expected-inflation]] — hiệu ứng Fisher: lạm phát kỳ vọng dịch chuyển cung cầu quỹ làm lãi suất danh nghĩa điều chỉnh tỷ lệ 1-1 với lạm phát kỳ vọng
- [[expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads]] — ba phương pháp đo lường lạm phát kỳ vọng: khảo sát kỳ vọng (Livingston), mô hình kinh tế lượng và chênh lệch TIPS
- [[negative-interest-rates-distort-financial-intermediation-and-test-the-zero-lower-bound]] — lãi suất âm phá vỡ giả định chặn dưới ZLB, bóp méo trung gian tài chính và cho thấy giới hạn của chính sách tiền tệ
- [[monetary-expansion-lowers-interest-rates-via-liquidity-effect-before-income-and-fisher-effects-raise-them]] — động học 3 pha của tăng cung tiền (thanh khoản -> thu nhập -> kỳ vọng giá); lãi suất danh nghĩa là chỉ báo đánh lừa về lập trường tiền tệ

**Cấu trúc lãi suất và đường cong lợi suất (Cargill — Ch.6)**
- [[interest-rate-structure-is-determined-by-default-risk-liquidity-taxes-and-maturity]] — khung 4 yếu tố xác định cấu trúc lãi suất, chuẩn mực kho bạc và phương trình Fisher mở rộng
- [[default-risk-premium-widens-during-recessions-and-narrows-during-expansions]] — phần bù rủi ro vỡ nợ đo lường qua credit spread và quy luật vận động ngược chu kỳ
- [[liquidity-premium-compensates-for-secondary-market-depth-and-transaction-costs]] — phần bù thanh khoản bù đắp độ sâu thị trường thứ cấp và chi phí giao dịch; sự hòa trộn với rủi ro vỡ nợ
- [[tax-exemption-lowers-municipal-bond-yields-and-reveals-implicit-marginal-tax-rates]] — miễn thuế trái phiếu chính quyền địa phương tạo trợ cấp ngầm và phản ánh thuế suất biên ngầm qua arbitrage
- [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates]] — giả thuyết kỳ vọng thuần túy: lãi suất dài hạn bằng trung bình cộng không thiên lệch của lãi suất ngắn hạn kỳ vọng
- [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves]] — giả thuyết phần bù thanh khoản gia tăng theo kỳ hạn giải thích toàn diện tính đồng biến và ưu thế áp đảo của đường cong dốc lên
- [[segmented-markets-hypothesis-views-maturities-as-disconnected-institutional-compartments]] — giả thuyết thị trường phân khúc và môi trường ưu tiên: định giá cục bộ theo kỳ hạn và hạn chế thể chế
- [[yield-curve-functions-as-a-rorschach-test-of-inflation-and-business-cycle-expectations]] — đường cong lợi suất là chỉ báo sớm về lạm phát và chu kỳ; đường cong đảo ngược cảnh báo suy thoái; ẩn dụ bài test vết mực Rorschach
- [[yield-curve]] — đường cong lợi suất: đồ thị biểu diễn mối quan hệ giữa lợi suất đáo hạn và kỳ hạn
- [[credit-spread]] — chênh lệch tín dụng: phần bù rủi ro vỡ nợ của trái phiếu doanh nghiệp so với trái phiếu chính phủ

**Kích thước quốc tế của hệ thống tài chính (Cargill — Ch.7)**
- [[statement-of-international-transactions-mirrors-current-and-financial-accounts]] — bảng giao dịch quốc tế phản chiếu giữa CA và FA ($CA + FA = 0$); thâm hụt CA đồng nghĩa là đơn vị thâm hụt ròng
- [[exchange-rate-determination-balances-short-run-financial-flows-and-long-run-trade]] — cơ chế xác định tỷ giá cân bằng giữa dòng tài sản tài chính ngắn hạn (FA view) và dòng hàng hóa dài hạn (CA view)
- [[real-interest-rate-increases-appreciate-currency-while-inflation-expectations-depreciate-it]] — hiệu ứng Fisher đối với tỷ giá: lãi suất thực tăng làm tăng giá đồng tiền, lạm phát kỳ vọng làm giảm giá đồng tiền
- [[internal-external-balance-links-domestic-saving-investment-gaps-to-current-account-deficits]] — cân bằng nội - ngoại $(S - I) + (T - G) = CA$; giải mã nghịch lý USD giảm giá nhưng thâm hụt vãng lai Mỹ tiếp tục phình to do spending binge
- [[sterilization]] — nghiệp vụ trung hòa: nghiệp vụ bù trừ tác động của can thiệp ngoại hối lên cung tiền trong nước

**Vai trò cơ bản của chính phủ trong chế độ tài chính - tiền tệ (Cargill — Ch.8)**
- [[greshams-law-and-uniform-coinage-rationalize-initial-government-monetary-roles]] — định luật Gresham ("tiền xấu đuổi tiền tốt") và nhu cầu đúc tiền chuẩn hóa; nguy cơ lạm dụng quyền năng đúc tiền tạo lạm phát
- [[government-safety-net-solves-bank-runs-but-generates-systemic-moral-hazard]] — mạng lưới an toàn (LOLR + FDIC) bảo vệ mô hình kim tự tháp ngược nhưng triệt tiêu kỷ luật thị trường, sinh rủi ro đạo đức, forbearance và too-big-to-fail
- [[government-credit-allocation-subsidies-distort-markets-and-induce-systemic-fragility]] — trợ cấp phân bổ tín dụng nhà ở (Fannie/Freddie, CRA 1977) bóp méo thị trường, gây bong bóng tài sản và khủng hoảng tài chính mà không nâng cao tỷ lệ sở hữu nhà bền vững
- [[public-choice-theory-explains-regulatory-capture-and-monetary-politicization]] — lý thuyết lựa chọn công: tha hóa thể chế (regulatory capture), tư bản thân hữu (crony capitalism) và áp lực chính trị tiền tệ hóa nợ công
- [[moral-hazard]] — rủi ro đạo đức: xu hướng chấp nhận rủi ro lớn hơn do có mạng lưới bảo hộ của nhà nước

**Quy định và thanh tra giám sát hệ thống tài chính (Cargill — Ch.9)**
- [[supervision-differs-from-regulation-through-continuous-monitoring-and-camels-examination]] — phân biệt quy định (luật chơi tĩnh) và thanh tra giám sát (đánh giá động); hệ thống CAMELS và nguyên tắc bảo mật thông tin xếp hạng
- [[prompt-corrective-action-establishes-tripwire-capital-ratios-to-curb-regulatory-forbearance]] — cơ chế can thiệp sớm bắt buộc (PCA) theo luật FDICIA 1991: hệ thống dây bẫy an toàn vốn 5 bậc xóa bỏ sự tùy quyền khoan hồng của thanh tra
- [[risk-based-capital-requirements-aim-to-constrain-leverage-but-incentivize-regulatory-arbitrage]] — quy chuẩn an toàn vốn Basel (I, II, III): trọng số rủi ro RWA và nghịch lý kinh doanh chênh lệch pháp lý (regulatory arbitrage)
- [[supervisory-stress-testing-provides-forward-looking-macroprudential-evaluation]] — kiểm tra sức chịu đựng giám sát (Dodd-Frank 2010): dự phóng 9 quý theo 3 kịch bản vĩ mô đối với SIFIs và công khai kết quả
- [[macroprudential-regulation-bridges-financial-stability-and-macroeconomic-policy-despite-informational-limits]] — quy định an toàn vĩ mô: hợp nhất ổn định tài chính và chính sách vĩ mô; 4 thách thức và giới hạn nhận diện bong bóng tài sản
- [[non-performing-loans]] — nợ xấu: các khoản tín dụng quá hạn hoặc có nguy cơ cao không thu hồi được đầy đủ

**Lịch sử chuyển đổi thể chế tài chính - tiền tệ Hoa Kỳ (Cargill — Ch.10)**
- [[regulatory-market-dialectic-drives-financial-regime-evolution]] — biện chứng quản lý – thị trường của Edward Kane: chu trình 5 bước xung đột giữa rào cản nhà nước và sáng tạo lách luật của thị trường
- [[dual-banking-system-emerged-as-a-market-innovation-around-taxation]] — hệ thống ngân hàng lưỡng tính Mỹ ra đời từ sáng tạo thị trường chuyển đổi giấy bạc sang tiền gửi thanh toán để lách thuế 10% năm 1863
- [[savings-and-loan-collapse-manifested-interest-rate-risk-and-disintermediation]] — sự sụp đổ của hệ thống S&L thập niên 1980 do đòn kép rủi ro kỳ hạn và phi trung gian hóa từ trần Regulation Q
- [[us-financial-deregulation-eliminated-great-depression-era-competitive-barriers]] — tiến trình phi điều tiết hóa tài chính 1980–1999: dỡ bỏ rào cản cạnh tranh thời New Deal (Regulation Q, Riegle-Neal, Gramm-Leach-Bliley)

**Thiết kế thể chế của ngân hàng trung ương (Cargill — Ch.11)**
- [[five-step-framework-structures-central-bank-policy-analysis]] — khung phân tích 5 bước của chính sách tiền tệ: thiết kế thể chế, công cụ trực tiếp, công cụ điều hành, mô hình kinh tế và mục tiêu cuối cùng
- [[central-banks-are-necessarily-public-institutions-despite-private-ownership-fictions]] — bản chất công quyền tất yếu của ngân hàng trung ương bất chấp hình thức sở hữu tư nhân; độc quyền phát hành tiền và phụng sự phúc lợi công
- [[de-jure-central-bank-independence-diverges-from-de-facto-policy-autonomy]] — sự phân kỳ giữa tính độc lập pháp lý (de jure) và quyền tự chủ chính sách thực tế (de facto); bài học áp lực chính trị Nixon - Burns 1972
- [[central-bank-transparency-anchors-public-expectations-across-five-dimensions]] — tính minh bạch của NHTW qua 5 chiều kích (chính trị, kinh tế, thủ tục, chính sách, vận hành); bước chuyển từ văn hóa bí mật sang định hướng kỳ vọng
- [[institutional-structure-of-the-federal-reserve-concentrates-power-in-the-board-and-fomc]] — cấu trúc thể chế của Fed: tam giác Hội đồng Thống đốc, 12 FRB khu vực và FOMC; sự tập trung quyền lực vào Thống đốc và FOMC

**Ngân hàng trung ương, tiền cơ sở và quá trình cung tiền (Cargill — Ch.12)**
- [[central-banks-create-base-money-out-of-thin-air-through-open-market-operations]] — quyền năng tạo lập và tiêu hủy tiền cơ sở từ hư không qua nghiệp vụ thị trường mở; mức giá thị trường không thể chối từ và lợi tức seigniorage
- [[money-supply-expansion-stops-when-absorbing-factors-exhaust-high-powered-money]] — phương trình điểm dừng của cung tiền: $\Delta H = rr \cdot \Delta T + \Delta C + \Delta E$; cơ chế bù trừ séc trong hệ thống đa ngân hàng
- [[currency-deposit-ratio-reflects-opportunity-costs-and-underground-economy-incentives]] — tỷ lệ tiền mặt trên tiền gửi giao dịch $k$: chi phí cơ hội lãi suất, quy mô kinh tế ngầm né thuế ("chicken tracks"), công nghệ ATM và an ninh xã hội
- [[central-bank-controls-the-monetary-base-but-cannot-predictably-control-the-money-supply]] — sự phân tách giữa kiểm soát tiền cơ sở và bất lực kiểm soát cung tiền trong ngắn hạn; vai trò triệt tiêu yếu tố tự trị qua danh mục chứng khoán
- [[money-multiplier-collapsed-post-2008-due-to-interest-on-excess-reserves-and-bank-risk-aversion]] — sự sụp đổ của số nhân tiền M2 hậu 2008: tỷ lệ dự trữ vượt mức $e$ tăng vọt từ 0,2% lên 130% do chính sách IOER và tâm lý né tránh rủi ro

**Công cụ chính sách tiền tệ và công cụ điều hành trung gian (Cargill — Ch.13)**
- [[selective-credit-controls-decayed-due-to-fungibility-and-regulatory-circumvention]] — sự suy tàn của các công cụ tín dụng chọn lọc do tính chuyển hóa linh hoạt của dòng vốn, chi phí hành chính và sáng tạo lách luật
- [[forward-guidance-evolved-from-moral-suasion-as-conditional-transparent-commitment]] — tiến hóa từ thuyết phục đạo đức sang định hướng kỳ vọng: cam kết công khai có điều kiện nhằm neo giữ kỳ vọng thị trường
- [[central-banks-cannot-simultaneously-target-money-supply-and-interest-rates]] — thế lưỡng nan Poole trong khung quỹ cho vay: sự đánh đổi tất yếu giữa biến động lãi suất và biến động khối tiền tệ
- [[interest-rate-targeting-dominates-monetary-aggregates-due-to-measurement-and-control-limits]] — bốn lý do thực tiễn khiến mục tiêu lãi suất thay thế hoàn toàn mục tiêu cung tiền; cảnh báo dài hạn của Cargill về rủi ro lạm phát

**Mô hình kinh tế của ngân hàng trung ương (Cargill — Ch.14)**
- [[macroeconomic-models-provide-road-map-for-central-bank-policy-transmission]] — ba chức năng của mô hình vĩ mô: nhận thức cân bằng dài hạn, so sánh hiệu lực chính sách và cung cấp bản đồ chỉ đường truyền dẫn
- [[natural-rate-hypothesis-invalidates-the-permanent-phillips-curve-tradeoff]] — sự sụp đổ của đường cong Phillips cổ điển trước hiện tượng đình lạm; đột phá Friedman-Phelps về hợp đồng tiền lương thực tế và đường LRPC thẳng đứng
- [[aggregate-supply-and-demand-framework-synthesizes-short-run-nonneutrality-and-long-run-neutrality]] — khung AD/AS tổng hợp tính phi trung tính ngắn hạn và trung tính dài hạn của tiền tệ; cơ chế hấp thụ cú sốc cầu và cú sốc giá
- [[macroeconomic-schools-diverge-on-market-stability-and-rules-versus-discretion]] — sự phân kỳ tư tưởng vĩ mô thế kỷ giữa Tân Keynes (Modigliani 1976, animal spirits, tùy nghi có kiềm chế) và Tân Cổ điển (Friedman 1967, thất bại chính phủ, chính sách theo quy tắc)

**Mục tiêu chính sách cuối cùng của ngân hàng trung ương (Cargill — Ch.15)**
- [[price-stability-is-defined-by-low-and-stable-inflation-rather-than-zero-percent]] — định nghĩa ổn định giá cả bằng lạm phát thấp và phương sai thấp; 3 chi phí của lạm phát dự tính; lý do chọn 2% để bù đắp sai số CPI và ngăn ngừa giảm phát
- [[monetary-policy-lags-can-render-countercyclical-stabilization-destabilizing]] — độ trễ tác động kéo dài và biến thiên khiến chính sách can thiệp phản chu kỳ tác động sai thời điểm và gây phản ứng thái quá
- [[inflation-targeting-framework-anchors-expectations-through-transparent-commitment]] — khuôn khổ lạm phát mục tiêu: cam kết thể chế công khai, phân định mục tiêu tường minh vs ngầm định, neo giữ kỳ vọng trước cú sốc
- [[federal-reserve-dual-mandate-creates-inflation-bias-and-time-inconsistency]] — phê phán nhiệm vụ kép của Fed: 4 khiếm khuyết cấu trúc, áp lực chính trị, thiên lệch lạm phát và bẫy bất nhất thời gian

**Chiến thuật, chiến lược và tranh luận quy tắc vs tùy nghi (Cargill — Ch.16)**
- [[monetary-policy-tactics-differ-from-strategy-in-central-bank-operations]] — sự khác biệt giữa chiến thuật (điều hành thanh khoản và OMOs hàng ngày) và chiến lược (mục tiêu vĩ mô dài hạn) trong quản trị NHTW
- [[taylor-rule-formalizes-systematic-feedback-and-the-taylor-principle]] — quy tắc Taylor: phản ứng lãi suất hệ thống trước độ lệch lạm phát và sản lượng; nguyên tắc Taylor ($h > 1$) đảm bảo ổn định kinh tế
- [[lucas-critique-invalidates-econometric-policy-evaluation-under-discretion]] — phê phán Lucas: sự vô hiệu của mô hình kinh tế lượng dựa trên dữ liệu quá khứ khi tham số hành vi thay đổi theo chế độ chính sách
- [[time-inconsistency-generates-inflation-bias-under-discretionary-monetary-policy]] — bẫy bất nhất thời gian Kydland-Prescott: chính sách tùy nghi tối ưu ngắn hạn tạo ra thiên lệch lạm phát cao mà không cải thiện sản lượng
- [[constrained-discretion-attempts-to-synthesize-rules-and-flexibility-in-central-banking]] — tùy nghi có kiềm chế: nỗ lực tổng hợp giữa quy tắc minh bạch và sự linh hoạt ứng phó cú sốc của NHTW

**Năm thời kỳ lịch sử của chế độ tài chính - tiền tệ Hoa Kỳ (Cargill — Ch.17)**
- [[great-depression-monetary-contraction-was-driven-by-federal-reserve-policy-failures]] — Đại Suy thoái 1929–1933: sự sụp đổ cung tiền và tín dụng do các sai lầm chính sách và thất bại cơ cấu của Cục Dự trữ Liên bang
- [[accord-of-nineteen-fifty-one-restored-formal-federal-reserve-independence-without-de-facto-autonomy]] — Hiệp ước Kho bạc – Fed 1951: khôi phục độc lập pháp lý về lãi suất nhưng không mang lại quyền tự chủ chính sách thực tế
- [[great-inflation-originated-from-excessive-accommodation-and-flawed-financial-regulation]] — Đại Lạm phát 1965–1981: nguồn gốc từ chính sách tiền tệ nới lỏng quá mức, trần lãi suất Regulation Q và áp lực chính trị
- [[great-moderation-benefited-from-volcker-disinflation-and-taylor-rule-benchmarking]] — Đại Điều hòa 1982–2007: kỷ nguyên ổn định kinh tế nhờ chính sách thắt chặt kiên quyết của Volcker và định chuẩn theo quy tắc Taylor
- [[great-recession-stemmed-from-the-fatal-combination-of-ultra-easy-money-and-housing-subsidies]] — Đại Suy thoái 2007–2009: bắt nguồn từ sự kết hợp chí mạng giữa tiền siêu rẻ của Fed và trợ cấp tín dụng nhà ở của chính phủ

**Các khái niệm bổ trợ cốt lõi (Stub concepts từ kết quả Lint 451 trang)**
- [[nominal-interest-rate]] — lãi suất danh nghĩa: tỷ lệ sinh lời hoặc chi phí vay vốn bằng tiền hiện hành chưa điều chỉnh lạm phát
- [[interbank-market]] — thị trường liên ngân hàng: thị trường bán buôn điều hòa dự trữ và xác lập lãi suất qua đêm mục tiêu tác nghiệp
- [[financial-intermediation]] — trung gian tài chính: quá trình định chế tài chính kết nối đơn vị thặng dư và thâm hụt qua chuyển đổi kỳ hạn và rủi ro
- [[deposit-insurance]] — bảo hiểm tiền gửi: cam kết bảo vệ người gửi tiền, cấu phần cốt lõi của mạng lưới an toàn ngăn ngừa bank run
- [[liquidity-risk]] — rủi ro thanh khoản: nguy cơ mất khả năng thanh toán ngắn hạn do lệch pha kỳ hạn giữa tài sản có và nợ
- [[adverse-selection]] — lựa chọn đối nghịch: thất bại thị trường do bất đối xứng thông tin tiền giao dịch thu hút đối tác rủi ro cao
- [[asset-bubble]] — bong bóng tài sản: hiện tượng giá tài sản tăng vọt phi lý vượt xa giá trị cơ bản nội tại do đầu cơ và tiền rẻ
- [[asymmetric-information]] — bất cân xứng thông tin: tình trạng chênh lệch thông tin giữa các bên sinh ra lựa chọn đối nghịch và rủi ro đạo đức
- [[reverse-repurchase-agreement]] — hợp đồng mua lại đảo ngược (reverse repo): nghiệp vụ thị trường mở hút thanh khoản và thiết lập sàn lãi suất

**Quản trị bảng cân đối ngân hàng thương mại và ALM (Clippings — Cụm 1)**
- [[alm-balance-sheet-balancing-progresses-through-four-operational-dimensions]] — quy trình cân đối bảng cân đối ALM tiến triển qua bốn chiều kích: dòng tiền, kỳ hạn, tỷ lệ/cấu trúc và hành vi/định giá FTP
- [[cash-flow-balancing-resolves-immediate-payment-obligations-against-excess-reserve-opportunity-cost]] — cân dòng tiền là lớp vận hành sơ cấp giải quyết nghĩa vụ thanh toán tức thời và chi phí cơ hội của dự trữ thặng dư
- [[maturity-balancing-manages-liquidity-duration-to-mitigate-rollover-and-repricing-risks]] — cân kỳ hạn xác định thời gian tồn tại của trạng thái thanh khoản để triệt tiêu rủi ro tái tài trợ rollover và rủi ro định giá lại
- [[behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales]] — mô hình hóa hành vi nguồn vốn TT1 bị biến dạng khi ngân hàng chủ động can thiệp giá và chính sách giữ chân tại thời điểm đáo hạn
- [[banks-fundamentally-rely-on-short-term-liabilities-to-finance-long-term-capital-formation]] — ngân hàng luôn dùng nợ phải trả ngắn hạn liên tục tái tục để tài trợ cho tích lũy tư bản dài hạn của nền kinh tế
- [[treasury-deposits-at-commercial-banks-provide-temporary-liquidity-without-easing-structural-funding-gaps]] — tiền gửi Kho bạc tại NHTM chỉ cung ứng thanh khoản tình thế trong ngắn hạn mà không giải quyết được khoảng trống vốn cấu trúc
- [[vietnams-banking-system-exhibits-structural-dichotomy-between-tt1-and-tt2]] — phân kỳ cấu trúc nhị phân giữa thị trường khách hàng TT1 và thị trường liên ngân hàng TT2 gây chia cắt dòng vốn
- [[multiple-balance-sheet-mismatches-compound-banking-systemic-risk]] — bốn tầng bất cân xứng đồng thời trên bảng cân đối (kỳ hạn, lãi suất, tiền tệ, phân khúc) tích tụ và khuếch đại rủi ro hệ thống
- [[tt1-deposit-rate-stickiness-prevents-interbank-liquidity-from-lowering-lending-rates]] — tính bám dính của lãi suất TT1 và tắc nghẽn vòng quay tín dụng ngắn hạn ngăn thanh khoản rẻ từ liên ngân hàng hạ lãi suất cho vay
- [[central-bank-interest-rate-corridor-requires-separate-facilities-for-interbank-and-credit-markets]] — hành lang lãi suất của NHTW cần các công cụ phân tầng riêng giữa liên ngân hàng ngắn hạn và tín dụng trung hạn
- [[active-spot-foreign-exchange-intervention-injects-primary-liquidity-directly-into-banking-system]] — can thiệp mua ngoại hối giao ngay chủ động (Buy Spot) tạo kênh bơm thanh khoản sơ cấp trực tiếp vào hệ thống NHTM và TT1
- [[central-banks-prioritize-public-policy-mandates-over-accounting-profitability]] — ngân hàng trung ương ưu tiên mục tiêu chính sách vĩ mô công quyền thay vì tối đa hóa lợi nhuận kế toán
- [[domestic-gold-pricing-diverges-from-international-benchmarks-due-to-structural-liquidity-constraints]] — giá vàng nội địa phân kỳ khỏi chuẩn quốc tế do thanh khoản cấu trúc căng thẳng, CASA suy giảm và kéo dãn kỳ hạn nợ

**Điều hành Fed, thị trường Repo và nợ công Kho bạc (Clippings — Cụm 2)**
- [[treasury-repo-market-operates-through-three-distinct-client-segments]] — cấu trúc thị trường repo Kho bạc vận hành qua ba phân khúc khách hàng C2D, Interdealer, D2C với các dealers làm trạm trung chuyển trung tâm
- [[repo-rate-spikes-transmit-to-federal-funds-rate-via-fhlb-arbitrage]] — các đợt tăng vọt lãi suất repo lan truyền sang lãi suất quỹ liên bang EFFR qua hoạt động kinh doanh chênh lệch giá của FHLB khi thanh khoản dự trữ khan hiếm
- [[quantitative-tightening-differs-from-quantitative-easing-through-balance-sheet-asymmetry]] — tính bất đối xứng giữa QE (mở rộng bảng cân đối) và QT (rút dự trữ sơ cấp Reserves -> UST mà không nhất thiết làm thu hẹp bảng cân đối ngân hàng)
- [[persistent-fiscal-deficits-operate-as-a-monetary-force-expanding-private-balance-sheets]] — thâm hụt tài khóa dai dẳng hoạt động như lực lượng tiền tệ trực tiếp bơm tiền gửi và tạo tài sản an toàn 0% risk weight tái cấu trúc hệ thống ngân hàng
- [[bank-absorption-of-sovereign-debt-is-governed-by-a-regulatory-triangle]] — tam giác quản trị quy định SLR (dung lượng), IRRBB (cơ cấu kỳ hạn), và Stress Testing (sức chống chịu) kiểm soát năng lực hấp thụ nợ công của hệ thống ngân hàng
- [[sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand]] — việc hấp thụ nợ công đòi hỏi năng lực trung gian lưu kho và tài trợ repo của các đại lý sơ cấp ngoài nhu cầu sở hữu cuối cùng của nhà đầu tư
- [[treasury-buybacks-function-as-debt-management-rather-than-monetary-yield-curve-control]] — nghiệp vụ mua lại trái phiếu của Kho bạc là công cụ quản trị nợ và giải phóng dung lượng dealer chứ không phải chính sách tiền tệ hay kiểm soát đường cong lợi suất YCC
- [[central-banks-face-policy-reaction-traps-when-energy-supply-shocks-elevate-headline-inflation]] — ngân hàng trung ương rơi vào bẫy hàm phản ứng khi duy trì thắt chặt quá mức vì áp lực uy tín trước các cú sốc năng lượng đẩy CPI bề nổi

**Lạm phát phi tuyến, chênh lệch tầng giá và cấu trúc tài chính vĩ mô toàn cầu (Clippings — Cụm 3)**
- [[supply-chain-disruptions-propagate-nonlinearly-through-input-output-cascades]] — lan truyền phi tuyến của gián đoạn chuỗi cung ứng: vượt qua năng lực đệm tồn kho, khuếch đại qua mạng lưới đầu vào - đầu ra và tạo lạm phát lõi kéo dài
- [[producer-price-stage-differential-signals-systemic-supply-chain-inflation-cascades]] — chênh lệch lạm phát sản xuất theo tầng $\Delta(t) = S1 - S4 \ge 3\text{ pp}$ kết hợp Stage 3 vượt Stage 4 là tín hiệu xác nhận sóng lạm phát chi phí đã lan tỏa vào khâu chế tạo trung gian
- [[sovereign-bond-term-premia-rise-from-fiscal-burdens-independently-of-inflation-expectations]] — phần bù kỳ hạn trái phiếu chính phủ gia tăng từ rủi ro gánh nặng tài khóa và dư cung nợ công ngay cả khi kỳ vọng lạm phát dài hạn vẫn neo giữ ổn định
- [[global-risk-appetite-reallocates-across-sectors-under-surging-sovereign-yields]] — khẩu vị rủi ro toàn cầu thích ứng bất đối xứng khi lợi suất tăng qua việc xoay trục dòng vốn giữa các lĩnh vực và khuếch đại biến động qua đòn bẩy ngắn hạn short gamma

**Thị trường ngoại hối châu Á, tỷ giá & Carry Trade (Clippings — Cụm 4)**
- [[industrial-overcapacity-drives-transition-from-supply-funding-to-productive-buyer-funding]] — dư thừa công suất công nghiệp và sự chuyển dịch từ tài trợ phía cung sang tài trợ người mua hiệu quả
- [[conditional-cny-carry-trade-finances-global-real-absorption-without-capital-account-liberalization]] — cơ chế CNY Carry Trade có điều kiện: xuất khẩu vốn gắn với kinh tế thực và thanh toán nội tệ không cần mở toang tài khoản vốn
- [[japan-net-international-creditor-position-anchors-global-jpy-carry-trade]] — vị thế chủ nợ quốc tế ròng của Nhật Bản định hình vai trò JPY funding và nguy cơ tăng chi phí vốn toàn cầu khi BOJ bình thường hóa
- [[sovereign-fx-intervention-integrates-fima-repo-facility-to-prevent-treasury-market-dislocation]] — can thiệp tỷ giá tích hợp FIMA repo: hoán đổi tạm thời UST lấy USD ngăn ngừa đứt gãy thị trường Kho bạc Mỹ
- [[commodity-import-energy-shocks-transmit-directly-into-offshore-dollar-funding-stresses]] — cú sốc nhập khẩu năng lượng chuyển hóa trực tiếp thành áp lực căng thẳng thanh khoản USD ngoại biên (Eurodollar)

**Cơ chế phản ứng của NHTW, Forward Guidance & thị trường định giá (Clippings — Cụm 5)**
- [[reaction-function-guidance-replaces-calendar-path-with-conditional-market-pricing]] — định hướng theo hàm phản ứng thay thế lộ trình lịch trình bằng cơ chế để thị trường tự định giá đường cong theo quy tắc vĩ mô
- [[asymmetric-monetary-reaction-functions-generate-ratchet-effects-on-real-rates]] — hàm phản ứng bất đối xứng tạo hiệu ứng bánh cóc đẩy lãi suất thực tăng vọt qua kênh kép của đồng nhất thức Fisher dù lãi suất điều hành giữ nguyên
- [[absence-of-policy-roadmaps-anchors-markets-to-high-frequency-data-noise]] — tình trạng thiếu vắng lộ trình chính sách khiến phần bù kỳ hạn IRS phẳng lỳ và buộc thị trường định giá sự bất định qua phản ứng thái quá với tin tức cao tần
- [[financial-market-duration-repricing-executes-monetary-tightening-on-central-banks-behalf]] — tái định giá rủi ro kỳ hạn thị trường tự động thắt chặt các điều kiện tài chính vĩ mô thay cho NHTW và giảm thiểu lợi ích biên của các đợt tăng lãi suất điều hành
- [[persistent-policy-rate-holds-compound-sovereign-bond-duration-and-refinancing-risks]] — giữ nguyên lãi suất kéo dài trước lạm phát cao làm xói mòn uy tín chính sách, mở rộng phần bù kỳ hạn và làm bùng nổ rủi ro tái cấp vốn nợ công

**Phương pháp luận vĩ mô, cấu trúc tín dụng tư nhân & rủi ro nợ công (Clippings — Cụm 6)**
- [[top-down-macro-analysis-fails-without-bottom-up-microstructure-and-capital-allocation]] — phân tích vĩ mô Top-down thất bại nếu tách rời cấu trúc vi mô, sự phân kỳ phân bổ vốn và mức độ cô đặc chỉ số
- [[private-credit-selective-defaults-obscure-systemic-banking-fragility]] — vỡ nợ có chọn lọc trong tín dụng tư nhân qua hoán đổi nợ kiệt quệ và PIK toggles che giấu rủi ro hệ thống lan truyền vào ngân hàng
- [[sovereign-debt-refinancing-dependency-constrains-monetary-policy-horizons]] — sự phụ thuộc vào tái cấp vốn nợ công biến nợ chính phủ thành bài toán luân chuyển dòng tiền và ràng buộc thời hạn thắt chặt của NHTW
- [[offshore-foreign-currency-debt-pricing-diverges-from-domestic-benchmarks]] — định giá nợ ngoại tệ offshore phân kỳ hoàn toàn khỏi lãi suất nội tệ nội địa và phản ánh các tầng phần bù rủi ro quốc tế
- [[endogenous-systemic-liquidity-circulation-distorts-accounting-equations-via-balance-sheet-resonance]] — hiện tượng cộng hưởng bảng cân đối do vận hành thanh khoản nội sinh làm biến dạng các phép cân đối số học và kéo dồn dòng tiền vào tài sản cuối
- [[technological-automation-shifts-scarcity-from-commodity-production-to-relational-sectors]] — tự động hóa công nghệ đẩy bản chất của sự khan hiếm và tỷ trọng chi tiêu từ sản xuất hàng hóa chuẩn hóa sang khu vực quan hệ

**Thị trường thu nhập cố định, Tiền tệ & Chính sách phi quy ước (Fixed Income Düring — Ch.1–9 / Part One)**
- [[fixed-income-instruments]] — hợp đồng quy định nghĩa vụ thanh toán xác định độc lập với tình trạng tài chính bên phát hành, phân biệt với vốn cổ phần
- [[securities-differ-from-bilateral-contracts-by-transferability-without-counterparty-consent]] — tính chuyển nhượng tự do không cần sự đồng thuận của đối tác phân biệt chứng khoán nợ khỏi hợp đồng song phương
- [[modern-credit-markets-shift-lenders-from-wealthy-elites-to-retirement-savers]] — sự đảo chiều cấu trúc tín dụng: người lao động tiết kiệm hưu trí cho doanh nghiệp và hộ gia đình vay nợ
- [[statutory-welfare-entitlements-function-as-virtual-fixed-income-claims-on-taxpayers]] — quyền lợi an sinh xã hội vô điều kiện vận hành như dòng niên kim thu nhập cố định ảo trên bảng cân đối quốc gia
- [[four-key-attributes-distinguish-cash-from-other-payment-assets]] — bốn đặc tính phân biệt tiền mặt: tất toán tức thì, ẩn danh, phi tập trung và dễ nhận biết
- [[seigniorage-and-transaction-costs-create-a-price-band-around-commodity-money-value]] — hành lang biến động giá trị tiền kim loại giữa chi phí đúc, nấu chảy và thuế seigniorage
- [[lex-monetae-grants-sovereign-currency-authority-but-does-not-eliminate-cross-border-or-market-constraints]] — nguyên lý chủ quyền tiền tệ không xóa bỏ ràng buộc nghĩa vụ nợ quốc tế hay liên minh tiền tệ
- [[fiat-money-removes-the-commodity-reserve-straightjacket-from-global-trade-settlement]] — tiền pháp định giải phóng thâm hụt thương mại quốc tế khỏi chiếc áo bó co hẹp dự trữ kim loại quý
- [[commercial-banks-create-inside-money-by-extending-credit]] — NHTM tạo tiền nội sinh ghi sổ thông qua mở rộng tín dụng song phương trên bảng cân đối kép
- [[multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures]] — bù trừ đa phương qua ma trận giao dịch tối ưu hóa thanh khoản và giảm thiểu rủi ro tín dụng đối tác
- [[commercial-bills-and-cheques-represent-claims-on-money-rather-than-money-itself]] — hối phiếu và séc đại diện cho quyền đòi tiền chứ không phải tiền tệ do thiếu tính pháp định và độ trễ tất toán
- [[bill-discounting-and-rediscounting-provide-dual-recourse-liquidity-to-the-banking-system]] — chiết khấu và tái chiết khấu hối phiếu cung cấp thanh khoản sơ cấp với cơ chế bảo đảm kép và là cội nguồn của cửa sổ chiết khấu
- [[narrow-banking-mandates-one-hundred-percent-reserve-backing-eliminating-private-credit-money]] — ngân hàng hẹp áp đặt dự trữ 100% bằng tiền trung ương để triệt tiêu việc tạo tiền tín dụng tư nhân
- [[price-level-targeting-commits-to-offset-past-inflation-deviations-unlike-inflation-targeting]] — mục tiêu mức giá ràng buộc bù đắp sai lệch lạm phát quá khứ, đối lập với lạm phát mục tiêu
- [[delphic-versus-odyssean-forward-guidance-delineates-forecast-contingency-from-unconditional-commitment]] — phân biệt forward guidance Delphic (dự báo có điều kiện) và Odyssean (cam kết vô điều kiện), đánh đổi tính khả tín và rủi ro vi phạm mandate
- [[large-scale-asset-purchases-expand-inside-money-and-lengthen-commercial-bank-balance-sheets]] — mua tài sản quy mô lớn từ khu vực phi ngân hàng mở rộng outside money đi kèm inside money, kéo giãn bảng cân đối NHTM và kích cầu repo GC
- [[helicopter-money-materializes-through-sovereign-debt-rollover-and-seigniorage-remittance]] — helicopter money vận hành qua tái đầu tư vô hạn gốc nợ chính phủ kết hợp hoàn trả thặng dư seigniorage thay vì hủy nợ hình thức
- [[index-tracking-asset-purchases-distort-free-float-liquidity-due-to-forced-holders]] — mua tài sản theo tỷ trọng chỉ số làm bóp nghẹt nguồn cung lưu hành tự do (free float) của tài sản chất lượng cao do sự hiện diện của forced holders
- [[prolonged-volatility-suppression-breeds-liquidity-fragility-and-var-shocks]] — nén biến động kéo dài làm suy thoái năng lực tạo lập thị trường, tích tụ vị thế một chiều và kích hoạt bán tháo cắt lỗ dây chuyền theo mô hình VaR
- [[central-bank-output-legitimacy-cannot-substitute-for-input-legitimacy-under-treaty-constraints]] — tính chính danh từ kết quả (output legitimacy) không thể thay thế cho ủy quyền hiến định (input legitimacy); nguyên tắc cân bằng tính tương xứng theo phán quyết BVerfG 2020

**Công cụ tiền mặt, Cấu trúc vi mô & Bù trừ trung tâm (Fixed Income Düring — Ch.10–12 / Part Two)**
- [[book-entry-securities-centralize-ownership-via-global-notes-and-csds]] — chứng khoán ghi sổ tập trung hóa sở hữu qua chứng chỉ nợ tổng (global note) và mạng lưới trung tâm lưu ký CSD/ICSD
- [[schuldschein-avoids-mark-to-market-accounting-through-transfer-restrictions]] — hợp đồng vay Schuldschein của Đức cho phép né tránh hạch toán giá thị trường nhờ giới hạn số lần chuyển nhượng
- [[fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities]] — quá trình khám phá giá truyền dẫn phân tầng từ công cụ thanh khoản dẫn dắt sang chứng khoán kém thanh khoản
- [[competitive-dealer-inquiries-incur-information-leakage-and-winners-curse]] — hỏi giá cạnh tranh qua nhiều đại lý làm rò rỉ thông tin dòng lệnh và gây ra rủi ro winner's curse cho đại lý thắng thầu
- [[delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles]] — cơ chế DvP triệt tiêu rủi ro thanh toán Herstatt thông qua các chu kỳ khớp lệnh và đối trừ định kỳ của tổ chức trung gian
- [[securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins]] — thất bại giao chứng khoán được kỷ luật bằng phí phạt giao trễ và xử lý qua nghiệp vụ vay repo hoặc mua ép buộc
- [[central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk]] — đối tác bù trừ trung tâm (CCP) chuyển hóa rủi ro tín dụng song phương thành rủi ro thanh khoản và rủi ro sụp đổ tập trung
- [[ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding]] — thác cơ chế bảo vệ của CCP ngăn ngừa mất khả năng thanh toán qua ký quỹ VM/IM, quỹ vỡ nợ tương hỗ và nghĩa vụ bỏ thầu bắt buộc
- [[xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices]] — hệ thống điều chỉnh định giá xVA (CVA, FVA, DVA) lượng hóa chi phí vốn và thanh khoản của các hợp đồng phái sinh song phương so với giá chuẩn bù trừ tập trung

**Thị trường tiền tệ, Chuẩn lãi suất RFRs & Cấu trúc Repo (Fixed Income Düring — Ch.13–14 / Part Two)**
- [[commercial-paper-and-short-term-instruments-compete-as-near-money]] — thương phiếu và công cụ ngắn hạn cạnh tranh trực tiếp với tiền gửi ngân hàng như tài sản tiền tệ gần (near-money)
- [[overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume]] — các chuẩn lãi suất phi rủi ro qua đêm (SOFR, €STR, SONIA) thay thế chuẩn IBOR nhờ khối lượng giao dịch thực tế
- [[lagged-compounded-overnight-rates-lack-term-risk-premia-and-delay-policy-transmission]] — lãi suất qua đêm dồn lãi có độ trễ thiếu phần bù rủi ro kỳ hạn và gây trễ hạn truyền dẫn chính sách tiền tệ
- [[futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows]] — khoản điều chỉnh lồi của hợp đồng tương lai phát sinh từ luồng tiền ký quỹ biến đổi (VM) hàng ngày
- [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]] — phân định giữa repo tài sản chung GC (định hướng tiền mặt) và repo specials (định hướng chứng khoán)
- [[repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk]] — tỷ lệ khấu trừ haircut quản trị biến động thanh lý nhưng tạo rủi ro sai chiều bất đối xứng cho bên cung cấp tài sản
- [[collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties]] — chuỗi tái thế chấp tài sản bảo đảm khuếch đại tình trạng chậm trễ thanh toán dây chuyền giữa các đối tác
- [[tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers]] — repo ba bên tập trung hóa quản trị tài sản bảo đảm và tiết giảm chi phí luân chuyển tiền mặt

**Định giá Trái phiếu, Rủi ro Lãi suất & Công cụ Lãi suất Thả nổi (Fixed Income Düring — Ch.15–17 / Part Two)**
- [[turn-premium-reflects-year-end-balance-sheet-constraints-rather-than-policy-rate-expectations]] — phần bù chuyển năm phản ánh áp lực co cụm bảng cân đối kế toán quy định cuối kỳ thay vì kỳ vọng lãi suất chính sách
- [[joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause]] — nghĩa vụ liên đới trong phát hành nợ công gây rủi ro đạo đức và bị Điều 125 TFEU cấm trong khu vực Euro
- [[dutch-and-american-auctions-differentiate-dealer-bidding-incentives-through-the-winners-curse]] — đấu thầu sơ cấp kiểu Mỹ và Hà Lan phân hóa động lực đặt lệnh của đại lý qua tác động bẫy kẻ thắng cuộc
- [[clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement]] — giá sạch loại bỏ biến động răng cưa của lãi dồn tích để định giá thị trường, giá bẩn xác định dòng tiền thanh toán
- [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]] — lợi suất đáo hạn giả định cấu trúc kỳ hạn phẳng và tái đầu tư đồng nhất, làm sai lệch tỷ suất sinh lời thực tế
- [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]] — modified duration đo rủi ro tương đối theo tài sản quản lý (AUM), PVBP đo rủi ro tiền mặt tuyệt đối theo sổ giao dịch danh nghĩa
- [[bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons]] — độ lồi nợ gốc đạt cực đại ở trung hạn rồi giảm ở kỳ hạn siêu dài do hiện giá suy giảm theo hàm mũ
- [[bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing]] — carry trái phiếu đo lường thu nhập ròng sau chi phí tài trợ repo và xác định mức giá kỳ hạn phi kinh doanh chênh lệch giá
- [[floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread]] — trái phiếu thả nổi tự động hồi quy về mệnh giá tại ngày chốt coupon khi biên độ chào bán bằng phần bù rủi ro tín dụng
- [[rfr-compounded-in-arrears-notes-require-observation-lags-and-synthetic-term-rates-to-quote-accrued-interest]] — trái phiếu thả nổi RFR tính lãi kép sau kỳ sử dụng lãi suất trung gian và độ trễ quan sát để niêm yết lãi dồn tích
- [[discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps]] — biên độ chiết khấu của FRN phân tách giữa phương pháp tính biệt lập giả định lãi suất phẳng và phương pháp hoán đổi tài sản theo đường cong
- [[constant-maturity-floaters-fail-par-reset-due-to-coupon-and-discount-tenor-mismatch]] — trái phiếu thả nổi kỳ hạn cố định phá vỡ đặc tính hồi quy mệnh giá do lệch pha kỳ hạn coupon và chiết khấu

**Thanh khoản thị trường, Mô hình đường cong & Phân tích cấu trúc kỳ hạn (Fixed Income Düring — Ch.18–20 / Part Two)**
- [[microscopic-versus-macroscopic-market-liquidity-separates-trade-breadth-from-balance-sheet-depth]] — phân tầng thanh khoản vi mô (bề rộng giao dịch) và thanh khoản vĩ mô (chiều sâu bảng cân đối lưu kho rủi ro)
- [[clobs-and-otc-market-making-differentiate-search-costs-from-information-leakage]] — sổ lệnh tập trung (CLOBs) và tạo lập thị trường OTC đánh đổi giữa chi phí tìm kiếm đối tác và rò rỉ thông tin
- [[spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias]] — độ phân tán sai số khớp đường cong spline đo lường gián tiếp sức chịu tải chênh lệch giá và sự thu hẹp bảng cân đối dealer
- [[on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures]] — phần bù thanh khoản on-the-run biến mất khi chức năng khám phá giá và phòng hộ tập trung vào hợp đồng tương lai
- [[yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields]] — liên kết chuyển đổi toán học giữa bốn biểu diễn cấu trúc kỳ hạn: hệ số chiết khấu, lãi suất zero, forward rate và par curve
- [[bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles]] — bóc tách bootstrapping trích xuất zero rates từ giá thị trường và reverse bootstrapping tái lập cấu trúc dòng tiền nghĩa vụ
- [[parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness]] — mô hình spline tham số hóa đánh đổi giữa độ chính xác định giá lại trái phiếu và độ trơn nhẵn của đường cong lãi suất kỳ hạn
- [[composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition]] — mô hình spline phức hợp phân tách đường cong chênh lệch để triệt tiêu hiện tượng giao cắt phi lý giữa đường cong cận quốc gia và chính phủ
- [[dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches]] — khớp giá theo trọng số DV01 tối ưu hóa bình phương tối thiểu tuyến tính, tăng tốc độ giải nghiệm hàng trăm lần so với tìm kiếm lợi suất phi tuyến
- [[parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments]] — dịch chuyển song song thống trị đường cong phản ánh điều chỉnh ước lượng lãi suất thực trung lập dài hạn và cam kết của NHTW
- [[convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end]] — thiên lệch độ lồi tăng theo căn bậc hai của kỳ hạn, đè nén lợi suất kỳ hạn dài và gây đảo ngược cấu trúc kỳ hạn đoạn siêu dài
- [[institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity]] — môi trường ưa thích của định chế và quy chế thanh khoản Solvency tạo trạng thái bán độ lồi cưỡng bức (short convexity)

**Carry, Roll-Down & Chênh lệch đường cong lợi suất (Fixed Income Düring — Ch.21–22 / Part Two)**
- [[upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields]] — cấu trúc toán học của đường cong dốc lên quy định forward rate vượt trên zero rate và zero rate vượt trên par yield
- [[holding-period-return-combines-carry-and-roll-down-quantified-by-break-even-yield-buffers]] — lợi suất nắm giữ tích hợp giữa carry tài trợ repo và roll-down trượt dốc, đo lường bằng đệm lợi suất hòa vốn
- [[z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves]] — z-spread (spline spread) chiết khấu từng dòng tiền độc lập trên đường cong zero, tự động điều chỉnh theo rủi ro thời lượng
- [[par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities]] — par swap spread phản ánh tính thanh khoản của trái phiếu chuẩn và bộc lộ các bước nhảy gián đoạn do phát hành mới
- [[par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks]] — hoán đổi tài sản par-par và proceeds phân hóa giữa cam kết vốn trả trước và rủi ro tín dụng đối tác khi đáo hạn
- [[interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision]] — chênh lệch hoán đổi nội suy (I-spread) đánh đổi giữa tính thanh khoản thực thi nhanh và độ trôi giá trị phòng hộ
- [[ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve]] — chênh lệch TED lượng hóa rủi ro liên ngân hàng bằng phương pháp dịch chuyển trực tiếp toàn bộ đường cong chiết khấu

**Trái phiếu liên kết lạm phát, Định giá TIPS & Động học lạm phát (Fixed Income Düring — Ch.23 / Part Three)**
- [[capital-indexed-tips-structure-operates-as-a-synthetic-foreign-currency-investment]] — cấu trúc nợ liên kết lạm phát TIPS bảo toàn sức mua thực tế, vận hành tương đương khoản đầu tư ngoại tệ tổng hợp
- [[sovereign-inflation-linked-issuance-hedges-tax-creep-and-extracts-the-inflation-risk-premium]] — phát hành nợ liên kết lạm phát phòng hộ hiện tượng trượt thuế (tax creep) và khai thác phần bù rủi ro lạm phát
- [[cpi-rebasing-and-ex-tobacco-conventions-prevent-index-distortions-in-inflation-linked-debt]] — kỹ thuật nối chuỗi đổi năm cơ sở và quy ước loại trừ thuốc lá bảo vệ tính liên tục và thanh khoản của nợ liên kết lạm phát
- [[inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering]] — tính mùa vụ của chỉ số CPI bắt buộc giá sạch hấp thụ biến động, gây méo mó lạm phát hòa vốn nếu thiếu lọc chu kỳ
- [[breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise]] — lạm phát hòa vốn thị trường phản ánh sự lây nhiễm từ biến động giá năng lượng và hoạt động phòng hộ của bàn giao dịch
- [[real-short-rates-and-inflation-forecasts-determine-the-arbitrage-free-carry-of-inflation-linked-bonds]] — chi phí mang của trái phiếu liên kết lạm phát phụ thuộc vào lãi suất ngắn hạn thực và dự báo lạm phát kỳ hạn
- [[comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves]] — mô hình định giá toàn diện xếp chồng động học lạm phát thực lên đường cong danh nghĩa, triệt tiêu sai số mùa vụ

**Rủi ro tín dụng, Thứ bậc nợ & Xếp hạng tín nhiệm (Fixed Income Düring — Ch.24 / Part Four)**
- [[default-insolvency-and-bankruptcy-differentiate-covenant-breaches-cash-shortfalls-and-terminal-liquidation]] — phân biệt vỡ nợ kỹ thuật (vi phạm covenant), mất khả năng thanh toán dòng tiền và phá sản giải thể tài sản
- [[debt-acceleration-and-cross-default-clauses-prevent-time-subordination-in-multi-creditor-structures]] — điều khoản gia tốc nợ và vỡ nợ chéo triệt tiêu tính ưu tiên hoàn trả theo thời gian trong cấu trúc nhiều chủ nợ
- [[statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors]] — thứ bậc nợ luật định và cơ chế bail-in (BRRD, TLAC/MREL, CoCo) cưỡng chế chia sẻ tổn thất cho chủ nợ ngân hàng
- [[sovereign-debt-operates-as-a-repeat-game-devoid-of-judicial-liquidation-and-enforceable-seniority]] — nợ chính phủ vận hành như trò chơi lặp lại không có cơ chế cưỡng chế thanh lý tư pháp hay thứ bậc nợ thực thi độc lập
- [[collective-action-clauses-resolve-creditor-coordination-failures-and-neutralize-hold-out-vultures]] — điều khoản hành động tập thể (CACs) ràng buộc biểu quyết đa số, phá vỡ bế tắc cân bằng Nash của các quỹ kền kền bám trụ
- [[credit-ratings-represent-ordinal-ranking-scales-distorted-by-the-issuer-pays-conflict-and-curse-of-the-commons]] — xếp hạng tín nhiệm là thang đo thứ bậc định tính, chịu méo mó từ xung đột lợi ích người phát hành trả tiền và bi kịch tài sản chung
- [[rating-migration-matrices-resolve-the-maturity-paradox-and-reveal-corporate-versus-sovereign-risk-divergence]] — ma trận dịch chuyển xếp hạng giải quyết nghịch lý rủi ro kỳ hạn và bộc lộ sự phân kỳ cấu trúc giữa doanh nghiệp và quốc gia

**Trái phiếu có bảo đảm, Chứng khoán hóa ABS & Thế chấp nhà ở RMBS (Fixed Income Düring — Ch.25–27 / Part Four)**
- [[covered-bonds-combine-on-balance-sheet-dual-recourse-with-insolvency-ring-fencing]] — trái phiếu có bảo đảm tối ưu hóa chi phí vốn qua cơ chế hoàn trả kép nội bảng và khoanh vùng tài sản khỏi thủ tục phá sản
- [[overcollateralization-optimizes-covered-bond-spreads-against-unsecured-asset-encumbrance]] — tài sản bảo đảm vượt mức (OC) tối ưu hóa giữa biên độ covered bond và chi phí đắt đỏ do trói buộc tài sản (asset encumbrance)
- [[danish-balance-principle-links-mortgage-origination-to-bond-pricing-through-delivery-and-prepayment-options]] — nguyên tắc cân bằng Đan Mạch khớp nối 1-1 khoản vay và trái phiếu qua quyền giao nộp (delivery) và trả trước (prepayment)
- [[asset-backed-securitization-achieves-bankruptcy-remoteness-via-true-sale-and-non-recourse-spvs]] — chứng khoán hóa ABS đạt tính cách ly phá sản ngoại bảng qua mua đứt bán đoạn (true sale) và SPV phi truy đòi
- [[tranching-mechanics-partition-collateral-losses-into-equity-mezzanine-and-senior-option-profiles]] — kỹ thuật phân tầng rủi ro phân bổ tổn thất tài sản thành các hồ sơ quyền chọn equity (call), mezzanine (straddle) và senior (put)
- [[mortgage-prepayments-combine-demographic-attrition-economic-refinancing-and-burn-out-effects]] — động học trả nợ trước hạn tích hợp hao mòn nhân khẩu, tái tài trợ kinh tế, hiệu ứng kiệt quệ (burn-out) và hàm bão hòa logistic
- [[rmbs-negative-convexity-arises-from-embedded-borrower-prepayment-options-and-wal-extension]] — độ lồi âm và thời lượng âm của RMBS phát sinh từ quyền chọn trả trước nhúng sẵn và hiện tượng kéo dài thời gian đáo hạn (WAL extension)
- [[tba-market-mechanics-and-dollar-rolls-manage-mortgage-origination-uncertainty]] — cơ chế thị trường giao dịch chuyển tiếp TBA và nghiệp vụ dollar roll (bù hoãn mua) xử lý bất định sản lượng nợ thế chấp

**Hợp đồng tương lai trái phiếu chính phủ & Kinh doanh chênh lệch giá Basis (Fixed Income Düring — Ch.28 / Part Five)**
- [[physical-delivery-bond-futures-deter-market-manipulation-through-post-settlement-inventory-exposure]] — giao nhận vật chất răn đe thao túng giá nhờ duy trì rủi ro kho hàng sau thanh toán, phụ thuộc sống còn vào thanh khoản repo
- [[bond-futures-market-microstructure-differentiates-clearing-netting-and-cftc-trader-categories]] — vi cấu trúc hợp đồng tương lai: bù trừ ròng agency vs principal netting, lọc nhiễu khối lượng roll và phân loại CFTC COT
- [[conversion-factors-induce-duration-dependent-cheapest-to-deliver-biases-around-notional-coupons]] — hệ số chuyển đổi chuẩn hóa giá hóa đơn quanh coupon danh nghĩa 6% và thiên kiến thời lượng định vị trái phiếu rẻ nhất CTD
- [[bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships]] — bộ ba gross basis, net basis và implied repo rate (IRR) trong kinh doanh chênh lệch giá cash-and-carry và tỷ lệ phòng hộ CTD
- [[quality-delivery-options-embed-negative-convexity-and-convexity-drag-in-bond-futures]] — quyền chọn hoán đổi chất lượng tạo độ lồi âm ngụ ý, lực cản độ lồi (convexity drag) và bước nhảy vọt rủi ro tại ngày thông báo giao hàng
- [[futures-rolls-maintain-interest-rate-hedges-via-pvbp-neutral-roll-ratios-below-parity]] — hoán đổi kỳ hạn futures roll ở trạng thái backwardation, tỷ lệ đảo vị thế trung hòa PVBP dưới 1 và cơ chế mở rộng Open Interest
- [[futures-delivery-windows-confer-timing-options-governed-by-carry-sign-and-repo-fails-risk]] — cửa sổ giao nhận mang lại quyền chọn định thời cho bên bán, phụ thuộc dấu của carry và rủi ro thất bại bù trừ repo fails
- [[futures-squeezes-and-repo-scarcity-invert-net-basis-into-negative-territory]] — hiện tượng ép giá futures qua thâu tóm repo specials đảo chiều net basis sang vùng âm và đẩy IRR tiệm cận trần lãi suất tái cấp vốn
- [[cash-settled-bond-futures-and-exchange-for-physical-substitute-delivery-with-swap-or-yield-baskets]] — hợp đồng tương lai thanh toán tiền mặt EDSP với PVBP cố định bằng 1 và giao dịch hoán đổi vật chất EFP bù trừ swap OTC

**Hợp đồng hoán đổi lãi suất, Nén giao dịch & Vi cấu trúc Swaps (Fixed Income Düring — Ch.29 / Part Five)**
- [[plain-vanilla-interest-rate-swaps-trade-pure-risk-and-resolve-preferred-habitat-friction]] — hoán đổi dòng tiền rủi ro thuần túy, giải tỏa ma sát môi trường ưa thích và phân hóa phụ lục bảo lãnh CSA
- [[swap-rate-term-structures-diverge-from-bank-bond-yields-due-to-panel-survivorship-bias]] — cấu trúc kỳ hạn swap rate phân kỳ khỏi lợi suất nợ ngân hàng do thiên lệch sống sót của hội đồng fixing và vai trò của IMM swaps
- [[multilateral-trade-compression-and-re-couponing-deflate-gross-notional-and-margin-drag]] — nén giao dịch đa phương TriOptima triệt tiêu danh nghĩa tổng và kỹ thuật re-couponing giải phóng lực cản ký quỹ bảng cân đối

**Giao dịch đường cong & Giá trị tương đối trái phiếu (Fixed Income Düring — Ch.30–32 / Part Six)**
- [[fixed-income-trade-governance-balances-probabilistic-stop-loss-and-epistemological-consistency]] — quản trị giao dịch thu nhập cố định: dừng lỗ xác suất trailing stop-loss, bẫy luật số lớn và giới hạn nhận thức luận Mean-Variance
- [[statistical-arbitrage-in-fixed-income-forfeits-initial-trend-movements-against-fundamental-dislocations]] — kinh doanh chênh lệch thống kê: sự đánh đổi giữa mean reversion và bỏ lỡ sóng dạt ban đầu trước các dịch chuyển cơ bản dài hạn
- [[curve-trading-hierarchies-systematically-immunize-lower-order-risk-dimensions]] — phân tầng rủi ro giao dịch đường cong: hệ n phương trình tự động triệt tiêu rủi ro bậc 1 đến n-1 độc lập với mô hình kinh tế
- [[steepeners-and-flatteners-neutralize-duration-via-pvbp-weighting-amid-structural-kinks]] — giao dịch dốc hóa và phẳng hóa: trung hòa thời lượng qua tỷ lệ PVBP và khai thác điểm gãy cấu trúc phòng hộ của bảo hiểm nhân thọ
- [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]] — giao dịch butterfly và condor: khai thác độ cong đường cong lợi suất và giải mã quy ước niêm yết trái ngược giữa bond và swap
- [[yield-curve-pca-factors-link-curvature-convexity-to-implied-rate-volatility]] — nhân tố PCA đường cong lợi suất: kết nối độ cong với độ biến động ngụ ý VXTYN qua độ lồi dương và hạn chế tham số Nelson-Siegel
- [[bond-relative-value-metrics-select-reference-curves-aligned-with-instrument-hedging-practices]] — lựa chọn đường cong tham chiếu giá trị tương đối: liên kết sovereign spline, composite spline và swap curve theo tập quán phòng hộ thực tế
- [[bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging]] — chiến lược giá trị tương đối trái phiếu: spread widener/tightener, basis trade mỏng và phòng hộ đa hợp đồng tương lai theo CTD

**Quản trị rủi ro danh mục, Phòng hộ & Tái cân bằng (Fixed Income Düring — Ch.33–38 / Part Seven)**
- [[pca-generalised-regression-resolves-bidirectional-noise-asymmetry-in-fixed-income]] — hồi quy tổng quát PCA: khắc phục bất đối xứng nhiễu hai chiều của OLS và khôi phục tính nghịch đảo đối xứng trong phòng hộ
- [[pca-eigenvalue-herfindahl-index-measures-yield-curve-complexity-and-hedging-breadth]] — chỉ số Herfindahl của giá trị riêng PCA: đo lường mức độ phức tạp động học đường cong và định hướng số lượng công cụ phòng hộ
- [[bond-index-construction-balances-ex-ante-replicability-and-liquidity-frictions]] — cơ chế xây dựng chỉ số trái phiếu: cân bằng giữa định nghĩa tiền nghiệm, tính khả thi sao chép thực tế và ma sát thanh khoản
- [[cross-market-settlement-conventions-induce-repo-funding-mismatches-in-global-indices]] — quy ước thanh toán đa thị trường: xung đột chu kỳ T+2 vs T+0/T+1 và giải pháp tài trợ repo trong tái phân bổ danh mục toàn cầu
- [[risk-neutral-portfolios-face-duration-aging-convexity-and-cross-gamma-instability]] — tính bất ổn định của danh mục trung hòa rủi ro: già hóa thời lượng DV01, hiệu ứng độ lồi và rủi ro cross-gamma ngoại hối
- [[long-only-fixed-income-portfolios-cannot-achieve-complete-risk-neutrality]] — danh mục trái phiếu chỉ mua: điều kiện độ nhạy trái dấu bất khả thi và tính bất khả triệt tiêu hoàn toàn rủi ro lãi suất thuần túy
- [[partial-index-replication-optimizes-tracking-error-against-cash-drag-and-turnover-costs]] — sao chép bán phần chỉ số: tối ưu hóa Lagrange spanning set, ràng buộc thanh khoản mềm và hóa giải lực cản tiền mặt bằng phái sinh
- [[yield-curve-model-hedges-immunize-state-variable-sensitivities-via-linear-systems]] — phòng hộ theo mô hình đường cong: triệt tiêu độ nhạy biến trạng thái qua hệ phương trình tuyến tính và cấu trúc bướm trung hòa PCA
- [[mean-variance-optimisation-fails-in-fixed-income-due-to-finite-maturity-and-covariance-instability]] — thất bại của tối ưu hóa Markowitz trong thu nhập cố định: kỳ hạn hữu hạn, già hóa duration và ma trận hiệp phương sai bất ổn
- [[dimension-reduction-via-asset-classes-and-pca-stabilizes-mean-variance-matrix-inversion]] — giảm chiều dữ liệu qua nhóm tài sản và PCA: ổn định phép nghịch đảo ma trận hiệp phương sai và kiểm soát rủi ro đặc thù
- [[portfolio-rebalancing-strategies-embed-implicit-assumptions-on-asset-return-autocorrelation]] — chiến lược tái cân bằng danh mục: giả định tự tương quan lợi suất ngầm định giữa no reallocation, tỷ trọng cố định, trend-following và mean reversion
- [[multi-currency-portfolio-rebalancing-distorts-asset-allocation-under-exchange-rate-shocks]] — biến dạng tái cân bằng danh mục đa tiền tệ: cú sốc tỷ giá hối đoái gây lệch pha quyết định mua bán giữa các quỹ nội địa và toàn cầu

**Thị trường trái phiếu chính phủ toàn cầu & Cấu trúc thể chế (Fixed Income Düring — Ch.39 / Part Eight)**
- [[euro-area-sovereign-debt-integration-relied-on-redenomination-and-reconventioning]] — hội nhập nợ công khu vực Euro: đổi đơn vị tiền tệ redenomination, chuẩn hóa quy ước reconventioning act/act và tổ chức lại bàn giao dịch
- [[sovereign-debt-maturity-trade-offs-balance-rate-volatility-against-refinancing-stability]] — đánh đổi cấu trúc kỳ hạn nợ công: cân bằng giữa biến động lãi suất và sự ổn định tái tài trợ, cùng giới hạn thị trường khi Kho bạc dùng hoán đổi IRS
- [[sovereign-exchange-auctions-and-liquidity-facilities-mitigate-redemption-profile-clumping]] — đấu thầu hoán đổi và cơ sở thanh khoản nợ công: kỹ thuật làm trơn hồ sơ đáo hạn của Bỉ, phát hành bổ sung trái phiếu cũ của Pháp và cơ sở repo của Hà Lan
- [[sovereign-floating-rate-debt-matches-retail-banking-assets-amid-benchmark-transitions]] — nợ chính phủ lãi suất thả nổi: công cụ CCT/CCT€ của Ý khớp dòng tiền ngân hàng tiết kiệm và chuyển dịch chuẩn đối chuẩn sang Euribor
- [[funded-pension-systems-anchor-ultra-long-sovereign-yield-curves-the-uk-gilt-case]] — hệ thống quỹ hưu trí tích lũy neo giữ đường cong siêu dài: cấu trúc thị trường trái phiếu chính phủ Anh Gilts, Consols và UKTI
- [[treasury-bill-maturity-clustering-functions-as-a-barometer-for-government-shutdown-risks]] — mật độ kỳ hạn tín phiếu Kho bạc Hoa Kỳ: phong vũ biểu định giá rủi ro chậm thanh toán trong các đợt bế tắc trần nợ công và đóng cửa chính phủ

**Quản trị rủi ro lãi suất sổ ngân hàng & Khung ALM (Tata 2025 — Ch.1)**
- [[interest-rate-risk-in-the-banking-book-irrbb]] — quản trị rủi ro lãi suất trên sổ ngân hàng: định nghĩa EBA/CRD IV, phân định banking book vs trading book và phạm vi các công cụ nhạy cảm lãi suất
- [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]] — hai góc nhìn bổ trợ song hành trong ALM: giá trị kinh tế EVE đo hiện giá dòng tiền dài hạn và thu nhập dồn tích NII đo lợi nhuận ngắn hạn
- [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]] — rủi ro khoảng chênh lệch lãi suất: bất cân xứng thời điểm và khối lượng định giá lại qua các dải kỳ hạn, phân tích khe hở tái định giá
- [[interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]] — rủi ro cơ sở lãi suất: tương quan không hoàn hảo giữa các chỉ số tham chiếu EURIBOR, OIS, RFR và Repo trên các công cụ cùng kỳ hạn
- [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]] — rủi ro quyền chọn lãi suất: quyền chọn tự động caps/floors/swaptions và quyền chọn hành vi ngầm định tiền gửi không kỳ hạn/trả trước nợ
- [[credit-spread-risk-in-the-banking-book-csrbb]] — rủi ro chênh lệch tín dụng sổ ngân hàng: biến động giá thị trường đối với rủi ro tín dụng và thanh khoản tách biệt khỏi đường cong lãi suất phi rủi ro
- [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]] — bài kiểm tra ngoại lệ giám sát SOT: 6 kịch bản sốc lãi suất theo CRD IV/EU 2024/856 và ngưỡng cảnh báo sớm 15% EVE, 5% NII theo vốn Tier 1
- [[banks-predominantly-hedge-duration-mismatches-on-balance-sheet-rather-than-via-derivatives]] — phòng hộ duration nội bảng trong thực tiễn ngân hàng: quy mô hoán đổi IRS ròng khiêm tốn do rào cản chuyên môn và điều kiện khắt khe của kế toán phòng hộ
- [[key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts]] — độ nhạy lãi suất điểm then chốt: cô lập độ nhạy giá trước cú sốc tại một điểm kỳ hạn, khắc phục giả định dịch chuyển song song để đo lường biến dạng đường cong

**Kỹ thuật ALM: Thước đo Giá trị Kinh tế & Thu nhập (Tata 2025 — Ch.2 cụm A)**
- [[economic-value-of-equity-eve-measures-net-present-value-of-banking-book-cash-flows]] — giá trị kinh tế của vốn chủ sở hữu EVE: hiện giá thuần NPV của toàn bộ dòng tiền sổ ngân hàng và nguyên tắc cấm kỵ vốn tự có trong mô hình
- [[repricing-gap-analysis-allocates-cash-flows-into-time-bands-by-next-reset-date]] — phân tích khe hở tái định giá: quy trình 5 bước phân bổ theo ngày reset kế tiếp, giao dịch at-par sau reset và tính toán tổng khe hở tái định giá
- [[duration-gap-analysis-quantifies-balance-sheet-mismatch-scaled-by-asset-base]] — phân tích khe hở thời lượng: đo lường bất cân xứng thời lượng tài sản - nguồn vốn điều chỉnh đòn bẩy, phản ánh kỳ hạn hành vi và so sánh sai số với Repricing Gap
- [[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]] — dự báo thu nhập lãi thuần NII: đường cơ sở baseline cho mô phỏng ALM hướng tới tương lai (prospective), chân trời 1–3 năm và cơ chế tự triệt tiêu sai số
- [[balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views]] — ba giả định tiến hóa bảng cân đối: góc nhìn tất toán dần (run-off), góc nhìn tĩnh (static view - chuẩn mực bắt buộc EBA) và góc nhìn động (dynamic view)
- [[interest-rate-projection-approaches-contrast-forward-rates-with-unchanged-yield-curves]] — hai trường phái dự phóng lãi suất ALM: lý thuyết kỳ vọng forward rates có thể phòng hộ đối lập giả định đường cong không đổi tránh thiên lệch phần bù thanh khoản
- [[earning-gap-analysis-estimates-short-term-nii-sensitivity-via-periodic-impact-weights]] — phân tích khe hở thu nhập: đo lường độ nhạy NII năm đầu tiên qua trọng số tác động định kỳ theo điểm giữa kỳ hạn
- [[receiver-interest-rate-swaps-stabilize-falling-rate-nii-while-magnifying-eve-duration-risk]] — phòng hộ NII bằng Receiver Swap: ổn định thu nhập khi lãi suất giảm, bẫy "too good to be true" khi giữ nguyên lãi suất và nghịch lý khuếch đại rủi ro EVE
- [[monitoring-market-value-changes-outside-nii-horizon-prevents-deferred-interest-rate-losses]] — giám sát biến động giá trị thị trường ngoài chân trời NII: đo lường Delta MV cho các vị thế Fair Value theo CDR (EU) 2024/857 chống che giấu tổn thất dài hạn

**Định giá Chuyển nhượng Vốn Nội bộ — FTP (Tata 2025 — Ch.2 cụm B)**
- [[funds-transfer-pricing-ftp-allocates-margins-and-centralizes-balance-sheet-risks]] — định giá chuyển nhượng vốn nội bộ FTP: phân bổ biên lãi thuần NIM, tập trung hóa rủi ro về Treasury và nguyên lý chi phí cơ hội
- [[matched-maturity-ftp-isolates-business-margins-and-structural-treasury-contributions]] — phương pháp cân khớp kỳ hạn: bóc tách NIM thành biên kinh doanh và đóng góp cấu trúc bù đắp rủi ro tái tài trợ và rủi ro lãi suất cho Treasury
- [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]] — bóc tách đường cong FTP: lãi suất phi rủi ro thuần túy cộng phần bù thanh khoản, 5 cách tiếp cận RFR và định giá sản phẩm lệch tenor reset
- [[ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation]] — chức năng điều hướng kinh doanh và bản chất chính trị của FTP: điều chỉnh cơ cấu bảng cân đối và nghiên cứu BCG về sự méo mó NII nội bộ
- [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] — tích hợp ràng buộc LCR và NSFR vào FTP: chi phí cận biên nắm giữ HQLA 30 ngày, hình phạt vốn dài hạn NSFR và chi phí ký quỹ bù trừ trung tâm CCP
- [[funds-transfer-pricing-contrasts-with-derivatives-funding-value-adjustments]] — so sánh FTP với FVA/XVA phái sinh: tài trợ 100% mệnh giá sổ ngân hàng vs chi phí ký quỹ tự tài trợ, và nguyên tắc loại trừ rủi ro tín dụng khỏi FTP
- [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]] — phụ phí thanh khoản dự phòng và quyền chọn ngầm định: phụ phí hạn mức cam kết tín dụng, điều chỉnh short/long optionality và 10 nguyên tắc vàng Farahvash

**Sản phẩm Không Kỳ hạn & Mô hình Danh mục Tái tạo (Tata 2025 — Ch.2 cụm C)**
- [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]] — sản phẩm không kỳ hạn NMP: sự phân kỳ giữa hồ sơ thanh khoản và hồ sơ lãi suất, cơ chế lãi suất chỉ định administered rate và 4 khung mô hình hóa
- [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]] — quyền chọn hành vi ngầm định: thực thi phi tối ưu do yếu tố nhân khẩu học, lợi ích ngân hàng khi short option và trần pháp lý EBA khống chế kỳ hạn tái định giá 5 năm
- [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]] — mô hình danh mục tái tạo: phân rã tiền gửi thành các tầng thế hệ vintage run-off, xác định duration kỳ vọng bình quân rủi ro lãi suất và kỳ hạn bình quân rủi ro thanh khoản
- [[rolling-portfolios-smooth-deposit-margins-through-moving-average-market-rates]] — danh mục cuốn chiếu rolling portfolio: cơ chế tái đầu tư dòng tiền bù đắp, tỷ suất cơ hội bình quân trượt MA làm mượt biên lợi nhuận và kết nối FTP
- [[replicating-portfolio-calibration-optimizes-margin-sharpe-ratios-across-key-rates]] — hiệu chuẩn danh mục tái tạo: tối ưu hóa tỷ số Sharpe của biên lợi nhuận, dung hòa đánh đổi giữa các lãi suất then chốt key rates 5Y vs 10Y và phân định ranh giới trách nhiệm ALM Desk
- [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]] — tái tạo động: phòng hộ biến động quy mô tiền gửi ở lãi suất thị trường giao ngay hiện hành, nguy cơ thua lỗ mark-to-market khi rút vốn lúc lãi suất tăng và các phân rã cấu trúc nâng cao
- [[sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models]] — phê phán thực nghiệm mô hình tái tạo: lãi suất dính sluggish pass-through 9% ngắn hạn, sự bất ổn của deposit beta qua các chu kỳ và hiện tượng sụp đổ duration thực nghiệm khi lãi suất đảo chiều

**Thực tiễn Quản trị ALM Ngân hàng (Tata 2025 — Ch.3)**
- [[bank-specific-alm-tailors-balance-sheet-governance-to-business-models-and-regional-habitats]] — tính đặc thù ngân hàng trong ALM: không có mô hình cào bằng, so sánh bảng cân đối ngân hàng đầu tư vs tiết kiệm, dị biệt vùng miền Châu Âu và tổ chức ALM Profit Center vs Cost Center
- [[net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]] — lập kế hoạch thu nhập lãi thuần NII: 3 chân trời Forecast/Budget/Plan, bản chất chính trị, kế hoạch quy mô run-off vs new business và hệ số Margin-Beta
- [[behavioral-alm-models-customer-irrbb-optionality-and-asymmetric-interbank-competition]] — kinh tế học hành vi trong ALM: bắt buộc EBA về mô hình hóa optionality, giới hạn backtesting và bất đối xứng cạnh tranh lãi suất giữa ngân hàng truyền thống vs neobanks
- [[holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage]] — ALM toàn diện: nâng tầm từ tuân thủ chiến thuật sang chiến lược sinh thái, vũ khí công nghệ AI, dữ liệu thay thế và thương mại hóa năng lực đo lường rủi ro
- [[zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp]] — sàn lãi suất 0% trong kỷ nguyên NIRP: sự hình thành tiền gửi cứng nhắc rigid deposits, xói mòn biên trung gian tài chính và phán quyết tư pháp BGH cấm lãi suất vay âm
- [[coupon-floors-and-indicator-floors-induce-asymmetric-nii-exposures-in-negative-rates]] — phân biệt Coupon Floor và Indicator Floor: công thức toán tài chính, tính chất in-the-money khi lãi suất âm và tác động bất đối xứng đẩy NII rơi vào vùng âm
- [[rapid-rate-tightening-exposes-duration-gaps-and-asymmetric-prepayment-speeds]] — chu kỳ tăng lãi suất thần tốc: sụp đổ tâm lý tự mãn, cảnh báo sớm của ECB bị bỏ quên, bùng nổ Duration Gap và sự phân hóa tốc độ trả nợ trước hạn giữa vay cố định và thả nổi

**Nghiên cứu Tình huống: Sự Sụp đổ của Silicon Valley Bank (Tata 2025 — Ch.4)**
- [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs]] — vụ sụp đổ Silicon Valley Bank: lệch pha thời lượng không phòng hộ, tiền gửi không bảo hiểm >88%, lỗ bán chứng khoán 1,8 tỷ USD và cuộc tháo chạy 42 tỷ USD/ngày
- [[held-to-maturity-gaap-accounting-masks-unrealized-economic-value-losses-in-banking-books]] — kế toán HTM theo GAAP che giấu lỗ EVE: giá gốc phân bổ che giấu khoản lỗ 15,2 tỷ USD xóa sạch vốn tự có 12 tỷ USD và ảo ảnh ổn định từ báo cáo NII dương 4,5 tỷ USD
- [[unhedged-interest-rate-swap-unwinding-magnifies-balance-sheet-vulnerability-for-short-term-pnl]] — gỡ bỏ vị thế hoán đổi IRS để thổi phồng P&L ngắn hạn: tỷ lệ phòng hộ danh mục trái phiếu 124 tỷ USD rớt từ 12,3% xuống 0,4% ngay trước chu kỳ tăng lãi suất
- [[svb-three-year-duration-gap-breached-supervisory-outlier-thresholds-absent-deposit-modeling-manipulation]] — khe hở thời lượng 3 năm của SVB: tổn thất 12,5 tỷ USD vượt 100% vốn tự có trước cú sốc 200 bps và nghịch lý toán học đòi hỏi duration tiền gửi >3,7 năm để lách SOT
- [[regulatory-arbitrage-via-deposit-duration-assumptions-distorts-supervisory-irrbb-compliance]] — trọng tài quy chế qua mô hình hóa thời lượng tiền gửi: báo cáo Michael Barr 2023 về việc sửa giả định thay vì phòng hộ bảng cân đối và cơ chế tháo chạy bad-news run
- [[supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb]] — thất bại quản trị và giám sát trong vụ SVB: khuyết chức danh CRO suốt 8 tháng, sự thiếu kiên quyết trong kỳ thi CAMELS 2020–2022 và 4 bài học lớn cho ALM

**Quy chuẩn Giám sát & Quản lý IRRBB Mới (Tata 2025 — Ch.5)**
- [[multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards]] — khung quản trị IRRBB đa tầng: 4 cấp độ BCBS, CRD I-VI, CRR I-III và EBA Single Rulebook
- [[eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement]] — phương pháp chuẩn hóa EBA SA theo CDR 2024/857: hài hòa đo lường EVE (run-off, optionality) và NII (constant balance sheet, 3 cấu phần dòng tiền, Delta MV)
- [[simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks]] — phương pháp chuẩn hóa đơn giản S-SA: tinh giản cho ngân hàng nhỏ SNCI, nguyên tắc thận trọng tối thiểu bằng SA và thẩm quyền can thiệp của NCA
- [[maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb]] — sàn lãi suất tuyến tính mới theo CDR 2024/856: điểm chặn dưới -150 bps tăng tuyến tính 3 bps/năm đến 0% tại kỳ hạn 50 năm
- [[simultaneous-compliance-problem-constrains-fixed-rate-allocation-under-dual-sot-limits]] — nghịch lý tuân thủ đồng thời: mâu thuẫn giữa chặn trên/dưới của SOT EVE và sàn tối thiểu của SOT NII, bài toán quy hoạch tuyến tính và vùng tuân thủ khả thi
- [[supervisory-irrbb-reporting-mandates-five-standardized-templates-under-eu-2024-855]] — báo cáo giám sát IRRBB theo CDR 2024/855: 5 bộ mẫu biểu chuẩn hóa bắt buộc từ tháng 10/2024 kết nối đánh giá tổng hợp, dòng tiền và thông số hành vi

**Tương lai của ALM: FinTech, Tài sản số, AI & Rủi ro Khí hậu (Tata 2025 — Ch.6)**
- [[fintech-disruption-accelerates-deposit-disintermediation-and-shortens-behavioral-maturities]] — đột phá FinTech và phi trung gian hóa tiền gửi: xói mòn quan hệ ngân hàng truyền thống, chuyển dịch tài sản thế hệ digital natives và rút ngắn kỳ hạn hành vi NMD
- [[tokenized-deposits-and-smart-contracts-enable-automated-interest-rate-arbitrage]] — tiền gửi mã hóa và hợp đồng thông minh: cơ chế chênh lệch lãi suất tự động, triệt tiêu quán tính tâm lý người gửi tiền và nguy cơ tháo chạy dòng vốn theo thuật toán
- [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]] — Deep ALM và phân tích nâng cao BD&AA: ứng dụng học tăng cường sâu, Deep Hedging/Deep Treasury và mô phỏng thời lượng tiền gửi cá nhân hóa theo thời gian thực
- [[model-governance-for-ai-in-alm-balances-predictive-power-against-black-box-opacity]] — quản trị mô hình AI trong ALM: chuẩn mực giải trình EBA GL/2022/14, rủi ro hộp đen FSB, nguy cơ bầy đàn mô hình model herding và trợ lý AI SupTech cho thanh tra
- [[climate-risk-transmission-channels-impact-bank-balance-sheets-and-ftp-pricing]] — rủi ro khí hậu trong ALM: 4 kênh truyền dẫn vào bảng cân đối, phụ phí định giá chuyển vốn Climate FTP add-on, bài kiểm tra sức ép ECB 2022 và Hướng dẫn mô hình nội bộ ECB 2024
- [[granular-customer-segmentation-enhances-behavioral-modeling-of-banking-book-optionality]] — phân khúc khách hàng đa biến vi mô: 5 tiêu chí định lượng Soulellis, kiểm định hồi tố backtesting và nhận diện các điểm mù tâm lý tổ chức theo thanh tra Fed hậu SVB

**Phân tích & Diễn giải Đường cong Lợi suất (Choudhry — Ch.1)**
- [[yield-curve]] — đường cong lợi suất: đồ thị thể hiện cấu trúc kỳ hạn, 4 chức năng thị trường, phân biệt lợi suất YTM và lãi suất zero-coupon thực sự
- [[coupon-bias-induces-relative-yield-distortions-along-ytm-curves]] — hiệu ứng coupon: rủi ro tái đầu tư và chính sách thuế khiến trái phiếu coupon cao giao dịch rẻ hơn so với đường cong
- [[par-yield-curve-derives-required-coupons-for-at-par-debt-issuance]] — đường cong lợi suất ngang mệnh giá: phương pháp bóc tách từ hệ số chiết khấu zero và vai trò ấn định coupon phát hành nợ sơ cấp
- [[implied-forward-rates-function-as-hedge-rates-rather-than-accurate-market-forecasts]] — lãi suất kỳ hạn ngụ ý: vận hành như mức lãi suất phòng hộ không chênh lệch giá thay vì công cụ dự báo chuẩn xác điểm rơi thị trường
- [[local-expectations-hypothesis-resolves-jensens-inequality-under-risk-neutrality]] — giả thuyết kỳ vọng cục bộ: biến thể duy nhất đảm bảo điều kiện phi kinh doanh chênh lệch giá và giải quyết bất đẳng thức Jensen
- [[humped-yield-curves-reflect-peaked-interest-rate-expectations-or-maturity-habitat-imbalances]] — đường cong lợi suất hình bướu: phản ánh kỳ vọng lãi suất tạo đỉnh hoặc sự bất đối xứng cung cầu giữa ngân hàng (đầu ngắn) và quỹ hưu trí (đầu dài)
- [[cubic-splines-preserve-forward-rate-smoothness-via-first-and-second-derivative-continuity]] — khớp đường cong cubic spline: duy trì tính liên tục của độ dốc và độ lồi tại các điểm nút, ngăn chặn bước nhảy gãy khúc trên đường cong forward
- [[collateralized-clearing-and-hedging-demand-drive-interest-rate-swaps-below-sovereign-yields]] — nghịch lý chênh lệch hoán đổi âm hậu 2008: cơ chế bù trừ CCP, cầu phòng hộ nhận cố định dài hạn và quy định vốn ngân hàng kéo lãi suất swap xuống dưới lợi suất trái phiếu chính phủ

**Động học Lãi suất Giao ngay & Kỳ hạn trong Thời gian Liên tục (Choudhry — Ch.2)**
- [[instantaneous-forward-curves-lead-spot-curve-inflections-and-peak-earlier]] — đường cong kỳ hạn tức thời dẫn dắt và tạo đỉnh sớm: hệ quả vi tích phân và quy luật tỷ suất biên khiến forward rate bắt buộc quay đầu giảm trước đỉnh của spot curve
- [[arbitrage-free-bond-prices-evolve-as-martingales-under-risk-neutral-measures]] — định giá trái phiếu phi trọng tài theo quá trình martingale: kỳ vọng trung lập rủi ro của tài khoản tiền tệ và tích phân lãi suất ngắn hạn
- [[mcculloch-spline-fitting-estimates-continuous-discount-functions-from-incomplete-and-noisy-coupon-bonds]] — phương pháp spline McCulloch và hồi quy OLS: ước lượng hàm chiết khấu liên tục, xử lý nhiễu thanh khoản và khoảng trống kỳ hạn của trái phiếu coupon
- [[term-structure-modeling-bifurcates-into-short-rate-diffusion-and-forward-rate-hjm-frameworks]] — hai trường phái mô hình hóa cấu trúc kỳ hạn: phân nhánh giữa khuếch tán lãi suất ngắn hạn (short-rate diffusion) và khung mô hình lãi suất kỳ hạn liên tục (HJM)

**Mô hình hóa Lãi suất I: Khái niệm Cơ sở, Bổ đề Itô & Khuếch tán Ngẫu nhiên (Choudhry — Ch.3)**
- [[ornstein-uhlenbeck-mean-reversion-prevents-infinite-drift-in-short-rate-diffusion]] — cơ chế hoàn lương Ornstein-Uhlenbeck: ngăn chặn sự trôi dạt vô cực của lãi suất ngắn hạn và hội tụ về mức trung hòa dài hạn
- [[itos-lemma-transforms-short-rate-stochastic-dynamics-into-bond-pricing-pdes]] — bổ đề Itô và phương trình vi phân định giá trái phiếu: biến đổi vi phân ngẫu nhiên bậc hai và phòng hộ phi chênh lệch giá
- [[one-factor-term-structure-models-force-perfect-yield-correlation-across-maturities]] — mô hình một nhân tố và rào cản tương quan hoàn hảo: sự cứng nhắc của giả định đơn biến và nhu cầu mở rộng đa nhân tố
- [[markov-property-reduces-contingent-claim-valuation-to-single-state-pdes]] — đặc tính Markov của lãi suất ngắn hạn: tính chất phi phụ thuộc quỹ đạo lịch sử và thu gọn định giá phái sinh về phương trình PDE đơn biến

**Mô hình hóa Lãi suất II: Động học Giá Tài sản, Chuyển động Brown & Phân phối Lognormal (Choudhry — Ch.4)**
- [[geometric-brownian-motion-ensures-strictly-positive-asset-prices-via-multiplicative-increments]] — chuyển động Brown hình học: bảo đảm giá tài sản luôn dương qua gia số nhân tử và giới hạn khi mô hình hóa lãi suất
- [[itos-lemma-derives-the-lognormal-asset-price-distribution-via-convexity-drag-correction]] — bổ đề Itô và phân phối log-normal: khấu trừ độ lồi $-\frac{1}{2}\sigma^2$ và sự suy giảm tăng trưởng tích lũy
- [[bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics]] — phương trình khuếch tán giá trái phiếu: xác lập quy luật tỷ lệ thời lượng và thặng dư độ lồi bậc hai $+\frac{1}{2}s^2(T-t)^2$
- [[pull-to-par-effect-forces-bond-price-volatility-to-decay-deterministically-to-zero-at-maturity]] — hiệu ứng kéo về mệnh giá: sự suy giảm tất định của độ biến động giá trái phiếu về không khi đáo hạn

**Mô hình hóa Lãi suất III: Mô hình Cân bằng, Mô hình Phi trọng tài & Cấu trúc Kỳ hạn Lãi suất Ngắn hạn (Choudhry — Ch.5)**
- [[equilibrium-models-generate-term-structures-from-macro-assumptions-while-arbitrage-free-models-calibrate-to-market-prices]] — mô hình cân bằng và phi trọng tài: sự đối lập triết học giữa suy diễn kinh tế vĩ mô dài hạn và kỹ thuật khớp giá thị trường
- [[vasicek-model-incorporates-mean-reversion-into-gaussian-dynamics-but-permits-negative-interest-rates]] — mô hình Vasicek: động học Gaussian Ornstein-Uhlenbeck, cấu trúc giá trái phiếu affine và rủi ro lãi suất âm khi biến động lớn
- [[cox-ingersoll-ross-model-scales-volatility-by-the-square-root-of-rates-to-preclude-negative-yields]] — mô hình Cox-Ingersoll-Ross: quá trình khuếch tán căn bậc hai $\sigma\sqrt{r_t}$, điều kiện Feller và loại trừ hoàn toàn lãi suất âm
- [[hull-white-model-extends-vasicek-via-time-dependent-drift-to-match-the-initial-yield-curve]] — mô hình Hull-White: mở rộng Vasicek qua hàm trôi dạt theo thời gian $\theta(t)$, tái lập chính xác đường cong giao ngay và duy trì nghiệm giải tích đóng
- [[black-derman-toy-model-imposes-lognormal-short-rate-dynamics-on-arbitrage-free-binomial-trees]] — mô hình Black-Derman-Toy: cấu trúc cây nhị phân lognormal, bảo đảm lãi suất luôn dương và thuật toán hiệu chuẩn số quy nạp xuôi

**Mô hình hóa Lãi suất IV: Khung HJM, Mô hình Thị trường BGM & Phân bổ Mô hình (Choudhry — Ch.6)**
- [[heath-jarrow-morton-framework-locks-forward-rate-drift-strictly-to-volatility-structures]] — khung mô hình Heath-Jarrow-Morton: sự tiến hóa toàn bộ đường cong kỳ hạn tức thời và điều kiện phi trọng tài khóa chặt trôi dạt theo biến động
- [[libor-market-models-bridge-hjm-to-observable-discrete-forward-rates-and-black-76-swaption-pricing]] — mô hình thị trường LIBOR / BGM: cầu nối giữa lý thuyết HJM và lãi suất kỳ hạn rời rạc quan sát được, tương thích chuẩn Black-76 cho caps và swaptions
- [[jump-diffusion-interest-rate-models-capture-abrupt-policy-rate-shocks-via-poisson-processes]] — mô hình khuếch tán bước nhảy: tích hợp quá trình Poisson nắm bắt cú sốc gián đoạn chính sách tiền tệ và giải thích nụ cười biến động
- [[relative-value-trading-mandates-equilibrium-models-while-derivative-market-making-requires-arbitrage-free-models]] — quy tắc phân công mô hình: giao dịch giá trị tương đối bắt buộc dùng mô hình cân bằng, tạo lập phái sinh bắt buộc dùng mô hình phi trọng tài
- [[multi-factor-term-structure-models-are-demanded-by-cross-rate-correlation-and-volatility-smiles]] — tiêu chuẩn lựa chọn mô hình đa nhân tố: sản phẩm nhạy cảm tương quan chéo spread/quanto, nụ cười biến động và chứng khoán thế chấp MBS nhạy cảm độ dốc

**Đường cong Lợi suất Trái phiếu Liên kết Lạm phát & Kỳ vọng Lạm phát (Choudhry — Ch.7)**
- [[real-yield-curves-reflect-real-cost-of-capital-and-fluctuate-with-economic-growth]] — đường cong lợi suất thực: phản ánh chi phí vốn thực, biến động theo tăng trưởng GDP thực và bác bỏ giả định hằng số cổ điển
- [[implied-forward-inflation-curves-isolate-marginal-inflation-expectations-via-fisher-identity]] — đường cong lạm phát kỳ hạn ngụ ý: bóc tách kỳ vọng lạm phát biên tại từng kỳ hạn qua đồng nhất thức Fisher ghép lãi và nhận diện phần bù bất định
- [[indexation-lags-require-iterative-consistency-procedures-in-real-term-structure-estimation]] — quy trình lặp nhất quán lạm phát: xử lý nghịch lý độ trễ chỉ số hóa dòng tiền và kỹ thuật giảm thiểu điểm nút spline khi khớp cấu trúc kỳ hạn thực

**Định giá và Phân tích Đường cong Lợi suất Kỷ nguyên Hậu 2008 (Choudhry — Ch.8)**
- [[dual-curve-discounting-separates-rate-projection-from-collateralized-cash-flow-discounting]] — khuôn khổ chiết khấu hai đường cong: phân định đường cong dự phóng LIBOR và đường cong chiết khấu OIS sau khủng hoảng 2008
- [[credit-support-annex-discounting-incorporates-cheapest-to-deliver-collateral-optionality]] — chiết khấu theo phụ lục CSA: quyền chọn giao nộp tài sản bảo đảm rẻ nhất (CTD) và đường cong chiết khấu lai đa tiền tệ
- [[derivatives-funding-valuation-adjustments-apply-bank-internal-cost-of-funds-directly-to-expected-exposure]] — điều chỉnh định giá vốn (FVA): áp dụng trực tiếp đường cong chi phí vốn nội bộ (COF/FTP) lên mức phơi nhiễm kỳ vọng
- [[cross-currency-basis-and-quanto-adjustments-align-internal-funding-curves-across-currencies]] — chênh lệch cơ sở tiền tệ chéo và điều chỉnh quanto: quy trình tập trung chuẩn hóa đường cong điều vốn ngoại tệ và bù đắp tương quan tỷ giá - tín dụng

**Phân tích Lợi suất và Chiết khấu trong Môi trường Lãi suất Âm (Choudhry — Ch.9)**
- [[discount-factor-functions-exhibit-asymmetric-convexity-and-exceed-unity-in-negative-interest-rates]] — hàm hệ số chiết khấu trong lãi suất âm: tính chất vượt quá 1, điểm kỳ dị tại r = -1, độ lồi bất đối xứng và cơ chế ghép lãi
- [[negative-yield-to-maturity-implies-bond-market-prices-exceed-nominal-aggregate-cash-flows]] — lợi suất đáo hạn âm: hàm ý giá thị trường trái phiếu vượt tổng danh nghĩa dòng tiền tương lai, tính đơn nhất nghiệm phương trình đa thức và phân tích thực nghiệm trái phiếu chính phủ Thụy Sĩ/Đức

**Ước lượng và Khớp Đường cong Lợi suất I: Spline và Mô hình Nelson-Siegel (Choudhry — Ch.10)**
- [[nelson-siegel-and-svensson-models-fit-parsimonious-forward-curves-with-asymptotic-long-rate-stability]] — mô hình Nelson-Siegel và Svensson: ước lượng cấu trúc kỳ hạn tinh gọn, bảo đảm tiệm cận ngang ở kỳ hạn dài $\beta_0$ và loại bỏ sự phụ thuộc vào điểm nút spline
- [[b-splines-and-regression-splines-transform-piecewise-polynomial-curve-fitting-into-linear-least-squares]] — B-splines và hồi quy spline: chuyển hóa bài toán khớp đường cong đa thức từng khúc thành hồi quy bình phương tối thiểu tuyến tính OLS thông qua hàm cơ sở và biến ghép
- [[forward-rate-oscillation-reveals-magnified-fitting-errors-and-disqualifies-linear-interpolation]] — hiện tượng dao động lãi suất kỳ hạn ngụ ý: sự khuếch đại sai số vi mô từ hàm chiết khấu và lý do thị trường bãi bỏ phép nội suy tuyến tính

**Ước lượng và Khớp Đường cong Lợi suất II: Mô hình VRP Spline và Anderson-Sleath (Choudhry — Ch.11)**
- [[variable-roughness-penalty-splines-balance-short-end-flexibility-and-long-end-smoothness]] — spline phạt độ gập ghềnh biến thiên: kỹ thuật Waggoner VRP và Fisher GCV dung hòa độ linh hoạt ngắn hạn và độ trơn ổn định dài hạn
- [[anderson-sleath-model-weights-fitting-errors-by-inverse-modified-duration]] — mô hình Anderson-Sleath của Bank of England: chuẩn hóa sai số định giá theo nghịch đảo thời lượng điều chỉnh $1/MD_i$ và đặc tính cô lập cú sốc cục bộ so với Svensson
- [[exponential-splines-linearize-discount-functions-via-asymptotic-maturity-transforms]] — spline hàm mũ Vasicek-Fong: tuyến tính hóa hàm chiết khấu qua phép biến đổi tiệm cận $x = 1 - e^{-\alpha T}$, cubic exponential splines và đánh giá thực nghiệm của Shea

**Đường cong Lợi suất và Giao dịch Giá trị Tương đối (Choudhry — Ch.12)**
- [[excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions]] — chênh lệch lợi suất thặng dư: bóc tách giá trị tương đối cục bộ qua mô hình chênh lệch coupon $r_m - r_{mp} = c(C_{PD} - r_{mp}) + d$, định kiến né tránh coupon cao và sàn thanh khoản tín phiếu kho bạc
- [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]] — giao dịch spread cân bằng BPV: triệt tiêu rủi ro thị trường định hướng bậc một, rủi ro trôi tỷ trọng phi tuyến của Modified Duration và khung kỷ luật ba nhân tố (target spread, fixed horizon, stop-loss 50%)
- [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]] — chi phí tài trợ repo và rủi ro lãi suất đặc biệt: ngưỡng hòa vốn của chiến lược spread liên phân đoạn, chi phí mang giữ ròng (net carry) và hiện tượng ép giá repo chân bán khống

**Xác định Giá trị Tương đối trên Thị trường Kho bạc Hoa Kỳ (Choudhry — Ch.13)**
- [[ancillary-yield-curves-expand-benchmark-definitions-via-strict-irr-admissibility]] — đường cong phụ trợ Ancillary Curve: mở rộng định nghĩa trái phiếu chuẩn qua tiêu chuẩn sàng lọc sai số IRR dưới 1 điểm cơ bản, độ chính xác MAPE vượt trội và sự hòa nhập đồng quy với Benchmark Curve
- [[geometric-programming-optimizes-continuous-discount-curves-under-bounded-uncertainty]] — quy hoạch hình học GP và bất định phi ngẫu nhiên: đổi biến hàm mũ $x_i = e^{y_i}$, tối ưu hóa posynomials, tiếp cận sai số bị chặn set-membership và điều kiện đối ngẫu hoàn hảo khi phân tách T-bills
- [[ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets]] — giao dịch Butterfly neo theo trái phiếu Ancillary: khai thác giá trị tương đối trong thị trường Kho bạc siêu thanh khoản, bán khống mã Ancillary định giá đắt và phòng hộ hai cánh qua bài toán quy hoạch tuyến tính LP trung hòa vốn và thời lượng
