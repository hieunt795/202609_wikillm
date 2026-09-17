# LLM Wiki — Macroeconomics

Một wiki tri thức do LLM biên soạn và bảo trì, xây trên hai kiến trúc tham chiếu:

- **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (Andrej Karpathy) — mô hình 3 lớp nguồn/wiki/schema, ba operation ingest · query · lint. Dự án thêm promote để quản vòng đời trang và review-node để đối chiếu trang với nguồn. LLM là người biên tập giữ một cơ sở tri thức tích luỹ, thay cho việc RAG lại từ đầu mỗi lần hỏi.
- **[Evergreen notes](https://notes.andymatuschak.org/z5E5QawiXCMbtNtupvxeoEX)** (Andy Matuschak) — nguyên tắc thiết kế từng trang: atomic, hướng khái niệm, liên kết dày, ontology liên tưởng, viết cho chính mình.

Chủ đề: kinh tế vĩ mô, tiền tệ, ngân hàng và thị trường thu nhập cố định.

## Bố cục

| Thư mục | Vai trò | Quyền |
|---|---|---|
| `01_sources/` | Tài liệu gốc | Chỉ đọc — bất biến, **không có trong kho này** |
| `02_wiki/` | Trang wiki | Agent sở hữu, cấu trúc phẳng |
| `03_state/` | Bản kê nguồn + trạng thái ingest | Agent sở hữu, máy đọc được |
| `00_schema.md` | Mô hình dữ liệu & quy tắc | Người + agent đồng tiến hoá |

`02_wiki/index.md` để điều hướng · `log.md` là nhật ký append-only mỗi operation (`grep "^## \[" log.md`) · `decisions.md` ghi lý do các quyết định thiết kế · `_inbox.md` chứa ý tưởng chưa đủ chín.

## Đọc từ đâu

| Muốn biết | Đọc |
|---|---|
| Luật cứng, bảng operation, công cụ kiểm | `CLAUDE.md` |
| Quy tắc trang wiki, taxonomy, ngưỡng, vòng đời | `00_schema.md` |
| Quy trình thực thi từng operation | `.claude/skills/{ingest,query,lint,promote,review-node}/SKILL.md` |
| Vì sao một luật tồn tại | `decisions.md` |

Hook `.claude/hooks/validate_wiki_page.py` tự kiểm mỗi lần ghi file trong `02_wiki/`; `--help` liệt kê các lệnh quét toàn bộ.

## Vì sao không có `01_sources/`

Nguồn là tài liệu của bên thứ ba có bản quyền (IMF, Oxford UP, Cambridge UP, Wiley, Springer, University of Chicago Press, Federal Reserve Bank of Chicago). Kho này chỉ phát hành phần wiki do dự án tự viết: mọi trang đều là chữ viết lại, không trích nguyên văn.

`03_state/_sources_manifest.md` ghi nhan đề, nơi xuất bản, số byte, số dòng và SHA-256 của từng file. Chú thích vị trí trỏ tới số dòng của file `.md` do luồng chuyển đổi PDF bên ngoài dự án tạo ra, nên chỉ kiểm chứng tuyệt đối được với đúng file `.md` đó; hash PDF dùng để đối chiếu bản gốc.

## Trạng thái

Số trang và tiến độ từng nguồn: `02_wiki/index.md` (mục `## Sources`). Lịch sử lint: `grep "^## \[.*\] lint" log.md`. Khoản nợ kỹ thuật đang mở: `_inbox.md`.

Tag `ch3-snapshot` giữ bản ingest Chương 1 + 3 (117 trang) đã rollback ngày 2026-09-15.
