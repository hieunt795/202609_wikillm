# Schema — Quy tắc dự án LLM Wiki

> File này định nghĩa mô hình dữ liệu (data model) của wiki. `agents.md` tham chiếu đến các mục dưới đây cho từng operation, không lặp lại nội dung.

## 1. Frontmatter chuẩn cho trang wiki (`02_wiki/*.md`)

```yaml
title:
type: entity | concept | case | analysis
tags: []
sources: []        # liên kết tới nguồn trong 01_sources
status: stub | draft | stable | stale     # vòng đời: xem §9
last_updated:
reviewed:          # TUỲ CHỌN — ngày người dùng xác nhận đã đọc qua; không có = chưa xác nhận (§9)
```

## 2. Taxonomy (phân loại trang wiki)

| type | Mô tả | Tạo ở operation nào |
|---|---|---|
| entity | Người, tổ chức, công cụ, khung/hệ thống có danh tính riêng (vd: SNA, GFS) | Ingest |
| concept | Khái niệm, ý tưởng, định nghĩa tổng quát — áp dụng được ngoài 1 bối cảnh cụ thể | Ingest |
| case | Tường thuật gắn với 1 bối cảnh cụ thể (quốc gia + giai đoạn thời gian), không tổng quát hóa được, dùng làm minh chứng thực tế cho `concept` liên quan | Ingest |
| analysis | Tổng hợp, so sánh, nhận định agent tự sinh ra từ nhiều nguồn/trang đã có trong wiki | Query (cần xác nhận người dùng trước khi tạo — xem `agents.md` §Query) |

Loại trừ (không tạo trang wiki): bài tập/exercise cuối chương, bảng số liệu thô. Nếu cần, chỉ trích dẫn số liệu bên trong trang `case` liên quan, không tạo trang riêng cho bảng.

**Ưu tiên lý luận trước tường thuật.** Khi một nguồn tách rõ phần khung khái niệm với phần tường thuật bối cảnh một quốc gia/giai đoạn, ingest phần khung khái niệm trước và ingest phần bối cảnh **chỉ khi** wiki còn thiếu minh chứng cho một `concept` đã có. Lý do: `case` tồn tại để chống lưng cho `concept` (bảng trên), nên khi một concept đã đủ minh chứng thì thêm case nữa không tăng sức giải thích mà chỉ làm loãng tỷ lệ lý luận/tường thuật của wiki. Phần bối cảnh bị bỏ qua vẫn phải có dòng riêng trong bản đồ chunk kèm lý do (§10), không xoá khỏi bảng.

`concept` có một pattern con cần nhận diện: **bridge note** — trang chỉ mô tả *quan hệ* giữa 2 khái niệm liền kề (vd `income-absorption-identity` nối absorption với GNDI). Bridge note là trang độc lập, không được nhét vào một trong hai trang đầu mút.

## 3. Quy ước cấu trúc & đặt tên

- `02_wiki/` là cấu trúc phẳng — không tách thư mục con theo loại; phân loại qua trường `type` trong frontmatter.
- Tên file trang wiki: kebab-case, khớp với `title`.
- `01_sources/` là bất biến — **chỉ đọc, không ngoại lệ**: không sửa nội dung, không thêm file, không đổi tên, không xoá. Mọi thứ agent cần *ghi* về một nguồn đều nằm ngoài thư mục đó.
- `03_state/` là vùng trạng thái do agent sở hữu, máy-đọc-được, gồm 2 loại file: 1 bản đồ chunk `03_state/<tên_nguồn>.md` cho mỗi nguồn dài, và 1 bản kê xuất xứ chung `03_state/_sources_manifest.md` (§10). Tách khỏi `01_sources/` chính là để luật bất biến ở trên không cần ngoại lệ nào.
- Vùng capture tạm `_inbox.md` nằm ở gốc dự án, **không** nằm trong `02_wiki/` (§11). Đây là văn xuôi cho người đọc, khác bản chất với `03_state/` nên không gộp chung.

## 4. Ngưỡng vận hành

| Hoạt động | Ngưỡng |
|---|---|
| Ingest | Tạo/cập nhật 5–15 trang wiki mỗi lần |
| Lint | Chạy sau mỗi 10 lần ingest, hoặc theo lịch định kỳ |
| Mâu thuẫn (conflict) | Không tự sửa — đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ xử lý |
| Phân loại nguồn ngắn / nguồn dài | Ngưỡng định lượng ở §10. Nguồn dài bắt buộc có file trạng thái trong `03_state/` |
| Triage `_inbox.md` | Mỗi lượt lint (§11) |

## 5. Nguyên tắc Atomic

Mỗi trang wiki chỉ chứa 1 ý tưởng/khái niệm duy nhất — **nhưng phải bao quát đầy đủ ý tưởng đó**. Atomic là một điểm cân bằng, không phải "càng nhỏ càng tốt": trang quá rộng làm mờ kết nối cụ thể, trang quá vụn làm loãng mạng liên kết.
Nếu nội dung trích từ nguồn chứa >1 ý tưởng độc lập có thể đứng riêng → tách thành nhiều trang, không gộp vào 1 trang dài.

**Ba phép kiểm, theo thứ tự. Không dùng số từ làm căn cứ ở bất kỳ bước nào.**

1. **Kiểm tra title** — có viết được một câu khẳng định duy nhất mô tả đúng toàn bộ nội dung trang không? Nếu title chính xác buộc phải dùng "và" để nối hai mệnh đề khác nhau thì trang đang chứa hai ý (§8).
2. **Kiểm tra nhu cầu liên kết tới từng phần** — có trang nào sẽ cần liên kết tới chỉ một phần của trang này không? Nếu có, phần đó cần tồn tại như một trang riêng. Đây là phép kiểm phân biệt được nhiều trường hợp nhất.
3. **Kiểm tra heading** — thân bài cần heading cấp 2+ để tách ý là dấu hiệu trang chứa nhiều ý (§7).

**Danh sách liệt kê lấy từ nguồn là một ý có N thành phần, không phải N ý.** Tách nó tạo ra N trang mà không trang nào cần liên kết tới riêng lẻ.

Khi một phần nội dung cần tồn tại độc lập, có hai cách xử lý. Theo Evergreen, chi phí của trang quá rộng là các liên kết tới phần nội dung nằm trong nó không hình thành được, vì phần đó không có tên riêng để liên kết tới. Cách xử lý là cấp tên riêng cho phần đó: tách thành trang mới, hoặc giữ nguyên trang dài và chuyển nó thành trang liên kết tới các trang đã tồn tại sẵn ở nơi khác.

**Độ dài không phải tiêu chí.** Đo trên 116 trang ngày 2026-09-14: độ dài với số outlink r = +0,07; độ dài với số backlink r = −0,09. Độ dài chủ yếu phụ thuộc việc nguồn có liệt kê hay không — trang có title dạng liệt kê trung vị 355 từ, các trang khác 268 từ. Trang ở bậc trên của thang phân loại Evergreen (trang tổng hợp, trang đầu mối) có độ dài lớn là đúng thiết kế: `system-of-national-accounts-sna` dài 405 từ và liên kết tới 10 trang khác.

Chủ đề (topic) là đơn vị gom nhóm tạm thời để tìm liên kết khi ingest (xem `agents.md` §Ingest bước 2b) — một chủ đề thường chứa nhiều trang atomic, không phải 1 chủ đề = 1 trang. Luật Atomic ở trên vẫn là luật quyết định ranh giới trang cuối cùng trong mỗi chủ đề.

## 6. Liên kết giữa các trang wiki (densely linked)

- Liên kết giữa trang wiki với trang wiki khác dùng `[[wikilink]]` ngay trong thân bài (không dùng field frontmatter riêng).
- **Hai dạng link, cùng một đích.** `[[tên-trang]]` và `[[tên-trang|nhãn hiển thị]]` là như nhau; dạng có `|` dùng khi tên trang không đọc lọt vào câu văn (vd `[[real-wages|lương thực]]`). Phần trước dấu `|` **luôn** là tên file, phần sau chỉ là chữ hiển thị. Mọi công cụ đếm liên kết phải cắt ở `|` trước khi so khớp — grep `[[tên-trang]]` trần sẽ bỏ sót toàn bộ link dạng này.
- `sources: []` trong frontmatter chỉ dùng để trỏ tới `01_sources/`, không dùng để liên kết giữa các trang wiki.
- Một trang hợp lệ cần có ít nhất 1 outlink (`[[wikilink]]` trỏ ra) và lý tưởng có backlink (trang khác trỏ vào) — trừ trang `status: stub` vốn chưa có thân bài (§9). Xem tiêu chí lint ở `agents.md` §Lint.
- Cách viết `[[wikilink]]` trong câu: xem §7.
- **`tags` KHÔNG phải cơ chế liên kết.** Tag chỉ là chỉ mục rẻ để lọc nhanh khi quét frontmatter (tối ưu token). Hai trang cùng tag *chưa* được coi là đã liên kết — quan hệ ý tưởng phải luôn được viết thành `[[wikilink]]` có lý do.
- **Stub link được khuyến khích:** khi cần trỏ tới một khái niệm chưa được ingest, tạo luôn trang `status: stub` (chỉ title + frontmatter, thân bài 1 câu định nghĩa ngắn hoặc để trống) rồi link tới — không hoãn liên kết lại để chờ ingest batch sau, vì liên kết bị hoãn thường mất luôn.
- Heuristic chọn trang để link ở bước Ingest 3b: hỏi **"trang này sẽ cần xuất hiện lại trong ngữ cảnh nào?"** — không hỏi "trang này thuộc category nào".

## 7. Cấu trúc thân bài trang wiki

Thân bài (phần dưới frontmatter) tuân theo 5 luật:

1. **Không dùng heading (`##`, `###`...) trong thân bài.** Title trong frontmatter là heading duy nhất của trang. Nếu nội dung cần heading để tách ý, đó là dấu hiệu phải tách thành nhiều trang (§5), không thêm heading vào 1 trang.
2. **Câu đầu tiên nêu thẳng định nghĩa/ý tưởng cốt lõi**, không dẫn nhập kiểu "Trong chương này...", "Theo tài liệu...". Không giải thích lại kiến thức phổ quát mà model đã biết.
3. **Liên kết `[[wikilink]]` nằm trong câu văn, kèm lý do liên kết ngắn** — không dồn thành danh sách "xem thêm" rời ở cuối trang. Một link không giải thích lý do không tạo giá trị mạng thật.
4. **Viết lại bằng ngôn ngữ của mình, không sao chép nguyên văn nguồn.** Sao chép nguyên văn không tạo ra hiểu biết — chỉ khi diễn đạt lại mới lộ ra chỗ chưa hiểu và chỗ mâu thuẫn. Công thức/định nghĩa kỹ thuật được phép giữ nguyên ký hiệu, nhưng phần diễn giải phải là lời viết lại.
5. **Claim lấy từ nguồn dài phải kèm chú thích vị trí.** Khi claim lấy từ một nguồn thuộc diện *nguồn dài* (§10), câu chứa claim ghi vị trí trong nguồn ngay sau claim, dạng `(<nguồn>, <chương>, <mục>)`, thêm dải dòng `d.<từ>–<đến>` khi mục dài. Lý do: `sources: []` chỉ nói claim đến *từ file nào* — với file 829 KB thì xác minh lại một câu phải đọc lại phần lớn nguồn. Nguồn ngắn không bắt buộc vì đọc trọn lại được trong 1 lượt.

   Chú thích đi kèm **claim**, không đi kèm trang: một trang gộp vật liệu từ nhiều mục thì mỗi claim mang chú thích của mục sinh ra nó. Không dồn tất cả thành một chú thích cuối trang — cùng lý do với luật 3.

   **Áp dụng từ lượt ingest kế tiếp trở đi.** Các trang có trước ngày luật có hiệu lực không sửa hàng loạt; backfill là một khoản nợ kỹ thuật riêng, đã ghi trong `log.md`. Hook thực thi luật này theo `last_updated`: trang nào được chạm vào và nâng ngày lên thì phải có chú thích, tức nợ trả dần theo lúc động tới chứ không sinh thêm nợ mới.

Ví dụ:

```markdown
---
title: gdp
type: concept
tags: [national-accounts, sna]
sources: [imf_macro_accounting]
status: draft
last_updated: 2026-09-12
---

GDP (Gross Domestic Product) là tổng giá trị gia tăng (value added) của tất cả các khu vực
trong nền kinh tế, tính theo nguyên tắc cư trú (residency) — chỉ sản xuất của đơn vị cư trú
được tính, không phân biệt quốc tịch (imf_macro_accounting, Ch.2, The Main Aggregates, d.650–679).

GDP có thể tính theo 3 cách tương đương: [[production-income-and-expenditure-approaches-yield-the-same-gdp]]
(imf_macro_accounting, Ch.2, Alternative Approaches to Determining GDP, d.684–750). Đây là khái niệm gross —
đã bao gồm khấu hao — nên khi cần đo năng lực sản xuất tăng thêm thật sự thì phải trừ khấu hao ra.
Bản thân con số GDP trộn lẫn thay đổi giá với thay đổi sản lượng, nên mọi so sánh qua thời gian
đều phải đi qua [[real-gdp]] (imf_macro_accounting, Ch.2, Nominal and Real GDP, d.882–915). Vì GDP chỉ
tính thu nhập phát sinh trong nước, nó bỏ qua thu nhập nhận từ/trả cho người không cư trú — đây là
lý do cần [[gni]] bổ sung (imf_macro_accounting, Ch.2, Gross National Income, d.757–779).
```

Bốn chú thích trong ví dụ trỏ tới bốn mục khác nhau của cùng một chương — đó là điểm của luật 5: mỗi claim
về đúng chỗ sinh ra nó, không phải về đúng file.

## 8. Quy ước đặt title

Title là **giao diện (API) của trang** — là thứ các trang khác "gọi" tới qua `[[wikilink]]`. Title phải đứng độc lập khỏi nguồn gốc: đọc riêng title vẫn hiểu trang nói gì, không cần biết nó trích từ tài liệu nào.

Chọn dạng title theo loại nội dung:

| Loại nội dung | Dạng title | Ví dụ |
|---|---|---|
| Thuật ngữ cốt lõi mà nhiều trang khác trỏ tới (`concept`, `entity`) | Danh từ / cụm danh từ | `gdp`, `absorption`, `system-of-national-accounts-sna` |
| Nhận định, phát hiện, tường thuật (`case`, `analysis`, bridge note) | **Câu hoàn chỉnh mang tính khẳng định** | `wage-controls-lose-effectiveness-rapidly-after-a-short-period` |
| Nội dung nguồn còn tranh luận, chưa đủ chứng cứ kết luận | **Câu hỏi** | `to-what-extent-was-poland-output-decline-1990-91-overstated` |

Ba luật kèm theo:

1. **Ưu tiên khẳng định tích cực thay vì phủ định.** Title phủ định che mất lý thuyết nằm dưới nó. Vd: thay vì `mps-khong-do-duoc-dich-vu-phi-vat-chat` → viết `mps-chi-tinh-san-luong-thuoc-linh-vuc-vat-chat`.
2. **Title dạng câu hỏi là trạng thái tạm.** Khi đã đủ chứng cứ, refactor thành title khẳng định và cập nhật các `[[wikilink]]` trỏ tới.
3. **Không đặt được title sắc gọn = dấu hiệu trang vi phạm Atomic** (§5) — tách trang, không đặt title mơ hồ cho xong.

Tên file luôn là kebab-case của title (§3), kể cả với title dạng câu.

## 9. Vòng đời `status`

| status | Nghĩa | Chuyển tiếp |
|---|---|---|
| `stub` | Chỉ có title + frontmatter, thân bài rỗng hoặc 1 câu. Sinh ra khi trang khác cần link tới khái niệm chưa ingest (§6) | → `draft` khi được ingest nội dung thật |
| `draft` | Đã có nội dung từ ít nhất 1 nguồn, chưa được đối chiếu/bồi đắp | → `stable` khi đã qua ít nhất 1 lượt lint không lỗi |
| `stable` | Nội dung đủ, liên kết đủ, không mâu thuẫn tồn đọng | → `stale` khi có nguồn mới liên quan được ingest sau `last_updated` |
| `stale` | Có nguồn mới liên quan nhưng trang chưa cập nhật | → `draft`/`stable` sau khi merge nội dung mới |

`stub` tồn đọng quá lâu là nợ kỹ thuật của wiki — lint phải báo cáo stub chưa được ingest sau nhiều lượt (xem `agents.md` §Lint).

### `status` không đo việc người dùng đã đọc qua

`status` chỉ đo **vòng đời nội dung**: trang đã đủ chất chưa, có nguồn mới chưa merge chưa. Nó không phân biệt "trang agent vừa viết cho agent dùng" với "trang người dùng đã đọc và xác nhận". Kể cả `stable` cũng chỉ có nghĩa *đã qua ít nhất 1 lượt lint không lỗi* — lint là kiểm máy, không phải người đọc.

Hai trục này trực giao nên **không gộp vào `status`**: gộp lại sẽ sinh ra các ô lai vô nghĩa (`stale` nhưng đã duyệt? `stub` đã duyệt?) và làm bảng chuyển tiếp ở trên mất tính đơn tuyến.

Giải pháp: trường **`reviewed:` tuỳ chọn** trong frontmatter (§1), giá trị là ngày người dùng xác nhận đã đọc qua trang. Không có trường này = chưa xác nhận.

- **Tuỳ chọn, không bắt buộc.** Hook không kiểm; các trang có sẵn không phải backfill.
- **Chỉ người dùng đặt `reviewed:`.** Agent không tự đặt, kể cả khi vừa sửa xong trang — trường này ghi nhận *người đã đọc*, agent đặt hộ thì trường mất hết ý nghĩa.
- `reviewed:` cũ hơn `last_updated:` nghĩa là trang đã đổi sau lần duyệt. Đây là **thông tin tham khảo, không phải lỗi lint** — cố ý không thêm tiêu chí lint cho trường này: ở quy mô một người dùng, biến nó thành lỗi chỉ tạo ra nhiễu phải bỏ qua mỗi lượt.

## 10. Nguồn dài: ngưỡng phân loại và file trạng thái ingest

### Ngưỡng phân loại

Một nguồn trong `01_sources/` là **nguồn dài** khi vượt bất kỳ ngưỡng nào dưới đây:

| Chỉ số | Ngưỡng nguồn dài |
|---|---|
| Dung lượng text | > 120 KB |
| Số dòng | > 1.200 dòng |
| Một chương đơn lẻ | tự nó đã vượt một trong hai ngưỡng trên |

Cơ sở của con số: ~120 KB ≈ 30k token — vẫn đọc trọn được 1 lượt, nhưng chiếm gần hết ngân sách context và không còn chỗ cho bước đối chiếu với toàn bộ `02_wiki/` (Ingest bước 2). Quá ngưỡng đó thì mẫu hai lượt mất tác dụng, buộc phải ingest theo chương/cụm.

Không dùng số heading làm tiêu chí: một nguồn ngắn có cấu trúc dày (`Modern Money Mechanics` có 66 heading trong 721 dòng) vẫn đọc trọn được 1 lượt.

Đo bằng lệnh, không ước lượng bằng mắt: `wc -c -l <file>`.

Hiện trạng:

| Nguồn | Dung lượng | Số dòng | Phân loại |
|---|---|---|---|
| `imf_macro_accounting` | 829 KB | 6.065 | **Nguồn dài** — có `03_state/imf_macro_accounting.md` |
| `Modern Money Mechanics` | 83 KB | 721 | Nguồn ngắn — ingest trọn 1 lượt, không cần file trạng thái |

### File trạng thái ingest

Mỗi **nguồn dài** có đúng 1 file trạng thái `03_state/<tên_nguồn>.md`.

Đây là **nguồn sự thật duy nhất** cho câu hỏi "còn lại phần nào" — agent không diễn giải lại văn xuôi trong `log.md` để trả lời câu hỏi đó. Phân vai: `log.md` là nhật ký append-only kể *chuyện gì đã xảy ra*; file trạng thái là bảng nói *hiện đang ở đâu*. Hai file không thay thế nhau và không được mâu thuẫn nhau.

**Vì sao `03_state/` chứ không đặt cạnh nguồn trong `01_sources/`:** đặt cạnh nguồn tra cứu tiện hơn một nhịp, nhưng phải khoét một ngoại lệ vào luật bất biến `01_sources/` (§3) — và một luật cứng đã có ngoại lệ thứ nhất thì sẽ có ngoại lệ thứ hai. `03_state/` giữ luật đó tuyệt đối và kiểm được bằng một câu hỏi duy nhất: *có file nào trong `01_sources/` không phải tài liệu nguồn không?* Đánh đổi: phải nhớ thêm một đường dẫn, và file trạng thái phải tự khai đường dẫn nguồn ở trường `file:`. Đây là lựa chọn có chủ đích, không phải sơ suất — lần audit sau đừng đề xuất chuyển ngược lại.

Cấu trúc bắt buộc: frontmatter tối thiểu + một bảng bản đồ chunk dạng checkbox.

```markdown
---
source: <tên thư mục nguồn>
file: <đường dẫn đầy đủ tới file nguồn, tính từ gốc dự án>
total_lines: <số dòng>
last_updated: YYYY-MM-DD
---

| Xong | Chunk | Dòng | Mục trong nguồn | Ghi chú |
|---|---|---|---|---|
| `[x]` | Ch.2 · cụm A — đại lượng hạch toán | d.607–934 | The System of National Accounts → Problems of GDP Measurement | 14 trang + 6 stub |
| `[~]` | Ch.3 — Fiscal Accounting | d.1954–3425 | ... | còn phần Tax Effort Analysis trở đi |
| `[ ]` | Ch.4 — Balance of Payments | d.3426–4529 | ... | |
```

Ô trạng thái dùng đúng 3 ký hiệu:

| Ký hiệu | Nghĩa |
|---|---|
| `[x]` | đã ingest xong |
| `[~]` | đang ingest dở — cột *Ghi chú* **phải** nêu rõ phần nào còn lại |
| `[ ]` | chưa ingest |

Đơn vị chunk: **chương** với nguồn có chương; **cụm chủ đề** khi một chương tự nó vượt ngưỡng nguồn dài. Mỗi chunk ghi kèm dải dòng `d.<từ>–<đến>` tính theo file nguồn khai ở `file:` — dải dòng chính là thứ khiến chú thích vị trí ở §7.5 kiểm chứng được. Số dòng dùng làm khoá tra cứu được chính vì `01_sources/` bất biến: nguồn không bị sửa thì số dòng không trôi.

Chunk cố ý bỏ qua (mục lục, lời tựa, bài tập cuối chương, phụ lục số liệu thô — §2) vẫn có dòng riêng, đánh `[x]` và ghi chú "bỏ qua, không tạo trang". Bỏ hẳn khỏi bảng sẽ khiến lượt sau tưởng là còn sót.

### Bản kê xuất xứ nguồn

`03_state/_sources_manifest.md` ghi cho **mọi** nguồn (dài lẫn ngắn): nhan đề, tác giả, nơi và năm xuất bản, đường dẫn từng file, số byte, số dòng, SHA-256.

Lý do tồn tại: `01_sources/` không được đưa lên kho công khai (tài liệu bên thứ ba), nên một bản clone không có file nguồn. Chú thích vị trí §7.5 và bản đồ chunk ở trên đều trỏ tới *số dòng* của file nguồn — chỉ còn kiểm chứng được nếu người đọc tự lấy bản gốc và đối chiếu được đúng bản nào. SHA-256 là thứ làm việc đó. Thêm nguồn mới thì thêm mục vào bản kê ngay trong lượt ingest đầu tiên.

## 11. Vùng capture tạm (`_inbox.md`)

`_inbox.md` ở gốc dự án là nơi ghi ý tưởng/insight chưa đủ chín thành trang evergreen: câu hỏi chợt nảy ra khi đọc nguồn, nghi ngờ về một trang đã có, liên kết chưa chắc, chủ đề muốn ingest sau.

Lý do tách khỏi `02_wiki/`: mọi trang trong `02_wiki/` phải là trang atomic hợp lệ (§5, §7) và bị hook kiểm mỗi lần ghi. Ý tưởng dang dở không thoả được luật đó — không có chỗ chứa riêng thì nó hoặc bị nhét bừa vào một trang (làm trang vi phạm Atomic), hoặc mất luôn. `status: stub` **không** thay thế được vùng này: stub giữ chỗ cho một *khái niệm đã biết tên*, còn inbox chứa được cả câu hỏi chưa có tên.

Quy ước:

- Định dạng phẳng, mỗi ý là 1 gạch đầu dòng kèm ngày: `- [YYYY-MM-DD] <ý tưởng>`. Không frontmatter, không luật trang wiki, không giới hạn atomic.
- `_inbox.md` nằm **ngoài mạng liên kết**: không trang nào trong `02_wiki/` được `[[wikilink]]` trỏ vào nó, và nó không xuất hiện trong `index.md`.
- **Triage mỗi lượt lint.** Mỗi mục có đúng 3 kết cục: nâng thành trang wiki, gộp vào trang đã có, hoặc xoá. Không có kết cục "để đó".
- Mục tồn quá 3 lượt lint là nợ kỹ thuật — lint báo cáo (tiêu chí *Nợ inbox*), không tự xử lý.
