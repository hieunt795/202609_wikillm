# Session handoff: Add `/research` skill

**Date:** 2026-09-23 15:30 UTC+7  
**Commit:** 5168e1e — feat(skill): add /research skill for deep-dive cluster analysis & enrich

## Tóm tắt phiên làm việc

Đã thiết kế, implement, và commit skill `/research` mới cho wiki tri thức. Skill gộp 3 chức năng: tổng hợp/đối chiếu liên trang, bổ sung claim từ nguồn đã ingest (chunk `[x]` chỉ), đánh giá gap tri thức theo cluster chủ đề. Thêm op thứ 8 `research` vào hệ thống operation logging.

## Kết quả

### Files tạo mới
- `.claude/skills/research/SKILL.md` (89 dòng) — frontmatter + quy trình 4 bước + mục "sai lầm thường gặp"

### Files sửa
- `00_schema.md` §2 (Taxonomy): thêm Research vào cột "Tạo ở operation nào" cho `analysis`
- `00_schema.md` §3: cập nhật tên file report (`research-<date>-<topic>.md`)
- `00_schema.md` §4: thêm ngưỡng Research (cluster max 10 trang, enrich max 5 trang)
- `00_schema.md` §9: thêm Research vào transition stable/stale→draft khi enrich
- `00_schema.md` §12: đổi "7 giá trị" → "8 giá trị" `<op>`, thêm `research` vào danh sách
- `decisions.md`: thêm 1 mục [2026-09-23] giải thích lý do thêm op, giới hạn phạm vi, không fan-out

## Kiểm chứng

- ✅ Baseline validate trước sửa: 635 trang, 0 lỗi
- ✅ Validate sau sửa schema: 635 trang, 0 lỗi (schema không phá vỡ gì)
- ✅ Commit thành công, lịch sử git sạch
- ✅ SKILL.md frontmatter đúng format, description đầy đủ trigger + loại trừ
- ✅ Quy trình 4 bước rõ ràng, cap size hợp lý, ranh giới với 4 skill khác đủ

## Kiến trúc quyết định đã implement

1. **Op mới `research`** — không tái dùng op cũ vì khác bản chất (đọc liên trang + quay lại nguồn + xuất báo cáo + thêm claim mới, không chỉ verify)
2. **Phạm vi enrich ở chunk `[x]` chỉ** — giữ `03_state/` là nguồn sự thật về tiến độ ingest, không tự mở rộng
3. **Trigger theo chủ đề/tag** — agent gom cluster rồi xác nhận với user trước khi đào sâu (giống bước 0 ingest)
4. **Mô hình enrich: duyệt-theo-lô-rồi-ghi** — giống `promote`, không phải "tự sửa rồi log" như `review-node` (enrich có rủi ro cao hơn verify)

## Không thực hiện gì

- Không làm thứ nào với `log.md` — handoff này không phải operation, chỉ là chuẩn bị framework. Khi user chạy `/research` lần đầu thì mới ghi log.
- Không spawn subagent — thiết kế đơn luồng nhất quán với quyết định 2026-09-23 của `/query`

## Công việc tiếp theo

1. **Thử nghiệm skill trực tế** — chọn 1 cluster nhỏ (vd "inflation" chủ đề) chạy `/research` đầy đủ bước 0–4 để xác nhận báo cáo xuất đúng, log ghi đúng
2. **Tối ưu trigger** — nếu thấy trigger description quá dài hoặc chưa rõ, có thể rút gọn sau khi thử
3. **Tài liệu dùng** — nếu người dùng yêu cầu, có thể viết 1 trang "Cách dùng /research" hoặc "Research workflow" vào `02_wiki/index.md` mục §Sources khi skill ổn định

## Trạng thái hiện tại

- ✅ Skill ready to use
- ✅ Schema updated & validated
- ✅ Quyết định ghi vào decisions.md
- 🟡 Chưa có operation log vì chưa ai chạy skill (theo quy tắc: operation chỉ ghi khi có thay đổi wiki)

## Lưu ý cho phiên sau

- Commit 5168e1e là anchor của feature này — nếu cần rollback, có thể revert toàn bộ 3 file cùng lúc
- Không cần cập nhật `index.md` §Sources — skill research không thêm/sửa trang wiki mới, chỉ là operation quản lý nội dung
- Quá trình thử lần đầu sẽ sinh báo cáo `Claude outputs/research-<date>-<topic>.md` → có thể xem để verify chất lượng xuất báo cáo
