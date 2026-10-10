---
name: lint
description: Kiểm tra sức khoẻ wiki 02_wiki và sửa các mục người dùng duyệt — mâu thuẫn tồn đọng, claim cũ, trang mồ côi, link chết, khái niệm chưa có trang, link còn thiếu, trang trùng, khoảng trống tri thức, nguồn trong 01_sources bị thay đổi hoặc chưa kê, triage _inbox. Dùng khi người dùng muốn lint, chạy lint, kiểm tra wiki, rà soát wiki, health check, tìm trang mồ côi, kiểm tra liên kết, audit wiki, dọn dẹp wiki, xử lý báo cáo lint, hoặc khi bảng nợ đầu phiên cho thấy đã nhiều lượt ingest chưa lint.
---

# Lint — kiểm tra sức khoẻ wiki

**Đọc `00_schema.md`:** §5–§9, §11, §12.
**Dừng chờ duyệt:** bước 3, sau khi xuất báo cáo có mã mục; chỉ sửa đúng các mã người dùng duyệt.
**Ghi log:** luôn, op `lint`.

Lint nhìn cả wiki một lượt nên dễ sửa hàng loạt theo một phán đoán sai. Vì vậy mọi thay đổi đi qua báo cáo có mã mục: người dùng duyệt mã nào, lint sửa mã đó, không hơn.

## Quy trình

**1. Chạy lệnh máy.**

```bash
python .claude/hooks/validate_wiki_page.py --lint
```

Lệnh gộp `--all`, `--verify-sources`, `--coverage`, `--size`, `--style`, `--ocr` và in một bảng tổng. Cần chi tiết của dòng nào thì chạy riêng lệnh đó. `--verify-sources` báo lệch nội dung thì ghi lên đầu báo cáo: đó là vi phạm quy tắc bắt buộc 1 và lint không sửa lại nguồn.

**2. Đối chiếu 6 tiêu chí.** Quét frontmatter trước, chỉ mở thân bài trang bị flag.

| Mã | Tiêu chí | Cách phát hiện |
|---|---|---|
| `K` | Mâu thuẫn tồn đọng | `grep -l "⚠️ Conflict" 02_wiki/*.md`; nêu hai claim và hỏi người dùng chọn hướng |
| `C` | Claim cũ | trang có `reviewed` cũ hơn `last_updated`; trang chỉ có 1 source id trong khi nguồn nạp sau có trang riêng về cùng khái niệm (ứng viên merge) |
| `O` | Mồ côi, link chết, sót index | phần `--all` của bảng tổng |
| `S` | Khái niệm chưa có trang | thuật ngữ được nhắc trong thân bài của ≥ 3 trang mà chưa có trang riêng; đếm bằng `grep -li "<thuật ngữ>" 02_wiki/*.md`, theo khái niệm chứ không theo chuỗi. Trang `stub` chưa có nội dung cũng vào đây |
| `L` | Link còn thiếu, trang trùng | hai trang cùng chủ đề không link nhau; hai trang mô tả cùng một thực thể |
| `G` | Khoảng trống | chunk `do`/`chua` của `--coverage`, file nguồn chưa kê, mục `_inbox.md` ghi "wiki thiếu"; kèm **câu hỏi mới đáng hỏi** và **nguồn nên tìm thêm** |

Kích thước, văn phong, OCR không phải tiêu chí riêng: báo cáo chép số của bảng tổng và nêu tối đa 5 trang nặng nhất mỗi loại. Ứng viên `--ocr` phải mở trang xác nhận trước khi báo; tên riêng như `Paasche` là báo giả.

**3. Xuất báo cáo và dừng.** Ghi `Claude outputs/lint-<YYYY-MM-DD>-<số trang>.md` (§3). Mỗi mục có mã ổn định (`K1`, `O3`, `S2`…), trang, lý do và hướng sửa đề xuất. Hai phần kèm theo:

- **Triage `_inbox.md`**: mỗi mục còn tồn đề xuất đúng 1 trong 3 kết cục — nâng thành trang, gộp vào trang đã có, hoặc xoá (§11). Mã `I1…`.
- **Câu hỏi mới và nguồn nên tìm**: 3–5 câu hỏi wiki hiện chưa trả lời được, và nguồn hoặc chương nào sẽ trả lời.

Trình tóm tắt trong chat, hỏi người dùng duyệt mã nào.

**4. Sửa đúng các mã đã duyệt.** Câu mới áp skill `writing-style` (profile wiki).

- `O`, `L`: chèn link vào câu kèm lý do; thêm dòng vào `index.md`. Không nâng `last_updated`.
- `S`: tạo `stub` rồi chèn link; nội dung thật là việc của `/ingest`.
- Đổi title: đổi tên file, sửa `title`, cập nhật mọi `[[wikilink]]` trỏ tới (`--backlinks <trang>` cho danh sách).
- Tách trang hoặc gộp trang trùng: giữ nguyên claim và chú thích, chỉ chuyển chỗ; trang bị gộp thì cập nhật mọi link trỏ tới rồi mới xoá. Xoá file phải được người dùng xác nhận riêng.
- `K`: ghi theo đúng lựa chọn của người dùng, bỏ dấu `⚠️ Conflict`; không tự chọn bên.
- `C`: không sửa ở đây; chuyển danh sách cho `/review-node` hoặc `/ingest`.
- `G`: đăng ký file nguồn chưa kê vào bản kê (§10); phần còn lại chỉ báo cáo.
- `I`: thực hiện kết cục đã duyệt, xoá dòng khỏi `_inbox.md`.

Sửa xong chạy `--all`, phải sạch cho các trang đã chạm.

**5. Ghi 1 mục vào cuối `log.md`** (§12): `## [<giờ>] lint | <số trang> trang`, tối đa 3 dòng: số mục theo mã, mã đã sửa, đường dẫn báo cáo. Giờ lấy bằng `--now`. Lượt chỉ báo cáo, chưa sửa gì, vẫn ghi log.

## Lưu ý

- Đếm backlink bằng `--backlinks <trang>`, không grep tay: `[[...]]` bị grep hiểu là bracket expression và bỏ sót dạng `[[trang|nhãn]]`.
- Không sửa mục chưa được duyệt, kể cả lỗi thấy rõ khi đang mở trang; ghi thêm vào báo cáo.
- Wiki vượt khoảng 600 trang: lượt quét frontmatter có thể giao subagent khi người dùng cho phép.
