# Handoff — ingest trọn chương LCR40 của basel_lcr

## Kết quả

Mọi thay đổi đã commit và push lên `origin/main` (`a5c13df`); working tree sạch trước khi ghi file này. File handoff này chưa commit.

- **Ingest `basel_lcr` chương LCR40, bốn lượt, 47 trang mới** (đoạn 40.5–40.93):
  - Lượt 1, 10 trang: tiền gửi bán lẻ (ổn định, kém ổn định, có kỳ hạn) và vốn bán buôn không bảo đảm (doanh nghiệp nhỏ, tiền gửi vận hành, mạng lưới hợp tác xã, nhóm 40%/20%, nhóm 100%).
  - Lượt 2, 14 trang: tài trợ có bảo đảm, dòng ra phái sinh và các giả định, tài sản bảo đảm và điều khoản hạ xếp hạng, công cụ cấu trúc và SPE.
  - Lượt 3, 12 trang: hạn mức tín dụng và thanh khoản cam kết, nghĩa vụ tài trợ tiềm tàng, dòng ra theo hợp đồng khác.
  - Lượt 4, 11 trang: dòng tiền vào (nguyên tắc, trần 75%, cho vay có bảo đảm, hạn mức, dòng vào theo đối tác).
- **Độ mịn do người dùng chọn:** sau lượt 1, người dùng yêu cầu "đào sâu hơn các khái niệm"; từ lượt 2 mỗi khái niệm mà chuẩn mực định nghĩa hoặc lập luận riêng có một trang, kể cả trang ngắn dựa trên một đoạn.
- **Merge:** `total-expected-cash-inflows` nhận claim 40.91–40.93; khoảng 25 trang có sẵn nhận một câu link (repo, covered bond, chứng khoán hóa, tái thế chấp, xếp hạng tín nhiệm, RCLF, FTP…). Không tạo stub nào.
- Trước đó trong cùng phiên (đã ghi ở handoff `2026-10-12-1624`): xong lô C, dọn dẹp, lint 839 trang.
- **Sai sót đã biết, chưa sửa:** message commit `1231ca7` ghi "review 57 trang", con số đúng là 48; sửa cần force push.

## Kiểm tra đã chạy

- `--all`: 886 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--relations`: 719 trên 4.247 link có loại, 0 cặp lệch, 125 link của trang tổng quan được miễn.
- `--verify-sources`: 203 file trong bản kê, 0 lệch hoặc thiếu, 11 file chưa kê.
- `--coverage basel_lcr`: 9 chunk, phủ 4, dở 1, chưa 3, miễn 1; LCR40 cụm A 88%, cụm B 91%.
- `--graph`: chạy sau mỗi lượt ingest; ảnh chụp cuối với 886 trang, 4.372 link. Thay đổi đáng kể trong bốn lượt: `liquidity-coverage-ratio-lcr`, `high-quality-liquid-assets-hqla` và `total-expected-cash-outflows` vào top 25.
- `--size` và `--style` chỉ được xem cho các trang mới của từng lượt, không chạy `--lint` trọn bộ sau ingest.

## Blocker

Không có việc nào đang kẹt chờ người dùng.

## Việc còn lại

Từ phần ingest LCR40:

- 47 trang ingest từ LCR40 chưa có `reviewed`; nên đưa vào hàng đợi `/review-node`, ưu tiên các trang có bảng tỷ lệ (`secured-funding-run-off-rates-…`, `committed-facility-drawdown-rates-…`, `secured-lending-inflow-rates-…`, `other-inflows-assume-continued-lending-…`).
- Trang tổng quan thanh khoản (`bank-liquidity-rules-pair-a-stressed-30-day-hqla-buffer-with-ratio-limits-on-funding-structure`) chưa phản ánh 47 trang mới của nhóm; cần một lượt `/research` có proposal. Phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
- Nhóm "Thanh khoản và nguồn vốn" trong `index.md` giờ khoảng 85 trang; nên tách nhóm con cho LCR40 (dòng ra, dòng vào).
- Chỗ nguồn `LCR.md` bị cắt giữa câu, đã ghi rõ trên trang: chú thích "bảo hiểm đầy đủ" (d.758) và câu trả lời FAQ2 của đoạn 40.47 (d.940). Cần đối chiếu bản gốc trên bis.org khi review.
- Câu do agent ghép hoặc viết lại, đã ghi rõ trên trang, cần người dùng nói giữ hay bỏ: các mức 15%, 25%, 50% của tài trợ có bảo đảm "trùng" haircut Level 2A và 2B; công thức `max(0, nghĩa vụ − 50% × dòng vào)` cho đoạn 40.66; bảng tỷ lệ rút xếp thành hai cột tín dụng và thanh khoản; bảng dòng vào theo đối tác; nhận xét hạn mức ở tổ chức khác "không đối xứng" với vế dòng ra.
- `basel_lcr` còn theo `--coverage`: LCR31 (d.400–700, stub `alternative-liquidity-approaches` đang chờ), LCR90 (d.1325–1334), LCR99 (d.1335–1421), và mục ngân hàng Shari'ah của LCR30 (d.391–399).
- `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới có trang trích tới phần đầu (đã gặp ở mục "Additional requirements" giữa hai lượt ingest).
- 3.528 link chưa có loại (4.247 trừ 719); trả dần qua `/review-node` và `/ingest`.
- Tỷ lệ link "mạnh" khoảng 11% (476 trên 4.372 link), dưới mục tiêu 15–30% của kế hoạch.

Chép từ handoff `2026-10-12-1624` và các handoff trước, chưa xử lý:

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
- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan đầu tiên:
  - Trang thanh khoản, đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp).
  - Trang IRRBB, đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517. Các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Hàng đợi review: 11 trang trục chưa review của nhóm thanh khoản (chỉ `liquidity-risk` đã review); các trang ingest từ Clippings ngày 2026-09-22 và 23 chưa review, có cùng kiểu lỗi đã gặp (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
- Việc cho lint sau: `supervisory-outlier-test-…` dài 1.144 từ.
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn trước khi dùng để quyết lô D (vector).
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0; số liệu đúng nằm ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
- Ngưỡng thông báo của `--graph` là số tạm, chưa qua một lượt ingest thật.
- `index.md`: gán nhóm theo mục cũ, chưa soát từng trang; hai nhóm lớn nên tách khi ingest thêm ("Công cụ và cơ chế vận hành chính sách tiền tệ", "Thanh khoản và nguồn vốn").
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model; chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`.
- Kế hoạch đồ thị nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A, B, C xong; lô D tuỳ chọn, chưa mở.
- `basel_lcr` LCR30 còn bốn đoạn chưa có trang: 30.26, 30.28, 30.29, 30.47. `--coverage` chỉ báo mục Shari'ah.
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

- `/research` cập nhật trang tổng quan thanh khoản theo 47 trang mới, kèm đề xuất tách nhóm con trong `index.md`.
- `/ingest basel_lcr` LCR31 (phương án thay thế cho đồng tiền thiếu HQLA), rồi LCR99, LCR90 và mục Shari'ah.
- `/review-node` cho các trang LCR40, bắt đầu từ các trang có bảng tỷ lệ; đối chiếu hai chỗ nguồn bị cắt với bản gốc trên bis.org.
- Khi ingest nguồn Basel khác hoặc quy định Việt Nam: đăng ký file vào bản kê trước; `basel/NSF/NSF.md` cho nội dung của stub NSFR.

Các script ingest và review dùng trong phiên nằm trong thư mục tạm của phiên và sẽ mất; cách làm: mỗi lượt một script tạo trang bằng hàm `new(...)` kèm chú thích `(basel_lcr, LCR40, <mục>, <đoạn>, d.<dòng>)`, rồi `--all`, `--coverage`, `--graph`, ghi log.
