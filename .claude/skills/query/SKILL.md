---
name: query
description: Trả lời câu hỏi bằng cách tổng hợp từ các trang trong 02_wiki. Dùng khi người dùng hỏi về nội dung tri thức trong wiki — kinh tế vĩ mô, hạch toán quốc gia, GDP, lạm phát, thất nghiệp, case Ba Lan, SNA — hoặc yêu cầu tra cứu, tổng hợp, so sánh, giải thích dựa trên wiki. Không dùng cho ingest nguồn mới hay kiểm tra sức khoẻ wiki.
---

# Query — tổng hợp câu trả lời từ wiki

**KHÔNG đọc `00_schema.md`.** Query không cần biết data model; đọc schema ở đây là lãng phí token thuần tuý.

## Quy trình hai lượt

**1. Định hướng.** Đọc `02_wiki/index.md` — mục `## Sources` ở đầu file cho biết ngay nguồn nào đã nạp tới đâu, trước khi mất công tìm trong mục lục chủ đề.

**2. Lượt rẻ — quét frontmatter.** Grep title/tags của các trang khả nghi. **Không mở full content** ở bước này. Vài chục trang × ~1,6 KB, mở hết là lãng phí.

**3. Lượt đắt — mở có chọn lọc.** Chỉ đọc full content những trang đã xác định là liên quan ở lượt 2. Đi theo `[[wikilink]]` trong thân bài để mở rộng nếu cần — mạng liên kết chính là đường dẫn tra cứu.

**4. Tổng hợp.** Trả lời kèm trích dẫn trang wiki lẫn nguồn gốc trong `01_sources/`.

Trang viết từ 2026-09-14 mang sẵn chú thích vị trí dạng `(<nguồn>, Ch.X, <mục>, d.<từ>–<đến>)` theo §7.5. **Chuyển nguyên dải dòng đó vào câu trả lời** thay vì chỉ nêu tên nguồn — người đọc kiểm lại được ngay mà không phải mở cả chương. Trang cũ hơn chưa có chú thích; nói rõ là chưa truy được tới dòng thay vì tự đoán vị trí.

**5. Kết tinh — chỉ khi đáng.** Nếu câu trả lời tạo ra tổng hợp có giá trị tái sử dụng lâu dài → **hỏi người dùng xác nhận** trước khi tạo trang `type: analysis`. Không tự ghi nếu không có gì mới đáng lưu.

Nếu người dùng đồng ý tạo trang: trang `analysis` tuân thủ đầy đủ luật trang wiki (title dạng câu khẳng định, không heading trong thân bài, link kèm lý do), và phải append 1 dòng vào `log.md`.

Hai điều kiện của hook mà trang `analysis` dễ vướng. `sources:` không được rỗng — ghi các nguồn gốc của những trang đã tổng hợp. Và nếu trong đó có nguồn dài thì §7.5 áp dụng như mọi trang khác: mỗi claim cần chú thích vị trí, lấy lại từ chính các trang đã tổng hợp chứ không tự dựng. Ghi trang bằng shell thì hook không chạy, nên chạy `python .claude/hooks/validate_wiki_page.py --all` trước khi ghi log.

## Khi wiki không đủ dữ liệu

Nói thẳng là wiki chưa phủ phần đó và chỉ ra chương/cụm nguồn nào cần ingest — đừng suy đoán lấp chỗ trống rồi trình bày như thể lấy từ wiki.

Phần nào của nguồn còn chưa nạp: đọc mục `## Sources` trong `02_wiki/index.md`; cần chi tiết theo chương/cụm thì mở `03_state/<tên_nguồn>.md`. **Không** đọc `log.md` để suy ra — nó là nhật ký, không phải bảng trạng thái.
