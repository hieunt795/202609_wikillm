---
name: query
description: 'Trả lời câu hỏi bằng cách tổng hợp từ các trang trong 02_wiki. Dùng cho mọi câu hỏi về nội dung tri thức đã nạp vào wiki — kinh tế vĩ mô, hạch toán quốc gia, cán cân thanh toán, tài khoá, tiền tệ, ngân hàng trung ương, ngân hàng, thị trường trái phiếu và thu nhập cố định, lạm phát, tỷ giá — kể cả khi người dùng không nhắc chữ "wiki"; và khi người dùng muốn tra cứu, tổng hợp, so sánh, giải thích dựa trên wiki, hỏi wiki đã có gì về một chủ đề, hoặc muốn tìm, liệt kê các trang nói về một khái niệm. Không dùng cho ingest nguồn mới, kiểm tra sức khoẻ wiki, review trang, hay đào sâu/bổ sung claim cho cả một cụm trang theo chủ đề (research).'
---

# Query — tổng hợp câu trả lời từ wiki

**Đọc `00_schema.md`:** không đọc khi chỉ trả lời (query không cần data model, đọc ở đây là tốn token vô ích). Nhánh tạo trang `analysis` (bước 5) mới đọc §1, §7, §8, §12.
**Dừng chờ duyệt:** trước khi tạo trang `analysis`.
**Ghi log:** chỉ khi tạo trang, op `query`.

## Quy trình hai lượt

**1. Định hướng qua `index.md`.** Grep mục lục theo từ khoá của câu hỏi, cả tiếng Việt lẫn thuật ngữ tiếng Anh; không đọc cả file:

```bash
grep -n -i -E "<từ khoá Việt>|<từ khoá Anh>" 02_wiki/index.md
```

Mỗi trang có một dòng tóm tắt trong `index.md`, nên đây là chỗ tìm được bằng tiếng Việt mà không phải mở thân bài.

**2. Lượt rẻ — tìm trang khả nghi bằng tên file và frontmatter.** **Không mở full content** ở bước này.

```bash
ls 02_wiki | grep -i "<từ khoá>"
grep -l -i -E "^(title|tags):.*<từ khoá>|^  - .*<từ khoá>" 02_wiki/*.md
```

Vế `^  - .*` bắt tag viết dạng YAML nhiều dòng (khoảng 1/10 số trang).

Title là tiếng Anh, thân bài tiếng Việt: câu hỏi tiếng Việt thì đổi sang thuật ngữ tiếng Anh trước khi grep (vd "dự trữ bắt buộc" → `required-reserve`).

Thuật ngữ có ≥ 2 cách dịch hợp lý không tương đương nghĩa (vd "dự trữ" → `reserve`/`reserve-money`/`foreign-exchange-reserve`), hoặc câu hỏi nhắc từ viết tắt/thực thể có thể hiểu nhiều nghĩa → hỏi người dùng làm rõ trước khi grep. Chỉ hỏi khi lựa chọn sai sẽ đổi hẳn kết quả tìm; không hỏi khi câu đã đủ rõ.

**3. Lượt đắt — mở có chọn lọc.** Chỉ đọc full content những trang đã xác định là liên quan. Đi theo `[[wikilink]]` trong thân bài để mở rộng khi cần — mạng liên kết chính là đường tra cứu.

Với mỗi trang cốt lõi (trực tiếp liên quan tới câu hỏi, không phải mọi trang mở rộng qua outlink), **luôn** gọi:

```bash
python .claude/hooks/validate_wiki_page.py --neighbors <trang>
```

Lệnh in mọi trang nối với trang đó theo cả hai chiều, mỗi trang một dòng: chiều link, loại quan hệ nhìn từ trang gốc, độ mạnh và nhóm chủ đề. Nó thay cho việc dò outlink bằng mắt cộng `--backlinks`, vì outlink một chiều bỏ sót trang trỏ ngược vào. Triage kết quả bằng tên file, loại quan hệ và nhóm như lượt rẻ; chỉ mở full content trang thực sự liên quan.

**Câu hỏi về cấu trúc thì lọc theo loại.** Thêm `--type <loại>` khi câu hỏi hỏi đúng một kiểu quan hệ:

| Câu hỏi dạng | `--type` |
|---|---|
| X gồm những gì, chia ra sao | `has_part` |
| X thuộc về cái gì | `part_of` |
| cái gì quy định, đo lường, giới hạn X | `governed_by` |
| X quy định, giới hạn cái gì | `governs` |
| cái gì tác động tới X, đầu vào của X | `driven_by` |
| X tác động tới cái gì | `drives` |
| X khác gì, đối chiếu với gì | `contrasts` |

Hai điều giữ cho bộ lọc không gây sót:

- Phần lớn link cũ chưa được gắn loại. Dòng cuối của lệnh báo có bao nhiêu link chưa có loại nằm ngoài bộ lọc; số đó khác 0 thì chạy lại không có `--type` và triage phần còn lại theo tên file. Kết quả lọc chỉ đầy đủ khi số đó bằng 0.
- Loại quan hệ là chỉ dẫn để chọn trang mở, do máy đọc từ frontmatter, không phải claim. Nội dung câu trả lời lấy từ thân bài các trang đã mở, không lấy từ nhãn loại.

**Câu hỏi toàn cảnh** ("wiki có gì về mảng X", "các mảng nối nhau thế nào"): ở bước 1 xác định nhóm chủ đề trong `index.md` (dòng in đậm). Nhóm có trang mang nhãn `*(tổng quan nhóm)*` thì mở trang đó trước và đi tiếp từ các link của nó. Nhóm chưa có thì đọc các dòng tóm tắt của nhóm trong `index.md`, chọn 2–4 trang trục, gọi `--neighbors` cho từng trang; cột nhóm trong kết quả cho biết mảng này nối sang mảng nào qua trang nào.

**Giới hạn 1 vòng:** chỉ mở rộng thêm đúng 1 vòng qua trang mới phát hiện từ `--neighbors`, không đệ quy tiếp sang vòng 2 dù trang mới mở lại có láng giềng riêng. Ngoại lệ duy nhất: câu hỏi "gồm những gì" được gọi `--neighbors <trang> --type has_part --hops 2` để lấy cả thành phần của thành phần. Sau 1 vòng vẫn thấy thiếu → nói rõ phạm vi đã tra cho người dùng, không tự mở rộng vô hạn.

**4. Tổng hợp.** Trả lời kèm trích dẫn trang wiki (`[[tên-trang]]`) và chú thích nguồn gốc đã có trên trang (source id, chương, dải dòng). Không tự dựng chú thích mà trang không có.

**5. Kết tinh — chỉ khi đáng.** Câu trả lời tạo ra tổng hợp có giá trị tái sử dụng lâu dài → **hỏi người dùng xác nhận** trước khi tạo trang `type: analysis` (quy tắc bắt buộc 4). Không có gì mới đáng lưu thì không đề nghị.

Trước khi tạo, kiểm trùng như `ingest` bước 2: `grep -l "^type: analysis" 02_wiki/*.md`, đối chiếu title các trang analysis đã có xem đã có trang nào tổng hợp đúng ý này chưa. Có → merge/cập nhật trang đó thay vì tạo trang mới. Không có → tạo mới.

Người dùng đồng ý → đọc `00_schema.md` §1, §7, §8, §12, rồi viết trang theo đủ luật trang wiki: title câu trần thuật, không heading, link kèm lý do, thân bài áp skill `writing-style` (profile wiki). Hai điều kiện hook dễ vướng: `sources:` không rỗng — ghi source id của các trang đã tổng hợp; nếu có nguồn dài thì §7 luật 5 áp dụng — chú thích lấy lại từ chính các trang đã tổng hợp, trang nguồn chưa có chú thích thì nói rõ là chưa truy được tới dòng. Thêm trang vào `index.md`, chạy `python .claude/hooks/validate_wiki_page.py --all`, rồi ghi 1 mục vào cuối `log.md`: `## [<giờ từ --now>] query | <câu hỏi rút gọn>`.

Câu trả lời không tạo trang thì **không** ghi log — log chỉ ghi operation làm thay đổi wiki.

## Khi wiki không đủ dữ liệu

Nói thẳng là wiki chưa phủ phần đó và chỉ ra nguồn/chương nào cần ingest — đừng suy đoán lấp chỗ trống rồi trình bày như thể lấy từ wiki. Kiến thức nền của model có thể bổ sung nếu người dùng cần, nhưng tách riêng và ghi rõ là không đến từ wiki.

Ghi một dòng vào `_inbox.md` để lượt lint sau nhặt lên: `- [YYYY-MM-DD] wiki thiếu: <câu hỏi rút gọn> — <nguồn/chương có thể trả lời, nếu biết>`. Đây là sổ sách, không cần hỏi và không ghi log.

Phần nào của nguồn còn chưa nạp: `python .claude/hooks/validate_wiki_page.py --coverage [<source id>]`. **Không** đọc `log.md` để suy ra — nó là nhật ký, không phải bảng trạng thái.
