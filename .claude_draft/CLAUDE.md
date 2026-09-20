# LLM Wiki — Macroeconomics · CLAUDE.md Draft

> Bản thử nghiệm để review thủ công trong `.claude_draft/`. Claude Code không tự
> nạp gói này; `CLAUDE.md` và `.claude/` ở root vẫn có hiệu lực.

## Tổng quan dự án

Wiki tri thức tích luỹ về kinh tế vĩ mô, tiền tệ, ngân hàng và thị trường thu
nhập cố định. Mục tiêu là biến tài liệu thô thành mạng trang atomic, liên kết và
truy ngược được về nguồn — không phải tập hợp bản tóm tắt sách hay hệ thống RAG.

Kết quả đúng là kiến thức được viết lại bằng tiếng Việt, có ranh giới khái niệm
rõ, tuân thủ schema và chỉ vào wiki sau đúng operation cùng các bước kiểm.

## Kiến trúc và nguồn sự thật

| Thành phần | Vai trò |
|---|---|
| `01_sources/` | Nguồn gốc bất biến, chỉ đọc |
| `02_wiki/` | Mạng trang wiki do agent bảo trì |
| `02_wiki/index.md` | Điều hướng và trạng thái ingest cấp nguồn |
| `03_state/_sources_manifest.md` | Source id, xuất xứ, kích thước và checksum |
| `03_state/<source-id>.md` | Trạng thái chunk của nguồn dài |
| `00_schema.md` | Data model và tiêu chuẩn trang wiki |
| `.claude_draft/.claude/skills/*/SKILL.md` | Quy trình thử nghiệm cho từng operation |
| `.claude_draft/.claude/hooks/validate_wiki_page.py` | Kiểm tra xác định được bằng máy |
| `log.md` | Nhật ký kết quả operation dạng append-only |
| `decisions.md` | Quyết định thiết kế và lý do |
| `_inbox.md` | Ý tưởng hoặc vấn đề chưa đủ chín |
| `Claude outputs/` | Báo cáo lint/audit, không phải tri thức xuất bản |

Không suy trạng thái hiện tại từ `log.md` khi đã có nguồn sự thật chuyên biệt.

## Năm operation

| Operation | Phạm vi |
|---|---|
| `/ingest` | Nguồn → 3–5 ý chính chờ duyệt → trang, index và state |
| `/query` | Câu hỏi → câu trả lời; trang `analysis` cần xác nhận |
| `/lint` | Kiểm tra và báo cáo; không tự sửa |
| `/promote` | Chỉ nâng danh sách người dùng đã duyệt |
| `/review-node` | Đối chiếu tối đa 5 trang với nguồn gốc |

Đọc skill tương ứng trước khi thực hiện. Skill giữ workflow chi tiết; file này và
rules chỉ giữ bối cảnh, guardrail và quy tắc áp dụng chéo.

## Quy tắc cố định

1. Không bao giờ thêm, sửa, đổi tên, xoá hoặc đổi line ending trong `01_sources/`.
2. Không tự giải quyết hai claim nguồn mâu thuẫn; ghi `⚠️ Conflict` kèm cả hai
   claim và locator, rồi chờ người dùng.
3. Không tự biến research, audit hoặc draft thành tri thức đã chấp nhận.
4. Cần người dùng xác nhận trước khi ingest ghi trang, query tạo `analysis`, hoặc
   promote `draft → stable`.
5. Không ghi đè thay đổi không liên quan của người dùng. Không xoá, rollback,
   force-push hoặc sửa hàng loạt khi chưa xác định phạm vi và khả năng khôi phục.
6. Chỉ operation làm thay đổi wiki hoặc trạng thái vận hành mới ghi một mục vào
   `log.md`; `/query` chỉ trả lời thì không ghi log.

Nếu `CLAUDE.md`, schema, rule và skill mâu thuẫn, dừng trước khi ghi, chỉ rõ các
đoạn mâu thuẫn và xin người dùng quyết định; không tự chọn một luật.

## Quy trình chung

1. Khảo sát chỉ dẫn, phạm vi, nguồn sự thật và Git status.
2. Xác nhận lựa chọn của người dùng tại các checkpoint bắt buộc.
3. Thực hiện thay đổi nhỏ nhất, giữ nguyên nội dung ngoài phạm vi.
4. Chạy hook/lệnh kiểm theo skill; xử lý hoặc báo rõ mọi lỗi.
5. Cập nhật đúng state/log/decision và tạo handoff nếu phiên có thay đổi.

## Phân tầng chỉ dẫn

- Rule chuyên biệt: `.claude_draft/.claude/rules/`; không dùng `@import`.
- Workflow theo tác vụ: `.claude_draft/.claude/skills/`.
- Guardrail cần thực thi bằng máy: `.claude_draft/.claude/hooks/` và
  `.claude_draft/.claude/settings.json`.
- Chi tiết data model, taxonomy và lifecycle: `00_schema.md`.

Khi kích hoạt, review rồi chuyển nội dung đã duyệt sang `CLAUDE.md` và `.claude/`
ở root. Không sao chép toàn bộ schema hoặc skill vào rules. Giữ file này dưới
120 dòng.

## Session handoff

Phiên làm thay đổi repo hoặc trạng thái vận hành phải tạo đúng một file mới:
`.claude_draft/session_handoffs/YYYY-MM-DD-HHmm-<short-slug>.md`. Phiên chỉ đọc,
khảo sát hoặc hỏi đáp không thay đổi trạng thái thì không tạo. Chi tiết ở rule
handoff.

## Ngoài phạm vi mặc định

Không áp quy tắc UI, typography, responsive, animation, screenshot hoặc Git
worktree trừ khi yêu cầu mới đưa chúng vào phạm vi rõ ràng.
