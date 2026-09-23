# Session Handoff: Hoàn Tất 100% Part Three — Inflation-Linked Debt (Chương 23, `fixed_income_during`)

- **Thời gian**: 2026-09-23 14:42 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest toàn bộ Part Three: Inflation-Linked Debt (Chương 23 — Trái phiếu liên kết lạm phát) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% Chương 23 và chính thức hoàn tất **100% Part Three — Inflation-Linked Debt**. Wiki đạt mốc **577 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 7 trang concept/declarative mới:
1. `capital-indexed-tips-structure-operates-as-a-synthetic-foreign-currency-investment`: Cấu trúc nợ liên kết lạm phát TIPS bảo toàn sức mua thực tế, vận hành tương đương khoản đầu tư ngoại tệ tổng hợp.
2. `sovereign-inflation-linked-issuance-hedges-tax-creep-and-extracts-the-inflation-risk-premium`: Phát hành nợ liên kết lạm phát phòng hộ hiện tượng trượt thuế (tax creep) và khai thác phần bù rủi ro lạm phát.
3. `cpi-rebasing-and-ex-tobacco-conventions-prevent-index-distortions-in-inflation-linked-debt`: Kỹ thuật nối chuỗi đổi năm cơ sở và quy ước loại trừ thuốc lá bảo vệ tính liên tục và thanh khoản của nợ liên kết lạm phát.
4. `inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering`: Tính mùa vụ của chỉ số CPI bắt buộc giá sạch hấp thụ biến động, gây méo mó lạm phát hòa vốn nếu thiếu lọc chu kỳ.
5. `breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise`: Lạm phát hòa vốn thị trường phản ánh sự lây nhiễm từ biến động giá năng lượng và hoạt động phòng hộ của bàn giao dịch.
6. `real-short-rates-and-inflation-forecasts-determine-the-arbitrage-free-carry-of-inflation-linked-bonds`: Chi phí mang của trái phiếu liên kết lạm phát phụ thuộc vào lãi suất ngắn hạn thực và dự báo lạm phát kỳ hạn.
7. `comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves`: Mô hình định giá toàn diện xếp chồng động học lạm phát thực lên đường cong danh nghĩa, triệt tiêu sai số mùa vụ.

### 5 trang cập nhật 2 chiều:
1. `expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads`: Bổ sung liên kết tới `breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise` và `inflation-seasonality-distorts-clean-prices-and-breakeven-rates-absent-cyclical-filtering`.
2. `composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition`: Bổ sung liên kết tới `comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves`.
3. `z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves`: Bổ sung liên kết tới `capital-indexed-tips-structure-operates-as-a-synthetic-foreign-currency-investment` và `comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves`.
4. `bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing`: Bổ sung liên kết tới `real-short-rates-and-inflation-forecasts-determine-the-arbitrage-free-carry-of-inflation-linked-bonds`.
5. `cpi`: Bổ sung liên kết tới `cpi-rebasing-and-ex-tobacco-conventions-prevent-index-distortions-in-inflation-linked-debt`.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **577 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.23. Toàn bộ Part One (Ch.1–9), Part Two (Ch.10–22) và Part Three (Ch.23) đã hoàn tất 100%.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Trái phiếu liên kết lạm phát, Định giá TIPS & Động học lạm phát (Fixed Income Düring — Ch.23 / Part Three)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:14-40-07]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Commit & Push Git**: Lưu lại mốc hoàn tất trọn vẹn Part Three (Chương 23).
2. **Tiến sang Part Four — Defaultable Claims (Chương 24–27)**:
   - Giai đoạn 1: **Chương 24 (Credit Risk)** — File `-25.md` (272 dòng): Rủi ro vỡ nợ, tỷ lệ thu hồi (recovery rate), credit spreads, mô hình cấu trúc Merton và mô hình dạng rút gọn (reduced-form models).
   - Giai đoạn 2: **Chương 25–27 (Covered Bonds, ABS & RMBS)** — File `-26.md` (173 dòng), `-27.md` (56 dòng), `-28.md` (124 dòng): Cấu trúc tài sản bảo đảm kép (dual recourse), chứng khoán hóa và rủi ro trả nợ trước hạn (prepayment risk).
