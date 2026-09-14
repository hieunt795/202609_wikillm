# Index

> Mục lục trang wiki theo chủ đề. Cập nhật mỗi lần ingest tạo trang mới (xem `agents.md` §Ingest).

## Sources

Trạng thái ingest từng nguồn trong `01_sources/`. **Cập nhật mỗi lượt ingest**, kể cả lượt không tạo trang mới (`ingest/SKILL.md` bước 6). Bảng này chỉ tóm tắt ở cấp nguồn — tiến độ theo chunk của nguồn dài nằm trong `03_state/<tên_nguồn>.md` (`00_schema.md` §10), và đó mới là nguồn sự thật khi cần biết chi tiết "còn lại phần nào".

| Nguồn | Phân loại | Trạng thái | Phần còn lại | State file |
|---|---|---|---|---|
| `imf_macro_accounting` | Nguồn dài (829 KB / 6.065 dòng) | **Đang ingest dở** | Phần **lý luận** của Ch.3 (tài khoá), Ch.4 (cán cân thanh toán), Ch.5 (tiền tệ + phụ lục IMF), Ch.6 (flow of funds) — ~2.150 dòng. Bối cảnh Ba Lan và Exercises của các chương này cố ý bỏ qua (§2). Đã xong Ch.1 và toàn bộ 7 cụm A–G của Ch.2 | `03_state/imf_macro_accounting.md` |
| `Modern Money Mechanics` | Nguồn ngắn (83 KB / 721 dòng) | **Chưa ingest** | Toàn bộ — dưới ngưỡng nguồn dài nên ingest trọn 1 lượt, không cần file trạng thái (§10) | — |

## Trang wiki theo chủ đề

**Khung hạch toán**
- [[system-of-national-accounts-sna]] — khung kế toán quốc tế, hub của toàn bộ chuỗi đại lượng
- [[sna-sequence-of-accounts]] — sáu tài khoản nối nhau qua balancing item
- [[institutional-sectors-in-the-sna]] — năm khu vực thể chế cộng phần còn lại của thế giới
- [[sna-records-transactions-on-an-accrual-basis-with-double-entry]] — quy ước ghi nhận
- [[residency-in-the-sna-follows-the-centre-of-economic-interest]] — ai là đơn vị cư trú
- [[valuation-in-the-sna]] — giá cơ bản, giá người sản xuất, giá người mua
- [[the-1993-sna-added-balance-sheets-and-fuller-income-accounts]] — khác biệt so với bản 1968
- [[mps-material-product-system]] — khung hạch toán của kinh tế kế hoạch

**Khung hạch toán tài khoá**
- [[government-finance-statistics-gfs]] — khung kế toán cho riêng khu vực chính phủ, hub của chuỗi tài khoá
- [[general-government]] — ranh giới khu vực chính phủ, và vì sao chức năng tiền tệ bị loại ra
- [[gfs-records-on-a-cash-basis-so-arrears-split-the-cash-deficit-from-the-accrual-deficit]] — lệch quy ước với SNA và cái giá của nó
- [[a-receipt-is-revenue-only-if-it-creates-no-repayment-obligation]] — phép thử giữ cho con số thâm hụt có nghĩa
- [[tax-revenue]] — bắt buộc và không đối ứng, hai vế làm việc cùng nhau
- [[grants-sit-above-the-line-in-gfs-but-belong-below-it-in-analysis]] — quy ước thống kê lệch cách đọc phân tích
- [[government-net-lending-is-grouped-with-expenditure-because-its-motive-is-policy-not-liquidity]] — bất đối xứng động cơ
- [[conventional-fiscal-deficit]] — balancing item của khung, và ba khoảng mù của nó
- [[extrabudgetary-operations-and-counterpart-funds-distort-the-measured-fiscal-position]] — khoảng mù phạm vi
- [[cash-based-gfs-hides-a-bank-recapitalization-until-the-interest-falls-due]] — khoảng mù thời điểm
- [[privatization-receipts-cut-the-deficit-once-and-raise-it-later-unless-the-proceeds-buy-assets]] — khoảng mù tính một lần

**Cân đối, thước đo và tài trợ thâm hụt**
- [[the-government-saving-investment-gap-equals-the-overall-fiscal-balance]] — ràng buộc ngân sách của khu vực chính phủ
- [[the-fiscal-deficit-measure-must-be-chosen-to-fit-the-question-asked]] — bốn yếu tố quyết định chọn thước đo nào
- [[public-sector-borrowing-requirement]] — phạm vi rộng nhất, đóng khoảng mù bao phủ
- [[government-saving-measured-as-the-current-fiscal-deficit-rests-on-an-arbitrary-capital-split]] — vì sao thâm hụt vãng lai yếu
- [[primary-fiscal-deficit]] — tách phần chính sách đang chủ động làm khỏi di sản
- [[operational-fiscal-deficit]] — khi lạm phát biến một phần trả lãi thành trả gốc
- [[each-way-of-financing-a-deficit-carries-its-own-macroeconomic-imbalance]] — bốn đường, bốn mất cân đối (hub)
- [[borrowing-from-commercial-banks-is-monetary-only-if-the-central-bank-accommodates]] — cùng giao dịch, hai kết quả trái ngược
- [[nonbank-borrowing-postpones-inflation-rather-than-avoiding-it]] — ngưỡng lãi suất thực vượt tăng trưởng
- [[external-financing-appreciates-the-exchange-rate-before-it-runs-out]] — êm ở đầu, gãy ở cuối
- [[payments-arrears-are-a-coercive-form-of-deficit-financing]] — đường thứ năm, không cần ai đồng ý
- [[expenditure-arrears-raise-the-cost-of-providing-government-services]] — vì sao khoản tiết kiệm từ việc không trả là vay lãi cao
- [[seigniorage]] — nguồn thu từ in tiền, và đường cong chữ U ngược
- [[the-inflation-tax-costs-the-public-more-than-it-raises-for-the-government]] — cơ sở thuế tự bào mòn

**Nợ công và tính bền vững tài khoá**
- [[debt-neutrality]] — giả thuyết vay nợ là thuế hoãn lại, và phán quyết thực nghiệm
- [[fiscal-policy-is-unsustainable-when-the-debt-to-gdp-ratio-rises-persistently]] — vì sao nợ cao vừa tốn kém vừa không trụ được
- [[solvency-is-a-weaker-requirement-than-stabilizing-the-debt-ratio]] — điều kiện cần, không đủ
- [[the-debt-ratio-has-built-in-momentum-set-by-the-interest-growth-gap]] — phương trình động lực nợ
- [[when-interest-exceeds-growth-a-permanent-primary-deficit-is-impossible]] — hệ quả số học khi r > g
- [[growing-out-of-debt-works-until-borrowing-pushes-interest-above-growth]] — và vì sao r < g tự huỷ nếu khai thác quá đà
- [[the-budget-identity-needs-net-debt-not-gross-debt]] — khối tồn ròng khớp với luồng ròng
- [[government-solvency-is-a-forward-looking-balance-sheet]] — tài sản gồm cả hiện giá thu tương lai
- [[three-indicators-turn-sustainability-into-a-required-adjustment]] — giá trị ròng dương, khoảng trống sơ cấp, khoảng trống thuế

**Phân tích thu**
- [[ad-hoc-tax-increases-produce-distortionary-systems-that-still-underyield]] — vì sao chắp vá thua ở cả hai vế
- [[tax-elasticity]] — tính linh hoạt tự có của hệ thống thuế
- [[buoyancy-exceeds-elasticity-when-discretionary-changes-raise-revenue]] — khoảng cách hai chỉ số mới là thông tin
- [[tax-effort-must-be-judged-against-taxable-capacity-not-gdp]] — cái bẫy của tỷ lệ thu trên GDP
- [[tax-effort-analysis]] — năng lực chịu thuế và ba yếu tố quyết định nó
- [[the-tanzi-diagnostic-test-scores-revenue-productivity-on-eight-questions]] — tám câu hỏi về thiết kế

**Phân tích chi**
- [[a-sound-public-expenditure-framework-rests-on-five-elements]] — năm cấu phần, trong đó thiết chế ngân sách hay bị quên
- [[public-spending-poses-a-level-an-efficiency-and-a-mix-problem]] — hai câu hỏi thực chứng, một câu chuẩn tắc
- [[civil-service-pay-and-headcount-are-two-separate-levers-on-the-wage-bill]] — trả quá thấp cho quá nhiều người
- [[building-new-capacity-while-maintenance-lapses-can-make-net-investment-negative]] — cắt băng khánh thành trong khi vốn teo lại
- [[public-investment-raises-private-returns-but-mostly-in-the-long-run]] — chèn lấn ngay, năng suất về sau
- [[spending-more-when-financing-capacity-is-limited-can-shrink-real-revenue]] — khoản chi thêm ăn vào nguồn thu nuôi nó
- [[subsidies]] — bảy hình thức, chỉ một hình thức trông giống khoản chi
- [[implicit-subsidies-keep-their-own-cost-out-of-the-budget]] — méo nằm ở chính sách giá, không ở kế toán
- [[judging-a-subsidy-takes-five-checks-not-just-its-budget-cost]] — hiệu lực, thời hạn, minh bạch, tài trợ, khả thi
- [[social-safety-nets]] — ba cấu phần, dựng thay phần trách nhiệm xã hội mà doanh nghiệp công bỏ lại
- [[social-safety-net-design-trades-targeting-against-incentives]] — cắt giảm dần là một sắc thuế biên ẩn
- [[quasi-fiscal-operations]] — hoạt động tài khoá trú ẩn trong tài khoản ngân hàng trung ương
- [[a-low-spending-to-gdp-ratio-can-mean-weak-financing-capacity-not-a-small-state]] — tỷ lệ đo kết quả, không đo ý định
- [[sequestering-spending-is-an-emergency-step-that-costs-allocation-quality]] — giữ được mức, hy sinh hiệu quả và cơ cấu

**Đại lượng sản lượng**
- [[value-added]] — giá trị thực sự tạo thêm, đơn vị nền của mọi phép đo sản lượng
- [[gdp]] — tổng value added theo nguyên tắc cư trú
- [[production-income-and-expenditure-approaches-yield-the-same-gdp]] — ba cách đo, một con số
- [[measured-gdp-covers-only-what-markets-price]] — GDP bỏ sót gì và vì sao

**Giá và sản lượng thực**
- [[real-gdp]] — sản lượng theo giá cố định
- [[gdp-deflator]] — chỉ số giá toàn nền kinh tế, so với CPI
- [[cpi]] — thước đo lạm phát phổ biến nhất, và hai giới hạn của nó
- [[laspeyres-and-paasche-indexes-bracket-true-inflation]] — quyền số cố định và quyền số hiện hành lệch hai phía

**Lạm phát**
- [[inflation]] — tăng giá chung kéo dài, phân biệt với giá tương đối
- [[types-of-inflation]] — do chính sách, chi phí đẩy, cầu kéo, quán tính
- [[core-inflation-strips-out-one-time-price-level-jumps]] — tốc độ nền so với con số đo được
- [[a-one-time-price-shock-becomes-inflation-only-if-monetary-policy-accommodates-it]] — điều kiện tiền tệ
- [[inertial-inflation-persists-because-it-is-written-into-contracts]] — vì sao quán tính tự duy trì

**Đại lượng thu nhập và sử dụng**
- [[gni]] — thu nhập người cư trú kiếm được
- [[gndi]] — thu nhập khả dụng để tiêu hoặc để dành
- [[absorption]] — tổng cầu nội địa (C + I)
- [[gross-national-saving]] — phần dư sau tiêu dùng
- [[final-consumption]] — ranh giới với tiêu dùng trung gian nằm ở mục đích sử dụng
- [[gross-investment]] — bổ sung vốn vật chất, không phải mua tài sản tài chính
- [[depreciation]] — đại lượng tách mọi cặp gộp/ròng
- [[leakages-equal-injections-in-the-circular-flow]] — hình ảnh trực quan dưới các đồng nhất thức

**Đồng nhất thức đối ngoại**
- [[current-account-deficit-means-absorption-exceeds-national-income]] — GNDI − A = CAB
- [[the-saving-investment-gap-equals-the-current-account-balance]] — S − I = CAB
- [[the-private-sector-resource-gap-must-be-financed-by-other-sectors]] — ràng buộc ngân sách ở cấp khu vực
- [[current-account-balance]] — cùng một con số đọc được từ ba phía

**Lao động và tiền lương**
- [[unemployment-rate]] — cách đo và các sai lệch của nó
- [[types-of-unemployment]] — thời vụ, ma sát, chu kỳ, cơ cấu, trá hình
- [[nairu]] — mức thất nghiệp tương thích với lạm phát ổn định
- [[real-wages]] — sức mua của lương, phân biệt với thu nhập thực
- [[real-wage-growth-is-bounded-by-productivity-growth]] — trần dài hạn của tăng lương

**Ổn định hoá vĩ mô**
- [[heterodox-stabilization]] — kỷ luật tài khoá + neo tỷ giá + chính sách thu nhập
- [[exchange-rate-anchor]] — neo danh nghĩa để chặn kỳ vọng, và năm bài học đi kèm
- [[dollarization]] — thước đo lòng tin vào nội tệ, đọc được cả hai chiều
- [[price-liberalization-needs-trade-opening-to-supply-the-missing-competition]] — vì sao hai việc phải đi cùng nhau

**Chính sách giá và thu nhập**
- [[price-liberalization]] — lợi ích và điều kiện đi kèm
- [[price-convergence-keeps-pressure-on-inflation-through-the-transition]] — vì sao áp lực giá kéo dài
- [[incomes-policy]] — ba cách tiếp cận và lý do dùng
- [[designing-wage-controls-means-choosing-a-norm-indexation-coverage-and-enforcement]] — bốn bước thiết kế
- [[wage-controls-lose-effectiveness-rapidly-after-a-short-period]] — vì sao chỉ nên tạm thời

**Đo lường trong kinh tế chuyển đổi**
- [[transition-statistics-understate-private-sector-growth]] — sai lệch ở khâu bao phủ
- [[a-real-output-index-needs-prices-that-reflect-relative-scarcity]] — sai lệch ở khâu định giá

**Case: Ba Lan trước cải cách**
- [[polands-partial-reforms-of-the-1980s-failed-because-they-created-no-real-markets]] — vì sao phân quyền nửa vời thất bại
- [[central-planning-left-six-structural-distortions-in-the-polish-economy]] — điểm xuất phát của cải cách
- [[polands-slide-toward-hyperinflation-in-1989-followed-the-loss-of-financial-control]] — 9% lên 55% một tháng trong 1989

**Case: Ba Lan 1989–1994**
- [[polands-output-collapse-1990-91-came-from-three-distinct-causes]] — vĩ mô, thể chế, đo lường
- [[to-what-extent-was-polands-output-decline-1990-91-overstated]] — câu hỏi còn để ngỏ
- [[polands-recovery-from-1992-was-led-by-consumption-then-exports]] — phục hồi 1992–94
- [[polish-national-saving-fell-sharply-at-the-onset-of-transition]] — tiết kiệm rơi rồi hồi
- [[polish-price-liberalization-left-inflation-stuck-at-30-percent]] — thả giá và lạm phát nền
- [[polands-excess-wage-tax-popiwek-was-discontinued-after-five-years]] — kiểm soát lương trên thực tế
- [[polish-unemployment-rose-from-near-zero-to-16-percent-in-four-years]] — từ thất nghiệp trá hình sang công khai
- [[polands-january-1990-package-combined-five-mutually-reinforcing-policies]] — gói ổn định hoá, năm chính sách
- [[polands-fiscal-deficit-swung-to-surplus-in-1990-then-slipped-back]] — điều chỉnh tài khoá và giới hạn của nó
- [[rising-money-demand-let-poland-cut-inflation-despite-monetized-deficits]] — vì sao tài trợ bằng tiền vẫn giảm được lạm phát
- [[polands-trade-liberalization-was-reversed-in-1991-then-resumed-by-negotiation]] — mở, đóng, rồi mở bằng đàm phán
