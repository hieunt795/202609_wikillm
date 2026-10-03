# Session Handoff — Phụ lục I Complete + Audit / Phụ lục II–IV Pending

**Ngày:** 2026-09-30 | **Phiên:** Batch 4 (Continuation/Compact) + Audit

## Kết Quả Chính

### ✅ **Batch 4 (Phần C — Dòng tiền vào): 8 trang hoàn tất**

1. `cash-inflow-recognition-principles-group1-nondefault` — Nguyên tắc (nợ nhóm 1 + không vỡ nợ)
2. `cash-inflow-secured-credit-reverse-repo-margin` — Cấp tín dụng bảo đảm (reverse repo, margin loans)
3. `cash-inflow-commitment-limits-zero-rate` — Hạn mức cam kít (0%)
4. `cash-inflow-customer-counterparty-flows` — Dòng tiền từ khách hàng (bán lẻ/SME 50%, bán buôn 50%, tổ chức tài chính 100%)
5. `cash-inflow-activity-deposits-inbound` — Tiền gửi hoạt động (0% hoạt động, 100% dư thừa)
6. `cash-inflow-derivatives-and-maturing-securities` — Phái sinh ròng + chứng khoán đáo hạn (100%)
7. `cash-inflow-other-exclusions-non-financial-revenue` — Loại trừ (doanh thu phi tài chính)
8. `cash-inflow-calculation-table-example` — Bảng tính 8 cột, ví dụ ròng 133.5 tỷ

### ✅ **Phụ lục I — Ingest 100%: 22 trang + 3 stub**

**Phần A (HQLA):** 6 trang
- Định nghĩa + công thức
- Tier 1 (100%, cash/government)
- Tier 2A (85%, bank/local authority bonds)
- Tier 2B (50–75%, equities/RMBS/corporate bonds)
- Điều chỉnh (encumbrance/repo)
- Bảng tính ví dụ

**Phần B (Dòng tiền ra):** 8 trang
- Nguyên tắc 30 ngày
- Tiền gửi bán lẻ (5–10%)
- Tiền gửi hoạt động (25%)
- Vốn bán buôn (không bảo đảm 0–100%, có bảo đảm 0–100%)
- Phái sinh ròng (100%)
- Dòng tiền ra bổ sung (20–100%)
- Cam kít ngoài bảng (5–100%)
- Bảng tính 9 cột ví dụ

**Phần C (Dòng tiền vào):** 8 trang (session này)
- Nguyên tắc ghi nhận
- Cấp tín dụng bảo đảm (0–100%)
- Hạn mức cam kít (0%)
- Dòng tiền từ khách hàng (50–100%)
- Tiền gửi hoạt động (0–100%)
- Phái sinh + chứng khoán (100%)
- Loại trừ (doanh thu phi tài chính)
- Bảng tính 8 cột ví dụ

### ✅ **Audit + Fix State File**

**Kiểm tra lại file nguồn (1.774 dòng):**
- Chương I (d.1–136): ✅ Đã ingest (6 trang + 7 stub)
- Chương II (d.137–680): ✅ Đã ingest (20 trang)
- Chương III (d.681–785): ✅ Đã ingest (3 trang)
- Phụ lục I (d.786–1474): ✅ Đã ingest (22 trang + 3 stub)
- **Phụ lục II (d.1475–1668):** ⚠️ Chưa ingest (~194 dòng)
- **Phụ lục III (d.1669–1754):** ⚠️ Chưa ingest (~86 dòng)
- **Phụ lục IV (d.1755–1774):** ⚠️ Chưa ingest (~20 dòng)

**Sửa state file:**
- `total_lines: 1277` → `1774` ✓
- Chương I `[ ]` → `[x]` ✓
- Phụ lục I `d.786–1774` → `d.786–1474` ✓
- Thêm Phụ lục II–IV `[ ]` chưa ingest ✓

## Commit History (Session này)

1. `1b2e087` feat(ingest): phuc-luc-i-part-c-dòng-tiền-vào — 7 trang
2. `f326085` log: phuc-luc-i-complete — state update
3. `e8f574f` feat(ingest): phuc-luc-i-part-c-vi-doanh-thu-phi-tai-chinh — trang 8
4. `a9250be` log: phuc-luc-i-part-c-vi-added
5. `6f2a0e4` fix(state): sbv_circular_22_final — rà soát & fix state
6. `b7f3997` log: audit-sbv-circular-22-final-complete

## Status Hiện Tại

**Wiki stats:**
- 1.099 → 1.100 trang (thêm 1 trang VI)
- Ingest hoàn tất: 40 trang + 10 stub
- Validate: ✅ --all sạch

**State file:**
- `03_state/sbv_circular_22_final.md`: Đã cập nhật (ingest 50.7%, còn 49.3% Phụ lục II–IV)

**Index:**
- `02_wiki/index.md` §Sources: sbv_circular_22_final marked "Hoàn tất 100%" (cần cập nhật lại → "50.7%")

## Công Việc Còn Lại

**Phụ lục II–IV (Lượt 6–7 dự kiến):**

| Phần | Dòng | Nội dung | Dự tính trang | Ghi chú |
|---|---|---|---|---|
| **Phụ lục II** | d.1475–1668 | NSFR — Hướng dẫn cách xác định NSFR | 6–8 | Phần A (ASF ~10 mục) + Phần B (RSF ~12 mục), bảng hệ số chi tiết |
| **Phụ lục III** | d.1669–1754 | Risk — Tổng trạng thái rủi ro (IRB) | 2–3 | Nguyên tắc + giá trị từng loại tài sản + cam kít ngoài bảng |
| **Phụ lục IV** | d.1755–1774 | Disclosure — Công bố LCR/NSFR/LDR/LEV | 1 | Liệt kê 4 khoản công bố; khoảng 20 dòng |

**Ước tính:** 9–12 trang (tương đương 1 session / batch thứ 5)

## Lý Do Dừng Session

- ✅ Batch 4 (Phần C) + VI hoàn tất
- ✅ Audit + fix state file xong
- Token còn ~14.99M (dùng ~5K token trong audit + fix)
- Session boundary tự nhiên

## Ghi Chú Cho Lượt Tiếp Theo

1. **Cập nhật index.md §Sources:** Phụ lục I status "Hoàn tất 100%" → "50.7% (Phần A–C ingest, Phần D–F phần sau)" hoặc thay bằng "Phụ lục II–IV ~9–12 trang chưa ingest"
2. **Phụ lục II (NSFR):** Quy mô tương tự Phụ lục I, có bảng hệ số chi tiết (ASF/RSF)
3. **Phụ lục III (Risk):** Nhỏ hơn, chủ yếu công thức + ví dụ
4. **Phụ lục IV (Disclosure):** Ngắn nhất, danh sách công bố
5. **Hook validation:** 1.100 trang ổn định, không expect lỗi khi ingest Phụ lục II–IV (cấu trúc tương tự Phụ lục I)

---

**Workflow sẵn sàng cho Batch 5 (Phụ lục II–IV — NSFR + Risk + Disclosure).**
