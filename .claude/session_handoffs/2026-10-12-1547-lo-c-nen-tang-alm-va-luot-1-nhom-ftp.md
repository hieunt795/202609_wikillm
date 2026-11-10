# Handoff — lô C: nhóm "Nền tảng ALM" xong, nhóm "Quản trị, FTP và quy định" xong lượt 1/3

## Kết quả

- **Commit gần nhất vẫn là `f226029`.** Mọi thứ sau đó chưa commit (người dùng đã yêu cầu không commit ở giữa phiên, chưa ra lệnh lại): 45 file đổi, 2 trang mới, 1 trang đổi tên, handoff `2026-10-12-1416` và handoff này.
- **Từ handoff `2026-10-12-1416` tới giờ:**
  - Review 19 trang nhóm "Nền tảng ALM và bảng cân đối" (bốn lượt); cả 20 trang của nhóm đã có `reviewed`.
  - Trang tổng quan nhóm thứ tư (lô C, 4/6): `alm-foundations-run-from-balance-sheet-balancing-through-eve-and-nii-measurement-to-bank-specific-and-technology-driven-practice`, 6 đoạn, 24 link, không gắn loại; dòng đầu nhóm trong `index.md`; backlink ở cuối trang `economic-value-and-earnings-perspectives-complement-each-other-in-alm`.
  - Review 5 trang đầu nhóm "Quản trị, FTP và quy định giám sát" (lượt 1/3): FTP, matched maturity FTP, đường cong FTP hai thành phần, FTP điều hướng kinh doanh, chi phí LCR/NSFR trong FTP.
- **Phần đã ghi ở handoff `1416` và vẫn chưa commit:** luật miễn gắn loại cho trang tổng quan nhóm (`00_schema.md` §6, `wiki_graph.py`, `research/SKILL.md`), đổi title trang tổng quan thanh khoản, review 10 trang nhóm tiền gửi, trang tổng quan nhóm tiền gửi.
- **Trạng thái lô C:**

  | Nhóm | Review | Trang tổng quan |
  | --- | --- | --- |
  | Thanh khoản và nguồn vốn | 1/12 trang trục | xong |
  | IRRBB | 16/16 | xong |
  | Tiền gửi và mô hình hành vi | 9/10 (1 trang chờ đổi title) | xong |
  | Nền tảng ALM và bảng cân đối | 20/20 | xong |
  | Quản trị, FTP và quy định giám sát | 5/13 | chưa |
  | Case: Silicon Valley Bank | 0/6 | chưa |

- **Điểm cần biết về các lượt review của phần này:**
  - Trang `multiple-balance-sheet-mismatches-…`: bốn lớp mismatch sửa theo nguồn (thanh khoản, duration, định giá lại, giá); bỏ đoạn mismatch tiền tệ qua FX swap và hệ quả lên giá vàng.
  - Trang `coupon-floors-and-indicator-floors-…`: kết quả NII từng khoảng do tôi tính từ công thức, vì chú thích nguồn (`tata_bank_alm` d.2512) in thiếu dấu; trang ghi rõ.
  - Bốn trang chương 6 của Tata có dòng "Xem thêm" ở cuối; đã lồng link vào câu hoặc bỏ.
  - Link bỏ có chủ ý (câu chứa link không có nguồn), không trang nào thành mồ côi: multi-mismatch → `domestic-gold-pricing-…`; economic value vs earnings → `alm-balance-sheet-balancing-…`; FinTech → `silicon-valley-bank-collapse-…`; Deep ALM → `net-interest-income-planning-…`.
  - Hai cặp quan hệ lệch do tôi gắn ở lượt FTP đã sửa trước khi viết handoff này (`regulatory-lcr-and-nsfr-…` ghi `driven_by` LCR; `matched-maturity-ftp-…` ghi `governs` liquidity-risk).
- **Lệch quy trình:** hai lượt research (nhóm tiền gửi, nhóm nền tảng ALM) không xuất file báo cáo vào `Claude outputs/`; log ghi rõ.
- **Công cụ tạm ngoài repo** (scratchpad của phiên, sẽ mất): `rv2.py` in một trang kèm các dòng nguồn nó trích; `rvlib.py` có hàm `apply(page, new_body, rel)` ghi lại thân bài, đặt `last_updated`, `reviewed`, `reviewed_by` và field quan hệ, in link bị bỏ. Phiên sau cần thì viết lại theo mô tả này.
- `log.md` có 10 mục của phiên từ 14:04 tới 15:45: 1 schema, 7 review, 2 research.

## Kiểm tra đã chạy

- `--all`: 830 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--relations`: 402/4.025 link có loại, 0 cặp lệch, 99 link của trang tổng quan nhóm được miễn.
- `--graph` (đã lưu ảnh chụp lúc 15:47): 830 trang, 4.124 link, 444 link mạnh. So với HEAD vẫn in 21 "ĐỔI LOẠI" và 40 "LINK MẤT" của lượt đổi tên trang thanh khoản; các dòng này sẽ hết sau khi commit.
- `--style`: trang tổng quan nền tảng ALM không bị báo. Các trang review trong phần này chưa soát cờ `--style`.
- `--size`: trang tổng quan nền tảng ALM không bị báo.
- Chưa chạy: `--lint`, `--verify-sources`, `--coverage`.

## Blocker

- `⚠️ Conflict` trên `level-2a-assets` chờ người dùng xử lý: Basel 30.43 ghi xếp hạng tối thiểu AA− (`basel_lcr`, d.291–292), Bindseil ghi AA (`bindseil_monetary_policy`, Ch.16, d.3664).
- `01_sources/basel/` và `01_sources/vietnam-regulator/alm/` đã đổi cấu trúc so với bản kê; chờ người dùng quyết có viết lại hai mục `basel` và `vietnam_regulator` theo đĩa hay không (việc đó xoá các dòng checksum cũ).
- `tt1-deposit-rate-stickiness-prevents-interbank-liquidity-from-lowering-lending-rates` chờ người dùng quyết đổi title (gợi ý trong `_inbox.md`) trước khi đặt `reviewed`.

## Việc còn lại

Từ phần này của phiên:

- Commit phần đang mở khi người dùng yêu cầu.
- Nhóm "Quản trị, FTP và quy định giám sát" còn 8 trang chưa review: `funds-transfer-pricing-contrasts-with-derivatives-funding-value-adjustments`, `contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons`, `multitiered-irrbb-regulatory-framework-spans-bcbs-crd-crr-and-eba-technical-standards`, `eba-standardized-approach-for-irrbb-harmonizes-eve-and-nii-measurement`, `simplified-standardized-approach-provides-conservative-irrbb-metrics-for-small-banks`, `maturity-dependent-linear-rate-floor-bounds-post-shock-yield-curves-under-irrbb`, `simultaneous-compliance-problem-constrains-fixed-rate-allocation-under-dual-sot-limits`, `supervisory-irrbb-reporting-mandates-five-standardized-templates-under-eu-2024-855`. Sau đó là proposal trang tổng quan nhóm.
- Nhóm "Case: Silicon Valley Bank" còn 6 trang chưa review, rồi proposal trang tổng quan nhóm.
- Trang trục `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` có `reviewed: 2026-09-24` nên không được đọc lại với nguồn trong phiên này; nó nhận nhiều link mới từ các trang vừa sửa.
- Đối chiếu con số duration 2,17 (trang replicating portfolios) với PDF gốc của Tata nếu có.
- `--graph` chưa nhận ra thao tác đổi tên trang (in thành "LINK MẤT").
- Dòng mô tả trong `index.md` của các trang vừa review (nhóm tiền gửi, nền tảng ALM, FTP) còn theo nội dung cũ; chưa cập nhật.
- Stub `deposit-beta` (25 từ) chưa được viết.
- Hai trang `central-bank-interest-rate-corridor-requires-separate-facilities-…` và `offshore-foreign-currency-debt-pricing-diverges-from-domestic-benchmarks` chỉ còn một backlink (từ trang TT1–TT2) và chưa review; cả hai thuộc đợt ingest Clippings ngày 2026-09-22 và 23, có dấu hiệu cùng kiểu lỗi.
- Chưa xuất báo cáo research cho nhóm tiền gửi và nhóm nền tảng ALM vào `Claude outputs/`.

Chép từ handoff `2026-10-12-1357`, chưa xử lý:

- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan (người dùng quyết để lượt review sau xử lý):
  - Trang thanh khoản, đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp).
  - Trang IRRBB, đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trang tổng quan thanh khoản sẽ cũ sau lượt ingest `basel_lcr` LCR40; phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài, nên chưa có gì tự nhắc.
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517, chưa mở d.1550. Các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Mẫu lỗi lặp lại ở các trang ingest từ `tata_bank_alm` ngày 2026-09-23 và 24: thêm tính từ mạnh ("khổng lồ", "cốt lõi", "nghiêm trọng"), biến mô tả thành nghĩa vụ ("bắt buộc", "phải"), tự thêm ví dụ và câu kết không có trong nguồn, chú thích trỏ dòng trống, dòng "Xem thêm" ở cuối trang. Còn 14 trang Tata chưa review ở hai nhóm ngân hàng cuối.
- Hàng đợi review cần nhắc lại: hai trang lệch ngày TAF (`collateral-pool-segregation-and-double-adverse-selection`, `central-bank-fx-swap-lines-and-cross-border-liquidity`); trong 12 trang trục của nhóm thanh khoản chỉ `liquidity-risk` đã review.
- Việc cho lint: `supervisory-outlier-test-…` dài 1.144 từ; `liquidity-regulation-and-central-bank-operations-arbitrage` lặp định nghĩa LCR, HQLA; ba trang ngoài cụm LCR (`credit-to-deposit-ratio`, `regulatory-ratios-can-relocate-…`, `treasury-deposits-at-commercial-banks-…`) không có link trực tiếp với các trang LCR.

Chép từ handoff `2026-10-12-1324`, chưa xử lý:

- 3.623 link chưa có loại (4.025 trừ 402); trả dần qua `/review-node` và `/ingest`, không có lô riêng.
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn (gắn với trang cụ thể phải được mở, claim cụ thể phải đúng) trước khi dùng nó để quyết lô D (vector). Mỗi câu mới chạy một lượt; `CLAUDE.md` nhắc tên `--neighbors` nên phía skill cũ không hoàn toàn mù lệnh mới.
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0 vì không nhận cấu trúc thư mục của workspace; số liệu đúng nằm ở `Claude outputs/query-workspace/iteration-1/grading-summary.md` và các `timing.json`.
- Tỷ lệ link "mạnh" là 11% (444 link), dưới mục tiêu 15–30% của kế hoạch; quy tắc hiện tại là "link trong câu đầu tiên của trang".
- Ngưỡng thông báo của `--graph` (top 25, nhảy 50 bậc trong 200 hạng đầu, độ mạnh cặp nhóm đổi từ 20% và từ 5 điểm) là số tạm, chưa qua một lượt ingest thật.
- `index.md`: gán nhóm theo cả mục cũ, chưa soát từng trang; `real-interest-rate` và `yield-curve` bị liệt kê hai lần; hai nhóm lớn nên tách khi ingest thêm ("Công cụ và cơ chế vận hành chính sách tiền tệ" 47 trang, "Thanh khoản và nguồn vốn" 33 trang).
- `_inbox.md`: hai mục chờ lint hoặc review từ trước (18 khái niệm ALM chưa có trang — NSFR, Basel III, maturity transformation, trading book đủ ngưỡng mã `S`; lệch ngày TAF), cộng mục title tt1-stickiness.
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ; file này vốn đã lệch từ trước.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model từ câu chứa link; chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html` để đánh giá.
- Kế hoạch đã duyệt nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A, B xong; lô C dở (4/6); lô D tuỳ chọn.
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
- `--style` báo 324/826 trang, `--size` 155 trang (số của `--lint` đầu phiên, trước các lượt review), 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
- `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- `ingest/SKILL.md:13` ghi "(§1–§12)".
- `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; `CLAUDE.md` đã đổi sang "§7 luật 5".
- Docstring `.claude/hooks/validate_wiki_page.py` các dòng mô tả `--tags`, `--style` hỏng chữ, còn "luat cung 1".
- `CLAUDE.md` hiện 854 từ theo `wc -w`, dưới mốc khoảng 950.
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".
- Chưa chạy 3 eval `research` bằng `skill-creator`.

## Bước tiếp theo

- Commit phần đang mở khi người dùng yêu cầu; nên tách hai commit (batch schema và đổi title; các lượt review và ba trang tổng quan).
- Lô C: `/review-node` lượt 2 và 3 cho 8 trang còn lại của nhóm "Quản trị, FTP và quy định giám sát" (đối chiếu `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md`, chủ yếu Ch.2 mục 2.3 và Ch.5), rồi `/research` cho proposal trang tổng quan nhóm.
- Lô C: nhóm "Case: Silicon Valley Bank", 6 trang (Tata Ch.4), cùng trình tự.
- Người dùng quyết title cho trang tt1-stickiness; sau đó đổi tên, cập nhật link và đặt `reviewed`.
- Ingest tiếp `basel_lcr` LCR40 cụm A theo từng khối (bán lẻ; bán buôn không bảo đảm; có bảo đảm; yêu cầu bổ sung); sau đó cập nhật trang tổng quan thanh khoản.
- Người dùng xử lý `⚠️ Conflict` AA− và AA, và quyết việc viết lại hai mục bản kê lệch đĩa.
