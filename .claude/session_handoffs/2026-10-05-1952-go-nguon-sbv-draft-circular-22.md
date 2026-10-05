# Handoff — gỡ nguồn `sbv_draft_circular_replace_22` (2026-10-05 19:52)

## Kết quả

Người dùng yêu cầu xoá mọi thứ liên quan tới `sbv_draft_circular_replace_22` và duyệt tự động phương án đề xuất. Chưa commit.

- **Giữ nguyên** file nguồn `01_sources/vietnam-regulator/alm/10_DTTT_thay_the_Thong_tu_22_260421_37a8.md` (quy tắc bất biến; SHA-256 không đổi). Nguồn hiện ở trạng thái "chưa kê" trong `--verify-sources`.
- **Xoá** `03_state/sbv_draft_circular_replace_22.md`; gỡ dòng bảng Source id và mục `## sbv_draft_circular_replace_22` trong `_sources_manifest.md`; gỡ dòng §Sources trong `02_wiki/index.md`; gỡ id khỏi `.claude/docs/luong-van-hanh.html`.
- **Xoá 12 trang wiki** (7 đơn nguồn + 5 trang dựng gần như toàn bộ từ dự thảo): `asf-and-rsf-factor-matrices…`, `basel-iii-leverage-ratio…`, `contractual-maturity-ladder…`, `equity-and-corporate-bond-financing-limits…`, `leverage-ratio-exposure-measure…`, `regulatory-liquidity-transition-rules…`, `sovereign-bond-holding-ceilings…`, `statutory-capital-real-value…`, `pillar-3-liquidity-disclosure-standards…`, `contingent-liquidity-outflows-and-credit-facility-drawdowns…`, `contractual-cash-inflow-caps…`, `retail-and-wholesale-deposit-run-off-rates…`.
- **Gỡ claim + chú thích ở 11 trang giữ lại** (đã nâng `last_updated: 2026-10-05`): LCR, NSFR, LDR, `hqla-eligibility…`, `contingent-liquidity-charge…`, `credit-underwriting…`, `deposit-product-vof…`, `liquidity-risk-management-framework…`, `regulatory-credit-conversion-factors…`, `regulatory-lcr-and-nsfr-constraints…`, `three-tier-capital-adequacy…`.
- **Sửa link ở 20 trang khác** (gỡ khỏi "Xem thêm", bỏ câu/mệnh đề trỏ tới trang đã xoá; 2 chỗ đổi sang `contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns`).
- Index: mục "Dự thảo thay thế Thông tư 22" đổi thành "Các Tỷ lệ Thanh khoản và Cấu trúc Nguồn vốn (LCR, NSFR, LDR, HQLA)" với 4 trang còn lại.

## Kiểm tra đã chạy

- `--all`: 1021 trang, 0 trang có vấn đề, 0 mồ côi.
- `--verify-sources`: 191 file trong bản kê, 0 lệch/thiếu.
- `--style` trên 5 trang sửa nhiều nhất: 0 cảnh báo.
- `grep` id nguồn: chỉ còn trong `log.md` (lịch sử, cố ý giữ) và các báo cáo cũ ở `Claude outputs/`.

## Việc còn lại / lưu ý

- **NSFR và LDR còn rất mỏng** (4 đoạn mỗi trang) nhưng vẫn `status: stable`. Câu mở đầu trang LDR và câu định nghĩa ASF/RSF ở trang NSFR chưa có chú thích §7.5. Nên `/review-node` hoặc `/research` để bồi lại từ `bcbs_238`, `tata_bank_alm`, hoặc hạ về `draft`.
- `hqla-eligibility…`: ký hiệu `KĐC` (của dự thảo) đã đổi thành `Adj`; mục phân tầng Cấp 1/2A/2B rút gọn thành một câu trỏ sang `hqla-asset-categorisation…`.
- Trang LCR vẫn giữ một đoạn trích từ `clippings` (file `DTTT thay thế TT22.md`) bàn về dự thảo — đó là nguồn khác, chưa đụng tới.
- Các báo cáo ở `Claude outputs/` (coverage, lint, research map) còn nhắc id và các trang đã xoá; research map `bank-balance-sheet` và `bank-cash-flow-liquidity-risk` có thể lệch.
- Chưa ghi `decisions.md` (người dùng không nêu lý do gỡ nguồn).

## Bước tiếp theo

1. Người dùng review `git status` + `git diff`, rồi commit nếu đồng ý. Hoàn tác toàn bộ: `git checkout -- .` (mọi thứ bị xoá đều đã commit ở `b8ee3d6`).
2. Quyết định số phận file nguồn trong `01_sources/` (xoá tay nếu muốn) và đoạn `clippings` liên quan.
