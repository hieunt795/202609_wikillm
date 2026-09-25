# Research chế độ tỷ giá — 2026-09-25

## Kết quả
- Cluster 16 trang (người dùng chỉ định, vượt giới hạn 10); enrich 5 trang: 7 claim mới (dollarization, foreign-currency-deposits, the-rate-of-crawl-…, perfect-capital-mobility-…, exchange-rate-regimes) + 7 link.
- stable → draft: exchange-rate-regimes, the-rate-of-crawl-…, foreign-currency-deposits.
- Báo cáo: `Claude outputs/research-2026-09-25-exchange-rate-regimes.md`; log + 2 mục `_inbox.md`.

## Kiểm
- `validate_wiki_page.py --all`: 778 trang, 0 vấn đề.

## Việc còn lại / bước tiếp
- `/ingest` imf_macro_accounting Ch.1 (d.377–606, `[ ]`) — chặn enrich trang Ba Lan; giải lệch Ch.1 d.524 vs Ch.4 d.4069.
- `/review-node`: currency-substitution-undermines-monetary-control, nfa-nda-offset-…, đoạn Cargill trên exchange-rate-regimes.
- `/lint`: dedupe dollarization vs currency-substitution; thống nhất thuật ngữ crawling peg.
- Chưa commit.

## Lint cluster tỷ giá (cùng phiên)
- Báo cáo `Claude outputs/lint-2026-09-25-16.md`; log đã ghi. Không sửa wiki.
- Chờ người dùng: promote 5 trang đủ điều kiện; chọn hướng cho stub `sterilization` (nâng hay xoá); dedupe dollarization; tạo stub managed-float, parallel-foreign-exchange-market; tách đoạn Cargill; đổi title nfa-nda-offset; triage 9 mục inbox; đăng ký file Clippings "Term premia models…" vào manifest.

## Ingest dọn nợ lint (cùng phiên)
- `sterilization` stub → draft; stub mới `managed-float`, `parallel-foreign-exchange-market`; 13 link; `--all` 780 trang sạch.
- Còn chờ: promote 5 trang; dedupe dollarization; tách đoạn Cargill; đổi title nfa-nda-offset; triage inbox; kê file Clippings. Chưa commit.
