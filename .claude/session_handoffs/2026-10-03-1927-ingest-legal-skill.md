# Handoff 2026-10-03 19:27 — skill `/ingest-legal`

## Kết quả

- Skill mới `.claude/skills/ingest-legal/SKILL.md`: nạp văn bản quy phạm từ `.docx` thành trang `type: provision` (1 Điều hoặc 1 Mục phụ lục = 1 trang; khoản/điểm/tiết = block ID `^d12-k4-a-iv`; nguyên văn; dẫn chiếu nội bộ thành link; chú giải viết lượt riêng).
- Script mới `.claude/hooks/legal_docx.py`: `--tree`, `--refs`, `--check-formulas`, `--nodes`, `--node`, `--write`, `--state`, `--verify`.
- Hook `validate_wiki_page.py`: nhận `provision`; `link_targets` cắt `#^id`; kiểm block ID chết; `--size`/`--style` bỏ qua `provision`; `--verify-sources` tính `.docx`.
- `00_schema.md` §1–§4 + §13 mới; `CLAUDE.md` (bảng operation, công cụ); `decisions.md`; `log.md` (1 mục `schema`).
- Chưa commit. Chưa ghi trang nào vào `02_wiki/`.

## Kiểm tra đã chạy

- Bản sao wiki ở scratchpad + TT50/2026 (`.docx`): 68 trang, 1.014/1.014 khối khớp nguồn, 0 link chết, 0 node thiếu; 348 dẫn chiếu nội bộ giải được, 0 chưa giải, 50 văn bản ngoài; 12/12 công thức khớp phân số; `--all` trên bản sao: 1.101 trang, 0 vấn đề, 0 mồ côi.
- Phép thử âm: sửa một chữ nguyên văn, đổi đích link sang block ID không tồn tại, đổi đích sang block ID khác còn tồn tại — đều bị bắt; chú giải được giữ khi `--write` lại.
- Repo thật: `--all` giống hệt trước khi sửa hook (1.033 trang, 0 vấn đề). `--verify-sources` báo thêm `TT50_2026_SBV.docx` chưa kê (đúng kỳ vọng).

## Chưa kiểm

- Hiển thị trong Obsidian: công thức LaTeX, bấm link `#^id`, link trong ô bảng (`\|`).
- Công thức chưa so bằng mắt với bản `.pdf`.
- Script mới thử trên một văn bản (TT50); văn bản có cấu trúc khác (Luật có Chương/Mục/Tiểu mục, nghị định có phụ lục biểu mẫu) có thể cần chỉnh mẫu nhận dạng.

## Việc còn lại

1. Người dùng gọi `/ingest-legal` cho `01_sources/vietnam-regulator/alm/TT50_2026_SBV/TT50_2026_SBV.docx` (`--short tt50-2026 --sid sbv_tt50_2026`): đăng ký bản kê + `index.md`, `--write 02_wiki`, state file, log.
2. Viết chú giải theo yêu cầu (≤ 15 node/lượt).
3. Commit khi người dùng yêu cầu.

## Lưu ý

- File `.docx` TT50 chưa điền số hiệu/ngày ban hành → ghi `doc_status`, không tự điền.
- Nhánh `review/nsfr-tt50-2026-10-02` đang ở `b8ee3d6`; các trang khái niệm `sbv-*` của TT50 và `03_state/sbv_tt50_2026.md` không còn trong thư mục làm việc (không do phiên này). Các commit ingest cũ vẫn có trong lịch sử git (`aadb8bf`, `5515fc4`, …).
- 26 file `.md`/`.pdf` khác trong `01_sources/` chưa kê từ trước, không thuộc phạm vi phiên này.
- Thư mục nguồn TT50 có file khoá `~$50_2026_SBV.docx` của Word; hook bỏ qua file `~$*`.
