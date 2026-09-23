---
name: research
description: 'Đào sâu một cụm trang wiki đã có trong 02_wiki theo chủ đề/tag: tổng hợp mâu thuẫn khung hiểu và khoảng trống liên kết giữa nhiều trang, bổ sung claim mới từ đúng đoạn nguồn đã ingest xong (chunk `[x]`) mà các trang đó còn thiếu, và đánh giá độ đầy đủ/độ sâu tri thức của cả cụm. Dùng khi người dùng muốn research, đào sâu, nghiên cứu kỹ hơn, tổng hợp lại toàn bộ mảng X, bổ sung claim còn thiếu cho các trang về Y, đánh giá wiki đã đủ sâu về Z chưa, so sánh các trang trong chủ đề W có nhất quán không, hoặc chỉ định rõ một nhóm trang cần rà lại cùng nhau. Không dùng cho: trả lời 1 câu hỏi tức thời không cần ghi gì mới (query); nạp nguồn mới hoặc phần nguồn còn `[~]`/`[ ]` trong chunk map (ingest); xác minh hoặc sửa claim SAI so với nguồn trên 1 trang cụ thể (review-node — research chỉ thêm claim mới, không sửa claim cũ); kiểm sức khoẻ/cấu trúc toàn wiki như link chết, trang mồ côi, OCR (lint); nâng draft lên stable (promote).'
---

# Research — đào sâu một cụm trang wiki theo chủ đề

Đọc `00_schema.md` §1, §2, §4, §5–§9, §10, §12 trước khi bắt đầu. Op ghi vào `log.md` là `research`.

Research **không phải** ingest (không đọc nguồn ngoài phần đã `[x]`), **không phải** review-node (không sửa claim sai, chỉ thêm claim mới), **không phải** query (không trả lời 1 câu hỏi tức thời, mà chủ động đào sâu cả cụm), **không phải** lint (không quét cấu trúc toàn wiki, chỉ đánh giá nội dung trong phạm vi cluster đã duyệt).

## Quy trình

### Bước 0 — Xác định cluster, xin duyệt trước khi đào sâu

- **Chủ đề/tag do người dùng nêu:** gom trang qua `grep -l -i -E "^tags:.*<từ khoá>"` + tên file, rồi mở rộng **đúng 1 vòng** qua `[[wikilink]]` outlink + `--backlinks` của các trang vừa gom (giới hạn giống `/query`, không đệ quy vòng 2).
- **Người dùng chỉ định thẳng danh sách trang:** dùng đúng danh sách đó, bỏ qua bước gom tự động.
- **Cluster > 10 trang:** giữ 10 trang liên quan nhất (backlink cao nhất + cùng tag trực tiếp), báo rõ đã cắt và đề xuất chia lượt theo sub-chủ đề.
- **Trình bày danh sách cluster kèm lý do đưa vào, chờ người dùng xác nhận/bớt/thêm** trước khi mở full content (như bước 0 của `ingest`).

### Bước 1 — Lượt đắt: mở full content toàn bộ trang trong cluster đã duyệt

Chạy cả 3 chức năng dưới đây theo thứ tự, trừ khi người dùng chỉ định rõ chỉ muốn 1–2 cái:

#### A. Tổng hợp/đối chiếu nội bộ (không cần nguồn mới)

Tìm giữa các trang trong cluster:
- Khoảng trống nội dung (chủ đề X được nhắc nhưng chưa có trang riêng cho khía cạnh Y)
- **Mâu thuẫn khung hiểu** (hai trang diễn giải lệch nhau — khác `⚠️ Conflict`, vốn là nguồn tự mâu thuẫn per luật cứng 2)
- Liên kết còn thiếu giữa các trang cùng cluster
- Khái niệm lặp lại ở ≥ 2 trang chưa có bridge note riêng

Phát hiện đáng giá trị tái sử dụng lâu dài → **hỏi người dùng xác nhận** trước khi tạo trang `type: analysis` (luật cứng 4), dedup trước bằng `grep -l "^type: analysis" 02_wiki/*.md` như `query` bước 5. Không có gì mới đáng lưu thì không đề nghị.

#### B. Bổ sung claim từ nguồn đã ingest (enrich) — tối đa 5 trang/lượt

Với từng trang trong cluster:

1. Map `sources:` → source id → tra `03_state/_sources_manifest.md` xem là nguồn ngắn hay dài.
2. **Nguồn ngắn** (không có state file): coi như đã đọc trọn ở lượt ingest, được phép enrich luôn.
3. **Nguồn dài:** tìm chunk trong `03_state/<source id>.md` có dải dòng phủ đúng chủ đề của trang.
   - Chunk `[x]` → đọc lại **trọn đoạn nguồn** (không chỉ đoạn đã trích ở chú thích §7.5 cũ) để tìm claim liên quan mà trang **chưa có**.
   - Chunk `[~]` hoặc `[ ]` → **dừng enrich cho trang này**, ghi rõ trong báo cáo, đề xuất người dùng chạy `/ingest` phần đó trước. Không tự đọc thêm (luật phạm vi).

4. **Không viết ngay.** Liệt kê claim đề xuất cho **cả lô** (tối đa 5 trang) trong báo cáo: trang · claim rút gọn · chú thích vị trí `(<source id>, <chương>, <mục>, d.<từ>–<đến>)`. Chờ người dùng duyệt cả danh sách (mô hình `promote`: duyệt theo lô, không phải "tự sửa rồi log" như `review-node`).

5. Người dùng duyệt → áp skill `writing-style` (bản local, profile wiki), viết đúng các claim đã duyệt vào đúng trang, theo §7 (không heading, viết lại bằng lời mình, chú thích §7.5), nâng `last_updated`; trang `stable`/`stale` được merge → về `draft` (§9). 
   - Claim cũ sai phát hiện giữa chừng → ghi `_inbox.md`, đề xuất `/review-node`, không tự sửa.
   - **Không đụng `reviewed`/`reviewed_by`** — quyền đó chỉ thuộc `/review-node`.

#### C. Đánh giá gap tri thức theo cluster (report-only)

Đánh giá độ đầy đủ (thiếu góc nào so với logic chủ đề), độ sâu (trang chỉ có 1 claim mỏng hay đủ sâu), độ liên kết nội cluster (outlink/backlink thưa).

**Không sửa trang nào ở phần này**, kể cả khi chức năng A/B đã chạy trong cùng lượt.

### Bước 2 — Xuất báo cáo

Vào `Claude outputs/research-<YYYY-MM-DD>-<topic>.md`:
- Danh sách cluster đã duyệt (tên trang, backlink count, tag trực tiếp)
- Kết quả A: tổng hợp/analysis đề xuất (nếu có)
- Danh sách claim B: đã duyệt/đã ghi cho từng trang, hoặc trang bị dừng enrich với lý do
- Đánh giá gap C: các điểm yếu về độ đầy đủ/sâu/liên kết

### Bước 3 — Kiểm lại quy trình

Chạy `python .claude/hooks/validate_wiki_page.py --all`, phải sạch nếu có ghi trang ở bước B.

### Bước 4 — Ghi log

1 mục vào **cuối** `log.md` (§12): `## [<giờ từ --now>] research | <chủ đề>`, tối đa 3 dòng:
- Dòng 1: quy mô cluster (N trang, M vòng mở rộng)
- Dòng 2: kết quả A/B/C (vd "2 claim mới ở 2 trang, 1 analysis đề xuất, báo cáo gap")
- Dòng 3: đường dẫn report

Giờ lấy bằng `python .claude/hooks/validate_wiki_page.py --now`.

## Sai lầm thường gặp

- **Đào sâu phần nguồn còn `[~]`/`[ ]`:** đó là việc của `/ingest`; research chỉ dùng lại chunk đã `[x]`, không tự mở rộng tiến độ ingest.
- **Sửa claim SAI khi đang enrich:** đó là `/review-node`; research chỉ THÊM claim mới, không sửa claim cũ. Phát hiện claim sai trong lúc đọc → ghi `_inbox.md`, đề xuất `/review-node`, không tự sửa.
- **Dùng cho câu hỏi tức thời đơn lẻ:** đó là `/query`, không phải `/research`. Research chỉ kích hoạt khi có chủ đề/cụm trang cần đào sâu.
- **Quét lỗi cấu trúc toàn wiki (link chết, trang mồ côi, OCR):** đó là `/lint`; research chỉ đánh giá độ đầy đủ nội dung trong phạm vi cluster đã duyệt.
- **Tự viết claim rồi mới báo cáo:** sai mô hình; phải liệt kê đề xuất theo lô, chờ duyệt, RỒI mới viết (mô hình `promote`).
- **Mở rộng cluster vượt cap (> 10 trang đọc, > 5 trang enrich) mà không báo:** phá vỡ nguyên tắc "xác nhận cluster trước khi đào sâu".
- **Nhầm "mâu thuẫn khung hiểu liên trang" (chức năng A) với `⚠️ Conflict`:** không dùng nhầm ký hiệu `⚠️ Conflict` cho loại A; ghi thành gap/khuyến nghị trong báo cáo.
- **Tạo trang `analysis` mà không dedup:** có thể trùng với trang analysis từ `/query`.
- **Enrich chỉ đọc đúng đoạn đã trích cũ ở chú thích §7.5:** phải đọc trọn chunk để tìm đúng loại claim cần bổ sung.
- **Đặt `reviewed` hoặc ghi đè `reviewed_by`:** quyền đó chỉ thuộc `/review-node`.
