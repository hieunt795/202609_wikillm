# Session Handoff: Liquidity Risk S1 Deep Read

**Date:** 2026-09-29 21:30  
**Status:** S1 Deep read complete; 5 draft ready to promote; 2 link dead (defer to /lint)  
**Next:** Promote 5 draft → stable → S2 ALM/FTP (43 pages) or continue directly

---

## Kết quả S1 Deep Read

**Trang:** 15/15 (5 draft + 10 stable)  
**Đặc điểm:** Gần như hoàn chỉnh; draft pages rất chi tiết (không mỏng)  
**Recommendation:** Promote 5 draft → stable; không enrich claim mới

---

## Bước promote 5 draft trang

Chỉ cần đổi `status: draft` → `status: stable` và cập nhật `last_updated: 2026-09-29` (không thêm claim).

**Lệnh (bash shell hoặc bằng tay Edit từng trang):**

```bash
# Trang 1
sed -i 's/^status: draft/status: stable/' "02_wiki/basel-iii-lcr-master-factor-matrix-and-comprehensive-calibration-architecture.md"
sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/basel-iii-lcr-master-factor-matrix-and-comprehensive-calibration-architecture.md"

# Trang 2
sed -i 's/^status: draft/status: stable/' "02_wiki/basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability.md"
sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability.md"

# Trang 3
sed -i 's/^status: draft/status: stable/' "02_wiki/basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers.md"
sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers.md"

# Trang 4
sed -i 's/^status: draft/status: stable/' "02_wiki/basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability.md"
sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability.md"

# Trang 5
sed -i 's/^status: draft/status: stable/' "02_wiki/loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity.md"
sed -i 's/^last_updated: .*/last_updated: 2026-09-29/' "02_wiki/loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity.md"

# Validate
python .claude/hooks/validate_wiki_page.py --all
```

---

## Link chết (defer để /lint)

Báo cáo phát hiện 2 trang missing:
1. `asf-and-rsf-factor-matrices-calibrate-nsfr-structural-funding-requirements` — link dead từ NSFR draft (d.line ~50)
2. `consolidated-lcr-cross-border-framework-regulates-home-host-discretion-and-trapped-liquidity` — link dead từ LCR draft (d.line ~51)

**Lựa chọn:**
- **Option A (nên làm):** Fix bằng `/lint` — triage, quyết định tạo stub hoặc update link
- **Option B (không làm):** Bỏ qua; promote trước, fix link sau

---

## Log entry (sau promote + validate)

```
## [2026-09-29:21-30-xx] research | liquidity-risk — S1
- Deep read: S1 15 node (5 draft + 10 stable), đầy đủ nội dung
- Promote: 5 draft → stable (LCR, NSFR, LDR, master-matrix, stress-framework)
- Link dead defer: 2 trang missing (ASF/RSF, consolidated-LCR) → /lint
- Báo cáo: Claude outputs/research-2026-09-29-liquidity-risk-S1.md
```

---

## Tiếp theo: S2 ALM & FTP

**Kích thước:** 43 trang — cụm lớn nhất  
**Thành phần chính:**
- FTP curve, matched-maturity FTP, term liquidity premium
- Structural contribution, internal liquidity cost allocation
- Cash flow, gap analysis, survival period metrics
- Maturity balancing, contingency funding plan

**Chiến lược:** Quét 43 trang, chia ≤ 15 node deep read, enrich ≤ 7 trang draft

---

## File quan trọng

- **Map:** `Claude outputs/research-map-liquidity-risk.md` (update S1 status → done)
- **Deep read báo cáo S0:** `Claude outputs/research-2026-09-29-liquidity-risk-S0.md`
- **Deep read báo cáo S1:** `Claude outputs/research-2026-09-29-liquidity-risk-S1.md`
- **Log:** `log.md` (append entry)

