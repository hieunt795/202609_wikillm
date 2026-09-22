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
| `choudhry_analysing_yield_curve` | Nguồn dài (703 KB / 6.177 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |
| `choudhry_fixed_income_markets` | Nguồn dài (1.941 KB / 15.414 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |
| `fixed_income_during` | Nguồn dài (42 file, 1.112 KB / 7.300 dòng) | **Chưa ingest** | Ch.1–39 (front matter, Bibliography, Index bỏ qua) | `03_state/fixed_income_during.md` |
| `tata_bank_alm` | Nguồn dài (450 KB / 3.345 dòng) | **Chưa ingest** | Toàn bộ | chưa dựng |

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
- [[sterilization-offsets-fx-intervention-but-only-temporarily]] — tiệt trùng và giới hạn, hội đồng tiền tệ
- [[perfect-capital-mobility-with-a-fixed-exchange-rate-strips-monetary-policy-of-independence]] — lãi suất trong nước bị ép về mức thế giới
- [[currency-substitution-undermines-monetary-control]] — đô la hoá
- [[financial-innovation-blurs-the-boundary-of-money]] — đổi mới tài chính, đánh đổi liên quan/kiểm soát
- [[foreign-exchange-intervention]] — mua bán ngoại tệ làm tài sản đối ngoại và tiền dự trữ đổi cùng chiều
- [[open-market-operations]] — mua bán giấy tờ có giá của chính phủ; công cụ trung hoà can thiệp ngoại hối
- [[discount-window]] — tín dụng của ngân hàng trung ương cho ngân hàng; lãi suất chiết khấu báo hiệu lập trường chính sách

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
- [[financial-programming]] — gói chính sách định lượng, phối hợp; khung IMF dựa trên phân biệt tiền nguồn gốc trong nước/đối ngoại

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
- [[sterilization]] — vô hiệu hóa: nghiệp vụ triệt tiêu tác động của can thiệp ngoại hối lên cung tiền trong nước

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



