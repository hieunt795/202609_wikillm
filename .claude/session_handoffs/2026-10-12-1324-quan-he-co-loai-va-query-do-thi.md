# Handoff — quan hệ có loại ở frontmatter, lệnh đồ thị, skill query đi theo đồ thị

## Kết quả

- **Chưa commit gì.** `main` vẫn ở `fa079d9`. Working tree: 44 file đổi (31 trang `02_wiki/` gồm `index.md`, 13 file chỉ dẫn và sổ sách) và 3 file mới chưa theo dõi (`.claude/hooks/wiki_graph.py`, `.claude/hooks/wiki_graph_map.html`, `03_state/_graph_snapshot.tsv`). Handoff trước `2026-10-10-2118-ingest-basel-lcr.md` cũng chưa được theo dõi.
- `02_wiki/index.md` sắp lại từ 111 mục theo nguồn/chương thành 9 lĩnh vực, 62 nhóm chủ đề; 828 dòng trang giữ nguyên nội dung, 25 trang được chuyển nhóm riêng.
- `00_schema.md` sửa §1, §2, §3, §6, §7: 9 field quan hệ ở frontmatter (`part_of`/`has_part`, `governs`/`governed_by`, `drives`/`driven_by`, `contrasts`, `analogous`, `related`); pattern *tổng quan nhóm* cho `analysis`; ảnh chụp đồ thị trong `03_state/`.
- Hook: `validate_wiki_page.py` kiểm field quan hệ sau mỗi lần ghi trang; `wiki_graph.py` thêm bốn lệnh `--graph`, `--neighbors`, `--relations`, `--map`; `--lint` và bảng nợ đầu phiên có dòng quan hệ.
- Skill ingest, review-node, lint, research, rule `wiki-pages`, `CLAUDE.md` sửa theo luật mới. Gắn loại quan hệ là sổ sách.
- 152 link trên 30 trang nhóm "Thanh khoản và nguồn vốn" đã có loại (chỉ sửa frontmatter, không nâng `last_updated`).
- Skill `query` bước 3 dùng `--neighbors` thay cho outlink cộng `--backlinks`; `evals.json` của query có 9 câu (thêm 6, sửa tiêu chí của câu 1 và 2).
- `_inbox.md` thêm 2 mục: 18 khái niệm ALM chưa có trang; lệch ngày TAF giữa hai trang.
- `decisions.md` thêm 3 mục ngày 2026-10-12; `log.md` thêm 3 mục `schema` (10-35-59, 11-33-38, 11-46-10).
- Ngoài git, trong `Claude outputs/`: `graph-map-alm.html` (bản đồ lĩnh vực ngân hàng), `query-workspace/` (bản chụp skill query cũ, 15 lượt thử, `grading-summary.md`, `review.html`), và ba file bản thử đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`) chưa xoá.
- Kế hoạch đã duyệt nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A và lô B xong; lô C chưa bắt đầu; lô D (vector) là tuỳ chọn.

## Kiểm tra đã chạy

- `--all` (sau lô B): 826 trang, 0 trang có vấn đề, 0 mồ côi, 0 sót index.
- `--relations`: 152/4.030 link có loại, 0 cặp gắn loại lệch nhau.
- `--graph`: 826 trang, 4.030 link, 445 mạnh, 419 cặp nhóm có link chéo; ảnh chụp 71 KB.
- Phép thử âm của hook trên thư mục `02_wiki` giả: 4 loại quan hệ sai đều bị báo, exit 2.
- Phát hiện cặp lệch: sửa thử một loại trên `level-1-assets`, `--relations` báo đúng, đã hoàn tác.
- `--neighbors` với `--type` và `--hops 2`: trả đúng láng giềng, đã gộp dòng trùng hai chiều.
- `--map ALM` mở bằng Edge không giao diện: 98 nút, đường nối, bảng nhóm, bảng xếp hạng đều vẽ ra.
- `--lint` (bảng tổng): `--verify-sources` vẫn exit 2 như handoff trước; các dòng khác exit 0.
- Eval query, 15 lượt bằng Sonnet: 6 câu mới, skill mới 49/49 tiêu chí, skill cũ 48/49; 3 câu cũ với skill mới 21/24 (3 tiêu chí trượt do tiêu chí lỗi thời, đã sửa). Bộ tiêu chí chưa phân biệt được hai bản.
- Chưa kiểm được: thông báo "ĐỔI LOẠI" và "không có thay đổi vượt ngưỡng" của `--graph`, vì link được so với HEAD và phiên này chưa commit. Trước commit, mỗi lần chạy `--graph` báo lại "152 link vừa được gắn loại".
- Chưa thử: rê chuột, bấm ghim và các nút lọc của bản đồ HTML; các ngưỡng thông báo của `--graph` với một lượt ingest thật.
- Chưa chạy trong phiên này: `--coverage` theo từng nguồn, `--size`, `--style` riêng lẻ (chỉ thấy dòng tổng trong `--lint`).

## Blocker

- `⚠️ Conflict` trên `level-2a-assets` chờ người dùng xử lý: Basel 30.43 ghi xếp hạng tối thiểu AA− (`basel_lcr`, d.291–292), Bindseil ghi AA (`bindseil_monetary_policy`, Ch.16, d.3664).
- `01_sources/basel/` và `01_sources/vietnam-regulator/alm/` đã đổi cấu trúc so với bản kê; chờ người dùng quyết có viết lại hai mục `basel` và `vietnam_regulator` theo đĩa hay không (việc đó xoá các dòng checksum cũ).

## Việc còn lại

Từ phiên này:

- Commit. `decisions.md` và `log.md` chứa mục của cả ba việc (sắp lại index, lô A, lô B) nên khó tách thành ba commit sạch nếu không staging từng phần.
- Lô C: 6 trang *tổng quan nhóm* cho lĩnh vực ngân hàng qua `/research`, mỗi lượt một nhóm, một trang, qua proposal chờ duyệt. Chưa cài phần kiểm "tổng quan nhóm đã cũ" trong `--relations`; skill lint đã nhắc tới tiêu chí này ở mã `R`.
- 3.878 link chưa có loại; trả dần qua `/review-node` và `/ingest`, không có lô riêng.
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn (gắn với trang cụ thể phải được mở, claim cụ thể phải đúng) trước khi dùng nó để quyết lô D. Mỗi câu mới chạy một lượt; `CLAUDE.md` nhắc tên `--neighbors` nên phía skill cũ không hoàn toàn mù lệnh mới.
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0 vì không nhận cấu trúc thư mục của workspace; số liệu đúng nằm ở `grading-summary.md` và các `timing.json`.
- Tỷ lệ link "mạnh" là 11% (445 link), dưới mục tiêu 15–30% của kế hoạch; quy tắc hiện tại là "link trong câu đầu tiên của trang".
- Ngưỡng thông báo của `--graph` (top 25, nhảy 50 bậc trong 200 hạng đầu, độ mạnh cặp nhóm đổi từ 20% và từ 5 điểm) là số tạm.
- `index.md`: gán nhóm theo cả mục cũ, chưa soát từng trang; `real-interest-rate` và `yield-curve` bị liệt kê hai lần; hai nhóm lớn nên tách khi ingest thêm ("Công cụ và cơ chế vận hành chính sách tiền tệ" 47 trang, "Thanh khoản và nguồn vốn" 32 trang).
- `_inbox.md` có 7 mục; hai mục mới chờ lint hoặc review: 18 khái niệm ALM chưa có trang (NSFR, Basel III, maturity transformation, trading book đủ ngưỡng mã `S`), và lệch ngày TAF giữa `collateral-pool-segregation-and-double-adverse-selection` (3/2008) với `central-bank-fx-swap-lines-and-cross-border-liquidity` (12/2007).
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ; file này vốn đã lệch từ trước.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế, chưa xoá; xoá cần người dùng xác nhận.
- Các loại quan hệ của 152 link là phán đoán của model từ câu chứa link; chưa ai soát.

Chép từ handoff trước, chưa xử lý:

- `basel_lcr` LCR30 còn bốn đoạn chưa có trang: 30.26 (thanh khoản trong ngày), 30.28 (giữ thêm 30 ngày khi tài sản mất tư cách HQLA), 30.29 (đa dạng hoá kho), 30.47 (ngân hàng Shari'ah). `--coverage` chỉ báo mục Shari'ah; ba đoạn kia phải nhớ tay.
- LCR40 cụm A (d.701–1185) còn 9 mục run-off; cụm B (dòng vào, d.1186–1324), LCR31, LCR90, LCR99 chưa đọc. Hai trang `total-expected-cash-outflows` và `total-expected-cash-inflows` mới có định nghĩa chung.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; bản trong `BaselFramework.md` cũng vậy. Trang trần 40%/15% dùng công thức dựng lại từ lời văn 30.35–30.39 và ghi rõ; cần đối chiếu bản gốc trên bis.org khi review.
- Câu minh hoạ ngoài nguồn, đã ghi rõ trong trang: ví dụ 150/100 (trang hạn chế chuyển thanh khoản), HQLA nội tệ với dòng ra USD (trang đồng tiền), ví dụ 60/50 (trang trần), repo 7 ngày (trang số điều chỉnh), "HQLA ít nhất 25% dòng ra" (trang dòng vào), chênh phí 25 điểm cơ bản (trang RCLF). Người dùng chưa nói giữ hay bỏ.
- `--verify-sources`: 11 file `basel/*.md` trong bản kê không còn trên đĩa (gồm `bcbs238.md`, `bcbs144.md`, `bcbs155.md`, `insights59.md`, các hướng dẫn EBA/ECB); chưa kê `basel/BaselFramework/`, `IRRBB-d368/`, `LEV/`, `NSF/`; `vietnam-regulator/alm/` 6 thiếu và 6 chưa kê; 1 file Clippings lệch byte (`ALM P10 UpdateTT50 (P3)...`, 6.219 so với 6.193).
- `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest file đó cần ghi `bỏ qua` cho phần trùng.
- Hook `PreToolUse` cho `--guard-sources`: phiên này xác nhận đã cấu hình trong `.claude/settings.json` (matcher `Bash|PowerShell`). Chưa thử xem nó có chặn được một lệnh ghi thật vào `01_sources/` hay không.
- Trang `liquidity-regulation-and-central-bank-operations-arbitrage` gộp nhiều ý với tiêu đề in đậm giả heading; phần định nghĩa LCR và HQLA ở đó giờ trùng với các trang mới.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json` (nơi đã có `finance@synced: false`).
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; ví dụ map FTP ghi 37 node, `02_wiki/` hiện còn 6 trang có `ftp` trong tên. Cần quét lại trước khi dùng.
- `lint` và `promote` chưa có evals.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ (during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4). Quyết định [2026-09-26] là hạ các chunk này về `[~]`; chưa ingest bù, chưa đổi `03_state/`.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6` (patch conflict, một số thay thế lệch nghĩa); mới sửa tay 4 trang ở `f966870`. Chờ người dùng quyết.
- `--style` báo 324/826 trang, `--size` 155 trang (số của `--lint` phiên này), 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
- `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- `ingest/SKILL.md:13` ghi "(§1–§12)".
- `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; `CLAUDE.md` đã đổi sang "§7 luật 5".
- Docstring `.claude/hooks/validate_wiki_page.py` các dòng mô tả `--tags`, `--style` hỏng chữ, còn "luat cung 1".
- `CLAUDE.md` hiện 854 từ theo `wc -w`, dưới mốc khoảng 950.
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".
- Chưa chạy 3 eval `research` bằng `skill-creator`.

## Bước tiếp theo

- Commit phần đang mở, rồi chạy `--graph` một lần để xác nhận nó báo "không có thay đổi vượt ngưỡng" sau commit.
- Mở bản đồ `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html` để người dùng đánh giá nhãn quan hệ và so hai bản skill query.
- Lô C: `/research` cho nhóm "Thanh khoản và nguồn vốn" trước, đề xuất một trang tổng quan nhóm; sau đó 5 nhóm ngân hàng còn lại.
- Ingest tiếp `basel_lcr`: LCR40 cụm A theo từng khối (bán lẻ; bán buôn không bảo đảm; có bảo đảm; yêu cầu bổ sung), mỗi khối một lượt qua bước duyệt. Đây là lượt ingest thật đầu tiên có gắn loại quan hệ và chạy `--graph`, dùng để chỉnh ngưỡng thông báo.
- Người dùng xử lý `⚠️ Conflict` AA− và AA, và quyết việc viết lại hai mục bản kê lệch đĩa.
- `/review-node` cho hai trang lệch ngày TAF và cho `level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock` sau khi có công thức 30.38 từ bản gốc.
