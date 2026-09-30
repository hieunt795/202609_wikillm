# Session handoff: Evergreen adjustments (hook part done)

## Đã xong (commit 1adb5d7)

**Hook `.claude/hooks/validate_wiki_page.py`:**
- Thêm 3 lệnh báo cáo (exit 0): `--size`, `--tags`, `--style`
- Docstring + help text cập nhật
- Test xác nhận: 139 trang > 1.000 từ, 1.511 tag (1.029 tag dùng 1 lần), 469 trang có cụm cấm/rule6

**`00_schema.md`:**
- §4: thêm dòng ngưỡng 1.000/250 từ

## Còn lại (7 mục)

1. **Schema §5, §6, §7 (luật 6)** — thêm dấu hiệu Atomic "vượt ngưỡng", luật tag từ vựng kiểm soát, luật 6 (người đọc là chủ wiki)
2. **CLAUDE.md** — 3 dòng bảng Công cụ kiểm
3. **ingest/SKILL.md** — 5 bước sửa (b.3 dùng `--tags`, b.4 chạy `--size` + phép thử tự đủ nghĩa, b.5 sửa outlink, b.9 chạy `--size`/`--style`)
4. **research/SKILL.md** — Pha 2 loại node vượt ngưỡng; Pha 3 áp luật 6 + chạy `--style`
5. **lint/SKILL.md** — bước 0 thêm 3 lệnh; "12 tiêu chí" → 15
6. **writing-style/SKILL.md** — thêm F4 (profile wiki); quy tắc 6
7. **Sổ sách** — `decisions.md`, `log.md`, handoff mới (file này)

## Lưu ý

- Ngưỡng 1.000/250 từ (không phải 800/150): áp bằng `--size`, chỉ báo cáo cho lint đọc tay.
- Luật 6 ngắn gọn: người đọc là chủ wiki → trang tự đủ nghĩa + tổ chức theo ý + không thuyết phục.
- writing-style F4 không thêm rule nào khác, chỉ rõ profile wiki là giọng phân tích kỹ thuật.
- Tag từ vựng kiểm soát: không dọn tag cũ, chỉ ghi quy tắc dùng lại tag có sẵn.
