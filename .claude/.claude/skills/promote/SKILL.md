---
name: promote
description: Nâng trạng thái trang wiki từ draft lên stable sau khi người dùng duyệt danh sách "Đủ điều kiện stable" do lint đưa ra. Dùng khi người dùng muốn promote, nâng status, duyệt trang lên stable, chốt trang ổn định, hoặc trả lời "duyệt danh sách" sau một báo cáo lint.
---

# Promote — nâng `draft` → `stable`

Đọc `00_schema.md` §7.5 (`last_updated` đo nội dung), §9 (vòng đời, điều kiện lên `stable`), §12 (log) trước khi ghi.

**Chỉ chạy trên danh sách người dùng đã duyệt.** Danh sách gốc là mục *Đủ điều kiện `stable`* trong báo cáo lint gần nhất (`Claude outputs/lint-*.md`). Người dùng có thể bỏ bớt trang; agent **không** tự thêm trang ngoài danh sách, vì `stable` chỉ có nghĩa khi người dùng đã chọn.

## Quy trình

**1. Kiểm lại điều kiện ngay trước khi ghi** — wiki có thể đã đổi từ lúc lint:

```bash
python .claude_draft/.claude/hooks/validate_wiki_page.py --all
python .claude_draft/.claude/hooks/validate_wiki_page.py --backlinks   # bảng đếm backlink
```

Với từng trang trong danh sách, xác nhận đồng thời: `status: draft`; `--all` không báo gì cho trang; outlink ≥ 1; backlink ≥ 2; không còn `⚠️ Conflict`. Trang nào trượt → bỏ khỏi lượt này và báo lại lý do, không sửa trang để nó qua.

**2. Ghi.** Chỉ đổi dòng `status: draft` → `status: stable` trong frontmatter. **Không** đổi `last_updated` (nội dung không đổi), **không** đặt `reviewed:` (việc của `/review-node` hoặc người dùng), không chạm thân bài.

**3. Chạy lại `--all`**, phải sạch.

**4. Ghi 1 mục vào cuối `log.md`** (§12): `## [<giờ>] promote | <số trang> trang lên stable`, dòng dưới liệt kê tên trang (hoặc số trang nếu quá dài) và các trang bị loại kèm lý do. Giờ lấy bằng `python .claude_draft/.claude/hooks/validate_wiki_page.py --now`.

## Sai lầm thường gặp

- Tự promote vì "lint đã sạch" mà chưa có người duyệt → `stable` mất nghĩa.
- Nâng `last_updated` khi promote → hook đòi chú thích §7.5 dù nội dung không đổi, và tiêu chí stale bị lệch.
- Thêm link cho trang thiếu backlink ngay trong lượt promote → đó là sửa nội dung, phải là lượt riêng và qua lint lại.
