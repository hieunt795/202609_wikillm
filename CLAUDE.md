# LLM Wiki — Macroeconomics

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
|---|---|---|
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái nguồn | `03_state/` | Agent sở hữu, máy đọc được: bản kê `_sources_manifest.md` + bản đồ chunk từng nguồn dài |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

Điều hướng nội dung: `02_wiki/index.md` (mục `## Sources` cho trạng thái ingest từng nguồn). Nhật ký thao tác: `log.md` (§12). Lý do các quyết định: `decisions.md`. Ý tưởng dang dở: `_inbox.md` (§11). Báo cáo lint/audit/research: `Claude outputs/` (§3).

## Quy tắc bắt buộc — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá, không đổi ký tự xuống dòng. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Phát hiện conflict → đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Cần người dùng xác nhận trước khi:** tạo trang `type: analysis`; ghi trang ở bước ingest (bước 2 — duyệt 5–10 ý chính và các mục bỏ qua); ghi trang ở research (bản đề xuất gộp, bước 2); nâng `draft → stable` (Promote).
5. Mỗi operation ghi đúng 1 mục vào **cuối** `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.
6. **Mỗi lượt ingest cập nhật `02_wiki/index.md` §Sources và `03_state/<source id>.md`**, kể cả lượt không tạo trang mới. Nguồn mới vào bản kê ngay lượt đầu (§10).

## Bảy operation

Quy trình thực thi nằm trong skill, nạp theo nhu cầu. Skill là nguồn thực thi duy nhất; sửa quy trình thì sửa `SKILL.md` và ghi lý do vào `decisions.md`.

| Operation | Skill | Đầu vào → đầu ra | Đọc `00_schema.md` |
|---|---|---|---|
| Nạp nguồn | `/ingest` | nguồn trong `01_sources/` → 5–10 ý chính chờ duyệt → tối đa 15 trang + stub + `index.md` + `03_state/` | Toàn bộ |
| Nạp văn bản quy phạm | `/ingest-legal` | file `.docx` → cây điều khoản + điểm nghi vấn chờ duyệt → mỗi Điều/Mục phụ lục 1 trang `provision` (nguyên văn, block ID, link dẫn chiếu) + mục lục + `index.md` + `03_state/`; chú giải viết lượt riêng (≤ 15 node) | §1, §3, §10, §12, §13 |
| Hỏi đáp | `/query` | câu hỏi → câu trả lời; tuỳ chọn 1 trang `analysis` (cần xác nhận) | Không; chỉ §1, §7, §8, §12 khi tạo trang |
| Kiểm tra sức khoẻ | `/lint` | toàn bộ `02_wiki/` + `_inbox.md` → báo cáo, triage inbox, danh sách *Đủ điều kiện `stable`* | §4–§9, §11, §12 |
| Nâng `draft → stable` | `/promote` | danh sách người dùng đã duyệt → đổi `status` | §7.5, §9, §12 |
| Review đối chiếu nguồn | `/review-node` | trang chỉ định hoặc hàng đợi (≤ 5 trang) → `reviewed_by: model`, sửa claim sai | §7–§10, §12 |
| Đào sâu vùng tri thức | `/research` | chủ đề → map subcluster (`research-map-<chủ đề>.md`); trang/sub → deep read 1 sub (≤ 15 đọc, ≤ 7 enrich) → proposal gộp chờ duyệt → claim mới từ chunk `[x]`, link, conflict, tuỳ chọn `analysis` + báo cáo gap | Không khi đề xuất; §7, §9, §10 (+ §1, §8 nếu tạo `analysis`) khi ghi |

Ingest, query, lint, research dùng mẫu **hai lượt**: lượt 1 quét frontmatter (rẻ), lượt 2 chỉ mở full content trang đã xác định là cần. Đây là cơ chế kiểm soát token chính.

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; những điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do, không dồn thành danh sách; không mở đầu bullet** (§7). Hook coi danh sách đó là "xem thêm", lồng link vào câu diễn giải.
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn (§7). Áp skill `writing-style` profile wiki.
- `sources:` dùng **source id**, bắt buộc inline list `[id1, id2]` — hook đọc theo dòng, không hiểu YAML nhiều dòng (§1, §10).
- Claim từ **nguồn dài** kèm chú thích `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim; áp cho `last_updated ≥ 2026-09-14` (§7.5). Chỉ link/chú thích → không nâng `last_updated`.
- Trang **`type: provision`** (điều khoản văn bản quy phạm) do script sinh từ `.docx`: **không sửa tay** phần trước dòng *Chú giải*; các luật viết lại/heading/chú thích `d.x–y` ở trên không áp cho loại này (§13).

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>`:

| Lệnh | Dùng khi |
|---|---|
| *(hook tự chạy)* | Mỗi lần Write/Edit file trong `02_wiki/`: frontmatter, heading, link chết, source id, chú thích §7.5 |
| `--all` | Ghi bằng shell (hook không chạy); cách duy nhất bắt trang mồ côi. **Bắt buộc** trước khi ghi log ở ingest, query (khi tạo trang), promote, review-node, research (khi ghi trang), và ở bước 0 của lint |
| `--verify-sources` | Bước 0 lint; bất cứ khi nào nghi `01_sources/` bị đổi |
| `--backlinks [<trang>]` | Đếm/liệt kê backlink (không grep tay) |
| `--ocr` · `--stub-debt` · `--inbox-debt` | Tiêu chí lint tương ứng |
| `--coverage [<source id>]` | Mục nguồn chưa trang nào trích; **bắt buộc** trước khi đánh chunk `[x]` (ingest bước 7) và ở bước 0 lint |
| `--size [<trang>]` | Trang > 1.000 từ hoặc đoạn > 250 từ; gợi ý tách (§4, §5). Chạy trước khi merge/enrich (ingest bước 4, research Pha 2) |
| `--tags [<từ khoá>]` | Tag + số trang dùng, tổng tag và số tag dùng 1 lần. Kiểm cơ sở tag khi ingest (ingest bước 3) |
| `--style [<trang>]` | Cộm cấm B2, filler I4, bold ≥ 5, fake-heading; luật 6: giọng khuyến nghị, nhấn mạnh tầm quan trọng, tự quy chiếu (§7.6, §7). Chạy trước khi ghi trang (ingest bước 9, research Pha 3) |
| `--now` | Giờ Việt Nam cho `log.md` |

Cảnh báo của hook phải xử lý ngay, không để tồn đến lượt lint.

`python .claude/hooks/legal_docx.py <docx> <lệnh>` — đọc văn bản quy phạm từ `.docx` cho `/ingest-legal` (§13): `--tree` · `--refs` · `--check-formulas` khảo sát; `--write 02_wiki` ghi trang; `--verify 02_wiki` so từng trang với bản sinh từ nguồn (**bắt buộc** sau mỗi lần ghi hoặc viết chú giải); `--state` sinh bảng node.

## Công cụ ghi câu hỏi theo yêu cầu

`python "Claude outputs/log_questions.py"` — chỉ chạy thủ công (local-only, gitignored); quét session `cwd` → phân loại user message → append `.claude/local/question-logger/questions.jsonl`. Tùy chọn: `--input <file.json|jsonl>`, `--dry-run`.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín → `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.

## Trạng thái phiên làm việc

Không ghi trạng thái vào file này (nạp mọi lượt → tốn token). Đầu session: đọc handoff mới nhất trong `.claude/session_handoffs/` + `02_wiki/index.md` §Sources.

