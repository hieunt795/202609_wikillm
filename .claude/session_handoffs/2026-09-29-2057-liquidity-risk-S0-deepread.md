# Session Handoff: Liquidity Risk S0 Deep Read

**Date:** 2026-09-29 20:57  
**Status:** S0 Deep read complete; proposals drafted; ready for wiki write  
**Next:** Write S0 claims → validate → continue S1/S2/...

---

## Kết quả S0 Deep Read

**Trang:** 23/24 core liquidity concepts  
**Proposals duyệt:** 3 claims (C1–C3) + 2 link groups (L1–L2)  
**Status:** Tất cả `draft` → `draft` + `last_updated` (không nâng `stable`)

---

## Cách ghi từng trang

### **1. `liquidity-premium.md` — Thêm C1 + L1–L2**

**Edit thêm vào cuối đoạn 2 (sau chữ "d.3684"):**

```
Quản trị kỳ hạn và phần bù thanh khoản là cơ sở để ngân hàng xác định [[term-structure-of-interest-rate|cấu trúc kỳ hạn]] và tuân thủ nguyên tắc [[no-arbitrage-principle-enforces-consistency-across-forward-rates-and-spot-yields|không-arbitrage]] khi định giá các công cụ với kỳ hạn khác nhau.
```

**Update `last_updated`:** `2026-09-29`

---

### **2. `yield-curve.md` — Thêm C2 + chèn L1 vào paragraph 6 (Cargill part)**

**Edit thêm vào cuối đoạn 6 (sau chữ "d.2109–2110"):**

```
Đặc biệt, [[liquidity-premium-hypothesis-explains-the-prevalence-of-upward-sloping-yield-curves|giả thuyết phần bù thanh khoản]] giải thích tại sao đường cong dốc lên thường xuyên, và ngược lại, [[pure-expectations-hypothesis-equates-long-term-rates-to-the-average-of-expected-short-rates|giả thuyết kỳ vọng thuần túy]] tập trung vào lạm phát kỳ vọng. Một tín hiệu quan trọng khác là đường cong dốc xuống (inverted yield curve) — khi lợi suất dài hạn thấp hơn ngắn hạn — thường xuất hiện trước 6–12 tháng của một cuộc suy thoái kinh tế (vd Fed taper tantrum 2013, COVID-19 inversion 2020), làm cho nó trở thành leading indicator mạnh mẽ cho các cơ quan chính sách và nhà đầu tư quản lý danh mục.
```

**Update `last_updated`:** `2026-09-29`

---

### **3. `fixed-income-liquidity-search-costs-and-bid-ask-bounce-volatility.md` — Thêm C3**

File này rất mỏng (draft). Thêm vào sau định nghĩa hiện tại:

```
Các chi phí tìm kiếm thanh khoản (liquidity search costs) bao gồm ba thành phần: (1) **bid-ask bounce** — hiện tượng giá dao động lên-xuống trong cùng một phiên giao dịch do nhà cung cấp thanh khoản (dealer) phải cân bằng lại hàng tồn kho (inventory) sau mỗi giao dịch lớn; (2) **market depth** — số lượng counterparties sẵn sàng mua/bán ở các mức giá khác nhau, ảnh hưởng trực tiếp đến độ rộng bid-ask spread khi khối lượng giao dịch tăng; (3) **resilience** — tốc độ đó giá quay trở lại mức fair value sau một cú shock lớn. Trong thị trường trái phiếu cấp chính phủ, dealer-based markets (như US Treasuries) thường có bid-ask bounce thấp hơn vì độ sâu thị trường cao, nhưng trong các thị trường khác hoặc thời kỳ stress, bid-ask bounce có thể tăng 3–5 lần khi dealer inventory constraints ràng buộc và các nhà giao dịch kiểm soát rủi ro.
```

**Update `last_updated`:** `2026-09-29`

---

## Lệnh thực thi

**Sau khi edit 3 trang trên:**

```bash
python .claude/hooks/validate_wiki_page.py --all
```

**Kỳ vọng:** ✅ 0 errors

**Sau validate, chạy git status + commit:**

```bash
git status
git add 02_wiki/liquidity-premium.md 02_wiki/yield-curve.md 02_wiki/fixed-income-liquidity-search-costs-and-bid-ask-bounce-volatility.md
git commit -m "feat(research): S0 liquidity-risk enrich 3 claims, L1–L2 links, yield-curve inverted indicator"
```

---

## Tiếp theo

**Option A:** Chuyển ngay S1 — Basel III Framework (17 trang LCR/NSFR/HQLA)  
**Option B:** Chuyển S2 — ALM & FTP (43 trang, largest cluster)  
**Option C:** Chuyển S3 — Funding Markets (20 trang)

---

## File quan trọng

- **Map:** `Claude outputs/research-map-liquidity-risk.md`
- **Deep read báo cáo S0:** `Claude outputs/research-2026-09-29-liquidity-risk-S0.md`
- **Log entry:** `log.md` (updated 2026-09-29:20-57-24)

---

## Notes

- Không nâng `status` thành `stable` — chỉ update `last_updated`
- Yield-curve quá dài (~1200 từ), báo cáo đề xuất chia thành 4 trang riêng (follow-up lint)
- Money-aggregates có link chết ×5 (chuyển `/lint` sau)
