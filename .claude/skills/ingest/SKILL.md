---
name: ingest
description: Nạp nguồn mới từ 01_sources vào wiki 02_wiki theo schema dự án. Dùng khi người dùng muốn ingest, nạp nguồn, thêm chương mới, đọc tài liệu vào wiki, trích xuất khái niệm từ nguồn, tạo trang wiki từ tài liệu, xử lý cụm tiếp theo, add source to wiki, hoặc bất kỳ yêu cầu nào biến nội dung trong 01_sources thành trang trong 02_wiki.
---

# Ingest — nạp nguồn vào wiki

Đọc `00_schema.md` §1 (frontmatter) + §2 (taxonomy) trước khi tạo trang đầu tiên. Với nguồn chưa từng ingest, đọc thêm §10 để phân loại nguồn ngắn / nguồn dài.

## Quy trình

**1. Đọc nguồn theo mạch gốc.** Đọc theo chương/thứ tự nguồn để giữ ngữ cảnh, không trích xuất rời rạc từng câu — ngữ cảnh là thứ quyết định phân loại đúng entity/concept/case.

Bỏ qua: bài tập cuối chương, bảng số liệu thô (§2). Số liệu cần thiết thì trích dẫn bên trong trang `case` liên quan, không tạo trang riêng.

Cũng bỏ qua phần tường thuật bối cảnh quốc gia khi wiki đã đủ minh chứng cho các concept liên quan — xem nguyên tắc *ưu tiên lý luận trước tường thuật* (§2). Với `imf_macro_accounting`, quyết định này đã được chốt cho từng chương trong bản đồ chunk ở `03_state/imf_macro_accounting.md`: đọc cột *Ghi chú* trước khi mở nguồn.

**Nguồn ngắn hay nguồn dài?** Đo bằng `wc -c -l <file>` rồi đối chiếu ngưỡng §10 — không ước lượng bằng mắt.

- **Nguồn ngắn** (≤ 120 KB *và* ≤ 1.200 dòng): đọc trọn 1 lượt. Không cần file trạng thái.
- **Nguồn dài** (vượt bất kỳ ngưỡng nào): không đọc trọn một lượt được — ingest theo chương/cụm. `03_state/<tên_nguồn>.md` là **nguồn sự thật duy nhất** cho câu hỏi "còn lại phần nào": đọc bảng chunk ở đó, chọn dòng `[ ]` hoặc `[~]` kế tiếp, lấy dải dòng `d.<từ>–<đến>` rồi chỉ đọc đúng dải đó.
  - Nguồn dài chưa có file trạng thái → **tạo `03_state/<tên_nguồn>.md` trước khi ingest**: quét heading của file nguồn, dựng bản đồ chunk đầy đủ (kể cả chunk sẽ bỏ qua), đánh dấu trạng thái hiện tại, rồi mới bắt đầu. **Không** ghi file này vào `01_sources/` — thư mục nguồn bất biến tuyệt đối (§3).
  - **Không** đọc `log.md` để suy ra còn lại phần nào. `log.md` kể chuyện đã xảy ra; state file nói hiện đang ở đâu (§10).

**2. Phân nhóm theo chủ đề.** Cụm hoá kết quả đã trích xuất ở bước 1 — **không đọc lại nguồn**. Đối chiếu mỗi cụm với **toàn bộ** `02_wiki/` hiện có (không chỉ phần đang đọc) để tránh tạo trang trùng chủ đề đã ingest từ chương trước.

Chủ đề là đơn vị gom nhóm tạm thời để tìm liên kết — một chủ đề thường chứa **nhiều** trang atomic, không phải 1 chủ đề = 1 trang.

**3. Với mỗi entity/concept/case trong cụm:** kiểm tra `02_wiki/` đã có trang chưa (grep theo title/alias).

- **Đã có** → merge thông tin mới, thêm nguồn vào `sources:`. Mâu thuẫn với nội dung cũ → §4: **không tự sửa**, đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn.
- **Chưa có** → tạo trang mới. Ranh giới trang quyết định bởi luật Atomic §5. Đặt title theo §8, viết thân bài theo §7.

Với **nguồn dài**: mỗi claim kèm chú thích vị trí `(<nguồn>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim, không dồn cuối trang (§7.5). Dải dòng lấy từ chunk đang đọc trong `03_state/<tên_nguồn>.md`. Nguồn ngắn không bắt buộc.

**4. Liên kết — làm trước khi lưu, không hoãn.** Với mỗi trang mới/cập nhật, tìm tối thiểu 1–3 trang liên quan bằng câu hỏi **"trang này sẽ cần xuất hiện lại trong ngữ cảnh nào?"** (§6) — không dựa vào tag trùng.

- Chèn `[[wikilink]]` từ trang mới → trang liên quan.
- Cập nhật ngược trang liên quan để có backlink 2 chiều.
- Khái niệm cần link mà chưa có trang → tạo luôn trang `status: stub` rồi link. **Không hoãn sang batch sau** — liên kết bị hoãn thường mất luôn.
- Không tìm được trang liên quan nào → ghi rõ vào `log.md` (concept cô lập, theo dõi ở lượt lint sau).

**5. Ngưỡng:** 5–15 trang mỗi lần (§4). Trang `stub` không tính vào ngưỡng này.

**6. Cập nhật `02_wiki/index.md`.** Hai phần, phần đầu **bắt buộc mỗi lượt**:

- Mục `## Sources` — trạng thái nguồn vừa xử lý + phần còn lại. Cập nhật kể cả lượt không tạo trang mới nào.
- Mục lục trang theo chủ đề — chỉ khi có trang mới.

**7. Cập nhật `03_state/<tên_nguồn>.md`** (nguồn dài). Đổi ô trạng thái chunk vừa xử lý sang `[x]`, hoặc `[~]` kèm ghi chú phần nào còn lại nếu dừng giữa chừng; cập nhật `last_updated`. Bảng này và mục `## Sources` ở index phải khớp nhau.

**8. Kiểm trước khi ghi log — bắt buộc, không bỏ qua kể cả khi thấy chắc chắn.**

```bash
python .claude/hooks/validate_wiki_page.py --all
```

Hook `PostToolUse` chỉ bắt tool `Write|Edit`; ingest thường ghi file bằng shell nên hook không chạy lần nào. Ngoài ra hook trên từng file **không thể** biết một trang có backlink hay không — đó là thuộc tính của cả đồ thị. Chế độ `--all` tính được và báo trang mồ côi.

Lỗi này đã xảy ra hai lần trong cùng một ngày: cụm A của Ch.3 và cụm D+E để lại tổng cộng 12 trang backlink = 0, đều là trường hợp cụm mới link ra ngoài đầy đủ nhưng không trang cũ nào link ngược vào. Bước 4 yêu cầu backlink hai chiều cho **từng trang** là chưa đủ, vì lỗi phát sinh ở **cấp cụm**.

Có trang mồ côi → thêm liên kết **có lý do thật** từ trang liên quan, không vá cho đủ chỉ tiêu. Nếu thực sự không tìm được lý do, ghi vào `log.md` như concept cô lập (bước 4) thay vì bịa một câu nối.

**9. Append 1 dòng vào `log.md`:** `[YYYY-MM-DD] ingest <nguồn> <chương/cụm> → <tóm tắt trang tạo/nâng cấp>`. Ghi rõ phần nào của nguồn còn lại chưa ingest.

## Sai lầm thường gặp

- Gộp cả cụm chủ đề vào 1 trang dài → vi phạm Atomic. Quyết định ranh giới bằng **ba phép kiểm §5** (title, nhu cầu liên kết tới từng phần, heading), theo đúng thứ tự đó. **Không dùng số từ làm căn cứ** — đo trên toàn wiki, độ dài không tương quan với bất kỳ chỉ số mạng nào.
- Sao chép nguyên văn nguồn → không tạo ra hiểu biết. Công thức giữ ký hiệu được, phần diễn giải phải viết lại.
- Dồn link thành mục "xem thêm" cuối trang → link không lý do không tạo giá trị mạng.
- Đặt title danh từ cho trang `case` → `case`/`analysis` phải dùng câu khẳng định hoàn chỉnh (§8).
- Đọc `log.md` để suy ra "còn lại phần nào" → sai nguồn sự thật. Với nguồn dài, chỉ `03_state/<tên_nguồn>.md` trả lời câu hỏi đó (§10).
- Ingest xong mà quên cập nhật `## Sources` + `03_state/<tên_nguồn>.md` → lượt sau phải đọc lại văn xuôi `log.md` để dựng lại trạng thái, đúng vấn đề mà hai bảng này sinh ra để giải quyết.
- Chép nguyên chú thích vị trí từ nguồn khác vào trang mới mà không kiểm lại dải dòng → chú thích sai còn tệ hơn không có chú thích.
- Ghi bất cứ file nào vào `01_sources/` (kể cả file trạng thái, ghi chú, bản trích) → vi phạm luật cứng 1. Mọi thứ agent ghi ra đều thuộc `02_wiki/`, `03_state/`, `_inbox.md` hoặc `log.md`.
