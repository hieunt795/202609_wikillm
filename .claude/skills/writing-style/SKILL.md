---
name: writing-style
description: "Bộ quy tắc văn phong tiếng Việt cho trang wiki và báo cáo kinh tế vĩ mô — chống \"văn AI\", ép chủ thể cụ thể, số liệu có nguồn, từ vựng kỷ luật. Tổng hợp từ ba nguồn: hard-rules nội bộ (báo cáo thanh khoản toàn cầu T4/2026), unslop guide (cursor/plugins), và mẫu BIS Quarterly Review. Các skill khác trích dẫn rule qua số ổn định (ví dụ \"áp A1, C2\"). Áp dụng mỗi khi viết hoặc sửa văn bản tiếng Việt — tạo trang wiki, viết báo cáo, trả lời query, sửa claim khi review."
---

# Quy tắc văn phong

Rà và sửa văn bản tiếng Việt (trang wiki, báo cáo) để loại dấu vết AI và giữ đúng giọng phân tích kinh tế nghiêm túc: chủ thể cụ thể, số liệu gắn nguồn, không ẩu dụ cực đoan, không câu nhồi nhét.

Rule số là ID ổn định — skill khác trích dẫn qua số ("áp A1, C1, C2"). Rule bị bỏ để lại khoảng trống số, không dồn lại.

## Quy trình

1. Quét văn bản theo từng nhóm rule bên dưới (A–I).
2. Sửa: giữ nguyên nghĩa, giữ đúng giọng đã chọn cho văn bản đó (§E).
3. Tự vấn: "Câu này có đọc như AI viết không?" — sửa nốt phần còn sót.
4. Nếu đoạn có box giải thích, định nghĩa thuật ngữ, hoặc số liệu dẫn chứng: đối chiếu với mẫu tham chiếu ở cuối file trước khi chốt.
5. Nếu là trang wiki dạng phẳng (không heading trong thân bài): áp thêm ràng buộc ở cuối mục §F (profile wiki). Nếu là báo cáo/tài liệu khác: áp profile báo cáo.
6. Rule nào trỏ tới `references/` chỉ cần mở khi gặp trường hợp nghi ngờ cụ thể (ví dụ: nghi ngờ câu không có chủ thể cụ thể thì mở `references/subject-guidelines.md`), không bắt buộc đọc trước.

---

## A — Cấu trúc câu

**A1. Cấm công thức "Cơ chế X [động từ] thông qua Y, bộc lộ/kích hoạt trong [điều kiện] [số liệu], dẫn đến hệ quả là Z"** — nhồi luận điểm + điều kiện + số liệu + kết luận vào một câu, mở bằng danh ngữ trừu tượng. Thay bằng: câu mở bằng số liệu, hoặc mở bằng hành động của chủ thể cụ thể, hoặc kết luận trước — giải thích sau.

**A2. Câu đơn tối đa 60 từ.** Mỗi câu một luận điểm chính. Tách tại mệnh đề phụ có thể đứng độc lập.

**A3. Cấm dồn mệnh đề điều kiện xuống cuối câu dưới dạng "trong điều kiện/bối cảnh [số liệu]".** Đưa số liệu thành câu/dữ kiện độc lập trước; dùng liên từ nhân-quả ở đầu câu mới ("vì vậy", "do đó").

**A4. Cấm nối quá 3 mệnh đề bằng dấu phẩy trong một câu.** Tách thành câu riêng hoặc cụm danh từ.

**A5. Cấm "không chỉ X mà còn Y."** Nói thẳng luận điểm.

**A6. Không ép ý tưởng vào nhóm ba khi số lượng tự nhiên khác ba.** Dùng đúng số mục thực tế.

**A7. Cấm "từ X đến Y" khi X, Y không nằm trên một thang đo có nghĩa.** Liệt kê trực tiếp các mục.

## B — Từ vựng

**B1. Hạn ngạch động từ/cụm sáo rỗng — tối đa 3 lần/từ:** phạm vi tính = mỗi trang wiki riêng, mỗi section báo cáo riêng, khi ingest lượt lớn tính từng trang không cộng dồn. Danh sách từ cấm và từ thay thế: xem `references/hollow-verbs.md`.

**B2. Cấm tuyệt đối từ cực đoan thuộc trường nghĩa bạo lực/thảm họa trong văn phân tích kinh tế:** *chết người, bạo liệt, ký sinh (cho nền kinh tế/mô hình), tàn khốc, khốc liệt, thiêu rụi, nghiền nát, quét sạch, tàn phá (không có thảm họa thật), đào mồ chôn.* Mô tả biến động mạnh chỉ cần đúng động từ tài chính chuẩn ("lao dốc", "biến động mạnh", "đảo chiều liên tục") — không cần từ cực đoan để nhấn mạnh.

**B3. Cấm "cơ chế" làm chủ ngữ của động từ hành động** ("triệt tiêu", "phá hủy", "ép buộc", "vận hành thông qua"...). Cơ chế chỉ được mô tả. Chủ ngữ hành động phải là tổ chức, biến số kinh tế, hoặc nhóm chủ thể cụ thể.

**B4. Hạn ngạch "Cơ chế X" làm chủ ngữ mở câu — tối đa 1 lần/mục (section) cấp 2.**

**B5. Cấm tính từ định tính đứng một mình không kèm số liệu:** *khổng lồ, cực đoan, nghiêm trọng, mong manh, tột độ, cực kỳ, hoàn toàn.* Kèm số ngay sau ("lên tới X tỷ", "ở mức X%, vượt ngưỡng Y%") hoặc xóa. Ngoại lệ: hằng số định nghĩa/luật định (ví dụ hạn mức bảo hiểm tiền gửi) không bắt buộc kèm số ngay cạnh, nhưng lần đầu xuất hiện phải gắn nguồn theo C2/C3.

**B6. Ưu tiên từ thường thay từ hoa mỹ khi nghĩa như nhau.** "Vận hành" → "chạy/làm"; "triển khai" → "làm/thực hiện"; "nhằm mục đích" → "để"; "do việc/do bởi" → "vì"; "cần lưu ý rằng" → xóa; "có thể có khả năng sẽ" → "có thể".

**B7. Cấm cụm marketing thay thuật ngữ học thuật** (ví dụ "dòng tiền thông minh" thay vì "dòng vốn tổ chức"/"dòng vốn định hướng lợi suất", hoặc mô tả hành vi cụ thể).

## C — Chủ thể và tính cụ thể

**C1. Mọi câu phân tích nhân-quả phải có chủ thể hành động cụ thể** — (1) tổ chức cụ thể (NHNN, IMF, ngân hàng thương mại), (2) biến số kinh tế đóng vai trò tác nhân (lãi suất, tỷ giá, cơ sở tiền tệ), hoặc (3) nhóm chủ thể xác định (các nhà đầu tư, người sử dụng lao động). Không phải danh ngữ trừu tượng (cơ chế, quy trình, rủi ro, xu hướng) hay tác nhân mơ hồ (thị trường, người ta, họ không định danh). Phân loại, ví dụ sai→đúng: `references/subject-guidelines.md`. Không xác định được chủ thể là dấu hiệu luận điểm chưa đủ cơ sở — kiểm tra lại trước khi viết.

**C2. Mọi số liệu thị trường/kỳ báo cáo phải gắn nguồn hoặc kỳ quan sát cụ thể** — dạng "[X] theo [nguồn], tính đến [thời điểm]", hoặc nếu văn bản đã định nghĩa một "kỳ báo cáo" chung ở đầu bài thì có thể neo vào đó xuyên suốt. Áp dụng cho số liệu mới đưa vào văn bản; khi chỉ rewrite/biên tập câu chữ của một đoạn đã có sẵn mà không thêm số liệu mới, không bắt buộc tự chế nguồn cho số liệu vốn đã thiếu nguồn trong bản gốc, trừ khi người dùng yêu cầu bổ sung. Với trang wiki có sẵn quy ước chú thích vị trí nguồn riêng, rule này chỉ nhắc lại, không thêm nghĩa vụ mới.

**C3. Thuật ngữ nhóm/phạm vi và hằng số định nghĩa/luật định phải có định nghĩa neo khi dùng lần đầu** nếu không hiển nhiên (ví dụ nhóm công ty nào tính là "hyperscaler", giai đoạn nào tính là "kỳ báo cáo", hạn mức bảo hiểm tiền gửi theo luật nào). Đặt ở chú thích cuối hoặc trong ngoặc đơn ngay sau, không nhét dài dòng vào câu phân tích chính.

## D — Nhất quán thuật ngữ

**D1. Một khái niệm — một thuật ngữ chuẩn dùng nhất quán toàn văn bản.** Định nghĩa lần đầu kèm viết tắt nếu có, sau đó dùng viết tắt xuyên suốt. Không đảo giữa các biến thể đồng nghĩa trong cùng một văn bản.

**D2. Quy tắc viết hoa:** tên tổ chức quốc tế viết tắt tiếng Anh kèm chú giải lần đầu ("Quỹ Tiền tệ Quốc tế (IMF)" → sau đó "IMF"); tên chính sách/văn bản pháp luật Việt Nam viết hoa chữ đầu mỗi từ danh riêng; thuật ngữ kinh tế thông dụng không viết hoa ("lãi suất", "tín dụng", "tỷ giá").

**D3. Quy tắc tiếng Anh trong văn bản tiếng Việt:** Nếu thuật ngữ tiếng Anh có dịch tiếng Việt ngắn gọn tương đương — định nghĩa 1 lần dạng "[Dịch Việt] ([Tiếng Anh])" rồi dùng bản dịch xuyên suốt (áp D1). Ví dụ: "hợp đồng tương lai (futures)", "hợp đồng mua lại (repurchase agreement hay repo)", sau đó dùng "hợp đồng tương lai" hoặc "repo". Nếu không có dịch ngắn gọn — giữ tiếng Anh xuyên suốt (ví dụ: haircut). **Cảnh báo:** một số thuật ngữ bị dịch sai nghiêm trọng (dịch máy theo nghĩa chuyên ngành khác) — đối chiếu `references/vietnamese-translation-errors.md` trước khi tự dịch thuật ngữ mới gặp lần đầu.

## E — Giọng văn

**E1. Mỗi văn bản (hoặc mỗi trang wiki) chỉ dùng một giọng.** Ba giọng tham khảo: phân tích kỹ thuật (số liệu, luận điểm, không khuyến nghị), giải thích phổ thông, khuyến nghị/brief. Không pha giọng trong cùng một đơn vị văn bản.

**E2. Đoạn văn tối thiểu 3 câu:** câu mở nêu luận điểm (≤40 từ) → câu dẫn chứng (số liệu/ví dụ cụ thể) → câu kết (hàm ý hoặc liên kết đoạn tiếp theo).

**E3. Cấm ẩn dụ quân sự/bạo lực trừ khi trích nguyên văn nguồn dùng thuật ngữ đó** ("cú sốc đình đốn" → "suy giảm đột ngột"; "van xả áp lực" → "công cụ điều tiết"; "chực chờ bùng nổ" → "có thể gia tăng nhanh").

**E4. Cấm ẩn dụ/hoa mỹ khi có cách nói thẳng tương đương** — nhân cách hóa số liệu/hệ thống, aphorism, cụm khuôn sáo. Nói đúng nghĩa.

## F — Cấu trúc tài liệu

**Hai profile khác nhau tùy nơi áp dụng — không trộn.**

**Profile wiki (trang phẳng):** không heading trong thân bài. Nếu một trang cần đổi giọng — ví dụ từ phân tích sang giải thích phổ thông — đó là dấu hiệu phải tách trang, không phải chèn heading hay hộp.

**Profile báo cáo/tài liệu khác:**
- **F1.** Phần mở đầu/Executive Summary dẫn bằng kết luận, không mô tả quy trình ("Báo cáo phân tích..."). Câu mở trả lời: người đọc nên biết/tin gì sau khi đọc xong.
- **F2.** Đoạn giải thích phổ thông xen giữa phần phân tích kỹ thuật phải tách thành hộp riêng có tiêu đề phân biệt (kiểu "Box A: ...", có thể kèm tên người viết) — không nhúng thẳng không phân cách.
- **F3.** Glossary/bảng thuật ngữ dùng giọng định nghĩa trung lập — không nhận định, không dự báo, không câu phân tích lẫn vào định nghĩa.

## G — Hình thức & kỹ thuật (áp dụng chung cả hai profile)

**G1.** Tránh lạm dụng gạch ngang. Dùng dấu chấm hoặc dấu phẩy.
**G2.** Dấu hai chấm chỉ đứng trước danh sách/ví dụ, không dùng làm liên từ giữa câu.
**G3.** Không in đậm tràn lan mọi danh từ riêng/thuật ngữ.
**G4.** Danh sách giả heading ("**Mục:** nội dung" lặp lại nhiều dòng liên tiếp) → viết lại thành văn xuôi, trừ khi mỗi dòng thực sự thêm chi tiết mới sau dấu chấm.
**G5.** Không emoji trang trí trong tiêu đề/gạch đầu dòng.
**G6.** Dùng dấu ngoặc kép thẳng, không dùng kiểu cong.
**G7.** Cấm cụm chatbot ("Hy vọng điều này hữu ích!", "Cho mình biết nếu...").
**G8.** Cấm giọng nịnh ("Câu hỏi hay!", "Bạn hoàn toàn đúng!") — trả lời thẳng.
**G9.** Kết luận chung chung không cụ thể ("tương lai sẽ tươi sáng") → nêu sự kiện/kế hoạch cụ thể.
**G10.** Vế bị động chỉ dùng khi không xác định được hoặc không cần chủ thể; còn lại nêu đích danh chủ thể hành động (liên kết với C1/B3).

## H — Né động từ "là" và quy kết mơ hồ

**H1. Cấm né "là" bằng cụm hoa mỹ khi "là" đủ nghĩa:** "đóng vai trò là", "được xem như là một", "hoạt động với tư cách là", "giữ vị trí của" → thay bằng "là" trực tiếp khi không mất sắc thái.

**H2. Cấm quy kết nguồn mơ hồ không định danh:** "giới phân tích cho rằng", "nhiều chuyên gia nhận định", "thị trường tin rằng" khi không nêu ai/tổ chức cụ thể → nêu tên theo C2, hoặc xóa nhận định nếu không xác định được nguồn.

**H3. Cấm thổi phồng tầm quan trọng không có cơ sở định lượng:** "thời khắc bước ngoặt", "bước ngoặt lịch sử", "thay đổi cục diện hoàn toàn" khi không kèm số liệu/sự kiện chứng minh mức độ — cùng logic B5/E2 nhưng nhắm vào cụm định tính-thời điểm thay vì tính từ đơn.

## I — Cụm tic hội thoại và tự quy chiếu

Áp dụng cho nội dung skill, trang wiki, báo cáo, và câu trả lời của trợ lý. Khác bản chất với §G (hình thức trình bày): đây là cụm ngôn ngữ tự nói về quá trình viết/sửa hoặc ẩu dụ mơ hồ, không phải quy tắc trình bày kỹ thuật.

**I1. Cấm cụm tự thông báo trạng thái/tiến độ nội dung:**

| Cụm bị cấm | Vì sao bị cấm | Thay bằng |
|---|---|---|
| giờ có nội dung thật | tự thông báo trạng thái, không phải nội dung | xóa, viết thẳng nội dung |
| giờ đã đầy đủ / hoàn chỉnh | tự đánh giá tiến độ, không có tiêu chí "xong" | xóa, hoặc nêu đúng phần còn thiếu nếu có |
| về cơ bản đã xong | mơ hồ, không có tiêu chí "xong" | nêu việc cụ thể đã/chưa làm |
| đã cập nhật với dữ liệu/thông tin mới nhất | "mới nhất" không có mốc thời gian | nêu ngày/kỳ dữ liệu cụ thể |

**I2. Cấm ẩn dụ "neo" dùng mơ hồ, không kèm đối tượng cụ thể:**

| Cụm bị cấm | Vì sao bị cấm | Thay bằng |
|---|---|---|
| giữ neo | không rõ neo vào cái gì, bằng cách nào | nêu cụ thể dựa trên gì, hoặc xóa |
| neo giữ / làm điểm neo / bám neo vào thực tế | cùng ẩu dụ lặp lại không cần thiết | "dựa trên [nguồn cụ thể]" |

**I3. Cấm cụm ghép sẵn dùng thay cho câu chữ rule gốc:**

| Cụm bị cấm | Vì sao bị cấm | Thay bằng |
|---|---|---|
| số liệu neo nguồn | cụm rút gọn thay cho câu C2, dùng lặp thành tic | "số liệu gắn nguồn/kỳ quan sát cụ thể" (đúng chữ C2) |
| chủ thể neo cụ thể | cùng lỗi — rút gọn rule C1 thành cụm cố định | nêu tên chủ thể trực tiếp, không dùng từ "neo" |

**I4. Cấm filler mở/kết câu và cụm tự khen:**

| Cụm bị cấm | Vì sao bị cấm | Thay bằng |
|---|---|---|
| nhìn chung / nói chung (mở đầu câu) | filler mở câu, không thêm nghĩa | xóa, vào thẳng luận điểm |
| tóm lại (lặp nhiều lần trong một văn bản) | lặp làm mất giá trị tín hiệu kết luận | chỉ giữ 1 lần ở đoạn kết thật sự |
| đáng chú ý là / điều đáng nói là | gắn cờ mơ hồ, không giải thích vì sao đáng chú ý | nêu thẳng sự kiện, bỏ khung dẫn |
| không thể phủ nhận rằng | cường điệu tu từ, không thêm thông tin | xóa |
| cần nhấn mạnh rằng | tự ra lệnh người đọc phải chú ý | xóa, để sự kiện tự nói |
| hoàn thiện / chỉn chu / chất lượng cao (tự mô tả sản phẩm của chính mình) | tự đánh giá, không phải nhận định khách quan | xóa, để người đọc tự đánh giá |

---

## Phụ lục — Mẫu tham chiếu

Không phải luật đếm được, chỉ dùng để hiệu chuẩn khi áp F2/C2/C3, dựa trên BIS Quarterly Review (T9/2026):

- Câu mở đoạn nêu chủ thể + hành động cụ thể ngay, không mở bằng danh ngữ trừu tượng.
- Box tách giọng có tiêu đề + tên người viết ngay dưới tiêu đề (kiểu "Box A: ... — [tên tác giả]").
- Định nghĩa nhóm/thuật ngữ đẩy xuống endnote đánh số ở cuối bài, không chen vào câu phân tích chính.
- Số liệu luôn kèm đơn vị + kỳ ngay trong câu, không tách rời số khỏi ngữ cảnh thời gian.
