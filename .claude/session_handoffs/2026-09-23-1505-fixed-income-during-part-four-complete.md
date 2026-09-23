# Session Handoff: Hoàn Tất 100% Part Four — Defaultable Claims (Chương 24–27, `fixed_income_during`)

- **Thời gian**: 2026-09-23 15:05 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest toàn bộ Part Four: Defaultable Claims (Chương 24–27: Credit Risk, Covered Bonds, Asset-Backed Securities, Residential Mortgage-Backed Securities) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (thân bài phẳng hoàn toàn, không heading, câu < 60 từ, chủ ngữ kinh tế rõ ràng, trích dẫn chuẩn vị trí) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% Chương 24, 25, 26, 27 và chính thức hoàn tất **100% Part Four — Defaultable Claims**. Wiki đạt mốc **592 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên (Cụm Ch.25–27)

### 8 trang concept/declarative mới:
1. `covered-bonds-combine-on-balance-sheet-dual-recourse-with-insolvency-ring-fencing`: Trái phiếu có bảo đảm tối ưu hóa chi phí vốn của ngân hàng qua cơ chế hoàn trả kép (dual recourse nội bảng) và khoanh vùng phá sản (insolvency ring-fencing), loại trừ khỏi thủ tục thanh lý tư pháp thông thường và miễn trừ gia tốc nợ (no acceleration); phân biệt trái phiếu luật định (statutory) và cấu trúc (structured).
2. `overcollateralization-optimizes-covered-bond-spreads-against-unsecured-asset-encumbrance`: Tài sản bảo đảm vượt mức (OC) là biến số tối ưu hóa giữa biên độ phát hành covered bond và chi phí đắt đỏ phát sinh từ trói buộc tài sản (asset encumbrance) đối với nợ không bảo đảm và tiền gửi; phân tích cơ chế thay thế tài sản xấu liên tục (asset replenishment) và tác động của thời điểm vỡ nợ ngân hàng.
3. `danish-balance-principle-links-mortgage-origination-to-bond-pricing-through-delivery-and-prepayment-options`: Thị trường thế chấp Đan Mạch khớp nối 1-1 khoản vay và trái phiếu hoàn vốn theo nguyên tắc cân bằng (balance principle); người vay quản trị nợ tối ưu hai chiều qua quyền giao nộp (delivery option mua trái phiếu dưới mệnh giá nộp lại để xóa nợ khi lãi suất tăng) và quyền trả trước (prepayment option khi lãi suất giảm); phân tích sản phẩm Flexlån.
4. `asset-backed-securitization-achieves-bankruptcy-remoteness-via-true-sale-and-non-recourse-spvs`: Chứng khoán hóa ABS tái tài trợ ngoại bảng qua chuyển nhượng dứt điểm (true sale) sang SPV phi truy đòi (non-recourse), đạt tính cách ly phá sản (bankruptcy-remoteness); phân tích động lực chênh lệch quy chế vốn Basel I, rủi ro tín dụng của bên thu hộ (servicer), bên cung cấp swap/GIC, và chuẩn mực STS của EU.
5. `tranching-mechanics-partition-collateral-losses-into-equity-mezzanine-and-senior-option-profiles`: Kỹ thuật phân tầng rủi ro và thác thanh toán trong ABS phân bổ tổn thất thành các hồ sơ quyền chọn chuyên biệt: equity tranche (long call), mezzanine tranche (short straddle), senior tranche (far out-of-the-money short put); kiểm soát thời lượng qua chứng chỉ khấu hao theo kế hoạch (PACs).
6. `mortgage-prepayments-combine-demographic-attrition-economic-refinancing-and-burn-out-effects`: Động học trả nợ trước hạn trong RMBS tích hợp hao mòn nhân khẩu (attrition phi kinh tế tạo mức sàn $b_k$), tái tài trợ kinh tế khi lãi suất giảm, hiện tượng kiệt quệ hoàn trả (burn-out effect), hiệu ứng báo chí truyền thông, và các rào cản phi kinh tế không hoàn trả (FICO, LTV) tạo nên hàm bão hòa logistic; chuẩn hóa qua SMM và CPR.
7. `rmbs-negative-convexity-arises-from-embedded-borrower-prepayment-options-and-wal-extension`: Mối quan hệ giá - lợi suất dị thường của RMBS bắt nguồn từ quyền chọn trả trước nhúng sẵn; việc giảm tốc độ tất toán khi lãi suất tăng làm kéo dài thời gian đáo hạn (WAL extension) và duy trì coupon cao, khiến giá ban đầu tăng theo lợi suất, tạo ra thời lượng âm và độ lồi âm; buộc các nhà quản lý danh mục phải liên tục phòng hộ động (dynamic hedging) trên thị trường Treasury on-the-run.
8. `tba-market-mechanics-and-dollar-rolls-manage-mortgage-origination-uncertainty`: Thị trường giao dịch chuyển tiếp TBA cho phép giao dịch kỳ hạn thanh khoản cao đối với conforming mortgages trước khi ấn định danh mục; xử lý bất định và thiếu hụt sản lượng khởi tạo qua nghiệp vụ dollar roll (bù hoãn mua / backwardation) và hoán đổi coupon (coupon swaps) để cân bằng bảng cân đối của các đại lý tạo lập thị trường.

### 5 trang cập nhật 2 chiều:
1. `statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors`: Bổ sung liên kết tới `covered-bonds-combine-on-balance-sheet-dual-recourse-...` và `overcollateralization-optimizes-covered-bond-spreads-...`.
2. `debt-acceleration-and-cross-default-clauses-prevent-time-subordination-in-multi-creditor-structures`: Bổ sung liên kết tới `tranching-mechanics-partition-collateral-losses-...` và `covered-bonds-combine-on-balance-sheet-dual-recourse-...`.
3. `bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons`: Bổ sung liên kết tới `rmbs-negative-convexity-arises-from-embedded-borrower-prepayment-options-and-wal-extension`.
4. `institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity`: Bổ sung liên kết tới `rmbs-negative-convexity-arises-from-embedded-borrower-prepayment-options-and-wal-extension`.
5. `market-impact-of-collateral-framework-and-leverage-constraints`: Bổ sung liên kết tới `asset-backed-securitization-achieves-bankruptcy-remoteness-via-true-sale-and-non-recourse-spvs`.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **592 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.24, Ch.25, Ch.26, Ch.27. Toàn bộ Part One (Ch.1–9), Part Two (Ch.10–22), Part Three (Ch.23) và Part Four (Ch.24–27) đã hoàn tất 100%.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Trái phiếu có bảo đảm, Chứng khoán hóa ABS & Thế chấp nhà ở RMBS (Fixed Income Düring — Ch.25–27 / Part Four)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:15-02-15]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Commit & Push Git**: Lưu lại mốc hoàn tất trọn vẹn **Part Four — Defaultable Claims** (Chương 24–27).
2. **Tiến sang Part Five — Derivatives (Chương 28–29)**:
   - **Chương 28: Bond Futures** — File `-29.md` (501 dòng): Hợp đồng tương lai trái phiếu chính phủ, hệ số chuyển đổi (conversion factor), trái phiếu rẻ nhất để giao hàng (cheapest-to-deliver - CTD), định giá cơ sở (basis trading) và quyền chọn giao hàng ngầm định (delivery options).
   - **Chương 29: Swaps** — File `-30.md` (89 dòng): Hợp đồng hoán đổi lãi suất, định giá par swap rates, và cấu trúc đường cong OIS/SOFR.
