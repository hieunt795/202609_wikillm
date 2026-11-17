# Handoff — TT83: khép phần IRRBB, nạp ALM/ALCO/ba tuyến bảo vệ và ICAAP; review 5 trang

## Kết quả

**Chưa commit.** Working tree: 15 file sửa, 13 file mới (12 trang wiki + `.claude/skills/normalize-source/` có từ trước); `git diff --stat`: 15 files changed, 299 insertions, 218 deletions. Thay đổi của handoff trước (lượt IRRBB 2026-11-15) đã nằm trong commit `6a015ee`.

Bốn operation, mỗi cái một mục trong `log.md`:

- `/ingest` (log 2026-11-17 21-36-50) — TT83 Đ3.K22, K32–K34, Phụ lục VI d.iv: tạo `banking-book`; nâng stub `trading-book` lên draft; merge TT83 vào `interest-rate-gap-risk-…`, `interest-rate-basis-risk-…`, `interest-rate-option-risk-…` (ba trang có `reviewed` 2026-10-12 cũ hơn `last_updated`), và vào `vietnamese-banks-may-measure-irrbb-…-until-end-2027` (công thức $C_E$, $RWA_{IRRBB}$ theo ΔEVE từ 2028).
- `/review-node` (log 21-44-21) — 5 trang theo hàng đợi backlink: đạt `liquidity-coverage-ratio-lcr`, `circular-83-2025-…` (hub), `the-saving-investment-gap-…`; sửa claim `interest-rate-risk-in-the-banking-book-irrbb` (CSRBB, "hai góc đo") và `repurchase-agreement` (specials, bỏ câu không có nguồn, thêm hậu tố file During).
- `/ingest` (log 21-59-03) — TT83 Đ4.K2, Đ6.K4, Đ25: tạo `tt83-alm-unit-runs-the-balance-sheet-funding-plans-ftp-and-pricing-and-polices-liquidity-and-irrbb-limits`, `asset-liability-committee-alco`, `three-lines-of-defence`; merge Đ25.K3.b vào `funds-transfer-pricing-ftp-allocates-…` (nâng `last_updated`, `reviewed` 2026-10-12 cũ hơn).
- `/ingest` (log 22-34-50) — TT83 Mục 9, Phụ lục III, Phụ lục VI: tạo `internal-capital-adequacy-assessment-process-icaap`, `tt83-target-capital-…`, `tt83-concentration-risk-rwa-…`, `tt83-capital-stress-tests-…`, `tt83-capital-plan-…`, `tt83-icaap-is-reviewed-independently-…`, `risk-adjusted-return-on-capital-raroc`; stub `capital-adequacy-ratio-car`.
- `index.md`: 3 nhóm mới (Quản trị ALM TT83; ICAAP TT83) và 2 dòng sổ ngân hàng/sổ kinh doanh. `_inbox.md`: 3 dòng mới (việc hoãn IRRBB đã làm; nguồn thừa ở `repurchase-agreement`; câu hỏi độc lập đo IRRBB vs bộ phận ALM).
- Hub TT83 cố ý không link tới cụm ALM và ICAAP: hub vừa `reviewed` 2026-11-17, thêm câu mới sẽ che claim chưa review; không có câu sẵn hợp để chèn link.

## Kiểm tra đã chạy

- `--all` (cuối phiên): 1015 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--size`, `--style` trên mọi trang tạo/sửa trong phiên: 0 cờ.
- `--coverage tt83_2025_sbv`: phu 6 (Mục 7, Mục 9, Phụ lục III, V A, V B–C, VI), do 5 (Chương I còn Điều 5, 7, 8, 10; Mục 1 còn Điều 17–22, 24; Mục 5 chỉ trích Điều 46 để đối chiếu; Chương V còn Điều 75; Phụ lục II), chua 9, mien 1.
- `--graph` (cuối phiên): 1015 trang, 5141 link (534 mạnh), 1413 đã gắn loại; lượt cuối so với ảnh chụp trước: +8 trang, +49 link (tính so với HEAD), 0 link mất; 1 đổi loại có chủ đích (LCR → kịch bản căng thẳng: `has_part, governed_by` → `governed_by`); nhóm IRRBB Việt Nam ↔ Quản trị ALM TT83 0→14, ↔ ICAAP TT83 0→11. Ảnh chụp đã lưu.
- Chưa chạy: `--lint` trọn bộ, `--verify-sources`.

## Việc còn lại

Từ phiên này:

- **Trang chờ review (TT83/IRRBB):** 13 trang TT83 tạo 2026-11-15 (trừ hub), 3 trang gap/basis/option và `funds-transfer-pricing-ftp-allocates-…` (`reviewed` cũ hơn `last_updated`), `vietnamese-banks-may-measure-irrbb-…`, `banking-book`, `trading-book`, 3 trang ALM/ALCO/ba tuyến, 7 trang ICAAP. Điểm agent tự rút cần soát: trang `$RWA_{COR}$` (sàn tăng qua từng mốc nếu dư nợ không đổi), trang RAROC (mẫu số gồm phần đệm kịch bản bất lợi), trang vốn mục tiêu (phần bất lợi chỉ cần CAR luật định), trang ALCO ("chỉ hội đồng rủi ro bị cấm Tổng giám đốc làm chủ tịch").
- **`repurchase-agreement`** khai `bindseil_monetary_policy`, `cargill_central_bank_policy` trong `sources:` nhưng không còn claim dẫn hai nguồn này (đã ghi `_inbox.md`).
- **Câu hỏi mở ALM vs độc lập đo IRRBB** (Đ54.K1.b, Đ25.K3, Đ4.K2) — đã ghi `_inbox.md`, không thành claim.
- **Hub TT83 chưa link** tới cụm ALM, ICAAP; khi review lại hub hoặc ingest Chương I tiếp thì thêm một câu có chú thích.
- **Stub `capital-adequacy-ratio-car`** chờ Thông tư 14/2025 (thông tư vốn).

Từ phiên 2026-11-15 (handoff `2026-11-15-2150-…`), còn mở:

- Điểm agent tự rút trên các trang TT83 cần soát khi review: VND không có trong Bảng 5; dấu ΔEVE của TT83 (EVE₀ − EVEᵢ + KAO) ngược trang EBA SA; "Phụ lục V không quy định sàn sau sốc"; "Mục 7 và Phụ lục V không ghi mức hạn mức bằng số"; hai ví dụ tự tính (lãi suất bình quân 6% → 360/500/240 bp; $S_{short}$ = 0,5 ở khoảng 2,8 năm).
- Câu "Chương III có chín Mục…" trên hub TT83 không có chú thích dòng riêng (chú thích heading Chương III làm `--coverage` báo sai Mục 1–8 đã phủ, nên đã thu hẹp về Đ3.K13 và Đ1.K2).
- Khi nạp Basel IRRBB (d368, d578) thì so tham số Phụ lục V (Bảng 2–6) với Basel.
- Câu "Nội dung của TT83 chưa có trong wiki" trên `liquidity-stress-test-reports-…` nay chỉ đúng với phần thanh khoản (đã ghi `_inbox.md`).
- TT83 còn chưa ingest: Chương I Điều 5, 7, 8, 10; Chương II (Điều 11–16); Chương III Mục 1 Điều 17–22, 24; Mục 2–6, 8; Chương IV; Chương V Điều 75; Phụ lục I, II (phần chung), IV.

Từ phiên 2026-11-14 (handoff `2026-11-14-2218-…`), còn mở:

- 4 trang đòn bẩy mới chưa `reviewed`; hai trang NSFR phái sinh có thêm một câu nối sau khi đã review (cùng ngày, lint không bắt).
- Thư mục `TT14_2025_SBV/` có cả bản gốc và bản chuẩn hóa; nếu dùng bản chuẩn hóa thì nên bỏ bản gốc trước khi ingest để chú thích không dẫn nhầm.
- Chuyển từ phiên 2026-11-10, còn mở:
  - 41 "LINK MẤT" do `--graph` báo so với HEAD trước merge, ví dụ `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` → `ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation`. Chưa kiểm từng link; đều là trang remote, nhiều khả năng do lint remote gỡ. Đối chiếu với diff `origin/main` nếu cần.
  - Script ghi file phải mở file với `newline="\n"` (script cũ ghi CRLF, gây diff cả file). Viết script Python vào scratchpad bằng Write rồi chạy, vì heredoc bash lỗi với dấu nháy tiếng Việt.
  - Văn bản ngoài TT50 được dẫn, cần ingest thêm (đã ghi tại chỗ dẫn và `_inbox.md`): Thông tư 41/2016/TT-NHNN (sửa đổi bởi 22/2019, 22/2023) và Thông tư 14/2025/TT-NHNN (cấu phần vốn, vốn cấp 1, hệ số rủi ro, bất động sản, định nghĩa vỡ nợ, tổ chức tài chính quốc tế, xếp hạng tín nhiệm, PFE, CCF, rủi ro tín dụng đối tác của repo); khoản 9 Phụ lục II của thông tư vốn (điều kiện thỏa thuận bù trừ hai bên đủ điều kiện, Điều 25 khoản 1); quy định chế độ báo cáo thống kê (báo cáo NSFR riêng lẻ, Điều 22 khoản 4); quy định phân loại tài sản có/CIC (Phụ lục I phần C mục I); Thông tư 83/2025/TT-NHNN phần thanh khoản (Mục 5, stress test).
  - Chunk TT50 chưa ingest: Điều 4–5 (d.141–194, chunk `do`); Chương II Mục 1 Điều 6–7 (d.195–258, vốn điều lệ); Mục 3 Điều 9–11 (d.277–372, giới hạn cấp tín dụng); Mục 4 Điều 12 (d.373–440, LDR); Mục 6–7 Điều 28–29 (d.955–1012, trái phiếu Chính phủ, góp vốn); Chương III Điều 30–38 (d.1013–1132, 6 mục chưa phủ: Điều 30, 32, 33, 35, 36, 38); Phụ lục IV (công bố, d.2282–2310; trang Điều 27 `tt50-banks-disclose-…` còn ghi "Phụ lục IV chưa nạp").
  - Cross-ref đang treo: Điều 28 so với điểm 3d mục II Phụ lục I (`level-1-assets`, `tt50-hqla-tiers-differ-from-basel-…`); Điều 4 khoản 5 (`foreign-bank-branches-may-count-parent-bank-committed-lines-…`); ngưỡng NSFR 100% ngay cho nhóm áp thẳng chỉ suy từ Điều 13 (Điều 22 khoản 2 không có dòng cho nhóm này).
  - Điểm mở ở `contractual-disbursement-obligations-run-off-at-100-percent-…-in-tt50`: tổng dòng vào dùng cho ngưỡng 50% ở khoản 2.2 là số gộp hay sau hệ số thu tiền; tính hai lần dòng vào với trần 75% (Điều 21); xử lý nghĩa vụ ngoại tệ; nhóm Bảo hiểm tiền gửi, Kho bạc, UBND tỉnh, tổ chức tài chính quốc tế gần chắc thuộc 2.2 (suy từ Phần C, chưa được khoản 2 nói thẳng).
  - So sánh TT50–Basel chưa làm: hệ số run-off và thu tiền (Phụ lục I phần B, C) với `basel_lcr` LCR40; quy tắc rổ bảo đảm và tài sản bị ràng buộc một phần; NSFR với Basel NSFR (`basel/NSF/` chưa ingest, chưa kê); LEV với Basel LEV (`basel/LEV/` chưa kê; trang `leverage-ratio-lev` đặt tên chung để merge). Danh sách trang cần so nằm ở `_inbox.md`.
  - `_inbox.md` mục [2026-10-10] về ngoại lệ ingest văn bản quy phạm (mỗi điều một node) chưa quyết; TT50, TT83 vẫn ingest như nguồn thường.
  - Phụ lục II TT50: dấu "—" trong bảng ASF/RSF được đọc là ô trống của biểu mẫu gốc, là suy luận, đã ghi trên trang.
- Chuyển từ handoff `2026-10-13-1144-…` và cũ hơn, còn mở:
  - 13 trang chưa `reviewed`: 7 trang LCR31, `alternative-liquidity-approaches`, `sharia-compliant-banks-…`, bốn trang tổng quan LCR. Người dùng nói chưa cần review vội.
  - `securities-lending-programmes-and-central-bank-collateral-swaps` viết "giữa các bên thị trường", đoạn 40.46 (d.917) không có; chờ `/review-node` (đã ghi `_inbox.md`).
  - Hai `⚠️ Conflict` chờ người dùng đối chiếu bản gốc bis.org (đã ghi `_inbox.md`): `downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade` (`LCR.md` d.978–980 ghi "40.51, 40.52 and 40.56", d.1008–1010 ghi "…40.55") và `the-hqla-stock-weights-…` (ngưỡng dưới Level 2B là BBB− ở 30.45 d.325–332, bảng 99.1 d.1352 ghi "A+ and BBB").
  - Chú thích trên ba trang tổng quan dòng ra, dòng vào, tử số ghi theo bảng, lấy từ trang con đã review, không mở lại nguồn cho từng dòng.
  - `bank-liquidity-rules-pair-…` ở đúng 1.000 từ; lượt bổ sung NSFR phải tách trước; trang này chưa nhắc LCR31.
  - `lcr-net-outflows-…` lặp một phần nội dung hai trang tổng quan dòng ra và dòng vào.
  - `hqla-insufficiency-…`: đã bỏ phương trình "phần thiếu = cầu − cung" do agent viết lại từ 31.27.
  - Lệch dấu câu trong nguồn, không đánh Conflict: 40.64 khoản (5) và (6).
  - Quyết định "tối thiểu là dạng chỉ tiêu, không đánh Conflict" (ba chỗ LCR99 ghi 10%, 50%, 0–5% so với LCR40) chưa có trong `decisions.md`.
  - Nhóm G của lint (người dùng bảo bỏ qua): `LCR.md` cắt giữa câu ở d.758 và d.940.
  - Stub: khoảng 38 stub (thêm `capital-adequacy-ratio-car`); `intraday-liquidity` chờ nguồn khác; `deposit-insurance` chờ `cargill_central_bank_policy`; `loan-to-deposit-ratio-ldr` chờ Điều 12 TT50.
  - `_inbox.md` còn 12 khái niệm ALM chờ ingest `basel/NSF/`, `basel/IRRBB-d368/`.
  - `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới trích phần đầu.
  - Link chưa có loại: khoảng 3.730 trên 5.141; tỷ lệ link mạnh khoảng 10%, dưới mục tiêu 15–30%. Kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
  - Ba trang tách từ `repo-specialness-…` chưa `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`.
  - Hai trang vượt ngưỡng: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và CRR) và `supervisory-irrbb-reporting-…` (đoạn 730 từ); `supervisory-outlier-test-…` dài 1.144 từ.
  - 9 file nguồn chưa kê, đăng ký khi ingest: `basel/BaselFramework/BaselFramework.md`, `basel/IRRBB-d368/d368_irrbb.md`, `basel/LEV/LEV.md`, `basel/NSF/NSF.md`, `Clippings/ALM P11 TT50(P4)…`, `vietnam-regulator/alm/ftp_transmission_analysis.md`, `TT14_2025_SBV/14_2025_TT-NHNN.md`, `TT14_2025_SBV/14_2025_TT-NHNN_normalized.md`, `VAB - Phương pháp luận FTP/VAB - Phương pháp luận FTP.md`.
  - `tata_bank_alm` còn 15 mục chưa phủ theo `--coverage` (Ch.1, Ch.2 cụm A và B, Ch.3, Ch.5, Ch.6).
  - Message commit `1231ca7` ghi "review 57 trang", đúng là 48; sửa cần force push.
  - Đối chiếu duration 2,17 (trang replicating portfolios) với PDF gốc Tata nếu có.
  - `--graph` chưa nhận ra đổi tên trang (in thành "LINK MẤT").
  - Chưa xuất báo cáo research cho bốn nhóm lô C vào `Claude outputs/`.
  - Câu chưa truy được tới dòng nguồn: trang thanh khoản tổng quan đoạn 1 và đoạn 9; trang IRRBB đoạn cuối về tiền gửi không kỳ hạn, FTP, SVB (review 2026-11-17 đã đối chiếu các đoạn khác của trang IRRBB, không thấy đoạn này trong thân bài hiện tại — kiểm lại khi lint).
  - Trong 14 trang IRRBB đã review: `receiver-interest-rate-swaps-…` còn trích d.1550 cho 3,63, mới xác nhận ở d.1517; câu nối không chú thích chỉ kiểm bằng từ khoá.
  - Hàng đợi review: `lcr-stress-scenario-…`; các trang ingest từ Clippings 2026-09-22 và 23 có cùng kiểu lỗi (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
  - `query/evals/evals.json` cần viết lại cho khó hơn trước khi quyết lô D (vector); `benchmark.json` của `skill-creator` ra toàn 0, số đúng ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
  - Ngưỡng thông báo `--graph` là số tạm; `index.md` gán nhóm theo mục cũ, nhóm "Công cụ và cơ chế vận hành chính sách tiền tệ" nên tách.
  - `.claude/docs/luong-van-hanh.html` chưa có lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
  - Ba file bản thử trong `Claude outputs/` (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`) chưa xoá; xoá cần người dùng xác nhận.
  - Loại quan hệ của link là phán đoán của model, chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`. Kế hoạch đồ thị: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`; lô A, B, C xong, lô D tuỳ chọn.
  - Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; trang trần 40%/15% dùng công thức dựng lại, cần đối chiếu bis.org.
  - Câu minh hoạ ngoài nguồn trên các trang LCR (150/100, repo 7 ngày, chênh phí 25 điểm cơ bản…); người dùng chưa nói giữ hay bỏ.
  - `BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest ghi `bỏ qua` phần trùng.
  - Hook `PreToolUse` `--guard-sources` chưa thử với lệnh ghi thật vào `01_sources/`.
  - Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển sang `~/.claude/settings.json`.
  - Map `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; quét lại trước khi dùng.
  - `lint` và `promote` chưa có evals; chưa chạy 3 eval `research`.
  - Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
  - `README.md:27` liệt kê skill thiếu `research`.
  - `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ; quyết định [2026-09-26] hạ về `[~]` chưa thực hiện. Đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy`.
  - Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6`; chờ người dùng quyết.
  - `--style` 319/790 trang, `--size` 154 trang (số cũ), 70% tag dùng 1 lần.
  - Vặt schema/hook: `ingest/SKILL.md:13` ghi "(§1–§12)"; §4 có hai hàng cùng tên "Kích thước 1 trang"; còn dạng `§7.5`; docstring `--tags`, `--style` hỏng chữ; `CLAUDE.md` 999 từ.
  - Hook không hiểu `[[trang\|nhãn]]` trong bảng markdown; trong bảng dùng `[[trang]]` không nhãn.
  - Xác nhận ở phiên mới: handoff tự hiện đầu phiên; danh sách skill không còn `engineering:*`, `design:*`, `harness`; sửa thử file trong `01_sources/` bị từ chối; "dùng source-verifier kiểm trang cpi" chạy được; `/query` có đọc §13 không.

## Bước tiếp theo

- Commit toàn bộ thay đổi của phiên (kèm file handoff này) khi người dùng yêu cầu; push chỉ khi người dùng nói.
- `/review-node` các trang TT83 (5/lượt), ưu tiên: `tt83-delta-eve-is-the-largest-sum-…`, `tt83-shock-sizes-…`, `tt83-six-shock-scenarios-…`, `tt83-core-non-maturity-…`, `tt83-target-capital-…`; rồi gap/basis/option, FTP, cụm ALM, cụm ICAAP, 4 trang đòn bẩy.
- `/ingest` TT83 Mục 5 (thanh khoản, Điều 45–49) để đóng chỗ "TT83 chưa có" ở trang stress test thanh khoản; sau đó Mục 1 (Điều 17–22, 24).
- `/ingest` TT50 Phụ lục IV (d.2282–2310), rồi Điều 4–5, 6–7, 9–12, 28–29, 30–38.
- Khi ingest Thông tư 14/2025: nâng stub `capital-adequacy-ratio-car`, đóng các chỗ "cần ingest thêm" trên trang NSFR, Phụ lục II, Điều 22–27 và 4 trang đòn bẩy.
- So sánh TT50–Basel về run-off và thu tiền: đọc danh sách trang trong `_inbox.md`, trình proposal trước khi viết.
