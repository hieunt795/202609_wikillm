# Session Handoff: 2026-09-23-0930 Clippings Cụm 2 Ingest

## 1. Kết quả phiên

- **Nạp nguồn Cụm 2 — Điều Hành Fed, Repo & Trái Phiếu Kho Bạc (Hoàn tất 100% — 15 bài viết)**:
  - Tạo mới **8 trang concept atomic** (`02_wiki/`), tuân thủ triệt để không heading trong thân bài (§7.1), câu đầu định nghĩa trực tiếp (§7.2), đan cài wikilink tự nhiên (§7.3), và chú thích tọa độ nguồn chi tiết theo từng file (§7.5):
    1. `treasury-repo-market-operates-through-three-distinct-client-segments`: Khung phân khúc C2D (MMFs-Deal), Interdealer (FICC) và D2C (Hedge Funds); dealers làm trạm trung chuyển trung tâm; chênh lệch spread định giá theo kỳ chốt sổ báo cáo.
    2. `repo-rate-spikes-transmit-to-federal-funds-rate-via-fhlb-arbitrage`: Cơ chế lan truyền căng thẳng thanh khoản repo sang EFFR qua kinh doanh chênh lệch giá của FHLB khi thanh khoản Fed giảm xuống dưới 10% GDP.
    3. `quantitative-tightening-differs-from-quantitative-easing-through-balance-sheet-asymmetry`: Tính bất đối xứng giữa QE (mở rộng bảng cân đối) và QT (rút dự trữ sơ cấp Reserves -> UST mà không nhất thiết thu hẹp bảng cân đối ngân hàng); giới hạn dừng ở thanh khoản khan hiếm.
    4. `persistent-fiscal-deficits-operate-as-a-monetary-force-expanding-private-balance-sheets`: Thâm hụt tài khóa dai dẳng bơm tiền gửi và tạo tài sản an toàn 0% risk weight tái cấu trúc hệ thống ngân hàng, phân định với bản chất hoán đổi tài sản của QE.
    5. `bank-absorption-of-sovereign-debt-is-governed-by-a-regulatory-triangle`: Tam giác quản trị SLR (Quantity), IRRBB (Duration), Stress Testing (Resilience); nguyên lý rủi ro tín dụng thấp không đồng nghĩa với rủi ro bảng cân đối thấp.
    6. `sovereign-debt-absorption-requires-dealer-intermediation-capacity-beyond-investor-demand`: Phân định giữa nhu cầu sở hữu cuối cùng và năng lực trung gian lưu kho/tài trợ repo của primary dealers trong việc hấp thụ nợ công.
    7. `treasury-buybacks-function-as-debt-management-rather-than-monetary-yield-curve-control`: Bản chất mua lại trái phiếu off-the-run để giải phóng dung lượng dealer; phân định ranh giới giữa quản trị nợ của Kho bạc và chính sách tiền tệ/YCC của NHTW.
    8. `central-banks-face-policy-reaction-traps-when-energy-supply-shocks-elevate-headline-inflation`: Bẫy hàm phản ứng của NHTW khi duy trì thắt chặt quá mức vì áp lực uy tín trước cú sốc năng lượng đẩy CPI bề nổi; đối chiếu qua TIPS breakevens và SOFR curve.
  - **Nâng cấp 3 trang từ `status: stub` lên `status: draft`** (giảm nợ stub):
    - `repurchase-agreement`: Bổ sung cơ chế cấu trúc 3 phân khúc C2D/Interdealer/D2C và lan truyền thanh khoản sang EFFR.
    - `reverse-repurchase-agreement`: Bổ sung vai trò cơ chế ON RRP trong tổng thanh khoản Fed và tiền đề kích hoạt nhạy cảm repo.
    - `quantitative-easing`: Bổ sung bản chất hoán đổi tài sản (asset swap) phân biệt với QT và thâm hụt tài khóa.
  - **Cập nhật liên kết 2 chiều với 5 trang hiện có**:
    - `risk-based-capital-requirements-aim-to-constrain-leverage-but-incentivize-regulatory-arbitrage`: Nối vào tam giác quy định hấp thụ nợ công.
    - `supervisory-stress-testing-provides-forward-looking-macroprudential-evaluation`: Nối vào đỉnh kiểm tra sức chống chịu rủi ro duration.
    - `interbank-market`: Nối vào kênh lan truyền repo sang lãi suất liên ngân hàng qua FHLB.
    - `core-inflation-strips-out-one-time-price-level-jumps`: Nối vào bẫy hàm phản ứng của NHTW khi đối mặt cú sốc cung tạm thời.
    - `expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads`: Nối vào vai trò TIPS hòa vốn dài hạn trong việc giải mã bẫy hàm phản ứng.
  - **Quản trị hệ thống**:
    - Cập nhật bản đồ chunk `03_state/clippings.md`: Đánh dấu hoàn tất `[x]` toàn bộ 15 file của Cụm 2, nâng `last_updated: 2026-09-23`.
    - Cập nhật mục `## Sources` và mục lục chủ đề trong `02_wiki/index.md` bổ sung phần `Điều hành Fed, thị trường Repo và nợ công Kho bạc (Clippings — Cụm 2)`.
    - Ghi nhận nhật ký vận hành vào `log.md`: `## [2026-09-23:09-28-36] ingest | clippings Cụm 2...`

## 2. Kiểm tra đã chạy

- `python .claude/.claude/hooks/validate_wiki_page.py --verify-sources`: 182/182 file nguồn trong bản kê toàn vẹn, 0 lệch/thiếu checksum, 0 file chưa kê.
- `python .claude/.claude/hooks/validate_wiki_page.py --all`: 481/481 trang quét, 0 lỗi schema, 0 lỗi heading, 0 link chết, 0 trang mồ côi.

## 3. Việc còn lại & Bước tiếp theo

- Nguồn `clippings` còn lại 4 cụm (46 bài viết):
  - **Cụm 3**: Lạm Phát Phi Tuyến & Báo Cáo Vĩ Mô Quốc Tế (Gianluca Benigno, BIS, CPI Reports) — 4 file (+ các báo cáo CPI định kỳ). *(Đề xuất ưu tiên kế tiếp)*
  - **Cụm 4**: Thị Trường Ngoại Hối Châu Á, Tỷ Giá & Carry Trade (CNY, JPY/Yen) — 9 file.
  - **Cụm 5**: Cơ Chế Phản Ứng Của NHTW & Forward Guidance — 16 file.
  - **Cụm 6**: Phương Pháp Luận & Rủi Ro Cấu Trúc Khác — 17 file.
- Quy trình tiếp theo: Thực hiện Bước 0 của `/ingest` cho cụm tiếp theo (đọc tổng hợp, thảo luận 3–5 ý chính và chốt danh sách trang trước khi ghi).
- Blocker: Không có.
