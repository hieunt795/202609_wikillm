# Session handoff: Sửa P0 skill writing-style

**Ngày:** 2026-09-24 21:08 UTC+7 · **Chưa commit**

## Kết Quả

Hoàn tất sửa 3 vấn đề ưu tiên cao (P0) trong skill `writing-style` dựa trên audit 2026-09-24:

### 1. Mở Rộng Rule C1 (Chủ Thể Cụ Thể)
- Thêm 3 loại chủ thể cụ thể chuẩn hóa: tổ chức cụ thể (NHNN, IMF, ngân hàng thương mại), biến số kinh tế tác nhân (lãi suất, tỷ giá, cơ sở tiền tệ), nhóm chủ thể xác định (các nhà đầu tư, người sử dụng lao động).
- Nêu rõ **không** tính là chủ thể cụ thể: danh ngữ trừu tượng (cơ chế, quy trình, rủi ro), tác nhân mơ hồ (thị trường, người ta, họ).
- SKILL.md C1 từ 3 dòng → 6 dòng (gợi ý, trỏ link `references/subject-guidelines.md`).
- Tạo `references/subject-guidelines.md`: 3 mục loại chủ thể + 1 mục phản ví dụ, mỗi mục 2–3 cặp sai→đúng từ ngôn ngữ kinh tế vĩ mô thực tế.

### 2. Làm Rõ Rule B1 (Quota Động Từ Sáo)
- Thêm định nghĩa phạm vi tính: mỗi trang wiki riêng, mỗi section báo cáo riêng, khi ingest lượt lớn tính từng trang không cộng dồn.
- SKILL.md B1 từ 2 dòng → 1 dòng (tóm tắt phạm vi + trỏ link `references/hollow-verbs.md`).
- Tạo `references/hollow-verbs.md`: bảng 11 từ cấm (giữ nguyên từ gốc) + từ thay thế, mục "Phạm Vi Tính" (chi tiết wiki/báo cáo/ingest), mục "Ngoại Lệ".

### 3. Thêm Rule D3 (Tiếng Anh Trong Văn Bản Tiếng Việt)
- Thêm rule D3 mới sau D2: nguyên tắc quyết định khi dùng tiếng Anh vs. dịch tiếng Việt (nếu có dịch ngắn gọn → định nghĩa 1 lần, dùng nhất quán; không có → giữ tiếng Anh).
- Cảnh báo: một số từ bị dịch sai nghiêm trọng (sterilization ≠ tiệt trùng) — phải đối chiếu `references/vietnamese-translation-errors.md` trước khi tự dịch.
- SKILL.md D3 = 5 dòng (nguyên tắc rõ ràng, cảnh báo, link).
- Tạo `references/vietnamese-translation-errors.md`: bảng từ dịch sai, seed 1 case đã xác nhận thật (sterilization), template trống + hướng dẫn bổ sung khi phát hiện lỗi mới.

### 4. Cập Nhật Quy Trình SKILL.md
- Thêm bước 6 vào mục "Quy Trình": rule trỏ `references/` chỉ mở khi gặp trường hợp nghi ngờ cụ thể, không bắt buộc đọc trước.

### 5. Ghi Decisions.md
- Thêm 1 mục `## [2026-09-24] Mở rộng C1/B1, thêm D3 cho writing-style; tách references/` với phần Quyết Định/Lý Do/File thay đổi.

## Kiểm Tra Đã Chạy

1. **SKILL.md sau sửa:**
   - Frontmatter (`name`, `description`) không đổi ✓
   - Số dòng: 164 dòng (từ 158 gốc + ~10 dòng thêm C1/B1/D3/quy trình) ✓
   - C1/B1/D3 link đúng đến file `references/` ✓
   - Quy trình bước 6 thêm ✓

2. **3 file `references/` mới:**
   - `subject-guidelines.md`: 100 dòng, 3 loại chủ thể + 1 phản ví dụ, bảng markdown render đúng ✓
   - `hollow-verbs.md`: 110 dòng, bảng 11 từ + phạm vi/ngoại lệ, ghi chú đầy đủ ✓
   - `vietnamese-translation-errors.md`: 60 dòng, seed sterilization (xác nhận từ audit 2026-09-23), template trống + hướng dẫn ✓

3. **Decisions.md:**
   - Mục mới đúng định dạng `## [YYYY-MM-DD] <tiêu đề>` ✓
   - Có **Quyết định**, **Lý do**, **File thay đổi** ✓
   - Trỏ đúng audit nguồn (2026-09-24) và audit liên quan (2026-09-23) ✓

4. **Grep cross-check:**
   - Không skill/file nào khác tham chiếu diễn giải C1/B1 cụ thể (chỉ trích số ID khi báo cáo vi phạm) ✓
   - Grep "tiệt trùng" wiki = 0 kết quả (đã sạch từ audit trước) ✓
   - Wiki thực tế: futures = "hợp đồng tương lai" (dịch chuẩn), repo = "hợp đồng mua lại (repurchase agreement hay repo)" (định nghĩa 1 lần), haircut = giữ tiếng Anh (không dịch) → D3 quy tắc khớp thực tế ✓

5. **Git status:**
   - Chỉ 6 file thay đổi/thêm: `.claude/skills/writing-style/SKILL.md` (sửa), 3 file `references/` (thêm), `decisions.md` (sửa), `.claude/session_handoffs/2026-09-24-2108-writing-style-p0-fixes.md` (thêm) ✓
   - Không đụng `02_wiki/`, `00_schema.md`, `CLAUDE.md`, bất kỳ skill khác ✓

## Việc Còn Lại / Bước Tiếp Theo

1. **Commit:** `git add .claude/skills/writing-style/ decisions.md .claude/session_handoffs/` → `git commit -m "feat(skill): sửa P0 writing-style — mở rộng C1/B1, thêm D3, tách references/"`.
2. **P1 (tuần):** Bổ sung danh sách B2 (từ cực đoan), rõ ràng C2 (sửa vs. thêm nội dung), mở rộng G4 (bullet vs. văn xuôi).
3. **P2 (khi rảnh):** Thêm ví dụ cụ thể cho từng rule, tạo quick-checklist top 10 lỗi.

## Blocker

Không có. Hook `validate_wiki_page.py` không áp cho file skill (chỉ áp `02_wiki/`) → không cần chạy.
