# Session: Tối ưu project CLAUDE.md (thử nghiệm)

**Thời gian:** 2026-09-29 18:57:38

## Kết quả
✅ Tối ưu `CLAUDE.md` thành công:
- Đổi thứ tự: "Luật cứng" chuyển lên trước "Sáu operation" → LLM nắm luật trước khi học các operation
- Gộp bullet: "Nhắc nhanh về trang wiki" từ 7 → 6 bullet (gộp 2 ý về `[[wikilink]]`)
- Rút gọn: "Công cụ ghi câu hỏi" từ 4 dòng → 1 dòng

Số dòng: 78 (tương đương / ít hơn xíu). Tất cả lệnh `validate_wiki_page.py` (`--all`, `--coverage`, `--backlinks`, etc.) và từ khoá chốt (`01_sources`, `⚠️ Conflict`, `[x]`, `§7.5`) vẫn tồn tại.

## Kiểm tra đã chạy
- ✅ `git diff CLAUDE.md` → chỉ có di chuyển khối, gộp bullet, rút gọn chữ; không mất ý nào
- ✅ `git status` → clean (chưa commit; phiên vừa thay đổi repo)
- ✅ Grep từ khoá: `01_sources`, `⚠️ Conflict`, `[x]`, `§7.5`, `--all`, `--coverage` — tất cả còn tồn tại

## Tương tự global CLAUDE.md (mục 1)
Mục 1 thêm "Quy tắc cốt lõi" ở đầu global (+6 bullet, ~1 dòng ròng). Mục 2 này thay vào đó di chuyển "Luật cứng" mà không thêm khối mới → tiết kiệm token hơn.

## Việc còn lại
- Chỉ test khi mở session mới: xem LLM có tuân thủ luật ưu tiên ("Luật cứng" là §14 giờ thay vì §29 trước không)
- Nếu hiệu quả, có thể xem xét optimize thêm các file khác (skills, hooks, v.v.)
- Global CLAUDE.md đã thay đổi (có "Quy tắc cốt lõi" mới); cần test cùng với project CLAUDE.md

## Blocker / Rủi ro
- Không có: file nằm ngoài `02_wiki/` → không cần chạy hook validate
- Di chuyển khối có thể ảnh hưởng skill nếu skill hard-code line number (grep để chắc)
