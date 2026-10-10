# Handoff — chặn ghi `01_sources/`, skill `/handoff`, hook `SessionStart`, subagent, evals

## Kết quả

- `.claude/settings.json`: `permissions.deny` cho `Edit(/01_sources/**)` và `Write(/01_sources/**)`; thêm hook `SessionStart` (matcher `startup|clear`) gọi `validate_wiki_page.py --session-start`. Hook `PostToolUse` giữ nguyên.
- `.claude/hooks/validate_wiki_page.py`: lệnh mới `--session-start` in handoff mới nhất, luôn exit 0.
- Skill mới `.claude/skills/handoff/SKILL.md`, chỉ người dùng gọi: chép lại nguyên việc tồn còn mở.
- Subagent mới `.claude/agents/source-verifier.md`: `Read, Grep, Glob`, model `sonnet`, chỉ trả bảng đối chiếu claim với nguồn. Không skill nào gọi nó tự động.
- `.claude/skills/research/evals/evals.json`: 3 eval (Map chủ đề repo; Deep read `required-reserves` từ Bindseil Ch.8; enrich `cpi` bị chặn bởi chunk IMF Ch.1 `[ ]`).
- `.claude/settings.local.json` (mới, ngoài git): tắt `github`, `harness`, `engineering`, `design`, `cowork-plugin-management` cho project này.
- `.claude/README.md`: thêm `agents/`, `/research`, `/handoff`.
- `decisions.md` 2 mục [2026-10-10]; `log.md` 2 mục `schema` (14-51-56, 14-55-07). Chưa commit.

## Kiểm tra đã chạy

- `py_compile` hook: đạt. `--session-start`: in đúng handoff mới nhất, exit 0.
- Ba file JSON (`settings.json`, `settings.local.json`, `evals.json`) parse được.
- `--all`: 790 trang, 0 lỗi, 4 trang mồ côi (có sẵn).
- Chưa kiểm trong phiên thật, vì cấu hình chỉ nạp từ phiên sau: rule `deny`, hook `SessionStart`, việc tắt plugin, subagent.
- Chưa chạy 3 eval của `research`. Chưa chạy `--verify-sources`.

## Việc còn lại

Từ phiên này:

- Lệnh shell vẫn ghi được vào `01_sources/`; chưa có hook `PreToolUse` trên `Bash|PowerShell`.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json` (nơi đã có `finance@synced: false`).
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; ví dụ map FTP ghi 37 node, `02_wiki/` hiện còn 6 trang có `ftp` trong tên. Cần quét lại trước khi dùng.
- `lint` và `promote` chưa có evals.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.

Chép từ các handoff trước, chưa xử lý:

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

## Bước tiếp theo

- Người dùng xem `git diff` rồi quyết định commit (gồm cả thay đổi của hai phiên trước trong ngày).
- Mở phiên mới để xác nhận bốn điểm: handoff này tự hiện đầu phiên; danh sách skill không còn `engineering:*`, `design:*`, `harness`; yêu cầu sửa thử một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi" chạy được.
- Chạy 3 eval `research` bằng `skill-creator`.
- Ingest bù theo lô, mỗi lô qua bước duyệt; đề xuất bắt đầu `imf_macro_accounting` + `bindseil_monetary_policy` (16 mục).
- Chạy thử một lượt `/query` để xem bước mồi có dẫn tới đọc §13 không.
