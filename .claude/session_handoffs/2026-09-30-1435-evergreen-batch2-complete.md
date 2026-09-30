# Session handoff: Evergreen audit — batch 2 done

## Completed (commit pending)

**Evergreen compliance strengthening — Audit → Plan → Implement batch 2:**
- Hook 3 lệnh (`--size`, `--tags`, `--style`) — commit 1adb5d7 [ALREADY DONE previous session]
- Schema §4–7 (ngưỡng mềm 1.000/250, dấu hiệu vượt ngưỡng, tag vocabulary rule, luật 6 định nghĩa)
- CLAUDE.md bảng công cụ +3 dòng
- ingest/SKILL.md (bước 3 `--tags`, bước 4 `--size`+phép thử luật 6, bước 5 outlink sửa, bước 9 `--size/--style`)
- research/SKILL.md (Pha 2 loại oversized node, Pha 3 luật 6 + chạy `--style`)
- lint/SKILL.md (bước 0 +3 lệnh, 12 → 15 tiêu chí, thêm 3 tiêu chí mới)
- writing-style/SKILL.md (F4 profile wiki +luật 6 tham chiếu)
- decisions.md +1 mục [2026-09-30]
- log.md +1 mục [2026-09-30:14-35-00]

## Verification (before commit)

```bash
python .claude/hooks/validate_wiki_page.py --help          # xác nhận 3 lệnh mới có trong help
python .claude/hooks/validate_wiki_page.py --size          # đo 139 trang > 1.000 từ (baseline)
python .claude/hooks/validate_wiki_page.py --tags          # đo 1.511 tag (baseline)
python .claude/hooks/validate_wiki_page.py --style         # đo 469 trang cụm cấm/luật 6 (baseline)
```

Tất cả sẽ exit 0 (lệnh báo cáo chỉ).

## State

- Hook chạy được từ session trước (commit 1adb5d7).
- Tất cả 7 file skill, schema, CLAUDE.md sửa xong.
- decisions.md + log.md + handoff ghi xong.
- Sẵn sàng commit toàn bộ batch 2.

## Next

1. User xác nhận hoặc yêu cầu sửa
2. Commit batch 2 với message:
   ```
   feat(schema,hook,skill): Evergreen compliance — Atomic size, tag vocabulary, writing-for-self rule 6
   ```
3. Nếu cần: sửa các page 02_wiki (không phạm vi batch này)
4. Session tiếp: ingest/research/lint/review sẽ áp quy tắc mới

## Notes

- Ngưỡng 1.000/250 từ (không phải 800/150): chỉ báo cáo, không chặn ghi; quyết định 2026-09-30
- Luật 6 "người đọc là chủ wiki": trang tự đủ nghĩa, không khuyến nghị, mật độ trước polish
- Writing-style F4 rõ: chỉ phân tích kỹ thuật; không mẫu BIS mở/kết; không giải thích phổ thông
- Tag từ vựng: không dọn cũ; chỉ ghi quy tắc dùng lại khi ingest tiếp
- Hook `--size/--tags/--style` là lệnh báo cáo (exit 0); sau có thể siết thành cảnh báo nếu cần
