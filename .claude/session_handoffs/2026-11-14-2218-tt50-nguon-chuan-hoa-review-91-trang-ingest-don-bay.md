# Handoff — TT50 chuyển sang nguồn chuẩn hóa, review 91 trang, ingest tỷ lệ đòn bẩy

## Kết quả

**Chưa commit.** Working tree: 96 file sửa, 5 file mới (4 trang wiki + `.claude/skills/normalize-source/` có từ trước phiên); `git diff --stat`: 96 files changed, 701 insertions, 241 deletions.

- Người dùng tự thay nguồn TT50 và TT83 trong `01_sources/` bằng bản chuẩn hóa (`TT50_2026_SBV_normalized.md`, `TT83_2025_SBV_normalized.md`; bản `.md` cũ đã bị xoá). Bản TT50 mới trùng từng byte với `Claude outputs/TT50_2026_SBV_normalized.md`, giữ 2.310 dòng, chữ và số không đổi, nên mọi chú thích `d.N` cũ vẫn đúng.
- `03_state/tt50_2026_sbv.md`: `file:` trỏ bản chuẩn hóa, thêm ghi chú về địa chỉ `<!-- @Đ… -->`. `03_state/_sources_manifest.md`: dòng TT50 đổi đường dẫn, 271.053 byte, SHA-256 `ee0577dd…efbf700d`.
- `/review-node` 19 lượt (log 2026-11-14 21-22-00 → 22-09-56): **91/91 trang dẫn `tt50_2026_sbv` đặt `reviewed: 2026-11-14`, `reviewed_by: model`**; 42 trang sửa claim, 0 trang giữ lại, 0 Conflict mới. Mọi link trên 91 trang đã gắn loại quan hệ. Loại lỗi chính: câu "suy ra" xếp sai nhóm hệ số (vd DNNVV không đủ điều kiện là 40% chứ không 100%; phần vượt mức tiền gửi hoạt động xếp theo bên gửi), đếm sai ("năm điều kiện" liệt kê bốn), câu cũ "Phần C/Phụ lục I chưa nạp", claim nguồn không nói (vd "trần 15% Level 2B giữ nguyên" dưới Option 3).
- `/ingest` Điều 8 + Phụ lục III (log 22-17-06): tạo `leverage-ratio-lev`, `tt50-leverage-exposure-measure-adds-on-balance-…`, `tt50-leverage-on-balance-exposure-…`, `tt50-leverage-derivative-exposure-is-1-4-times-…`; chèn link vào `circular-50-2026-tt-nhnn-…`, thêm câu nối ở hai trang NSFR phái sinh; thêm khối "Tỷ lệ đòn bẩy ở Việt Nam" vào `index.md`.
- Không tạo stub mới. Không ghi `decisions.md`, `_inbox.md`.

## Kiểm tra đã chạy

- `--verify-sources` (sau khi sửa `03_state`): 203 file trong bản kê, 0 lệch/thiếu, 11 file `.md`/`.pdf` chưa kê.
- `--coverage tt50_2026_sbv` (cuối phiên): phu 8, do 2, chua 6, mien 1. Mới `phu`: d.259–276 (78%), d.2176–2281 (89%).
- `--all` (cuối phiên): 989 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--style`: 0 cờ trên các trang sửa/tạo trong phiên (các cờ `rule6:nên` do câu agent viết đã sửa ngay).
- `--size`: 4 trang mới và các trang dài đã sửa (`level-1-assets`, `total-expected-cash-outflows`, `high-quality-liquid-assets-hqla`, `tt50-hqla-tiers-…`) đều dưới ngưỡng.
- `--relations`: 1.252/4.785 link đã gán loại, 0 cặp lệch.
- `--graph` (cuối phiên): 989 trang, 5.004 link (513 mạnh); nhóm đòn bẩy ↔ nhóm LCR độ mạnh 0→6, ↔ nhóm NSFR 0→12; `leverage-ratio-lev` là điểm nối duy nhất nhóm LCR ↔ nhóm đòn bẩy; top 25: vào `supervisory-outlier-test-…`, ra `gdp-deflator`. Ảnh chụp đã lưu.
- Chưa chạy: `--lint` trọn bộ, `source-verifier`, review cho 4 trang đòn bẩy mới.

## Việc còn lại

Từ phiên này:

- **4 trang đòn bẩy mới chưa `reviewed`**; hai trang NSFR phái sinh có thêm một câu nối sau khi đã review (cùng ngày, lint không bắt).
- **`decisions.md` chưa ghi** việc wiki dẫn bản chuẩn hóa của TT50 (đã đề xuất, người dùng chưa trả lời).
- **Chữ "hoặc" ở Phụ lục I Phần B mục IV khoản 2.2b (d.1685):** điều kiện tài sản bảo đảm nhận từ đối tác "không bị ràng buộc hoặc không phát sinh từ việc thế chấp lại"; trang `collateral-valuation-changes-…` ghi theo chữ văn bản. Có thể Basel ý là "và"; chưa đối chiếu `basel_lcr`, chưa ghi `_inbox.md` (đã hỏi, chưa có trả lời).
- **Thư mục `TT14_2025_SBV/` có cả bản gốc và bản chuẩn hóa**; nếu dùng bản chuẩn hóa thì nên bỏ bản gốc trước khi ingest để chú thích không dẫn nhầm. TT83 đã thay nhưng chưa có source id.
- Chuyển từ phiên 2026-11-10, còn mở:
  - **41 "LINK MẤT"** do `--graph` báo so với HEAD trước merge, ví dụ `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` → `ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation`. Chưa kiểm từng link; đều là trang remote, nhiều khả năng do lint remote gỡ. Đối chiếu với diff `origin/main` nếu cần.
  - **Script ghi file:** các script phải mở file với `newline="\n"` (script cũ ghi CRLF, gây diff cả file). Cách dùng: viết script Python vào scratchpad bằng Write rồi chạy, vì heredoc bash lỗi với dấu nháy tiếng Việt.
  - **Văn bản ngoài TT50 được dẫn, cần ingest thêm** (đã ghi tại chỗ dẫn và `_inbox.md`): Thông tư 41/2016/TT-NHNN (sửa đổi bởi 22/2019, 22/2023) và Thông tư 14/2025/TT-NHNN (cấu phần vốn, vốn cấp 1, hệ số rủi ro, bất động sản, định nghĩa vỡ nợ, tổ chức tài chính quốc tế, xếp hạng tín nhiệm, PFE, CCF, rủi ro tín dụng đối tác của repo); khoản 9 Phụ lục II của thông tư vốn (điều kiện thỏa thuận bù trừ hai bên đủ điều kiện, Điều 25 khoản 1); quy định chế độ báo cáo thống kê (báo cáo NSFR riêng lẻ, Điều 22 khoản 4); quy định phân loại tài sản có/CIC (Phụ lục I phần C mục I); Thông tư 83/2025/TT-NHNN (quản lý rủi ro thanh khoản, stress test).
  - **Chunk TT50 chưa ingest:** Điều 4–5 (d.141–194, chunk `do`); Chương II Mục 1 Điều 6–7 (d.195–258, vốn điều lệ); Mục 3 Điều 9–11 (d.277–372, giới hạn cấp tín dụng); Mục 4 Điều 12 (d.373–440, LDR); Mục 6–7 Điều 28–29 (d.955–1012, trái phiếu Chính phủ, góp vốn); Chương III Điều 30–38 (d.1013–1132, 6 mục chưa phủ: Điều 30, 32, 33, 35, 36, 38); Phụ lục IV (công bố, d.2282–2310; trang Điều 27 `tt50-banks-disclose-…` còn ghi "Phụ lục IV chưa nạp").
  - **Cross-ref đang treo trong wiki:** Điều 28 so với điểm 3d mục II Phụ lục I (`level-1-assets`, `tt50-hqla-tiers-differ-from-basel-…`); Điều 4 khoản 5 (`foreign-bank-branches-may-count-parent-bank-committed-lines-…`); ngưỡng NSFR 100% ngay cho nhóm áp thẳng chỉ suy từ Điều 13 (Điều 22 khoản 2 không có dòng cho nhóm này).
  - **Điểm mở ở `contractual-disbursement-obligations-run-off-at-100-percent-…-in-tt50`:** tổng dòng vào dùng cho ngưỡng 50% ở khoản 2.2 là số gộp hay sau hệ số thu tiền; tính hai lần dòng vào với trần 75% (Điều 21); xử lý nghĩa vụ ngoại tệ; nhóm Bảo hiểm tiền gửi, Kho bạc, UBND tỉnh, tổ chức tài chính quốc tế gần chắc thuộc 2.2 (suy từ Phần C, chưa được khoản 2 nói thẳng). Phần C không trả lời.
  - **So sánh TT50–Basel chưa làm:** hệ số run-off và hệ số thu tiền (Phụ lục I phần B, C) với `basel_lcr` LCR40; quy tắc rổ bảo đảm và tài sản bị ràng buộc một phần (Phụ lục I phần A không có quy tắc rổ, đã xác nhận trong phiên); NSFR với Basel NSFR (`basel/NSF/` chưa ingest, chưa có trong bản kê); LEV với Basel LEV (`basel/LEV/` chưa kê; trang `leverage-ratio-lev` đặt tên chung để merge). Danh sách trang cần so nằm ở `_inbox.md`.
  - `_inbox.md` mục [2026-10-10] về ngoại lệ ingest văn bản quy phạm (mỗi điều một node) chưa quyết; TT50 vẫn được ingest như nguồn thường.
  - Phụ lục II: dấu "—" trong các bảng ASF/RSF được đọc là ô trống của biểu mẫu gốc (kỳ hạn không áp dụng), là suy luận, đã ghi trên trang.
- Chuyển từ handoff `2026-10-13-1144-lint-review-lcr40-va-nap-het-basel-lcr.md` và các handoff cũ hơn, còn mở:
  - 13 trang mới chưa có `reviewed`: 7 trang LCR31, `alternative-liquidity-approaches`, `sharia-compliant-banks-…`, bốn trang tổng quan LCR. Người dùng nói chưa cần review vội.
  - Trang `securities-lending-programmes-and-central-bank-collateral-swaps` viết "giữa các bên thị trường", đoạn 40.46 (d.917) không có; chờ `/review-node` (đã ghi `_inbox.md`).
  - Hai `⚠️ Conflict` chờ người dùng đối chiếu bản gốc trên bis.org (đã ghi `_inbox.md`): `downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade` (cùng một FAQ, `LCR.md` d.978–980 ghi "40.51, 40.52 and 40.56", d.1008–1010 ghi "…40.55"; trang chưa có `reviewed`) và `the-hqla-stock-weights-…` (ngưỡng dưới trái phiếu doanh nghiệp Level 2B là BBB− ở 30.45 d.325–332, bảng 99.1 d.1352 ghi "A+ and BBB", có thể mất dấu trừ khi chuyển file).
  - Chú thích trên ba trang tổng quan dòng ra, dòng vào, tử số ghi theo bảng (một dải đoạn cho cả bảng), lấy từ trang con đã review, không mở lại nguồn cho từng dòng.
  - Trang `bank-liquidity-rules-pair-…` ở đúng 1.000 từ; lượt bổ sung NSFR phải tách trước. Trang này chưa nhắc LCR31.
  - Trang `lcr-net-outflows-…` đứng đầu nhóm "LCR: tổng dòng tiền ra ròng (mẫu số)"; các đoạn lặp một phần nội dung hai trang tổng quan dòng ra và dòng vào.
  - Trang `hqla-insufficiency-…`: đã bỏ phương trình "phần thiếu = cầu − cung" do agent viết lại từ 31.27 để trang xuống dưới 1.000 từ.
  - Lệch dấu câu trong nguồn, không đánh Conflict: 40.64 khoản (5) "insurance companies, fiduciaries, and beneficiaries" và khoản (6) "insurance companies' fiduciaries and beneficiaries".
  - Quyết định của người dùng "tối thiểu là dạng chỉ tiêu, không đánh Conflict" (ba chỗ LCR99 ghi 10%, 50%, 0–5% so với LCR40) chưa có trong `decisions.md`.
  - Nhóm G của lint (người dùng bảo bỏ qua): `LCR.md` bị cắt giữa câu ở d.758 (chú thích "bảo hiểm đầy đủ") và d.940 (FAQ2 của đoạn 40.47).
  - Stub: cả wiki khoảng 37 stub; `intraday-liquidity` chờ nguồn khác; `deposit-insurance` chờ `cargill_central_bank_policy`; `loan-to-deposit-ratio-ldr` chờ Điều 12.
  - `_inbox.md` còn 12 khái niệm ALM chờ ingest `basel/NSF/`, `basel/IRRBB-d368/`.
  - `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới có trang trích tới phần đầu.
  - Link chưa có loại: khoảng 3.530 trên 4.785; tỷ lệ link mạnh khoảng 10%, dưới mục tiêu 15–30% của kế hoạch đồ thị. Phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
  - Ba trang tách từ `repo-specialness-…` chưa có `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`.
  - Hai trang vượt ngưỡng kích thước: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và chuỗi CRR) và `supervisory-irrbb-reporting-…` (một đoạn 730 từ); `supervisory-outlier-test-…` dài 1.144 từ.
  - 11 file nguồn chưa kê, người dùng muốn đăng ký khi ingest: `basel/BaselFramework/BaselFramework.md`, `basel/IRRBB-d368/d368_irrbb.md`, `basel/LEV/LEV.md`, `basel/NSF/NSF.md`, `Clippings/ALM P11 TT50(P4)…`, `vietnam-regulator/alm/ftp_transmission_analysis.md`, `TT14_2025_SBV/14_2025_TT-NHNN.md`, `TT14_2025_SBV/14_2025_TT-NHNN_normalized.md`, `TT83_2025_SBV/TT83_2025_SBV.pdf`, `TT83_2025_SBV/TT83_2025_SBV_normalized.md`, `VAB - Phương pháp luận FTP/VAB - Phương pháp luận FTP.md`.
  - `tata_bank_alm` còn 15 mục chưa phủ theo `--coverage`, rải ở Ch.1, Ch.2 cụm A và B, Ch.3, Ch.5, Ch.6.
  - Message commit `1231ca7` ghi "review 57 trang", đúng là 48; sửa cần người dùng yêu cầu force push.
  - Đối chiếu con số duration 2,17 (trang replicating portfolios) với PDF gốc của Tata nếu có.
  - `--graph` chưa nhận ra thao tác đổi tên trang (in thành "LINK MẤT").
  - Chưa xuất báo cáo research cho bốn nhóm của lô C vào `Claude outputs/`.
  - Câu chưa truy được tới dòng nguồn trên hai trang tổng quan đầu tiên: trang thanh khoản đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp); trang IRRBB đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
  - Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517; các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
  - Hàng đợi review: các trang trục chưa review của nhóm thanh khoản (`liquidity-coverage-ratio-lcr`, `lcr-stress-scenario-…`; `high-quality-liquid-assets-hqla` đã review trong phiên này); các trang ingest từ Clippings ngày 2026-09-22 và 23 chưa review, có cùng kiểu lỗi đã gặp (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
  - Bộ tiêu chí `query/evals/evals.json` cần viết lại cho khó hơn trước khi dùng để quyết lô D (vector). `benchmark.json` của `skill-creator` ra toàn số 0; số liệu đúng ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
  - Ngưỡng thông báo của `--graph` là số tạm. `index.md`: gán nhóm theo mục cũ, chưa soát từng trang; nhóm "Công cụ và cơ chế vận hành chính sách tiền tệ" nên tách khi ingest thêm.
  - `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
  - Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
  - Loại quan hệ của các link là phán đoán của model, chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`. Kế hoạch đồ thị nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`; lô A, B, C xong, lô D tuỳ chọn.
  - Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; trang trần 40%/15% dùng công thức dựng lại từ lời văn, cần đối chiếu bản gốc trên bis.org. TT50 Phụ lục I phần A cho công thức KĐC15%/KĐC40% khớp bản dựng lại (trang đã ghi rõ TT50 chỉ ủng hộ, không thay công thức Basel).
  - Câu minh hoạ ngoài nguồn trên các trang LCR (ví dụ 150/100, repo 7 ngày, chênh phí 25 điểm cơ bản…); người dùng chưa nói giữ hay bỏ.
  - `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest cần ghi `bỏ qua` cho phần trùng.
  - Hook `PreToolUse` cho `--guard-sources` chưa được thử với một lệnh ghi thật vào `01_sources/`; lệnh shell có thể vẫn ghi được vào `01_sources/`.
  - Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json`.
  - Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; cần quét lại trước khi dùng.
  - `lint` và `promote` chưa có evals; chưa chạy 3 eval `research` bằng `skill-creator`.
  - Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
  - `README.md:27` liệt kê skill thiếu `research`.
  - `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ (during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4); quyết định [2026-09-26] là hạ về `[~]`, chưa ingest bù, chưa đổi `03_state/`. Đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy` (16 mục).
  - Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6` (patch conflict, một số thay thế lệch nghĩa); chờ người dùng quyết.
  - `--style` báo 319/790 trang, `--size` 154 trang (số cũ), 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
  - Vặt trong schema và hook: `ingest/SKILL.md:13` ghi "(§1–§12)"; `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang"; schema, skill và docstring hook còn dùng dạng `§7.5`; docstring `--tags`, `--style` hỏng chữ, còn "luat cung 1"; `CLAUDE.md` 999 từ, muốn rút thì cắt câu mở đầu mục "Khởi động".
  - Hook kiểm trang không hiểu `[[trang\|nhãn]]` trong bảng markdown (báo link chết); trong bảng phải dùng `[[trang]]` không nhãn.
  - Mở phiên mới để xác nhận: handoff tự hiện đầu phiên; danh sách skill không còn `engineering:*`, `design:*`, `harness`; yêu cầu sửa thử một file trong `01_sources/` bị từ chối; "dùng source-verifier kiểm trang cpi" chạy được; chạy thử một lượt `/query` xem bước mồi có dẫn tới đọc §13 không.

## Bước tiếp theo

- Commit toàn bộ thay đổi của phiên (kèm file handoff này) khi người dùng yêu cầu; push chỉ khi người dùng nói.
- `/ingest` TT50 Phụ lục IV (d.2282–2310), merge vào `tt50-banks-disclose-liquidity-ratios-…` và bỏ câu "Phụ lục IV chưa nạp"; rồi Điều 4–5, Điều 6–7, 9–12, 28–29, 30–38.
- `/review-node` 4 trang đòn bẩy mới.
- Hỏi lại người dùng: ghi `decisions.md` về nguồn chuẩn hóa TT50; ghi `_inbox.md` về chữ "hoặc" ở d.1685.
- Làm so sánh TT50–Basel về hệ số run-off và thu tiền: đọc danh sách trang trong `_inbox.md`, trình proposal trước khi viết.
- Khi ingest Thông tư 14/2025, 41/2016 và quy định chế độ báo cáo: đóng các chỗ "cần ingest thêm" trên các trang NSFR, Phụ lục II, Điều 22–27 và 4 trang đòn bẩy.
