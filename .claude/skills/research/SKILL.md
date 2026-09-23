---
name: research
description: 'Đào sâu một cụm trang wiki đã có trong 02_wiki theo chủ đề/tag — chỉ trên wiki nội bộ và nguồn đã ingest trong 01_sources, không tìm kiếm web: tổng hợp mâu thuẫn khung hiểu và khoảng trống liên kết giữa nhiều trang, bổ sung claim mới từ đúng đoạn nguồn đã ingest xong (chunk `[x]`) mà các trang đó còn thiếu, và đánh giá độ đầy đủ/độ sâu tri thức của cả cụm. Dùng khi người dùng muốn research, đào sâu, nghiên cứu kỹ hơn, tổng hợp lại toàn bộ mảng X trong wiki, bổ sung claim còn thiếu cho các trang về Y, đánh giá wiki đã đủ sâu về Z chưa, so sánh các trang trong chủ đề W có nhất quán không, hoặc chỉ định rõ một nhóm trang cần rà lại cùng nhau. Không dùng cho: trả lời 1 câu hỏi tức thời không cần ghi gì mới (query); nạp nguồn mới hoặc phần nguồn còn `[~]`/`[ ]` trong chunk map (ingest); xác minh hoặc sửa claim SAI so với nguồn trên 1 trang cụ thể (review-node — research chỉ thêm claim mới, không sửa claim cũ); kiểm sức khoẻ/cấu trúc toàn wiki như link chết, trang mồ côi, OCR (lint); nâng draft lên stable (promote); nghiên cứu chủ đề trên web hoặc tài liệu ngoài wiki.'
---

# Research — đào sâu một cụm trang wiki theo chủ đề

Research **không phải** ingest (không đọc nguồn ngoài phần đã `[x]`), **không phải** review-node (không sửa claim sai, chỉ thêm claim mới), **không phải** query (không trả lời 1 câu hỏi tức thời, mà chủ động đào sâu cả cụm), **không phải** lint (không quét cấu trúc toàn wiki, chỉ đánh giá nội dung trong cluster đã duyệt). Op ghi vào `log.md` là `research`.

**Đọc `00_schema.md` theo nhánh, không đọc trước.** Bước 0–2 không cần schema: giới hạn và luật cần thiết đã ghi trong skill này. Chỉ khi người dùng đã duyệt đề xuất và sắp ghi trang (bước 3) mới đọc §7 (thân bài, chú thích §7.5), §9 (vòng đời), §10 mục *nguồn nhiều file* nếu có; thêm §1, §8 nếu tạo trang `analysis`. Schema khoảng 21 KB — đọc sớm cho một lượt có thể kết thúc ở báo cáo là tốn token vô ích.

Giới hạn (§4): **đọc trọn tối đa 10 trang, enrich tối đa 5 trang mỗi lượt.**

## Quy trình

### Bước 0 — Xác định cluster, xin duyệt trước khi mở full content

- **Người dùng chỉ định thẳng danh sách trang:** dùng đúng danh sách đó, bỏ qua bước gom.
- **Người dùng nêu chủ đề/tag:** title và tag là tiếng Anh, nên đổi thuật ngữ Việt sang Anh trước (vd "dự trữ bắt buộc" → `required-reserve`); thuật ngữ có ≥ 2 cách dịch không tương đương nghĩa thì hỏi lại như `query` bước 2. Gom trang bằng lượt rẻ:

  ```bash
  ls 02_wiki | grep -i "<từ khoá>"
  grep -l -i -E "^(title|tags):.*<từ khoá>|^  - .*<từ khoá>" 02_wiki/*.md
  ```

  Vế `^  - .*` bắt tag viết dạng YAML nhiều dòng (khoảng 1/10 số trang); thiếu nó, lượt rẻ bỏ sót phần lớn cụm.

  Mở rộng **đúng 1 vòng**, vẫn không mở full content: outlink lấy bằng `grep -o "\[\[[^]|]*" 02_wiki/<trang>.md | sort -u`, backlink bằng `python .claude/hooks/validate_wiki_page.py --backlinks <trang>`. Không đệ quy vòng 2.
- **Cluster > 10 trang:** giữ 10 trang gắn chủ đề nhất (khớp title/tag trực tiếp trước, rồi backlink cao), báo rõ đã cắt những trang nào và đề xuất chia lượt theo sub-chủ đề.

Trình bày danh sách cluster (tên trang · lý do đưa vào · backlink · `status`), **chờ người dùng xác nhận/bớt/thêm**. Người dùng cũng có thể chỉ chọn 1–2 trong 3 chức năng A/B/C; mặc định chạy cả ba.

### Bước 1 — Đọc cluster và nguồn (chưa ghi gì)

Mở full content các trang đã duyệt, rồi làm ba việc sau. Kết quả của cả ba chỉ là **đề xuất**, gom lại ở bước 2.

**A. Đối chiếu nội bộ giữa các trang** (không cần nguồn):

- Khoảng trống nội dung: khía cạnh được nhắc nhưng chưa có trang riêng.
- **Mâu thuẫn khung hiểu:** hai trang diễn giải cùng một điểm lệch nhau. Đây không phải `⚠️ Conflict` (vốn dành cho hai *nguồn* nói khác nhau) — chỉ ghi vào báo cáo.
- Liên kết còn thiếu giữa các trang cùng cluster → đề xuất câu chèn `[[link]]` kèm lý do.
- Ý lặp lại ở ≥ 2 trang chưa có bridge note hoặc trang tổng hợp → nếu đáng tái sử dụng lâu dài, đề xuất 1 trang `type: analysis`. Dedup trước: `grep -l "^type: analysis" 02_wiki/*.md`, đối chiếu title; đã có trang cùng ý thì đề xuất cập nhật trang đó. Không có gì đáng lưu thì không đề xuất.

**B. Tìm claim mới từ nguồn đã ingest (enrich)** — chọn tối đa 5 trang, ưu tiên trang mỏng (ít claim) có backlink cao và có chunk `[x]` phủ chủ đề; nói rõ lý do chọn.

1. Xác định chunk cần đọc cho mỗi trang. Nguồn hợp lệ gồm: nguồn trong `sources:` của trang, **và** nguồn mà các trang khác trong cluster đã trích dẫn tới đúng chủ đề này (chú thích §7.5 của chúng chỉ sẵn chunk — không lục toàn bộ nguồn để tìm). Tra `03_state/_sources_manifest.md` để biết nguồn ngắn hay dài và đường dẫn file.
   - **Nguồn dài:** tìm chunk trong `03_state/<source id>.md` phủ chủ đề của trang. Chỉ dùng chunk `[x]`. Chunk `[~]`/`[ ]` → **dừng enrich trang đó từ chunk này**, ghi vào báo cáo và đề xuất `/ingest` phần đó trước: state file là nguồn sự thật về tiến độ ingest, nếu research đọc trước thì wiki sẽ đi trước bản đồ chunk.
   - **Nguồn nhiều file** (vd `fixed_income_during`): cột *Mục trong nguồn* của dòng chunk ghi file (vd `File -5.md: Chapter 4`); dải dòng tính trong file đó.
   - **Nguồn ngắn** (không có state file): coi như đã ingest trọn; `grep -n` từ khoá trên file, đọc đoạn quanh kết quả.
2. **Gom trang theo chunk, mỗi chunk chỉ mở một lần** cho mọi trang dùng nó. Chunk thường là cả chương (có thể hàng nghìn dòng), nên đừng đọc trọn chương: `grep -n` heading trong dải dòng của chunk để tìm **mục** phủ chủ đề của trang, rồi đọc trọn mục đó. Đọc trọn mục, không chỉ vài dòng đã trích ở chú thích cũ — claim còn thiếu thường nằm ngay cạnh đoạn đã trích. Chunk ngắn (≲ 400 dòng) thì đọc trọn.
3. Với mỗi đoạn nguồn, phân loại:
   - Claim nguồn nói mà trang **chưa có** → đề xuất thêm, kèm chú thích vị trí `(<source id>, <chương>, <mục>, d.<từ>–<đến>)`; nguồn nhiều file thêm file: `(<source id>, <chương>, <mục>, file <hậu tố>, d.<từ>–<đến>)`.
   - Đoạn nguồn **nói khác** một claim trên trang mà claim đó đến từ **nguồn khác** → đây là mâu thuẫn nguồn (luật cứng 2): đề xuất đánh `⚠️ Conflict` kèm cả hai claim + vị trí, không tự chọn bên nào đúng.
   - Claim trên trang **sai so với chính nguồn nó dẫn** → không sửa; ghi `_inbox.md` (`- [YYYY-MM-DD] <trang>: <claim> lệch <vị trí nguồn>`) và đề xuất `/review-node`.
   - Claim mới cần một khái niệm **chưa có trang** → vẫn đề xuất claim, không tạo stub (stub là việc của ingest, §9); ghi khái niệm đó vào phần gap C.

**C. Đánh giá gap của cluster** (chỉ báo cáo): độ đầy đủ (thiếu góc nào so với logic chủ đề), độ sâu (trang nào chỉ có 1 claim mỏng), độ liên kết nội cluster (outlink/backlink thưa), khái niệm còn thiếu trang từ B.3.

### Bước 2 — Trình một bản đề xuất gộp, chờ duyệt một lần

Không viết gì vào `02_wiki/` trước bước này. Trình trong chat, gom theo trang:

- Claim mới B: trang · claim rút gọn · chú thích vị trí · nguồn mới cần thêm vào `sources:` (nếu có).
- `⚠️ Conflict` đề xuất đánh dấu (B.3).
- Link bổ sung A: trang · câu chèn link.
- Trang `analysis` đề xuất A (title + ý chính), nếu có.
- **Hệ quả status:** đánh dấu rõ trang nào đang `stable`/`stale` sẽ về `draft` nếu thêm claim (§9), để người dùng cân nhắc — nhiều trang vừa được promote.
- Tóm tắt A (mâu thuẫn khung hiểu) và C (gap) — phần này không cần duyệt vì không ghi vào wiki.

Người dùng duyệt cả lô, bớt mục, hoặc từ chối hết. Gộp một lần duyệt giúp người dùng thấy toàn cảnh thay vì bị hỏi rải rác qua từng chức năng.

### Bước 3 — Ghi đúng phần đã duyệt

Đọc schema theo nhánh (xem đầu skill), áp skill `writing-style` profile wiki cho mọi câu mới.

- **Claim mới:** viết vào đúng trang, theo §7 (không heading, viết lại bằng lời mình, link trong câu, chú thích ngay sau claim). Nâng `last_updated`; trang `stable`/`stale` về `draft`. Nguồn mới → thêm source id vào `sources:` (inline list). Không backfill chú thích cho claim cũ — việc đó thuộc `/review-node` khi đối chiếu.
- **`⚠️ Conflict`:** chèn cả hai claim + vị trí; không sửa claim nào.
- **Link bổ sung:** chèn vào câu kèm lý do; không nâng `last_updated` (§7.5).
- **Trang `analysis`:** title câu trần thuật (§8); `sources:` không rỗng — ghi source id của các trang đã tổng hợp; chú thích §7.5 lấy lại từ chính các trang đó, trang nào chưa có chú thích thì nói rõ là chưa truy được tới dòng; thêm trang vào `02_wiki/index.md`.
- **Không đụng `reviewed`/`reviewed_by`** — quyền đó thuộc `/review-node`.

### Bước 4 — Xuất báo cáo

Luôn xuất, kể cả khi người dùng từ chối hết: `Claude outputs/research-<YYYY-MM-DD>-<chủ đề>.md`, gồm cluster đã duyệt (trang · backlink · tag), kết quả A, danh sách B (đã ghi / bị từ chối / bị dừng vì chunk chưa `[x]`), gap C, các mục đã ghi `_inbox.md`.

### Bước 5 — Kiểm

Có ghi bất kỳ file nào trong `02_wiki/` (claim, link, conflict, analysis, `index.md`) → chạy `python .claude/hooks/validate_wiki_page.py --all`, phải sạch trước khi ghi log. Đây là cách duy nhất bắt trang `analysis` mồ côi.

### Bước 6 — Ghi log

Mỗi lượt research ghi đúng 1 mục vào **cuối** `log.md`, kể cả lượt chỉ ra báo cáo — như lint, vì báo cáo là sản phẩm cần truy vết. Giờ lấy bằng `python .claude/hooks/validate_wiki_page.py --now`:

```markdown
## [<giờ>] research | <chủ đề>
- Cluster N trang; enrich M trang
- <kết quả, vd "5 claim mới ở 3 trang, 2 link, 1 analysis; 1 trang dừng vì chunk [~]">
- Báo cáo: Claude outputs/research-<...>.md
```

## Sai lầm thường gặp

- **Viết trước rồi mới báo:** mọi thay đổi trong `02_wiki/` đi qua bản đề xuất gộp ở bước 2.
- **Đọc trọn cả chương cho mỗi trang:** gom theo chunk, thu hẹp tới mục bằng heading — nhưng cũng đừng chỉ đọc lại đúng vài dòng đã trích cũ.
- **Đào vào chunk `[~]`/`[ ]`:** đó là việc của `/ingest`.
- **Sửa claim sai của chính nguồn trang dẫn:** ghi `_inbox.md`, đề xuất `/review-node`.
- **Lẫn hai loại mâu thuẫn:** hai *trang* diễn giải lệch nhau → chỉ báo cáo; hai *nguồn* nói khác nhau → `⚠️ Conflict`.
- **Quên hậu tố file khi trích nguồn nhiều file** → chú thích trỏ sai chỗ còn tệ hơn không có.
- **Tạo stub cho khái niệm mới:** research không tạo stub; ghi vào gap C.
