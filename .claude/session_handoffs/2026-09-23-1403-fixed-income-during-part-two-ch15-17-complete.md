# Session Handoff: Ingest Part Two — Cash Instruments (Chương 15–17, `fixed_income_during`)

- **Thời gian**: 2026-09-23 14:03 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest cụm tiếp theo của Part Two: Cash Instruments (Chương 15 — Lãi suất giao ngay & kỳ hạn, Chương 16 — Thị trường trái phiếu, Chương 17 — Trái phiếu lãi suất thả nổi) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% cụm Ch.15–17. Wiki đạt mốc **551 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 12 trang concept/declarative mới:
1. `turn-premium-reflects-year-end-balance-sheet-constraints-rather-than-policy-rate-expectations`: Phần bù chuyển năm phản ánh áp lực co cụm bảng cân đối kế toán quy định cuối kỳ thay vì kỳ vọng lãi suất chính sách.
2. `joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause`: Nghĩa vụ liên đới trong phát hành nợ công gây rủi ro đạo đức và bị Điều 125 TFEU cấm trong khu vực Euro.
3. `dutch-and-american-auctions-differentiate-dealer-bidding-incentives-through-the-winners-curse`: Đấu thầu sơ cấp kiểu Mỹ và Hà Lan phân hóa động lực đặt lệnh của đại lý qua tác động bẫy kẻ thắng cuộc.
4. `clean-and-dirty-bond-prices-separate-market-valuation-from-accrued-interest-settlement`: Giá sạch loại bỏ biến động răng cưa của lãi dồn tích để định giá thị trường, giá bẩn xác định dòng tiền thanh toán.
5. `yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates`: Lợi suất đáo hạn giả định cấu trúc kỳ hạn phẳng và tái đầu tư đồng nhất, làm sai lệch tỷ suất sinh lời thực tế.
6. `modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases`: Modified duration đo rủi ro tương đối theo tài sản quản lý (AUM), PVBP đo rủi ro tiền mặt tuyệt đối theo sổ giao dịch danh nghĩa.
7. `bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons`: Độ lồi nợ gốc đạt cực đại ở trung hạn rồi giảm ở kỳ hạn siêu dài do hiện giá suy giảm theo hàm mũ.
8. `bond-carry-measures-net-income-after-repo-financing-and-defines-forward-pricing`: Carry trái phiếu đo lường thu nhập ròng sau chi phí tài trợ repo và xác định mức giá kỳ hạn phi kinh doanh chênh lệch giá.
9. `floating-rate-notes-reset-to-par-at-coupon-dates-when-quoted-margin-equals-credit-spread`: Trái phiếu thả nổi tự động hồi quy về mệnh giá tại ngày chốt coupon khi biên độ chào bán bằng phần bù rủi ro tín dụng.
10. `rfr-compounded-in-arrears-notes-require-observation-lags-and-synthetic-term-rates-to-quote-accrued-interest`: Trái phiếu thả nổi RFR tính lãi kép sau kỳ sử dụng lãi suất trung gian và độ trễ quan sát để niêm yết lãi dồn tích.
11. `discount-margin-evaluates-frn-spreads-through-isolated-flat-resets-or-curve-asset-swaps`: Biên độ chiết khấu của FRN phân tách giữa phương pháp tính biệt lập giả định lãi suất phẳng và phương pháp hoán đổi tài sản theo đường cong.
12. `constant-maturity-floaters-fail-par-reset-due-to-coupon-and-discount-tenor-mismatch`: Trái phiếu thả nổi kỳ hạn cố định phá vỡ đặc tính hồi quy mệnh giá do lệch pha kỳ hạn coupon và chiết khấu.

### 6 trang cập nhật 2 chiều:
1. `fixed-income-instruments`: Bổ sung cầu nối với quy ước giá sạch/giá bẩn và cấu trúc CMT/CMS.
2. `yield-to-maturity-equates-present-value-of-cash-flows-to-asset-price`: Bổ sung liên kết đối chiếu khiếm khuyết giả định đường cong phẳng của YTM.
3. `general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing`: Bổ sung liên kết tới carry tài trợ repo và turn premium.
4. `overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume`: Bổ sung liên kết tới trái phiếu thả nổi và cấu trúc tính lãi kép sau kỳ của RFRs.
5. `competitive-dealer-inquiries-incur-information-leakage-and-winners-curse`: Bổ sung liên kết đối chiếu winner's curse giữa thị trường thứ cấp và đấu thầu kiểu Mỹ sơ cấp.
6. `central-bank-output-legitimacy-cannot-substitute-for-input-legitimacy-under-treaty-constraints`: Bổ sung liên kết tới Điều khoản cấm cứu trợ tài chính No-Bailout (Điều 125 TFEU) và nghĩa vụ liên đới.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/.claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **551 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.15–17.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Định giá Trái phiếu, Rủi ro Lãi suất & Công cụ Lãi suất Thả nổi (Fixed Income Düring — Ch.15–17 / Part Two)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:14-01-33]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Tiếp tục Part Two nguồn `fixed_income_during`**:
   - Cụm **Ch.18–20 (Thanh khoản thị trường tài sản, Mô hình đường cong & Phân tích đường cong)**: File `-19.md` (156 dòng), `-20.md` (342 dòng), `-21.md` (172 dòng).
   - Tiếp sau đó: Ch.21–22 (Carry/Roll-down và Curve Spreads, hoàn tất Part Two).
2. **Nguồn ngắn trọn gói**: Ingest toàn bộ tài liệu `Modern Money Mechanics` (85 KB / 721 dòng) trong 1 lượt chạy.
3. **Đóng gói nguồn**: Hoàn tất Ch.1 của `imf_macro_accounting`.
