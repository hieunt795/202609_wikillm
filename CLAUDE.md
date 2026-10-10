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
| Điều hướng nội dung | `02_wiki/index.md` |
| Nguồn nào nạp tới đâu | `--coverage` (tính từ chú thích trên trang và `03_state/`, §10) |
| Nhật ký thao tác | `log.md` (§12) |
| Lý do các quyết định | `decisions.md` |
| Ý tưởng dang dở | `_inbox.md` (§11) |
| Báo cáo lint, audit, research | `Claude outputs/` (§3) |

## Quy tắc bắt buộc — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá, không đổi ký tự xuống dòng. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự xử lý mâu thuẫn giữa hai nguồn.** Đánh dấu `⚠️ Conflict` kèm cả hai claim và nguồn, rồi chờ người xử lý.
3. **Mọi thay đổi claim trong `02_wiki/` đi qua một lần duyệt danh sách thay đổi**: ý chính và bảng merge ở ingest, proposal ở research, mã mục ở lint, trang `type: analysis` ở query. Ngoại lệ duy nhất: `/review-node` sửa claim cho khớp chính nguồn nó dẫn. Sổ sách agent tự làm, không hỏi: `index.md`, backlink, stub, bản kê, state file.
4. Mỗi operation ghi đúng 1 mục vào **cuối** `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.

## Khởi động

Ba lớp chỉ dẫn, mỗi quy tắc chỉ nằm ở một nơi: file này giữ phần phải thấy mọi lượt; `00_schema.md` §1–§12 mô tả wiki trông như thế nào; mỗi `SKILL.md` trong `.claude/skills/` là quy trình từng bước của một operation. Khi lệch nhau, ưu tiên theo thứ tự file này, `00_schema.md`, skill, và báo người dùng chỗ lệch.

1. **Đầu phiên** — hook `SessionStart` đã nạp handoff mới nhất và bảng nợ. Không ghi trạng thái phiên vào file này.
2. **Mỗi operation** (`/ingest`, `/query`, `/lint`, `/review-node`, `/research`) — chạy skill tương ứng. Đầu mỗi skill nêu mục schema cần đọc, điểm dừng chờ duyệt và việc ghi log; không đọc `00_schema.md` trước khi skill yêu cầu. Skill `writing-style` được tự gọi mỗi khi viết hoặc sửa thân bài trong `02_wiki/`, không cần hỏi.
3. **Cuối phiên có thay đổi repo** — nhắc người dùng gọi `/handoff`; không tự tạo handoff.

Quy ước viết trang wiki được nạp từ `.claude/rules/wiki-pages.md` khi chạm file trong `02_wiki/`.

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>` — chi tiết từng lệnh: `--help`. Hook cũng tự chạy sau mỗi Write/Edit trong `02_wiki/` (frontmatter, heading, link chết, source id, chú thích theo §7 luật 5). Exit 2 nghĩa là có vấn đề: xử lý ngay, không để tồn đến lượt lint. Không có lệnh kiểm riêng một trang; kiểm bằng tay thì dùng `--all`.

Bắt buộc:

| Lệnh | Khi nào |
| --- | --- |
| `--all` | Trước khi ghi log ở mọi operation có ghi trang. Cách duy nhất bắt trang mồ côi, trang sót trong `index.md` và file ghi bằng shell |
| `--coverage [<source id>]` | Chọn chunk và chốt lượt ở ingest; kiểm chunk đã phủ ở research |
| `--lint` | Bước 1 của lint: chạy gộp mọi lệnh quét, in một bảng tổng |
| `--verify-sources` | Bất cứ khi nào nghi `01_sources/` bị đổi (`--lint` đã gồm) |
| `--now` | Lấy giờ Việt Nam cho `log.md` |

Các lệnh theo nhu cầu (`--backlinks`, `--size`, `--style`, `--ocr`): xem `--help`; skill nêu lúc nào cần chạy.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- `python "Claude outputs/log_questions.py"` — ghi câu hỏi của người dùng vào `.claude/local/question-logger/questions.jsonl`; chỉ chạy khi người dùng yêu cầu (local-only). Tuỳ chọn: `--input <file.json|jsonl>`, `--dry-run`.
