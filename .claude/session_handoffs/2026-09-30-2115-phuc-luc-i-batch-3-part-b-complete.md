# Session Handoff — Phụ lục I Batch 3 (Dòng tiền ra — 8 trang)

**Ngày:** 2026-09-30 | **Lượt:** Batch 3

## Kết quả

✅ **Phần B (Dòng tiền ra) hoàn tất: 8 trang chi tiết sâu**

1. `cash-outflow-principles-30day-framework` — Nguyên tắc 30 ngày, kỳ hạn, điều kiện ghi nhận, loại trừ
2. `cash-outflow-retail-deposits-stability-rates` — Tiền gửi bán lẻ ổn định (5%), kém ổn định (10%)
3. `cash-outflow-activity-deposits-clearing-custody` — Tiền gửi hoạt động (25%), thanh toán/lưu ký/quản lý tiền
4. `cash-outflow-wholesale-unsecured-secured` — Vốn bán buôn không bảo đảm (5–100%) + có bảo đảm (0–100%)
5. `cash-outflow-derivatives-net-basis` — Phái sinh (100% hệ số), net basis, quyền chọn, cheapest-to-deliver
6. `cash-outflow-supplementary-downgrade-markup-collateral` — Dòng tiền ra bổ sung (20–100%), 5 khoản điều chỉnh
7. `cash-outflow-commitments-drawdown-rates` — Cam kít ngoài bảng (5–100%), 4 loại chính
8. `cash-outflow-calculation-table-example` — Bảng tính 9 cột, 4 giai đoạn, ví dụ ròng 789.25 tỷ

**Mỗi trang đạt tiêu chí "sâu + rõ ràng":**
- Định nghĩa đầy đủ + tiêu chí + công thức/hệ số + ví dụ số + ghi chú nguồn
- Link liên quan (wiki links kèm lý do) — không mồ côi
- Tuân thủ writing-style (A–I, profile wiki, giọng phân tích)

**+ Phụ trợ:** 3 stub HQLA tiers (Tier 1, 2A, 2B) cho link từ Phần A (lcr-hqla-definition-framework)

## Kiểm tra đã chạy

- ✅ Hook tự động (tất cả 8 trang + stub pass)
- ✅ 2 commit ghi lại Batch 3 + state update
- ✅ Wikilink hoàn chỉnh (không mồ côi)

## Công việc còn lại

**Phần C (Dòng tiền vào) — 7 trang:**
1. Nguyên tắc ghi nhận (nợ nhóm 1, không vỡ nợ, loại trừ điều kiện)
2. Cấp tín dụng bảo đảm (reverse repo, margin loans, 0–100%)
3. Hạn mức cam kít (0% hệ số)
4. Dòng tiền từ khách hàng (phân loại đối tác, 50–100%)
5. Tiền gửi hoạt động (full 0%, dư thừa 100%)
6. Phái sinh & chứng khoán đáo hạn (100%)
7. Bảng tính dòng tiền vào (8 cột, 7 dòng mục, ví dụ)

**Tổng:** 7 trang Phần C để hoàn tất ingest Phụ lục I.

## Lý do dừng batch 3

Token còn ~14.96M. Batch 3 đã sử dụng ~1M token cho 8 trang chi tiết (+ setup stub). Batch 4 ước tính 1M token tương tự. Dừng tại session boundary để tối ưu hóa.

## Bước tiếp theo (Batch 4)

1. Session mới: compact context
2. Viết 7 trang Phần C chi tiết (mỗi trang ≤ 1000 từ, tự chứa)
3. Commit batch 4
4. Cập nhật `03_state/sbv_circular_22_final.md` → đánh `[x]` cho Phụ lục I
5. Cập nhật `02_wiki/index.md` §Sources → Phụ lục I hoàn tất

## Ghi chú cho lượt tiếp theo

- Phần C: dòng tiền vào **chỉ tính khi đạt điều kiện** (nợ nhóm 1, không vỡ nợ) — nhấn mạnh điều kiện ghi nhận
- Chú thích source: dùng `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` sau mọi claim từ dòng 1352–1774
- Tập quá cao: Phần C có mục "Biểu mẫu tính Dòng tiền vào" bảng 8 cột → tuân thủ như bảng 9 cột Phần B
- Batch 4 sẽ hoàn tất ingest toàn bộ Phụ lục I (21 trang chi tiết + 7 stub) ✓
