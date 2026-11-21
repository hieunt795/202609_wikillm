# Handoff — xử lý ba ⚠️ Conflict trên trang B02/B04 (VBHN 04)

## Kết quả

**Chưa commit.** 9 file đổi: 5 trang `02_wiki/`, `02_wiki/index.md`, `decisions.md`, `log.md`, `03_state/_graph_snapshot.tsv`.

- Trả lời người dùng: khung BCTC (Chương I–III) và B02 của `vbhn04_2022_sbv` đã nạp đủ theo `--coverage`; 89 trang B02 đều `draft`, 3 trang có `reviewed`.
- `b02-available-for-sale-investment-securities`: gỡ ⚠️ Conflict TK 12. Chú thích (1)(2) dùng "có thể", không loại trừ A.VIII.2; viết lại thành câu mô tả (A.VIII.2 cũng cộng DN TK 121–123, không gắn chú thích (2); A.VIII.3 trừ DC TK 129 tương ứng).
- `b02-other-liabilities`: giữ ⚠️ Conflict, viết lại chính xác: chỉ dòng nhóm B.VII dẫn V.22; VII.2 dẫn V.22.2, VII.3 và VII.4 dẫn V.21, VII.1 không dẫn.
- Conflict B04 dòng 11 (phái sinh): người dùng quyết cột cách lấy số "khoản nợ tài chính" là lỗi đánh máy, dòng 11 lấy chênh lệch A.V. Gỡ Conflict trên trang nhóm thay đổi tài sản/công nợ B04, trang dòng 11 B04, trang A.V B02; sửa 2 dòng `index.md`. Trang chỉ dẫn căn cứ trực tiếp (dòng 20); căn cứ dòng 13 gián tiếp (d.2745–2755) chỉ ghi ở `decisions.md` để giữ quyết định [2026-11-19] gỡ phương pháp gián tiếp.
- `decisions.md`: mục [2026-11-21] B04 dòng 11 lỗi đánh máy, kèm tiền lệ (chỉ áp khi người dùng quyết từng trường hợp).
- 2 mục `lint` trong `log.md` (18-44-54, 20-08-11).

## Kiểm tra đã chạy

- `--all` (sau mỗi lượt sửa, lần cuối sau khi bỏ chú thích gián tiếp): 1247 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--graph`: không thay đổi vượt ngưỡng (3 lần).
- `--style`: không báo trên 5 trang đã sửa.
- `--coverage vbhn04_2022_sbv`: 20 chunk, phu 18, mien 2.
- Chưa chạy: `--lint` trọn bộ, `--verify-sources`, `--relations`.

## Blocker

Chờ người dùng quyết:
- ⚠️ Conflict `b02-other-liabilities`: dòng nhóm B.VII dẫn V.22 (d.1499–1507); dòng con dẫn V.22.2 và V.21; trong B05 V.21 là "Các khoản nợ khác", V.22 là thuế hoãn lại. Có thể quyết theo tiền lệ lỗi đánh máy ở `decisions.md`.
- ⚠️ Conflict `b04-cash-and-cash-equivalents-of-vietnamese-credit-institutions`: B04 dòng VII kê 5 khoản (có tín phiếu Chính phủ, GTCG tái chiết khấu; "tiền mặt tại quỹ", d.2566–2575), B05 VII.34 kê 4 khoản ("tiền mặt và các khoản tương đương tiền tại quỹ", d.4605–4611).
- ⚠️ Conflict B04 hoạt động tài chính dòng 03 (d.2502–2509).
- B02 XII.5 dẫn V.14.3, B05 để dự phòng ở V.14.5 (ghi `_inbox.md`, chưa đánh Conflict).
- Đổi title `b04-changes-in-operating-assets-and-liabilities-are-period-changes-of-b02-lines` (dòng 13, 22 không phải chênh lệch B02).
- Câu "hai mẫu / wiki chỉ ghi phương pháp trực tiếp" trên trang tổng B04.

## Việc còn lại

Từ phiên này:

- **Commit** 9 file nêu ở Kết quả.
- **5 trang sửa trong phiên** vẫn `draft`, chưa `reviewed`.

Từ phiên 2026-11-20 tối (handoff `2026-11-20-2321-…`), còn mở:

- **Review:** 177 trang đã rà đoạn "cách đọc" vẫn chưa đặt `reviewed`; lượt rà chỉ đối chiếu các câu trong đoạn đó, không đọc lại claim ở phần đầu trang. Hàng đợi `/review-node` cho VBHN 04 không đổi.
- **Câu "chưa nạp" và tự quy chiếu còn trong thân bài** ngoài các đoạn đã rà: `b02-loans-to-customers-gross` (tên cụm TK 21–29), trang tổng B04 ("wiki chỉ ghi phương pháp trực tiếp"). Quét lại bằng `grep -n "chưa nạp\|wiki chỉ\|ngoài nguồn này" 02_wiki/*.md` trước lượt lint.
- **Hook `--style` không bắt cụm "Phần sau là cách đọc của wiki"** và cụm "chưa nạp vào wiki"; đề xuất thêm vào danh sách cấm, gộp vào lần sửa hook theo batch.
- **Link mất trong phiên (khoảng 40)** đều có chủ ý theo bảng đã duyệt, gồm 1 link ngoài dự kiến `b02-provision-for-other-on-balance-sheet-assets → b02-provision-for-loans-to-customers`; người dùng có thể muốn thêm lại.
- **Field quan hệ:** script chỉ gắn `related` cho link mới; các link có sẵn chưa có loại (ví dụ về trang tổng B03) để dành cho `/lint --relations`.
- **Bài học kỹ thuật:** `glob` trên Windows trả đường dẫn có `\`, cần đổi sang `/` trước `git show HEAD:`; `--graph` so với ảnh chụp lần chạy trước, nên muốn xem tổng link mất so với HEAD phải chạy trước khi chạy `--graph` lần nữa; script `engine.py`, `lot*.py` ở scratchpad không giữ sau phiên.

Từ phiên 2026-11-20 sáng (handoff `2026-11-20-1941-…`), còn mở:

- **Review:** 179 trang `sources:` có `vbhn04_2022_sbv` chưa `reviewed` (89 B02, khoảng 47 B04, 22 B03, 6 B05 cùng các trang khác). Kiểu lỗi đã gặp, soát kỹ ở lượt sau: câu suy luận không chú thích nằm trong đoạn claim; link đúng chủ đề nhưng sai trang (trang đích không nói điều câu văn gán); bảng tóm tắt bỏ điều kiện "không bao gồm…" của cột cách lấy số liệu; chú thích trỏ vào vùng `bỏ qua` (phương pháp gián tiếp B04, d.2584–3129).
- **Các trang mới trong phiên chưa `reviewed`:** `vamc-special-bonds` (câu giải nghĩa tên VAMC nguồn không ghi), bảng thay đổi vốn chủ sở hữu, tài sản bảo đảm, bên liên quan, bảng định lại lãi suất, bảng kỳ đáo hạn, báo cáo bộ phận, `b05a-…`, `condensed-…` (dòng XI–XII B03b "trước/sau ngày phân phối" không định nghĩa), `foreign-currency-position`.
- **Trang tổng B05** đã bỏ câu chữ ký cuối biểu (d.6034) khi rút gọn; trang đang gần 1.000 từ, thêm nội dung thì tách trước.
- **Wiki chỉ trình bày phương pháp trực tiếp**; B04a và B04b giữa niên độ ghi "trực tiếp hoặc gián tiếp" (đã ghi trên trang giữa niên độ).
- **Vốn ủy thác:** VIII.40.1 là "hoạt động ủy thác", 40.2 là "nhận ủy thác" (chiều gần B.V), 40.2 chỉ có tiêu đề.
- **Bài học kỹ thuật:** lệnh `cat > file` không có stdin vẫn treo (lặp lại phiên này); heredoc bash làm hỏng chuỗi `"\n"` trong Python, dùng `chr(10)`; in tiếng Việt từ Python cần `python -X utf8`; tách câu bằng regex phải phủ chữ hoa tiếng Việt như "Ở"; script `wl.py`, `r1lib.py` ở scratchpad không giữ sau phiên.

Từ phiên 2026-11-19 (handoff `2026-11-19-2340-…`), còn mở:

- **⚠️ Conflict B04 chờ người dùng:** dòng 03 hoạt động tài chính "tiền chi thanh toán" nhưng cách lấy chép câu "tiền nhận được" của dòng 02 (d.2502–2509). Conflict dòng 11 đã xử lý phiên 2026-11-21.
- **Câu còn giữ trên trang tổng B04:** nêu biểu có hai mẫu trực tiếp/gián tiếp (d.2098, d.2585), wiki chỉ ghi trực tiếp; người dùng chưa xác nhận giữ hay bỏ.
- **Mục log 2026-11-19 22-40-17** (thêm dạng max vào hai trang phái sinh B02) ghi op `query`; §12 không có op riêng cho sửa trang sau query. Đổi op thì ghi mục đính chính.
- **Hai node B02 mất câu nối B04** khi gỡ phương pháp gián tiếp: `b02-interest-and-fees-receivable`, `b02-interest-and-fees-payable` (dòng tương ứng chỉ có ở gián tiếp); vẫn được node B04 dòng 01, 02 trỏ tới.
- **`--coverage` B04 báo 47%** vì phần gián tiếp d.2584–3129 là `bỏ qua:` theo duyệt; chunk vẫn `phu`.
- **Bài học kỹ thuật:** wikilink có nhãn `[[a|b]]` trong ô bảng markdown làm vỡ cột; trong bảng dùng `[[a]]`.

Từ phiên 2026-11-19 (handoff `2026-11-19-2222-…`), còn mở:

- **Thiếu tên tài khoản:** cột (5) B02 chỉ có số TK. Tên TK nằm ở `01_sources/vietnam-regulator/accounting/19_VBHN_NHNN_2026_He_thong_tai_khoan_ke_toan.pdf` — chưa kê manifest, chưa ingest. Thân bài `b02-loans-to-customers-gross` còn câu "văn bản chưa nạp vào wiki" về tên các cụm TK 21–29; `_inbox.md` có dòng TK 486.
- **Lỗi bản chuyển đổi ghi trên trang/state:** "Điền 11" (d.349), ngoặc kép thừa Điều 3a (d.108), tên cũ "Bảng cân đối kế toán giữa niên độ" (d.148), "[^77]7" ở B.I, "được và được" ở cột (6) lợi thế thương mại, dòng XII.5 thiếu ô cột (6), "hành chính" thay "hoàn chỉnh" ở chú thích (3), tiêu đề "Báo cáo TTHC" ở ngoại bảng.
- **Tính hiện hành:** căn cứ của VBHN là Luật TCTD 1997, Luật Kế toán 2003; chưa đối chiếu chế độ sau Luật TCTD 2024. Trang ghi "theo VBHN 04/2022".
- **Backlink chưa thêm** từ hai trang IMF `consolidation-nets-out-…` và `foreign-currency-items-in-monetary-statistics-…` về trang mới (thêm cần viết claim mới).
- **Bài học coverage:** dải chunk không có heading (B02) báo `phu` ngay khi có một chú thích trích vào dải; trong phiên phải ghi tiến độ thật vào cột Ghi chú state file, đã xoá khi xong.

Từ phiên 2026-11-18 (handoff `2026-11-18-2139-…`), còn mở:

- **Phần TT83 người dùng cho dừng** (ít liên quan ALM), còn: Chương I Điều 5, 7, 8, 10; Chương II (Điều 11–16); Chương IV (Điều 64–73); Chương V Điều 75; Phụ lục I. Phụ lục II, IV đã nạp. Agent đã gợi ý nếu nạp thêm thì Đ16 (kiểm soát giao dịch tự doanh) trước, Đ8 (MIS) chỉ khi cần trang dữ liệu rủi ro. Nếu muốn `--coverage` thôi báo, cần người dùng cho ghi `bỏ qua:` vào state file.
- **Câu mới trên hub TT83** (bốn báo cáo năm, Đ9.K2) nằm ngoài bảng merge đã duyệt; người dùng chưa xác nhận giữ hay chỉ để link.
- **5 trang mới chưa `reviewed`**, cộng các trang merge trong phiên đó (`risk-appetite`, `tt83-risk-data-…`, `contingency-funding-plan`, `tt83-internal-model-risk-reports-…`, `tt83-irrbb-is-measured-quarterly-…`, hub `circular-83-…`). Điểm agent tự rút cần soát:
  - Phụ lục II: danh sách người kiến nghị không có kiểm toán nội bộ, khác báo cáo nội bộ (Đ55, Đ58) — viết thành câu so sánh trên trang khung lặp và trang báo cáo nội bộ mô hình.
  - Đ9.K4 không nói ai duyệt báo cáo kiểm toán nội bộ của chi nhánh ngân hàng nước ngoài; trang chỉ ghi người ký theo mẫu.
  - Trang khung stress test: "ngân hàng vẫn có thể thêm rủi ro hoạt động, tập trung vào quy định nội bộ" suy từ chữ "tối thiểu".
  - Trang phương pháp: "stress test ngược đi từ tác động ngược về cú sốc" là diễn giải K3.c.
- **Bài học coverage (lặp lại):** `--coverage` tính theo heading, nên Phụ lục II mục II (chỉ có II.6) và Điều 23 (chỉ có K1, K4, K5) từng báo đã phủ dù thiếu nội dung.
- **Hub TT83 chưa link** tới cụm ALM (`tt83-alm-unit-…`, ALCO) và ICAAP; trang Chương III cũng chưa nối ICAAP.

Từ phiên 2026-11-18 (handoff `2026-11-18-1912-…`), còn mở:

- **40 trang mới chưa `reviewed`**, cộng các trang merge trong phiên đó (`contingency-funding-plan`, `intraday-liquidity-management`, `liquidity-risk`, `loan-to-deposit-ratio-ldr`, `liquidity-stress-test-reports-…`, `trading-book`, `three-lines-of-defence`, `risk-adjusted-return-on-capital-raroc`, hub `circular-83-…`: `reviewed` cũ hơn `last_updated`). Điểm agent tự rút cần soát:
  - "Tỷ lệ khả năng chi trả" ở Đ45.K3 được trình bày trung lập (TT22 30 ngày hay LCR theo tên gọi của TT50); TT22 vẫn áp tới khi ngân hàng chuyển sang LCR/NSFR.
  - `tt83-problem-credits-…`: không khẳng định nợ xấu bắt đầu từ nhóm 3.
  - `tt83-collateral-…`: đối chiếu tỷ lệ khấu trừ dự phòng với `haircut`.
  - `tt83-market-risk-measurement-…`: "điều chỉnh hạn mức khi theo dõi là điểm riêng của rủi ro thị trường".
  - `tt83-internal-concentration-risk-reports-…`: "báo cáo ngắn nhất", "không có mục stress test".
  - `tt83-concentration-risk-is-measured-…`: "khoản chưa hạch toán làm danh mục rộng hơn bảng cân đối".
  - `tt83-chapter-iii-…`: đoạn so chu kỳ báo cáo tổng hợp từ sáu Điều.
- **Stub `foreign-currency-position`** đã lên draft với bảng B05 47.2, nhưng vẫn chờ văn bản quy định cách xác định trạng thái ngoại tệ, trạng thái vàng cho hạn mức. `TT14_2025_SBV/14_2025_TT-NHNN_normalized.md` Phụ lục IV mục IV.2 (d.3759–3773) có cách tính trạng thái nguyên tệ cho vốn yêu cầu, nhưng TT14 chưa đăng ký trong manifest.
- **Bài học coverage:** chú thích dải rộng (ví dụ "Chương III, d.543–1684") làm `--coverage` báo sai mọi heading trong dải là đã phủ.
- **Op của mục tách trang** (log 2026-11-18 19-08-33) ghi `lint`; nếu người dùng muốn op khác thì mục log kế tiếp cùng loại ghi đính chính.

Từ phiên 2026-11-17 (handoff `2026-11-17-2235-…`), còn mở:

- **Trang chờ review (TT83/IRRBB):** 13 trang TT83 tạo 2026-11-15 (trừ hub), 3 trang gap/basis/option và `funds-transfer-pricing-ftp-allocates-…` (`reviewed` cũ hơn `last_updated`), `vietnamese-banks-may-measure-irrbb-…`, `banking-book`, `trading-book`, 3 trang ALM/ALCO/ba tuyến, 7 trang ICAAP. Điểm agent tự rút cần soát: trang `$RWA_{COR}$` (sàn tăng qua từng mốc nếu dư nợ không đổi), trang RAROC (mẫu số gồm phần đệm kịch bản bất lợi), trang vốn mục tiêu (phần bất lợi chỉ cần CAR luật định), trang ALCO ("chỉ hội đồng rủi ro bị cấm Tổng giám đốc làm chủ tịch").
- **`repurchase-agreement`** khai `bindseil_monetary_policy`, `cargill_central_bank_policy` trong `sources:` nhưng không còn claim dẫn hai nguồn này (đã ghi `_inbox.md`).
- **Câu hỏi mở ALM vs độc lập đo IRRBB** (Đ54.K1.b, Đ25.K3, Đ4.K2) — đã ghi `_inbox.md`, không thành claim.
- **Stub `capital-adequacy-ratio-car`** chờ Thông tư 14/2025 (thông tư vốn).

Từ phiên 2026-11-15 (handoff `2026-11-15-2150-…`), còn mở:

- Điểm agent tự rút trên các trang TT83 cần soát khi review: VND không có trong Bảng 5; dấu ΔEVE của TT83 (EVE₀ − EVEᵢ + KAO) ngược trang EBA SA; "Phụ lục V không quy định sàn sau sốc"; "Mục 7 và Phụ lục V không ghi mức hạn mức bằng số"; hai ví dụ tự tính (lãi suất bình quân 6% → 360/500/240 bp; $S_{short}$ = 0,5 ở khoảng 2,8 năm).
- Câu "Chương III có chín Mục…" trên hub TT83 không có chú thích dòng riêng (chú thích heading Chương III làm `--coverage` báo sai Mục 1–8 đã phủ, nên đã thu hẹp về Đ3.K13 và Đ1.K2).
- Khi nạp Basel IRRBB (d368, d578) thì so tham số Phụ lục V (Bảng 2–6) với Basel.

Từ phiên 2026-11-14 (handoff `2026-11-14-2218-…`), còn mở:

- 4 trang đòn bẩy mới chưa `reviewed`; hai trang NSFR phái sinh có thêm một câu nối sau khi đã review (cùng ngày, lint không bắt).
- Thư mục `TT14_2025_SBV/` có cả bản gốc và bản chuẩn hóa; nếu dùng bản chuẩn hóa thì nên bỏ bản gốc trước khi ingest để chú thích không dẫn nhầm.
- Chuyển từ phiên 2026-11-10, còn mở:
  - 41 "LINK MẤT" do `--graph` báo so với HEAD trước merge, ví dụ `alm-balance-sheet-balancing-progresses-through-four-operational-dimensions` → `ftp-business-steering-functions-as-a-political-tool-for-balance-sheet-allocation`. Chưa kiểm từng link; đều là trang remote, nhiều khả năng do lint remote gỡ. Đối chiếu với diff `origin/main` nếu cần.
  - Script ghi file phải mở file với `newline="\n"` (script cũ ghi CRLF, gây diff cả file). Viết script Python vào scratchpad bằng Write rồi chạy, vì heredoc bash lỗi với dấu nháy tiếng Việt.
  - Văn bản ngoài TT50 được dẫn, cần ingest thêm (đã ghi tại chỗ dẫn và `_inbox.md`): Thông tư 41/2016/TT-NHNN (sửa đổi bởi 22/2019, 22/2023) và Thông tư 14/2025/TT-NHNN (cấu phần vốn, vốn cấp 1, hệ số rủi ro, bất động sản, định nghĩa vỡ nợ, tổ chức tài chính quốc tế, xếp hạng tín nhiệm, PFE, CCF, rủi ro tín dụng đối tác của repo); khoản 9 Phụ lục II của thông tư vốn (điều kiện thỏa thuận bù trừ hai bên đủ điều kiện, Điều 25 khoản 1); quy định chế độ báo cáo thống kê (báo cáo NSFR riêng lẻ, Điều 22 khoản 4); quy định phân loại tài sản có/CIC (Phụ lục I phần C mục I).
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
  - Stub: khoảng 37 stub (`capital-adequacy-ratio-car` vẫn stub; `foreign-currency-position` đã lên draft phiên này); `intraday-liquidity` chờ nguồn khác; `deposit-insurance` chờ `cargill_central_bank_policy`; `loan-to-deposit-ratio-ldr` đã thành draft (TT83 Đ45), vẫn chờ Điều 12 TT50.
  - `_inbox.md` còn 12 khái niệm ALM chờ ingest `basel/NSF/`, `basel/IRRBB-d368/`.
  - `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới trích phần đầu.
  - Link chưa có loại: khoảng 3.800 trên 6.500; tỷ lệ link mạnh khoảng 12%, dưới mục tiêu 15–30%. Kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.
  - Ba trang tách từ `repo-specialness-…` chưa `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`.
  - Hai trang vượt ngưỡng: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và CRR) và `supervisory-irrbb-reporting-…` (đoạn 730 từ); `supervisory-outlier-test-…` dài 1.144 từ.
  - 9 file nguồn chưa kê, đăng ký khi ingest: `basel/BaselFramework/BaselFramework.md`, `basel/IRRBB-d368/d368_irrbb.md`, `basel/LEV/LEV.md`, `basel/NSF/NSF.md`, `Clippings/ALM P11 TT50(P4)…`, `vietnam-regulator/alm/ftp_transmission_analysis.md`, `TT14_2025_SBV/14_2025_TT-NHNN.md`, `TT14_2025_SBV/14_2025_TT-NHNN_normalized.md`, `VAB - Phương pháp luận FTP/VAB - Phương pháp luận FTP.md`. Thêm `vietnam-regulator/accounting/19_VBHN_NHNN_2026_He_thong_tai_khoan_ke_toan.pdf`.
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

- Commit thay đổi phiên này.
- Hỏi người dùng các mục ở Blocker, trước hết B.VII → V.22 và XII.5 → V.14.3 (cùng loại lệch số thuyết minh).
- `/review-node` trên cụm B02 (5 trang/lượt), bắt đầu từ trang tổng `b02-statement-of-financial-position-of-vietnamese-credit-institutions` rồi các trang nhóm.
- `/lint` trọn bộ: `--verify-sources`, `--relations`; quét câu "chưa nạp" và tự quy chiếu còn sót.
- Đăng ký và ingest `19_VBHN_NHNN_2026_He_thong_tai_khoan_ke_toan.pdf` để có tên tài khoản cho node B02, B03.
