---
name: handoff
description: Tạo handoff cuối phiên trong .claude/session_handoffs/ và chép lại việc tồn còn mở từ handoff trước. Chỉ chạy khi người dùng gọi /handoff.
disable-model-invocation: true
---

# Handoff — ghi trạng thái cuối phiên

Luật gốc: `.claude/rules/session-handoff.md`. Skill này chỉ là quy trình thực thi; handoff không thay `log.md`, state, manifest hay `decisions.md`.

**Phiên không đổi repo hoặc trạng thái vận hành thì không tạo handoff.** Báo lại người dùng và dừng.

## Quy trình

**1. Gom dữ kiện của phiên** — không dựa vào trí nhớ hội thoại:

```bash
git status --short
git diff --stat
python .claude/hooks/validate_wiki_page.py --now
```

Đọc các mục `log.md` ghi trong phiên này (cuối file) và handoff mới nhất trong `.claude/session_handoffs/`.

**2. Chuyển tiếp việc tồn.** Với từng mục ở *Việc còn lại* của handoff mới nhất: phiên này đã làm xong thì bỏ, chưa xong thì **chép lại nguyên nội dung** vào handoff mới. Không viết "việc tồn từ handoff X không đổi": handoff mới nhất phải tự đủ để phiên sau không đọc ngược. Handoff trước trỏ tiếp sang handoff cũ hơn thì đọc theo chuỗi một lần, chép hết các mục còn mở, để chuỗi dừng ở đây.

**3. Ghi đúng một file mới** `.claude/session_handoffs/YYYY-MM-DD-HHmm-<short-slug>.md`, giờ lấy từ `--now`. Không sửa, không ghi đè handoff cũ. Khung:

```markdown
# Handoff — <việc chính của phiên>

## Kết quả
## Kiểm tra đã chạy
## Việc còn lại
## Bước tiếp theo
```

Thêm `## Blocker` khi có việc đang kẹt chờ người dùng hoặc chờ nguồn. *Kiểm tra đã chạy* ghi lệnh kèm kết quả đếm được (ví dụ `--all`: 790 trang, 0 lỗi); lệnh chưa chạy thì ghi là chưa chạy. *Kết quả* nêu rõ đã commit hay chưa.

**4. Không ghi `log.md`.** Handoff không phải operation (§12).

## Sai lầm thường gặp

- Chép transcript, output dài hoặc cả diff vào handoff → handoff chỉ giữ kết luận.
- Ghi lập luận của quyết định vào handoff → lý do nằm ở `decisions.md`.
- Ghi "đã kiểm" cho lệnh chạy ở phiên trước → chỉ ghi lệnh chạy trong phiên này.
