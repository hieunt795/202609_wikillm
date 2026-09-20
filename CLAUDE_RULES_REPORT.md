# Báo cáo thiết kế hệ thống chỉ dẫn Claude cho LLM Wiki

## Tóm tắt điều hành

Một project không cần dồn mọi quy tắc vào `CLAUDE.md`. Hệ thống chỉ dẫn tốt
được chia thành nhiều tầng, mỗi tầng giải quyết một loại vấn đề:

```text
CLAUDE.md
    Bối cảnh và guardrail luôn phải biết

.claude/rules/
    Quy tắc chuyên biệt theo chủ đề hoặc đường dẫn

.claude/skills/
    Workflow nhiều bước cho từng loại tác vụ

.claude/agents/
    Subagent chuyên trách cho tác vụ độc lập, nặng context

.claude/agent-memory/
    Kinh nghiệm lâu dài riêng của từng subagent

.claude/hooks/
    Kiểm tra hoặc cưỡng chế xác định bằng chương trình

.claude/settings*.json
    Quyền công cụ, hook và cấu hình vận hành
```

Đối với LLM Wiki, phần lớn nền tảng đã tồn tại: `CLAUDE.md`, schema, năm skill,
hook kiểm tra và các file trạng thái. Việc cần làm không phải phát minh thêm hệ
thống mới, mà là phân tầng lại nội dung để giảm trùng lặp, giữ đúng nguồn sự thật
và nạp đúng chỉ dẫn vào đúng thời điểm.

## 1. Mô hình tổ chức chỉ dẫn Claude Code

### 1.1. Nguyên tắc nguồn sự thật duy nhất

Mỗi loại thông tin phải có một nơi chịu trách nhiệm chính:

- Context luôn cần biết → `CLAUDE.md`.
- Quy tắc theo file/chủ đề → `.claude/rules/`.
- Quy trình theo tác vụ → `.claude/skills/`.
- Công việc chuyên trách cần context riêng → `.claude/agents/`.
- Kinh nghiệm riêng của agent → `.claude/agent-memory/`.
- Kiểm tra deterministic → `.claude/hooks/`.
- Quyền và trigger → `.claude/settings.json`.
- Data model nghiệp vụ → schema của project.
- Trạng thái nghiệp vụ → file state chuyên trách của project.

Một quy tắc có thể được nhắc ngắn ở tầng cao để tạo guardrail, nhưng đặc tả đầy
đủ chỉ nên tồn tại ở một nơi. Ví dụ, `CLAUDE.md` có thể nói “không sửa nguồn”,
rule giải thích metadata nguồn phải đi đâu, còn hook xác minh nguồn có bị đổi hay
không.

### 1.2. Tiêu chí lựa chọn nơi lưu

| Câu hỏi | Nơi lưu phù hợp |
|---|---|
| Claude có phải biết điều này trong mọi phiên? | `CLAUDE.md` |
| Điều này chỉ áp dụng cho một nhóm file? | `.claude/rules/` có `paths` |
| Đây là một chuỗi thao tác cần suy luận? | `.claude/skills/` |
| Tác vụ có thể chạy độc lập trong context riêng? | `.claude/agents/` |
| Chỉ agent đó cần nhớ bài học này? | `.claude/agent-memory/` |
| Có thể kiểm tra chắc chắn bằng code? | `.claude/hooks/` |
| Đây là quyền truy cập hoặc trigger hook? | `.claude/settings.json` |
| Đây là preference riêng của một máy? | `.claude/settings.local.json` |
| Đây là dữ liệu hoặc trạng thái nghiệp vụ? | File chuyên trách của project |

### 1.3. Nguyên tắc chất lượng

- Quy tắc phải cụ thể, có thời điểm áp dụng và cách kiểm.
- Không dùng câu mơ hồ như “hãy viết code tốt”.
- Không nhúng API documentation hoặc tài liệu nguồn dài vào chỉ dẫn luôn-nạp.
- Không tạo file mới nếu nội dung đã có nguồn sự thật phù hợp.
- Guardrail sống còn không nên chỉ dựa vào việc model nhớ; nếu có thể, dùng hook.
- Review định kỳ để xoá rule lỗi thời, gộp rule trùng và sửa tham chiếu chết.
- `CLAUDE.md` nên ngắn, dễ quét và dưới khoảng 200 dòng.

## 2. Vai trò của từng thành phần

### 2.1. `CLAUDE.md`

`CLAUDE.md` là chỉ dẫn cấp project được nạp trong mọi phiên. Nó nên trả lời nhanh
các câu hỏi:

- Project làm gì và phục vụ ai?
- Kiến trúc chính là gì?
- Nguồn sự thật nằm ở đâu?
- Vùng nào được phép hoặc không được phép sửa?
- Hành động nào cần người dùng xác nhận?
- Có những workflow chính nào?
- Phải kiểm tra gì trước khi tuyên bố hoàn thành?

Nội dung nên giữ:

- project overview;
- bản đồ kiến trúc và nguồn sự thật;
- command thường dùng;
- guardrail toàn cục;
- checkpoint xác nhận;
- danh sách workflow và nơi chứa skill;
- bản đồ rules, hooks và settings;
- điều kiện tạo handoff.

Nội dung nên chuyển ra ngoài:

- workflow nhiều bước;
- data model chi tiết;
- rule chỉ áp dụng cho một nhóm file;
- báo cáo, trạng thái phiên hoặc tiến độ thường xuyên thay đổi;
- tài liệu kỹ thuật dài.

### 2.2. `.claude/rules/`

Rules chứa chỉ dẫn chuyên biệt. Rule có thể áp dụng toàn project hoặc được giới
hạn bằng YAML frontmatter:

```markdown
---
paths:
  - "src/**/*.py"
---

# Python rules

- Dùng type hints cho public function.
- Test nằm trong `tests/`.
```

Một rule tốt:

- chỉ có một trách nhiệm;
- dùng `paths` khi có thể thu hẹp phạm vi;
- ngắn và dễ kiểm tra;
- trỏ về schema thay vì chép lại toàn bộ;
- không chứa workflow nhiều bước;
- không thay thế hook cho guardrail cần cưỡng chế.

### 2.3. `.claude/skills/`

Skill mô tả cách thực hiện một loại tác vụ lặp lại. Một skill nên có:

- điều kiện kích hoạt;
- đầu vào và đầu ra;
- thứ tự thực hiện;
- checkpoint cần người dùng xác nhận;
- công cụ và command cần chạy;
- failure mode;
- điều kiện hoàn thành.

Skill trả lời câu hỏi “làm tác vụ này như thế nào?”, trong khi rule trả lời “khi
làm việc trong phạm vi này phải tuân thủ điều gì?”.

### 2.4. `.claude/agents/`

Agents định nghĩa subagent chuyên trách có context và công cụ riêng. Agent phù
hợp khi công việc:

- độc lập với luồng chính;
- tốn nhiều context;
- có đầu ra rõ và kiểm chứng được;
- không cần liên tục hỏi lại người dùng;
- có thể giao quyền công cụ hẹp.

Mỗi agent cần xác định nhiệm vụ, điều kiện gọi, đầu ra, công cụ, quyền ghi và các
hành động phải chuyển lại cho agent chính. Không tạo agent chỉ để chia nhỏ một
workflow mà skill hiện tại đã xử lý tốt.

### 2.5. `.claude/agent-memory/`

Agent memory tại `.claude/agent-memory/<agent-name>/MEMORY.md` lưu kinh nghiệm lâu
dài riêng cho từng subagent: pattern lỗi, false positive, giới hạn công cụ và
cách thu hẹp phạm vi tìm kiếm. Không dùng nó cho data model, trạng thái nghiệp
vụ, tri thức đã chấp nhận, quyết định kiến trúc hoặc tiến độ phiên.

Chỉ tạo memory khi agent ổn định và liên tục phải học lại cùng một bài học.

### 2.6. `.claude/hooks/`

Hooks thực hiện kiểm tra hoặc cưỡng chế bằng chương trình, chẳng hạn:

- chạy validator sau khi sửa file;
- chặn ghi vào vùng bảo vệ;
- kiểm tra schema và format;
- phát hiện link chết;
- xác minh checksum;
- chặn command nguy hiểm.

Nếu một điều phải luôn đúng và có thể xác định bằng code, hook đáng tin cậy hơn
chỉ dẫn văn bản.

### 2.7. `.claude/settings.json` và `settings.local.json`

`settings.json` dùng cho cấu hình dùng chung:

- hooks và trigger;
- quyền công cụ;
- biến môi trường không nhạy cảm;
- cấu hình vận hành của project.

`settings.local.json` dùng cho cấu hình riêng theo máy và không nên là nguồn sự
thật chung. Không lưu secrets trong file được commit.

### 2.8. Các thành phần tùy chọn khác

Các thành phần tùy chọn gồm `.claude/commands/` cho prompt một file,
`.claude/output-styles/` cho cách trình bày và `.claude/loop.md` cho `/loop`.
Ở gốc project có thể có `.mcp.json`, `.worktreeinclude` và `CLAUDE.local.md`;
chỉ thêm khi project phát sinh nhu cầu tương ứng.

## 3. Memory và dữ liệu bền vững

### 3.1. Memory của Claude Code

Claude Code có thể lưu auto-memory theo project bên ngoài repository:

```text
~/.claude/projects/<project>/memory/
```

Transcript phiên thường nằm trong cùng cây project dưới dạng `.jsonl`. Đây là dữ
liệu local để tiếp tục phiên hoặc hỗ trợ Claude nhớ một số bài học; nó không phải
nguồn sự thật được chia sẻ và không bảo đảm lưu mọi nội dung quan trọng.

### 3.2. Memory của repository

Thông tin cần chia sẻ, version-control hoặc kiểm chứng phải được lưu trong repo ở
đúng nơi: `CLAUDE.md`, schema, state, decisions, log hoặc tri thức nghiệp vụ.

Nguyên tắc:

```text
Auto-memory      → hỗ trợ cá nhân, có thể thiếu hoặc thay đổi
Repository       → nguồn sự thật chia sẻ và kiểm chứng được
Agent memory     → bài học riêng của một subagent
Session history  → lịch sử để resume/debug, không phải tài liệu dự án
```

## 4. Áp dụng cho LLM Wiki

### 4.1. Mục tiêu và phạm vi

LLM Wiki tích luỹ tri thức về kinh tế vĩ mô, tiền tệ, ngân hàng và thị trường
thu nhập cố định. Tài liệu thô được chuyển thành các trang:

- atomic và độc lập;
- tái sử dụng được;
- liên kết với nhau;
- truy ngược được tới đúng đoạn nguồn;
- viết lại bằng tiếng Việt.

Project không phải tập hợp bản tóm tắt sách, kho phát hành tài liệu gốc hoặc hệ
thống RAG trả lời lại từ đầu mỗi lần hỏi.

### 4.2. Nguồn sự thật của project

| Loại thông tin | Nguồn sự thật |
|---|---|
| Tài liệu gốc | `01_sources/` |
| Tri thức đã vào wiki | `02_wiki/` |
| Điều hướng và tiến độ cấp nguồn | `02_wiki/index.md` |
| Danh mục và checksum nguồn | `03_state/_sources_manifest.md` |
| Tiến độ chunk nguồn dài | `03_state/<source-id>.md` |
| Data model và luật trang | `00_schema.md` |
| Workflow operation | `.claude/skills/*/SKILL.md` |
| Kiểm tra tự động | `.claude/hooks/validate_wiki_page.py` |
| Kết quả operation | `log.md` |
| Quyết định và lý do | `decisions.md` |
| Ý tưởng chưa đủ chín | `_inbox.md` |
| Báo cáo lint/audit | `Claude outputs/` |
| Bàn giao phiên | `session_handoffs/` sau khi kích hoạt |

Không dùng `log.md`, transcript hay auto-memory để suy ra trạng thái hiện tại khi
đã có nguồn sự thật chuyên biệt.

### 4.3. Guardrail và checkpoint toàn cục

Những điều phải luôn xuất hiện ngắn gọn trong `CLAUDE.md`:

1. Không bao giờ sửa, thêm, đổi tên, xoá hoặc đổi line ending trong
   `01_sources/`.
2. Không tự giải quyết hai claim nguồn mâu thuẫn; ghi conflict và chờ người dùng.
3. Không biến research, audit hoặc draft thành tri thức đã chấp nhận.
4. Không ghi đè thay đổi ngoài phạm vi của người dùng.
5. Không xoá, rollback, force-push hoặc sửa hàng loạt khi chưa xác định phạm vi
   và khả năng khôi phục.

Checkpoint cần xác nhận:

- trước khi `/ingest` ghi trang sau bước duyệt 3–5 ý chính;
- trước khi `/query` tạo trang `analysis`;
- trước khi `/promote` nâng `draft → stable`;
- trước thao tác phá huỷ hoặc mở rộng đáng kể ngoài phạm vi ban đầu.

### 4.4. Nội dung của `CLAUDE.md`

`CLAUDE.md` mục tiêu nên giữ:

- project overview;
- bảng nguồn sự thật;
- năm operation;
- guardrail và checkpoint;
- quy tắc logging tổng quát;
- workflow chung khảo sát → xác nhận → thực hiện → kiểm tra → bàn giao;
- bản đồ schema, rules, skills, hooks và settings;
- trigger tạo session handoff.

Năm operation:

| Operation | Vai trò |
|---|---|
| `/ingest` | Chuyển nội dung nguồn thành trang wiki |
| `/query` | Trả lời từ tri thức đã có |
| `/lint` | Kiểm tra và báo cáo sức khoẻ wiki |
| `/promote` | Nâng trang được duyệt lên `stable` |
| `/review-node` | Đối chiếu claim của trang với nguồn |

Chỉ operation làm thay đổi wiki hoặc trạng thái vận hành mới ghi log. `/query`
chỉ trả lời thì không ghi log.

### 4.5. Bộ `.claude/rules/` mục tiêu

#### `wiki-pages.md`

Phạm vi: `02_wiki/*.md`.

- Tên file là kebab-case của title.
- Title tiếng Anh; thân bài tiếng Việt.
- Mỗi trang chứa một ý tưởng atomic; thân bài không có heading.
- Wikilink nằm trong câu và có lý do; tags không thay thế liên kết.
- Claim từ nguồn dài có locator.
- Chỉ nâng `last_updated` khi claim thay đổi.
- Không tự promote hoặc ghi đè `reviewed_by: user`.
- `index.md` được miễn luật thân bài của trang atomic.

#### `source-management.md`

Phạm vi: `01_sources/**`, `03_state/**`, `02_wiki/index.md`.

- `01_sources/` tuyệt đối chỉ đọc.
- Nguồn mới phải đăng ký trong manifest.
- Nguồn dài có đúng một file state.
- State là nguồn sự thật về tiến độ ingest; không dựng tiến độ từ log.
- Mỗi lượt ingest cập nhật đồng bộ state và index.
- Kiểm integrity bằng `--verify-sources`.

#### `project-records.md`

Phạm vi: `log.md`, `decisions.md`, `_inbox.md`, `Claude outputs/**`.

- Log lưu kết quả; decisions lưu lý do.
- Inbox lưu ý tưởng chưa đủ chín; state lưu tiến độ hiện tại.
- Log là append-only; mỗi operation có thay đổi ghi đúng một mục.
- Query chỉ trả lời thì không ghi log.
- Lint chỉ báo cáo, không tự sửa.

#### `session-handoff.md`

Không giới hạn `paths` vì trigger cần được biết trong toàn phiên.

- Phiên có thay đổi tạo đúng một handoff mới.
- Phiên chỉ đọc hoặc hỏi đáp không thay đổi trạng thái thì không tạo.
- Không sửa handoff cũ.
- Ghi kết quả, kiểm tra, việc còn lại, blocker và bước tiếp theo.
- Không chép transcript hoặc diff dài.
- Handoff không thay thế log, state hoặc decisions.

### 4.6. Bộ skills hiện tại

| Skill | Workflow cốt lõi |
|---|---|
| `/ingest` | Chọn chunk → đọc → trình ý chính → chờ duyệt → ghi → link → state/index → kiểm → log |
| `/query` | Xác định coverage → tìm trang → đọc chọn lọc → tổng hợp → tùy chọn analysis có duyệt |
| `/lint` | Chạy kiểm máy → quét rẻ → đọc trang bị flag → báo cáo → triage |
| `/promote` | Nhận danh sách đã duyệt → kiểm lại → chỉ đổi status → kiểm → log |
| `/review-node` | Tách claim → mở nguồn → đối chiếu → sửa claim sai → kiểm → log |

Workflow chi tiết tiếp tục nằm trong từng `SKILL.md`; rules không chép lại các
bước này.

### 4.7. Hooks và settings

Hook hiện tại kiểm tra frontmatter, taxonomy, title, heading, link chết, source
id, locator, lifecycle fields, backlink, orphan, OCR, nợ stub/inbox và integrity
của nguồn.

Cải tiến có thể cân nhắc sau này: thêm guardrail chặn ghi vào `01_sources/`, thay
vì chỉ phát hiện sai lệch sau đó. Đây là thay đổi riêng, không thuộc đợt tái cấu
trúc rules hiện tại.

### 4.8. Agents và agent memory

Project hiện chưa cần agents. Năm operation đã có skill rõ ràng và các checkpoint
quan trọng cần agent chính phối hợp trực tiếp với người dùng.

Chỉ cân nhắc agent khi tác vụ đủ độc lập và nặng context:

| Agent tương lai | Nhiệm vụ | Quyền mặc định |
|---|---|---|
| `source-verifier` | Đối chiếu claim với nguồn và báo evidence gap | Chỉ đọc |
| `wiki-auditor` | Rà cấu trúc, trùng lặp, conflict và Atomic | Chỉ đọc |
| `source-mapper` | Lập bản đồ heading/chunk nguồn dài | Chỉ đọc, trả đề xuất |

Agents không tự ingest, promote, publish hoặc xử lý conflict. Agent chính giữ
trách nhiệm mutation, checkpoint người dùng và kiểm tra cuối.

Chỉ tạo agent memory khi agent liên tục phải học lại pattern OCR, false positive,
giới hạn parser hoặc cách tìm đoạn nguồn. Không lưu nội dung wiki, trạng thái
ingest, schema, quyết định chung hoặc tiến độ phiên trong agent memory.

### 4.9. Cấu trúc mục tiêu

```text
LLM Wiki/
├── CLAUDE.md
├── 00_schema.md
├── 01_sources/
├── 02_wiki/
├── 03_state/
├── log.md
├── decisions.md
├── _inbox.md
├── session_handoffs/
└── .claude/
    ├── settings.json
    ├── settings.local.json
    ├── rules/
    │   ├── wiki-pages.md
    │   ├── source-management.md
    │   ├── project-records.md
    │   └── session-handoff.md
    ├── skills/
    │   ├── ingest/
    │   ├── query/
    │   ├── lint/
    │   ├── promote/
    │   └── review-node/
    └── hooks/
        └── validate_wiki_page.py
```

Khi thật sự cần subagent, mở rộng thêm:

```text
.claude/
├── agents/
│   └── <agent-name>.md
└── agent-memory/
    └── <agent-name>/
        └── MEMORY.md
```

## 5. Trạng thái hiện tại và lộ trình kích hoạt

### 5.1. Trạng thái hiện tại

- `CLAUDE.md` hiện hành vẫn là chỉ dẫn có hiệu lực.
- `CLAUDEV4_1.local.md` là bản thử nghiệm, không tự được nạp.
- `.claude/rules-draft/` chứa bốn rule thử nghiệm, không phải thư mục auto-load.
- V2–V4 được giữ để so sánh.
- Chưa có `session_handoffs/`, agents hoặc agent memory.

### 5.2. Các bước kích hoạt

1. Review V4.1 và bốn rules về nội dung, trùng lặp và mâu thuẫn.
2. Đối chiếu với `00_schema.md`, năm skills và validator.
3. Sửa mọi tham chiếu chết và xác nhận glob `paths`.
4. Thay `CLAUDE.md` bằng bản V4.1 đã duyệt.
5. Đổi `.claude/rules-draft/` thành `.claude/rules/`.
6. Chạy một tác vụ thử cho từng nhóm: wiki, source/state, records và handoff.
7. Chỉ sau khi ổn định mới xoá hoặc lưu trữ các bản thử nghiệm cũ.

### 5.3. Tiêu chí chấp nhận

- `CLAUDE.md` dưới 200 dòng và không chứa workflow dài.
- Mỗi rule có một trách nhiệm và scope rõ.
- Không có đường dẫn hoặc command không tồn tại.
- Không có mâu thuẫn với schema hoặc skills.
- `/query` không thay đổi wiki không ghi log.
- `index.md` không bị áp luật thân bài atomic.
- `01_sources/` vẫn bất biến.
- Phiên có thay đổi tạo một handoff; phiên chỉ đọc không tạo.
- Auto-memory, transcript và agent memory không được dùng thay nguồn sự thật của
  repository.

## 6. Kết luận

Kiến trúc phù hợp cho LLM Wiki ở thời điểm hiện tại là:

```text
CLAUDE.md + rules + skills + hooks + settings
```

Agents và agent memory là khả năng mở rộng, chưa phải thành phần bắt buộc. Trọng
tâm trước mắt là review V4.1, kích hoạt bộ rules sau khi duyệt, giữ mỗi loại thông
tin ở đúng nguồn sự thật và dùng hook cho những guardrail có thể kiểm bằng máy.
