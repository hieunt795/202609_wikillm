# Session handoff: audit và sửa `/research`

**Ngày:** 2026-09-23 19:37 UTC+7 · **Chưa commit**

## Kết quả

- Audit `/research` bằng skill-creator; người dùng duyệt đề xuất và cho phép dùng subagent.
- Viết lại `.claude/skills/research/SKILL.md`:
  - Chỉ còn một lượt duyệt đề xuất chung.
  - Đọc schema theo nhánh, chỉ khi sắp ghi trang.
  - Gom trang theo chunk, đọc theo mục thay vì trọn chương.
  - Chú thích nguồn nhiều file có hậu tố `file`.
  - Xử lý mâu thuẫn nguồn bằng `⚠️ Conflict`; claim sai của chính nguồn trang dẫn thì ghi `_inbox.md`.
  - Enrich liên nguồn có giới hạn; luôn ghi log.
- Sửa lệnh grep tag cho tag YAML nhiều dòng trong `research` và `query`.
- Đồng bộ `CLAUDE.md` (bảng 6 operation, luật cứng 4, `--all`), description của `query` và `.claude/rules/project-records.md`.
- Ghi `decisions.md`, 1 mục `log.md` op `schema`, và 3 mục `_inbox.md`:
  - Chuẩn chú thích During lệch giữa header state file và schema §7.5.
  - Chú thích Ch.28 lệch số mục và dải dòng.
  - Bản kê Cargill lệch với state file.

## Kiểm tra đã chạy

- Eval dry-run 3 case (IRRBB/Tata, bond futures/During, LOLR/Bindseil+Cargill), mỗi case chạy bản mới và snapshot bản cũ.
  - Workspace và viewer: `Claude outputs/research-workspace/`, `Claude outputs/eval-review-research-iter1.html`.
  - Cả hai bản 9/9 assertion, nên assertion chưa phân biệt được hai bản.
- Đã xác nhận không run nào ghi vào repo: checksum `_inbox.md`, `log.md` không có mục research, `writes/` không trùng trang thật.
- Trong lúc eval, một phiên khác ingest Tata Ch.2 cụm A và cụm B song song. Phiên này không đụng vào các thay đổi đó.

## Việc còn lại / bước tiếp theo

1. Commit các thay đổi phiên này. Tách riêng khỏi thay đổi của phiên ingest Tata khi `git add`.
2. Quyết định chuẩn chú thích During: hậu tố `file` hay chỉ số chương (mục inbox).
3. Nếu làm vòng eval 2: viết assertion phân biệt được hai bản (số lượt duyệt, dòng nguồn đọc, phát hiện `⚠️ Conflict` thật), và dùng cluster không bị phiên khác sửa song song.
4. Tuỳ chọn: tối ưu description (`run_loop`) cho `/research` so với `anthropic-skills:deep-research`.

## Blocker

- Không có. Lưu ý: harness chặn subagent ghi file tên `report.md`.
