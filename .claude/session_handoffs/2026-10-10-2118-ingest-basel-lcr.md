# Handoff — ingest `basel_lcr`: LCR10, LCR20, LCR30 phần chính, mục định nghĩa LCR40

## Kết quả

- Đã commit và push: `fa079d9` trên `main`, `origin/main` đồng bộ, working tree sạch.
- Nguồn mới `basel_lcr` (`01_sources/basel/LCR/LCR.md`, 274.583 byte, 1.421 dòng): thêm dòng vào bảng Source id và mục riêng trong `03_state/_sources_manifest.md`; tạo `03_state/basel_lcr.md` với 9 chunk.
- Lượt 1 (LCR10 + LCR20): 15 trang mới và stub `principles-for-sound-liquidity-risk-management-and-supervision`. Trang gốc: `liquidity-coverage-ratio-lcr`, `high-quality-liquid-assets-hqla`, `total-net-cash-outflows`.
- Lượt 2 (LCR30 + LCR40 d.701–720): 11 trang mới (`level-1-assets`, `level-2a-assets`, `level-2b-assets`, trần 40%/15%, số điều chỉnh, đặc tính HQLA, `hqla-operational-requirements`, `unencumbered-assets`, RCLF, `total-expected-cash-outflows`, `total-expected-cash-inflows`), stub `alternative-liquidity-approaches`, merge vào 4 trang của lượt 1.
- Backlink chèn vào câu có sẵn của `liquidity-risk`, `liquidity-regulation-and-central-bank-operations-arbitrage`, `regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp`; không nâng `last_updated`.
- `log.md`: 2 mục `ingest` (21-09-21, 21-17-05).
- Xác nhận được trong phiên thật hai điểm của handoff trước: hook `SessionStart` tự nạp handoff đầu phiên; danh sách skill không còn `engineering:*`, `design:*`, `harness`. Subagent `source-verifier` có trong danh sách agent, chưa chạy thử.

## Kiểm tra đã chạy

- `--all` (sau lượt 2): 826 trang, 0 trang có vấn đề, 0 mồ côi, 0 sót index.
- `--coverage basel_lcr`: phủ 2 (LCR10, LCR20), dở 2 (LCR30 80%, LCR40 cụm A 3%), chưa 4, miễn 1.
- `--size`: 3 trang mới vượt 250 từ/đoạn do danh sách đánh số; đã chèn dòng trống giữa các mục bằng script, chạy lại không còn báo.
- `--style`: 5 cờ trên trang lượt 1 đã sửa; lượt 2 không có cờ trên trang mới.
- `--verify-sources`: exit 2 — 220 file trong bản kê, 18 lệch/thiếu, 10 file `.md`/`.pdf` chưa kê.
- Chưa chạy: `--lint`, 3 eval của `research`, thử rule `deny` trên `01_sources/`.

## Blocker

- `⚠️ Conflict` trên `level-2a-assets` chờ người dùng xử lý: Basel 30.43 ghi xếp hạng tối thiểu AA− (`basel_lcr`, d.291–292), Bindseil ghi AA (`bindseil_monetary_policy`, Ch.16, d.3664).
- `01_sources/basel/` và `01_sources/vietnam-regulator/alm/` đã đổi cấu trúc so với bản kê; chờ người dùng quyết có viết lại hai mục `basel` và `vietnam_regulator` theo đĩa hay không (việc đó xoá các dòng checksum cũ).

## Việc còn lại

Từ phiên này:

- `basel_lcr` LCR30 còn bốn đoạn chưa có trang: 30.26 (thanh khoản trong ngày), 30.28 (giữ thêm 30 ngày khi tài sản mất tư cách HQLA), 30.29 (đa dạng hoá kho), 30.47 (ngân hàng Shari'ah). `--coverage` chỉ báo mục Shari'ah; ba đoạn kia phải nhớ tay.
- LCR40 cụm A (d.701–1185) còn 9 mục run-off; cụm B (dòng vào, d.1186–1324), LCR31, LCR90, LCR99 chưa đọc. Hai trang `total-expected-cash-outflows` và `total-expected-cash-inflows` mới có định nghĩa chung.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; bản trong `BaselFramework.md` cũng vậy. Trang trần 40%/15% dùng công thức dựng lại từ lời văn 30.35–30.39 và ghi rõ; cần đối chiếu bản gốc trên bis.org khi review.
- Câu minh hoạ ngoài nguồn, đã ghi rõ trong trang: ví dụ 150/100 (trang hạn chế chuyển thanh khoản), HQLA nội tệ với dòng ra USD (trang đồng tiền), ví dụ 60/50 (trang trần), repo 7 ngày (trang số điều chỉnh), "HQLA ít nhất 25% dòng ra" (trang dòng vào), chênh phí 25 điểm cơ bản (trang RCLF). Người dùng chưa nói giữ hay bỏ.
- `--verify-sources`: 11 file `basel/*.md` trong bản kê không còn trên đĩa (gồm `bcbs238.md`, `bcbs144.md`, `bcbs155.md`, `insights59.md`, các hướng dẫn EBA/ECB); chưa kê `basel/BaselFramework/`, `IRRBB-d368/`, `LEV/`, `NSF/`; `vietnam-regulator/alm/` 6 thiếu và 6 chưa kê; 1 file Clippings lệch byte (`ALM P10 UpdateTT50 (P3)...`, 6.219 so với 6.193).
- `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest file đó cần ghi `bỏ qua` cho phần trùng.
- Chưa kiểm hook `PreToolUse` cho `--guard-sources` đã được cấu hình trong `settings.json` hay chưa; code guard có trong `validate_wiki_page.py`.
- Trang `liquidity-regulation-and-central-bank-operations-arbitrage` gộp nhiều ý với tiêu đề in đậm giả heading; phần định nghĩa LCR và HQLA ở đó giờ trùng với các trang mới.

Chép từ handoff trước, chưa xử lý:

- Lệnh shell vẫn ghi được vào `01_sources/`; chưa có hook `PreToolUse` trên `Bash|PowerShell` (xem mục chưa kiểm ở trên).
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json` (nơi đã có `finance@synced: false`).
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; ví dụ map FTP ghi 37 node, `02_wiki/` hiện còn 6 trang có `ftp` trong tên. Cần quét lại trước khi dùng.
- `lint` và `promote` chưa có evals.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn 247 mục chưa phủ (during 74, choudhry 74, cargill 37, clippings 31, tata 15, bindseil 12, imf 4). Quyết định [2026-09-26] là hạ các chunk này về `[~]`; chưa ingest bù, chưa đổi `03_state/`.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6` (patch conflict, một số thay thế lệch nghĩa); mới sửa tay 4 trang ở `f966870`. Chờ người dùng quyết.
- `--style` báo 319/790 trang, `--size` 154 trang, 70% tag dùng 1 lần: tín hiệu thô cho lượt lint sau.
- `.claude/docs/luong-van-hanh.html` còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- `ingest/SKILL.md:13` ghi "(§1–§12)".
- `00_schema.md` §4 có hai hàng cùng tên "Kích thước 1 trang".
- `00_schema.md`, skill và docstring hook vẫn dùng dạng `§7.5`; `CLAUDE.md` đã đổi sang "§7 luật 5".
- Docstring `.claude/hooks/validate_wiki_page.py` các dòng mô tả `--tags`, `--style` hỏng chữ, còn "luat cung 1".
- `CLAUDE.md` 999 từ, vượt mốc khoảng 950; muốn rút thì cắt câu mở đầu mục "Khởi động".
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".
- Chưa chạy 3 eval `research` bằng `skill-creator`.
- Chưa chạy thử một lượt `/query` để xem bước mồi có dẫn tới đọc §13 không.

## Bước tiếp theo

- Ingest tiếp `basel_lcr`: LCR40 cụm A theo từng khối (bán lẻ; bán buôn không bảo đảm; có bảo đảm; yêu cầu bổ sung), mỗi khối một lượt qua bước duyệt; sau đó cụm B, rồi bốn đoạn LCR30 còn lại, LCR31, LCR99.
- Người dùng xử lý `⚠️ Conflict` AA− và AA, và quyết việc viết lại hai mục bản kê lệch đĩa.
- `/review-node` cho `level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock` sau khi có công thức 30.38 từ bản gốc.
- Ingest bù các nguồn cũ theo lô; đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy` (16 mục).
