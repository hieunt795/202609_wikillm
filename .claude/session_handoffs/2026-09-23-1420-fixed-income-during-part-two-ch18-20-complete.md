# Session Handoff: Ingest Part Two — Cash Instruments (Chương 18–20, `fixed_income_during`)

- **Thời gian**: 2026-09-23 14:20 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest cụm tiếp theo của Part Two: Cash Instruments (Chương 18 — Thị trường tài sản và thanh khoản, Chương 19 — Đường cong và mô hình đường cong, Chương 20 — Phân tích đường cong lợi suất) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% cụm Ch.18–20. Wiki đạt mốc **563 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 12 trang concept/declarative mới:
1. `microscopic-versus-macroscopic-market-liquidity-separates-trade-breadth-from-balance-sheet-depth`: Phân tầng thanh khoản vi mô (bề rộng giao dịch) và thanh khoản vĩ mô (chiều sâu bảng cân đối lưu kho rủi ro).
2. `clobs-and-otc-market-making-differentiate-search-costs-from-information-leakage`: Sổ lệnh tập trung (CLOBs) và tạo lập thị trường OTC đánh đổi giữa chi phí tìm kiếm đối tác và rò rỉ thông tin.
3. `spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias`: Độ phân tán sai số khớp đường cong spline đo lường gián tiếp sức chịu tải chênh lệch giá và sự thu hẹp bảng cân đối dealer.
4. `on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures`: Phần bù thanh khoản on-the-run suy giảm khi khám phá giá và phòng hộ tập trung vào hợp đồng tương lai.
5. `yield-curve-representations-bridge-discount-factors-zero-rates-and-par-yields`: Liên kết chuyển đổi toán học giữa bốn biểu diễn cấu trúc kỳ hạn: hệ số chiết khấu, lãi suất zero, forward rate và par curve.
6. `bootstrapping-and-reverse-bootstrapping-isolate-zero-rates-and-replicate-cash-flow-profiles`: Bóc tách bootstrapping trích xuất zero rates từ giá thị trường và reverse bootstrapping tái lập cấu trúc dòng tiền nghĩa vụ.
7. `parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness`: Mô hình spline tham số hóa đánh đổi giữa độ chính xác định giá lại trái phiếu và độ trơn nhẵn của đường cong lãi suất kỳ hạn.
8. `composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition`: Mô hình spline phức hợp phân tách đường cong chênh lệch để triệt tiêu hiện tượng giao cắt phi lý giữa đường cong cận quốc gia và chính phủ.
9. `dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches`: Khớp giá theo trọng số DV01 tối ưu hóa bình phương tối thiểu tuyến tính, tăng tốc độ giải nghiệm hàng trăm lần so với tìm kiếm lợi suất phi tuyến.
10. `parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments`: Dịch chuyển song song thống trị đường cong phản ánh điều chỉnh ước lượng lãi suất thực trung lập dài hạn và cam kết của NHTW.
11. `convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end`: Thiên lệch độ lồi tăng theo căn bậc hai của kỳ hạn, đè nén lợi suất kỳ hạn dài và gây đảo ngược cấu trúc kỳ hạn đoạn siêu dài.
12. `institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity`: Môi trường ưa thích của định chế và quy chế thanh khoản Solvency tạo trạng thái bán độ lồi cưỡng bức (short convexity).

### 4 trang cập nhật 2 chiều:
1. `fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities`: Bổ sung liên kết tới `on-the-run-liquidity-premium-diminishes-when-price-discovery-concentrates-in-bond-futures` và `composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition`.
2. `bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons`: Bổ sung liên kết tới `convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end`.
3. `modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases`: Bổ sung liên kết tới `dv01-weighted-price-fitting-accelerates-yield-curve-optimization-over-nonlinear-yield-searches`.
4. `financial-market-duration-repricing-executes-monetary-tightening-on-central-banks-behalf`: Bổ sung liên kết tới `parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments`.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/.claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **563 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.18–20.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Thanh khoản thị trường, Mô hình đường cong & Phân tích cấu trúc kỳ hạn (Fixed Income Düring — Ch.18–20 / Part Two)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:14-18-31]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Hoàn tất 100% Part Two nguồn `fixed_income_during`**:
   - Cụm **Ch.21–22 (Carry/Roll-down và Curve Spreads)**: File `-22.md` (40 dòng), `-23.md` (84 dòng) $\rightarrow$ Khối lượng gọn (124 dòng), kết thúc trọn vẹn toàn bộ Phần Hai: Công cụ tiền mặt (*Part Two — Cash Instruments*).
2. **Tiến sang Part Three**:
   - Ch.23: Trái phiếu liên kết lạm phát (*Part Three — Inflation-Linked Debt*, File `-24.md`, 362 dòng).
