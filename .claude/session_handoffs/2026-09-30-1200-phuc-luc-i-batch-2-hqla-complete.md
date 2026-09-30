# Session Handoff — Phụ lục I Batch 2 (HQLA — 6 trang)

**Ngày:** 2026-09-30 | **Lượt:** Batch 2

## Kết quả

✅ **Phần A (HQLA) hoàn tất: 6 trang chi tiết sâu**

1. `lcr-hqla-definition-framework` — LCR tổng quan, công thức, vai trò 3 cấp HQLA, lộ trình áp dụng 70%→85%→100%
2. `hqla-tier-1-criteria-formula` — Cấp 1 (tiền, trái phiếu CP, nợ NHNN), hệ số 100%, xử lý repo ≤30 ngày
3. `hqla-tier-2a-criteria-calculation` — Cấp 2A (trái phiếu ngân hàng A–, chính quyền địa phương A–), hệ số 85%, cap 40%, xử lý downgrade
4. `hqla-tier-2b-criteria-haircut` — Cấp 2B (cổ phiếu VN30, RMBS, trái phiếu công ty BBB–), hệ số 50–75%, haircut 25–35%, cap 15%
5. `hqla-adjustments-encumbrance-repo-unwinding` — Ràng buộc tài sản, repo/reverse repo xử lý, điều chỉnh giá trị, downgrade
6. `hqla-calculation-table-example` — Bảng 7 cột ví dụ: mục, danh mục, dư nợ, hệ số, giá trị sau nhân, haircut, giá trị cuối cùng; kiểm tra giới hạn 40%/15%

**Mỗi trang đạt tiêu chí "sâu + rõ ràng":**
- Định nghĩa đầy đủ (định nghĩa khái niệm, danh mục cụ thể)
- Công thức/tiêu chí chi tiết (tiêu chí nhập, hệ số, điều kiện)
- Ví dụ số thực tế (không chỉ lý thuyết)
- Ghi chú từ nguồn (§7.5 ingest: chú thích d. số từ sbv_circular_22_final)
- Link liên quan (wiki links kèm lý do)

## Kiểm tra đã chạy

- ✅ Hook tự động (tất cả 6 trang pass)
- ✅ 2 commit ghi lại tiến độ (batch 1 + batch 2)
- ✅ Stub tạo trước: 4 trang (Cấp 2A, 2B, Điều chỉnh, Cash outflow rates)

## Công việc còn lại

**Phần B (Dòng tiền ra) — 8 trang:**
1. Nguyên tắc cơ bản (định nghĩa, 30 ngày, kỳ hạn, điều kiện ghi nhận)
2. Tiền gửi bán lẻ (ổn định 5%, không ổn định 10%)
3. Vốn bán buôn (bảo đảm/không bảo đảm 0–100%)
4. Nợ & phái sinh (hệ số 100%, phát hành, call, điều khoản)
5. Cam kít ngoài bảng (khoản cấp quay vòng, hệ số drawdown 0–100%)
6. Điều chỉnh dòng tiền ra (ký quỹ biến động, unwinding repo <30 ngày)
7. Cơ chế cap 75% (công thức ròng, ví dụ)
8. Bảng tính dòng tiền ra (9 cột, 7 dòng mục, ví dụ)

**Phần C (Dòng tiền vào) — 7 trang:**
1. Nguyên tắc ghi nhận (nợ nhóm 1, không vỡ nợ, loại trừ điều kiện)
2. Cấp tín dụng bảo đảm (reverse repo, margin loans, hệ số 0–100%)
3. Hạn mức cam kít (hệ số 0%)
4. Dòng tiền từ khách hàng (phân loại đối tác 50–100%)
5. Tiền gửi hoạt động (full 0%, dư thừa 100%)
6. Phái sinh & chứng khoán đáo hạn (100%)
7. Bảng tính dòng tiền vào (8 cột, 7 dòng mục, ví dụ)

**Tổng cộng:** 15 trang Phần B+C

## Lý do dừng batch 2

Token còn ~15K — không đủ viết chi tiết 15 trang Phần B+C theo tiêu chí "sâu + rõ ràng" mà user yêu cầu. Batch 3 ở session mới sẽ viết Phần B (8 trang) đầu tiên.

## Bước tiếp theo (Batch 3)

1. Session mới: compact context
2. Viết 8 trang Phần B chi tiết (mỗi trang ≤ 1000 từ, tự chứa đủ)
3. Commit batch 3
4. Tiếp tục batch 4 (7 trang Phần C)
5. Cập nhật `03_state/sbv_circular_22_final.md` → đánh `[x]` cho Phụ lục I
6. Cập nhật `02_wiki/index.md` §Sources → Phụ lục I hoàn tất

## Ghi chú cho lượt tiếp theo

- Không thay đổi nội dung Phần A đã viết (pass kiểm tra, commit xong)
- Stub 4 trang (Cấp 2A, 2B, Điều chỉnh, Cash outflow) đã tạo → thay thế bằng nội dung thực khi viết
- Phần B: dòng tiền ra từ **tất cả loại** khách hàng (bán lẻ, bán buôn, TCTC, chính phủ, phái sinh) — cần chi tiết hệ số tương ứng từng loại
- Phần C: dòng tiền vào **chỉ tính khi đạt điều kiện** (nợ nhóm 1, không vỡ nợ) — cần nhấn mạnh điều kiện ghi nhận
- Chú thích source: dùng `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` sau claim (§7.5 ingest)
