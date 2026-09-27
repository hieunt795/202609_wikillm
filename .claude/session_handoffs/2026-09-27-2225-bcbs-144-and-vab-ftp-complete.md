# Handoff — Hoàn tất Ingest vab_ftp_methodology và Chuẩn hóa 17 Nguyên tắc BCBS 144 (2026-09-27)

## Kết quả Phiên làm việc

### 1. Hoàn tất 100% Nguồn `vab_ftp_methodology` (2.118 dòng / 243 KB)
- Rà soát toàn bộ 4 chunk, đặc biệt bóc tách chi tiết từng sản phẩm FTP theo chỉ đạo của người dùng và nguyên lý Atomic (§5: mỗi sản phẩm 1 node riêng biệt):
  - **14 concept mới ở Chunk 2**: 6 node VOF tiền gửi (`bullet-term-deposit`, `installment-deposit`, `non-maturity-deposit`, `margin-and-escrow`, `retail-certificate-of-deposit`, `early-deposit-redemption`) và 8 node COF tín dụng/tài sản (`straight-term-bullet`, `amortizing-loan`, `non-maturity-credit`, `promotional-hybrid`, `overdue-loan`, `extended-loan`, `corporate-bond-portfolio`, `loan-prepayment`).
  - **2 concept mới ở Chunk 3**: `entrusted-oda-and-foreign-funding-ftp-mechanism-aligns-bilateral-project-cash-flows` và `ftp-governance-exception-handling-authorizes-ceo-and-alco-interventions`.
  - Cập nhật 6 trang ở Chunk 4, hoàn thiện hệ thống biểu mẫu MB01–MB07.
- State file `03_state/vab_ftp_methodology.md`: Toàn bộ 4/4 chunk `[x]`, 0 mục chưa phủ.

### 2. Rà soát Chi tiết & Hoàn tất 100% Nguồn `bcbs_144` (641 dòng / 138 KB)
- Phân tích chi tiết 17 Nguyên tắc của Basel Committee (BCBS 144) theo yêu cầu làm rõ tách node mới vs merge:
  - **Tạo mới 2 concept độc lập (§5 Atomic)**:
    1. `foreign-currency-liquidity-management-and-fx-swap-risk-mitigation-framework`: Quản trị rủi ro thanh khoản ngoại tệ, bẫy tài trợ chéo và rủi ro đứt gãy thị trường FX Swap theo **Principle 5.c** (d.252–259).
    2. `intragroup-liquidity-governance-and-cross-entity-transfer-constraints-framework`: Quản trị thanh khoản tập đoàn, rào giậu pháp lý của cơ quan giám sát nước sở tại (*ring-fencing*), thanh khoản mắc kẹt (*trapped liquidity*) và hạn mức rủi ro nội bộ nhóm theo **Principle 6** (d.317–331).
  - **Merge & Cập nhật 3 trang hiện có**:
    1. `intraday-liquidity-risk-management-mandates-real-time-monitoring-and-priority-sequencing`: Merge **Principle 5.d** (d.260–267) về hoạt động ngân hàng đại lý, lưu ký, bù trừ và rủi ro *failure-to-settle*.
    2. `funding-diversification-and-market-access-testing-mitigate-wholesale-refinancing-freezes`: Tinh lọc cho **Principle 7** (d.332–371), bóc tách Principle 6 sang node riêng.
    3. `bcbs-sound-principles-establish-foundational-liquidity-risk-management-and-supervisory-mandates`: Merge cập nhật khung kiến trúc 4 trụ cột 17 nguyên tắc (d.91–136).
  - **Dọn sạch triệt để danh sách `Xem thêm:`** tại các trang liên quan theo `00_schema.md` §7.
  - State file `03_state/bcbs_144.md`: Toàn bộ 4/4 chunk `[x]`, 18 concept mới, ghi nhận 2 mục hành chính bỏ qua (bìa BIS d.3–24 và danh sách Working Group d.632–641).

---

## Trạng thái Kiểm định & Sức khỏe Wiki

- **Kiểm định Schema toàn bộ Wiki**: Quét toàn bộ **982 trang** trong `02_wiki/`:
  - 0 lỗi frontmatter.
  - 0 heading trong thân bài (100% tuân thủ cấu trúc phẳng).
  - 0 danh sách "Xem thêm:" phản quy tắc.
  - 0 liên kết chết (dead links).
  - 0 trang mồ côi mới.
- **Index `02_wiki/index.md`**: Cập nhật cả 2 nguồn `vab_ftp_methodology` và `bcbs_144` sang **Hoàn tất 100%** trong bảng `## Sources`; bổ sung đầy đủ các liên kết concept mới vào các danh mục chuyên đề FTP và Basel BCBS 144.
- **Nhật ký `log.md`**: Đã ghi nhận đầy đủ các lượt ingest và chuẩn hóa cấu trúc với format chuẩn 3 dòng.

---

## Việc Tiếp theo Cho Phiên Sau

- Tiếp tục ingest các nguồn dài đang dở trong `03_state/`:
  1. `bcbs_238` (LCR) và `bcbs_368` (IRRBB) — rà soát các chunk còn lại để đưa độ phủ lên 100%.
  2. `insights_59`, `bindseil_monetary_policy`, `cargill_central_bank_policy`, `tata_bank_alm`.
- Định kỳ chạy `/lint` để rà soát nâng trạng thái các trang draft đủ điều kiện lên stable.
