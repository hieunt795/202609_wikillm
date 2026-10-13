# Handoff — lint, review 47 trang LCR40, nạp hết basel_lcr, bốn trang tổng quan LCR

## Kết quả

**Chưa commit gì trong phiên này.** Working tree có 94 mục: 72 file sửa (549 dòng thêm, 324 dòng bớt) và 22 file mới, gồm cả handoff `2026-10-12-1658` của phiên trước và file này. HEAD vẫn là `a5c13df`.

Tám operation, theo thứ tự trong `log.md` ngày 2026-10-13:

- **Lint** (3 mục log): phạm vi 4 lượt ingest LCR40. Người dùng duyệt nhóm S, O, L, R, I, rồi C1, C2; **bỏ qua nhóm G**. Kết quả: 8 stub mới, `index.md` tách nhóm LCR, khoảng 25 trang nhận link, 6 chú thích. Báo cáo: `Claude outputs/lint-2026-10-13-886.md`.
- **Review** (2 mục log): 47 trang LCR40 đối chiếu với `LCR.md` d.700–1323. 46 trang đặt `reviewed: 2026-10-13`, `reviewed_by: model`. Bốn claim đã sửa: `committed-facility-drawdown-rates-…`, `secured-lending-inflow-rates-…`, `lcr-retail-deposits-split-…`, `a-liquidity-facility-backstops-…`. Một trang giữ lại với `⚠️ Conflict` (mục Blocker). Lượt 43 trang vượt ngưỡng 5 trang mỗi lượt của §4, làm theo duyệt trực tiếp của người dùng, ghi một mục log.
- **Research**: trang tổng quan thanh khoản ở 993 từ nên không dồn thêm; tạo trang `lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap`. Báo cáo: `Claude outputs/research-2026-10-13-lcr-net-outflows-overview.md`.
- **Ingest LCR31**: 7 trang mới (trần sử dụng, Option 1–3, ba nguyên tắc, chứng minh thiếu HQLA, nghĩa vụ giám sát); stub `alternative-liquidity-approaches` thành draft; 4 trang có sẵn nhận một câu.
- **Ingest LCR90, LCR99, phần còn lại của LCR30**: trang `sharia-compliant-banks-…`, stub `intraday-liquidity`, 5 trang có sẵn nhận claim. **`basel_lcr` đã phủ hết.**
- **Bốn trang tổng quan LCR** (`type: analysis`), mỗi nhóm index một trang, theo yêu cầu của người dùng về bảng thành phần chi tiết:
  - tử số: `the-hqla-stock-weights-three-asset-levels-by-haircut-under-40-and-15-percent-caps`
  - mẫu số gộp: `lcr-net-outflows-weight-liabilities-…`
  - dòng ra: `lcr-cash-outflows-apply-run-off-and-drawdown-rates-to-four-blocks-of-liabilities-and-commitments`
  - dòng vào: `lcr-cash-inflows-count-contractual-receivables-by-counterparty-under-a-75-percent-cap`
- **`index.md`**: nhóm "Thanh khoản và nguồn vốn" tách thêm bốn nhóm: "LCR: kho HQLA (tử số)", "LCR: tổng dòng tiền ra ròng (mẫu số)", "LCR: dòng tiền ra", "LCR: dòng tiền vào".
- **Quyết định của người dùng trong phiên**: ba chỗ bảng LCR99 ghi 10%, 50%, 0–5% trong khi LCR40 ghi "tối thiểu" hoặc "hoặc thấp hơn" không đánh Conflict ("tối thiểu là dạng chỉ tiêu"). Chưa ghi vào `decisions.md`.

## Kiểm tra đã chạy

- `--all` (lần cuối): 907 trang, 0 vấn đề, 0 mồ côi, 0 sót index.
- `--coverage basel_lcr`: 9 chunk, phủ 8, miễn 1.
- `--graph` (lần cuối): 907 trang, 4.572 link (500 mạnh), 825 link có loại, 449 cặp nhóm có link chéo; ảnh chụp đã lưu. Hai link đổi loại so với HEAD: `operational-deposits` → `total-expected-cash-inflows` (drives ⇒ related), `retail-term-deposits-…` → `lcr-retail-deposits-split-…` (contrasts ⇒ governed_by). Điểm nối duy nhất giữa "Thanh khoản và nguồn vốn" và "Thị trường tiền tệ, chuẩn lãi suất RFR và repo" là trang `bank-liquidity-rules-pair-…`.
- `--size`: 0 trang vượt ngưỡng trong số trang viết hoặc sửa ở phiên này; trang `bank-liquidity-rules-pair-…` ở đúng 1.000 từ.
- `--style`: chỉ xem cho các trang mới, không báo gì.
- `--lint` trọn bộ: chạy ở đầu phiên (886 trang), **chưa chạy lại** sau hai lượt ingest.
- `--verify-sources`: chỉ chạy trong `--lint` đầu phiên, chưa chạy lại.

## Blocker

Hai `⚠️ Conflict` chờ người dùng đối chiếu bản gốc trên bis.org; cả hai đã ghi `_inbox.md`:

- `downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade`: cùng một FAQ, `LCR.md` d.978–980 ghi "40.51, 40.52 and 40.56", d.1008–1010 ghi "…40.55". Trang chưa có `reviewed`.
- `the-hqla-stock-weights-…`: ngưỡng dưới của trái phiếu doanh nghiệp Level 2B là BBB− ở 30.45 (d.325–332), bảng 99.1 (d.1352) ghi "A+ and BBB". Có thể dấu trừ mất khi chuyển file.

## Việc còn lại

Từ phiên này:

- Commit toàn bộ thay đổi (chỉ khi người dùng yêu cầu; xem `git status` và `git diff` trước).
- 13 trang mới chưa có `reviewed`: 7 trang LCR31, `alternative-liquidity-approaches`, `sharia-compliant-banks-…`, bốn trang tổng quan. Người dùng nói chưa cần review vội.
- Trang `securities-lending-programmes-and-central-bank-collateral-swaps` viết "giữa các bên thị trường", đoạn 40.46 (d.917) không có; chờ `/review-node` (đã ghi `_inbox.md`).
- Chú thích trên ba trang tổng quan dòng ra, dòng vào, tử số ghi theo bảng (một dải đoạn cho cả bảng), lấy từ trang con đã review, không mở lại nguồn cho từng dòng.
- Trang `bank-liquidity-rules-pair-…` ở đúng 1.000 từ; lượt bổ sung kế tiếp (NSFR) phải tách trước. Trang này chưa nhắc LCR31.
- Trang `lcr-net-outflows-…` đứng đầu nhóm "LCR: tổng dòng tiền ra ròng (mẫu số)"; các đoạn của nó lặp một phần nội dung hai trang tổng quan dòng ra và dòng vào.
- Trang `hqla-insufficiency-…`: đã bỏ phương trình "phần thiếu = cầu − cung" do agent viết lại từ 31.27 để trang xuống dưới 1.000 từ.
- Lệch dấu câu trong nguồn, không đánh Conflict: 40.64 khoản (5) "insurance companies, fiduciaries, and beneficiaries" và khoản (6) "insurance companies' fiduciaries and beneficiaries".
- Quyết định "tối thiểu là dạng chỉ tiêu, không đánh Conflict" chưa có trong `decisions.md`.
- Nhóm G của lint (người dùng bảo bỏ qua, chỉ ghi nhận): 11 file nguồn chưa kê; `LCR.md` bị cắt giữa câu ở d.758 (chú thích "bảo hiểm đầy đủ") và d.940 (FAQ2 của đoạn 40.47).
- Stub: cả wiki khoảng 38 stub; `net-stable-funding-ratio-nsfr` và `intraday-liquidity` chờ `basel/NSF/` và nguồn khác; `deposit-insurance` chờ `cargill_central_bank_policy`.
- `_inbox.md` còn 12 khái niệm ALM chờ ingest `basel/NSF/`, `basel/IRRBB-d368/`.
- `--coverage` tính theo heading: một mục dài có thể báo đã phủ khi mới có trang trích tới phần đầu.
- Link chưa có loại: 4.572 trừ 825. Tỷ lệ link mạnh khoảng 11% (500 trên 4.572), dưới mục tiêu 15–30% của kế hoạch.
- Phần kiểm "tổng quan nhóm đã cũ" trong `--relations` chưa cài.

Chép từ handoff `2026-10-12-1658` và các handoff trước, chưa xử lý:

- Ba trang tách từ `repo-specialness-…` chưa có `reviewed`: trang gốc, `liquidity-makes-bonds-of-similar-duration-trade-at-different-yields-with-t-bills-lowest`, `treasury-bills-and-short-coupon-bonds-are-priced-apart-and-need-separate-fitted-curves`. Claim đã khớp nguồn ở lượt review 2026-10-10; lint không đặt `reviewed`.
- Hai trang vượt ngưỡng kích thước: `multitiered-irrbb-regulatory-framework-…` (1.236 từ, nên tách chuỗi CRD và chuỗi CRR) và `supervisory-irrbb-reporting-…` (một đoạn 730 từ). `supervisory-outlier-test-…` dài 1.144 từ.
- 11 file nguồn chưa kê, người dùng muốn đăng ký khi ingest: `basel/BaselFramework/`, `basel/IRRBB-d368/`, `basel/LEV/`, `basel/NSF/`, `Clippings/ALM P11 TT50(P4)…`, và 6 file dưới `vietnam-regulator/alm/`.
- `tata_bank_alm` còn 15 mục chưa phủ theo `--coverage`, rải ở Ch.1, Ch.2 cụm A và B, Ch.3, Ch.5, Ch.6.
- Message commit `1231ca7` ghi "review 57 trang", đúng là 48; sửa cần người dùng yêu cầu force push.
- Việc còn mở ghi ở `decisions.md`: ngoại lệ ingest cho văn bản quy phạm pháp luật (TT50/2026) chưa có trong schema §10.
- Đối chiếu con số duration 2,17 (trang replicating portfolios) với PDF gốc của Tata nếu có.
- `--graph` chưa nhận ra thao tác đổi tên trang (in thành "LINK MẤT").
- Chưa xuất báo cáo research cho bốn nhóm của lô C vào `Claude outputs/`.
- Câu chưa truy được tới dòng nguồn trên hai trang tổng quan đầu tiên:
  - Trang thanh khoản, đoạn 1 (rủi ro sinh từ chuyển đổi kỳ hạn, dẫn tới rút tiền hàng loạt) và đoạn 9 (vốn vay ngân hàng trung ương phụ thuộc tài sản thế chấp; định nghĩa HQLA hẹp hơn danh mục tài sản bảo đảm; haircut và chuỗi tái thế chấp).
  - Trang IRRBB, đoạn cuối (mối nối sang tiền gửi không kỳ hạn, FTP, SVB).
- Trong 14 trang IRRBB đã review: trang `receiver-interest-rate-swaps-…` còn trích d.1550 cho con số 3,63, mới xác nhận ở d.1517. Các câu nối không có chú thích chỉ được kiểm bằng tìm từ khoá.
- Hàng đợi review: 11 trang trục chưa review của nhóm thanh khoản (chỉ `liquidity-risk` đã review; `high-quality-liquid-assets-hqla`, `liquidity-coverage-ratio-lcr`, `lcr-stress-scenario-…` vừa nhận thêm claim); các trang ingest từ Clippings ngày 2026-09-22 và 23 chưa review, có cùng kiểu lỗi đã gặp (tính từ mạnh, biến mô tả thành nghĩa vụ, câu kết không có nguồn).
- Bộ tiêu chí của `query/evals/evals.json` cần viết lại cho khó hơn trước khi dùng để quyết lô D (vector).
- Bảng tổng hợp của `skill-creator` (`benchmark.json`) ra toàn số 0; số liệu đúng nằm ở `Claude outputs/query-workspace/iteration-1/grading-summary.md`.
- Ngưỡng thông báo của `--graph` là số tạm.
- `index.md`: gán nhóm theo mục cũ, chưa soát từng trang; nhóm "Công cụ và cơ chế vận hành chính sách tiền tệ" nên tách khi ingest thêm.
- `.claude/docs/luong-van-hanh.html` chưa có các lệnh đồ thị và luật quan hệ, còn ghi "§1–§12" và "Đọc schema: Không" cho query.
- Ba file bản thử trong `Claude outputs/` đã bị thay thế (`wiki_graph.py`, `relations-draft.tsv`, `graph-snapshot.json`), chưa xoá; xoá cần người dùng xác nhận.
- Loại quan hệ của các link là phán đoán của model; chưa ai soát. Người dùng chưa mở `Claude outputs/graph-map-alm.html` và `Claude outputs/query-workspace/iteration-1/review.html`.
- Kế hoạch đồ thị nằm ngoài repo: `~/.claude/plans/l-p-k-hoa-ch-i-u-immutable-goblet.md`. Lô A, B, C xong; lô D tuỳ chọn, chưa mở.
- Công thức kho HQLA (30.38) mất trong `LCR.md` d.229, công thức điều chỉnh trần 15% (d.233) hỏng ký tự; trang trần 40%/15% dùng công thức dựng lại từ lời văn, cần đối chiếu bản gốc trên bis.org.
- Câu minh hoạ ngoài nguồn trên các trang LCR (ví dụ 150/100, repo 7 ngày, chênh phí 25 điểm cơ bản…); người dùng chưa nói giữ hay bỏ.
- `BaselFramework/BaselFramework.md` chứa lại chương LCR (d.14570 trở đi); khi ingest cần ghi `bỏ qua` cho phần trùng.
- Hook `PreToolUse` cho `--guard-sources` chưa được thử với một lệnh ghi thật vào `01_sources/`.
- Nếu `enabledPlugins` ở `settings.local.json` không có tác dụng, chuyển 5 dòng đó sang `~/.claude/settings.json`.
- Các map trong `Claude outputs/research-map-*.md` lập trước khi `main` lùi về `6adf39e`; cần quét lại trước khi dùng.
- `lint` chưa có evals; chưa chạy 3 eval `research` bằng `skill-creator`.
- Global `CLAUDE.md` ghi model mặc định Haiku 4.5, `~/.claude/settings.json` đặt `"model": "opus"`.
- `README.md:27` liệt kê skill thiếu `research`.
- `--coverage`: 74 chunk `[x]` còn mục chưa phủ; quyết định [2026-09-26] là hạ về `[~]`, chưa ingest bù.
- Chưa áp 3 commit sửa văn phong `8c32c43`, `51d5c3c`, `b8ee3d6`; chờ người dùng quyết.
- Vặt trong schema và hook: `ingest/SKILL.md:13` ghi "(§1–§12)"; §4 có hai hàng cùng tên "Kích thước 1 trang"; schema, skill và docstring hook còn dùng dạng `§7.5`; docstring `--tags`, `--style` hỏng chữ.
- Hook kiểm trang không hiểu `[[trang\|nhãn]]` trong bảng markdown (báo link chết); trong bảng phải dùng `[[trang]]` không nhãn.
- Chưa thử trong phiên thật: yêu cầu sửa một file trong `01_sources/` bị từ chối; gọi "dùng source-verifier kiểm trang cpi".

## Bước tiếp theo

- Commit các thay đổi của phiên khi người dùng yêu cầu.
- `/ingest` nguồn `basel/NSF/` (NSFR): chưa có trong bản kê, lượt đầu gồm đăng ký nguồn và dựng bản đồ chunk; tách trang `bank-liquidity-rules-pair-…` trước khi thêm NSFR vào đó.
- Người dùng đối chiếu hai chỗ Conflict với bản gốc bis.org; có kết quả thì sửa trang và đặt `reviewed` cho `downgrade-triggers-…`.
- `/review-node` cho 13 trang mới và trang `securities-lending-programmes-…` khi người dùng muốn.

Các script dùng trong phiên (`add_reviewed.py`, `merge_lcr99.py`) nằm trong thư mục tạm của phiên và sẽ mất. Cách làm: sửa file bằng Python đọc và ghi với `newline=''` để giữ ký tự xuống dòng, rồi `--all`, `--coverage`, `--graph`, ghi log.
