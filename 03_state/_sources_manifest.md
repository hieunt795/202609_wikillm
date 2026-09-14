---
type: sources-manifest
last_updated: 2026-09-14
---

Xuất xứ và checksum của các nguồn trong `01_sources/`.

`01_sources/` **không được commit** (xem `.gitignore`): đó là tài liệu của bên thứ ba, kho này chỉ phát hành phần wiki do dự án tự viết. File này tồn tại để một bản clone vẫn kiểm chứng được mọi chú thích vị trí (`00_schema.md` §7.5) và bản đồ chunk trong `03_state/`: chú thích trỏ tới số dòng của file nguồn, nên chỉ cần bản bạn tự lấy có đúng SHA-256 dưới đây thì số dòng khớp tuyệt đối.

Muốn dựng lại môi trường đầy đủ: tự lấy bản gốc từ nhà xuất bản, đặt đúng đường dẫn ở cột *Đường dẫn*, rồi đối chiếu `sha256sum`.

## imf_macro_accounting

| | |
|---|---|
| Nhan đề | *Macroeconomic Accounting and Analysis in Transition Economies* |
| Tác giả | Abdessatar Ouanes, Subhash Thakur — với đóng góp của Ian Lienert, Philippe Marciniak, Karen Swiderski |
| Xuất bản | International Monetary Fund, tháng 6/1997 — © 1997 International Monetary Fund |
| Phân loại | Nguồn dài (`00_schema.md` §10) |
| Tiến độ ingest | `03_state/imf_macro_accounting.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md` | 849.006 | 6.065 | `13db03df3dd8e2b2dfdaf352dedc2b9c005700dcd0a86fcaf92063d697182859` |
| `01_sources/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.pdf` | 13.141.692 | — | `185f77f9524bc162c460eccb357dcbd0342b175e18b3c8593be8e347122e9310` |

File `.md` là bản OCR của PDF và là bản mà mọi chú thích vị trí trỏ tới. Bản OCR có lỗi thật (`Waaes`, `lmbalance`, `tO`, `1 993`…) — đây là lý do lint có tiêu chí *Nhiễu OCR còn sót*.

## Modern Money Mechanics

| | |
|---|---|
| Nhan đề | *Modern Money Mechanics* |
| Xuất bản | Federal Reserve Bank of Chicago |
| File gốc | `frbchi_modernmoneymechanics_1961.pdf`, 31 trang |
| Phân loại | Nguồn ngắn (`00_schema.md` §10) — không cần file trạng thái |
| Tiến độ ingest | Chưa ingest (`02_wiki/index.md` §Sources) |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/Modern Money Mechanics/Modern Money Mechanics.md` | 84.768 | 721 | `c26b222a173146511d25243f4aee44d38ea3806a265e7f076b89496c3af65b38` |

Thư mục còn 16 file phụ do bước OCR sinh ra (`Modern Money Mechanics.json` + 15 ảnh `_page_*.jpeg`) — là vật liệu nguồn, không phải file do agent tạo.
