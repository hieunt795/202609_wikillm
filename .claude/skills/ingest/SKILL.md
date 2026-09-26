---
name: ingest
description: Nạp nguồn từ 01_sources vào wiki 02_wiki theo schema dự án — **PHẢI dùng skill này cho mọi lượt cập nhật wiki từ tài liệu nguồn.** Trigger khi người dùng: nạp, thêm chương/sách, đọc tài liệu vào wiki, trích khái niệm, tạo trang, xử lý cụm tiếp theo, cập nhật trạng thái ingest, ingest lại các mục chưa phủ / chunk `[~]` mà `--coverage` báo — hoặc chỉ nêu tên tác giả (Bindseil, Choudhry, During, Friedman, IMF, Tata ALM) mà không nói "ingest". Không bỏ skill này dù người dùng không nói rõ ràng.
---

# Ingest — nạp nguồn vào wiki

Đọc toàn bộ `00_schema.md` trước khi tạo trang đầu tiên: ingest dùng gần như mọi mục (§1 frontmatter, §2 taxonomy, §3 đặt tên, §4 ngưỡng, §5 atomic, §6 liên kết, §7 thân bài, §8 title, §9 status, §10 nguồn, §11 inbox, §12 log).

## Tham chiếu (Bundled resources)

**Tài liệu bắt buộc đọc:**
- `../../00_schema.md` — Schema wiki (§1–§12), định nghĩa mọi mục
- `.claude/rules/source-management.md` — Quy tắc quản lý nguồn
- `.claude/rules/wiki-pages.md` — Quy tắc trang wiki

**Công cụ:**
- `.claude/hooks/validate_wiki_page.py` — Validator hook, chạy tự động sau Write/Edit hoặc bằng `--all`; `--coverage` cho bước 2 và 7

**Skill phụ:**
- `/writing-style` — Bộ quy tắc viết (gọi ở bước 4 trước khi viết thân bài)

## Quy trình

**1. Xác định nguồn và phần sẽ đọc.** Tra bảng Source id trong `03_state/_sources_manifest.md` để lấy source id, đường dẫn file và phân loại.

- **Nguồn chưa có trong bản kê** → thêm ngay trong lượt này (§10): chọn source id snake_case; đo `wc -c -l` và `sha256sum` cho từng file `.md`/`.pdf`; ghi nhan đề, tác giả, nơi và năm xuất bản (đọc trang bìa/copyright của file); thêm dòng vào bảng Source id và mục riêng; thêm dòng vào `02_wiki/index.md` §Sources. Không bỏ bước này — thiếu nó thì hook không biết nguồn là nguồn dài và không ép chú thích §7.5.
- **Nguồn ngắn** (≤ 120 KB *và* ≤ 1.200 dòng, tính trên tổng các file): đọc trọn 1 lượt. Không có state file nên không qua cổng `--coverage`; đọc trọn là cách bảo đảm độ phủ.
- **Nguồn dài**: ingest theo chương/cụm. `03_state/<source id>.md` là **nguồn sự thật duy nhất** cho câu hỏi "còn lại phần nào": chọn dòng `[ ]` hoặc `[~]` kế tiếp, lấy dải dòng `d.<từ>–<đến>` rồi chỉ đọc đúng dải đó.
  - Chưa có file trạng thái → **tạo trước khi ingest**: quét heading của file nguồn (`grep -n "^#"`), dựng bản đồ chunk đầy đủ (kể cả chunk sẽ bỏ qua), rồi mới bắt đầu. Nguồn nhiều file: mỗi file một dòng, ghi tên file ở cột *Mục trong nguồn* (§10). **Không** ghi file nào vào `01_sources/` (luật cứng 1).
  - **Không** đọc `log.md` để suy ra còn lại phần nào (§10).

Đọc theo chương/thứ tự nguồn để giữ ngữ cảnh — ngữ cảnh quyết định phân loại đúng entity/concept/case. Bỏ qua bài tập cuối chương, bảng số liệu thô (§2).

**2. Bàn ý chính với người dùng — dừng lại, không ghi gì trước khi được duyệt.** Lý do: gist Karpathy đặt bước "đọc và bàn ý chính" trước khi ghi, và Evergreen chỉ tạo ra *better thinking* khi người viết thật sự tham gia — trang agent tự viết mà người chưa từng xem thì chỉ là ghi chép. Trình:

- **5–10 ý chính** của phần nguồn đã đọc, kèm danh sách trang dự kiến tạo/cập nhật (và trang `stable` sẽ về `draft`).
- **Danh sách mục của chunk**, mỗi mục một hướng: viết trang / merge / đề xuất `bỏ qua:` + lý do. Chunk `[ ]`: lấy mục bằng `grep -n "^#"` trong dải dòng. Chunk `[~]`: lấy mục chưa phủ và % phủ bằng `--coverage <source id>`. Ý chính để bàn, **không** khoanh phạm vi — phạm vi là mọi mục, kiểm ở bước 7. Nguồn nào cũng có mục không đáng ingest (trang bìa, danh sách thành viên, bảng số); duyệt chúng ở đây để bước 7 không phải thêm một vòng.

Chờ người dùng xác nhận, bỏ bớt hoặc bổ sung. Lượt chạy không có người (lịch định kỳ) thì ghi 5–10 ý vào `_inbox.md` và dừng, không tự ingest.

**3. Phân nhóm theo chủ đề.** Cụm hoá kết quả của bước 1 — **không đọc lại nguồn**. Một chủ đề thường chứa **nhiều** trang atomic. Đối chiếu mỗi cụm với **toàn bộ** `02_wiki/` để tránh trùng trang đã có, bằng tên file và frontmatter, không mở thân bài:

```bash
ls 02_wiki | grep -i "<từ khoá>"
grep -l -i -E "^(title|tags):.*<từ khoá>" 02_wiki/*.md
```

Dùng vài từ khoá tiếng Anh cho mỗi khái niệm (thuật ngữ gốc và biến thể: `reserve`, `reserves`, `required-reserve`). Chỉ mở thân bài các trang trúng để quyết định merge hay tạo mới.

**4. Với mỗi entity/concept/case trong cụm:**

- **Đã có trang** → merge thông tin mới, thêm source id vào `sources:`, nâng `last_updated`. Trang `stable`/`stale` được merge → về `draft` (§9). Mâu thuẫn với nội dung cũ → **không tự sửa**, đánh dấu `⚠️ Conflict` kèm cả hai claim + nguồn (luật cứng 2) — kể cả khi hai chương của cùng một nguồn cho số khác nhau.
- **Trang `stable` liên quan tới nguồn này nhưng lượt ingest không merge vào** → đổi sang `stale` (§9). Ngoại lệ: lượt ingest lại ở chế độ đối chiếu đã đọc lại trang và thấy đúng thì giữ `stable` (decisions.md 2026-09-25).
- **Chưa có** → tạo trang mới. Ranh giới trang theo §5, title theo §8, thân bài theo §7.

Viết thân bài bằng lời của mình. Trước khi viết hoặc sửa thân bài trang mới/cập nhật, **gọi Skill tool với `writing-style`** (bản local tại `.claude/skills/writing-style/`, profile wiki) để nạp bộ quy tắc A–I, rồi áp quy tắc đó vào văn bản đang viết. Với **nguồn dài**: mỗi claim kèm chú thích `(<source id>, <chương>, <mục>, d.<từ>–<đến>)` ngay sau claim (§7.5). Nguồn nhiều file ghi `file <tên file>` trong **mọi** chú thích, không viết "cùng file", và mỗi ngoặc một nguồn — `--coverage` đọc chú thích theo đúng dạng này để biết dòng nào đã được trích. Dải dòng lấy từ chunk đang đọc.

**5. Liên kết — làm trước khi lưu, không hoãn.** Với mỗi trang mới/cập nhật, tìm 1–3 trang liên quan bằng câu hỏi **"trang này sẽ cần xuất hiện lại trong ngữ cảnh nào?"** (§6) — không dựa vào tag trùng.

- Chèn `[[wikilink]]` từ trang mới → trang liên quan, trong câu văn kèm lý do.
- Cập nhật ngược trang liên quan để có backlink 2 chiều (`index.md` không tính là backlink).
- Khái niệm cần link mà chưa có trang → tạo luôn trang `status: stub` rồi link. **Không hoãn sang batch sau** — liên kết bị hoãn thường mất luôn.
- Chỉ chèn link vào câu có sẵn của trang cũ (không đổi claim) → **không** nâng `last_updated` của trang đó (§7.5).
- Không tìm được trang liên quan nào → ghi vào `_inbox.md` (concept cô lập, triage ở lượt lint sau).

**6. Ngưỡng:** tối đa 15 trang mỗi lượt (§4), trang `stub` không tính. Đây là nhịp độ, không phải phạm vi: chunk chưa hết thì dừng ở `[~]`, lượt sau làm tiếp. Không có ngưỡng dưới — đừng tách trang cho đủ số.

**7. Cập nhật `03_state/<source id>.md`** (nguồn dài). Chạy `python .claude/hooks/validate_wiki_page.py --coverage <source id>` và đọc danh sách mục của chunk đang xử lý — không dựa vào exit code, vì lệnh chỉ trả lỗi cho chunk đã `[x]`. Mỗi mục chưa phủ phải được viết vào trang, hoặc ghi `bỏ qua: <heading> — <lý do>` ở cột Ghi chú **chỉ cho mục người dùng đã duyệt bỏ qua ở bước 2** — agent tự bỏ qua thì cổng này mất tác dụng. Hết mục → `[x]`; còn mục → `[~]` kèm phần còn lại. Cập nhật `last_updated`. Cổng đo ở cấp mục: claim còn thiếu bên trong một mục đã có trang trích là việc của `/research` (chức năng B).

**8. Cập nhật `02_wiki/index.md`** — **bắt buộc mỗi lượt** (luật cứng 6), sau bước 7 để khớp trạng thái vừa chốt:

- Mục `## Sources` — dòng của nguồn vừa xử lý. Ô *Phần còn lại* chỉ một câu (vd "Ch.5–12; chi tiết ở state file"); diễn biến từng lượt thuộc về `log.md`.
- Mục lục trang theo chủ đề — chỉ khi có trang mới.

**9. Kiểm trước khi ghi log — bắt buộc.**

```bash
python .claude/hooks/validate_wiki_page.py --all
```

Hook `PostToolUse` chỉ bắt tool `Write|Edit`; file ghi bằng shell đi vòng qua nó. Trang mồ côi chỉ `--all` tính được. Có trang mồ côi → thêm liên kết **có lý do thật** từ trang liên quan, không vá cho đủ chỉ tiêu.

**10. Ghi 1 mục vào cuối `log.md`** (§12): `## [<giờ>] ingest | <source id> <chương/cụm>`, tối đa 3 dòng: trang tạo/cập nhật, stub mới, phần nguồn còn lại. Giờ lấy bằng `python .claude/hooks/validate_wiki_page.py --now`.

## Sai lầm thường gặp

- Gộp cả cụm chủ đề vào 1 trang dài → vi phạm Atomic. Cần heading để tách ý = phải tách trang.
- Sao chép nguyên văn nguồn → không tạo ra hiểu biết. Công thức giữ ký hiệu được, phần diễn giải phải viết lại.
- Dồn link thành mục "xem thêm" cuối trang → link không lý do không tạo giá trị mạng.
- Đặt title danh từ cho trang `case` → `case`/`analysis` dùng câu trần thuật hoàn chỉnh (§8).
- Bỏ qua bước 2 vì "nguồn đơn giản" → người dùng mất vai trò trong vòng lặp.
- Nguồn mới mà không thêm vào bản kê → hook bỏ qua kiểm §7.5 và báo `sources:` lạ cho mọi trang của nguồn đó.
- Đọc `log.md` để suy ra "còn lại phần nào" → sai nguồn sự thật (§10).
- Đánh `[x]` khi còn mục chưa phủ chưa được duyệt bỏ qua → research không bù được, vì nó chỉ đi từ trang đã có.
- Ingest xong mà quên `## Sources` + `03_state/<source id>.md` → lượt sau phải dựng lại trạng thái từ văn xuôi `log.md`.
- Chép nguyên chú thích vị trí từ trang khác mà không kiểm lại dải dòng → chú thích sai còn tệ hơn không có.
- Ghi bất cứ file nào vào `01_sources/`, hoặc mở file nguồn bằng công cụ tự đổi ký tự xuống dòng → vi phạm luật cứng 1. Chỉ đọc nguồn bằng `sed -n`, `grep`, Read.

## Xử lý lỗi

Trang mồ côi và concept cô lập: xử lý như bước 5 và bước 9. Lỗi không sửa được trước khi ghi log (link hỏng, chú thích sai dạng, liên kết dở dang): **dừng** — không commit, không ghi log, báo người dùng danh sách file đã ghi. Không tự `git checkout`/xoá file để làm lại: lệnh đó huỷ cả thay đổi chưa commit của lượt khác; việc huỷ do người dùng quyết định.
