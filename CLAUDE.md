# LLM Wiki — Macroeconomics

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
|---|---|---|
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái ingest | `03_state/` | Agent sở hữu, máy đọc được — tách khỏi `01_sources/` để luật bất biến không cần ngoại lệ |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

Điều hướng nội dung: `02_wiki/index.md` (mục `## Sources` cho trạng thái ingest từng nguồn). Nhật ký thao tác: `log.md` (định dạng §12). Lý do các quyết định thiết kế: `decisions.md`. Ý tưởng dang dở: `_inbox.md` (§11). Tiến độ ingest theo chunk của nguồn dài: `03_state/<nguồn>.md` (§10).

## Năm operation

Quy trình thực thi nằm trong skill, nạp theo nhu cầu:

| Operation | Skill | Cần `00_schema.md`? |
|---|---|---|
| Nạp nguồn mới vào wiki | `/ingest` | Có (§1, §2, §4–§12) |
| Hỏi đáp trên wiki | `/query` | **Không** — tiết kiệm token |
| Kiểm tra sức khoẻ wiki | `/lint` | Có (§4–§9, §11, §12) |
| Nâng `draft` → `stable` sau khi người dùng duyệt | `/promote` | Có (§9, §12) |
| Review trang đối chiếu nguồn, đặt `reviewed_by: model` | `/review` | Có (§7, §8, §9, §10, §12) |

`agents.md` là bản đặc tả tổng quan cho người đọc; skill là bản thực thi.

## Luật cứng — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Phát hiện conflict → đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Cần người dùng xác nhận trước khi:** tạo trang `type: analysis`; ghi trang ở bước ingest (bước 0 — duyệt 3–5 ý chính); nâng `draft → stable` (Promote).
5. Mỗi operation ghi đúng 1 mục vào `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; năm điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do**, không dồn thành danh sách "xem thêm" cuối trang (§7).
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc rẻ (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn nguồn (§7).
- Claim từ **nguồn dài** phải kèm chú thích vị trí `(<nguồn>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7.5) — áp dụng cho trang có `last_updated` từ 2026-09-14, không backfill trang cũ. Chỉ chèn link thì **không** nâng `last_updated`.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `agents.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín để thành trang → ghi vào `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.
- Hook `PostToolUse` tự kiểm frontmatter, heading, link chết và chú thích §7.5 mỗi khi `Write|Edit` một file trong `02_wiki/`. Ghi bằng shell thì hook không chạy — chạy `python .claude/hooks/validate_wiki_page.py --all` (cũng là cách duy nhất bắt trang mồ côi). Cảnh báo phải xử lý ngay, không để tồn đến lượt lint.
