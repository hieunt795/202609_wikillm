# Handoff — kiểm độ phủ nguồn khi ingest (`--coverage`)

## Kết quả

- `validate_wiki_page.py --coverage [<source id>]`: liệt kê mục (heading) trong chunk chưa được chú thích §7.5 nào trích. Hỗ trợ nguồn một file, nhiều file có `file <tên>`, và `fixed_income_during` (Ch.n → file `-(n+1).md`). Exit 2 khi chunk `[x]` còn mục chưa phủ.
- Sửa `ingest/SKILL.md` (113 → 97 dòng): bước 0 ý chính không khoanh phạm vi; bước 5 chỉ còn trần 15 trang/lượt; bước 7 bắt buộc `--coverage` trước `[x]`; bỏ Test prompts (→ `evals/evals.json`); Xử lý lỗi bỏ `git checkout -- 02_wiki/`.
- `lint/SKILL.md` thêm tiêu chí 12; `00_schema.md` §4 §10; `CLAUDE.md` bảng công cụ; `decisions.md`, `log.md` (op `schema`).
- Báo cáo: `Claude outputs/coverage-2026-09-26.md` — 96/217 chunk `[x]` đo được còn mục chưa phủ.

## Kiểm đã chạy

- `--coverage` trên 15 state file, không lỗi; Bindseil Ch.15 = 15%, khớp đo thử.
- `--verify-sources`: 0 lệch (20 file `.md/.pdf` chưa kê là tồn đọng cũ).
- `--all`: 5 trang có vấn đề + 1 mồ côi, đều thuộc lượt ingest `insights_59` đang chạy dở ở phiên khác.

- Migration (sau khi phiên `insights_59` xong): hạ 99 chunk / 15 state file `[x]` → `[~]`, Ghi chú nối "còn N mục chưa phủ, xem `--coverage <sid>`"; `index.md` §Sources 15 nguồn → "Đang ingest dở". Sau migration: `--coverage` exit 0, `--all` sạch (954 trang), `--verify-sources` 0 lệch.

- Tài liệu luồng vận hành: `.claude/docs/luong-van-hanh.html`, artifact https://claude.ai/artifact/TEwJQkC8saF42J3rJ7yrTQ (version 2).
- Ingest mục chưa phủ của `imf_macro_accounting`: 4 trang mới, merge 4 trang (→ draft), `polish-price-liberalization-…` → stale, 2 ⚠️ Conflict Ch.1 vs Ch.2 (thất nghiệp cuối 1991: 13% vs >11%; lạm phát CPI 1990–91: 250%/60% vs >550%/70%). 4 mục `bỏ qua:` theo duyệt. IMF 36/36 `[x]`; `--all` sạch 958 trang.
- Skill ingest: bước 0 trình mục chưa phủ; `bỏ qua:` cần người duyệt (decisions.md 2026-09-26).

- Audit skill ingest (21:55): đánh số lại bước 1–10 (duyệt = bước 2, `--coverage` = bước 7, index = bước 8); hook `--coverage` đọc đủ chú thích (0 mất); 2 chunk trả về `[x]`; còn 93 chunk `[~]`. Artifact version 3. Sau đó nâng ý chính ở bước 2 lên 5–10 (artifact version 4).

## Việc còn lại

- Người dùng xử lý 2 ⚠️ Conflict mới của IMF; sau đó `polish-price-liberalization-…` cần merge lại (đang stale).

- `/ingest` lại các mục chưa phủ của 14 nguồn còn lại (94 chunk), lấy danh sách bằng `--coverage <sid>`. Ưu tiên: `fixed_income_during` (23 chunk), `choudhry_analysing_yield_curve` (13), `cargill_central_bank_policy` (12). Mục không đáng ingest thì ghi `bỏ qua: <heading> — <lý do>` rồi đánh lại `[x]`.
- sbv_* báo theo từng Điều nên số mục cao; cân nhắc ghi `bỏ qua:` hàng loạt cho Điều thủ tục (hiệu lực, trách nhiệm thi hành).
- Chưa commit. Working tree lẫn thay đổi của phiên `insights_59` (chưa commit) — review `git status`/`git diff` và tách commit theo phiên.
