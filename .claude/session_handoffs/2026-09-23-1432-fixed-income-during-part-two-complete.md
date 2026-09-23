# Session Handoff: Hoàn Tất 100% Part Two — Cash Instruments (Chương 21–22, `fixed_income_during`)

- **Thời gian**: 2026-09-23 14:32 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest cụm cuối cùng của Part Two: Cash Instruments (Chương 21 — Carry & Roll-Down, Chương 22 — Chênh lệch đường cong lợi suất) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% cụm Ch.21–22 và chính thức hoàn tất **100% Part Two — Cash Instruments (Chương 10–22)**. Wiki đạt mốc **570 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 7 trang concept/declarative mới:
1. `upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields`: Thứ bậc toán học giữa forward rate, zero rate và par yield trên đường cong dốc lên.
2. `holding-period-return-combines-carry-and-roll-down-quantified-by-break-even-yield-buffers`: Lợi suất nắm giữ tích hợp giữa carry tài trợ repo và roll-down trượt dốc, đo lường bằng đệm lợi suất hòa vốn.
3. `z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves`: Z-spread (spline spread) chiết khấu từng dòng tiền độc lập trên đường cong zero, tự động điều chỉnh theo rủi ro thời lượng.
4. `par-swap-spreads-reflect-benchmark-liquidity-and-exhibit-issuance-driven-jump-discontinuities`: Par swap spread phản ánh tính thanh khoản của trái phiếu chuẩn và bộc lộ các bước nhảy gián đoạn do phát hành mới.
5. `par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks`: Hoán đổi tài sản par-par và proceeds phân hóa giữa cam kết vốn trả trước và rủi ro tín dụng đối tác khi đáo hạn.
6. `interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision`: Chênh lệch hoán đổi nội suy (I-spread) đánh đổi giữa tính thanh khoản thực thi nhanh và độ trôi giá trị phòng hộ.
7. `ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve`: Chênh lệch TED lượng hóa rủi ro liên ngân hàng bằng phương pháp dịch chuyển trực tiếp toàn bộ đường cong chiết khấu.

### 4 trang cập nhật 2 chiều:
1. `bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing`: Bổ sung liên kết tới `holding-period-return-combines-carry-and-roll-down-quantified-by-break-even-yield-buffers`.
2. `yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields`: Bổ sung liên kết tới `upward-sloping-yield-curves-mandate-forward-rates-to-exceed-zero-rates-and-par-yields` và `z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves`.
3. `spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias`: Bổ sung liên kết đối chiếu với `z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves`.
4. `discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps`: Bổ sung liên kết tới `par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks` và `interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision`.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **570 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.21–22. Toàn bộ Part One (Ch.1–9) và Part Two (Ch.10–22) đã hoàn tất 100%.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Carry, Roll-Down & Chênh lệch đường cong lợi suất (Fixed Income Düring — Ch.21–22 / Part Two)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:14-30-50]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Commit & Push Git**: Lưu lại mốc hoàn tất trọn vẹn Part Two (Ch.10–22) và Ch.18–20 trước đó.
2. **Tiến sang Part Three — Inflation-Linked Debt**:
   - **Chương 23: Trái phiếu liên kết lạm phát** (*Inflation-Indexed Bonds*, File `-24.md`, 362 dòng): Khung phân tích lạm phát thực/danh nghĩa, cơ chế bảo vệ nợ gốc/coupon, breakeven inflation rate và seasonal adjustments.
