# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## LLM Wiki — Macroeconomics

Ký hiệu `§N` trong file này trỏ tới mục N của `00_schema.md`.

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
| --- | --- | --- |
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái nguồn | `03_state/` | Agent sở hữu, máy đọc được: bản kê `_sources_manifest.md` + bản đồ chunk từng nguồn dài |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

`01_sources/` và `Claude outputs/` không nằm trong git. Thiếu `01_sources/` thì ingest, review-node và `--verify-sources` không chạy được.

| Cần gì | File |
| --- | --- |
| Điều hướng nội dung, trạng thái ingest từng nguồn | `02_wiki/index.md` (trạng thái ở mục `## Sources`) |
| Nhật ký thao tác | `log.md` (§12) |
| Lý do các quyết định | `decisions.md` |
| Ý tưởng dang dở | `_inbox.md` (§11) |
| Báo cáo lint, audit, research | `Claude outputs/` (§3) |

## Quy tắc bắt buộc — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá, không đổi ký tự xuống dòng. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Khi phát hiện conflict, đánh dấu `⚠️ Conflict` kèm cả hai claim và nguồn, rồi chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Cần người dùng xác nhận trước khi:**
   - tạo trang `type: analysis`;
   - ghi trang ở ingest (bước 2 — duyệt 5–10 ý chính và các mục bỏ qua);
   - ghi trang ở research (Pha 3 — bản đề xuất gộp);
   - nâng `draft → stable` (promote).
5. Mỗi operation ghi đúng 1 mục vào **cuối** `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.
6. **Mỗi lượt ingest cập nhật mục `## Sources` của `02_wiki/index.md` và `03_state/<source id>.md`**, kể cả lượt không tạo trang mới. Nguồn mới vào bản kê ngay lượt đầu (§10).

## Khởi động

File này và `00_schema.md` cùng là lớp schema của dự án (mô hình Karpathy). File này chỉ giữ phần phải thấy mọi lượt; quy ước và luồng vận hành nằm ở `00_schema.md`.

1. **Đầu phiên** — đọc handoff mới nhất trong `.claude/session_handoffs/` và mục `## Sources` của `02_wiki/index.md`. Không ghi trạng thái phiên vào file này.
2. **Trước mọi operation** (`/ingest`, `/query`, `/lint`, `/promote`, `/review-node`, `/research`) — đọc `00_schema.md` §13: trình tự một phiên, bảng operation, mục schema cần đọc thêm, điểm dừng chờ duyệt. Sau đó mới chạy skill.

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; những điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do, không dồn thành danh sách; không mở đầu bullet** (§7). Hook báo lỗi danh sách link kiểu "xem thêm"; cách sửa là lồng từng link vào câu diễn giải.
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn (§7). Áp skill `writing-style` profile wiki.
- `sources:` dùng **source id**, bắt buộc inline list `[id1, id2]` — hook đọc theo dòng, không hiểu YAML nhiều dòng (§1, §10).
- Claim từ **nguồn dài** kèm chú thích `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7 luật 5). Luật áp cho trang có `last_updated` từ 2026-09-14 trở đi.
- Lượt sửa chỉ thêm link hoặc chú thích thì không nâng `last_updated`.

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>` — chi tiết từng lệnh: `--help`. Hook cũng tự chạy sau mỗi Write/Edit trong `02_wiki/` (frontmatter, heading, link chết, source id, chú thích theo §7 luật 5). Exit 2 nghĩa là có vấn đề: xử lý ngay, không để tồn đến lượt lint. Không có lệnh kiểm riêng một trang; kiểm bằng tay thì dùng `--all`.

Bắt buộc:

| Lệnh | Khi nào |
| --- | --- |
| `--all` | Trước khi ghi log ở ingest, query (khi tạo trang), promote, review-node, research (khi ghi trang); bước 0 lint. Cách duy nhất bắt trang mồ côi và file ghi bằng shell |
| `--coverage [<source id>]` | Trước khi đánh chunk `[x]` ở ingest; bước 0 lint |
| `--verify-sources` | Bước 0 lint; bất cứ khi nào nghi `01_sources/` bị đổi |
| `--now` | Lấy giờ Việt Nam cho `log.md` |

Theo nhu cầu:

- `--backlinks [<trang>]` — đếm/liệt kê backlink (không grep tay).
- `--size [<trang>]` — trang trên 1.000 từ hoặc đoạn trên 250 từ; chạy trước khi merge/enrich (§4, §5).
- `--tags [<từ khoá>]` — tag đang có + số trang dùng; kiểm trước khi đặt tag mới ở ingest (§6).
- `--style [<trang>]` — tín hiệu thô về văn phong và §7 luật 6; chạy trên trang vừa viết ở ingest và research.
- `--ocr`, `--stub-debt`, `--inbox-debt` — tiêu chí lint tương ứng.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín thì ghi vào `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.
- `python "Claude outputs/log_questions.py"` — ghi câu hỏi của người dùng vào `.claude/local/question-logger/questions.jsonl`; chỉ chạy khi người dùng yêu cầu (local-only). Tuỳ chọn: `--input <file.json|jsonl>`, `--dry-run`.
