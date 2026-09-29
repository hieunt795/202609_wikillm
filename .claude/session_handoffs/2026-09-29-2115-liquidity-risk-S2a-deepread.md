# Session Handoff: Liquidity Risk S2a Deep Read

**Date:** 2026-09-29 21:15  
**Status:** S2a Deep read complete; 6 draft ready to promote (fix 4 link dead first)  
**Next:** Fix links → Promote S2a → Deep read S2b (FTP Pricing Detail, 15 trang) hoặc S2c (ALM & Gap, 14 trang)

---

## Kết quả S2a Deep Read

**Trang:** 12/12 (6 draft + 6 stable)  
**Type:** 1 analysis + 11 concept  
**Đặc điểm:** Draft pages rất chi tiết, không mỏng

---

## Bước 1: Fix 4 link dead (trước promote)

FTP coordinates (analysis) link tới 4 trang không tìm thấy:

1. **`the-typical-deposit-money-bank-balance-sheet-groups-assets-by-counterparty-and-liabilities-by-instrument`**
   - Hành động: Grep để tìm hoặc tạo stub
   - Lệnh: `grep -r "typical-deposit-money" 02_wiki/ | head -1`
   
2. **`alm-balance-sheet-balancing-progresses-through-four-operational-dimensions`**
   - Hành động: Kiểm tra S3 (ALM cluster) hoặc tạo trang nếu thiếu
   - Lệnh: `ls 02_wiki/*alm*balance* 02_wiki/*four*operational*`
   
3. **`holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage`**
   - Hành động: Grep hoặc tạo stub
   - Lệnh: `grep -r "holistic-alm" 02_wiki/`
   
4. **`regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp`**
   - Hành động: Verify trang tồn tại (có thể ở S2c)
   - Lệnh: `ls 02_wiki/*regulatory-lcr-and-nsfr*`

**Nếu trang không tìm thấy:** Cập nhật link trong FTP coordinates hoặc tạo stub tạm thời (recommend: update link → đặt vào `/lint` để triage).

---

## Bước 2: Promote 6 draft → stable

```bash
for f in \
  "ftp-coordinates-asset-liability-structure-with-risk-adjusted-margin-allocation" \
  "ftp-curve-decomposition-separates-pure-interest-rate-risk-from-liquidity-premium" \
  "cost-of-funds-in-alm-establishes-internal-hurdle-rate-for-business-margin-allocation" \
  "vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing" \
  "ftp-reporting-architecture-synthesizes-multi-dimensional-nii-and-nim-performance" \
  "matched-maturity-term-liquidity-spread-isolates-repricing-tenor-mismatch"; do
  sed -i 's/^status: draft/status: stable/' "02_wiki/$f.md"
  sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/$f.md"
done

python .claude/hooks/validate_wiki_page.py --all
```

---

## Bước 3: Log & update map

```
## [2026-09-29:21-15-xx] research | liquidity-risk — S2a
- Deep read: S2a 12 node (6 draft + 6 stable), core FTP concepts
- Promote: 6 draft → stable (link dead 4 fixed); 1 analysis (ftp-coordinates) + 5 concept
- Báo cáo: Claude outputs/research-2026-09-29-liquidity-risk-S2a.md
```

Update map: S2a → done 2026-09-29

---

## S2 Strategy — 3 Sub

S2 ALM & FTP (41–43 trang) chia:
- **S2a: Core FTP Concepts** (12 trang) — ✅ Done
- **S2b: FTP Pricing Operationalization** (~15 trang) — Next deep read
  - Trang chính: loan/deposit pricing, promotional, early-redemption, extended, corporate-bond, non-earning, non-maturity, overdue, entrusted-oda, contractual-amendment, etc.
  
- **S2c: ALM & Gap Management** (~14 trang) — After S2b
  - Trang chính: cash-flow, survival-period, maturity-ladder, contingency-funding, collateral, liquidity-risk-management, prospective-cash, standardised-repricing, etc.

---

## Files quan trọng

- **Map:** `Claude outputs/research-map-liquidity-risk.md` (update S2a status)
- **Deep read báo cáo S2a:** `Claude outputs/research-2026-09-29-liquidity-risk-S2a.md`
- **Log:** `log.md` (append entry)

---

## Notes

- Link dead 4 trang là vấn đề chính; nên fix trước promote để tránh orphan pages
- S2b & S2c có thể chạy tuần tự hoặc song song (nếu context cho phép)
- Lượt S2b sẽ có ~15 trang draft + pricing operationalization claims

