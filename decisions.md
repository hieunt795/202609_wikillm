# Decisions

> Lý do các quyết định thiết kế. `log.md` chỉ ghi *chuyện gì đã xảy ra*; file này ghi *vì sao*. Quyết định nào đã có lý do đầy đủ trong `00_schema.md` thì ở đây chỉ trỏ tới mục đó, không chép lại.
>
> Định dạng: mỗi quyết định là 1 mục `## [YYYY-MM-DD] <tiêu đề>`, gồm *Quyết định* · *Lý do* · *Thay cho* (nếu có). Quyết định bị đảo thì thêm mục mới trỏ về mục cũ, không sửa mục cũ.
>
> Bản log dài trước 2026-09-15 (chứa lập luận gốc của các mục 2026-09-12 → 2026-09-14): `git show e2adb7a:log.md`.

## [2026-09-14] Thêm mục `## Sources` vào `index.md`
- **Quyết định:** bảng trạng thái cấp nguồn ở đầu `index.md`, cập nhật mỗi lượt ingest kể cả lượt không tạo trang.
- **Lý do:** trước đó muốn biết nguồn nạp tới đâu phải diễn giải lại văn xuôi trong `log.md`.

## [2026-09-14] Trạng thái ingest nằm ở `03_state/`, không đặt cạnh nguồn
- **Quyết định:** lớp thứ tư `03_state/`, luật `01_sources/` bất biến không ngoại lệ. Lý do đầy đủ: `00_schema.md` §10.
- **Thay cho:** file `_ingest_state.md` đặt trong `01_sources/` (đã hoàn nguyên cùng ngày — tiền tố `_` không phân biệt được nguồn với không-nguồn, vì `Modern Money Mechanics` đã có sẵn 15 file `_page_*.jpeg`).

## [2026-09-14] Ngưỡng nguồn dài: > 120 KB hoặc > 1.200 dòng
- Lý do và lý do không dùng số heading: `00_schema.md` §10. Ngưỡng đặt ở schema chứ không ở skill vì nó quyết định nguồn có state file hay không — là thuộc tính data model.

## [2026-09-14] Chú thích vị trí cho claim từ nguồn dài, không backfill
- Lý do: `00_schema.md` §7 luật 5. Nợ backfill theo dõi ở `_inbox.md`.

## [2026-09-14] Thêm `_inbox.md`
- Lý do `status: stub` không thay được vùng capture: `00_schema.md` §11.

## [2026-09-14] Lint có tiêu chí *Nhiễu OCR còn sót*
- 6 họ mẫu, đối chứng ngược bắt 8/9 lỗi thật của nguồn IMF; giới hạn đã biết ghi trong `lint/SKILL.md`.

## [2026-09-14] `reviewed:` là trường tuỳ chọn, không có tiêu chí lint
- Lý do: `00_schema.md` §9 mục *`status` không đo việc người dùng đã đọc qua*.

## [2026-09-14] Không đưa `01_sources/` lên GitHub; bù bằng bản kê SHA-256
- **Lý do:** repo public, nguồn là ấn phẩm IMF có bản quyền. Chú thích §7.5 trỏ tới số dòng nên cần checksum để người clone kiểm chứng được: `03_state/_sources_manifest.md`. `.claude/` được commit vì hook và skill là đặc tả thực thi.

## [2026-09-15] Rollback toàn bộ về `e2adb7a`
- **Quyết định:** bỏ lượt ingest Ch.1 + Ch.3 (117 trang), giữ ở tag `ch3-snapshot`.
- **Lý do:** người dùng chọn làm lại từ bản 51 trang. Chi tiết audit bản 117 trang: `Claude outputs/audit-2026-09-15.md` (không commit).

## [2026-09-15] Lấy lại riêng hook từ `ch3-snapshot`
- **Quyết định:** chỉ phục hồi `.claude/hooks/validate_wiki_page.py` (có `--all`, bắt link chết, `sources` rỗng, trang mồ côi, §7.5 theo `last_updated`); không phục hồi nội dung Ch.3, không phục hồi các thay đổi §2/§5 của commit đó.
- **Lý do:** hook cũ cho qua trang có link chết và `sources: []` (đã thử). Các thay đổi §2 (*ưu tiên lý luận trước tường thuật*) và §5 (*ba phép kiểm, bỏ tiêu chí độ dài*) là chính sách nội dung gắn với lượt ingest Ch.3 — để người dùng quyết khi làm lại Ch.3.

## [2026-09-15] Định dạng log mới
- **Quyết định:** `## [YYYY-MM-DD:hh-MM-ss] <op> | <tiêu đề>` + tối đa 3 dòng; 6 op cố định; giờ Việt Nam; mục cũ không rõ giờ ghi `00-00-00`. Chi tiết: `00_schema.md` §12.
- **Lý do:** gist Karpathy dùng tiền tố `## [` để grep được; log cũ dài 431–3.779 ký tự/mục, có 10 loại động từ, kiêm cả biên bản quyết định.
- **Ánh xạ động từ cũ:** `bồi đắp` → `ingest`; `schema-batch`, `đính chính` → `schema`; `publish` → `repo`.

## [2026-09-15] Thêm operation Promote
- **Quyết định:** lint đưa ra danh sách *Đủ điều kiện `stable`* (hook sạch, outlink ≥ 1, backlink ≥ 2, không conflict, không bị flag) → người dùng duyệt → `/promote` đổi status.
- **Lý do:** §9 cũ không gán bước `draft → stable` cho operation nào nên 51/51 trang kẹt ở `draft`, kéo theo tiêu chí stale và sai vòng đời không bao giờ kích hoạt. Ngưỡng backlink ≥ 2 do người dùng duyệt.

## [2026-09-15] Ingest có bước 0: duyệt 3–5 ý chính
- **Lý do:** gist Karpathy đặt bước "đọc và bàn ý chính" trước khi ghi; audit đo được `reviewed` 0/51 và `_inbox.md` chưa từng dùng — người dùng vắng mặt khỏi vòng lặp.

## [2026-09-15] `last_updated` đo nội dung, không đo liên kết
- **Quyết định:** chỉ chèn `[[wikilink]]` vào câu có sẵn thì không nâng `last_updated` (`00_schema.md` §7 luật 5).
- **Lý do:** tiêu chí stale so `last_updated` với ngày ingest nguồn; và hook đòi chú thích §7.5 cho mọi trang có ngày từ 2026-09-14 — nâng ngày vì một cái link sẽ buộc backfill chú thích cho claim không hề đổi.

## [2026-09-15] Không tạo trang tóm tắt nguồn
- Lý do: `00_schema.md` §2.

## [2026-09-15] Title tiếng Anh, thân bài tiếng Việt
- Lý do: `00_schema.md` §3. Chốt theo thực tế 51/51 trang.

## [2026-09-15] Không tạo stub `fiscal-deficit`
- **Lý do:** audit đề xuất dựa trên đếm chuỗi "thâm hụt" (5 trang), nhưng 4/5 trang nói thâm hụt vãng lai; thâm hụt ngân sách chỉ xuất hiện ở 1 trang — dưới ngưỡng ≥ 3 trang. Tạo lại khi ingest Ch.3.

## [2026-09-15] Cho phép model tự review trang
- **Quyết định:** agent được đặt `reviewed:` qua `/review`, luôn kèm `reviewed_by: model`; người dùng đặt `reviewed_by: user`. Agent không ghi đè `user`.
- **Lý do:** người dùng chọn giao việc review cho model. Tách `reviewed_by` để trường vẫn phân biệt được *model đã đối chiếu nguồn* với *người đã đọc* — lý do gốc của quyết định 2026-09-14 (`reviewed:` chỉ người đặt).
- **Thay cho:** mục [2026-09-14] *`reviewed:` là trường tuỳ chọn, không có tiêu chí lint* — phần "chỉ người dùng đặt" bị thay; phần "không có tiêu chí lint" giữ nguyên.
- **Giới hạn đã biết:** model soát trang do model viết, không độc lập hoàn toàn; bù bằng yêu cầu đọc lại đúng đoạn nguồn và gắn chú thích §7.5 cho từng claim đã đối chiếu.

## [2026-09-15] Ch.3 chỉ ingest phần lý luận, ingest lại từ nguồn
- **Quyết định:** ingest 5 cụm lý luận A–E; bỏ qua bối cảnh tài khoá Ba Lan (d.2531–2603) và Exercises/bảng/phụ lục (d.2604–3425). Viết mới từ nguồn, không khôi phục trang từ tag `ch3-snapshot`. Duyệt ý chính từng cụm.
- **Lý do:** người dùng chọn. Phục hồi nguyên tắc §2 *ưu tiên lý luận trước tường thuật* làm căn cứ ghi trong bản đồ chunk.
