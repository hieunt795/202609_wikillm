---
name: ingest-legal
description: Nạp văn bản quy phạm pháp luật (thông tư, nghị định, luật, quyết định) từ file .docx trong 01_sources thành trang `provision` — mỗi Điều một trang, mỗi khoản/điểm/tiết một block ID, nguyên văn giữ đúng chữ, dẫn chiếu nội bộ thành link. Dùng khi người dùng muốn node hoá, tra chính xác điều khoản, hoặc viết chú giải cho trang điều khoản. Nguồn không phải văn bản quy phạm thì dùng /ingest.
---

# Ingest-legal — nạp văn bản quy phạm thành trang điều khoản

Luật của trang `provision` ở `00_schema.md` §13; đọc §13 cùng §1, §3, §10, §12 trước khi chạy. Khác `/ingest`: đơn vị là điều khoản, nội dung chính là nguyên văn, và nguyên văn do script sinh chứ không do model viết.

## Công cụ

`python .claude/hooks/legal_docx.py <docx> <lệnh>` — chỉ đọc nguồn. Gọi tắt `L` bên dưới; `--short <tiền tố tên trang>` và `--sid <source id>` bắt buộc với lệnh ghi.

| Lệnh | Việc |
|---|---|
| `--tree [<địa chỉ>]` | Cây địa chỉ, số Điều/khoản/điểm/tiết, điểm nghi vấn (số nhảy cóc, địa chỉ trùng), cảnh báo chưa có số hiệu |
| `--refs [<địa chỉ>]` | Dẫn chiếu: nội bộ giải được · chưa giải được (`??`) · văn bản ngoài |
| `--check-formulas` | Tử/mẫu mỗi phân số trong LaTeX khớp XML gốc |
| `--nodes` · `--node <địa chỉ>` | Danh sách trang; in thử một trang |
| `--write 02_wiki` | Ghi mọi trang + mục lục; giữ chú giải đã viết |
| `--state 02_wiki` | Bảng node cho state file |
| `--verify 02_wiki` | Từng trang = bản sinh từ nguồn; link `#^id`; node thiếu trang; khối ngoài mọi trang |

## Quy trình — nạp nguyên văn

**1. Xác định nguồn.** File `.docx` trong `01_sources/`. Chỉ có `.pdf`/`.md` → dừng, báo người dùng cần bản `.docx` (không tự chuyển đổi, không ghi vào `01_sources/`). Chọn `source id` (snake_case) và `short` (kebab, vd `tt50-2026`); `short` là tiền tố tên mọi trang nên phải chưa có trang nào dùng (`ls 02_wiki | grep "^<short>"`).

**2. Khảo sát — chưa ghi gì.**

```bash
L="python .claude/hooks/legal_docx.py <docx>"
$L --tree | tail -20      # thống kê + điểm nghi vấn
$L --refs                 # dòng ?? = dẫn chiếu chưa giải được
$L --check-formulas
```

**3. Trình người dùng duyệt — dừng.** Trình: số Điều/khoản/điểm/tiết/bảng/công thức; số trang sẽ tạo (`--nodes`); từng điểm nghi vấn và từng dẫn chiếu `??` kèm nguyên văn chỗ đó; công thức lệch; trạng thái văn bản (đã có số hiệu, ngày chưa); 1–2 trang in thử (`--node`). Điểm nghi vấn do văn bản gốc (đánh số nhảy cóc thật) thì ghi vào state file; do script đọc sai thì **sửa script, không sửa trang**. Chờ xác nhận. Lượt không có người → ghi tóm tắt vào `_inbox.md` và dừng.

**4. Đăng ký nguồn.** Thêm vào `03_state/_sources_manifest.md`: dòng bảng Source id (Nguồn dài, state file) và mục riêng (nhan đề, cơ quan ban hành, số hiệu/ngày hoặc "chưa có số hiệu", bảng đường dẫn · bytes · `—` · SHA-256 cho `.docx`; file `.pdf`/`.md` cùng thư mục kê kèm, ghi rõ không dùng làm nguồn tham chiếu). Thêm dòng vào `02_wiki/index.md` §Sources. Văn bản thay thế/sửa đổi văn bản đã có trong wiki → ghi quan hệ ở mục bản kê.

**5. Ghi và đối chiếu.**

```bash
$L --write 02_wiki --short <short> --sid <source id> --tags "<tag1>, <tag2>"
$L --verify 02_wiki                                  # phải: 0 lệch, 0 link chết, 0 node thiếu, 0 khối ngoài
python .claude/hooks/validate_wiki_page.py --all      # ghi bằng shell nên hook không tự chạy
python .claude/hooks/validate_wiki_page.py --verify-sources
```

Tag: kiểm bằng `validate_wiki_page.py --tags` trước; dùng tag có sẵn của cơ quan ban hành + tag `<short>`.

**6. State, index, log.** Tạo `03_state/<source id>.md` theo §13 (bảng từ `$L --state 02_wiki ...`). Cập nhật dòng §Sources và thêm mục văn bản vào mục lục `index.md` (link tới trang `<short>`). Ghi một mục `log.md`: `## [<--now>] ingest | <source id> — nguyên văn, <N> trang provision`.

## Quy trình — viết chú giải (lượt riêng, khi người dùng yêu cầu)

1. Người dùng chỉ định node hoặc cụm (≤ 15 node/lượt). Đọc trang và các trang nó dẫn tới.
2. Gọi skill `writing-style` (profile wiki). Viết ≤ 150 từ thay cho `(chưa viết)` dưới dòng *Chú giải*: quy định nói gì khi gộp các khoản, nối với điều nào; dẫn khoản bằng `k4`, `k5.b`. Nhận định ngoài văn bản phải nói rõ là diễn giải. Trang khái niệm liên quan đã có trong wiki → link trong câu kèm lý do.
3. **Chỉ sửa phần dưới dòng *Chú giải*.** Không đổi nguyên văn, block ID, link, hai danh sách tham chiếu. Không nâng `last_updated`.
4. `$L --verify 02_wiki` + `validate_wiki_page.py --all`; cập nhật cột *Chú giải* ở state file; một mục `log.md` (`ingest | <source id> — chú giải <N> node`).

## Khi nguồn đổi

`--verify` báo "SHA nguồn trong trang khác file hiện tại" → file `.docx` đã bị thay. Không tự ghi đè: chạy `--tree`/`--refs` trên bản mới, trình khác biệt (số điều, khối lệch), chờ người dùng quyết; sau đó `--write` (chú giải được giữ), cập nhật SHA ở bản kê và state file.

## Sai lầm thường gặp

- **Sửa tay nguyên văn hoặc link** → `--verify` báo "khác bản sinh từ nguồn". Sai ở đâu sửa ở script.
- **Dùng bản `.md` chuyển từ PDF** → công thức mất, đánh số hỏng (`6. đ)`), số hiệu văn bản mất gạch nối.
- **Đọc phẳng công thức** → `15/85` thành "1585". Luôn chạy `--check-formulas`; gộp chữ trong công thức chỉ trong cùng một cấp, không xuyên qua phân số.
- **Điều khoản sửa đổi văn bản khác** (vd "Sửa đổi, bổ sung Điều 2 Thông tư số … như sau: “…”"): đoạn trong ngoặc kép là văn bản khác — script xếp thành khối `q<n>`, không tách khoản/điểm, không link. Thấy khoản/điểm trùng địa chỉ ở `--tree` thì kiểm ngoặc kép trước.
- **Trích dẫn liệt kê** ("khoản 5 Mục I; khoản 2 Mục II và khoản 2 Mục IV Phần A Phụ lục I"): phần đuôi áp cho cả dãy.
- **"Phụ lục I Thông tư số …"** là phụ lục của văn bản khác, không phải của văn bản đang nạp.
- **Điền số hiệu/ngày cho văn bản chưa có** → sai sự thật; ghi `doc_status`.
- **Tự suy link cho thuật ngữ định nghĩa** (vd "Tổng Nợ phải trả bình quân" → khoản 13 Điều 3) trong nguyên văn → chỉ dẫn chiếu tường minh mới thành link; quan hệ suy ra đặt ở chú giải.
- **Ghi bất cứ file nào vào `01_sources/`** → vi phạm quy tắc bắt buộc 1.

## Xử lý lỗi

`--verify` hoặc `--all` còn lỗi sau bước 5: **dừng**, không ghi log, không commit; báo danh sách trang đã ghi. Không tự xoá trang hay `git checkout` để làm lại — việc huỷ do người dùng quyết định.
