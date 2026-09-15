# LLM Wiki — Macroeconomics

Một wiki tri thức do LLM biên soạn và bảo trì, xây trên hai kiến trúc tham chiếu:

- **[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (Andrej Karpathy) — mô hình 3 lớp nguồn/wiki/schema, ba operation ingest · query · lint (dự án thêm promote để quản vòng đời trang và review để đối chiếu trang với nguồn). LLM là người biên tập giữ một cơ sở tri thức tích luỹ, thay cho việc RAG lại từ đầu mỗi lần hỏi.
- **[Evergreen notes](https://notes.andymatuschak.org/z5E5QawiXCMbtNtupvxeoEX)** (Andy Matuschak) — nguyên tắc thiết kế từng trang: atomic, hướng khái niệm, liên kết dày, ontology liên tưởng, viết cho chính mình.

Chủ đề hiện tại: kế toán và phân tích vĩ mô (hạch toán quốc gia, lạm phát, lao động, case chuyển đổi Ba Lan).

## Bố cục

| Thư mục | Vai trò | Quyền |
|---|---|---|
| `01_sources/` | Tài liệu gốc | Chỉ đọc — bất biến, **không có trong kho này** |
| `02_wiki/` | Trang wiki | Agent sở hữu, cấu trúc phẳng |
| `03_state/` | Trạng thái ingest + xuất xứ nguồn | Agent sở hữu, máy đọc được |
| `00_schema.md` | Mô hình dữ liệu & quy tắc | Người + agent đồng tiến hoá |

`02_wiki/index.md` để điều hướng · `log.md` là nhật ký append-only mỗi operation (`grep "^## \[" log.md`) · `decisions.md` ghi lý do các quyết định thiết kế · `_inbox.md` chứa ý tưởng chưa đủ chín.

## Đọc từ đâu

| Muốn biết | Đọc |
|---|---|
| Quy tắc trang wiki, taxonomy, ngưỡng, vòng đời | `00_schema.md` |
| Tổng quan vận hành cho người đọc | `agents.md` |
| Quy trình thực thi từng operation | `.claude/skills/{ingest,query,lint,promote,review}/SKILL.md` |
| Nhắc nhanh + luật cứng | `CLAUDE.md` |

Mỗi lần ghi file trong `02_wiki/`, hook `.claude/hooks/validate_wiki_page.py` tự kiểm frontmatter, luật không-heading, link chết và chú thích vị trí. `python .claude/hooks/validate_wiki_page.py --all` quét toàn bộ và bắt thêm trang mồ côi.

## Vì sao không có `01_sources/`

Nguồn là tài liệu của bên thứ ba (ấn phẩm IMF có bản quyền), kho này chỉ phát hành phần wiki do dự án tự viết — mọi trang đều là chữ viết lại, không trích nguyên văn.

Chú thích vị trí trong trang wiki trỏ tới **số dòng** của file nguồn, nên vẫn kiểm chứng được: `03_state/_sources_manifest.md` ghi nhan đề, nơi xuất bản và SHA-256 của từng file. Tự lấy bản gốc, đặt đúng đường dẫn, đối chiếu checksum là số dòng khớp tuyệt đối.

## Trạng thái

Số trang và phần nguồn đã nạp: `02_wiki/index.md` (mục `## Sources`). Hiện đã ingest Chương 2 của nguồn IMF. Lịch sử audit: các mục `lint` trong `log.md` (`grep "^## \[.*\] lint" log.md`); khoản nợ kỹ thuật đang mở: `_inbox.md`.

Bản ingest Chương 1 + 3 (117 trang) đã được rollback và lưu ở tag `ch3-snapshot`.
