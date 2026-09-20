---
name: review-node
description: 'Dùng skill này khi người dùng muốn xác minh một trang wiki trong 02_wiki có đúng với nguồn gốc trong 01_sources hay không. Kích hoạt với yêu cầu ngắn kiểu "review trang X" và cả khi không có chữ "review", chỉ cần ý định là "check lại trang này với sách/nguồn": nghi một câu hoặc số liệu trên trang sai, thiếu điều kiện, diễn giải lệch; nghi trang có câu do agent tự thêm mà nguồn không nói; nghi chú thích trích dẫn (dải dòng, file nguồn) dẫn sai chỗ; muốn đối chiếu từng claim với đúng đoạn nguồn; muốn soát, duyệt, kiểm chứng một trang hay một lô trang; muốn chọn N trang chưa review (theo backlink hoặc hàng đợi mặc định) để xử lý; muốn đánh dấu trang đã kiểm là reviewed. Không dùng cho: review code, pull request, hay tài liệu ngoài wiki; kiểm sức khoẻ và cấu trúc toàn wiki hoặc kiểm nguồn bị sửa (lint); nạp nguồn mới (ingest); sửa văn phong hay góp ý bố cục mà không đối chiếu nguồn.'
---

# Review-node — đối chiếu trang với nguồn

Đọc `00_schema.md` §7 (thân bài, chú thích §7.5), §8 (title), §9 (`reviewed` / `reviewed_by`), §10 (bản kê, bản đồ chunk, nguồn nhiều file), §12 (log) trước khi bắt đầu.

Review là **kiểm chứng nội dung khớp nguồn**. Không phải lint (lint soát cấu trúc cả wiki), không phải ingest (không thêm kiến thức mới). Op ghi vào `log.md` là `review`.

## Quy trình

**1. Chọn trang.** Người dùng chỉ định; nếu không, lấy hàng đợi mặc định: trang `status` khác `stub`, chưa có `reviewed` hoặc có `reviewed` cũ hơn `last_updated`, bỏ trang đã có `reviewed_by: user`, xếp theo số backlink giảm dần (`python .claude_draft/.claude/hooks/validate_wiki_page.py --backlinks` in sẵn bảng đếm). **Tối đa 5 trang mỗi lượt** (§4) — review cẩn thận quan trọng hơn review nhiều.

**2. Đọc trọn trang**, tách thân bài thành danh sách claim.

**3. Tìm đúng đoạn nguồn cho từng claim.** Lấy đường dẫn file từ `sources:` qua bảng Source id trong `03_state/_sources_manifest.md`.
- Trang đã có chú thích §7.5 → đọc đúng dải dòng đó (nguồn nhiều file: đúng file ghi trong chú thích).
- Nguồn dài, chưa có chú thích → lấy dải dòng của chunk trong `03_state/<source id>.md`, `grep -n` heading và từ khoá trong dải đó để thu hẹp, rồi chỉ đọc đoạn tìm được.
- Nguồn ngắn (không có state file) → `grep -n` từ khoá trên cả file nguồn, đọc đoạn quanh kết quả. File ngắn đọc trọn được nếu grep không thu hẹp nổi.
- Không tìm thấy đoạn nguồn cho một claim → claim đó **không đạt** (có thể là kiến thức agent tự thêm).

**4. Kiểm năm mục cho từng trang:**

| Mục | Đạt khi |
|---|---|
| Đúng nguồn | mỗi claim khớp nghĩa đoạn nguồn; không thêm điều nguồn không nói; không bỏ điều kiện/giới hạn làm đổi nghĩa; số liệu khớp |
| Diễn đạt lại | không chép nguyên văn (§7.4); không có token OCR |
| Liên kết | mỗi `[[link]]` có lý do đúng — trang đích thật sự nói điều câu văn gán cho nó |
| Title | mô tả đúng **toàn bộ** nội dung trang (§8, §5) |
| Nhất quán | không mâu thuẫn với trang được link về cùng một điểm |

**5. Ghi kết quả.**
- **Đạt** → thêm chú thích §7.5 cho các claim đã đối chiếu (ngay sau claim), rồi thêm `reviewed: <ngày>` và `reviewed_by: model` ngay dưới `last_updated`. Thêm chú thích không đổi claim nên **không** nâng `last_updated` (§7.5).
- **Claim sai so với nguồn** → sửa đúng claim đó theo nguồn, kèm chú thích, nâng `last_updated`; trang `stable` thì về `draft` (§9). Câu sửa áp skill `writing-style` profile wiki. Sau khi sửa và kiểm lại cả trang mới được đặt `reviewed`.
- **Hai đoạn nguồn nói khác nhau** → **không sửa**: đánh `⚠️ Conflict` kèm cả hai claim + vị trí (luật cứng 2); không đặt `reviewed`.
- **Vấn đề cấu trúc** (title sai, cần tách trang, link sai đích) → không tự tách/đổi tên; ghi `_inbox.md`; không đặt `reviewed`.
- **Trang khác mắc cùng lỗi** (chép cùng claim sai hoặc cùng dải dòng sai, phát hiện khi đối chiếu) → không sửa trang đó trong lượt này, vì nó chưa được đọc trọn; ghi `_inbox.md` một mục nêu tên trang, chú thích sai và vị trí đúng, để lượt review sau nhặt lên.
- Không bao giờ ghi đè `reviewed_by: user`.

**6. Chạy `python .claude_draft/.claude/hooks/validate_wiki_page.py --all`**, phải sạch.

**7. Ghi 1 mục vào cuối `log.md`** theo §12: `## [<giờ từ --now>] review | <số trang> trang`, tối đa 3 dòng: trang đạt · trang đã sửa (kèm claim sai ngắn gọn) · trang bị giữ lại và lý do.

## Sai lầm thường gặp

- Đối chiếu với trí nhớ thay vì đọc lại đoạn nguồn → mất toàn bộ giá trị của review. Model đã viết trang này; đọc lại chính trang mà không mở nguồn chỉ xác nhận lại điều mình đã tin.
- Đặt `reviewed` cho trang còn claim chưa tìm được nguồn → "đạt" giả.
- Viết lại cả trang cho "hay hơn" → review không phải ingest; chỉ sửa claim sai.
- Chép dải dòng từ trang khác mà không kiểm → chú thích sai còn tệ hơn không có (§7.5).
