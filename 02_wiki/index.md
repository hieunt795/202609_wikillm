# Index

> Mục lục trang wiki theo chủ đề. Cập nhật mỗi khi có trang mới (xem `.claude/skills/ingest/SKILL.md` bước 6).

## Sources

Trạng thái ingest từng nguồn trong `01_sources/`. **Cập nhật mỗi lượt ingest**, kể cả lượt không tạo trang mới (`ingest/SKILL.md` bước 6). Bảng này chỉ tóm tắt ở cấp nguồn — tiến độ theo chunk của nguồn dài nằm trong `03_state/<tên_nguồn>.md` (`00_schema.md` §10), và đó mới là nguồn sự thật khi cần biết chi tiết "còn lại phần nào".

| Nguồn | Phân loại | Trạng thái | Phần còn lại | State file |
|---|---|---|---|---|
| `imf_macro_accounting` | Nguồn dài (829 KB / 6.065 dòng) | **Đang ingest dở** | Ch.1 (tổng quan chuyển đổi Ba Lan); Ch.3 cụm C–E (tài khoá: nợ công, phân tích thu, phân tích chi); Ch.4 (cán cân thanh toán); Ch.5 (tiền tệ); Ch.6 (flow of funds). Đã xong: Ch.2 toàn bộ 7 cụm; Ch.3 cụm A–B. Ch.3 bỏ qua phần bối cảnh Ba Lan và Exercises (§2) | `03_state/imf_macro_accounting.md` |
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

**Đại lượng sản lượng**
- [[value-added]] — giá trị thực sự tạo thêm, đơn vị nền của mọi phép đo sản lượng
- [[gdp]] — tổng value added theo nguyên tắc cư trú
- [[production-income-and-expenditure-approaches-yield-the-same-gdp]] — ba cách đo, một con số
- [[measured-gdp-covers-only-what-markets-price]] — GDP bỏ sót gì và vì sao

**Giá và sản lượng thực**
- [[real-gdp]] — sản lượng theo giá cố định
- [[gdp-deflator]] — chỉ số giá toàn nền kinh tế, so với CPI
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

**Chính sách giá và thu nhập**
- [[price-liberalization]] — lợi ích và điều kiện đi kèm
- [[price-convergence-keeps-pressure-on-inflation-through-the-transition]] — vì sao áp lực giá kéo dài
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
- [[polish-national-saving-fell-sharply-at-the-onset-of-transition]] — tiết kiệm rơi rồi hồi
- [[polish-price-liberalization-left-inflation-stuck-at-30-percent]] — thả giá và lạm phát nền
- [[polands-excess-wage-tax-popiwek-was-discontinued-after-five-years]] — kiểm soát lương trên thực tế
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
- [[seigniorage]] — nguồn thu từ phát hành tiền, tách thành phần thuần và thuế lạm phát
- [[inflation-tax-revenue-peaks-because-high-inflation-shrinks-its-base]] — đường chữ U ngược

**Stub — khái niệm đã có tên, chờ nội dung**
- [[central-bank]] — cơ quan phát hành tiền cơ sở
- [[cpi]] — chỉ số giá tiêu dùng, dạng Laspeyres
- [[crowding-out]] — vay của chính phủ ép chi tiêu tư nhân qua lãi suất
- [[exchange-rate]] — giá đồng tiền, neo danh nghĩa trong ổn định hoá
- [[hyperinflation]] — lạm phát tới mức tiền mất chức năng cất trữ
- [[indexation]] — tự điều chỉnh khoản danh nghĩa theo chỉ số giá
- [[reserve-money]] — tiền cơ sở, nền của khối tiền
- [[subsidies]] — chuyển nhượng cho người sản xuất, lệch các mức giá SNA
