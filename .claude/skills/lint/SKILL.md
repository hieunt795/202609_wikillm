---
name: lint
description: Kiểm tra sức khoẻ wiki 02_wiki — trang mồ côi, mâu thuẫn tồn đọng, trang stale, trùng lặp, vi phạm Atomic, vi phạm quy ước title, nợ stub, sai vòng đời status, nhiễu OCR còn sót từ nguồn, nợ inbox chưa triage. Dùng khi người dùng muốn lint, kiểm tra wiki, rà soát, health check, tìm trang mồ côi, kiểm tra liên kết, audit wiki, dọn dẹp wiki.
---

# Lint — kiểm tra sức khoẻ wiki

Chạy sau mỗi 10 lượt ingest hoặc theo lịch (§4). Kiểm tra chi tiết luật ở `00_schema.md` §5–§9, §11.

**Lint chỉ báo cáo. Tuyệt đối không tự sửa.** Xuất báo cáo, chờ người xác nhận hướng xử lý.

## Quy trình hai lượt

**0. Chạy trình kiểm trang hàng loạt trước mọi thứ khác:**

```bash
python .claude/hooks/validate_wiki_page.py --all
```

Hook `PostToolUse` chỉ bắt được tool `Write|Edit` — file ghi bằng shell (`cat >`, script, `sed -i`) đi vòng qua nó hoàn toàn. Chế độ `--all` quét lại tất cả.

**Script phủ đúng những thứ sau, không hơn:** frontmatter đủ trường, `type` và `status` hợp lệ, tên file khớp title, `sources` không rỗng, `last_updated` đúng dạng ngày, heading trong thân bài, `[[wikilink]]` trỏ tới trang không tồn tại, link dồn thành danh sách, chú thích §7.5 với trang có `last_updated` từ 2026-09-14, title §8 dạng danh từ cho `case`/`analysis`, và **trang mồ côi theo chiều backlink**.

**Script KHÔNG phủ:** mâu thuẫn tồn đọng, trang stale, trùng lặp entity, vế *độ dài kèm outlink thấp* của tiêu chí Atomic, nợ stub, sai vòng đời status, nhiễu OCR, nợ inbox. Bảy tiêu chí này vẫn phải kiểm tay.

Đừng suy ra phạm vi của script từ tên tiêu chí. Tiêu chí *Trang mồ côi* có hai vế; trước 2026-09-14 script chỉ phủ vế outlink, và việc giả định nó phủ cả vế backlink là nguyên nhân để lọt 12 trang mồ côi qua hai lượt ingest.

**1. Lượt rẻ — quét frontmatter toàn bộ `02_wiki/`.** Không đọc full content.

**2. Đối chiếu 10 tiêu chí:**

| Lỗi | Cách phát hiện |
|---|---|
| Trang mồ côi | outlink = 0 (không có `[[wikilink]]` nào trong thân bài) **HOẶC** backlink = 0 (không trang nào trỏ tới). Tiêu chí outlink **không** áp cho `status: stub`. Cả hai vế do bước 0 tự kiểm; lệnh grep thủ công ở cuối file chỉ dùng khi cần truy một trang cụ thể |
| Mâu thuẫn tồn đọng | còn `⚠️ Conflict` chưa xử lý |
| Trang stale | `last_updated` cũ hơn nguồn liên quan đã ingest sau đó |
| Trùng lặp entity | hai trang cùng mô tả một thực thể. Khi so khớp văn bản, **cắt bỏ chuỗi chú thích §7.5** `(<nguồn>, Ch.X, <mục>, d.…)` trước — giống như đã cắt `[[wikilink]]`; nếu không, mọi trang cùng trích một mục sẽ báo trùng giả (lượt audit 2026-09-14: `seigniorage` và `the-inflation-tax-...` báo 7 cụm trùng mà toàn bộ là chuỗi chú thích) |
| Vi phạm Atomic | thân bài có heading cấp 2+; hoặc `[[wikilink]]` dồn thành danh sách "xem thêm" không kèm lý do; hoặc độ dài lớn kết hợp số outlink thấp — xem ghi chú bên dưới (§5, §7) |
| Vi phạm title | `case`/`analysis` đặt title danh từ thay vì câu khẳng định; title phủ định; title mơ hồ (§8) |
| Nợ stub | `status: stub` chưa được ingest nội dung sau 3 lượt ingest kể từ khi tạo (§9) |
| Sai vòng đời status | `stable` nhưng có nguồn mới ingest sau `last_updated` mà chưa chuyển `stale` (§9) |
| Nhiễu OCR còn sót | thân bài chứa token đặc trưng lỗi OCR bị copy nguyên từ nguồn — xem bộ mẫu bên dưới |
| Nợ inbox | mục trong `_inbox.md` chưa được triage sau 3 lượt lint (§11) |

Tiêu chí **Nhiễu OCR** cần quét thân bài (không phải frontmatter), và **bỏ `[[wikilink]]` ra khỏi phạm vi quét** — tên trang kebab-case không phải văn bản. Sáu họ mẫu:

| Họ mẫu | Ví dụ trong nguồn IMF |
|---|---|
| `l` / `O` đứng thay chữ số hoặc chữ `I` hoa | `lmbalance`, `tO`, `DeficitlO` |
| Số chú thích cuối chương dính vào từ | `Economiesl3`, `lmbalance12` |
| Chữ số bị tách bởi khoảng trắng | `1 993`, `1 989` |
| HOA–thường lẫn trong một từ | `COLmtries` |
| Nguyên âm nhân đôi bất thường | `Waaes` (wages) |
| Rác markdown của bản OCR bị copy | `<sup>`, `<span id=`, `[#page-`, ký tự thay thế `�` |

**Giới hạn đã biết:** bộ mẫu không bắt được lỗi OCR tạo ra *từ có thật* (`set our` thay `set out`, `Governmenr` thay `Government`) — loại này chỉ lộ ra khi đọc. Đây là lý do tiêu chí chỉ là lưới lọc thô, không phải bảo chứng.

Nhiễu OCR là **lỗi sao chép nguyên văn**: nếu một token OCR lọt được vào trang wiki thì câu chứa nó gần như chắc chắn vi phạm luật viết lại bằng lời mình (§7.4). Báo cáo kèm cả hai lỗi.

Vế thứ ba của tiêu chí **Vi phạm Atomic** — *độ dài lớn kèm outlink thấp* — chỉ là điều kiện kích hoạt rà soát, **không phải căn cứ để tách**. Trang dài kèm nhiều outlink là trang đầu mối và không cần xử lý; trang dài mà gần như không trỏ ra đâu là trang đang chứa nội dung thay vì liên kết tới trang chứa nội dung đó. Gặp trường hợp sau thì chạy ba phép kiểm ở `00_schema.md` §5 rồi mới kết luận. Độ dài đứng một mình không mang thông tin: đo trên toàn wiki, tương quan giữa độ dài với số outlink là r = +0,07 và với số backlink là r = −0,09.

Lệnh tính ba đại lượng cho mọi trang:

```bash
python3 - <<'EOF'
import re,glob,os,collections
pg={}
for p in sorted(glob.glob("02_wiki/*.md")):
    n=os.path.basename(p)[:-3]
    if n=="index": continue
    t=open(p,encoding="utf-8-sig").read(); pg[n]=t[t.index("---",3)+3:]
out={n:{x.split("|")[0].strip() for x in re.findall(r"\[\[([^\]]+)\]\]",b)} for n,b in pg.items()}
back=collections.defaultdict(int)
for n,ls in out.items():
    for l in ls:
        if l in pg and l!=n: back[l]+=1
def wc(n): return len(re.sub(r"\(imf_macro_accounting[^)]*\)|\(d\.[^)]*\)","",re.sub(r"\[\[([^\]|]+)\|?[^\]]*\]\]",r"\1",pg[n])).split())
for n in sorted(pg,key=lambda x:-wc(x)):
    print("%4d tu | out=%-2d | back=%-2d | %s"%(wc(n),len(out[n]&set(pg)),back[n],n))
EOF
```

**3. Lượt đắt — chỉ mở full content các trang bị flag ở lượt 2.**

**4. Xuất báo cáo** nhóm theo loại lỗi, mỗi mục nêu trang + lý do + hướng sửa đề xuất. Không thực hiện sửa.

Kèm mục **triage `_inbox.md`**: liệt kê từng mục còn tồn, mỗi mục đề xuất đúng 1 trong 3 kết cục — nâng thành trang wiki, gộp vào trang đã có, hoặc xoá (§11). Lint chỉ đề xuất; người dùng quyết định và thực hiện.

**5. Append 1 dòng vào `log.md`:** `[YYYY-MM-DD] lint <số trang quét> → <tóm tắt số lỗi theo loại>`.

## Lưu ý về chi phí

Ở quy mô vài chục trang (dưới ~150 KB toàn thư mục), lượt 1 quét frontmatter toàn bộ vẫn rẻ. Số trang hiện tại lấy từ `02_wiki/index.md`, không ghi cứng ở đây. Khi wiki vượt ~200 trang, cân nhắc giao lượt 1 cho subagent `Explore` để không đổ toàn bộ kết quả quét vào context chính — nhưng chỉ làm khi người dùng yêu cầu rõ.

Tiêu chí backlink cần quét chéo toàn bộ `02_wiki/` một lượt, không grep từng trang một.

**Dùng đúng lệnh này** — `grep "[[<tên-trang>]]"` là SAI và sai cả hai chiều: `[[...]]` bị hiểu là bracket expression nên `types-of-inflation` ra 0 file (thực tế có 3 trang trỏ tới) còn `real-wages` ra 52/52 file. Lệnh đúng:

```bash
grep -rlE "\[\[<tên-trang>(\||\])" 02_wiki/ --exclude=index.md
```

`-E` cộng dấu `\[` thoát nghĩa để `[[` là chuỗi thật; nhánh `(\||\])` bắt cả `[[tên-trang]]` lẫn `[[tên-trang|nhãn]]` (§6); `--exclude=index.md` để mục lục không bị tính thành backlink.

Tiêu chí nhiễu OCR cũng chạy bằng grep một lượt trên cả thư mục — không mở full content chỉ để quét. Trang nào có hit mới mở ở lượt 3 để xác nhận (tên riêng nước ngoài dễ báo giả: `Paasche` khớp mẫu nguyên-âm-nhân-đôi nhưng là tên người có thật).
