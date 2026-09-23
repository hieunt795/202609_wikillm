# Decisions

> Lý do các quyết định thiết kế. `log.md` chỉ ghi *chuyện gì đã xảy ra*; file này ghi *vì sao*. Quyết định nào đã có lý do đầy đủ trong `00_schema.md` thì ở đây chỉ trỏ tới mục đó, không chép lại.
>
> Định dạng: mỗi quyết định là 1 mục `## [YYYY-MM-DD] <tiêu đề>`, gồm *Quyết định* · *Lý do* · *Thay cho* (nếu có). Quyết định bị đảo thì thêm mục mới trỏ về mục cũ, không sửa mục cũ.
>
> Bản log dài trước 2026-09-15 (chứa lập luận gốc của các mục 2026-09-12 → 2026-09-14): `git show e2adb7a:log.md`.
>
> Từ 2026-09-17, mục cũ ghi "Lý do: `00_schema.md` §X" được hiểu là tiểu mục §X của mục *[2026-09-17] Lý do dời từ `00_schema.md`* bên dưới; bản schema còn lý do: `git show 812200a:00_schema.md`.

## [2026-09-14] Thêm mục `## Sources` vào `index.md`
- **Quyết định:** bảng trạng thái cấp nguồn ở đầu `index.md`, cập nhật mỗi lượt ingest kể cả lượt không tạo trang.
- **Lý do:** trước đó muốn biết nguồn nạp tới đâu phải diễn giải lại văn xuôi trong `log.md`.

## [2026-09-14] Trạng thái ingest nằm ở `03_state/`, không đặt cạnh nguồn
- **Quyết định:** lớp thứ tư `03_state/`, luật `01_sources/` bất biến không ngoại lệ. Lý do đầy đủ: `00_schema.md` §10.
- **Thay cho:** file `_ingest_state.md` đặt trong `01_sources/` (đã hoàn nguyên cùng ngày — tiền tố `_` không phân biệt được nguồn với không-nguồn, vì `Modern Money Mechanics` đã có sẵn 15 file `_page_*.jpeg`).

## [2026-09-14] Ngưỡng nguồn dài: > 120 KB hoặc > 1.200 dòng
- Lý do và lý do không dùng số heading: `00_schema.md` §10. Ngưỡng đặt ở schema chứ không ở skill vì nó quyết định nguồn có state file hay không — là thuộc tính data model.

## [2026-09-14] Chú thích vị trí cho claim từ nguồn dài, không backfill
- Lý do: `00_schema.md` §7 luật 5. Nợ backfill theo dõi ở `_inbox.md`.

## [2026-09-14] Thêm `_inbox.md`
- Lý do `status: stub` không thay được vùng capture: `00_schema.md` §11.

## [2026-09-14] Lint có tiêu chí *Nhiễu OCR còn sót*
- 6 họ mẫu, đối chứng ngược bắt 8/9 lỗi thật của nguồn IMF; giới hạn đã biết ghi trong `lint/SKILL.md`.

## [2026-09-14] `reviewed:` là trường tuỳ chọn, không có tiêu chí lint
- Lý do: `00_schema.md` §9 mục *`status` không đo việc người dùng đã đọc qua*.

## [2026-09-14] Không đưa `01_sources/` lên GitHub; bù bằng bản kê SHA-256
- **Lý do:** repo public, nguồn là ấn phẩm IMF có bản quyền. Chú thích §7.5 trỏ tới số dòng nên cần checksum để người clone kiểm chứng được: `03_state/_sources_manifest.md`. `.claude/` được commit vì hook và skill là đặc tả thực thi.

## [2026-09-15] Rollback toàn bộ về `e2adb7a`
- **Quyết định:** bỏ lượt ingest Ch.1 + Ch.3 (117 trang), giữ ở tag `ch3-snapshot`.
- **Lý do:** người dùng chọn làm lại từ bản 51 trang. Chi tiết audit bản 117 trang: `Claude outputs/audit-2026-09-15.md` (không commit).

## [2026-09-15] Lấy lại riêng hook từ `ch3-snapshot`
- **Quyết định:** chỉ phục hồi `.claude/hooks/validate_wiki_page.py` (có `--all`, bắt link chết, `sources` rỗng, trang mồ côi, §7.5 theo `last_updated`); không phục hồi nội dung Ch.3, không phục hồi các thay đổi §2/§5 của commit đó.
- **Lý do:** hook cũ cho qua trang có link chết và `sources: []` (đã thử). Các thay đổi §2 (*ưu tiên lý luận trước tường thuật*) và §5 (*ba phép kiểm, bỏ tiêu chí độ dài*) là chính sách nội dung gắn với lượt ingest Ch.3 — để người dùng quyết khi làm lại Ch.3.

## [2026-09-15] Định dạng log mới
- **Quyết định:** `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng; 6 op cố định; giờ Việt Nam; mục cũ không rõ giờ ghi `00-00-00`. Chi tiết: `00_schema.md` §12.
- **Lý do:** gist Karpathy dùng tiền tố `## [` để grep được; log cũ dài 431–3.779 ký tự/mục, có 10 loại động từ, kiêm cả biên bản quyết định.
- **Ánh xạ động từ cũ:** `bồi đắp` → `ingest`; `schema-batch`, `đính chính` → `schema`; `publish` → `repo`.

## [2026-09-15] Thêm operation Promote
- **Quyết định:** lint đưa ra danh sách *Đủ điều kiện `stable`* (hook sạch, outlink ≥ 1, backlink ≥ 2, không conflict, không bị flag) → người dùng duyệt → `/promote` đổi status.
- **Lý do:** §9 cũ không gán bước `draft → stable` cho operation nào nên 51/51 trang kẹt ở `draft`, kéo theo tiêu chí stale và sai vòng đời không bao giờ kích hoạt. Ngưỡng backlink ≥ 2 do người dùng duyệt.

## [2026-09-15] Ingest có bước 0: duyệt 3–5 ý chính
- **Lý do:** gist Karpathy đặt bước "đọc và bàn ý chính" trước khi ghi; audit đo được `reviewed` 0/51 và `_inbox.md` chưa từng dùng — người dùng vắng mặt khỏi vòng lặp.

## [2026-09-15] `last_updated` đo nội dung, không đo liên kết
- **Quyết định:** chỉ chèn `[[wikilink]]` vào câu có sẵn thì không nâng `last_updated` (`00_schema.md` §7 luật 5).
- **Lý do:** tiêu chí stale so `last_updated` với ngày ingest nguồn; và hook đòi chú thích §7.5 cho mọi trang có ngày từ 2026-09-14 — nâng ngày vì một cái link sẽ buộc backfill chú thích cho claim không hề đổi.

## [2026-09-15] Không tạo trang tóm tắt nguồn
- Lý do: `00_schema.md` §2.

## [2026-09-15] Title tiếng Anh, thân bài tiếng Việt
- Lý do: `00_schema.md` §3. Chốt theo thực tế 51/51 trang.

## [2026-09-15] Không tạo stub `fiscal-deficit`
- **Lý do:** audit đề xuất dựa trên đếm chuỗi "thâm hụt" (5 trang), nhưng 4/5 trang nói thâm hụt vãng lai; thâm hụt ngân sách chỉ xuất hiện ở 1 trang — dưới ngưỡng ≥ 3 trang. Tạo lại khi ingest Ch.3.

## [2026-09-15] Cho phép model tự review trang
- **Quyết định:** agent được đặt `reviewed:` qua `/review`, luôn kèm `reviewed_by: model`; người dùng đặt `reviewed_by: user`. Agent không ghi đè `user`.
- **Lý do:** người dùng chọn giao việc review cho model. Tách `reviewed_by` để trường vẫn phân biệt được *model đã đối chiếu nguồn* với *người đã đọc* — lý do gốc của quyết định 2026-09-14 (`reviewed:` chỉ người đặt).
- **Thay cho:** mục [2026-09-14] *`reviewed:` là trường tuỳ chọn, không có tiêu chí lint* — phần "chỉ người dùng đặt" bị thay; phần "không có tiêu chí lint" giữ nguyên.
- **Giới hạn đã biết:** model soát trang do model viết, không độc lập hoàn toàn; bù bằng yêu cầu đọc lại đúng đoạn nguồn và gắn chú thích §7.5 cho từng claim đã đối chiếu.

## [2026-09-15] Ch.3 chỉ ingest phần lý luận, ingest lại từ nguồn
- **Quyết định:** ingest 5 cụm lý luận A–E; bỏ qua bối cảnh tài khoá Ba Lan (d.2531–2603) và Exercises/bảng/phụ lục (d.2604–3425). Viết mới từ nguồn, không khôi phục trang từ tag `ch3-snapshot`. Duyệt ý chính từng cụm.
- **Lý do:** người dùng chọn. Phục hồi nguyên tắc §2 *ưu tiên lý luận trước tường thuật* làm căn cứ ghi trong bản đồ chunk.

## [2026-09-15] Viết lại Ch.2 từ nguồn, theo từng cụm
- **Quyết định:** viết lại toàn bộ Ch.2 thay cho ingest bổ sung hay review tiếp. Bản cũ lưu ở tag `ch2-snapshot` (commit 49efa84). Trang cũ của một cụm chỉ bị thay/xoá khi cụm đó được viết lại; giữ title cũ khi title vẫn đúng. Tách cụm A thành A1 (d.607–795) và A2 (d.797–934); chuyển d.1011–1017 từ cụm B sang C. Duyệt ý chính từng cụm.
- **Lý do:** người dùng chọn. Khoảng 39 link từ Ch.3 trỏ vào trang Ch.2 — xoá cả 51 trang một lần sẽ để lại link chết qua nhiều lượt và `--all` không sạch (ingest bước 8). Cụm A cũ vượt ngưỡng 15 trang/lượt (§4). d.1011–1017 là văn bản chính của mục *Measuring Inflation* nằm sau Box 2.3.
- **Bổ sung theo yêu cầu người dùng (cụm A1):** trang riêng cho năm khu vực phân tích (d.636–648) và stub `macroeconomic-sectors` — tương tác giữa các khu vực là trọng tâm cần phát triển (Ch.6 flow of funds); stub `net-exports`.

## [2026-09-15] Hạ `current-account-balance` về stub cho tới khi ingest Ch.4
- **Quyết định:** trang chuyển `draft → stub`, thân bài còn 1 câu định nghĩa nối tới hai đồng nhất thức đối ngoại.
- **Lý do:** người dùng chọn. Trong Ch.2, định nghĩa CAB chỉ có ở chú thích 10 (d.831); chương gốc là Ch.4 (d.3426–4529). Bước chuyển này không có trong bảng §9 — là ngoại lệ có chủ đích, trang sẽ lên `draft` khi ingest Ch.4.

## [2026-09-16] Title phủ định là hợp lệ
- **Quyết định:** bỏ luật "ưu tiên khẳng định tích cực thay vì phủ định" (§8 luật 1 cũ). Title phủ định hợp lệ khi nhận định vốn là phủ định; lint không còn flag title phủ định. Giữ nguyên `full-employment-does-not-mean-zero-unemployment` và `when-interest-exceeds-growth-a-permanent-primary-deficit-cannot-exceed-seigniorage`.
- **Lý do:** người dùng chỉ ra phủ định thường không có dạng xác định tương đương ("không ăn cơm" không đồng nghĩa "ăn cháo"); ép đổi sẽ làm sai nghĩa. "Khẳng định" trong §8 được hiểu là câu trần thuật.
- **Thay cho:** §8 luật 1 bản trước 2026-09-16.


## [2026-09-16] Thành phần có tên kinh tế riêng phải có trang wiki riêng
- **Quyết định:** áp dụng hồi tố cho toàn bộ wiki đã ingest (Ch.2–Ch.6, ~211 trang). Mọi thành phần trong một đồng nhất thức, bảng cân đối hay box có tên gọi kinh tế/tài chính thật (compensation of employees, operating surplus, private/government consumption, required/excess reserves, Treasury bills, SDR holdings...) được tách thành trang `concept` riêng, kể cả khi trang đó rất ngắn. Không tách trang cho hệ số/tỷ trọng đại số thuần tuý không mang tên riêng (trọng số tăng trưởng, $b$, $t$/$t-1$...). Chi tiết: `00_schema.md` §5.
- **Lý do:** người dùng phát hiện qua Box 2.1 (SNA: Key Aggregates) rằng nhiều đại lượng có tên riêng (W, OS, TSP, CP, CG, Y_f, TR_f...) chỉ được giải thích lồng trong câu văn của trang identity, không tra được như một node độc lập.
- **Hệ quả vận hành:** backfill là một dự án nhiều lượt, đi theo từng chương (Ch.2 trước vì vừa được rà, sau đó Ch.3–Ch.6); mỗi lượt vẫn theo ngưỡng 5–15 trang/lượt (§4) và phải chạy `validate_wiki_page.py --all` + ghi log riêng.

## [2026-09-16] §5 không có ngoại lệ mới — huỷ các "quyết định phạm vi" của backfill Batch 2–4
- **Quyết định:** mọi thành phần có tên kinh tế riêng đều có trang riêng, kể cả mục liệt kê định tính trong box (Box 3.5, 3.6, 3.7, 4.4) và khoản mục chi tiết của bảng cân đối MA/DMB (vàng, ngoại hối, SDR, tín phiếu kho bạc, tiền gửi chính phủ, CY, DD, NDA, NCG, CPS, CDMB, OIN...). Chỉ giữ hai ngoại lệ đã có ở `00_schema.md` §5 (hệ số đại số thuần tuý; đại lượng đã có trang dưới tên khác). Làm theo lượt B–D, mỗi lượt duyệt ý chính riêng.
- **Lý do:** người dùng chốt khi xử lý lint 240 trang: không đặt ngoại lệ, tìm phương án tách trang cho từng thành phần.
- **Thay cho:** các đoạn "Quyết định phạm vi (giữ nguyên, không tách trang)" trong ghi chú Backfill §5 Batch 2–4 ở `03_state/imf_macro_accounting.md`.

## [2026-09-16] Promote 188 trang không qua `/review`
- **Quyết định:** nâng toàn bộ danh sách *Đủ điều kiện `stable`* của lint 240 trang mà không chạy `/review` trước.
- **Lý do:** người dùng chọn. Hệ quả: `stable` ở lượt này chỉ có nghĩa hook sạch, đủ liên kết và không Conflict; 0/188 trang có `reviewed`.

## [2026-09-17] Reset về `38d3381`, bỏ toàn bộ việc ngày 2026-09-17
- **Quyết định:** đưa `main` về bản cuối ngày 2026-09-16 và force-push; không giữ nhánh backup. Bị bỏ: 10 commit `6287ec9` → `b1ba033` (audit skill lần 1 với đổi tên `review-node` và cờ `--backlinks/--ocr/--now`; trường `school`; source id; ingest Bindseil Intro–Ch.13 và Capitalism and Freedom Ch.II–V, IX; lint 479 trang). Các commit này chỉ còn trong reflog máy cục bộ, sẽ mất khi git dọn reflog.
- **Lý do:** người dùng chọn làm lại từ bản 295 trang.
- **Lưu ý cho lượt audit sau:** một số thứ bị bỏ được làm lại có chủ đích trong batch audit v2 cùng ngày (đổi tên `review-node`, cờ hook, source id, bản kê đủ 10 nguồn). Trường `school` và nội dung ingest Bindseil/Friedman **không** được làm lại; đừng đề xuất khôi phục chỉ vì chúng từng tồn tại.

## [2026-09-17] Khôi phục CRLF cho file OCR của IMF
- **Quyết định:** đổi `Macroeconomic Accounting and Analysis IMF.md` từ LF về CRLF để khớp lại SHA-256 trong bản kê.
- **Lý do:** lúc 13:40 ngày 2026-09-17 một công cụ đã đổi ký tự xuống dòng CRLF sang LF (giảm đúng 6.065 byte = số dòng). Nội dung và số dòng không đổi nên chú thích §7.5 vẫn đúng; khôi phục CRLF cho đúng từng byte bản gốc. Người dùng duyệt việc ghi vào `01_sources/` này. Phòng ngừa: `validate_wiki_page.py --verify-sources` ở bước 0 của lint.

## [2026-09-17] Chuyển `_source_note.md` ra khỏi `01_sources/`
- **Quyết định:** ghi chú người dùng trong `01_sources/fixed_income_during/_source_note.md` (ISBN, chia phần, PDF có text layer, dự kiến file highlight) chuyển sang bản kê và `03_state/fixed_income_during.md`; file gốc xoá theo quyết định của người dùng.
- **Lý do:** giữ phép thử §3 "mọi file `.md`/`.pdf` trong `01_sources/` đều là nguồn có trong bản kê" đúng tuyệt đối, cùng lý do đã hoàn nguyên `_ingest_state.md` ngày 2026-09-14.

## [2026-09-17] Sách During là một nguồn nhiều file
- **Quyết định:** 42 file chương của *Fixed Income Trading and Risk Management* là một source id `fixed_income_during`, một state file, 42 dòng chunk; chú thích §7.5 thêm hậu tố file.
- **Lý do:** người dùng chọn. Từng file đều dưới ngưỡng nguồn dài nhưng tổng 1.112 KB / 7.300 dòng vượt ngưỡng; tách 42 nguồn sẽ làm `sources:` và `index.md` §Sources vụn theo chương, trái với cách các sách khác được khai.
- **Thay cho:** —. Quy ước chung: `00_schema.md` §10 mục *Nguồn nhiều file*.

## [2026-09-17] Đổi skill `review` thành `review-node`
- **Quyết định:** thư mục và `name:` đổi thành `review-node`; op trong `log.md` vẫn là `review`.
- **Lý do:** skill không nạp được vì description chứa `reviewed_by: model` không có nháy (YAML đọc thành mapping); tên `review` còn trùng lệnh dựng sẵn `/review` của Claude Code. Description giờ đặt trong nháy kép.

## [2026-09-17] Ingest, review-node và trang `analysis` của query áp skill `writing-style`
- **Quyết định:** khi viết hoặc sửa thân bài trang wiki, agent áp skill `writing-style` (cấp tài khoản) theo profile wiki.
- **Lý do:** người dùng chọn cho ingest và review; trang `analysis` của query là trang wiki nên áp cùng quy tắc. Câu trả lời query không tạo trang thì không bắt buộc.
- **Thay cho:** việc chưa có quyết định nào (audit v2, B16).

## [2026-09-17] Gộp `agents.md` vào `CLAUDE.md`
- **Quyết định:** xoá `agents.md`; ràng buộc 6 (cập nhật §Sources + state file mỗi lượt ingest), mẫu hai lượt và danh sách lượt bắt buộc chạy `--all` chuyển vào `CLAUDE.md`. README chỉ trỏ.
- **Lý do:** ba file lặp bảng operation và luật cứng, và đã lệch nhau (5 luật so với 7 ràng buộc). `CLAUDE.md` là file Claude Code tự nạp nên giữ nó.

## [2026-09-17] Báo cáo lint/audit lưu ở `Claude outputs/`
- **Quyết định:** mọi báo cáo do Claude xuất ra nằm ở `Claude outputs/` (không commit), tên theo `00_schema.md` §3. Thư mục `.audit_reports/` bị bỏ; báo cáo lint 479 trang của nhánh đã reset chuyển sang `Claude outputs/lint-2026-09-17-479-discarded.md`.
- **Lý do:** preference của người dùng; lint skill trước đó không quy định đường dẫn nên log và thư mục thực tế lệch nhau.

## [2026-09-17] Hook xác định nguồn dài từ bản kê; thêm lệnh phụ trợ
- **Quyết định:** `validate_wiki_page.py` coi một nguồn là nguồn dài khi bản kê xếp "Nguồn dài" hoặc có state file, và báo `sources:` trỏ tới id không có trong bản kê. Thêm `--backlinks`, `--ocr`, `--stub-debt`, `--inbox-debt`, `--verify-sources`, `--now`.
- **Lý do:** trước đó nguồn dài chưa có state file lọt qua kiểm §7.5. Các phép đếm backlink, quét OCR, đếm nợ và lấy giờ trước đây skill bắt model tự dựng bằng grep/awk; lint từng ghi nhận grep `[[...]]` sai cả hai chiều và awk so ngày đếm sai nợ stub.

## [2026-09-17] Lint gộp *Trang stale* và *Sai vòng đời status*
- **Quyết định:** còn 11 tiêu chí; tiêu chí gộp tên *Stale chưa đánh dấu*.
- **Lý do:** hai tiêu chí cùng định nghĩa "trang `stable` có nguồn liên quan ingest sau `last_updated`".

## [2026-09-17] Bỏ `.claude/memory/`
- **Quyết định:** xoá hai file tóm tắt khái niệm Karpathy/Matuschak trong `.claude/memory/`; nguồn tham chiếu duy nhất là hai link gốc trong phần Context của Project (và README).
- **Lý do:** hai nơi cùng giữ một nội dung dễ lệch nhau; người dùng đã chọn Context dạng link để luôn đọc bản gốc. Bản cũ: `git show 812200a:.claude/memory/`.

## [2026-09-17] Lý do dời từ `00_schema.md`
Schema chỉ giữ luật; lý do dời về đây theo từng mục.
- **§2 Ưu tiên lý luận trước tường thuật:** `case` tồn tại để chống lưng cho `concept`, nên khi concept đã đủ minh chứng thì thêm case không tăng sức giải thích mà chỉ làm loãng wiki.
- **§2 Không có trang tóm tắt nguồn:** gist Karpathy tạo trang tóm tắt cho mỗi nguồn; Evergreen yêu cầu wiki hướng khái niệm, và trang "tóm tắt cuốn X" chính là *literature note* mà Matuschak xếp ngoài thang evergreen.
- **§3 Title tiếng Anh:** giữ được thuật ngữ gốc của nguồn và không phải bỏ dấu khi chuyển sang kebab-case.
- **§5 Thành phần có tên riêng:** người dùng phát hiện qua Box 2.1 rằng nhiều đại lượng có tên riêng chỉ được giải thích lồng trong câu của trang đồng nhất thức, không tra được như một node độc lập (xem mục 2026-09-16).
- **§6 Hai dạng link:** grep `[[tên-trang]]` trần bỏ sót toàn bộ link dạng `[[tên-trang|nhãn]]`, và `[[...]]` trong grep bị hiểu là bracket expression.
- **§6 Stub link:** liên kết bị hoãn sang batch sau thường mất luôn.
- **§7.4 Viết lại, không chép:** chỉ khi diễn đạt lại mới lộ ra chỗ chưa hiểu và chỗ mâu thuẫn. Đồng nhất thức viết dạng công thức vì người đọc cần nhận ra ngay và trích lại chính xác; `S − I = CAB` lẫn trong câu dễ bị đọc lướt như một cụm từ (người dùng chốt 2026-09-16).
- **§7.5 Chú thích vị trí:** `sources:` chỉ nói claim đến từ file nào; với file 849 KB, xác minh một câu phải đọc lại phần lớn nguồn. Nguồn ngắn đọc trọn lại được trong 1 lượt nên không bắt buộc. Không backfill hàng loạt để không sinh một dự án sửa 51 trang cùng lúc; nợ trả dần khi trang được sửa.
- **§7.5 `last_updated` đo nội dung:** xem mục 2026-09-15.
- **§8 Title là API:** title đứng độc lập khỏi nguồn thì trang tái sử dụng được ở ngữ cảnh khác. Title phủ định hợp lệ vì phủ định thường không có dạng xác định tương đương: "không ăn cơm" không đồng nghĩa với "ăn cháo" (người dùng chốt 2026-09-16).
- **§9 Bảng "Ai làm":** trước 2026-09-15 không operation nào sở hữu bước `draft → stable`, nên mọi trang kẹt ở `draft` và tiêu chí stale không bao giờ kích hoạt. Backlink ≥ 2 để một trang `stable` không thành mồ côi chỉ vì mất một cạnh.
- **§9 `reviewed` tách khỏi `status`:** hai trục trực giao; gộp lại sinh ô lai vô nghĩa (`stale` nhưng đã duyệt, `stub` đã duyệt) và làm bảng chuyển tiếp mất tính đơn tuyến. Tách `reviewed_by` để trường vẫn trả lời được *người dùng đã đọc trang này chưa* (lọc `reviewed_by: user`). Không có tiêu chí lint cho `reviewed:` cũ hơn `last_updated:` vì ở quy mô một người dùng nó chỉ tạo nhiễu phải bỏ qua mỗi lượt.
- **§10 Ngưỡng 120 KB:** khoảng 30k token, vẫn đọc trọn được 1 lượt nhưng chiếm gần hết ngân sách context, không còn chỗ cho bước đối chiếu với toàn bộ `02_wiki/`. Không dùng số heading: `Modern Money Mechanics` có 66 heading trong 721 dòng mà vẫn đọc trọn được.
- **§10 `03_state/` thay vì đặt cạnh nguồn:** đặt cạnh nguồn tra cứu tiện hơn một nhịp nhưng phải khoét ngoại lệ vào luật bất biến, và luật cứng đã có ngoại lệ thứ nhất thì sẽ có ngoại lệ thứ hai. Đánh đổi: nhớ thêm một đường dẫn, state file tự khai `file:`.
- **§10 Bản kê SHA-256:** `01_sources/` không commit (tài liệu bên thứ ba); chú thích §7.5 và bản đồ chunk trỏ tới số dòng, nên người đọc chỉ kiểm chứng được khi đối chiếu đúng bản file. Chunk bỏ qua vẫn có dòng riêng để lượt sau không tưởng còn sót. Số dòng dùng làm khoá được vì nguồn bất biến.
- **§11 `_inbox.md` tách khỏi `02_wiki/`:** mọi trang trong `02_wiki/` phải atomic hợp lệ và bị hook kiểm mỗi lần ghi; ý tưởng dang dở không thoả luật đó, không có chỗ riêng thì bị nhét bừa vào một trang hoặc mất luôn.
- **§12 Tiền tố `## [`:** theo gist Karpathy, để `grep` lấy được các mục gần nhất.

## [2026-09-23] Copy skill `writing-style` từ cấp tài khoản vào project local

- **Quyết định:** tạo bản sao `writing-style` SKILL.md vào `.claude/.claude/skills/writing-style/` (cùng cấp với `ingest`, `lint`, `promote`, `query`, `review-node`). Skill `/ingest` gọi tường minh bản local qua Skill tool trước khi viết/sửa thân bài trang wiki, thay vì chỉ nhắc tên skill cấp tài khoản.
- **Lý do:** skill cấp tài khoản nằm ngoài repo, có thể đổi hoặc không sync giữa máy/phiên; bản local đảm bảo ingest luôn áp đúng bộ quy tắc A–I đã kiểm chứng, theo dõi được qua git history.
- **Phạm vi:** chỉ sửa `ingest/SKILL.md` bước 3 theo yêu cầu người dùng. `review-node` và `query` vẫn trích dẫn skill `writing-style` cấp tài khoản như quyết định 2026-09-17 — chưa đồng bộ, cần quyết định riêng nếu sau này muốn áp toàn bộ.
- **Rủi ro theo dõi:** nếu bản cấp tài khoản được cập nhật thêm rule hoặc đổi ID, bản local sẽ lệch — cần đối chiếu thủ công khi phát hiện khác biệt.

## [2026-09-23] Sửa lỗi nesting `.claude/.claude/` và dọn file thừa

- **Phát hiện:** commit `abd8dbc` (2026-09-21) đã vô tình rename `.claude/{hooks,rules,skills,settings.json}` thành `.claude/.claude/{hooks,rules,skills,settings.json}` — lồng sai một cấp. Hậu quả: `.claude/settings.json` hook path tự tham chiếu đúng nội bộ nhưng không nằm ở vị trí chuẩn, và 6 skill chính bị harness scope riêng cho `.claude/` thay vì project-wide.
- **Quyết định:** (1) Dùng `git mv` để đưa `.claude/.claude/*` lên `.claude/` (rename-tracked, giữ lịch sử); sửa path tự tham chiếu trong `settings.json`, 5 SKILL file, và rule `source-management.md`. (2) Xoá `.claude/CLAUDE.md` (duplicate), giữ root `CLAUDE.md` (có session status) làm bản chính thức. (3) Archive `CLAUDEV4_1.local.md` và `CLAUDE_RULES_REPORT.md` vào `.claude/archive/`. (4) Sửa root `CLAUDE.md:65` path `log_questions.py` → `Claude outputs/log_questions.py`.
- **Lý do:** lỗi nesting gây mất chức năng, không chỉ tổ chức. Skill bị scope sai khiến lệnh cốt lõi có thể không xuất hiện bình thường.
- **Rủi ro:** không có — all changes là git mv + path updates. Kiểm chứng: 0 ref tới `.claude/.claude/` còn lại ngoài log; hook chạy được; skill project-wide.

## [2026-09-23] Bỏ trạng thái phiên khỏi `CLAUDE.md`

- **Quyết định:** xoá mục "Trạng thái phiên làm việc" (~35 dòng) khỏi root `CLAUDE.md`, thay bằng 1 dòng trỏ tới handoff mới nhất + `index.md` §Sources. Hai quy tắc định dạng còn dùng lâu dài (`sources:` inline list; bullet không mở đầu bằng `[[wikilink]]`) chuyển vào mục "Nhắc nhanh về trang wiki".
- **Lý do:** `CLAUDE.md` nạp vào mọi lượt của mọi session; trạng thái phiên trùng với `.claude/session_handoffs/` và đã lỗi thời (còn ghi Part One trong khi handoff 14:32 đã xong Part Two). Người dùng duyệt để tối ưu token.
- **Ch.17 `fixed_income_during`:** năm thời kỳ lịch sử được tách thành trang atomic xoay quanh cơ chế thất bại chính sách (policy failure) và xung đột thể chế, không tường thuật sự kiện — chuyển từ `CLAUDE.md` sang đây.

## [2026-09-23] `/query` lượt đắt luôn gọi `--backlinks` cho trang cốt lõi

- **Quyết định:** với mỗi trang trực tiếp liên quan tới câu hỏi (không phải mọi trang mở rộng qua outlink), lượt đắt của `/query` luôn gọi `validate_wiki_page.py --backlinks <trang>` bên cạnh việc đi theo `[[wikilink]]` outlink, rồi triage kết quả bằng tên file như lượt rẻ. Áp dụng mọi lượt, không chỉ khi outlink có vẻ chưa đủ.
- **Lý do:** ingest chỉ *yêu cầu* backlink 2 chiều khi tạo/sửa trang (§6), không đảm bảo mọi trang cũ tuân thủ đủ — một trang B có thể trỏ vào A mà A không có outlink ngược lại B, khiến đi outlink từ A không bao giờ thấy B. `--backlinks` là lệnh CLI rẻ (không tốn token đọc file), nên chạy đều mỗi lượt rẻ hơn việc dựa vào phán đoán chủ quan "outlink có vẻ thiếu" — người dùng chọn phương án luôn chạy để nhất quán.
- **Phạm vi:** chỉ sửa `query/SKILL.md` bước 3; không đổi lượt rẻ, không đổi `00_schema.md` (không phải thay đổi data model).

## [2026-09-23] `/query` — 3 kỷ luật mượn từ `anthropic-skills:deep-research`

- **Quyết định:** sau khi đọc trực tiếp `SKILL.md` thật của `deep-research` (kiến trúc coordinator → N subagent song song → report writer) và so với `query/SKILL.md`, thêm 3 kỷ luật không cần subagent: (1) bước 3 giới hạn đúng 1 vòng mở rộng qua outlink/`--backlinks` mới phát hiện, không đệ quy vòng 2; (2) bước 2 thêm hướng dẫn hỏi làm rõ khi thuật ngữ Việt có ≥ 2 cách dịch Anh không tương đương nghĩa, chỉ hỏi khi lựa chọn sai đổi hẳn kết quả; (3) bước 5 thêm dedup `grep -l "^type: analysis" 02_wiki/*.md` trước khi tạo trang `analysis` mới, theo đúng mẫu `ingest` bước 2.
- **Lý do:** deep-research giới hạn cứng "chỉ 1 vòng bổ sung" để tránh phình chi phí/độ trễ vô hạn — `/query` vừa thêm `--backlinks` (mục trên) nhưng chưa có cap, có thể đệ quy không giới hạn. Deep-research có bước hỏi làm rõ trước khi nghiên cứu khi thuật ngữ mơ hồ — `/query` mới chỉ cảnh báo rủi ro dịch Việt→Anh, chưa có hướng dẫn khi nào nên hỏi lại. Deep-research kiểm trùng thư mục báo cáo trước khi tạo report mới — `/query` bước 5 (tạo `analysis`) chưa có bước tương đương, khác `ingest` vốn luôn dedup trước khi tạo trang.
- **Không mượn:** cơ chế fan-out song song qua subagent (giá trị cốt lõi của deep-research) — đụng luật cứng CLAUDE.md global "không tự động spawn agent/subagent"; `/query` giữ nguyên thiết kế đơn luồng vì corpus là kho đóng đã ingest, không cần đi tìm nguồn mới.

## [2026-09-23] Thêm skill `/research` và op thứ 8 `research`

- **Quyết định:** thêm `.claude/skills/research/SKILL.md`, gộp 3 chức năng (tổng hợp/đối chiếu nội bộ nhiều trang, bổ sung claim từ nguồn đã ingest, đánh giá gap tri thức theo cluster chủ đề). Ghi log bằng op mới `research` — không tái dùng `query`/`review`/`lint`. Sửa `00_schema.md` §2 (Taxonomy `analysis`: Query, Research), §4 (ngưỡng cluster/enrich), §9 (stable/stale→draft thêm Research khi enrich), §12 (7→8 giá trị `<op>`).
- **Lý do thêm op mới thay vì tái dùng:** research vừa đọc liên trang như `query` (nhưng chủ động chọn cả cụm, không dừng ở 1 câu hỏi), vừa quay lại nguồn như `review-node` (nhưng THÊM claim mới thay vì chỉ verify claim có sẵn), vừa xuất báo cáo như `lint` (nhưng giới hạn trong 1 cluster, không toàn wiki). Không op nào trong 7 op cũ mô tả đúng "chủ động mở rộng nội dung 1 cụm theo chủ đề, có quay lại nguồn". Gộp vào op cũ sẽ xoá mất khả năng phân biệt sau này khi đọc `log.md`: "trang X được sửa vì nghi sai" (review) khác hẳn "cụm trang Y được chủ động đào sâu, thêm claim mới" (research) — hai loại rủi ro khác nhau khi audit lại lịch sử.
- **Lý do giới hạn phạm vi enrich chỉ chunk `[x]`:** `03_state/<source id>.md` là nguồn sự thật duy nhất cho tiến độ ingest (`.claude/rules/source-management.md`). Nếu research tự đọc thêm chunk `[~]`/`[ ]` để lấy claim, nội dung wiki sẽ vượt trước bản đồ chunk mà không ai cập nhật nó — vi phạm nguyên tắc "không dựng lại trạng thái từ dấu vết khác" theo chiều ngược (nội dung đi trước, state file theo sau, thay vì state file luôn phản ánh đúng hiện trạng). Research dừng và đề xuất `/ingest` để giữ đúng vai: research đào sâu phần đã có, ingest mở rộng phần mới.
- **Lý do không mượn fan-out subagent:** nhất quán với quyết định [2026-09-23] "`/query` — 3 kỷ luật mượn từ `anthropic-skills:deep-research`" — luật cứng CLAUDE.md global cấm tự động spawn agent/subagent song song. Research cũng đọc trên kho đã ingest (đóng), không cần tốc độ song song vốn chỉ có giá trị khi phải tìm nguồn mới trên web.
