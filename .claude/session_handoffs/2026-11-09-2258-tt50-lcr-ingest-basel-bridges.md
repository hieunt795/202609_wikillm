# Handoff — ingest TT50/2026 Điều 13–21 (LCR) và cầu nối so sánh với Basel

## Kết quả

- Tách source id `tt50_2026_sbv` khỏi `vietnam_regulator`: sửa `03_state/_sources_manifest.md` (dòng bảng Source id, mục riêng, trừ 2 file TT50 khỏi mục cũ, cập nhật số KiB/dòng của `vietnam_regulator`), tạo `03_state/tt50_2026_sbv.md` (17 chunk).
- `/ingest` chunk Mục 5 cụm A (d.441–722): 8 trang mới (entity TT50; ngưỡng LCR quy VNĐ 50%→100%; hai đường đăng ký sớm; thôi tuân thủ TT22; ba loại LCR; vi phạm LCR; nguy cơ mất khả năng chi trả 90%/30 ngày; quyền khắc phục Điều 15), 4 trang `analysis` so sánh TT50–Basel (trùng khớp công thức; tính ràng buộc và báo cáo; cấp áp dụng và đồng tiền; điều kiện vận hành HQLA), 3 trang merge (`hqla-operational-requirements`, `total-net-cash-outflows`, `high-quality-liquid-assets-hqla`), 2 stub (`net-stable-funding-ratio-nsfr`, `loan-to-deposit-ratio-ldr`), 4 backlink vào trang Basel, `index.md` thêm 2 mục, `_inbox.md` thêm 2 dòng, `log.md` thêm 1 mục ingest (22-56-49).
- Không có `⚠️ Conflict`. Không ghi `bỏ qua:` nào.
- Chưa commit: 11 file sửa, 16 file mới (git status cuối phiên).

## Kiểm tra đã chạy

- `--all`: 840 trang, 0 trang có vấn đề, 0 mồ côi, 0 sót index (chạy lại sau khi sửa văn phong).
- `--coverage tt50_2026_sbv`: chunk d.441–722 `do`, còn 1 mục chưa phủ (Điều 14); chunk d.25–194 `do` (Điều 4, 5); d.1013–1132 `do` (6 mục); 13 chunk `chua`; 1 `mien`.
- `--coverage basel_lcr`: LCR30 còn 1 mục (Shari'ah); LCR40 cụm A còn 9 mục.
- `--style`, `--size` lọc theo các trang mới: không còn cờ sau khi sửa.
- `--verify-sources`: báo 220 file trong bản kê, 18 lệch/thiếu, 11 file chưa kê (TT83, VAB FTP... có từ trước). Không xử lý; chưa đối chiếu lại số này với danh sách 36 file của handoff trước.
- Chưa chạy `--lint`, chưa chạy `source-verifier`, chưa `/review-node` cho trang nào của lượt này.

## Việc còn lại

Từ phiên này:

- Điều 14 TT50 (d.475–552) chưa viết trang: khoản 1–4 (quản lý theo TT83, giả định thanh khoản khi căng thẳng, kế hoạch tài trợ dự phòng và truyền thông, đồng tiền trọng yếu), khoản 5 (phạm vi, hạn mức mùa cao điểm, số dư vượt mức tiền gửi hoạt động), khoản 6 (thanh khoản trong ngày), khoản 7 (tài sản bảo đảm), khoản 8 (quy mô HQLA), khoản 9 (stress test, dữ liệu ≥10 năm, báo cáo 30 ngày sau quý). Người dùng đã yêu cầu không bỏ qua; lượt trước dừng vì hạn 15 trang.
- Khi ingest Điều 14, bổ sung so sánh với Basel LCR30 30.26 (LCR không phủ thanh khoản trong ngày) và 30.27 (theo dõi theo đồng tiền) vào trang `tt50-binds-the-solo-vnd-equivalent-lcr-while-basel-applies-a-consolidated-ratio-in-one-reporting-currency` hoặc trang mới.
- Các so sánh Basel–TT50 chưa làm được: giá trị hệ số run-off và hệ số thu tiền (Phụ lục I phần B, C); quy tắc rổ bảo đảm và tài sản bị ràng buộc một phần (Phụ lục I phần A).
- Chunk TT50 chưa ingest: Điều 4–5, Điều 22–27 (NSFR, phái sinh, công bố), Phụ lục I–IV, Điều 6–12, 28–29, 30–38; Điều 19 chỉ mới merge ở mức phân loại.
- Quyết ở lượt lint: mục `_inbox.md` [2026-10-10] về ngoại lệ ingest văn bản quy phạm (mỗi điều một node); lượt này đã ingest TT50 như nguồn thường.
- Cân nhắc `/review-node` cho 4 trang `analysis` và trang ngưỡng 90% (có đoạn suy ra từ công thức Điều 16, đã ghi rõ trên trang).

Chép từ handoff `2026-10-10-1452-deny-sources-handoff-skill.md`, chưa xử lý (một số mục có thể đã cũ, chưa kiểm lại trong phiên này):

- Lệnh shell vẫn ghi được vào `01_sources/`; chưa có hook `PreToolUse` trên `Bash|PowerShell`.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json` (nơi đã có `finance@synced: false`).
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; ví dụ map FTP ghi 37 node, `02_wiki/` hiện còn 6 trang có `ftp` trong tên. Cần quét lại trước khi dùng.
- `lint` và `promote` chưa có evals.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ (during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4). Quyết định [2026-09-26] là hạ các chunk này về `[~]`; chưa ingest bù, chưa đổi `03_state/`.
- `--verify-sources` (chạy 2026-10-09): 36 file trong `01_sources/` chưa kê trong manifest.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6` (patch conflict, một số thay thế lệch nghĩa); mới sửa tay 4 trang ở `f966870`. Chờ người dùng quyết.
- `--style` báo 319/790 trang, `--size` 154 trang, 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
- `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- `ingest/SKILL.md:13` ghi "(§1–§12)".
- `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; `CLAUDE.md` đã đổi sang "§7 luật 5".
- Docstring `.claude/hooks/validate_wiki_page.py` các dòng mô tả `--tags`, `--style` hỏng chữ, còn "luat cung 1".
- `CLAUDE.md` 999 từ, vượt mốc khoảng 950; muốn rút thì cắt câu mở đầu mục "Khởi động".
- Mở phiên mới để xác nhận: handoff tự hiện đầu phiên (đã thấy hoạt động ở phiên này); danh sách skill không còn `engineering:*`, `design:*`, `harness`; yêu cầu sửa thử một file trong `01_sources/` bị từ chối; "dùng source-verifier kiểm trang cpi" chạy được. Chạy 3 eval `research` bằng `skill-creator`. Chạy thử một lượt `/query` xem bước mồi có dẫn tới đọc §13 không.
- Ingest bù theo lô, mỗi lô qua bước duyệt; đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy` (16 mục).

## Bước tiếp theo

- Người dùng xem `git diff` rồi quyết định commit lượt TT50 (27 file).
- `/ingest TT50 - LCR` tiếp: Điều 14 trước, sau đó Điều 22–27 (NSFR) hoặc Phụ lục I phần A theo ý người dùng.
