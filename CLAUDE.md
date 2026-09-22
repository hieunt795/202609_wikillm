# LLM Wiki — Macroeconomics

Wiki tri thức 3 lớp theo mô hình Karpathy, kèm 1 vùng trạng thái phụ trợ:

| Lớp | Thư mục | Quyền |
|---|---|---|
| Nguồn thô | `01_sources/` | **Chỉ đọc — bất biến** |
| Wiki | `02_wiki/` | Agent sở hữu, cấu trúc phẳng |
| *(phụ trợ)* Trạng thái nguồn | `03_state/` | Agent sở hữu, máy đọc được: bản kê `_sources_manifest.md` + bản đồ chunk từng nguồn dài |
| Schema | `00_schema.md` | Người + agent đồng tiến hoá |

Điều hướng nội dung: `02_wiki/index.md` (mục `## Sources` cho trạng thái ingest từng nguồn). Nhật ký thao tác: `log.md` (§12). Lý do các quyết định: `decisions.md`. Ý tưởng dang dở: `_inbox.md` (§11). Báo cáo lint/audit: `Claude outputs/` (§3).

## Năm operation

Quy trình thực thi nằm trong skill, nạp theo nhu cầu. Skill là nguồn thực thi duy nhất; sửa quy trình thì sửa `SKILL.md` và ghi lý do vào `decisions.md`.

| Operation | Skill | Đầu vào → đầu ra | Đọc `00_schema.md` |
|---|---|---|---|
| Nạp nguồn | `/ingest` | nguồn trong `01_sources/` → 3–5 ý chính chờ duyệt → 5–15 trang + stub + `index.md` + `03_state/` | Toàn bộ |
| Hỏi đáp | `/query` | câu hỏi → câu trả lời; tuỳ chọn 1 trang `analysis` (cần xác nhận) | Không; chỉ §1, §7, §8, §12 khi tạo trang |
| Kiểm tra sức khoẻ | `/lint` | toàn bộ `02_wiki/` + `_inbox.md` → báo cáo, triage inbox, danh sách *Đủ điều kiện `stable`* | §4–§9, §11, §12 |
| Nâng `draft → stable` | `/promote` | danh sách người dùng đã duyệt → đổi `status` | §7.5, §9, §12 |
| Review đối chiếu nguồn | `/review-node` | trang chỉ định hoặc hàng đợi (≤ 5 trang) → `reviewed_by: model`, sửa claim sai | §7–§10, §12 |

Ingest, query, lint dùng mẫu **hai lượt**: lượt 1 quét frontmatter (rẻ), lượt 2 chỉ mở full content trang đã xác định là cần. Đây là cơ chế kiểm soát token chính.

## Luật cứng — không vi phạm trong mọi trường hợp

1. **Không bao giờ sửa nội dung trong `01_sources/`.** Không ngoại lệ: không sửa, không thêm file, không đổi tên, không xoá, không đổi ký tự xuống dòng. Mọi thứ agent cần ghi về một nguồn đều đi ra `03_state/` (§3, §10).
2. **Không tự sửa mâu thuẫn.** Phát hiện conflict → đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn, chờ người xử lý.
3. **Lint chỉ báo cáo, không tự sửa.**
4. **Cần người dùng xác nhận trước khi:** tạo trang `type: analysis`; ghi trang ở bước ingest (bước 0 — duyệt 3–5 ý chính); nâng `draft → stable` (Promote).
5. Mỗi operation ghi đúng 1 mục vào **cuối** `log.md`, dạng `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng (§12). Lập luận không nằm trong log.
6. **Mỗi lượt ingest cập nhật `02_wiki/index.md` §Sources và `03_state/<source id>.md`**, kể cả lượt không tạo trang mới. Nguồn mới vào bản kê ngay lượt đầu (§10).

## Nhắc nhanh về trang wiki

Chi tiết ở `00_schema.md`; những điều dễ sai nhất:

- Thân bài **không có heading** — cần heading nghĩa là phải tách trang (§5, §7).
- `[[wikilink]]` nằm **trong câu văn kèm lý do**, không dồn thành danh sách "xem thêm" (§7).
- **`tags` không phải liên kết** — chỉ là chỉ mục lọc rẻ (§6).
- **Viết lại bằng lời mình**, không sao chép nguyên văn nguồn (§7); thân bài áp skill `writing-style` profile wiki.
- `sources:` dùng **source id** của bản kê (§1, §10).
- Claim từ **nguồn dài** kèm chú thích vị trí `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7.5) — áp cho trang có `last_updated` từ 2026-09-14. Chỉ chèn link hoặc chú thích thì **không** nâng `last_updated`.

## Công cụ kiểm

`python .claude/hooks/validate_wiki_page.py <lệnh>`:

| Lệnh | Dùng khi |
|---|---|
| *(hook tự chạy)* | Mỗi lần Write/Edit file trong `02_wiki/`: frontmatter, heading, link chết, source id, chú thích §7.5 |
| `--all` | Ghi bằng shell (hook không chạy); cách duy nhất bắt trang mồ côi. **Bắt buộc** trước khi ghi log ở ingest, query (khi tạo trang), promote, review-node, và ở bước 0 của lint |
| `--verify-sources` | Bước 0 lint; bất cứ khi nào nghi `01_sources/` bị đổi |
| `--backlinks [<trang>]` | Đếm/liệt kê backlink (không grep tay) |
| `--ocr` · `--stub-debt` · `--inbox-debt` | Tiêu chí lint tương ứng |
| `--now` | Giờ Việt Nam cho `log.md` |

Cảnh báo của hook phải xử lý ngay, không để tồn đến lượt lint.

## Công cụ ghi câu hỏi theo yêu cầu

`python .claude/tools/log_questions.py` chỉ chạy khi được gọi thủ công. Mặc định, công cụ quét toàn bộ Codex session có `cwd` thuộc repo hiện tại; `--input <conversation.json|jsonl>` giới hạn vào một file cụ thể. Công cụ lấy message `role=user`, phân loại bằng rule cục bộ, bỏ bản trùng và append vào `.claude/local/question-logger/questions.jsonl`; không gọi LLM. Dùng `--dry-run` để xem record dự kiến mà không ghi file.

## Ghi chú vận hành

- Không sửa `00_schema.md` / `CLAUDE.md` / skill vụn vặt từng lần — gộp theo batch để giữ prompt cache ổn định.
- Ý tưởng chưa đủ chín → `_inbox.md`, **không** nhét vào một trang `02_wiki/` cho tiện (§11). Triage mỗi lượt lint.

## Trạng thái phiên làm việc (Session Status & Next Steps)

*Cập nhật lúc: 2026-09-22:22-20-45 (Wiki đạt 460 trang, 0 lỗi, 0 mồ côi)*

### 1. Những gì đã hoàn thành trong session này
- Ingest hoàn tất toàn bộ các chương còn lại của nguồn `cargill_central_bank_policy` (Thomas F. Cargill, 2017) từ Ch.10 đến Ch.17 (100% nguồn sách hoàn tất):
  - Ch.10 (Lịch sử chuyển đổi thể chế tài chính - tiền tệ Hoa Kỳ): 4 trang mới + 3 cập nhật liên kết.
  - Ch.11 (Khung phân tích 5 bước, bản chất công quyền NHTW, de jure vs de facto): 5 trang mới + 3 cập nhật liên kết.
  - Ch.12 (Tạo tiền cơ sở OMO, phương trình hấp thụ, tỷ lệ k, sụp đổ số nhân tiền): 5 trang mới + 3 cập nhật liên kết.
  - Ch.13 (Công cụ tín dụng chọn lọc suy tàn, forward guidance, thế lưỡng nan Poole, mục tiêu lãi suất): 4 trang mới + 4 cập nhật liên kết.
  - Ch.14 (Mô hình kinh tế vĩ mô làm bản đồ dẫn đường, giả thuyết tỷ lệ tự nhiên, khung AD/AS, phân kỳ trường phái): 4 trang mới + 3 cập nhật liên kết.
  - Ch.15 (Ổn định giá cả lạm phát thấp phương sai thấp, độ trễ chính sách, lạm phát mục tiêu, phê phán nhiệm vụ kép Fed): 4 trang mới + 3 cập nhật liên kết.
  - Ch.16 (Chiến thuật điều hành OMOs vs chiến lược vĩ mô, quy tắc Taylor và nguyên tắc Taylor, phê phán Lucas, bẫy bất nhất thời gian Kydland-Prescott, tùy nghi có kiềm chế Bernanke-Mishkin): 5 trang mới + 3 cập nhật liên kết.
  - Ch.17 (Năm thời kỳ lịch sử: Đại Suy thoái 1929 và thất bại Fed, Hiệp ước 1951 và chính sách even keel, Đại Lạm phát 1965–1981 và Reg Q, Đại Điều hòa 1982–2007 và Volcker disinflation, Đại Suy thoái 2007–2009 tiền rẻ và trợ cấp nợ nhà ở): 5 trang mới + 3 cập nhật liên kết.
- Cập nhật đồng bộ các file quản trị: `03_state/cargill_central_bank_policy.md` (đánh dấu hoàn tất 17/17 chương - 100%), `02_wiki/index.md` (chuyển sang Hoàn tất 100% và bổ sung danh mục 10 trang Ch.16 & Ch.17), `log.md`.
- Chạy quy trình kiểm tra sức khỏe wiki `/lint` trên toàn bộ 451 trang: xuất báo cáo chi tiết `Claude outputs/lint-2026-09-22-451.md`, xác định 147 trang draft đủ điều kiện thăng hạng `stable`, đề xuất tạo 9 khái niệm mới và xử lý 1 mục inbox.
- Thực hiện operation `/promote`: nâng 147 trang draft đủ điều kiện lên `stable` theo duyệt của người dùng (tổng số trang stable đạt 388).
- Triage hoàn tất `_inbox.md`: chuẩn hóa trích dẫn d.4584 trong `central-bank.md` và làm sạch inbox.
- Tạo 9 trang `status: stub` từ kết quả lint: `nominal-interest-rate`, `interbank-market`, `financial-intermediation`, `deposit-insurance`, `liquidity-risk`, `adverse-selection`, `asset-bubble`, `asymmetric-information`, `reverse-repurchase-agreement`, liên kết từ 10 trang liên quan và cập nhật `index.md`.
- Kiểm định toàn bộ 460 trang bằng `validate_wiki_page.py --all`: 0 lỗi schema/heading/link/sources, 0 trang mồ côi (388 stable, 52 draft, 20 stub).

### 2. Trạng thái hiện tại của từng phần
- `cargill_central_bank_policy`: **Hoàn tất 100%** (17/17 chương, 5.623 dòng).
- `bindseil_monetary_policy`: **Hoàn tất 100%** (18/18 chương).
- `imf_macro_accounting`: Hoàn thành Ch.2–6, còn Ch.1.
- Các nguồn còn lại: `Modern Money Mechanics` (nguồn ngắn 85 KB, sẵn sàng ingest trọn 1 lượt), `capitalism_and_freedom`, `choudhry_*`, `fixed_income_during`, `tata_bank_alm` đang ở trạng thái chưa ingest.

### 3. Các bước tiếp theo cần làm trong session sau
- Tùy chọn nguồn ingest kế tiếp:
  - **Lựa chọn 1**: Ingest nguồn ngắn `Modern Money Mechanics` (85 KB / 721 dòng, quy trình tạo tiền qua bảng cân đối ngân hàng thương mại của Fed Chicago, hoàn thành trọn 1 lượt).
  - **Lựa chọn 2**: Hoàn tất nốt Ch.1 của `imf_macro_accounting` để đưa nguồn này lên 100%.
  - **Lựa chọn 3**: Ingest nguồn dài kinh điển `capitalism_and_freedom` (Milton Friedman, 565 KB / 2.055 dòng) hoặc các nguồn chuyên sâu về định chế/ngân hàng (`choudhry_principles_of_banking`, `fixed_income_during`).

### 4. Quyết định quan trọng đã đưa ra và lý do
- **Định dạng `sources:` trong Frontmatter bắt buộc là inline list `[source_id]`**: Hook kiểm định `validate_wiki_page.py` dùng regex đơn giản khớp theo từng dòng (`line.splitlines()`), không hỗ trợ cấu trúc YAML multi-line (`sources:\n  - id`).
- **Tuân thủ triệt để Quy tắc §7.3 về danh sách bullet**: Đầu dòng bullet (`- `, `* `) không được mở đầu trực tiếp bằng `[[wikilink]]` để tránh bị hook bắt lỗi "dồn link thành danh sách xem thêm". Wikilink bắt buộc phải được lồng tự nhiên trong ngữ cảnh văn xuôi diễn giải.
- **Tập trung hóa các khái niệm lịch sử vào phân tích thể chế chính sách**: Năm thời kỳ lịch sử trong Ch.17 được cấu trúc thành các trang atomic tập trung vào cơ chế thất bại chính sách (policy failure) và xung đột thể chế thay vì chỉ tường thuật diễn biến sự kiện thuần túy.


