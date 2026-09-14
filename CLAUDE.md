# LLM Wiki — Macroeconomics

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
|---|---|---|
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái ingest | `03_state/` | Agent sở hữu, máy đọc được — tách khỏi `01_sources/` để luật bất biến không cần ngoại lệ |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

Điều hướng nội dung: `02_wiki/index.md` (mục `## Sources` cho trạng thái ingest từng nguồn). Nhật ký thao tác: `log.md`. Ý tưởng dang dở: `_inbox.md` (§11). Tiến độ ingest theo chunk của nguồn dài: `03_state/<nguồn>.md` (§10).

## Ba operation

Quy trình thực thi nằm trong skill, nạp theo nhu cầu:

| Operation | Skill | Cần `00_schema.md`? |
|---|---|---|
| Nạp nguồn mới vào wiki | `/ingest` | Có (§1, §2, §4–§11) |
| Hỏi đáp trên wiki | `/query` | **Không** — tiết kiệm token |
| Kiểm tra sức khoẻ wiki | `/lint` | Có (§4–§9, §11) |

`agents.md` là bản đặc tả tổng quan cho người đọc; skill là bản thực thi.

## Luật cứng — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Phát hiện conflict → đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Trang `type: analysis` cần người xác nhận trước khi tạo.**
5. Mỗi operation append đúng 1 dòng vào `log.md`.

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; năm điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do**, không dồn thành danh sách "xem thêm" cuối trang (§7).
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc rẻ (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn nguồn (§7).
- Claim từ **nguồn dài** phải kèm chú thích vị trí `(<nguồn>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7.5) — áp dụng từ lượt ingest kế tiếp, không backfill 51 trang cũ.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `agents.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín để thành trang → ghi vào `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.
- Hook `PostToolUse` tự kiểm frontmatter và liên kết mỗi khi ghi file trong `02_wiki/`. Cảnh báo từ hook phải xử lý ngay, không để tồn đến lượt lint.
