# Index

> Mục lục trang wiki theo chủ đề. Cập nhật mỗi khi có trang mới (xem `.claude/skills/ingest/SKILL.md` bước 6).

## Sources

Trạng thái ingest từng nguồn trong `01_sources/`. **Cập nhật mỗi lượt ingest**, kể cả lượt không tạo trang mới (`ingest/SKILL.md` bước 6). Bảng này chỉ tóm tắt ở cấp nguồn — tiến độ theo chunk của nguồn dài nằm trong `03_state/<tên_nguồn>.md` (`00_schema.md` §10), và đó mới là nguồn sự thật khi cần biết chi tiết "còn lại phần nào".

| Nguồn | Phân loại | Trạng thái | Phần còn lại | State file |
|---|---|---|---|---|
| `imf_macro_accounting` | Nguồn dài (829 KB / 6.065 dòng) | **Đang ingest dở** | Ch.2 đã viết lại toàn bộ từ nguồn (2026-09-15; bản cũ ở tag `ch2-snapshot`). Chưa ingest: Ch.1 (tổng quan chuyển đổi Ba Lan); Ch.4 (cán cân thanh toán); Ch.5 (tiền tệ); Ch.6 (flow of funds). Đã xong: Ch.3 phần lý luận (cụm A–E); Ch.3 bỏ qua phần bối cảnh Ba Lan và Exercises (§2) | `03_state/imf_macro_accounting.md` |
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
- [[gndi]] — thu nhập khả dụng để tiêu hoặc để dành
- [[absorption]] — tổng cầu nội địa (C + I)
- [[aggregate-demand]] — cầu với hàng trong nước, gồm xuất khẩu ròng
- [[gross-national-saving]] — phần dư sau tiêu dùng
- [[final-consumption]] — phần hộ gia đình và chính phủ sử dụng, đối lập với tiêu dùng trung gian
- [[gross-investment]] — bổ sung vốn vật chất, không phải mua tài sản tài chính
- [[depreciation]] — đại lượng tách mọi cặp gộp/ròng
- [[leakages-equal-injections-in-the-circular-flow]] — dòng luân chuyển nối các khu vực, rò rỉ bằng bơm vào

**Đồng nhất thức đối ngoại**
- [[balance-of-payments]] — báo cáo giao dịch với phần còn lại của thế giới; chương gốc là Ch.4
- [[current-account-deficit-means-absorption-exceeds-national-income]] — GNDI − A = CAB
- [[the-saving-investment-gap-equals-the-current-account-balance]] — S − I = CAB
- [[the-private-sector-resource-gap-must-be-financed-by-other-sectors]] — ràng buộc ngân sách ở cấp khu vực

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
- [[inflation-tax-revenue-peaks-because-high-inflation-shrinks-its-base]] — đường chữ U ngược

**Nợ công và tính bền vững**
- [[fiscal-sustainability]] — hub: định nghĩa đồng thuận, ổn định nợ và khả năng thanh toán
- [[real-interest-rate]] — lãi suất trừ lạm phát kỳ vọng; biến trung tâm của bền vững nợ
- [[high-debt-ratios-raise-real-interest-rates-and-erode-market-confidence]] — nợ cao tốn kém rồi mất bền
- [[public-debt-dynamics-depend-on-the-primary-balance-seigniorage-and-the-interest-growth-gap]] — phương trình động học nợ
- [[when-interest-exceeds-growth-a-permanent-primary-deficit-cannot-exceed-seigniorage]] — hai chế độ r > g và r < g
- [[stabilizing-the-debt-ratio-caps-the-deficit-at-debt-times-nominal-growth]] — mục tiêu ngân sách để ổn định nợ
- [[government-solvency-is-a-forward-looking-balance-sheet]] — ràng buộc liên thời gian, tài sản ròng
- [[fiscal-sustainability-indicators-measure-the-adjustment-needed]] — tài sản ròng, primary gap, tax gap
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
- [[subsidies]] — định nghĩa, bảy dạng, công khai và ngầm
- [[effective-subsidies-are-targeted-temporary-transparent-and-budget-financed]] — năm tiêu chí đánh giá trợ cấp
- [[public-investment-should-complement-rather-than-compete-with-markets]] — chi đầu tư
- [[social-safety-nets-trade-targeting-against-work-incentives]] — lưới an sinh
- [[quasi-fiscal-operations]] — hoạt động bán tài khoá của ngân hàng trung ương và ngân hàng công
- [[sequestering-expenditures-is-an-emergency-cut-that-distorts-allocation]] — phong toả chi
- [[public-expenditure-raises-supply-in-the-long-run-but-crowds-out-private-spending]] — tác động vĩ mô
- [[in-transition-economies-extra-spending-can-worsen-financing-through-inflation]] — vòng chi – lạm phát – thu

**Stub — khái niệm đã có tên, chờ nội dung**
- [[central-bank]] — cơ quan phát hành tiền cơ sở
- [[current-account-balance]] — cán cân vãng lai; chờ nội dung từ Ch.4
- [[macroeconomic-sectors]] — các khu vực vĩ mô và tương tác giữa chúng
- [[net-exports]] — xuất khẩu trừ nhập khẩu, tác động của ngoại thương lên tổng cầu
- [[reserve-money]] — tiền cơ sở, nền của khối tiền
- [[soft-budget-constraint]] — ràng buộc ngân sách doanh nghiệp lách được nhờ nhà nước, ngân hàng
