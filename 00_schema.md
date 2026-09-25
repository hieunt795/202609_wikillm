# Schema — Quy tắc dự án LLM Wiki

> File này định nghĩa mô hình dữ liệu (data model) của wiki. `CLAUDE.md` và các skill trong `.claude/skills/` tham chiếu tới các mục dưới đây, không lặp lại nội dung. Lý do đứng sau từng luật nằm ở `decisions.md` (mục *[2026-09-17] Lý do dời từ `00_schema.md`* và các mục trước đó); schema chỉ giữ luật.

## 1. Frontmatter chuẩn cho trang wiki (`02_wiki/*.md`)

```yaml
title:
type: entity | concept | case | analysis
tags: []
sources: []        # source id trong 03_state/_sources_manifest.md (§10)
status: stub | draft | stable | stale     # vòng đời: xem §9
last_updated:
reviewed:          # TUỲ CHỌN — ngày trang được review đối chiếu nguồn; không có = chưa review (§9)
reviewed_by:       # user | model — bắt buộc khi có reviewed (§9)
```

## 2. Taxonomy (phân loại trang wiki)

| type | Mô tả | Tạo ở operation nào |
|---|---|---|
| entity | Người, tổ chức, công cụ, khung/hệ thống có danh tính riêng (vd: SNA, GFS) | Ingest |
| concept | Khái niệm, ý tưởng, định nghĩa tổng quát — áp dụng được ngoài 1 bối cảnh cụ thể | Ingest |
| case | Tường thuật gắn với 1 bối cảnh cụ thể (quốc gia + giai đoạn thời gian), không tổng quát hóa được, dùng làm minh chứng thực tế cho `concept` liên quan | Ingest |
| analysis | Tổng hợp, so sánh, nhận định agent tự sinh ra từ nhiều nguồn/trang đã có trong wiki | Query, Research (cần xác nhận người dùng trước khi tạo — `.claude/skills/query/SKILL.md` bước 5, `.claude/skills/research/SKILL.md` chức năng A) |

Loại trừ (không tạo trang wiki): bài tập/exercise cuối chương, bảng số liệu thô. Nếu cần, chỉ trích dẫn số liệu bên trong trang `case` liên quan, không tạo trang riêng cho bảng.

`concept` có một pattern con: **bridge note** — trang chỉ mô tả *quan hệ* giữa 2 khái niệm liền kề (vd `current-account-deficit-means-absorption-exceeds-national-income` nối `absorption` với `gndi`). Bridge note là trang độc lập, không nhét vào một trong hai trang đầu mút.

**Ưu tiên lý luận trước tường thuật.** Khi một nguồn tách rõ phần khung khái niệm với phần tường thuật bối cảnh, ingest phần khung khái niệm trước; ingest phần bối cảnh **chỉ khi** wiki còn thiếu minh chứng cho một `concept` đã có. Phần bối cảnh bị bỏ qua vẫn có dòng riêng trong bản đồ chunk kèm lý do (§10).

**Không có trang tóm tắt nguồn.** Vai trò đó chia cho `index.md` §Sources, `03_state/` và trường `sources:` cộng chú thích §7.5 trên từng trang. Đây là lựa chọn có chủ đích, không phải thiếu sót.

## 3. Quy ước cấu trúc & đặt tên

- `02_wiki/` là cấu trúc phẳng — không tách thư mục con theo loại; phân loại qua trường `type`.
- Tên file trang wiki: kebab-case, khớp với `title`.
- **Ngôn ngữ:** `title` và tên file viết bằng **tiếng Anh**; thân bài viết bằng **tiếng Việt**, theo profile wiki của skill `writing-style`.
- `01_sources/` là bất biến — **chỉ đọc, không ngoại lệ**: không sửa nội dung, không thêm file, không đổi tên, không xoá. Mọi thứ agent cần *ghi* về một nguồn đều nằm ngoài thư mục đó. Phép thử: mọi file `.md`/`.pdf` trong `01_sources/` đều có trong bản kê và khớp SHA-256 (`validate_wiki_page.py --verify-sources`).
- `03_state/` là vùng trạng thái do agent sở hữu, máy đọc được, gồm 1 bản kê xuất xứ chung `03_state/_sources_manifest.md` và 1 bản đồ chunk `03_state/<source id>.md` cho mỗi nguồn dài đã bắt đầu ingest (§10).
- Vùng capture tạm `_inbox.md` nằm ở gốc dự án, **không** nằm trong `02_wiki/` (§11).
- Báo cáo lint/audit/research lưu ở `Claude outputs/` (không commit), tên `lint-<YYYY-MM-DD>-<số trang>.md`, `audit-<YYYY-MM-DD>-<chủ đề>.md`, hoặc `research-<YYYY-MM-DD>-<chủ đề>.md`.

## 4. Ngưỡng vận hành

| Hoạt động | Ngưỡng |
|---|---|
| Ingest | Tạo/cập nhật 5–15 trang wiki mỗi lần (stub không tính) |
| Lint | Chạy sau mỗi 10 lần ingest, hoặc theo lịch định kỳ |
| Review | Tối đa 5 trang mỗi lượt |
| Research | Cluster đọc trọn tối đa 10 trang/lượt; enrich (ghi claim mới) tối đa 5 trang/lượt |
| Mâu thuẫn (conflict) | Không tự sửa — đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ xử lý |
| Kích thước 1 trang | Đủ nhỏ để viết trọn trong 1 lượt. Không viết hết được trong 1 lượt → trang đang gộp nhiều ý, phải tách (§5) |
| Phân loại nguồn ngắn / nguồn dài | Ngưỡng ở §10. Nguồn dài có file trạng thái trong `03_state/` từ lượt ingest đầu |
| Triage `_inbox.md` | Mỗi lượt lint (§11) |

## 5. Nguyên tắc Atomic

Mỗi trang wiki chỉ chứa 1 ý tưởng/khái niệm duy nhất — **nhưng phải bao quát đầy đủ ý tưởng đó**. Atomic là điểm cân bằng, không phải "càng nhỏ càng tốt". Nội dung trích từ nguồn chứa >1 ý tưởng độc lập có thể đứng riêng → tách thành nhiều trang.

Hai dấu hiệu vi phạm:
- Trang có heading cấp 2+ trong thân bài → cần tách (§7).
- **Không đặt được title sắc gọn** → tư duy chưa rõ, hoặc trang đang chứa nhiều ý (§8).

Chủ đề (topic) là đơn vị gom nhóm tạm thời khi ingest (`.claude/skills/ingest/SKILL.md` bước 2) — một chủ đề thường chứa nhiều trang atomic. Luật Atomic quyết định ranh giới trang cuối cùng.

**Thành phần có tên kinh tế riêng phải có trang riêng.** Mọi thành phần trong một đồng nhất thức, bảng cân đối hay box có tên gọi kinh tế/tài chính thật (vd $W$ compensation of employees, $OS$ operating surplus, $CP$/$CG$, Treasury bills, SDR holdings) được tách thành trang `concept` riêng, dù trang có thể rất ngắn. Không có ngoại lệ theo loại box hay bảng (quyết định 2026-09-16).

**Không tách trang cho:** hệ số/tỷ trọng thuần đại số không mang tên kinh tế riêng (trọng số tăng trưởng trong công thức 5.4, tỷ lệ $b$ trong số nhân tiền, chỉ số thời gian $t$/$t-1$); đại lượng đã có trang riêng dưới tên khác — kiểm trùng bằng grep title/alias trước khi tạo.

## 6. Liên kết giữa các trang wiki (densely linked)

- Liên kết giữa trang wiki dùng `[[wikilink]]` ngay trong thân bài (không dùng field frontmatter riêng).
- **Hai dạng link, cùng một đích.** `[[tên-trang]]` và `[[tên-trang|nhãn hiển thị]]` là như nhau; phần trước `|` luôn là tên file. Đếm liên kết bằng `validate_wiki_page.py --backlinks [<trang>]`, không grep tay.
- `sources: []` chỉ trỏ tới nguồn (source id), không dùng để liên kết giữa các trang wiki.
- Trang hợp lệ có ít nhất 1 outlink và lý tưởng có backlink — trừ trang `status: stub` (§9). Tiêu chí lint: `.claude/skills/lint/SKILL.md`.
- Cách viết `[[wikilink]]` trong câu: §7.
- **`tags` KHÔNG phải cơ chế liên kết.** Tag chỉ là chỉ mục rẻ để lọc khi quét frontmatter. Quan hệ ý tưởng phải viết thành `[[wikilink]]` có lý do.
- **Stub link được khuyến khích:** khi cần trỏ tới khái niệm chưa ingest, tạo luôn trang `status: stub` rồi link — không hoãn sang batch sau.
- Heuristic chọn trang để link khi ingest: hỏi **"trang này sẽ cần xuất hiện lại trong ngữ cảnh nào?"** — không hỏi "trang này thuộc category nào".

## 7. Cấu trúc thân bài trang wiki

Thân bài (phần dưới frontmatter) tuân theo 5 luật:

1. **Không dùng heading (`##`, `###`...) trong thân bài.** Title là heading duy nhất. Cần heading để tách ý = phải tách trang (§5).
2. **Câu đầu tiên nêu thẳng định nghĩa/ý tưởng cốt lõi**, không dẫn nhập kiểu "Trong chương này...". Không giải thích lại kiến thức phổ quát.
3. **`[[wikilink]]` nằm trong câu văn, kèm lý do liên kết ngắn** — không dồn thành danh sách "xem thêm" cuối trang.
4. **Viết lại bằng ngôn ngữ của mình, không sao chép nguyên văn nguồn.** Công thức/định nghĩa kỹ thuật được giữ ký hiệu, phần diễn giải phải là lời viết lại. **Đồng nhất thức và công thức trình bày dưới dạng công thức**: `$$...$$` cho công thức đứng riêng dòng, `$...$` cho ký hiệu chèn trong câu.
5. **Claim lấy từ nguồn dài phải kèm chú thích vị trí** ngay sau claim, dạng `(<source id>, <chương>, <mục>, d.<từ>–<đến>)`. Nguồn nhiều file (§10) thêm file: `(<source id>, <chương>, <mục>, file <hậu tố>, d.<từ>–<đến>)`, vd `(fixed_income_during, Ch.4, Bank Money Creation, file -5, d.12–30)`. Nguồn ngắn không bắt buộc.

   Chú thích đi kèm **claim**, không đi kèm trang: mỗi claim mang chú thích của mục sinh ra nó; không dồn thành một chú thích cuối trang.

   **Áp dụng cho trang có `last_updated` từ 2026-09-14.** Trang cũ hơn không backfill hàng loạt; nợ trả dần khi trang được sửa nội dung. Hook thực thi theo `last_updated`.

   **`last_updated` đo nội dung, không đo liên kết.** Chỉ nâng khi claim thay đổi (thêm, sửa, xoá claim; merge nguồn mới). Chỉ chèn `[[wikilink]]` hoặc thêm chú thích vị trí cho claim có sẵn → **không** nâng.

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

Bốn chú thích trỏ tới bốn mục khác nhau của cùng một chương: mỗi claim về đúng chỗ sinh ra nó.

## 8. Quy ước đặt title

Title là **giao diện (API) của trang** — thứ các trang khác gọi tới qua `[[wikilink]]`. Đọc riêng title vẫn hiểu trang nói gì, không cần biết nguồn.

| Loại nội dung | Dạng title | Ví dụ |
|---|---|---|
| Thuật ngữ cốt lõi nhiều trang trỏ tới (`concept`, `entity`) | Danh từ / cụm danh từ | `gdp`, `absorption`, `system-of-national-accounts-sna` |
| Nhận định, phát hiện, tường thuật (`case`, `analysis`, bridge note) | **Câu trần thuật hoàn chỉnh** | `polands-excess-wage-tax-popiwek-was-discontinued-after-five-years` |
| `concept` có nội dung là nhận định (*declarative note*) | **Câu trần thuật hoàn chỉnh** | `wage-controls-lose-effectiveness-rapidly-after-a-short-period` |
| Nội dung nguồn còn tranh luận, chưa đủ chứng cứ | **Câu hỏi** | `to-what-extent-was-polands-early-transition-output-decline-overstated` |

Ba luật kèm theo:

1. **Title phủ định hợp lệ khi bản thân nhận định là phủ định.** Không ép đổi sang dạng xác định; chỉ viết lại khi có dạng xác định vừa giữ nghĩa vừa nói được nhiều hơn (vd `mps-cannot-measure-non-material-services` → `mps-counts-only-output-of-the-material-sphere`).
2. **Title dạng câu hỏi là trạng thái tạm.** Đủ chứng cứ thì refactor thành câu trần thuật và cập nhật các `[[wikilink]]` trỏ tới.
3. **Không đặt được title sắc gọn = trang vi phạm Atomic** (§5) — tách trang.

Tên file luôn là kebab-case của title (§3).

## 9. Vòng đời `status`

| status | Nghĩa | Chuyển tiếp | Ai làm |
|---|---|---|---|
| `stub` | Chỉ có title + frontmatter, thân bài rỗng hoặc 1 câu. Sinh ra khi trang khác cần link tới khái niệm chưa ingest (§6) | → `draft` khi được ingest nội dung thật | Ingest (tạo và nâng) |
| `draft` | Đã có nội dung từ ít nhất 1 nguồn | → `stable` khi người dùng duyệt danh sách *Đủ điều kiện `stable`* của lint | **Promote** (`.claude/skills/promote/SKILL.md`) |
| `stable` | Nội dung đủ, liên kết đủ, không mâu thuẫn tồn đọng | → `stale` khi nguồn mới liên quan được ingest mà lượt đó không merge vào trang | Ingest |
| `stale` | Có nguồn mới liên quan nhưng trang chưa cập nhật | → `draft` sau khi merge nội dung mới, rồi lại qua Promote | Ingest |

`stable`/`stale` được merge nội dung mới → về `draft` (Ingest; Review khi sửa claim sai; Research khi enrich thêm claim mới sau khi người dùng duyệt danh sách đề xuất — `.claude/skills/research/SKILL.md` chức năng B).

**Điều kiện lên `stable`:** hook `--all` không báo gì cho trang; outlink ≥ 1; backlink ≥ 2; không còn `⚠️ Conflict`; không bị flag ở tiêu chí nào của lượt lint gần nhất.

**Nợ stub:** stub chưa được ingest nội dung sau 3 lượt ingest kể từ khi tạo. Đếm bằng `validate_wiki_page.py --stub-debt`.

### Trường `reviewed` / `reviewed_by`

`status` chỉ đo vòng đời nội dung, không đo việc trang đã được đối chiếu hay đã được người đọc. Trục đó dùng cặp trường tuỳ chọn **`reviewed:` + `reviewed_by:`** (§1). Không có cặp này = chưa review.

- Hook chỉ kiểm khi trường có mặt: `reviewed:` là ngày `YYYY-MM-DD` và đi kèm `reviewed_by: user` hoặc `reviewed_by: model`.
- **`reviewed_by: model`** — agent đặt qua `/review-node` (`.claude/skills/review-node/SKILL.md`) sau khi đối chiếu từng claim với đúng đoạn nguồn. Đây là kiểm chứng nội dung khớp nguồn, không phải *người đã đọc*.
- **`reviewed_by: user`** — chỉ người dùng ghi. Agent không ghi đè `user`; người dùng được ghi đè `model` bằng `user`.
- `reviewed:` cũ hơn `last_updated:` = trang đã đổi sau lần duyệt. Đây là thông tin tham khảo, **không** phải lỗi lint; hàng đợi mặc định của `/review-node` nhặt lại các trang này.

## 10. Nguồn: phân loại, bản kê và file trạng thái

### Ngưỡng phân loại

Một nguồn là **nguồn dài** khi vượt bất kỳ ngưỡng nào:

| Chỉ số | Ngưỡng nguồn dài |
|---|---|
| Dung lượng text | > 120 KB |
| Số dòng | > 1.200 dòng |
| Một chương đơn lẻ | tự nó vượt một trong hai ngưỡng trên |

Không dùng số heading làm tiêu chí. Đo bằng lệnh `wc -c -l <file>`, không ước lượng. Nguồn nhiều file đo trên tổng các file.

Phân loại của từng nguồn ghi ở bản kê (dưới), không ghi ở đây.

### Bản kê xuất xứ nguồn

`03_state/_sources_manifest.md` là nơi duy nhất liệt kê nguồn. Gồm:

- **Bảng Source id**: `source id` · thư mục trong `01_sources/` · phân loại · state file. `source id` là khoá dùng trong `sources:` (§1), trong chú thích §7.5 và làm tên `03_state/<source id>.md`. Nguồn mới dùng snake_case. Hook đọc bảng này để biết nguồn nào là nguồn dài và để báo `sources:` trỏ tới id lạ.
- **Mỗi nguồn một mục**: nhan đề, tác giả, nơi và năm xuất bản, cách có file, và bảng đường dẫn · bytes · số dòng · SHA-256 cho từng file `.md`/`.pdf`.

Thêm nguồn mới vào bản kê và `index.md` §Sources **ngay trong lượt ingest đầu tiên** của nguồn đó. `validate_wiki_page.py --verify-sources` so bản kê với đĩa; chạy ở bước 0 của lint.

### File trạng thái ingest

Mỗi **nguồn dài** có đúng 1 file `03_state/<source id>.md`, tạo ở lượt ingest đầu. Đây là **nguồn sự thật duy nhất** cho câu hỏi "còn lại phần nào". `log.md` kể *chuyện gì đã xảy ra*; file trạng thái nói *hiện đang ở đâu*. Hai file không mâu thuẫn nhau.

Không đặt file trạng thái cạnh nguồn trong `01_sources/` (luật bất biến §3). Lượt audit sau đừng đề xuất chuyển ngược lại.

Cấu trúc: frontmatter tối thiểu + một bảng bản đồ chunk dạng checkbox.

```markdown
---
source: <source id>
file: <đường dẫn file nguồn, tính từ gốc dự án>
total_lines: <số dòng>
last_updated: YYYY-MM-DD
---

| Xong | Chunk | Dòng | Mục trong nguồn | Ghi chú |
|---|---|---|---|---|
| `[x]` | Ch.2 · cụm A — đại lượng hạch toán | d.607–934 | The System of National Accounts → Problems of GDP Measurement | 14 trang + 6 stub |
| `[~]` | Ch.3 — Fiscal Accounting | d.1954–3425 | ... | còn phần Tax Effort Analysis trở đi |
| `[ ]` | Ch.4 — Balance of Payments | d.3426–4529 | ... | |
```

| Ký hiệu | Nghĩa |
|---|---|
| `[x]` | đã ingest xong |
| `[~]` | đang ingest dở — cột *Ghi chú* **phải** nêu rõ phần nào còn lại |
| `[ ]` | chưa ingest |

Đơn vị chunk: **chương** với nguồn có chương; **cụm chủ đề** khi một chương tự nó vượt ngưỡng nguồn dài. Mỗi chunk ghi dải dòng `d.<từ>–<đến>` theo file khai ở `file:`. Chunk cố ý bỏ qua (mục lục, lời tựa, bài tập, phụ lục số liệu thô — §2) vẫn có dòng riêng, đánh `[x]` và ghi "bỏ qua, không tạo trang".

**Nguồn nhiều file** (một cuốn sách tách thành nhiều file, vd `fixed_income_during` có 42 file theo chương): một source id, một mục bản kê liệt kê mọi file, một state file. `file:` khai mẫu tên file; mỗi dòng chunk ghi file ở cột *Mục trong nguồn* (vd `File -5.md: Chapter 4`); dải dòng tính trong file đó. Chú thích §7.5 thêm hậu tố file.

Dòng ghi chú về nguồn (ghi chú người dùng, đặc điểm bản chuyển đổi) được phép đặt giữa frontmatter và bảng; lịch sử xử lý không đặt ở đây.

## 11. Vùng capture tạm (`_inbox.md`)

`_inbox.md` ở gốc dự án ghi ý tưởng/insight chưa đủ chín thành trang evergreen: câu hỏi chợt nảy ra khi đọc nguồn, nghi ngờ về một trang đã có, liên kết chưa chắc, chủ đề muốn ingest sau, vấn đề cấu trúc do review phát hiện. `status: stub` không thay được vùng này: stub giữ chỗ cho khái niệm *đã biết tên*.

- Định dạng phẳng, mỗi ý 1 gạch đầu dòng kèm ngày: `- [YYYY-MM-DD] <ý tưởng>`. Không frontmatter, không luật trang wiki.
- `_inbox.md` nằm **ngoài mạng liên kết**: không `[[wikilink]]` nào trỏ vào, không xuất hiện trong `index.md`.
- **Triage mỗi lượt lint.** Mỗi mục có đúng 3 kết cục: nâng thành trang wiki, gộp vào trang đã có, hoặc xoá.
- Mục tồn quá 3 lượt lint là nợ kỹ thuật — lint báo cáo (tiêu chí *Nợ inbox*, đếm bằng `validate_wiki_page.py --inbox-debt`).

## 12. Định dạng `log.md`

`log.md` là nhật ký append-only, mỗi operation đúng **1 mục**:

```markdown
## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề ngắn>
- tối đa 3 dòng gạch đầu dòng: kết quả, số trang, phần còn lại
```

- **Dấu thời gian:** giờ Việt Nam (UTC+7), 24 giờ. Lấy bằng `python .claude/hooks/validate_wiki_page.py --now` — không ước lượng, không dùng giờ UTC của máy. Mục ghi trước 2026-09-15 để `00-00-00` = *không rõ giờ*.
- **`<op>` chỉ nhận 8 giá trị:** `ingest` · `query` · `lint` · `promote` · `review` (skill `/review-node`) · `research` (skill `/research`) · `schema` (sửa schema/skill/hook/tài liệu vận hành) · `repo` (git: publish, rollback, tag).
- **Tiền tố `## [` là giao diện máy đọc** — `grep "^## \[" log.md | tail -5` lấy 5 mục gần nhất. Không viết `## [` ở đầu dòng cho mục đích khác.
- **Log không chứa lập luận.** Lý do → `decisions.md`. Ý tưởng dang dở → `_inbox.md`. Trạng thái "còn lại phần nào" → `03_state/`.
- Mục mới luôn thêm ở **cuối file**; không sửa mục cũ. Mục cũ sai thì mục kế tiếp cùng loại ghi đính chính.
- Bản log dài trước khi rút gọn (2026-09-15): `git show e2adb7a:log.md`.
