---
name: ingest
description: Nạp nguồn từ 01_sources vào wiki 02_wiki theo schema dự án — **PHẢI dùng skill này cho mọi lượt cập nhật wiki từ tài liệu nguồn.** Trigger khi người dùng: nạp, thêm chương/sách, đọc tài liệu vào wiki, trích khái niệm, tạo trang, xử lý cụm tiếp theo, ingest lại các mục chưa phủ mà `--coverage` báo — hoặc chỉ nêu tên tác giả (Bindseil, Choudhry, During, Friedman, IMF, Tata ALM) mà không nói "ingest". Không bỏ skill này dù người dùng không nói rõ ràng.
---

# Ingest — nạp nguồn vào wiki

**Đọc `00_schema.md`:** toàn bộ §1–§12, trước khi tạo trang đầu tiên.
**Dừng chờ duyệt:** bước 2, sau khi trình ý chính, bảng merge và các mục bỏ qua; không ghi gì trước khi người dùng đồng ý.
**Ghi log:** luôn, op `ingest`.

Công cụ: `python .claude/hooks/validate_wiki_page.py` (gọi tắt `$H`). Hook tự chạy sau mỗi Write/Edit trong `02_wiki/`.

## Quy trình

**1. Chọn phần sẽ đọc.** Tra bảng Source id trong `03_state/_sources_manifest.md` để lấy source id, đường dẫn file và phân loại.

- **Nguồn chưa có trong bản kê** → đăng ký ngay (§10): chọn source id snake_case; đo `wc -c -l` và `sha256sum` cho từng file `.md`/`.pdf`; ghi nhan đề, tác giả, nơi và năm xuất bản; thêm dòng vào bảng Source id và mục riêng. Thiếu bước này thì hook không biết nguồn là nguồn dài và không ép chú thích §7 luật 5.
- **Nguồn ngắn** (≤ 120 KB *và* ≤ 1.200 dòng, tính trên tổng các file): đọc trọn 1 lượt, không cần state file.
- **Nguồn dài**: chạy `$H --coverage <source id>`, chọn chunk `chua` hoặc `do` kế tiếp, chỉ đọc đúng dải dòng của chunk đó. Chưa có `03_state/<source id>.md` → tạo trước: quét heading (`grep -n "^#"`), dựng bản đồ chunk đầy đủ, kể cả chunk sẽ bỏ qua; nguồn nhiều file thì mỗi file một dòng (§10).

Đọc theo thứ tự nguồn để giữ ngữ cảnh. Bỏ qua bài tập cuối chương và bảng số liệu thô (§2). Không đọc `log.md` để suy ra còn lại phần nào.

**2. Bàn với người dùng — dừng lại, không ghi gì trước khi được duyệt.** Trình ba thứ:

- **5–10 ý chính** của phần vừa đọc.
- **Bảng merge**: mỗi khái niệm một dòng `khái niệm · merge vào <trang có sẵn> | tạo mới · lý do`. Trước khi đề xuất tạo mới, tìm trang có sẵn bằng cả ba cách:

  ```bash
  ls 02_wiki | grep -i "<từ khoá>"
  grep -l -i -E "^title:.*<từ khoá>" 02_wiki/*.md
  grep -i "<từ khoá tiếng Anh hoặc tiếng Việt>" 02_wiki/index.md
  ```

  Dùng vài biến thể cho mỗi khái niệm (`reserve`, `reserves`, `required-reserve`, "dự trữ bắt buộc"). Trang trúng thì mở thân bài để quyết định. Nguồn thứ hai nói về cùng khái niệm thì mặc định là merge; tạo trang mới phải có lý do theo §5.
- **Danh sách mục của chunk**, mỗi mục một hướng: viết trang, merge, hoặc đề xuất `bỏ qua:` kèm lý do. Lấy mục bằng `grep -n "^#"` trong dải dòng; chunk `do` thì lấy mục chưa phủ từ `--coverage`.

Chờ người dùng xác nhận, bớt hoặc bổ sung. Lượt chạy không có người thì ghi các ý chính vào `_inbox.md` và dừng.

**3. Viết trang và liên kết.** Trước khi viết thân bài, gọi skill `writing-style` (profile wiki). Tối đa 15 trang mỗi lượt, stub không tính (§4); chunk chưa hết thì lượt sau làm tiếp.

- **Merge vào trang có sẵn**: thêm claim, thêm source id vào `sources:`, nâng `last_updated`. Claim mới mâu thuẫn với claim cũ → không sửa, đánh `⚠️ Conflict` kèm cả hai claim và nguồn (quy tắc bắt buộc 2), kể cả khi hai chương của cùng một nguồn cho số khác nhau.
- **Tạo trang mới**: ranh giới theo §5, title theo §8, thân bài theo §7. Trang dự tính vượt 1.000/250 từ thì tách trước khi viết (`$H --size <trang>`).
- **Chú thích** (nguồn dài): mỗi claim kèm `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim. Nguồn nhiều file ghi `file <tên file>` trong mọi chú thích, không viết "cùng file", mỗi ngoặc một nguồn; `--coverage` đọc đúng dạng này.
- **Liên kết, làm ngay không hoãn**: với mỗi trang, tìm 1–3 trang liên quan bằng câu hỏi "trang này sẽ cần xuất hiện lại trong ngữ cảnh nào?" (§6). Chèn `[[wikilink]]` trong câu kèm lý do, và cập nhật ngược trang kia để có backlink. Khái niệm chưa có trang → tạo `status: stub` rồi link. Chỉ chèn link vào câu có sẵn thì không nâng `last_updated` của trang đó. Không tìm được trang liên quan → ghi `_inbox.md`.
- **Phép thử tự đủ nghĩa** (§7 luật 6): đọc riêng trang cùng các link của nó, không mở nguồn, vẫn hiểu ý chính và lý do nối với trang khác.

**4. Kiểm và sổ sách.**

```bash
$H --coverage <source id>   # nguồn dài
$H --all
```

- Mỗi mục `--coverage` báo chưa phủ trong chunk vừa làm phải được viết vào trang, hoặc ghi `bỏ qua: <heading> — <lý do>` ở cột *Ghi chú* của state file. Chỉ ghi `bỏ qua:` cho mục người dùng đã duyệt ở bước 2. Còn mục thì chunk ở trạng thái `do`; không cần đánh dấu gì thêm.
- Thêm trang mới vào mục lục chủ đề của `02_wiki/index.md`, mỗi trang một dòng tóm tắt.
- `--all` phải sạch: trang mồ côi thì thêm liên kết có lý do thật từ trang liên quan, không vá cho đủ chỉ tiêu.

**5. Ghi 1 mục vào cuối `log.md`** (§12): `## [<giờ>] ingest | <source id> <chương/cụm>`, tối đa 3 dòng: trang tạo và trang merge, stub mới, phần còn lại của chunk. Giờ lấy bằng `$H --now`.

## Sai lầm thường gặp

- Tạo trang mới cho khái niệm đã có trang dưới tên khác → wiki phình mà không hợp nhất. Bảng merge ở bước 2 là chỗ chặn.
- Gộp cả cụm chủ đề vào 1 trang dài → vi phạm Atomic. Cần heading để tách ý nghĩa là phải tách trang.
- Sao chép nguyên văn nguồn → công thức giữ ký hiệu được, phần diễn giải phải viết lại.
- Dồn link thành mục "xem thêm" cuối trang.
- Bỏ qua bước 2 vì "nguồn đơn giản".
- Tự ghi `bỏ qua:` cho mục người dùng chưa duyệt → cổng coverage mất tác dụng.
- Chép chú thích vị trí từ trang khác mà không kiểm lại dải dòng.
- Ghi bất cứ file nào vào `01_sources/`, hoặc mở file nguồn bằng công cụ tự đổi ký tự xuống dòng. Chỉ đọc nguồn bằng `sed -n`, `grep`, Read.

## Xử lý lỗi

Lỗi không sửa được trước khi ghi log (link hỏng, chú thích sai dạng, liên kết dở dang): dừng, không commit, không ghi log, báo người dùng danh sách file đã ghi. Không tự `git checkout` hay xoá file để làm lại: lệnh đó huỷ cả thay đổi chưa commit của lượt khác.
