# Handoff — ingest TT50 (Điều 14, Phụ lục I–II, NSFR Điều 22–27) và merge với origin/main

## Kết quả

Đã commit và push lên `origin/main`; working tree sạch trước khi tạo file handoff này (file này mới, chưa commit).

- Commit `a117f6e`: 100 file (79 trang wiki mới, 16 trang sửa), gồm cả phần TT50 của phiên 2026-11-09 chưa commit trước đó.
- Merge `7917593` (`origin/main` vào `main`): 18 xung đột đã giải. Nguyên nhân gốc là các script cũ ghi file với CRLF; đã chuẩn hóa 146 file về LF. Trang wiki: hợp nhất frontmatter (sources, `last_updated` mới nhất, field quan hệ của remote) và đoạn thân bài hai phía. `index.md` lấy bố cục lĩnh vực của remote, thêm 7 khối TT50 vào lĩnh vực "Ngân hàng: ALM, rủi ro lãi suất và thanh khoản". `log.md` giữ cả hai phía (remote trước). `_inbox.md` không khôi phục mục remote đã triage. Bản kê bỏ 6 dòng file không còn trên đĩa (theo lint remote) và 2 dòng TT50 đã chuyển sang mục riêng.
- `net-stable-funding-ratio-nsfr`: giữ thân TT50, hợp nhất tags; bỏ câu stub `tata_bank_alm` của remote vì không có chú thích dòng.
- `level-2a-assets`: bỏ câu "không làm thay đổi ⚠️ Conflict" ở đoạn TT50 vì remote đã xử lý conflict AA− so với Bindseil.
- Các lượt ingest `tt50_2026_sbv` trong phiên (log `2026-11-10`): Điều 14 (18-34-02); Phụ lục I phần A (18-57-17); phần B B1 (19-04-20) và B2 (19-07-50, mục log này ghi nhầm Conflict, đã đính chính ở 19-46-26); bổ sung tiêu chí mục V khoản 2 (21-05-00); phần C dòng tiền vào (21-18-28); Phụ lục II NSFR (21-36-01); cụm B Điều 22–27 (22-49-55). Không có mục log cho merge (không thuộc 5 operation).
- Chunk TT50 đã `phu`: d.441–722, 723–954, 1133–1393, 1394–1857, 1858–2004, 2005–2175. Không ghi `bỏ qua:` nào.
- Quyết định của người dùng trong phiên: biểu mẫu mục 5.2.2 khớp mục V khoản 2.2 (100% áp lên phần vượt 50% dòng vào), không phải Conflict; mọi văn bản ngoài thông tư được dẫn thì ghi "cần ingest thêm" tại chỗ dẫn; phải đọc và viết 100% nội dung từng điều; hoãn so sánh TT50–Basel về hệ số run-off, thu tiền (đã nạp xong `basel_lcr` ở remote, có thể làm).

## Kiểm tra đã chạy

Trong phiên này, sau merge:

- `--all`: 985 trang, 0 vấn đề, 0 mồ côi, 0 sót index (chạy lại sau lần sửa index cuối).
- `--verify-sources`: 203 file trong bản kê, 0 lệch/thiếu, 11 file `.md`/`.pdf` chưa kê (TT83_2025_SBV, VAB FTP... và các file khác có từ trước).
- `--coverage tt50_2026_sbv`: phu d.441–722, 723–954, 1133–1393, 1394–1857, 1858–2004, 2005–2175; `do` d.25–194 (Điều 4, 5 chưa phủ) và d.1013–1132 (6 mục); `chua` d.195–440, 955–1012, 2176–2310; `mien` d.1–24.
- `--style`, `--size` lọc theo các trang TT50 mới: không còn cờ sau khi sửa (lọc bằng `grep`, chưa chạy toàn bộ).
- `--graph`: +78 trang, +583 link, −41 link, 461 link vừa được gắn loại, 0 đổi loại so với ảnh chụp 2026-10-13; ảnh chụp đã lưu (vào merge commit).
- `--relations`: 825/4.767 link đã gán loại, 0 cặp lệch.
- Chưa chạy: `--lint` trọn bộ, `source-verifier`, `/review-node` cho bất kỳ trang nào của phiên này.

## Việc còn lại

Từ phiên này:

- **Gắn loại quan hệ cho trang TT50.** Remote đổi quy ước (§6: field `part_of`, `has_part`, `governs`, `governed_by`, `drives`, `driven_by`, `contrasts`, `analogous`, `related` ở frontmatter). Khoảng 79 trang TT50 mới (gồm trang phiên 2026-11-09) và các link chèn vào trang cũ viết trước merge nên chưa có loại. Không có lệnh báo lỗi, nhưng phải đọc câu chứa từng link để chọn loại.
- **41 "LINK MẤT"** do `--graph` báo so với HEAD trước merge, ví dụ `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` → `ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation`. Chưa kiểm từng link; đều là trang remote, nhiều khả năng do lint remote gỡ. Đối chiếu với diff `origin/main` nếu cần.
- **Script ghi file:** các script phải mở file với `newline="\n"` (script cũ ghi CRLF, gây diff cả file). Cách dùng: viết script Python vào scratchpad bằng Write rồi chạy, vì heredoc bash lỗi với dấu nháy tiếng Việt.
- **Văn bản ngoài TT50 được dẫn, cần ingest thêm** (đã ghi tại chỗ dẫn và `_inbox.md`): Thông tư 41/2016/TT-NHNN (sửa đổi bởi 22/2019, 22/2023) và Thông tư 14/2025/TT-NHNN (cấu phần vốn, hệ số rủi ro, bất động sản, định nghĩa vỡ nợ, tổ chức tài chính quốc tế, xếp hạng tín nhiệm); khoản 9 Phụ lục II của thông tư vốn (điều kiện thỏa thuận bù trừ hai bên đủ điều kiện, Điều 25 khoản 1); quy định chế độ báo cáo thống kê (báo cáo NSFR riêng lẻ, Điều 22 khoản 4); quy định phân loại tài sản có/CIC (Phụ lục I phần C mục I).
- **Chunk TT50 chưa ingest:** Điều 4–5 (d.141–194); Điều 6–12 (d.195–440: vốn điều lệ, đòn bẩy Điều 8, giới hạn cấp tín dụng Điều 9–11, LDR Điều 12); Điều 28–29 (d.955–1012: trái phiếu Chính phủ, góp vốn); Chương III Điều 30–38 (d.1013–1132, 6 mục chưa phủ: Điều 30, 32, 33, 35, 36, 38); Phụ lục III (đòn bẩy, d.2176–2281); Phụ lục IV (công bố, d.2282–2310; trang Điều 27 `tt50-banks-disclose-…` chưa có nội dung công bố cụ thể).
- **Cross-ref đang treo trong wiki:** Điều 28 so với điểm 3d mục II Phụ lục I (`level-1-assets`, `tt50-hqla-tiers-differ-from-basel-…`); Điều 4 khoản 5 (`foreign-bank-branches-may-count-parent-bank-committed-lines-…`); ngưỡng NSFR 100% ngay cho nhóm áp thẳng chỉ suy từ Điều 13 (Điều 22 khoản 2 không có dòng cho nhóm này).
- **Điểm mở ở `contractual-disbursement-obligations-run-off-at-100-percent-…-in-tt50`:** tổng dòng vào dùng cho ngưỡng 50% ở khoản 2.2 là số gộp hay sau hệ số thu tiền; tính hai lần dòng vào với trần 75% (Điều 21); xử lý nghĩa vụ ngoại tệ; nhóm Bảo hiểm tiền gửi, Kho bạc, UBND tỉnh, tổ chức tài chính quốc tế gần chắc thuộc 2.2 (suy từ Phần C, chưa được khoản 2 nói thẳng). Phần C không trả lời.
- **So sánh TT50–Basel chưa làm:** hệ số run-off và hệ số thu tiền (Phụ lục I phần B, C) với `basel_lcr` LCR40 (đã ingest ở remote); quy tắc rổ bảo đảm và tài sản bị ràng buộc một phần (Phụ lục I phần A); NSFR với Basel NSFR (`basel/NSF/` chưa ingest, chưa có trong bản kê). Danh sách trang cần so nằm ở `_inbox.md`.
- Trang đã đánh dấu suy luận (nguồn không nói thẳng) rải trên các trang TT50; cân nhắc `/review-node`, ưu tiên 4 trang `analysis` so sánh TT50–Basel, trang ngưỡng 90%, và các trang Điều 14 và NSFR.
- `_inbox.md` mục [2026-10-10] về ngoại lệ ingest văn bản quy phạm (mỗi điều một node) chưa quyết; TT50 vẫn được ingest như nguồn thường.
- Phụ lục II: dấu "—" trong các bảng ASF/RSF được đọc là ô trống của biểu mẫu gốc (kỳ hạn không áp dụng), là suy luận, đã ghi trên trang.

Từ handoff `2026-10-13-1144-lint-review-lcr40-va-nap-het-basel-lcr.md` (phiên khác, đã merge) và các handoff cũ hơn trong chuỗi, chưa xử lý, chép nguyên:

- 13 trang mới chưa có `reviewed`: 7 trang LCR31, `alternative-liquidity-approaches`, `sharia-compliant-banks-…`, bốn trang tổng quan LCR. Người dùng nói chưa cần review vội.
- Trang `securities-lending-programmes-and-central-bank-collateral-swaps` viết "giữa các bên thị trường", đoạn 40.46 (d.917) không có; chờ `/review-node` (đã ghi `_inbox.md`).
- Hai `⚠️ Conflict` chờ người dùng đối chiếu bản gốc trên bis.org (đã ghi `_inbox.md`): `downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade` (cùng một FAQ, `LCR.md` d.978–980 ghi "40.51, 40.52 and 40.56", d.1008–1010 ghi "…40.55"; trang chưa có `reviewed`) và `the-hqla-stock-weights-…` (ngưỡng dưới trái phiếu doanh nghiệp Level 2B là BBB− ở 30.45 d.325–332, bảng 99.1 d.1352 ghi "A+ and BBB", có thể mất dấu trừ khi chuyển file).
- Chú thích trên ba trang tổng quan dòng ra, dòng vào, tử số ghi theo bảng (một dải đoạn cho cả bảng), lấy từ trang con đã review, không mở lại nguồn cho từng dòng.
- Trang `bank-liquidity-rules-pair-…` ở đúng 1.000 từ; lượt bổ sung NSFR phải tách trước. Trang này chưa nhắc LCR31.
- Trang `lcr-net-outflows-…` đứng đầu nhóm "LCR: tổng dòng tiền ra ròng (mẫu số)"; các đoạn lặp một phần nội dung hai trang tổng quan dòng ra và dòng vào.
- Trang `hqla-insufficiency-…`: đã bỏ phương trình "phần thiếu = cầu − cung" do agent viết lại từ 31.27 để trang xuống dưới 1.000 từ.
- Lệch dấu câu trong nguồn, không đánh Conflict: 40.64 khoản (5) "insurance companies, fiduciaries, and beneficiaries" và khoản (6) "insurance companies' fiduciaries and beneficiaries".
- Quyết định của người dùng "tối thiểu là dạng chỉ tiêu, không đánh Conflict" (ba chỗ LCR99 ghi 10%, 50%, 0–5% so với LCR40) chưa có trong `decisions.md`.
- Nhóm G của lint (người dùng bảo bỏ qua): 11 file nguồn chưa kê; `LCR.md` bị cắt giữa câu ở d.758 (chú thích "bảo hiểm đầy đủ") và d.940 (FAQ2 của đoạn 40.47).
- Stub: cả wiki khoảng 38 stub; `intraday-liquidity` chờ nguồn khác; `deposit-insurance` chờ `cargill_central_bank_policy`; `loan-to-deposit-ratio-ldr` chờ Điều 12.
- `_inbox.md` còn 12 khái niệm ALM chờ ingest `basel/NSF/`, `basel/IRRBB-d368/`.
- `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới có trang trích tới phần đầu.
- Link chưa có loại: khoảng 3.900 trên 4.767; tỷ lệ link mạnh khoảng 11%, dưới mục tiêu 15–30% của kế hoạch đồ thị. Phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
- Ba trang tách từ `repo-specialness-…` chưa có `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`.
- Hai trang vượt ngưỡng kích thước: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và chuỗi CRR) và `supervisory-irrbb-reporting-…` (một đoạn 730 từ); `supervisory-outlier-test-…` dài 1.144 từ.
- 11 file nguồn chưa kê, người dùng muốn đăng ký khi ingest: `basel/BaselFramework/`, `basel/IRRBB-d368/`, `basel/LEV/`, `basel/NSF/`, `Clippings/ALM P11 TT50(P4)…`, và 6 file dưới `vietnam-regulator/alm/`.
- `tata_bank_alm` còn 15 mục chưa phủ theo `--coverage`, rải ở Ch.1, Ch.2 cụm A và B, Ch.3, Ch.5, Ch.6.
- Message commit `1231ca7` ghi "review 57 trang", đúng là 48; sửa cần người dùng yêu cầu force push.
- Đối chiếu con số duration 2,17 (trang replicating portfolios) với PDF gốc của Tata nếu có.
- `--graph` chưa nhận ra thao tác đổi tên trang (in thành "LINK MẤT").
- Chưa xuất báo cáo research cho bốn nhóm của lô C vào `Claude outputs/`.
- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan đầu tiên: trang thanh khoản đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp); trang IRRBB đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517; các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Hàng đợi review: 11 trang trục chưa review của nhóm thanh khoản (`high-quality-liquid-assets-hqla`, `liquidity-coverage-ratio-lcr`, `lcr-stress-scenario-…` vừa nhận thêm claim); các trang ingest từ Clippings ngày 2026-09-22 và 23 chưa review, có cùng kiểu lỗi đã gặp (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
- Bộ tiêu chí `query/evals/evals.json` cần viết lại cho khó hơn trước khi dùng để quyết lô D (vector). `benchmark.json` của `skill-creator` ra toàn số 0; số liệu đúng ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
- Ngưỡng thông báo của `--graph` là số tạm. `index.md`: gán nhóm theo mục cũ, chưa soát từng trang; nhóm "Công cụ và cơ chế vận hành chính sách tiền tệ" nên tách khi ingest thêm.
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model, chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`. Kế hoạch đồ thị nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`; lô A, B, C xong, lô D tuỳ chọn.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; trang trần 40%/15% dùng công thức dựng lại từ lời văn, cần đối chiếu bản gốc trên bis.org. TT50 Phụ lục I phần A đã cho công thức KĐC15%/KĐC40% khớp bản dựng lại.
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

- Commit và push file handoff này khi người dùng yêu cầu.
- Gắn loại quan hệ cho các trang TT50 (sổ sách, không cần hỏi; đọc từng câu chứa link, không rõ thì `related`), rồi `--all` và `--graph`.
- `/ingest` TT50 tiếp theo ý người dùng: Phụ lục III (đòn bẩy) và Phụ lục IV (công bố) để trang Điều 27 có nội dung, rồi Điều 4–5, 6–12, 28–29, 30–38.
- Làm so sánh TT50–Basel về hệ số run-off và thu tiền, nay `basel_lcr` đã nạp đủ: đọc danh sách trang trong `_inbox.md`, trình proposal trước khi viết.
- Khi ingest Thông tư 14/2025, 41/2016 và quy định chế độ báo cáo: đóng các chỗ "cần ingest thêm" đã ghi trên trang NSFR, Phụ lục II và Điều 22–27.
