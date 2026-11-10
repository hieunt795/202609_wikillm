# Handoff — lô C: hai trang tổng quan nhóm, review cả nhóm IRRBB

Tiếp nối cùng phiên với handoff `2026-10-12-1324-quan-he-co-loai-va-query-do-thi.md`; file này thay nó làm handoff mới nhất.

## Kết quả

- **Đã commit và push** phần của handoff trước: `f8be726` trên `main` (sắp lại index, lô A quan hệ có loại, lô B skill query). Handoff trước ghi "chưa commit gì" là trạng thái lúc nó được viết.
- **Chưa commit** phần làm sau đó: 19 file đổi, 2 trang mới chưa theo dõi, cộng file handoff này.
- Lô C, 2 trên 6 nhóm ngân hàng đã có trang tổng quan (`type: analysis`, đứng dòng đầu nhóm trong `index.md`, nhãn *(tổng quan nhóm)*), cả hai đều qua proposal được người dùng duyệt:
  - `the-lcr-buffers-liquidity-risk-for-30-days-while-ratio-compliance-leaves-the-funding-mismatch-in-place` (nhóm "Thanh khoản và nguồn vốn").
  - `irrbb-measurement-pairs-economic-value-and-earnings-views-over-gap-basis-and-option-risk` (nhóm "Rủi ro lãi suất sổ ngân hàng (IRRBB)").
  - Mỗi trang kèm một câu backlink ở cuối trang trục của nhóm (`liquidity-coverage-ratio-lcr`, `interest-rate-risk-in-the-banking-book-irrbb`), không nâng `last_updated`.
- Review 14 trang chưa review của nhóm IRRBB, đối chiếu với `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md`: cả 14 đều có claim phải sửa, đều đã sửa, nâng `last_updated` và đặt `reviewed_by: model`. Cả 16 trang của nhóm giờ đã review. Lượt thứ hai làm 9 trang một lượt theo yêu cầu người dùng, vượt mốc 5 trang của §4.
- Loại quan hệ: 287/4.090 link có loại (lúc commit `f8be726` là 152/4.030); 0 cặp lệch.
- `log.md` thêm 4 mục sau commit: 2 `research` (13-41-22, 13-46-26), 2 `review` (13-50-37, 13-56-05).
- Ngoài git, trong `Claude outputs/`: `research-2026-10-12-liquidity-and-funding-overview.md`, `research-2026-10-12-irrbb-overview.md`.

## Kiểm tra đã chạy

- `--all`: 828 trang, 0 trang có vấn đề, 0 mồ côi, 0 sót index.
- `--relations`: 287/4.090 link có loại, 0 cặp gắn loại lệch nhau.
- `--graph` sau commit `f8be726` (`--no-save`): "không có thay đổi vượt ngưỡng". Đây là phép thử handoff trước ghi chưa kiểm được.
- `--graph` sau trang tổng quan thanh khoản: lần đầu báo một dòng vượt ngưỡng thật, độ mạnh "Chính sách tiền tệ trong khủng hoảng" ↔ "Thanh khoản và nguồn vốn" 29 → 35.
- `--graph` sau lượt review cuối: +63 link, −3 link, 72 link vừa gắn loại; báo đúng 3 link bị bỏ có chủ ý (`balance-sheet-evolution-…` → SOT và → `economic-value-and-earnings-…`; `credit-spread-risk-in-the-banking-book-csrbb` → `liquidity-risk`); số cặp nhóm có link chéo 419 → 418.
- `--size` và `--style` trên hai trang tổng quan và 14 trang đã review: 0 cờ (hai trang tổng quan có cờ "nên" dùng làm liên từ, đã viết lại).
- Chưa kiểm được: thông báo "ĐỔI LOẠI" của `--graph` (chưa có lần nào đổi loại một link đã commit).
- Chưa chạy trong phần này của phiên: `--lint`, `--verify-sources`, `--coverage`.

## Blocker

- `⚠️ Conflict` trên `level-2a-assets` chờ người dùng xử lý: Basel 30.43 ghi xếp hạng tối thiểu AA− (`basel_lcr`, d.291–292), Bindseil ghi AA (`bindseil_monetary_policy`, Ch.16, d.3664).
- `01_sources/basel/` và `01_sources/vietnam-regulator/alm/` đã đổi cấu trúc so với bản kê; chờ người dùng quyết có viết lại hai mục `basel` và `vietnam_regulator` theo đĩa hay không (việc đó xoá các dòng checksum cũ).

## Việc còn lại

Từ phần này của phiên:

- Commit 19 file đổi, 2 trang mới và handoff này.
- Lô C còn 4 nhóm ngân hàng chưa có trang tổng quan: "Nền tảng ALM và bảng cân đối", "Tiền gửi và mô hình hành vi", "Quản trị, FTP và quy định giám sát", "Case: Silicon Valley Bank". Mỗi nhóm một lượt `/research` với proposal riêng.
- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan:
  - Trang thanh khoản, đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp).
  - Trang IRRBB, đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trang tổng quan thanh khoản sẽ cũ sau lượt ingest `basel_lcr` LCR40; phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài, nên chưa có gì tự nhắc.
- Title trang tổng quan thanh khoản mang nhận định "tuân thủ tỷ lệ không xoá bất cân xứng"; nguồn chỉ nói điều này cho CDR và thân bài giữ đúng phạm vi đó. Bản title trung tính đã đề xuất: `bank-liquidity-rules-pair-a-stressed-30-day-hqla-buffer-with-ratio-limits-on-funding-structure`; người dùng chưa chọn rõ giữa hai bản.
- Hai trang tổng quan gắn `related` cho mọi link (39 và 20 link), làm loại `related` lên 111 link. Câu hỏi còn mở với người dùng: miễn gắn loại cho trang tổng quan (cần sửa schema §6) hay giữ như hiện tại.
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517, chưa mở d.1550. Các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Mẫu lỗi lặp lại ở các trang ingest từ `tata_bank_alm` ngày 2026-09-23 và 24: thêm tính từ mạnh ("khổng lồ", "cốt lõi", "nghiêm trọng"), biến mô tả thành nghĩa vụ ("bắt buộc", "phải"), tự thêm ví dụ và câu kết không có trong nguồn, chú thích trỏ dòng trống. Các trang Tata ở nhóm khác chưa review.
- Hàng đợi review cần nhắc lại: hai trang lệch ngày TAF (`collateral-pool-segregation-and-double-adverse-selection`, `central-bank-fx-swap-lines-and-cross-border-liquidity`); trong 12 trang trục của nhóm thanh khoản chỉ `liquidity-risk` đã review.
- Việc cho lint: `supervisory-outlier-test-…` dài 1.144 từ; `liquidity-regulation-and-central-bank-operations-arbitrage` lặp định nghĩa LCR, HQLA; ba trang ngoài cụm LCR (`credit-to-deposit-ratio`, `regulatory-ratios-can-relocate-…`, `treasury-deposits-at-commercial-banks-…`) không có link trực tiếp với các trang LCR.

Chép từ handoff `2026-10-12-1324`, chưa xử lý:

- 3.803 link chưa có loại; trả dần qua `/review-node` và `/ingest`, không có lô riêng.
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn (gắn với trang cụ thể phải được mở, claim cụ thể phải đúng) trước khi dùng nó để quyết lô D (vector). Mỗi câu mới chạy một lượt; `CLAUDE.md` nhắc tên `--neighbors` nên phía skill cũ không hoàn toàn mù lệnh mới.
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0 vì không nhận cấu trúc thư mục của workspace; số liệu đúng nằm ở `Claude outputs/query-workspace/iteration-1/grading-summary.md` và các `timing.json`.
- Tỷ lệ link "mạnh" là 11% (445 link), dưới mục tiêu 15–30% của kế hoạch; quy tắc hiện tại là "link trong câu đầu tiên của trang".
- Ngưỡng thông báo của `--graph` (top 25, nhảy 50 bậc trong 200 hạng đầu, độ mạnh cặp nhóm đổi từ 20% và từ 5 điểm) là số tạm, chưa qua một lượt ingest thật.
- `index.md`: gán nhóm theo cả mục cũ, chưa soát từng trang; `real-interest-rate` và `yield-curve` bị liệt kê hai lần; hai nhóm lớn nên tách khi ingest thêm ("Công cụ và cơ chế vận hành chính sách tiền tệ" 47 trang, "Thanh khoản và nguồn vốn" 33 trang).
- `_inbox.md` có 7 mục; hai mục chờ lint hoặc review: 18 khái niệm ALM chưa có trang (NSFR, Basel III, maturity transformation, trading book đủ ngưỡng mã `S`), và lệch ngày TAF.
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ; file này vốn đã lệch từ trước.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model từ câu chứa link; chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html` để đánh giá.
- Kế hoạch đã duyệt nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A, B xong; lô C dở (2/6); lô D tuỳ chọn.
- `basel_lcr` LCR30 còn bốn đoạn chưa có trang: 30.26 (thanh khoản trong ngày), 30.28 (giữ thêm 30 ngày khi tài sản mất tư cách HQLA), 30.29 (đa dạng hoá kho), 30.47 (ngân hàng Shari'ah). `--coverage` chỉ báo mục Shari'ah; ba đoạn kia phải nhớ tay.
- LCR40 cụm A (d.701–1185) còn 9 mục run-off; cụm B (dòng vào, d.1186–1324), LCR31, LCR90, LCR99 chưa đọc. Hai trang `total-expected-cash-outflows` và `total-expected-cash-inflows` mới có định nghĩa chung.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; bản trong `BaselFramework.md` cũng vậy. Trang trần 40%/15% dùng công thức dựng lại từ lời văn 30.35–30.39 và ghi rõ; cần đối chiếu bản gốc trên bis.org khi review.
- Câu minh hoạ ngoài nguồn, đã ghi rõ trong trang: ví dụ 150/100 (trang hạn chế chuyển thanh khoản), HQLA nội tệ với dòng ra USD (trang đồng tiền), ví dụ 60/50 (trang trần), repo 7 ngày (trang số điều chỉnh), "HQLA ít nhất 25% dòng ra" (trang dòng vào), chênh phí 25 điểm cơ bản (trang RCLF). Người dùng chưa nói giữ hay bỏ.
- `--verify-sources`: 11 file `basel/*.md` trong bản kê không còn trên đĩa (gồm `bcbs238.md`, `bcbs144.md`, `bcbs155.md`, `insights59.md`, các hướng dẫn EBA/ECB); chưa kê `basel/BaselFramework/`, `IRRBB-d368/`, `LEV/`, `NSF/`; `vietnam-regulator/alm/` 6 thiếu và 6 chưa kê; 1 file Clippings lệch byte (`ALM P10 UpdateTT50 (P3)...`, 6.219 so với 6.193).
- `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest file đó cần ghi `bỏ qua` cho phần trùng.
- Hook `PreToolUse` cho `--guard-sources` đã cấu hình trong `.claude/settings.json` (matcher `Bash|PowerShell`). Chưa thử xem nó có chặn được một lệnh ghi thật vào `01_sources/` hay không.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json` (nơi đã có `finance@synced: false`).
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; ví dụ map FTP ghi 37 node, `02_wiki/` hiện còn 6 trang có `ftp` trong tên. Cần quét lại trước khi dùng.
- `lint` và `promote` chưa có evals.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ (during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4). Quyết định [2026-09-26] là hạ các chunk này về `[~]`; chưa ingest bù, chưa đổi `03_state/`.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6` (patch conflict, một số thay thế lệch nghĩa); mới sửa tay 4 trang ở `f966870`. Chờ người dùng quyết.
- `--style` báo 324/826 trang, `--size` 155 trang (số của `--lint` đầu phiên, trước lượt review), 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
- `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- `ingest/SKILL.md:13` ghi "(§1–§12)".
- `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; `CLAUDE.md` đã đổi sang "§7 luật 5".
- Docstring `.claude/hooks/validate_wiki_page.py` các dòng mô tả `--tags`, `--style` hỏng chữ, còn "luat cung 1".
- `CLAUDE.md` hiện 854 từ theo `wc -w`, dưới mốc khoảng 950.
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".
- Chưa chạy 3 eval `research` bằng `skill-creator`.

## Bước tiếp theo

- Commit phần đang mở.
- Lô C: `/research` cho nhóm "Nền tảng ALM và bảng cân đối" (20 trang, nối mạnh nhất với IRRBB), rồi ba nhóm còn lại.
- `/review-node` cho các trang Tata chưa review ở các nhóm ngân hàng khác, ưu tiên theo số backlink; nếu người dùng cho phép thì dùng subagent `source-verifier` để đối chiếu song song.
- Ingest tiếp `basel_lcr` LCR40 cụm A theo từng khối (bán lẻ; bán buôn không bảo đảm; có bảo đảm; yêu cầu bổ sung); sau đó cập nhật trang tổng quan thanh khoản.
- Người dùng xử lý `⚠️ Conflict` AA− và AA, quyết việc viết lại hai mục bản kê lệch đĩa, và trả lời hai câu còn mở: title trang tổng quan thanh khoản, có miễn gắn loại cho trang tổng quan hay không.
