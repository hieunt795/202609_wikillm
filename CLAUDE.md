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

Ba lớp chỉ dẫn, mỗi quy tắc chỉ nằm ở một nơi: file này giữ phần phải thấy mọi lượt; `00_schema.md` §1–§12 mô tả wiki trông như thế nào; mỗi `SKILL.md` trong `.claude/skills/` là quy trình từng bước của một operation. Khi lệch nhau, ưu tiên theo thứ tự file này, `00_schema.md`, skill, và báo người dùng chỗ lệch.

1. **Đầu phiên** — hook `SessionStart` đã nạp handoff mới nhất; đọc thêm mục `## Sources` của `02_wiki/index.md`. Không ghi trạng thái phiên vào file này.
2. **Mỗi operation** (`/ingest`, `/query`, `/lint`, `/promote`, `/review-node`, `/research`) — chạy skill tương ứng. Đầu mỗi skill nêu mục schema cần đọc, điểm dừng chờ duyệt và việc ghi log; không đọc `00_schema.md` trước khi skill yêu cầu.
3. **Cuối phiên có thay đổi repo** — nhắc người dùng gọi `/handoff`; không tự tạo handoff.

Quy ước viết trang wiki được nạp từ `.claude/rules/wiki-pages.md` khi chạm file trong `02_wiki/`.

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>` — chi tiết từng lệnh: `--help`. Hook cũng tự chạy sau mỗi Write/Edit trong `02_wiki/` (frontmatter, heading, link chết, source id, chú thích theo §7 luật 5). Exit 2 nghĩa là có vấn đề: xử lý ngay, không để tồn đến lượt lint. Không có lệnh kiểm riêng một trang; kiểm bằng tay thì dùng `--all`.

Bắt buộc:

| Lệnh | Khi nào |
| --- | --- |
| `--all` | Trước khi ghi log ở ingest, query (khi tạo trang), promote, review-node, research (khi ghi trang); bước 0 lint. Cách duy nhất bắt trang mồ côi và file ghi bằng shell |
| `--coverage [<source id>]` | Trước khi đánh chunk `[x]` ở ingest; bước 0 lint |
| `--verify-sources` | Bước 0 lint; bất cứ khi nào nghi `01_sources/` bị đổi |
| `--now` | Lấy giờ Việt Nam cho `log.md` |

Các lệnh theo nhu cầu (`--backlinks`, `--size`, `--tags`, `--style`, `--ocr`, `--stub-debt`, `--inbox-debt`): xem `--help`; skill nêu lúc nào cần chạy.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- `python "Claude outputs/log_questions.py"` — ghi câu hỏi của người dùng vào `.claude/local/question-logger/questions.jsonl`; chỉ chạy khi người dùng yêu cầu (local-only). Tuỳ chọn: `--input <file.json|jsonl>`, `--dry-run`.
