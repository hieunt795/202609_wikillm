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

*Cập nhật lúc: 2026-09-21:21-04-47 (Wiki đạt 404 trang, 0 lỗi, 0 mồ côi)*

### 1. Những gì đã hoàn thành trong session này
- Ingest liên tiếp 9 chương đầu của nguồn `cargill_central_bank_policy` (Thomas F. Cargill, 2017):
  - Ch.1 (Khái niệm chế độ tài chính - tiền tệ): 9 trang mới + 6 cập nhật liên kết.
  - Ch.2 (Khái niệm cơ bản về tiền tệ, lạm phát, kim tự tháp ngược): 8 trang mới + 5 cập nhật.
  - Ch.3 (Hệ thống tài chính và luồng vốn): 6 trang mới + 4 cập nhật.
  - Ch.4 (Lãi suất trong hệ thống tài chính, trần lãi suất, rủi ro kỳ hạn): 6 trang mới + 4 cập nhật.
  - Ch.5 (Mặt bằng lãi suất, quỹ cho vay, hiệu ứng Fisher, tiền tệ hóa nợ): 7 trang mới + 5 cập nhật.
  - Ch.6 (Cấu trúc lãi suất và đường cong lợi suất): 8 trang mới + 5 cập nhật.
  - Ch.7–9 (Kích thước quốc tế, Vai trò chính phủ, Quy định và giám sát hệ thống tài chính): 13 trang mới + 5 cập nhật.
- Cập nhật đồng bộ các file quản trị: `03_state/cargill_central_bank_policy.md`, `02_wiki/index.md`, `log.md`.
- Kiểm định toàn bộ 404 trang bằng `validate_wiki_page.py --all`: 0 lỗi schema/heading/link/sources, 0 trang mồ côi.

### 2. Trạng thái hiện tại của từng phần
- `cargill_central_bank_policy`: Đang ingest dở, đã hoàn thành 9/17 chương (dòng 424–3009, 2.586 dòng / 46.0% dung lượng nguồn).
- `bindseil_monetary_policy`: Đã hoàn tất 100% (18/18 chương).
- `imf_macro_accounting`: Hoàn thành Ch.2–6, còn Ch.1.
- Các nguồn còn lại: `Modern Money Mechanics`, `capitalism_and_freedom`, `choudhry_*`, `fixed_income_during`, `tata_bank_alm` đang ở trạng thái chưa ingest.

### 3. Các bước tiếp theo cần làm trong session sau
- **Lựa chọn 1**: Tiếp tục ingest các chương tiếp theo của `cargill_central_bank_policy`:
  - Ch.10: *A Short History of the U.S. Financial and Monetary Regime in Transition* (d.3010–3312, 303 dòng) — lịch sử các cuộc chuyển đổi thể chế tài chính Mỹ.
  - Ch.11: *The Five Steps and Step 1: The Institutional Design of the Central Bank* (d.3313–3570, 258 dòng) — thiết kế thể chế và tính độc lập của NHTW.
  - Ch.12: *Central Banks, Base Money and the Money Supply* (d.3571–4010, 440 dòng) — tiền cơ sở, số nhân tiền tệ và kiểm soát cung tiền.
- **Lựa chọn 2**: Chạy `/lint` rà soát toàn diện kho tri thức khi vượt mốc 400 trang để đánh giá các ứng viên đủ điều kiện thăng hạng `stable`.

### 4. Quyết định quan trọng đã đưa ra và lý do
- **Định dạng `sources:` trong Frontmatter bắt buộc là inline list `[source_id]`**: Hook kiểm định `validate_wiki_page.py` dùng regex đơn giản khớp theo từng dòng (`line.splitlines()`), không hỗ trợ cấu trúc YAML multi-line (`sources:\n  - id`). Nếu viết multi-line, trường `sources` sẽ bị coi là rỗng và báo lỗi vi phạm §1.
- **Ghép 3 chương (Ch.7, 8, 9) với ngân sách 13 trang atomic (~4–5 trang/chương)**: Tối ưu hóa dung lượng nguồn (~900 dòng) nằm trọn trong trần 5–15 trang/lượt của skill `/ingest`, bảo đảm tính cô đọng sâu sắc của từng claim mà không gây loãng đồ thị tri thức.
- **Tái sử dụng các hub và trang sẵn có từ Ch.2–3**: Thay vì tạo mới các trang trùng lặp về phân loại thặng dư/thâm hụt hay trung gian tài chính, các trang mới trỏ trực tiếp về `modern-monetary-system-functions-as-an-inverted-pyramid`, `economic-sectors-are-classified-into-surplus-deficit-and-balanced-units`, `financial-institutions-operate-as-balanced-budget-entities-in-the-flow-of-funds`, giúp tăng độ sâu mạng lưới và giữ tỷ lệ trang mồ côi bằng 0.

