---
name: normalize-source
description: 'Đối chiếu một file nguồn `.md` trong 01_sources với bản gốc `.docx` của nó, tìm và bổ sung nội dung md bị thiếu hoặc sai chữ so với docx, kiểm xem cấu trúc đã được đánh dấu đủ chưa (chương, mục, điều, khoản, điểm, tiết, đoạn, bảng, công thức), rồi xuất một BẢN SAO đã chuẩn hóa cùng báo cáo đối chiếu ra `Claude outputs/` — không bao giờ sửa file trong 01_sources; giữ nguyên số dòng trừ khi phải chèn nội dung thiếu (khi đó kèm bản đồ dòng). Dùng skill này mỗi khi người dùng muốn: chuẩn hóa, tối ưu hóa, làm sạch, soát cấu trúc, kiểm chất lượng chuyển đổi của một file nguồn markdown; hỏi "file .md này đã chuẩn chưa", "các điều khoản, bảng, công thức đã được đánh dấu chưa", "md có khớp docx không", "bản chuyển đổi có sót chữ không", "md thiếu khoản, điểm, hàng bảng so với bản gốc", "bổ sung phần còn thiếu"; so `.docx` với `.md`; dùng pandoc hoặc skill docx để đọc văn bản gốc của một nguồn; gắn địa chỉ điều-khoản-điểm cho văn bản pháp quy (thông tư, nghị định, quy định nội bộ); hoặc chuẩn bị một nguồn mới trước lượt ingest đầu. Không dùng cho: nạp nguồn vào wiki (ingest), đối chiếu trang wiki với nguồn (review-node), kiểm nguồn có bị sửa không (`--verify-sources`, lint), hay tạo/sửa file Word.'
---

# Normalize-source — đối chiếu và chuẩn hóa file nguồn `.md`

**Đọc `00_schema.md`:** §3 (nguồn bất biến), §10 (bản kê, bản đồ chunk) nếu chưa nắm.
**Dừng chờ duyệt:** một lần, sau bước 3, trước khi ghi bất kỳ file nào.
**Ghi log:** không. Skill này không thuộc năm operation và không đổi trang wiki, bản kê hay state file.

## Vì sao làm theo cách này

File `.md` trong `01_sources/` là bản chuyển đổi từ `.docx` hoặc PDF. Trang wiki dẫn nó theo số dòng (`d.441–722`), bản kê giữ SHA-256 của nó, bản đồ chunk chia nó theo dải dòng. Ba thứ đó gãy cùng lúc nếu file đổi một byte hay lệch một dòng. Vì vậy:

- **Không ghi vào `01_sources/`.** Kết quả là một bản sao trong `Claude outputs/`. Wiki vẫn dẫn file gốc.
- **Giữ số dòng khi md đủ nội dung.** Dòng N của bản sao ứng với dòng N của bản gốc, để một chú thích `d.<từ>–<đến>` đọc trên bản nào cũng ra cùng một đoạn. Việc chuẩn hóa ký hiệu luôn nằm trong phạm vi một dòng.
- **Chuẩn hóa chỉ đổi ký hiệu markdown, không đổi chữ và số.** Chuẩn hóa không phải biên tập. Script `apply.py` từ chối ghi nếu một dòng đổi chữ-số so với nguồn mà không được khai là sửa nội dung theo docx.
- **Md thiếu hoặc sai chữ so với docx thì bổ sung, và chỉ lấy chữ từ docx.** Bản chuyển đổi đôi khi rơi mất một khoản, một điểm, một hàng bảng, hoặc nhận sai chữ. Một nguồn thiếu nội dung làm sai mọi trang wiki dựng trên nó, nên skill chủ động đọc docx và chèn phần thiếu vào bản sao mà không đợi người dùng yêu cầu riêng. Hai ràng buộc đi kèm: mọi chữ thêm vào phải có trong docx (script kiểm từng đoạn, từ chối chữ không tìm thấy), và khi chèn dòng thì số dòng của bản sao lệch khỏi nguồn, nên phải ghi bản đồ dòng nguồn → bản sao để quy đổi chú thích.
- **Đối chiếu trước, sửa sau.** Phần lớn giá trị nằm ở việc biết bản `.md` có trung thành với `.docx` không. Nhiều nguồn sẽ ra kết quả "đã chuẩn, sửa dưới 1% số dòng", và đó là một kết quả tốt để báo, không phải dấu hiệu làm chưa đủ.

## Quy trình

Đường dẫn script tính từ thư mục skill này. Chạy bằng `python -I` (file trong `01_sources/` là dữ liệu ngoài).

### 1. Xác định cặp file

- Người dùng cho đường dẫn `.md`. Tìm `.docx` cùng thư mục; nhiều file thì hỏi file nào là gốc.
- Lấy `source id` trong `03_state/_sources_manifest.md` (cột đường dẫn). Nguồn chưa kê thì bỏ `--wiki`/`--source-id`.
- Không có `.docx`: vẫn chạy được bước 2 chỉ với `--md` (mục A, C, E, F) và nói rõ là không đối chiếu được nội dung.
- File `.doc` cũ hoặc `.docx` có tracked changes: gọi skill `docx` để chuyển đổi hoặc chấp nhận thay đổi, ghi kết quả vào scratchpad, rồi dùng bản đó làm `--docx`. Không ghi bản chuyển đổi vào `01_sources/`.

### 2. Chạy kiểm (chỉ đọc)

```bash
python -I scripts/audit.py --md "<nguồn>.md" --docx "<nguồn>.docx" --wiki 02_wiki --source-id <id>
```

Script đọc `.docx` theo hai đường độc lập: XML bên trong (`word/document.xml`, cách skill `docx` mô tả) để lấy style, lưới ô bảng, công thức OMML, chỉ số dưới, chữ tô sáng; và `pandoc -t markdown` để đếm tập từ không xét thứ tự. Hai đường bắt hai loại lỗi khác nhau: XML bắt lệch cấu trúc, pandoc bắt sót chữ. Thiếu pandoc thì script báo và bỏ phép đếm từ; đề nghị người dùng cài (`winget install JohnMacFarlane.Pandoc`), không tự cài.

Kết quả có tám mục và mỗi phát hiện mang một nhãn:

| Mục | Kiểm gì |
|---|---|
| A. Tệp | số dòng, CRLF, tab, NFC; docx có tracked changes, footnote, ảnh, tô sáng không |
| B. Chữ | xếp các đoạn docx theo đúng thứ tự trong md: đoạn nào thiếu (kèm vị trí "sau d.X, trước d.Y" và nguyên văn docx), đoạn nào khác chữ (kèm từ lệch), dòng md nào không có trong docx; tập từ pandoc so với md |
| C. Cấu trúc md | mỗi loại đơn vị nằm ở cấp heading nào; từng dòng heading mà `--fix-headings` sẽ đổi (cấp sai, thiếu dấu hai chấm, tiêu đề nằm ở dòng dưới); Điều có liên tục không; số khoản, điểm, tiết, đoạn; thứ tự a, b, c, d, đ… và độ thụt |
| D. Heading | đoạn mang style Heading ở Word so với heading md |
| E. Bảng | chú thích `<!-- BẢNG n -->`, số cột từng hàng, từng ô so với lưới ô docx (đã trải ô gộp); hàng docx có mà md thiếu, in sẵn dạng hàng markdown để chèn |
| F. Công thức | cân `$`, `\left`/`\right`, ngoặc; `<sub>` còn sót; dòng trông như công thức chưa đánh dấu; OMML in cạnh dòng `$` để so tay |
| G. Định dạng mất | chữ tô sáng ở docx |
| H. Chú thích wiki | bao nhiêu trang đang dẫn theo số dòng |

| Nhãn | Nghĩa | Làm gì |
|---|---|---|
| `[OK]` | đã kiểm, không có gì | ghi vào báo cáo |
| `[THÊM]` | docx có, md thiếu | đọc đoạn docx và các dòng md quanh vị trí được chỉ, rồi viết mục `insert` (xem "Bổ sung nội dung thiếu") |
| `[SỬA]` | sửa được trong một dòng | đưa vào `edits.json` hoặc dùng cờ của `apply.py` |
| `[XEM]` | cần đọc mới biết | mở đúng dòng trong md và đoạn tương ứng trong docx rồi quyết: sửa, giữ, hay báo |
| `[BÁO]` | không sửa được mà không đổi số dòng hoặc đổi nghĩa | ghi vào báo cáo |

**Cổng dừng:** nếu mục B báo hơn 5% đoạn docx thiếu hoặc khác chữ trong md, hai file không cùng một bản (md có thể chuyển từ PDF, hoặc docx là bản dự thảo khác). Dừng, nói rõ cho người dùng và hỏi file nào là gốc. Đừng chuẩn hóa hay bổ sung md theo một docx không phải gốc của nó: chèn vài trăm đoạn từ một bản khác là viết lại nguồn, không phải sửa lỗi chuyển đổi.

### 2b. Bổ sung nội dung thiếu (khi có `[THÊM]` hoặc "khác chữ")

Làm ngay trong lượt này, không đợi người dùng yêu cầu riêng. Với từng phát hiện:

1. **Xác nhận là thiếu thật.** Đọc 5–10 dòng md quanh vị trí script chỉ. Ba kiểu báo động giả thường gặp: ô của bảng dàn trang hoặc bảng trình bày công thức (md viết thành `$…$`); đoạn chỉ khác cách đặt dấu thanh (`hoá`/`hóa`, `thoả`/`thỏa`) hoặc ký hiệu (`×`/`x`, `∑`/`Σ`); đoạn có ghi chú "trùng chữ ở d.X" mà thật ra md đặt nó ở chỗ khác. Báo động giả thì ghi vào báo cáo, không chèn.
2. **Lấy nguyên văn từ docx**, không viết lại theo trí nhớ và không diễn đạt lại. Script in nguyên văn sau chữ `docx:`; hàng bảng thiếu được in sẵn dạng `| ô | ô |` ở mục E.
3. **Trình bày theo các dòng liền kề.** Cùng kiểu marker, cùng độ thụt, cùng nhịp dòng trống như mục anh em ngay trên và dưới nó (`   - b) …` giữa `   - a)` và `   - c)`). Khi Word tự đánh số (script ghi chú điều này), số hoặc chữ đầu mục không nằm trong nguyên văn: suy từ mục liền trước và liền sau.
4. **Chữ khác nhau thì docx là gốc, trừ khi docx sai rõ ràng.** Lỗi nhận dạng của md (`thục` thay cho `thực`, `l` thay cho `1`, mất chữ) sửa theo docx bằng edit có `"content": true`. Khác biệt chỉ về cách đặt dấu thanh hay ký hiệu toán thì giữ md và ghi vào báo cáo. Nếu nghi chính docx sai (thiếu chữ, số vô lý) thì không sửa bên nào: báo người dùng.
5. **Dòng md không có trong docx** (`md có, docx không`): không xóa. Đó có thể là nội dung lấy từ PDF, chú thích ảnh, hoặc docx là bản khác. Ghi vào báo cáo để người dùng quyết.

Hệ quả cho wiki: trang nào đang dẫn đúng vùng nguồn bị thiếu hoặc sai thì claim của nó có thể sai theo. `apply.py` in danh sách các chú thích đó; nêu trong báo cáo và đề nghị `/review-node` cho các trang ấy. Không sửa trang wiki trong skill này.

### 3. Lập danh sách thay đổi và dừng chờ duyệt

Đọc từng mục `[XEM]`. Với công thức, so tử số, mẫu số, Σ, ngoặc và chỉ số của từng dòng `$` với dòng OMML tương ứng mà script in ra; pandoc đôi khi làm rỗng nội dung trong ngoặc lớn, nên dựa vào OMML.

Áp các quy tắc ở mục "Quy tắc chuẩn hóa" để lập danh sách sửa. Trình người dùng trong chat:

1. Kết quả đối chiếu (một bảng ngắn theo mục A–H).
2. Nội dung sẽ bổ sung hoặc sửa theo docx, tách riêng khỏi phần chuẩn hóa ký hiệu: vị trí, nguyên văn chèn, và câu "bản sao sẽ có số dòng khác nguồn" nếu có chèn.
3. Danh sách dòng định sửa ký hiệu: số dòng, trước, sau, lý do.
4. Chỗ lệch không sửa được và lý do.
5. Các đường dẫn file sẽ ghi.

Chờ đồng ý rồi mới sang bước 4. Hỏi luôn có gắn địa chỉ điều-khoản-điểm không (cờ `--anchors`, xem dưới) nếu người dùng chưa nói. Nếu điểm a), b) nằm ở cột 0 như khoản, nói rõ và đề nghị xếp cấp bằng `nest_lists.py` + `anchors_by_marker.py` (xem "Điểm nằm ở cột 0"), kèm số đoạn tiếp nối sẽ được gán.

### 4. Ghi bản chuẩn hóa

Viết danh sách sửa vào một file JSON trong scratchpad (dùng công cụ Write, đừng viết qua heredoc của shell vì dấu `\` của LaTeX bị nuốt):

```json
[
  {"line": 1624, "old": "###### 3.2.1. Nguyên tắc chung", "new": "**3.2.1. Nguyên tắc chung**", "why": "heading N.N.N. → dòng in đậm"},
  {"line": 2256, "old": "Max [\\left(", "new": "Max \\left[ \\left(", "why": "ngoặc Max dùng \\left \\right"}
]
```

`old` phải xuất hiện đúng một lần trong dòng đó của nguồn. Một dòng có thể có nhiều edit.

Hai dạng mục dành cho nội dung, cả hai buộc phải chạy kèm `--docx`:

```json
[
  {"line": 43, "old": "bên nhân chuyển giao bắt buôc", "new": "bên nhận chuyển giao bắt buộc", "why": "sai chính tả so với docx", "content": true},
  {"after": 31, "insert": ["", "   - b) Tỷ lệ khả năng chi trả (sau đây gọi là tỷ lệ LCR);"], "why": "điểm b khoản 1 Điều 1 thiếu trong md"},
  {"after": 1628, "insert": ["| b) Nguồn vốn được bảo đảm bằng HQLA cấp 2A | 15% |"], "why": "hàng bảng thiếu trong md"}
]
```

- `"content": true` cho phép edit đó đổi chữ-số của dòng; dòng sau khi sửa phải khớp docx.
- `after` là số dòng **của nguồn** (0 = đầu file); `insert` là danh sách dòng, mỗi phần tử một dòng, `""` là dòng trống. Tự đặt dòng trống ngăn cách cho đúng nhịp của các mục liền kề.
- Script tách mỗi dòng chèn theo `|` và `<br>`, bỏ marker, rồi tìm từng đoạn trong docx. Đoạn nào không có trong docx thì cả lượt bị từ chối. Đoạn chứa `$` không kiểm tự động được; script đếm và nhắc so tay với OMML.

```bash
python -I scripts/apply.py --src "<nguồn>.md" --out "Claude outputs/<tên nguồn>_normalized.md" \
  --edits <scratchpad>/edits.json --fix-headings --sub-to-math [--nfc] [--anchors] \
  [--docx "<nguồn>.docx" --linemap "Claude outputs/<tên nguồn>_linemap.tsv"] \
  --changes <scratchpad>/changes.md --wiki 02_wiki --source-id <id>
```

| Cờ | Tác dụng |
|---|---|
| `--fix-headings` | đưa mỗi loại đơn vị về đúng một cấp; nối nhãn với tiêu đề (`Mục 3: TÊN MỤC`), kể cả khi tiêu đề nằm ở dòng dưới. Chạy sau `--edits`. Dòng có trong `edits.json` là bản cuối: cờ này không viết lại nó, chỉ kéo tiêu đề ở dòng dưới lên khi dòng đó còn thiếu tiêu đề (`**Chương I**` → `## Chương I` trong edits, cờ nối thành `## Chương I: …`). Giữ dấu ngăn có sẵn của nguồn (`.`, `:`, `Mục 1 - Tên`) và dấu ngoặc kép mở (`“Điều 3a.`) |
| `--sub-to-math` | `X<sub>y</sub>` → `$X_{y}$` trên các dòng chưa có edit riêng |
| `--nfc` | đưa Unicode về NFC (dùng khi mục A báo "NFC KHÔNG"); chữ hiển thị không đổi |
| `--anchors` | gắn địa chỉ vào cuối mỗi dòng khoản, điểm, tiết; suy cấp từ độ thụt, nên chỉ dùng khi điểm đã thụt dưới khoản (xem "Điểm nằm ở cột 0" dưới) |
| `--changes` | ghi bảng thay đổi ra file để dán vào báo cáo |
| `--docx` | bản gốc để kiểm từng đoạn chèn hoặc sửa nội dung; bắt buộc khi `edits.json` có `insert` hoặc `"content": true` |
| `--linemap` | khi có chèn dòng: ghi bảng `dòng nguồn → dòng bản sao` (TSV) |

Script kiểm năm điều trước khi ghi và thoát mã 1, không ghi gì, nếu một điều sai: cùng số dòng; dòng N cùng chữ-số với nguồn; dòng N cùng dấu ngoặc kép và ngoặc đơn với nguồn (phép so chữ-số bỏ qua dấu câu, nên dấu `“` hay `(` mất đi sẽ lọt nếu không kiểm riêng); độ thụt của dòng đã sửa không đổi; không dòng nào đổi ngoài danh sách. Khi nó từ chối, sửa `edits.json`; đừng nới phép kiểm.

Khi có chèn dòng, phép kiểm "cùng số dòng" áp cho phần lấy từ nguồn: các dòng của nguồn vẫn đủ, đúng thứ tự, chỉ có thêm dòng chèn xen vào. Script in "SỐ DÒNG ĐÃ ĐỔI" kèm dòng đầu tiên bị lệch. Từ đó trở đi, chú thích `d.N` của wiki đọc trên bản sao phải quy đổi qua bản đồ dòng; nói rõ điều này trong báo cáo và trong tin nhắn kết thúc lượt.

Ngoại lệ của "dòng N cùng chữ-số" ngoài sửa nội dung: khi `--fix-headings` kéo tiêu đề lên dòng nhãn, chữ của tiêu đề chuyển từ dòng dưới lên dòng trên. Với các dòng đó script kiểm trên toàn văn: chữ-số của bản sao đọc từ trên xuống phải trùng khít nguồn. Một chú thích wiki trỏ đúng vào dòng tiêu đề cũ sẽ gặp dòng trống ở bản sao; `apply.py` in danh sách chú thích bị chạm, nêu chúng trong báo cáo.

**Địa chỉ (`--anchors`).** Khoản và điểm trong md chỉ là mục danh sách, không tự cho biết thuộc điều nào. Cờ này thêm một chú thích HTML ở cuối dòng, không hiện khi render và không đổi số dòng:

```
1. Thông tư này quy định về… <!-- @Đ1.K1 -->
   - a) Hạn chế, giới hạn cấp tín dụng; <!-- @Đ1.K1.a -->
      - (i) Đối với ngân hàng… <!-- @Đ3.K14.b.i -->
- b) Đối với hạn mức cam kết… <!-- @PLI.A.I.5.b -->
```

Dạng địa chỉ: `Đ<điều>.K<khoản>.<điểm>.<tiết>` trong thân văn bản; `PL<số>.<phần>.<mục La Mã>.<mục số>.<điểm>` trong phụ lục. Địa chỉ trùng nhau được thêm hậu tố `~2`; script in số lượng trùng, và mỗi chỗ trùng là một chỗ cấu trúc md chưa rõ cần xem lại (thường là một tiêu đề nhỏ chưa được nhận ra). Tra một địa chỉ: `grep -n "@Đ16.K3.b " <bản chuẩn hóa>`.

**Điểm nằm ở cột 0.** Bản chuyển từ docx dạng HTML (văn bản hợp nhất VBHN, văn bản tải từ cổng pháp luật) thường để khoản `1.`, điểm `a)` và gạch đầu dòng cùng ở cột 0. Dấu hiệu: `audit.py` mục C đếm nhiều điểm a) nhưng "đoạn tiếp nối" gần 0, và `--anchors` chạy thử cho hàng chục địa chỉ trùng thiếu số khoản (`@Đ3.a~2`). `apply.py` chặn mọi thay đổi độ thụt, nên khi người dùng đồng ý xếp cấp, chạy hai script sau trên đầu ra của `apply.py` (không dùng `--anchors`):

```bash
python -I scripts/nest_lists.py --src <đầu ra apply.py> --out <scratchpad>/nested.md \
  [--keep-col0 170,233] [--dieu-word Điền] --log <scratchpad>/nest.tsv
python -I scripts/anchors_by_marker.py --src <scratchpad>/nested.md --out "Claude outputs/<tên nguồn>_normalized.md" \
  [--dieu-word Điền] [--preamble-prefix QĐ] [--section-key "TIÊU ĐỀ HEADING=KHÓA" ...]
```

- `nest_lists.py` thụt điểm dưới khoản (`   - a)`), điểm con và tiết dưới điểm, đổi gạch đầu dòng `\-` thành `- `, và thụt đoạn tiếp nối theo mục đứng ngay trên nó. Việc gán đoạn tiếp nối là diễn giải: đọc `nest.tsv`, tìm đoạn kết của cả Điều (thường sau một danh sách liệt kê ngắn, mở bằng "Ngoài…", "Trường hợp…") và đưa số dòng vào `--keep-col0`, rồi nêu các đoạn đó trong báo cáo. Script tự kiểm trước khi ghi: cùng số dòng, cùng chữ-số từng dòng, chỉ đổi khoảng trắng đầu dòng và dấu `- `.
- `anchors_by_marker.py` suy cấp từ loại ký hiệu (`1.`, `a)`, `a.1.`, `(i)`), không từ độ thụt. Điều của văn bản ban hành nằm trước Điều đầu tiên của văn bản được ban hành (`**Điều 1.** Ban hành kèm theo…`) mang tiền tố `--preamble-prefix`, để `QĐ.Đ1` không trùng `Đ1`. Điểm nằm ngoài Điều (thuyết minh, biểu mẫu) lấy đường dẫn từ nhãn heading, mở đầu bằng khóa của `--section-key`.
- `--dieu-word` thêm một từ đọc như "Điều" khi chính docx gõ sai (`Điền 11.`); ghi vào báo cáo đó là diễn giải.
- Sau hai script: dựng bản cuối bằng pandoc (`pandoc -f gfm -t html`) và kiểm không có `<pre>` (dòng thụt từ 4 dấu cách nằm ngoài danh sách sẽ thành khối code).

### 5. Kiểm sau khi ghi

- `python .claude/hooks/validate_wiki_page.py --verify-sources` phải báo 0 lệch, 0 thiếu: bằng chứng `01_sources/` không đổi.
- `git status` phải sạch (`Claude outputs/` nằm ngoài git).
- Chạy lại `audit.py` với `--md` trỏ vào bản chuẩn hóa: số `[SỬA]` phải giảm về mức đã định giữ, mục B và E không được xấu đi. Nếu đã bổ sung nội dung, số `[THÊM]` và "khác chữ" phải về 0 hoặc đúng bằng số báo động giả đã ghi nhận.
- `apply.py` đã in số chú thích wiki có dải dòng chứa dòng bị đổi; nêu con số đó trong báo cáo.

### 6. Viết báo cáo

Ghi `Claude outputs/doi-chieu-<YYYY-MM-DD>-<tên nguồn>.md` theo khung dưới. Số liệu lấy từ đầu ra của hai script, không ước lượng.

```markdown
# Đối chiếu <tên nguồn> `.docx` với `.md` và bản markdown chuẩn hóa

Ngày, đường dẫn hai file nguồn, đường dẫn bản chuẩn hóa. Một câu: bản chuẩn hóa không phải nguồn của wiki.

## Kết luận
Hai, ba câu: md có khớp docx không; bản chuẩn hóa đổi bao nhiêu dòng trên tổng số, thuộc loại gì.

## Kết quả đối chiếu
Bảng: hạng mục · cách kiểm · kết quả (theo mục A–H).

## Nội dung bổ sung và sửa theo docx
(Bỏ mục này nếu không có.) Từng chỗ chèn và từng dòng sửa nội dung: vị trí ở nguồn, nguyên văn, lý do.
Nếu có chèn: số dòng nguồn → số dòng bản sao, dòng đầu tiên bị lệch, đường dẫn bản đồ dòng.
Trang wiki đang dẫn vùng nguồn bị thiếu hoặc sai, đề nghị /review-node.

## Các dòng đã đổi ký hiệu
Bảng từ `--changes`, gom theo loại (heading, bảng, danh sách, công thức).

## Chỗ không đổi và lý do
Mỗi `[BÁO]` và mỗi `[XEM]` quyết định giữ: vị trí, hiện trạng, vì sao giữ.

## Kiểm tra đã chạy
Bảng: phép kiểm · kết quả.
```

Trong tin nhắn kết thúc lượt: nêu kết luận, số dòng đổi, các chỗ là diễn giải của agent (không phải nguyên dạng docx), và đường dẫn hai file.

## Quy tắc chuẩn hóa

Áp cho văn bản pháp quy tiếng Việt; với loại tài liệu khác, giữ nguyên tắc (một loại đơn vị một cấp, một kiểu viết cho một loại ký hiệu) và bỏ phần tên gọi.

**Heading — một loại đơn vị, một cấp.**

| Cấp | Đơn vị |
|---|---|
| `#` | tên văn bản (THÔNG TƯ, NGHỊ ĐỊNH) |
| `##` | Chương, Phụ lục |
| `###` | Mục, PHẦN |
| `###` | mục chữ cái `A.`, `B.` của phụ lục (ngang PHẦN) |
| `####` | Điều; mục La Mã (I., II.) |
| `#####`, `######` | mục `N.`, mục `N.N.` |
| dòng in đậm | mục `N.N.N.` trở xuống (markdown hết cấp heading) |

- **Cấp theo loại đơn vị, không theo style Word.** Một loại đơn vị nằm ở đúng một cấp trong cả file, kể cả khi Word đặt khác: phụ lục không có PHẦN thì mục La Mã của nó vẫn là `####` (chấp nhận nhảy cấp từ `##`), để máy đọc heading suy ra loại đơn vị từ cấp mà không cần biết ngữ cảnh. Người dùng đã chốt quy tắc này ngày 2026-11-12; mục D (so với style Word) chỉ còn để phát hiện heading bị sót hoặc thừa.
- **Nhãn và tiêu đề trên cùng một dòng.** Văn bản quy phạm Việt Nam trình bày "Chương II", "Mục 3", "Phụ lục I" trên một dòng căn giữa và tên của nó ở dòng dưới. Trong md, hai phần đó là một heading, cách nhau bằng dấu hai chấm: `### Mục 3: HẠN CHẾ, GIỚI HẠN CẤP TÍN DỤNG`. Thiếu tiêu đề trên dòng heading thì người đọc mục lục chỉ thấy "Mục 3" và bộ chia chunk mất tên mục.
  - Nhãn và tiêu đề cùng dòng, cách bằng dấu cách: thêm `: `. Nguồn đã tự viết dấu chấm hoặc hai chấm (`Mục 1. QUY ĐỊNH…`) thì giữ dấu của nguồn.
  - Tiêu đề nằm ở dòng dưới (dạng heading, in đậm hay chữ thường viết hoa): kéo lên dòng nhãn; dòng cũ của tiêu đề để trống, nên số dòng không đổi. Tiêu đề viết hoa bị ngắt thành nhiều dòng liền nhau thì nối cả.
  - `Điều N.` đứng một mình: kéo tên điều ở dòng dưới lên (`#### Điều 28. Tỷ lệ mua…`), chỉ khi dòng dưới ngắn và không kết thúc bằng dấu chấm, chấm phẩy hay hai chấm (thân điều thì có).
  - Dòng `*(Kèm theo Thông tư số …)*` dưới tên phụ lục không phải tiêu đề, giữ nguyên.
- Hai việc trên do `apply.py --fix-headings` làm tự động; `audit.py` mục C liệt kê trước từng dòng nó sẽ đổi. Đọc danh sách đó trước khi trình người dùng: phép nhận tiêu đề dựa trên chữ viết hoa, nên một dòng viết hoa không phải tiêu đề (tên biểu mẫu ngay dưới "Phụ lục") có thể bị kéo nhầm. Chỗ nào nhầm thì bỏ cờ và viết các dòng đúng vào `edits.json`.
- Loại đơn vị script chưa biết ("khác": Tiểu mục, Phần thứ nhất, tiêu đề tự do) được giữ nguyên cấp; xem tay và sửa bằng `edits.json` nếu cần.
- Điều được trích trong ngoặc kép (nội dung sửa đổi văn bản khác) không phải heading.

**Khoản, điểm, tiết, đoạn.**

- Khoản: `1.` ở cột 0. Điểm: `- a)` thụt bằng bề rộng marker cha (3 dấu cách sau `9.`, 4 sau `10.`). Tiết: `- (i)` thụt thêm 2. Đoạn tiếp nối: thụt bằng nội dung của mục chứa nó.
- `- 1.1.` phải là gạch đầu dòng vì `1.1.` không phải marker danh sách số của markdown.
- Không đổi độ thụt chỉ để cho đều: độ thụt là cấp lồng. Chỉ sửa khi mục C báo dòng thụt không khớp cấp cha và docx xác nhận cấp đúng. `apply.py` chặn mọi thay đổi độ thụt, nên chỗ này là `[BÁO]`. Ngoại lệ: cả văn bản để điểm ở cột 0 (không có cấp lồng nào để giữ) thì xếp cấp bằng `nest_lists.py` khi người dùng đồng ý (xem "Điểm nằm ở cột 0").
- Thứ tự đứt quãng (điểm `d)` sau `b)`, khoản 5 sau khoản 2) là dấu hiệu sót nội dung khi chuyển đổi, trừ khi nằm trong đoạn trích văn bản khác. Mục B thường đã báo chính đoạn bị sót kèm nguyên văn docx; chèn theo bước 2b. Nếu mục B không báo gì ở chỗ đó thì docx cũng thiếu: báo người dùng, không tự viết thêm.

**Bảng.**

- Mỗi bảng có cặp chú thích `<!-- BẢNG n | bắt đầu | vị trí: … | C cột × H hàng -->` và `<!-- BẢNG n | kết thúc -->`. Thiếu thì ghi `[BÁO]`: thêm chú thích là thêm dòng.
- Ô gộp ngang: nội dung ở ô đầu, các ô sau để trống. Ô gộp dọc: nội dung ở hàng đầu, các hàng dưới để trống. Không lặp lại nội dung.
- Nhiều đoạn trong một ô nối bằng `<br>`. Dấu `|` trong ô viết `\|`.
- Bảng dàn trang của Word (quốc hiệu, nơi nhận, chữ ký) là văn bản thường trong md.

**Công thức.**

- Công thức đứng riêng: `$$…$$` trên một dòng. Công thức nằm sau số thứ tự của danh sách (`1. $…$`) giữ `$…$`.
- Ký hiệu có chỉ số trong câu: `$E_{OnB}$`, không dùng `<sub>`.
- Ngoặc bao biểu thức cao (phân số, Σ): `\left( … \right)`, `\left[ … \right]`. Nhãn ngắn như `(\%)`, `(ASF)`: ngoặc thường.
- Chữ trong công thức: `\text{…}`. Số thập phân kiểu Việt trong `$`: `1{,}4`. Giữ nguyên chữ như docx (`Max`, không đổi thành `\max`).
- Khi ký hiệu trong câu viết khác công thức ngay cạnh nó (`Eoff` + chỉ số i so với `E_{off_{i}}`), viết theo công thức và ghi trong báo cáo rằng đó là diễn giải.

**Không bao giờ làm:** thêm hoặc sửa chữ, số mà docx không có (kể cả khi "rõ ràng là lỗi" của văn bản gốc); diễn đạt lại nội dung chèn; xóa dòng md vì docx không có; đổi thứ tự câu; thêm chữ tô sáng hay ghi chú vào thân văn bản; gộp hoặc tách dòng của nguồn; bỏ dòng trống.

## Khi người dùng muốn bản chuẩn hóa thay bản gốc

Đó là sửa `01_sources/`, trái quy tắc bắt buộc 1 của `CLAUDE.md`, và nằm ngoài skill này. Nêu hệ quả (SHA trong bản kê, bản đồ chunk, mọi chú thích theo số dòng phải được kiểm lại) và để người dùng quyết định riêng. Nhờ ràng buộc giữ số dòng, việc thay thế về sau không làm lệch chú thích nào; đó là lý do giữ ràng buộc này ngay cả với nguồn chưa có trang wiki nào dẫn.
