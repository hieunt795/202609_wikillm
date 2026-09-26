---
name: query
description: 'Trả lời câu hỏi bằng cách tổng hợp từ các trang trong 02_wiki. Dùng cho mọi câu hỏi về nội dung tri thức đã nạp vào wiki — kinh tế vĩ mô, hạch toán quốc gia, cán cân thanh toán, tài khoá, tiền tệ, ngân hàng trung ương, ngân hàng, thị trường trái phiếu và thu nhập cố định, lạm phát, tỷ giá — kể cả khi người dùng không nhắc chữ "wiki"; và khi người dùng muốn tra cứu, tổng hợp, so sánh, giải thích dựa trên wiki, hỏi wiki đã có gì về một chủ đề, hoặc muốn tìm, liệt kê các trang nói về một khái niệm. Không dùng cho ingest nguồn mới, kiểm tra sức khoẻ wiki, review trang, hay đào sâu/bổ sung claim cho cả một cụm trang theo chủ đề (research).'
---

# Query — tổng hợp câu trả lời từ wiki

**Không đọc `00_schema.md` khi chỉ trả lời.** Query không cần data model; schema dài khoảng 21 KB, đọc ở đây là tốn token vô ích. Nhánh tạo trang `analysis` (bước 5) mới đọc §1, §7, §8, §12.

## Quy trình hai lượt

**1. Định hướng.** Chỉ đọc mục `## Sources` của `02_wiki/index.md` (cho biết nguồn nào đã nạp tới đâu), không đọc cả file:

```bash
sed -n '/^## Sources/,/^## Trang/p' 02_wiki/index.md
```

Cần mục lục chủ đề thì grep trong `index.md` theo từ khoá thay vì đọc hết.

**2. Lượt rẻ — tìm trang khả nghi bằng tên file và frontmatter.** **Không mở full content** ở bước này.

```bash
ls 02_wiki | grep -i "<từ khoá>"
grep -l -i -E "^(title|tags):.*<từ khoá>|^  - .*<từ khoá>" 02_wiki/*.md
```

Vế `^  - .*` bắt tag viết dạng YAML nhiều dòng (khoảng 1/10 số trang).

Title là tiếng Anh, thân bài tiếng Việt: câu hỏi tiếng Việt thì đổi sang thuật ngữ tiếng Anh trước khi grep (vd "dự trữ bắt buộc" → `required-reserve`).

Thuật ngữ có ≥ 2 cách dịch hợp lý không tương đương nghĩa (vd "dự trữ" → `reserve`/`reserve-money`/`foreign-exchange-reserve`), hoặc câu hỏi nhắc từ viết tắt/thực thể có thể hiểu nhiều nghĩa → hỏi người dùng làm rõ trước khi grep. Chỉ hỏi khi lựa chọn sai sẽ đổi hẳn kết quả tìm; không hỏi khi câu đã đủ rõ.

**3. Lượt đắt — mở có chọn lọc.** Chỉ đọc full content những trang đã xác định là liên quan. Đi theo `[[wikilink]]` trong thân bài để mở rộng khi cần — mạng liên kết chính là đường tra cứu.

Với mỗi trang cốt lõi (trực tiếp liên quan tới câu hỏi, không phải mọi trang mở rộng qua outlink), **luôn** gọi thêm:

```bash
python .claude/hooks/validate_wiki_page.py --backlinks <trang>
```

Outlink một chiều có thể bỏ sót trang trỏ ngược vào (backlink 2 chiều chỉ được đảm bảo từ lượt ingest tạo/sửa trang — §6 — không đảm bảo mọi trang cũ). Triage kết quả bằng tên file như lượt rẻ, chỉ mở full content trang backlink thực sự liên quan.

**Giới hạn 1 vòng:** chỉ mở rộng thêm đúng 1 vòng qua trang mới phát hiện (từ outlink hoặc từ `--backlinks`) — không đệ quy tiếp sang vòng 2 dù trang mới mở lại có outlink/backlink riêng. Sau 1 vòng vẫn thấy thiếu → nói rõ phạm vi đã tra cho người dùng, không tự mở rộng vô hạn.

**4. Tổng hợp.** Trả lời kèm trích dẫn trang wiki (`[[tên-trang]]`) và chú thích nguồn gốc đã có trên trang (source id, chương, dải dòng). Không tự dựng chú thích mà trang không có.

**5. Kết tinh — chỉ khi đáng.** Câu trả lời tạo ra tổng hợp có giá trị tái sử dụng lâu dài → **hỏi người dùng xác nhận** trước khi tạo trang `type: analysis` (luật cứng 4). Không có gì mới đáng lưu thì không đề nghị.

Trước khi tạo, kiểm trùng như `ingest` bước 3: `grep -l "^type: analysis" 02_wiki/*.md`, đối chiếu title các trang analysis đã có xem đã có trang nào tổng hợp đúng ý này chưa. Có → merge/cập nhật trang đó thay vì tạo trang mới. Không có → tạo mới.

Người dùng đồng ý → đọc `00_schema.md` §1, §7, §8, §12, rồi viết trang theo đủ luật trang wiki: title câu trần thuật, không heading, link kèm lý do, thân bài áp skill `writing-style` (profile wiki). Hai điều kiện hook dễ vướng: `sources:` không rỗng — ghi source id của các trang đã tổng hợp; nếu có nguồn dài thì §7.5 áp dụng — chú thích lấy lại từ chính các trang đã tổng hợp, trang nguồn chưa có chú thích thì nói rõ là chưa truy được tới dòng. Thêm trang vào `index.md`, chạy `python .claude/hooks/validate_wiki_page.py --all`, rồi ghi 1 mục vào cuối `log.md`: `## [<giờ từ --now>] query | <câu hỏi rút gọn>`.

Câu trả lời không tạo trang thì **không** ghi log — log chỉ ghi operation làm thay đổi wiki.

## Khi wiki không đủ dữ liệu

Nói thẳng là wiki chưa phủ phần đó và chỉ ra nguồn/chương nào cần ingest — đừng suy đoán lấp chỗ trống rồi trình bày như thể lấy từ wiki. Kiến thức nền của model có thể bổ sung nếu người dùng cần, nhưng tách riêng và ghi rõ là không đến từ wiki.

Phần nào của nguồn còn chưa nạp: mục `## Sources`; cần chi tiết theo chương thì mở `03_state/<source id>.md`. **Không** đọc `log.md` để suy ra — nó là nhật ký, không phải bảng trạng thái.
