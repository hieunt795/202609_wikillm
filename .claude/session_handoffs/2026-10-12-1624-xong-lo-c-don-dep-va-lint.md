# Handoff — xong lô C, dọn dẹp và lint 2026-10-12

## Kết quả

Mọi thay đổi đã commit và push lên `origin/main`; working tree sạch. Ba commit của phần này: `070b412` (luật miễn gắn loại cho trang tổng quan nhóm), `1231ca7` (lô C), `b3768a7` (dọn dẹp và lint).

- **Lô C xong, 6 trên 6 trang tổng quan nhóm của lĩnh vực ngân hàng.** Phần này của phiên review nốt 8 trang nhóm "Quản trị, FTP và quy định giám sát" và 6 trang nhóm "Case: Silicon Valley Bank", rồi viết hai trang tổng quan đã được duyệt:
  - `bank-steering-rules-run-from-internal-funds-transfer-pricing-to-eu-irrbb-measurement-outlier-tests-and-reporting`
  - `the-svb-case-links-hidden-htm-losses-removed-hedges-and-a-three-year-duration-gap-to-governance-and-supervisory-failure`
- **Dọn dẹp sau lô C.** Review 4 trang: trang trục bốn bước cân đối ALM, hành lang lãi suất SBV so với PBOC, định giá nợ ngoại tệ offshore, thanh khoản nội sinh. Viết lại dòng mô tả `index.md` của 51 trang đã review; bỏ hai dòng index trùng (`real-interest-rate`, `yield-curve`).
- **Lint 839 trang, sửa các mã người dùng duyệt:**
  - Gỡ cả ba dấu `⚠️ Conflict`. `level-2a-assets` theo AA− của Basel (quyết định ghi ở `decisions.md`); hai đoạn Conflict trên các trang Ba Lan bị bỏ theo ý người dùng.
  - Thêm 4 stub: `net-stable-funding-ratio-nsfr`, `basel-iii`, `maturity-transformation`, `trading-book`, kèm 8 link.
  - Ba trang nhóm thanh khoản link tới `liquidity-coverage-ratio-lcr`; trang `liquidity-regulation-and-central-bank-operations-arbitrage` thay phần định nghĩa lặp bằng link.
  - Tách `repo-specialness-…` thành ba trang; tách trang thanh khoản nội sinh thành hai trang (trang mới: `real-estate-and-gold-act-as-final-assets-and-fx-reserves-bound-a-shift-to-consumption-led-growth`).
  - Đổi title trang tt1-stickiness thành `weak-short-term-credit-absorption-breaks-balance-sheet-turnover-and-keeps-long-term-lending-rates-high` và đặt `reviewed`.
  - Bản kê nguồn: bỏ 17 dòng file không còn trên đĩa, gộp hai mục `## clippings`, cập nhật byte và checksum của file `ALM P10…` (chỉ đổi ký tự xuống dòng).
  - `_inbox.md` còn một mục (14 khái niệm ALM dưới ngưỡng tạo trang).
- **Sai sót đã biết:** message của commit `1231ca7` ghi "review 57 trang", con số đúng là 48. Chưa sửa vì cần force push.
- Báo cáo lint: `Claude outputs/lint-2026-10-12-832.md` (ngoài git). Ba lượt research của lô C không xuất báo cáo riêng vào `Claude outputs/`, lệch skill; proposal nằm trong hội thoại.

## Kiểm tra đã chạy

- `--all`: 839 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--relations`: 501 trên 4.029 link có loại, 0 cặp lệch, 125 link của trang tổng quan được miễn.
- `--verify-sources`: 203 file trong bản kê, 0 lệch hoặc thiếu, 11 file chưa kê.
- `--lint` (trước khi sửa, lúc 832 trang): `--size` 152 trang, `--style` 320 trang, `--ocr` 24 ứng viên đều là báo giả, `--coverage` 232 chunk (phủ 110, dở 77, chưa 27, miễn 18).
- `--graph`: chạy sau mỗi lượt ghi; ảnh chụp cuối lúc 16:22 với 839 trang, 4.154 link.
- Chưa chạy lại `--lint` trọn bộ sau khi sửa.

## Blocker

Không có việc nào đang kẹt chờ người dùng. Ba blocker của handoff trước (Conflict AA− và AA, bản kê lệch đĩa, title trang tt1-stickiness) đã được xử lý trong lượt lint.

## Việc còn lại

Từ phần này của phiên:

- Ba trang tách từ `repo-specialness-…` chưa có `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`. Claim đã khớp nguồn ở lượt review 2026-10-10; lint không đặt `reviewed`.
- Hai trang vừa review vượt ngưỡng kích thước: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và chuỗi CRR) và `supervisory-irrbb-reporting-…` (một đoạn 730 từ).
- 11 file nguồn chưa kê, người dùng muốn đăng ký khi ingest: `basel/BaselFramework/`, `basel/IRRBB-d368/`, `basel/LEV/`, `basel/NSF/`, `Clippings/ALM P11 TT50(P4)…`, và 6 file dưới `vietnam-regulator/alm/`.
- 4 stub mới chỉ có một câu định nghĩa không dẫn nguồn; nội dung thật chờ ingest (NSFR từ `basel/NSF/NSF.md`).
- `tata_bank_alm` còn 15 mục chưa phủ theo `--coverage`, rải ở Ch.1, Ch.2 cụm A và B, Ch.3, Ch.5, Ch.6.
- Message commit `1231ca7` sai số trang; sửa cần người dùng yêu cầu force push.
- Việc còn mở ghi ở `decisions.md`: ngoại lệ ingest cho văn bản quy phạm pháp luật (TT50/2026) chưa có trong schema §10.
- Đối chiếu con số duration 2,17 (trang replicating portfolios) với PDF gốc của Tata nếu có.
- `--graph` chưa nhận ra thao tác đổi tên trang (in thành "LINK MẤT").
- Chưa xuất báo cáo research cho bốn nhóm của lô C vào `Claude outputs/`.

Chép từ các handoff trước, chưa xử lý:

- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan đầu tiên:
  - Trang thanh khoản, đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp).
  - Trang IRRBB, đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trang tổng quan thanh khoản sẽ cũ sau lượt ingest `basel_lcr` LCR40; phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517. Các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Hàng đợi review: 11 trang trục chưa review của nhóm thanh khoản (chỉ `liquidity-risk` đã review); các trang ingest từ Clippings ngày 2026-09-22 và 23 chưa review, có cùng kiểu lỗi đã gặp (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
- Việc cho lint sau: `supervisory-outlier-test-…` dài 1.144 từ.
- 3.528 link chưa có loại (4.029 trừ 501); trả dần qua `/review-node` và `/ingest`.
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn trước khi dùng để quyết lô D (vector).
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0; số liệu đúng nằm ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
- Tỷ lệ link "mạnh" khoảng 11% (447 link), dưới mục tiêu 15–30% của kế hoạch.
- Ngưỡng thông báo của `--graph` là số tạm, chưa qua một lượt ingest thật.
- `index.md`: gán nhóm theo mục cũ, chưa soát từng trang; hai nhóm lớn nên tách khi ingest thêm ("Công cụ và cơ chế vận hành chính sách tiền tệ", "Thanh khoản và nguồn vốn").
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model; chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`.
- Kế hoạch đồ thị nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A, B, C xong; lô D tuỳ chọn, chưa mở.
- `basel_lcr` LCR30 còn bốn đoạn chưa có trang: 30.26, 30.28, 30.29, 30.47. `--coverage` chỉ báo mục Shari'ah.
- LCR40 cụm A (d.701–1185) còn 8 mục run-off; cụm B (d.1186–1324), LCR31, LCR90, LCR99 chưa đọc.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; trang trần 40%/15% dùng công thức dựng lại từ lời văn, cần đối chiếu bản gốc trên bis.org.
- Câu minh hoạ ngoài nguồn trên các trang LCR (ví dụ 150/100, repo 7 ngày, chênh phí 25 điểm cơ bản…); người dùng chưa nói giữ hay bỏ.
- `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest cần ghi `bỏ qua` cho phần trùng.
- Hook `PreToolUse` cho `--guard-sources` chưa được thử với một lệnh ghi thật vào `01_sources/`.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json`.
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; cần quét lại trước khi dùng.
- `lint` chưa có evals; chưa chạy 3 eval `research` bằng `skill-creator`.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn mục chưa phủ; quyết định [2026-09-26] là hạ về `[~]`, chưa ingest bù.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6`; chờ người dùng quyết.
- Vặt trong schema và hook: `ingest/SKILL.md:13` ghi "(§1–§12)"; §4 có hai hàng cùng tên "Kích thước 1 trang"; schema, skill và docstring hook còn dùng dạng `§7.5`; docstring `--tags`, `--style` hỏng chữ.
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".

## Bước tiếp theo

- `/ingest` `basel_lcr` LCR40 cụm A theo từng khối (bán lẻ; bán buôn không bảo đảm; có bảo đảm; yêu cầu bổ sung), rồi cập nhật trang tổng quan thanh khoản.
- Khi ingest nguồn Basel hoặc quy định Việt Nam: đăng ký file vào bản kê trước; `basel/NSF/NSF.md` cho nội dung của stub NSFR.
- `/review-node` cho ba trang tách từ `repo-specialness-…` và cho 11 trang trục của nhóm thanh khoản.
- Lượt lint sau: tách `multitiered-irrbb-regulatory-framework-…` và xem lại 14 khái niệm còn trong `_inbox.md`.

Hai script review dùng trong phiên (`rv2.py` in trang kèm đúng dòng nguồn được trích; `rvlib.py` ghi lại thân bài, `last_updated`, `reviewed` và field quan hệ) nằm trong thư mục tạm của phiên và sẽ mất.
