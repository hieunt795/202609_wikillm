---
name: lint
description: Kiểm tra sức khoẻ wiki 02_wiki — trang mồ côi, mâu thuẫn tồn đọng, trang stale, trùng lặp, vi phạm Atomic, vi phạm quy ước title, nợ stub, sai vòng đời status, nhiễu OCR còn sót từ nguồn, nợ inbox chưa triage. Dùng khi người dùng muốn lint, kiểm tra wiki, rà soát, health check, tìm trang mồ côi, kiểm tra liên kết, audit wiki, dọn dẹp wiki.
---

# Lint — kiểm tra sức khoẻ wiki

Chạy sau mỗi 10 lượt ingest hoặc theo lịch (§4). Kiểm tra chi tiết luật ở `00_schema.md` §5–§9, §11.

**Lint chỉ báo cáo. Tuyệt đối không tự sửa.** Xuất báo cáo, chờ người xác nhận hướng xử lý.

## Quy trình hai lượt

**1. Lượt rẻ — quét frontmatter toàn bộ `02_wiki/`.** Không đọc full content.

**2. Đối chiếu 10 tiêu chí:**

| Lỗi | Cách phát hiện |
|---|---|
| Trang mồ côi | outlink = 0 (không có `[[wikilink]]` nào trong thân bài) **HOẶC** backlink = 0 (không trang nào trỏ tới). Tiêu chí outlink **không** áp cho `status: stub` |
| Mâu thuẫn tồn đọng | còn `⚠️ Conflict` chưa xử lý |
| Trang stale | `last_updated` cũ hơn nguồn liên quan đã ingest sau đó |
| Trùng lặp entity | hai trang cùng mô tả một thực thể |
| Vi phạm Atomic | thân bài có heading cấp 2+, hoặc `[[wikilink]]` dồn thành danh sách "xem thêm" không kèm lý do (§5, §7) |
| Vi phạm title | `case`/`analysis` đặt title danh từ thay vì câu khẳng định; title phủ định; title mơ hồ (§8) |
| Nợ stub | `status: stub` chưa được ingest nội dung sau 3 lượt ingest kể từ khi tạo (§9) |
| Sai vòng đời status | `stable` nhưng có nguồn mới ingest sau `last_updated` mà chưa chuyển `stale` (§9) |
| Nhiễu OCR còn sót | thân bài chứa token đặc trưng lỗi OCR bị copy nguyên từ nguồn — xem bộ mẫu bên dưới |
| Nợ inbox | mục trong `_inbox.md` chưa được triage sau 3 lượt lint (§11) |

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

Kèm mục **triage `_inbox.md`**: liệt kê từng mục còn tồn, mỗi mục đề xuất đúng 1 trong 3 kết cục — nâng thành trang wiki, gộp vào trang đã có, hoặc xoá (§11). Lint chỉ đề xuất; người dùng quyết định và thực hiện.

**5. Append 1 dòng vào `log.md`:** `[YYYY-MM-DD] lint <số trang quét> → <tóm tắt số lỗi theo loại>`.

## Lưu ý về chi phí

Wiki hiện có 51 trang (~81 KB). Lượt 1 quét frontmatter toàn bộ vẫn rẻ. Khi wiki vượt ~200 trang, cân nhắc giao lượt 1 cho subagent `Explore` để không đổ toàn bộ kết quả quét vào context chính — nhưng chỉ làm khi người dùng yêu cầu rõ.

Tiêu chí backlink cần quét chéo toàn bộ `02_wiki/`: grep `[[<tên-trang>]]` một lượt cho tất cả trang, không grep từng trang một.

Tiêu chí nhiễu OCR cũng chạy bằng grep một lượt trên cả thư mục — không mở full content chỉ để quét. Trang nào có hit mới mở ở lượt 3 để xác nhận (tên riêng nước ngoài dễ báo giả: `Paasche` khớp mẫu nguyên-âm-nhân-đôi nhưng là tên người có thật).
