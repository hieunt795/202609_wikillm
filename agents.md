# Agents — Tổng quan vận hành LLM Wiki

> File này là **bản đặc tả tổng quan cho người đọc**. Quy trình thực thi chi tiết nằm trong skill (`.claude/skills/`) — Claude Code nạp chúng theo nhu cầu, nên không lặp lại nội dung ở đây.
>
> Nguyên tắc cũ vẫn giữ: không lặp lại nội dung đã có trong `00_schema.md` — chỉ trích dẫn mục cần đọc.

## Bốn operation

| Operation | Skill (nguồn thực thi) | Đầu vào | Đầu ra | Cần `00_schema.md`? |
|---|---|---|---|---|
| **Ingest** | `.claude/skills/ingest/SKILL.md` | Nguồn mới trong `01_sources/`; file trạng thái `03_state/<nguồn>.md` (§10) | 3–5 ý chính chờ duyệt → 5–15 trang `02_wiki/` + stub + cập nhật `index.md` (§Sources + mục lục) + cập nhật `03_state/<nguồn>.md` + 1 mục `log.md` | Có — §1, §2, §4–§12 |
| **Query** | `.claude/skills/query/SKILL.md` | Câu hỏi của người dùng | Câu trả lời tổng hợp; tuỳ chọn 1 trang `analysis` (cần xác nhận) | **Không** |
| **Lint** | `.claude/skills/lint/SKILL.md` | Toàn bộ `02_wiki/` + `_inbox.md` | Báo cáo lỗi + triage inbox + danh sách *Đủ điều kiện `stable`* + 1 mục `log.md` | Có — §4–§9, §11, §12 |
| **Promote** | `.claude/skills/promote/SKILL.md` | Danh sách *Đủ điều kiện `stable`* đã được người dùng duyệt | Đổi `status: draft → stable` + 1 mục `log.md` | Có — §9, §12 |

Ingest, Query, Lint đều dùng mẫu **hai lượt**: lượt 1 quét frontmatter (rẻ), lượt 2 chỉ mở full content những trang đã xác định là cần. Đây là cơ chế kiểm soát token chính của dự án.

## Ràng buộc chung cho mọi operation

1. `01_sources/` bất biến — không bao giờ sửa nội dung nguồn, và không ghi bất cứ file nào vào đó. Trạng thái ingest đi ra `03_state/` (§3, §10).
2. Mâu thuẫn: không tự sửa. Đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn (§4).
3. Lint chỉ báo cáo, không tự sửa.
4. Cần người dùng xác nhận trước khi: tạo trang `type: analysis`; ghi trang khi ingest (bước 0); nâng `draft → stable`.
5. Mỗi operation ghi đúng 1 mục vào `log.md` theo định dạng §12 — không chứa lập luận; lý do quyết định nằm ở `decisions.md` hoặc trong schema.
6. **Mỗi lượt ingest phải cập nhật mục `## Sources` trong `02_wiki/index.md` và file trạng thái `03_state/<nguồn>.md`** — kể cả lượt không tạo trang mới. Trạng thái nguồn đọc được từ bảng, không phải từ việc diễn giải lại văn xuôi trong `log.md` (§10).
7. Claim lấy từ nguồn dài kèm chú thích vị trí trong nguồn (§7.5), áp dụng từ lượt ingest kế tiếp trở đi.

## Ghi chú vận hành

- Không sửa `agents.md` / `00_schema.md` / skill vụn vặt từng lần — gộp thay đổi theo batch để giữ nội dung ổn định (hỗ trợ prompt caching).
- Không bao giờ sửa nội dung trong `01_sources/`, và không thêm file nào vào đó — kể cả file do agent sở hữu (§3).
- Ý tưởng/insight chưa đủ chín thành trang evergreen → `_inbox.md` ở gốc dự án, tách khỏi `02_wiki/` (§11). Triage mỗi lượt lint, mỗi mục có đúng 3 kết cục: nâng thành trang, gộp vào trang đã có, hoặc xoá.
- Hook `PostToolUse` (`.claude/hooks/validate_wiki_page.py`) tự kiểm frontmatter, luật không-heading, link chết và chú thích §7.5 mỗi khi `Write|Edit` một file trong `02_wiki/`. Chế độ `--all` quét cả thư mục và bắt thêm trang mồ côi — bắt buộc chạy trước khi ghi log ở ingest, query (khi tạo trang), promote, và ở bước 0 của lint. Cảnh báo hook phải xử lý ngay, không để dồn tới lượt lint.

## Khi sửa quy trình

Sửa trong `SKILL.md` tương ứng — đó là nguồn thực thi duy nhất. File này chỉ cập nhật khi thay đổi ảnh hưởng tới bức tranh tổng thể (thêm/bớt operation, đổi ràng buộc chung). Ghi lý do thay đổi vào `decisions.md`.
