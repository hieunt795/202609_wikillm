---
name: promote
description: Nâng trạng thái trang wiki từ draft lên stable sau khi người dùng duyệt danh sách "Đủ điều kiện stable" do lint đưa ra. Dùng khi người dùng muốn promote, nâng status, duyệt trang lên stable, chốt trang ổn định.
---

# Promote — nâng `draft` → `stable`

Đọc `00_schema.md` §9 (vòng đời `status`, mục *Ai chịu trách nhiệm từng bước chuyển*) trước khi ghi.

**Chỉ chạy trên danh sách người dùng đã duyệt.** Danh sách gốc là mục *Đủ điều kiện `stable`* trong báo cáo lint gần nhất. Người dùng có thể bỏ bớt trang; agent **không** tự thêm trang ngoài danh sách.

## Quy trình

**1. Kiểm lại điều kiện ngay trước khi ghi** — wiki có thể đã đổi từ lúc lint:

```bash
python .claude/hooks/validate_wiki_page.py --all
```

Với từng trang trong danh sách, xác nhận đồng thời: `status: draft`; hook không báo gì cho trang; outlink ≥ 1; backlink ≥ 2 (đếm theo `lint/SKILL.md`); không còn `⚠️ Conflict`. Trang nào trượt → bỏ khỏi lượt này và báo lại lý do, không sửa trang để nó qua.

**2. Ghi.** Chỉ đổi dòng `status: draft` → `status: stable` trong frontmatter. **Không** đổi `last_updated` (nội dung không đổi — §7.5), **không** đặt `reviewed:` (chỉ người dùng đặt — §9), không chạm thân bài.

**3. Chạy lại `--all`**, phải sạch.

**4. Ghi 1 mục `log.md`** theo §12: `## [YYYY-MM-DD:hh-MM-ss] promote | <số trang> trang lên stable`, dòng dưới liệt kê tên trang (hoặc số trang nếu quá dài) và các trang bị loại kèm lý do.

## Sai lầm thường gặp

- Tự promote vì "lint đã sạch" mà chưa có người duyệt → vi phạm §9; `stable` mất nghĩa.
- Nâng `last_updated` khi promote → trang bị hook đòi chú thích §7.5 dù nội dung không đổi, và tiêu chí stale bị lệch.
- Thêm link cho trang đủ backlink ≥ 2 ngay trong lượt promote → đó là sửa nội dung, phải là lượt riêng và qua lint lại.
