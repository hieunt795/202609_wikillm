# Handoff — áp lại quy trình research, Evergreen và coverage lên nền 6adf39e

## Kết quả

- `main` đang ở `6adf39e`, sau khi lùi về trước loạt 23 commit `abbd2cb..b8ee3d6` (còn trên `origin/main` và nhánh `review/nsfr-tt50-2026-10-02`).
- Áp lại toàn bộ phần quy trình của loạt đó, **chưa commit**, mọi thay đổi đang staged: `14423ad`, `81ca974`, `e9bcea0` (research Map → Deep read); `b4b5b2f`, `1adb5d7`, `d62c086` (Evergreen); phần quy trình của `7e9470d` (`--coverage`, đánh số lại bước ingest, 5–10 ý chính, bỏ ngưỡng dưới).
- Hook, 6 skill, `00_schema.md`, `CLAUDE.md`, `.claude/docs/luong-van-hanh.html` giờ khớp đúng bản `b8ee3d6`. `decisions.md` khớp `b8ee3d6` cộng một dòng "Áp lại 2026-10-09". `log.md` chỉ thêm 2 mục `schema` (29/09, 30/09).
- Không lấy: trang wiki ingest, `03_state/`, lượt research FTP và S5a (`97fe77b`, `13c5013`), `.obsidian/workspace.json`.

## Kiểm tra đã chạy

- `py_compile` hook: đạt. `--size`, `--tags`, `--style`, `--coverage`: chạy được.
- `--all`: 790 trang, 0 lỗi, 4 trang mồ côi — có sẵn ở `6adf39e`.
- `--verify-sources`: 36 file chưa kê — có sẵn từ trước.
- `02_wiki/`, `03_state/`, `01_sources/` không đổi.

## Việc còn lại

- `--coverage` báo 74 chunk `[x]` còn mục chưa phủ trên 7 nguồn (during 23, choudhry 13, cargill 12, clippings 11, tata 6, bindseil 5, imf 4). Quyết định [2026-09-26] là hạ các chunk này về `[~]`; việc đó nằm trong `03_state/` của loạt ingest nên chưa làm lại.
- Chưa áp 3 commit sửa văn phong trang wiki (`8c32c43`, `51d5c3c`, `b8ee3d6`): patch conflict và một số thay thế làm lệch nghĩa (vd "Theo Cargill," → "Chuẩn Cargill phát biểu rằng"; bỏ tên Friedman–Schwartz, Bernanke). Chờ người dùng quyết.
- `README.md` dòng 25 còn chữ "Luật cứng".
- `--style` báo 319/790 trang, `--size` 154 trang, 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.

## Cập nhật cuối phiên

- Đã commit phần quy trình: `944cbe5`. `git push origin main` bị từ chối (local lùi 26 commit so với `origin/main`); chưa force push, chờ người dùng xác nhận.
- Sửa văn phong tay 4 trang, chưa commit: bỏ tác giả làm chủ ngữ ở `autonomous-factors-of-central-bank-balance-sheet`, `central-bank-balance-sheet-sterilization-capacity-…`, `sterilization`; `bank-runs-investor-strikes-and-multiple-equilibria` chuyển trích dẫn về dạng §7.5. Không nâng `last_updated`. `--all` sau sửa: 790 trang, 0 lỗi.
- Cố ý không sửa: trang `the-policy-anchor-…` (so sánh khung Cargill và Bindseil, tên tác giả là nội dung), Friedman–Schwartz và Bernanke ở trang Great Depression, "Theo BPM5", "Theo Basel I".
- 74 chunk = 247 mục chưa phủ: during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4. Chưa ingest, chưa đổi `03_state/`.

## Bước tiếp theo

- Người dùng chọn cách push (force `main`, hay nhánh riêng).
- Ingest bù theo lô, mỗi lô qua bước duyệt (quy tắc bắt buộc 4); đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy` (16 mục).
