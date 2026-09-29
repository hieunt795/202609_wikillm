# Handoff: thiết kế lại skill `/research`

## Kết quả

- `.claude/skills/research/SKILL.md` viết lại (130 dòng): 2 pha **Map** (lưu `Claude outputs/research-map-<chủ đề>.md`, subcluster ≤ 15) và **Deep read** (1 sub/lượt, đọc ≤ 15, enrich ≤ 7, ≤ 3 claim/trang, proposal mã C/L/K/N ≤ 20 mục). Bỏ trục A/B/C. Không tách `research-node`/`research-topic`.
- `00_schema.md` §2, §3 (tên báo cáo + map), §4 (giới hạn 15/7), §9 cập nhật tham chiếu.
- `CLAUDE.md` dòng `/research` trong bảng operation cập nhật.
- `decisions.md` mục [2026-09-29]; `log.md` mục `schema`.
- Plan thiết kế: `~/.claude/plans/h-y-thi-t-k-l-i-wise-dragon.md`.

## Kiểm tra

- `validate_wiki_page.py --all`: 1033 trang, 0 vấn đề, 0 mồ côi.
- grep không còn giới hạn 10/5 hay "chức năng A/B" của research.

## Việc còn lại

- Chưa commit.
- Chưa dry-run skill mới. Đề xuất lượt đầu: Map "bank sources-and-uses" (tái tạo S1/S2 done, S3 LDR/NSFR/LCR pending), rồi Deep read S3.
- Log research 2026-09-28 có mục 4 dòng (vượt luật 3 dòng) và tạo trang mới ngoài phạm vi — không sửa hồ sơ cũ; lint có thể nêu.
