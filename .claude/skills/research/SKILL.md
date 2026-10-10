---
name: research
description: 'Đọc lại một vùng tri thức đã có trong 02_wiki theo chủ đề, chỉ dựa trên wiki và nguồn đã ingest (mục `--coverage` báo đã phủ), không tìm web. Hai pha: Map quét rộng metadata + neighborhood 1 vòng, chia chủ đề thành subcluster ≤ 15 node và lưu bản đồ vào Claude outputs; Deep read đọc trọn một subcluster, enrich ≤ 7 node từ mục nguồn đã phủ, tìm link thiếu, ⚠️ Conflict giữa nguồn, mâu thuẫn khung hiểu và gap, rồi trình một proposal gộp chờ duyệt. Dùng khi người dùng muốn research, đào sâu, rà lại, tổng hợp toàn bộ mảng X trong wiki, bổ sung claim còn thiếu cho các trang về Y, đánh giá wiki đã đủ sâu về Z chưa, kiểm các trang cùng chủ đề có nhất quán không, làm tiếp subcluster của một map có sẵn, hoặc enrich một/vài trang chỉ định từ nguồn đã ingest. Không dùng cho: trả lời 1 câu hỏi tức thời (query); nạp nguồn mới hoặc mục nguồn chưa phủ (ingest); sửa claim sai so với nguồn, backfill chú thích, đặt reviewed (review-node); sửa cấu trúc/format, link chết, mồ côi (lint); nghiên cứu trên web.'
---

# Research — đọc lại một vùng tri thức theo chủ đề

Research đọc lại cái wiki **đã có**, đối chiếu với nguồn **đã ingest xong**, và đề xuất bổ sung. Nó không nạp nguồn mới (ingest), không sửa claim sai (review-node), không sửa cấu trúc (lint). Op ghi `log.md` là `research`.

**Điểm vào:**

- Đầu vào là **chủ đề/tag** → Pha 1 Map, dừng ở câu hỏi chọn subcluster.
- Đầu vào là **tên trang, danh sách trang, hoặc subcluster của map có sẵn** → vào thẳng Pha 2 Deep read. Trang đơn lẻ = subcluster gồm trang đó; người dùng có thể thêm láng giềng.

**Giới hạn (§4):**

| Phạm vi | Giới hạn |
|---|---|
| Map | không giới hạn node quét (chỉ metadata); neighborhood đúng 1 vòng |
| Subcluster / Deep read | ≤ 15 node full content, 1 subcluster mỗi lượt |
| Enrich | ≤ 7 node mỗi lượt (mục tiêu 5); ≤ 3 claim mỗi node |
| Proposal | ≤ 20 mục cần duyệt; ≤ 1 trang `analysis` |
| Nguồn | mục đã phủ theo `--coverage`, hoặc nguồn ngắn; không web |

**Đọc `00_schema.md`:** theo nhánh, không đọc trước. Pha 1–2 không cần schema. Chỉ khi sắp ghi (Pha 3) mới đọc §7, §10 mục *nguồn nhiều file*; thêm §1, §8 nếu tạo `analysis`.
**Dừng chờ duyệt:** Pha 3, sau khi trình proposal gộp; không ghi wiki trước khi người dùng đồng ý.
**Ghi log:** luôn, kể cả lượt chỉ Map, op `research`.

## Pha 1 — Map (rẻ, không mở full content)

1. Đổi thuật ngữ Việt sang Anh (title/tag là tiếng Anh, vd "dự trữ bắt buộc" → `required-reserve`). Thuật ngữ có ≥ 2 cách dịch không tương đương nghĩa → hỏi lại.
2. **Map có sẵn:** nếu đã có `Claude outputs/research-map-<chủ đề>.md`, dùng lại; chỉ quét thêm node mới (so `last_updated`/tên file) và báo phần thay đổi.
3. Gom node:

   ```bash
   ls 02_wiki | grep -i "<từ khoá>"
   grep -l -i -E "^(title|tags):.*<từ khoá>|^  - .*<từ khoá>" 02_wiki/*.md
   ```

   Vế `^  - .*` bắt tag YAML nhiều dòng; thiếu nó sẽ sót phần lớn cụm. Mở rộng **đúng 1 vòng**: outlink `grep -o "\[\[[^]|]*" 02_wiki/<trang>.md | sort -u`, backlink `python .claude/hooks/validate_wiki_page.py --backlinks <trang>`. Không đệ quy.
4. Chia **subcluster ≤ 15 node** theo tag/title đồng xuất hiện và mật độ link giữa node. Mỗi sub có tên ngắn và lý do. Node chỉ vào qua neighborhood mà không khớp sub nào → *node rìa*.
5. Ghi map (mục *Output contract*), trình tóm tắt, hỏi chọn sub. Cả chủ đề ≤ 15 node → một sub duy nhất, hỏi luôn "deep read ngay?" để gộp Pha 1–3 trong một lượt.

Lượt dừng ở Map vẫn ghi log (Pha 3 bước 5).

## Pha 2 — Deep read (một subcluster, chưa ghi wiki)

Mở full content các node của sub. Mọi kết quả chỉ là đề xuất.

**Đối chiếu nội bộ:**

- Link còn thiếu giữa node cùng sub → câu chèn `[[link]]` kèm lý do.
- **Mâu thuẫn khung hiểu:** hai trang diễn giải cùng một điểm lệch nhau → chỉ báo cáo. Không phải `⚠️ Conflict` (vốn dành cho hai *nguồn* nói khác).
- Ý lặp ở ≥ 2 trang trong sub, đáng tái sử dụng lâu dài → có thể đề xuất 1 trang `type: analysis`. Dedup trước: `grep -l "^type: analysis" 02_wiki/*.md`, đối chiếu title; đã có trang cùng ý thì đề xuất cập nhật trang đó.

**Enrich ≤ 7 node** — ưu tiên trang mỏng, backlink cao, có mục nguồn đã phủ nói về chủ đề; nói rõ lý do chọn. **Loại node vượt 1.000/250 từ khỏi danh sách enrich** (chạy `--size` trước): node sắp tách trang không nên merge thêm claim.

1. Nguồn hợp lệ: nguồn trong `sources:` của node, **và** nguồn mà node khác trong sub đã trích tới đúng chủ đề (chú thích §7 luật 5 chỉ sẵn chunk — không lục toàn bộ nguồn). Tra `03_state/_sources_manifest.md` để biết nguồn ngắn/dài và đường dẫn.
   - **Nguồn dài:** chunk trong `03_state/<source id>.md`. Chạy `python .claude/hooks/validate_wiki_page.py --coverage <source id>`: chỉ đọc chunk `phu` và các mục của chunk `do` mà lệnh không liệt kê là chưa phủ. Chunk `chua` và mục chưa phủ → dừng enrich từ phần đó, ghi vào mục *chặn ingest*. Phần nguồn chưa qua bước bàn ý chính của ingest thì research không đọc trước.
   - **Nguồn nhiều file** (vd `fixed_income_during`): cột *Mục trong nguồn* ghi file; dải dòng tính trong file đó.
   - **Nguồn ngắn** (không có state file): coi như đã ingest trọn; `grep -n` từ khoá, đọc đoạn quanh kết quả.
2. **Gom theo chunk, mỗi chunk mở một lần** cho mọi node dùng nó. `grep -n` heading trong dải dòng để tìm **mục** phủ chủ đề, rồi đọc trọn mục — không chỉ vài dòng đã trích cũ, claim thiếu thường nằm ngay cạnh. Chunk ≲ 400 dòng thì đọc trọn.
3. Phân loại từng đoạn nguồn:
   - Claim nguồn nói mà trang **chưa có** → đề xuất, kèm `(<source id>, <chương>, <mục>, d.<từ>–<đến>)`; nguồn nhiều file thêm `file <hậu tố>` trước dải dòng.
   - Đoạn nguồn **nói khác** claim trên trang mà claim đó đến từ **nguồn khác** → đề xuất `⚠️ Conflict` kèm cả hai claim + vị trí (quy tắc bắt buộc 2).
   - Claim trên trang **sai so với chính nguồn nó dẫn** → không sửa; ghi `_inbox.md` (`- [YYYY-MM-DD] <trang>: <claim> lệch <vị trí nguồn>`), gợi ý `/review-node`.
   - Claim cần khái niệm **chưa có trang** → vẫn đề xuất claim, không tạo stub; ghi khái niệm vào gap.

**Gap** (chỉ báo cáo): góc chủ đề còn thiếu, node chỉ có 1–2 claim mỏng, liên kết nội sub thưa, khái niệm chưa có trang.

## Pha 3 — Proposal → duyệt → ghi

1. **Trình một proposal gộp** (mục *Output contract*), một lần duyệt. Người dùng duyệt cả lô, bớt theo mã mục, hoặc từ chối hết. Không ghi gì vào `02_wiki/` trước khi duyệt.
2. **Ghi đúng các mục đã duyệt** — áp skill `writing-style` profile wiki cho mọi câu mới. **Áp luật 6 (§7):** trang tự đủ nghĩa qua link, không giọng thuyết phục/khuyến nghị, ưu tiên mật độ ý. Chạy `python .claude/hooks/validate_wiki_page.py --style` trước khi ghi log kiểm luật này.
   - `C` claim: không heading, viết lại bằng lời mình, link nằm trong câu, chú thích ngay sau claim (§7). Nâng `last_updated`. Source id mới → `sources:` (inline list).
   - `L` link: chèn vào câu kèm lý do; không nâng `last_updated` (§7 luật 5).
   - `K` conflict: chèn cả hai claim + vị trí; không sửa claim nào.
   - `N` analysis: title câu trần thuật (§8); `sources:` = source id của các trang đã tổng hợp; chú thích §7 luật 5 lấy từ chính các trang đó, thiếu thì nói rõ chưa truy được tới dòng; thêm vào `02_wiki/index.md`.
   - **Không làm ngoài proposal:** không dọn format ("Xem thêm", heading…), không backfill chú thích claim cũ, không đụng `reviewed`/`reviewed_by`, không đổi `status`. Gặp lỗi cấu trúc → nêu trong báo cáo cho `/lint`.
3. Có ghi file trong `02_wiki/` → `python .claude/hooks/validate_wiki_page.py --all`, phải sạch trước khi log (cách duy nhất bắt `analysis` mồ côi).
4. Xuất báo cáo, cập nhật trạng thái sub trong map (`done <ngày>` / `partial`).
5. Ghi đúng 1 mục vào **cuối** `log.md`, kể cả lượt chỉ Map hoặc từ chối hết. Giờ lấy bằng `python .claude/hooks/validate_wiki_page.py --now`.

## Output contract

**Map** — `Claude outputs/research-map-<chủ đề>.md`

- Đầu file: chủ đề, từ khoá EN, ngày quét, tổng node.
- Bảng subcluster: `id · tên · số node · trạng thái` (`pending` / `done <ngày>` / `partial`).
- Mỗi sub: bảng `trang · lý do vào · backlink · status · nguồn chính`.
- Danh sách node rìa.

**Proposal** (trong chat, mã mục để duyệt từng phần)

- `C1…` claim mới: trang · claim rút gọn · chú thích vị trí · source id mới (nếu có).
- `L1…` link: trang · câu chèn link.
- `K1…` `⚠️ Conflict`: hai claim + hai vị trí.
- `N1` `analysis` (nếu có): title + ý chính + trang nguồn.
- **Chặn ingest:** mỗi chunk hoặc mục chưa phủ một dòng — `⚠️ <source id> <chunk/mục> chưa phủ: chặn enrich <T1>, <T2>; cần /ingest trước.`
- Không cần duyệt (không ghi wiki): mâu thuẫn khung hiểu, gap, mục đã ghi `_inbox.md`.

**Báo cáo** — `Claude outputs/research-<YYYY-MM-DD>-<chủ đề>-<sub id>.md`: sub đã đọc (trang · backlink · status), mục đã ghi / bị từ chối / bị chặn, mâu thuẫn khung hiểu, gap, mục `_inbox.md`, lỗi cấu trúc chuyển `/lint`. Lượt chỉ Map thì map là báo cáo.

**Log**

```markdown
## [<giờ>] research | <chủ đề> — <map | sub id>
- Map: N node, K sub | Deep: sub X, đọc N, enrich M
- <C claim, L link, K conflict, N analysis; P trang → draft; chặn: <chunk>>
- Báo cáo: Claude outputs/research-<...>.md
```

## Sai lầm thường gặp

- **Viết trước rồi mới báo:** mọi thay đổi `02_wiki/` đi qua proposal.
- **Deep read nhiều sub trong một lượt:** một lượt một sub; sub còn lại để `pending` trong map.
- **Quên cập nhật map:** lượt sau sẽ quét lại hoặc làm lại sub đã xong.
- **Dọn format tiện tay khi ghi:** việc của lint; diff research chỉ chứa mục đã duyệt.
- **Đọc trọn cả chương cho mỗi trang** hoặc **chỉ đọc lại đúng vài dòng đã trích:** gom theo chunk, thu hẹp tới mục, đọc trọn mục.
- **Đào vào phần nguồn chưa phủ, sửa claim sai, tạo stub:** lần lượt là việc của ingest, review-node, ingest.
- **Lẫn hai loại mâu thuẫn:** hai *trang* lệch nhau → báo cáo; hai *nguồn* nói khác → `⚠️ Conflict`.
- **Quên hậu tố file khi trích nguồn nhiều file** → chú thích trỏ sai còn tệ hơn không có.

## Ví dụ rút gọn

**Lượt 1 — Map.** "Research cân đối nguồn – sử dụng nguồn ngân hàng." Từ khoá `balance-sheet`, `ftp`, `alm`, `ldr`, `nsfr`, `lcr`. Gom 18 node + 4 node rìa → 3 sub: S1 cấu trúc bảng cân đối & gap (7), S2 FTP điều phối nguồn vốn (6), S3 giới hạn quy định LDR/NSFR/LCR (5). Ghi `research-map-bank-sources-and-uses.md`, hỏi chọn sub. Log: `research | bank sources-and-uses — map`.

**Lượt 2 — Deep read S3.** Đọc 5 node; enrich 3. Proposal: C1–C4 claim từ mục đã phủ của `bcbs_238` và `bcbs_368`, L1–L2 link LCR ↔ NSFR, gap "chưa có trang về HQLA haircut". Người dùng bỏ C3 → ghi C1, C2, C4, L1, L2 → `--all` sạch → báo cáo → map S3 `done` → log.

Lượt 3 có thể gọi thẳng "research S2 của map bank-sources-and-uses" để vào Deep read.
