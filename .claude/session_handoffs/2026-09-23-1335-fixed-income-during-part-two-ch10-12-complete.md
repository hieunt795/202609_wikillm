# Session Handoff: Ingest Part Two — Cash Instruments (Chương 10–12, `fixed_income_during`)

- **Thời gian**: 2026-09-23 13:35 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest cụm mở đầu Part Two: Cash Instruments (Chương 10–12) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% cụm Ch.10–12. Wiki đạt mốc **531 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 9 trang concept mới:
1. `book-entry-securities-centralize-ownership-via-global-notes-and-csds`: Cơ chế chứng khoán ghi sổ tập trung hóa sở hữu qua chứng chỉ nợ tổng (global note) và mạng lưới CSD/ICSD (Euroclear, Clearstream).
2. `schuldschein-avoids-mark-to-market-accounting-through-transfer-restrictions`: Hợp đồng vay Schuldschein của Đức cho phép né tránh hạch toán giá thị trường nhờ giới hạn số lần chuyển nhượng.
3. `fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities`: Khám phá giá phân tầng truyền dẫn từ các tài sản chuẩn thanh khoản cao nhất sang các chứng khoán kém thanh khoản.
4. `competitive-dealer-inquiries-incur-information-leakage-and-winners-curse`: Rủi ro rò rỉ thông tin dòng lệnh và lời nguyền người thắng cuộc khi hỏi giá cạnh tranh nhiều đại lý.
5. `delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles`: Cơ chế DvP triệt tiêu rủi ro thanh toán Herstatt thông qua các chu kỳ đối trừ định kỳ của định chế trung gian.
6. `securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins`: Kỷ luật đối với thất bại giao chứng khoán qua phí phạt và các phương thức khắc phục (repo, buy-in).
7. `central-counterparties-transform-bilateral-counterparty-risk-into-liquidity-and-concentration-risk`: CCP chuyển hóa rủi ro tín dụng đối tác song phương thành rủi ro thanh khoản và rủi ro sụp đổ tập trung.
8. `ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding`: Thác bảo vệ của CCP ngăn ngừa mất khả năng thanh toán qua ký quỹ VM/IM, quỹ vỡ nợ tương hỗ và nghĩa vụ bỏ thầu bắt buộc.
9. `xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices`: Hệ điều chỉnh định giá xVA (CVA, FVA, DVA) lượng hóa chi phí vốn và thanh khoản giữa phái sinh song phương và chuẩn bù trừ CCP.

### 2 trang cập nhật 2 chiều:
1. `securities-differ-from-bilateral-contracts-by-transferability-without-counterparty-consent`: Bổ sung phân loại chứng khoán vô danh, ghi danh, ghi sổ và công cụ lai Schuldschein từ Ch.10.
2. `multilateral-netting-minimizes-interbank-settlement-flows-and-credit-exposures`: Mở rộng từ bù trừ liên ngân hàng sang cơ chế give-up của CCP và các chu kỳ thanh toán bù trừ DvP.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/.claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **531 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.10–12.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Công cụ tiền mặt, Cấu trúc vi mô & Bù trừ trung tâm (Fixed Income Düring — Ch.10–12 / Part Two)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:13-33-43]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Tiếp tục Part Two nguồn `fixed_income_during`**:
   - Cụm **Ch.13–14 (Thị trường tiền tệ & Thị trường Repo)**: File `-14.md` (279 dòng) và `-15.md` (64 dòng).
   - Tiếp sau đó: Ch.15–17 (Lãi suất giao ngay/kỳ hạn, Thị trường trái phiếu & FRN).
2. **Nguồn ngắn**: Ingest `Modern Money Mechanics` (85 KB / 721 dòng) trong 1 lượt chạy.
3. **Đóng gói nguồn**: Hoàn tất Ch.1 của `imf_macro_accounting`.
