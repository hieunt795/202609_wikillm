# Session Handoff: Ingest Part Two — Cash Instruments (Chương 13–14, `fixed_income_during`)

- **Thời gian**: 2026-09-23 13:48 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest cụm tiếp theo của Part Two: Cash Instruments (Chương 13 — Thị trường tiền tệ & Chương 14 — Thị trường Repo) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), áp dụng bộ quy tắc văn phong `writing-style` (bản local) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% cụm Ch.13–14. Wiki đạt mốc **539 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 8 trang concept mới:
1. `commercial-paper-and-short-term-instruments-compete-as-near-money`: Thương phiếu và các công cụ nợ ngắn hạn (CD, T-bills, BA) cạnh tranh trực tiếp với tiền gửi ngân hàng như tài sản tiền tệ gần (near-money).
2. `overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume`: Các chuẩn lãi suất phi rủi ro qua đêm (SOFR, €STR, SONIA, TONAR) thay thế các chỉ số IBOR dựa trên khảo sát nhờ khối lượng giao dịch thị trường thực tế khổng lồ.
3. `lagged-compounded-overnight-rates-lack-term-risk-premia-and-delay-policy-transmission`: Lãi suất qua đêm dồn lãi có độ trễ thiếu phần bù rủi ro kỳ hạn thực sự và gây ra độ trễ truyền dẫn đối với chính sách tiền tệ.
4. `futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows`: Khoản điều chỉnh lồi của hợp đồng tương lai ngắn hạn phát sinh từ tính bất đối xứng của luồng tiền ký quỹ biến đổi (VM) hàng ngày.
5. `general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing`: Phân định cấu trúc vi mô giữa repo tài sản chung GC (định hướng tiền mặt) và repo specials (định hướng mượn chứng khoán).
6. `repo-haircuts-manage-liquidation-volatility-but-generate-asymmetric-wrong-way-risk`: Tỷ lệ khấu trừ tài sản bảo đảm (haircut) quản trị biến động thanh lý nhưng tạo rủi ro sai chiều bất đối xứng cho bên cung cấp tài sản.
7. `collateral-rehypothecation-chains-amplify-cascading-settlement-delays-across-counterparties`: Chuỗi tái thế chấp tài sản bảo đảm khuếch đại tình trạng chậm trễ thanh toán dây chuyền giữa các đối tác.
8. `tri-party-repo-centralizes-collateral-administration-and-economizes-on-cash-transfers`: Repo ba bên tập trung hóa quản trị tài sản bảo đảm và tiết giảm chi phí luân chuyển tiền mặt.

### 3 trang cập nhật 2 chiều:
1. `repurchase-agreement`: Bổ sung phân loại GC vs Specials, tri-party repo và cầu nối với các tài sản tiền tệ gần.
2. `securities-lending-programmes-and-central-bank-collateral-swaps`: Bổ sung cơ chế hoán đổi nâng hạng tài sản thế chấp (collateral transformation/upgrades) và chương trình TSLF của Fed từ Ch.14.
3. `xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices`: Bổ sung cầu nối với khoản điều chỉnh lồi (convexity adjustment) phát sinh từ ký quỹ hợp đồng tương lai.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/.claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **539 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.13–14.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và bổ sung phân mục *Thị trường tiền tệ, Chuẩn lãi suất RFRs & Cấu trúc Repo (Fixed Income Düring — Ch.13–14 / Part Two)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:13-47-15]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Tiếp tục Part Two nguồn `fixed_income_during`**:
   - Cụm **Ch.15–17 (Lãi suất giao ngay & kỳ hạn, Thị trường trái phiếu & FRN)**: File `-16.md` (108 dòng), `-17.md` (487 dòng), `-18.md` (126 dòng).
   - Tiếp sau đó: Ch.18–22 (Thanh khoản thị trường tài sản, Mô hình đường cong lợi suất, Carry/Roll-down và Curve spreads).
2. **Nguồn ngắn trọn gói**: Ingest toàn bộ tài liệu `Modern Money Mechanics` (85 KB / 721 dòng) trong 1 lượt chạy.
3. **Đóng gói nguồn**: Hoàn tất Ch.1 của `imf_macro_accounting`.
