# Session Handoff: Research Cân Đối Nguồn - Sử Dụng Nguồn Ngân Hàng (Sub-cluster 2)

**Date:** 2026-09-28:23-11-10  
**Status:** ✅ Complete, validated, logged

## Summary

Completed `/research` operation on Sub-cluster 2 ("Cơ chế Điều phối & Tối ưu hoá nguồn vốn nội bộ qua FTP" / Funding Steering & Optimization via FTP) under the topic "Cân đối nguồn - sử dụng nguồn của ngân hàng":
- Cluster: 6 trang (`cost-of-funds-...`, `funds-transfer-pricing-...`, `vietnam-banking-ftp-...`, `balance-sheet-optimization-...`, `ftp-business-steering-...`, `ftp-transmission-channels-...`).
- Enriched: 5 trang (`cost-of-funds-...`, `funds-transfer-pricing-...`, `vietnam-banking-ftp-...`, `balance-sheet-optimization-...`, `ftp-business-steering-...`), bổ sung 5 claim mới từ `tata_bank_alm` và `vab_ftp_methodology`. Cả 4 trang `stable` đã chuyển status `stable → draft`, trang `cost-of-funds-...` giữ `draft`, tất cả nâng `last_updated: 2026-09-28`.
- Cross-links: Bổ sung 2 liên kết chéo tới trang analysis `bank-balance-sheet-balancing-reconciles-monetary-accounting-liquidity-gaps-and-economic-value.md` từ `cost-of-funds-...` và `vietnam-banking-ftp-...`.
- Sources: Bổ sung `tata_bank_alm` vào `sources:` của `balance-sheet-optimization-models-calibrate-ftp-as-a-control-variable`.
- Validation: `python .claude/hooks/validate_wiki_page.py --all` đạt 100% sạch (**1030 trang quét, 0 vấn đề, 0 mồ côi**).
- Report: `Claude outputs/research-2026-09-28-bank-sources-and-uses-sub2-ftp.md`.
- Log: Ghi entry vào `log.md` `[2026-09-28:23-11-10] research | Cân đối nguồn - sử dụng nguồn ngân hàng (Sub-cluster 2)`.

## Next Steps

- Tiến hành Sub-cluster 3 (*Giới hạn quy định & Tỷ lệ an toàn cân đối nguồn: LDR, NSFR, LCR, Quy định chuyển đổi kỳ hạn*, 5 trang).
