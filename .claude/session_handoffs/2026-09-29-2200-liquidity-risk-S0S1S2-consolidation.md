# Session Handoff: Liquidity Risk Research — S0, S1, S2 Consolidation

**Date:** 2026-09-29 22:00  
**Status:** S0, S1, S2 (a/b/c) deep read complete; 31 draft pages ready to promote + 3 claim enrich proposed  
**Next:** Promote all draft → stable; enrich S0 claims → write wiki

---

## Consolidation Summary

**Deep read completed:**
- ✅ S0: 3 claim enrich proposed (ready to write wiki)
- ✅ S1: 5 draft → promote; 2 link dead defer to /lint
- ✅ S2a: 6 draft → promote; 4 link dead to fix
- ✅ S2b: 14 draft → promote; 0 link dead
- ✅ S2c: 3 draft → promote; 0 link dead

**Total pages ready to promote:** 31 draft → stable

---

## Batch 1: Fix S2a link dead (4 trang) — BEFORE promote

S2a `ftp-coordinates` references 4 missing pages:
1. `the-typical-deposit-money-bank-balance-sheet-groups-assets-by-counterparty-and-liabilities-by-instrument`
2. `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` ← **EXISTS in S2c!**
3. `holistic-alm-elevates-balance-sheet-strategy-from-tactical-compliance-to-technological-advantage`
4. `regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp`

**Action:** 
- Verify link #2 (alm-balance-sheet-balancing) — already in wiki, link is correct
- Grep/verify #1, #3, #4; decide: create stub, update link, or defer to /lint

```bash
grep -r "the-typical-deposit-money" 02_wiki/
grep -r "holistic-alm-elevates" 02_wiki/
grep -r "regulatory-lcr-and-nsfr-constraints" 02_wiki/
```

---

## Batch 2: Promote 31 draft → stable

**S1 (5 draft):**
```bash
for f in \
  "basel-iii-lcr-master-factor-matrix-and-comprehensive-calibration-architecture" \
  "basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability" \
  "basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers" \
  "basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability" \
  "loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity"; do
  sed -i 's/^status: draft/status: stable/' "02_wiki/$f.md"
  sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/$f.md"
done
```

**S2a (6 draft):** (after fix link dead)
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
```

**S2b (14 draft):**
```bash
for f in \
  "amortizing-loan-cof-pricing-applies-weighted-average-tenor" \
  "bullet-term-deposit-vof-pricing-locks-fixed-spread-at-origination" \
  "corporate-bond-portfolio-ftp-pricing-differentiates-banking-book-and-trading-book" \
  "deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles" \
  "extended-loan-ftp-pricing-resets-cof-to-cumulative-maturity" \
  "installment-deposit-vof-pricing-preserves-commercial-margin" \
  "margin-and-escrow-deposit-vof-pricing-evaluates-collateral-lock-up-intensity" \
  "non-maturity-credit-facility-cof-pricing-applies-behavioral-redemption-curve" \
  "non-maturity-deposit-vof-pricing-combines-redemption-curve-and-regulatory-floor" \
  "overdue-loan-ftp-pricing-freezes-original-cof-and-forfeits-promotional-spreads" \
  "promotional-and-behavioral-loan-ftp-pricing-decomposes-hybrid-cash-flows" \
  "promotional-hybrid-loan-ftp-pricing-evaluates-dual-tenor-and-component-decomposition" \
  "retail-certificate-of-deposit-vof-pricing-differentiates-planned-and-alco-campaigns" \
  "straight-term-bullet-loan-cof-pricing-decomposes-repricing-and-term-risk"; do
  sed -i 's/^status: draft/status: stable/' "02_wiki/$f.md"
  sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/$f.md"
done
```

**S2c (3 draft):**
```bash
for f in \
  "cash-flow-survival-period-metrics-identify-initial-liquidity-exhaustion-thresholds" \
  "contractual-maturity-ladder-and-cash-flow-reporting-framework-monitors-lcr-mismatches" \
  "maturity-balancing-manages-liquidity-duration-to-mitigate-rollover-and-repricing-risks"; do
  sed -i 's/^status: draft/status: stable/' "02_wiki/$f.md"
  sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/$f.md"
done
```

**Validate:**
```bash
python .claude/hooks/validate_wiki_page.py --all
```

---

## Batch 3: Log & update map

Log entry:
```
## [2026-09-29:22-00-xx] research | liquidity-risk — S1 + S2a + S2b + S2c
- Promote: S1 5 draft + S2a 6 draft + S2b 14 draft + S2c 3 draft = 31 draft → stable (after S2a link fix)
- Phát hiện: S1 2 link dead defer /lint; S2a 4 link dead (1 exists in S2c, verify 3 others)
- Báo cáo: research-2026-09-29-liquidity-risk-S1/S2a/S2b/S2c.md
```

Update map: S1 → done; S2a/S2b/S2c → done

---

## Batch 4: Write S0 enrich claims (optional lượt này hoặc lượt sau)

S0 proposed 3 claims từ liquidity-premium deep read:
- C1: Liquidity premium trong term structure
- C2: Liquidity premium hypothesis giải thích upward-sloping curves  
- C3: Relationship giữa credit risk, liquidity tax, maturity premiums

**Quyết định:** Enrich ngay lần này (3 claim nhỏ) hay defer đến lượt S3 deep read?

---

## Next Steps

**Session kế tiếp:**
1. Fix S2a link dead (verify 3 trang missing)
2. Promote 31 draft → stable (batch)
3. Log + update map
4. Quyết định: Write S0 enrich claims hay Deep read S3?

**S3–S5 Pending:**
- S3: Funding Markets & Liquidity Pricing (20 trang)
- S4: Crisis & Systemic Contagion (17 trang)
- S5: Central Bank & Policy Tools (16 trang)

---

## Files

- **Deep read reports:** `research-2026-09-29-liquidity-risk-{S0,S1,S2a,S2b,S2c}.md`
- **Map:** `research-map-liquidity-risk.md` (updated S2a/S2b/S2c status)
- **Log:** `log.md` (append when promote)

