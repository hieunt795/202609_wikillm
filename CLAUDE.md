# LLM Wiki — Macroeconomics

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
|---|---|---|
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái nguồn | `03_state/` | Agent sở hữu, máy đọc được: bản kê `_sources_manifest.md` + bản đồ chunk từng nguồn dài |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

Điều hướng nội dung: `02_wiki/index.md` (mục `## Sources` cho trạng thái ingest từng nguồn). Nhật ký thao tác: `log.md` (§12). Lý do các quyết định: `decisions.md`. Ý tưởng dang dở: `_inbox.md` (§11). Báo cáo lint/audit: `Claude outputs/` (§3).

## Năm operation

Quy trình thực thi nằm trong skill, nạp theo nhu cầu. Skill là nguồn thực thi duy nhất; sửa quy trình thì sửa `SKILL.md` và ghi lý do vào `decisions.md`.

| Operation | Skill | Đầu vào → đầu ra | Đọc `00_schema.md` |
|---|---|---|---|
| Nạp nguồn | `/ingest` | nguồn trong `01_sources/` → 3–5 ý chính chờ duyệt → 5–15 trang + stub + `index.md` + `03_state/` | Toàn bộ |
| Hỏi đáp | `/query` | câu hỏi → câu trả lời; tuỳ chọn 1 trang `analysis` (cần xác nhận) | Không; chỉ §1, §7, §8, §12 khi tạo trang |
| Kiểm tra sức khoẻ | `/lint` | toàn bộ `02_wiki/` + `_inbox.md` → báo cáo, triage inbox, danh sách *Đủ điều kiện `stable`* | §4–§9, §11, §12 |
| Nâng `draft → stable` | `/promote` | danh sách người dùng đã duyệt → đổi `status` | §7.5, §9, §12 |
| Review đối chiếu nguồn | `/review-node` | trang chỉ định hoặc hàng đợi (≤ 5 trang) → `reviewed_by: model`, sửa claim sai | §7–§10, §12 |

Ingest, query, lint dùng mẫu **hai lượt**: lượt 1 quét frontmatter (rẻ), lượt 2 chỉ mở full content trang đã xác định là cần. Đây là cơ chế kiểm soát token chính.

## Luật cứng — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá, không đổi ký tự xuống dòng. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Phát hiện conflict → đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Cần người dùng xác nhận trước khi:** tạo trang `type: analysis`; ghi trang ở bước ingest (bước 0 — duyệt 3–5 ý chính); nâng `draft → stable` (Promote).
5. Mỗi operation ghi đúng 1 mục vào **cuối** `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.
6. **Mỗi lượt ingest cập nhật `02_wiki/index.md` §Sources và `03_state/<source id>.md`**, kể cả lượt không tạo trang mới. Nguồn mới vào bản kê ngay lượt đầu (§10).

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; những điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do**, không dồn thành danh sách "xem thêm" (§7).
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc rẻ (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn nguồn (§7); thân bài áp skill `writing-style` profile wiki.
- `sources:` dùng **source id** của bản kê (§1, §10), bắt buộc dạng inline list `[id1, id2]` — hook đọc theo dòng, không hiểu YAML nhiều dòng.
- Bullet không được mở đầu bằng `[[wikilink]]` (hook coi là danh sách "xem thêm"); lồng link vào câu diễn giải.
- Claim từ **nguồn dài** kèm chú thích vị trí `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7.5) — áp cho trang có `last_updated` từ 2026-09-14. Chỉ chèn link hoặc chú thích thì **không** nâng `last_updated`.

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>`:

| Lệnh | Dùng khi |
|---|---|
| *(hook tự chạy)* | Mỗi lần Write/Edit file trong `02_wiki/`: frontmatter, heading, link chết, source id, chú thích §7.5 |
| `--all` | Ghi bằng shell (hook không chạy); cách duy nhất bắt trang mồ côi. **Bắt buộc** trước khi ghi log ở ingest, query (khi tạo trang), promote, review-node, và ở bước 0 của lint |
| `--verify-sources` | Bước 0 lint; bất cứ khi nào nghi `01_sources/` bị đổi |
| `--backlinks [<trang>]` | Đếm/liệt kê backlink (không grep tay) |
| `--ocr` · `--stub-debt` · `--inbox-debt` | Tiêu chí lint tương ứng |
| `--now` | Giờ Việt Nam cho `log.md` |

Cảnh báo của hook phải xử lý ngay, không để tồn đến lượt lint.

## Công cụ ghi câu hỏi theo yêu cầu

`python "Claude outputs/log_questions.py"` chỉ chạy khi được gọi thủ công (local-only, gitignored). Mặc định, công cụ quét toàn bộ Codex session có `cwd` thuộc repo hiện tại; `--input <conversation.json|jsonl>` giới hạn vào một file cụ thể. Công cụ lấy message `role=user`, phân loại bằng rule cục bộ, bỏ bản trùng và append vào `.claude/local/question-logger/questions.jsonl`; không gọi LLM. Dùng `--dry-run` để xem record dự kiến mà không ghi file.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín → `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.

## Trạng thái phiên làm việc

Không ghi trạng thái vào file này (nạp mọi lượt → tốn token). Đầu session: đọc handoff mới nhất trong `.claude/session_handoffs/` + `02_wiki/index.md` §Sources.

