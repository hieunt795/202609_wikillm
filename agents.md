# Agents — Tổng quan vận hành LLM Wiki

> File này là **bản đặc tả tổng quan cho người đọc**. Quy trình thực thi chi tiết nằm trong skill (`.claude/skills/`) — Claude Code nạp chúng theo nhu cầu, nên không lặp lại nội dung ở đây.
>
> Nguyên tắc cũ vẫn giữ: không lặp lại nội dung đã có trong `00_schema.md` — chỉ trích dẫn mục cần đọc.

## Ba operation

| Operation | Skill (nguồn thực thi) | Đầu vào | Đầu ra | Cần `00_schema.md`? |
|---|---|---|---|---|
| **Ingest** | `.claude/skills/ingest/SKILL.md` | Nguồn mới trong `01_sources/`; file trạng thái `03_state/<nguồn>.md` (§10) | 5–15 trang `02_wiki/` + stub + cập nhật `index.md` (§Sources + mục lục) + cập nhật `03_state/<nguồn>.md` + 1 dòng `log.md` | Có — §1, §2, §4–§11 |
| **Query** | `.claude/skills/query/SKILL.md` | Câu hỏi của người dùng | Câu trả lời tổng hợp; tuỳ chọn 1 trang `analysis` (cần xác nhận) | **Không** |
| **Lint** | `.claude/skills/lint/SKILL.md` | Toàn bộ `02_wiki/` + `_inbox.md` | Báo cáo lỗi + danh sách triage inbox + 1 dòng `log.md` | Có — §4–§9, §11 |

Cả ba đều dùng mẫu **hai lượt**: lượt 1 quét frontmatter (rẻ), lượt 2 chỉ mở full content những trang đã xác định là cần. Đây là cơ chế kiểm soát token chính của dự án.

## Ràng buộc chung cho mọi operation

1. `01_sources/` bất biến — không bao giờ sửa nội dung nguồn, và không ghi bất cứ file nào vào đó. Trạng thái ingest đi ra `03_state/` (§3, §10).
2. Mâu thuẫn: không tự sửa. Đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn (§4).
3. Lint chỉ báo cáo, không tự sửa.
4. Trang `type: analysis` cần người dùng xác nhận trước khi tạo.
5. Mỗi operation append đúng 1 dòng vào `log.md`.
6. **Mỗi lượt ingest phải cập nhật mục `## Sources` trong `02_wiki/index.md` và file trạng thái `03_state/<nguồn>.md`** — kể cả lượt không tạo trang mới. Trạng thái nguồn đọc được từ bảng, không phải từ việc diễn giải lại văn xuôi trong `log.md` (§10).
7. Claim lấy từ nguồn dài kèm chú thích vị trí trong nguồn (§7.5), áp dụng từ lượt ingest kế tiếp trở đi.

## Ghi chú vận hành

- Không sửa `agents.md` / `00_schema.md` / skill vụn vặt từng lần — gộp thay đổi theo batch để giữ nội dung ổn định (hỗ trợ prompt caching).
- Không bao giờ sửa nội dung trong `01_sources/`, và không thêm file nào vào đó — kể cả file do agent sở hữu (§3).
- Ý tưởng/insight chưa đủ chín thành trang evergreen → `_inbox.md` ở gốc dự án, tách khỏi `02_wiki/` (§11). Triage mỗi lượt lint, mỗi mục có đúng 3 kết cục: nâng thành trang, gộp vào trang đã có, hoặc xoá.
- Hook `PostToolUse` (`.claude/hooks/validate_wiki_page.py`) tự kiểm frontmatter, wikilink, link chết, luật không-heading, chú thích §7.5 và quy ước title §8 mỗi khi ghi file trong `02_wiki/`. Cảnh báo hook phải xử lý ngay, không để dồn tới lượt lint.
- **Hook chỉ bắt được tool `Write|Edit`.** File ghi bằng shell đi vòng qua nó. Sau mỗi lượt ghi file bằng shell, chạy `python .claude/hooks/validate_wiki_page.py --all` để quét lại toàn bộ.

## Khi sửa quy trình

Sửa trong `SKILL.md` tương ứng — đó là nguồn thực thi duy nhất. File này chỉ cập nhật khi thay đổi ảnh hưởng tới bức tranh tổng thể (thêm/bớt operation, đổi ràng buộc chung).
