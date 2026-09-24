# Session Handoff: Improve skill `/ingest` theo audit

**Ngày tạo**: 2026-09-24:21-24-xx

## Kết quả

Sửa `.claude/skills/ingest/SKILL.md` theo 4 khuyến nghị từ audit skill-creator:

### 1. Mạnh hóa description (frontmatter)
- Từ: "Dùng khi người dùng muốn ingest..."
- Thành: "**PHẢI dùng skill này cho mọi lượt cập nhật wiki từ tài liệu nguồn.** Trigger khi... Không bỏ skill này dù người dùng không nói rõ ràng."
- Lý do: Tránh undertriggering theo tiêu chuẩn skill-creator

### 2. Thêm mục "Test prompts"
- 3 ví dụ prompt thực tế cho người dùng validate skill
- Vị trí: Sau phần "Tham chiếu", trước "## Quy trình"

### 3. Thêm mục "Xử lý lỗi"
- 4 scenario chi tiết: trang mồ côi, không tìm liên kết, lỗi fatal, liên kết thất bại giữa chừng
- Vị trí: Sau "## Sai lầm thường gặp"
- Mục đích: Làm rõ quy trình fallback và khi nào dừng lại

### 4. Thêm mục "Tham chiếu (Bundled resources)"
- Liệt kê: tài liệu (schema.md, rules), công cụ (hook), skill phụ (writing-style)
- Vị trí: Đầu file, sau intro đọc schema
- Mục đích: Progressive disclosure rõ ràng

## Kiểm tra

- Sửa file bằng Edit tool → hook PostToolUse chạy tự động
- `python .claude/hooks/validate_wiki_page.py --all` → 744 trang, 0 lỗi, 0 trang mồ côi ✅
- Markdown linting: có 5 warning MD032/MD033 (list format) nhưng không ảnh hưởng chức năng

## Công việc còn lại

Không có. Audit + cải tiến skill ingest hoàn tất.

## Context

Sau audit skill `/ingest` theo phương pháp skill-creator (4 tiêu chí: cấu trúc, hiệu quả, tuân thủ, scope), báo cáo gợi ý 4 khuyến nghị. Lượt này thực hiện luôn các khuyến nghị tránh cần thêm phiên làm việc riêng.

Skill description được cập nhật tự động trong hệ thống (system-reminder báo danh sách skill có sẵn).
