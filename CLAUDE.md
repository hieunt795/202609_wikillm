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

*Cập nhật lúc: 2026-09-23:11-45-00 (Wiki đạt 522 trang, 0 lỗi, 0 mồ côi)*

### 1. Những gì đã hoàn thành trong session này
- Hoàn tất 100% **Part One: Preliminaries** của nguồn `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*, Ch.1–9):
  - Ch.1–2 (Mở đầu & Tiền tệ, tín dụng): 8 trang mới + 1 stub (`dollarization`) + cập nhật 5 trang liên quan (log 10:18:30).
  - Ch.3–6 (Ngân hàng, Bù trừ, Hối phiếu, NHTW, Mục tiêu mức giá): 6 trang mới + cập nhật 4 trang (log 11:04:53).
  - Ch.7–9 (Khung vận hành, Delphic/Odyssean Forward Guidance, QE 8 kênh, Inside/Outside money, Helicopter money, Free float distortion, VaR shock, Input/Output Legitimacy): 6 trang mới + cập nhật 6 trang (log 11:38:36).
  - Tổng cộng Part One: 20 trang concept mới, 1 stub, cập nhật 15 trang.
- Trước đó trong buổi sáng: Ingest hoàn tất 100% toàn bộ nguồn `clippings` (82 bài viết, 6 cụm, đưa wiki từ 460 lên 501 trang).
- Cập nhật đồng bộ các file quản trị:
  - `03_state/fixed_income_during.md`: Đánh dấu Ch.1–9 `[x]`, hoàn tất 100% Part One.
  - `02_wiki/index.md`: Cập nhật bảng Sources (còn Ch.10–39) và bổ sung 20 trang mới vào phân mục Thị trường thu nhập cố định.
  - `log.md`: Đã append các entry chuẩn xác.
  - Session handoff: Tạo file `.claude/session_handoffs/2026-09-23-1145-fixed-income-during-part-one-complete.md`.
- Kiểm định toàn bộ 522 trang bằng `validate_wiki_page.py --all`: **0 lỗi schema, 0 trang mồ côi**.

### 2. Trạng thái hiện tại của từng phần
- `clippings`: **Hoàn tất 100%** (82 file, 6 cụm).
- `cargill_central_bank_policy`: **Hoàn tất 100%** (17/17 chương).
- `bindseil_monetary_policy`: **Hoàn tất 100%** (18/18 chương).
- `fixed_income_during`: **Hoàn tất Part One (Ch.1–9)**; còn lại Part Two–Eight (Ch.10–39, chi tiết ở `03_state/fixed_income_during.md`).
- `imf_macro_accounting`: Hoàn thành Ch.2–6, còn Ch.1.
- Các nguồn còn lại: `Modern Money Mechanics` (nguồn ngắn 85 KB, sẵn sàng ingest trọn 1 lượt), `capitalism_and_freedom`, `choudhry_*`, `tata_bank_alm` đang ở trạng thái chưa ingest.

### 3. Các bước tiếp theo cần làm trong session sau
- Tùy chọn nguồn ingest kế tiếp:
  - **Lựa chọn 1**: Tiếp tục nguồn `fixed_income_during` sang Part Two — Cash Instruments (bắt đầu bằng Ch.10–12 hoặc Ch.13–14).
  - **Lựa chọn 2**: Ingest nguồn ngắn `Modern Money Mechanics` (85 KB / 721 dòng, quy trình tạo tiền qua bút tệ ngân hàng của Fed Chicago) trong đúng 1 lượt chạy.
  - **Lựa chọn 3**: Hoàn tất nốt Ch.1 của `imf_macro_accounting` để đưa nguồn này lên 100%.

### 4. Quyết định quan trọng đã đưa ra và lý do
- **Định dạng `sources:` trong Frontmatter bắt buộc là inline list `[source_id]`**: Hook kiểm định `validate_wiki_page.py` dùng regex đơn giản khớp theo từng dòng (`line.splitlines()`), không hỗ trợ cấu trúc YAML multi-line (`sources:\n  - id`).
- **Tuân thủ triệt để Quy tắc §7.3 về danh sách bullet**: Đầu dòng bullet (`- `, `* `) không được mở đầu trực tiếp bằng `[[wikilink]]` để tránh bị hook bắt lỗi "dồn link thành danh sách xem thêm". Wikilink bắt buộc phải được lồng tự nhiên trong ngữ cảnh văn xuôi diễn giải.
- **Tập trung hóa các khái niệm lịch sử vào phân tích thể chế chính sách**: Năm thời kỳ lịch sử trong Ch.17 được cấu trúc thành các trang atomic tập trung vào cơ chế thất bại chính sách (policy failure) và xung đột thể chế thay vì chỉ tường thuật diễn biến sự kiện thuần túy.


