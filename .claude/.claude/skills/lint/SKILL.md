---
name: lint
description: Kiểm tra sức khoẻ wiki 02_wiki — trang mồ côi, link chết, khái niệm chưa có trang, trang đủ điều kiện stable, mâu thuẫn tồn đọng, trang stale, trùng lặp, vi phạm Atomic, vi phạm quy ước title, nợ stub, nhiễu OCR còn sót, nợ inbox chưa triage, nguồn trong 01_sources bị thay đổi. Dùng khi người dùng muốn lint, chạy lint, kiểm tra wiki, rà soát wiki, health check, tìm trang mồ côi, kiểm tra liên kết, audit wiki, dọn dẹp wiki, hoặc sau khoảng 10 lượt ingest.
---

# Lint — kiểm tra sức khoẻ wiki

Chạy sau mỗi 10 lượt ingest hoặc theo lịch (§4). Đọc `00_schema.md` §4–§9, §11, §12.

**Lint chỉ báo cáo, không tự sửa** (luật cứng 3). Xuất báo cáo, chờ người xác nhận hướng xử lý. Lý do: lint nhìn cả wiki một lượt nên dễ sửa hàng loạt theo một phán đoán sai; người dùng duyệt trước thì lỗi dừng ở báo cáo.

## Quy trình hai lượt

**0. Chạy các lệnh máy trước mọi thứ khác:**

```bash
H=.claude/.claude/hooks/validate_wiki_page.py
python $H --all              # trang: frontmatter, heading, link chết, source id, §7.5, title, mồ côi
python $H --verify-sources   # 01_sources/ khớp bản kê (luật cứng 1)
python $H --ocr              # ứng viên nhiễu OCR
python $H --stub-debt        # nợ stub
python $H --inbox-debt       # nợ inbox
```

Hook `PostToolUse` chỉ bắt tool `Write|Edit` — file ghi bằng shell đi vòng qua nó, nên `--all` quét lại tất cả. Số trang của lượt lint lấy từ dòng cuối của `--all`. `--verify-sources` báo lệch thì ghi lên đầu báo cáo: đó là vi phạm luật cứng, không phải lỗi trang, và lint không sửa lại nguồn.

**`--all` phủ:** frontmatter đủ trường, `type`/`status` hợp lệ, tên file khớp title, `sources` không rỗng và là source id có trong bản kê, `last_updated` đúng dạng ngày, heading trong thân bài, link chết (kể cả `[[trang|nhãn]]`), link dồn thành danh sách, chú thích §7.5, title danh từ cho `case`/`analysis`, trang mồ côi theo chiều backlink.

**Phải kiểm tay ở bước 2:** mâu thuẫn tồn đọng, stale chưa đánh dấu, trùng lặp, khái niệm chưa có trang, vi phạm title ngoài phần máy bắt được, xác nhận ứng viên OCR, danh sách đủ điều kiện `stable`.

**1. Lượt rẻ — quét frontmatter toàn bộ `02_wiki/`.** Không đọc full content. Với khoảng 300 trang, frontmatter chỉ khoảng 3.000 dòng nên vẫn làm trong context chính; giao subagent `Explore` khi wiki vượt khoảng 600 trang hoặc khi người dùng yêu cầu.

**2. Đối chiếu 11 tiêu chí:**

| Lỗi | Cách phát hiện |
|---|---|
| Trang mồ côi | outlink = 0 **HOẶC** backlink = 0. Vế outlink không áp cho `status: stub`. Bước 0 (`--all`) kiểm cả hai |
| Link chết | `[[x]]` hoặc `[[x\|nhãn]]` trỏ tới trang không tồn tại (§6). Bước 0 kiểm |
| Khái niệm chưa có trang | thuật ngữ được nhắc trong thân bài của **≥ 3 trang** mà chưa có trang riêng (§6). Đề xuất tạo `status: stub` rồi chèn link |
| Mâu thuẫn tồn đọng | còn `⚠️ Conflict` chưa xử lý (`grep -l "⚠️ Conflict" 02_wiki/*.md`) |
| Stale chưa đánh dấu | trang `stable` có nguồn liên quan được ingest sau `last_updated` mà chưa chuyển `stale` (§9). So `sources:` + `last_updated` với các mục `ingest` trong `log.md` |
| Trùng lặp entity | hai trang cùng mô tả một thực thể |
| Vi phạm Atomic | thân bài có heading cấp 2+, hoặc `[[wikilink]]` dồn thành danh sách "xem thêm" (§5, §7). Bước 0 kiểm |
| Vi phạm title | `case`/`analysis` đặt title danh từ; title mơ hồ hoặc không mô tả toàn bộ nội dung trang (§8). Title phủ định **không** phải lỗi (§8 luật 1) |
| Nợ stub | dòng `NO` của `--stub-debt` (≥ 3 lượt ingest kể từ khi tạo, §9) |
| Nhiễu OCR còn sót | ứng viên của `--ocr`, đã mở trang xác nhận |
| Nợ inbox | dòng `NO` của `--inbox-debt` (≥ 3 lượt lint, §11) |

**Khái niệm chưa có trang** không có lệnh tự động: đọc lướt thân bài các trang ở lượt 3, ghi lại thuật ngữ lặp lại chưa có `[[link]]`, rồi đếm bằng `grep -li "<thuật ngữ>" 02_wiki/*.md --exclude=index.md`. Đếm theo khái niệm, không theo chuỗi: "thâm hụt" có thể là thâm hụt vãng lai hoặc thâm hụt ngân sách.

**Nhiễu OCR:** `--ocr` quét thân bài sau khi bỏ `[[link]]`, `$công thức$`, `` `code` `` và chú thích §7.5, theo sáu họ mẫu: `l`/`O` thay chữ số hoặc `I` hoa (`lmbalance`, `tO`); số chú thích dính vào từ (`Economiesl3`); chữ số bị tách (`1 993`); HOA–thường lẫn (`COLmtries`); nguyên âm nhân đôi (`Waaes`); rác markdown (`<sup>`, `<span id=`, `[#page-`, `�`). Ứng viên chỉ là lưới lọc thô: tên riêng như `Paasche` là báo giả, và lỗi OCR tạo ra từ có thật (`set our` thay `set out`) chỉ lộ ra khi đọc. Token OCR lọt vào trang gần như chắc chắn nằm trong câu chép nguyên văn (§7.4), nên báo cáo kèm cả hai lỗi.

**3. Lượt đắt — chỉ mở full content các trang bị flag ở lượt 2.**

**4. Xuất báo cáo** vào `Claude outputs/lint-<YYYY-MM-DD>-<số trang>.md` (§3), nhóm theo loại lỗi, mỗi mục nêu trang + lý do + hướng sửa đề xuất. Không thực hiện sửa. Báo cáo kèm hai mục:

- **Đủ điều kiện `stable`** (§9): mọi trang `status: draft` thoả **đồng thời** — `--all` không báo gì cho trang; outlink ≥ 1; backlink ≥ 2 (`--backlinks`); không còn `⚠️ Conflict`; không bị flag ở tiêu chí nào của lượt này. Lint **không** đổi `status`; người dùng duyệt danh sách rồi chạy `/promote`.
- **Triage `_inbox.md`**: mỗi mục còn tồn đề xuất đúng 1 trong 3 kết cục — nâng thành trang, gộp vào trang đã có, hoặc xoá (§11). Người dùng quyết định.

**5. Ghi 1 mục vào cuối `log.md`** (§12): `## [<giờ>] lint | <số trang> trang`, tối đa 3 dòng: số lỗi theo loại, số trang đủ điều kiện `stable`, đường dẫn báo cáo. Giờ lấy bằng `python .claude/.claude/hooks/validate_wiki_page.py --now`.

## Lưu ý

- Đếm backlink bằng `--backlinks <trang>`, không grep tay: `grep "[[<trang>]]"` sai cả hai chiều vì `[[...]]` bị hiểu là bracket expression, và bỏ sót dạng `[[trang|nhãn]]`.
- `--stub-debt` lấy thời điểm tạo stub từ commit git đầu tiên thêm file; stub chưa commit dùng mtime. Stub vừa tạo trong lượt chưa commit vì thế có thể bị đếm thiếu, không bị đếm thừa.
