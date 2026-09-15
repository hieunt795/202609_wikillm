---
name: lint
description: Kiểm tra sức khoẻ wiki 02_wiki — trang mồ côi, link chết, khái niệm chưa có trang, trang đủ điều kiện stable, mâu thuẫn tồn đọng, trang stale, trùng lặp, vi phạm Atomic, vi phạm quy ước title, nợ stub, sai vòng đời status, nhiễu OCR còn sót từ nguồn, nợ inbox chưa triage. Dùng khi người dùng muốn lint, kiểm tra wiki, rà soát, health check, tìm trang mồ côi, kiểm tra liên kết, audit wiki, dọn dẹp wiki.
---

# Lint — kiểm tra sức khoẻ wiki

Chạy sau mỗi 10 lượt ingest hoặc theo lịch (§4). Kiểm tra chi tiết luật ở `00_schema.md` §5–§9, §11.

**Lint chỉ báo cáo. Tuyệt đối không tự sửa.** Xuất báo cáo, chờ người xác nhận hướng xử lý.

## Quy trình hai lượt

**0. Chạy trình kiểm trang hàng loạt trước mọi thứ khác:**

```bash
python .claude/hooks/validate_wiki_page.py --all
```

Hook `PostToolUse` chỉ bắt tool `Write|Edit` — file ghi bằng shell (`cat >`, script, `sed -i`) đi vòng qua nó. Chế độ `--all` quét lại tất cả.

**Script phủ:** frontmatter đủ trường, `type`/`status` hợp lệ, tên file khớp title, `sources` không rỗng, `last_updated` đúng dạng ngày, heading trong thân bài, **link chết** (kể cả dạng `[[trang|nhãn]]`), link dồn thành danh sách, chú thích §7.5 với trang có `last_updated` từ 2026-09-14, title §8 dạng danh từ cho `case`/`analysis`, và **trang mồ côi theo chiều backlink**.

**Script không phủ** — phải kiểm tay ở bước 2: mâu thuẫn tồn đọng, trang stale, trùng lặp entity, khái niệm chưa có trang, nợ stub, sai vòng đời status, nhiễu OCR, nợ inbox, danh sách đủ điều kiện `stable`.

**1. Lượt rẻ — quét frontmatter toàn bộ `02_wiki/`.** Không đọc full content.

**2. Đối chiếu 12 tiêu chí:**

| Lỗi | Cách phát hiện |
|---|---|
| Trang mồ côi | outlink = 0 (không có `[[wikilink]]` nào trong thân bài) **HOẶC** backlink = 0 (không trang nào trỏ tới). Tiêu chí outlink **không** áp cho `status: stub`. Cả hai vế do bước 0 kiểm |
| Link chết | `[[x]]` hoặc `[[x\|nhãn]]` trỏ tới trang không tồn tại (§6). Bước 0 kiểm |
| Khái niệm chưa có trang | một thuật ngữ được nhắc trong thân bài của **≥3 trang** mà chưa có trang riêng (§6, stub link). Đề xuất tạo `status: stub` rồi chèn link từ các trang đó |
| Mâu thuẫn tồn đọng | còn `⚠️ Conflict` chưa xử lý |
| Trang stale | `last_updated` cũ hơn nguồn liên quan đã ingest sau đó |
| Trùng lặp entity | hai trang cùng mô tả một thực thể |
| Vi phạm Atomic | thân bài có heading cấp 2+, hoặc `[[wikilink]]` dồn thành danh sách "xem thêm" không kèm lý do (§5, §7) |
| Vi phạm title | `case`/`analysis` đặt title danh từ thay vì câu trần thuật; title mơ hồ hoặc không mô tả toàn bộ nội dung trang (§8). Title phủ định **không** phải lỗi (§8 luật 1) |
| Nợ stub | `status: stub` chưa được ingest nội dung sau 3 lượt ingest kể từ khi tạo (§9) |
| Sai vòng đời status | `stable` nhưng có nguồn mới ingest sau `last_updated` mà chưa chuyển `stale` (§9) |
| Nhiễu OCR còn sót | thân bài chứa token đặc trưng lỗi OCR bị copy nguyên từ nguồn — xem bộ mẫu bên dưới |
| Nợ inbox | mục trong `_inbox.md` chưa được triage sau 3 lượt lint (§11) |

Tiêu chí **Khái niệm chưa có trang** không có lệnh tự động: đọc lướt thân bài các trang ở lượt 3, ghi lại thuật ngữ lặp lại chưa có `[[link]]`, rồi đếm số trang bằng `grep -li "<thuật ngữ>" 02_wiki/*.md --exclude=index.md`. Cẩn thận nghĩa đồng âm: "thâm hụt" có thể là thâm hụt vãng lai hoặc thâm hụt ngân sách — đếm theo khái niệm, không theo chuỗi.

Tiêu chí **Nhiễu OCR** cần quét thân bài (không phải frontmatter), và **bỏ `[[wikilink]]` ra khỏi phạm vi quét** — tên trang kebab-case không phải văn bản. Sáu họ mẫu:

| Họ mẫu | Ví dụ trong nguồn IMF |
|---|---|
| `l` / `O` đứng thay chữ số hoặc chữ `I` hoa | `lmbalance`, `tO`, `DeficitlO` |
| Số chú thích cuối chương dính vào từ | `Economiesl3`, `lmbalance12` |
| Chữ số bị tách bởi khoảng trắng | `1 993`, `1 989` |
| HOA–thường lẫn trong một từ | `COLmtries` |
| Nguyên âm nhân đôi bất thường | `Waaes` (wages) |
| Rác markdown của bản OCR bị copy | `<sup>`, `<span id=`, `[#page-`, ký tự thay thế `�` |

**Giới hạn đã biết:** bộ mẫu không bắt được lỗi OCR tạo ra *từ có thật* (`set our` thay `set out`, `Governmenr` thay `Government`) — loại này chỉ lộ ra khi đọc. Đây là lý do tiêu chí chỉ là lưới lọc thô, không phải bảo chứng.

Nhiễu OCR là **lỗi sao chép nguyên văn**: nếu một token OCR lọt được vào trang wiki thì câu chứa nó gần như chắc chắn vi phạm luật viết lại bằng lời mình (§7.4). Báo cáo kèm cả hai lỗi.

**3. Lượt đắt — chỉ mở full content các trang bị flag ở lượt 2.**

**4. Xuất báo cáo** nhóm theo loại lỗi, mỗi mục nêu trang + lý do + hướng sửa đề xuất. Không thực hiện sửa.

Kèm mục **Đủ điều kiện `stable`** (§9): liệt kê mọi trang `status: draft` thoả **đồng thời** — bước 0 không báo vấn đề gì cho trang đó; outlink ≥ 1; backlink ≥ 2; không còn `⚠️ Conflict`; không bị flag ở bất kỳ tiêu chí nào của lượt lint này. Lint **không** đổi `status`; danh sách này chuyển cho người dùng duyệt rồi chạy `/promote`.

Kèm mục **triage `_inbox.md`**: liệt kê từng mục còn tồn, mỗi mục đề xuất đúng 1 trong 3 kết cục — nâng thành trang wiki, gộp vào trang đã có, hoặc xoá (§11). Lint chỉ đề xuất; người dùng quyết định và thực hiện.

**5. Ghi 1 mục vào `log.md`** theo định dạng `00_schema.md` §12: `## [YYYY-MM-DD:hh-MM-ss] lint | <số trang quét> trang`, kèm tối đa 3 dòng tóm tắt số lỗi theo loại và số trang đủ điều kiện `stable`.

## Lưu ý về chi phí

Ở quy mô vài chục trang (dưới ~150 KB toàn thư mục), lượt 1 quét frontmatter toàn bộ vẫn rẻ. Số trang hiện tại lấy từ `02_wiki/index.md`, không ghi cứng ở đây. Khi wiki vượt ~200 trang, cân nhắc giao lượt 1 cho subagent `Explore` để không đổ toàn bộ kết quả quét vào context chính — nhưng chỉ làm khi người dùng yêu cầu rõ.

Tiêu chí backlink đã do bước 0 tính cho toàn đồ thị. Khi cần truy một trang cụ thể, **dùng đúng lệnh này** — `grep "[[<tên-trang>]]"` là SAI cả hai chiều vì `[[...]]` bị hiểu là bracket expression (`types-of-inflation` ra 0 file dù có 3 trang trỏ tới; `real-wages` ra 52/52 file):

```bash
grep -rlE "\[\[<tên-trang>(\||\])" 02_wiki/ --exclude=index.md
```

`-E` cộng `\[` thoát nghĩa để `[[` là chuỗi thật; nhánh `(\||\])` bắt cả `[[tên-trang]]` lẫn `[[tên-trang|nhãn]]` (§6); `--exclude=index.md` để mục lục không bị tính thành backlink.

Tiêu chí nhiễu OCR cũng chạy bằng grep một lượt trên cả thư mục — không mở full content chỉ để quét. Trang nào có hit mới mở ở lượt 3 để xác nhận (tên riêng nước ngoài dễ báo giả: `Paasche` khớp mẫu nguyên-âm-nhân-đôi nhưng là tên người có thật).
