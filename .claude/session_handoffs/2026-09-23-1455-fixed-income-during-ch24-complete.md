# Session Handoff: Hoàn Tất Chương 24 — Credit Risk (`fixed_income_during` / Part Four)

- **Thời gian**: 2026-09-23 14:55 (Local Time, UTC+7)
- **Mục tiêu phiên**: Ingest toàn bộ Chương 24: Credit Risk (Rủi ro tín dụng) của nguồn sách `fixed_income_during` (Alexander Düring, *Fixed Income Trading and Risk Management*), mở đầu cho **Part Four — Defaultable Claims (Ch.24–27)**, áp dụng bộ quy tắc văn phong `writing-style` (thân bài phẳng, không heading, câu < 60 từ, chủ ngữ kinh tế rõ ràng, trích dẫn chuẩn vị trí) và tuân thủ `00_schema.md`, `CLAUDE.md`, skill `ingest`.
- **Kết quả**: Hoàn tất 100% Chương 24. Wiki đạt mốc **584 trang**, **0 lỗi schema**, **0 trang mồ côi**.

---

## 1. Tóm Tắt Các Khối Đã Ingest Trong Phiên

### 7 trang concept/declarative mới:
1. `default-insolvency-and-bankruptcy-differentiate-covenant-breaches-cash-shortfalls-and-terminal-liquidation`: Phân biệt vỡ nợ kỹ thuật (vi phạm covenant đòn bẩy), mất khả năng thanh toán dòng tiền đến hạn và phá sản thanh lý; giải thích động lực tái cơ cấu nợ để bảo toàn giá trị doanh nghiệp hoạt động (going-concern value) và tránh chiết khấu bán tháo tài sản vô hình (fire-sale discount).
2. `debt-acceleration-and-cross-default-clauses-prevent-time-subordination-in-multi-creditor-structures`: Điều khoản gia tốc nợ và vỡ nợ chéo triệt tiêu tính ưu tiên hoàn trả theo thời gian (time subordination) trong cấu trúc nhiều chủ nợ, phân tích quy chế thu hồi nợ (clawbacks), trái phiếu trả lãi bằng nợ mới (PIK notes) và rating triggers.
3. `statutory-subordination-and-bail-in-frameworks-mandate-loss-absorption-for-systemic-bank-creditors`: Thứ bậc nợ luật định và cơ chế giải cứu nội bộ (bail-in) theo chỉ thị BRRD, chuẩn TLAC/MREL cùng trái phiếu CoCo cưỡng chế chia sẻ tổn thất cho chủ nợ ngân hàng; phân biệt với cơ chế ưu tiên tuyệt đối của cover pool trong trái phiếu có bảo đảm (covered bonds).
4. `sovereign-debt-operates-as-a-repeat-game-devoid-of-judicial-liquidation-and-enforceable-seniority`: Nợ chính phủ vận hành như trò chơi lặp lại (repeat game) giữa con nợ có tuổi thọ vô hạn và thị trường vốn, không có cơ chế cưỡng chế thanh lý tư pháp hay thứ bậc nợ thực thi độc lập (senior sovereign debt thuần túy là lời hứa chính trị); phân tích bảo lãnh liên đới (joint and several) vs riêng rẽ (several) và first-call vs sufficiency support.
5. `collective-action-clauses-resolve-creditor-coordination-failures-and-neutralize-hold-out-vultures`: Điều khoản hành động tập thể (CACs) ràng buộc biểu quyết đa số áp đảo, phá vỡ bế tắc cân bằng Nash của các quỹ kền kền bám trụ (hold-out vultures); phân biệt single-limb vs dual-limb CACs, model CACs theo ESM Treaty 2013 và tiền lệ Hy Lạp 2012 áp dụng CACs hồi tố bằng luật quốc nội (PSI).
6. `credit-ratings-represent-ordinal-ranking-scales-distorted-by-the-issuer-pays-conflict-and-curse-of-the-commons`: Xếp hạng tín nhiệm cấu thành thang đo thứ bậc (ordinal scale) phản ánh mức độ rủi ro tương đối chứ không phải thông số định lượng tuyệt đối (cardinal scale); phân tích độc quyền nhóm tự nhiên, bi kịch tài sản chung (curse of the commons), xung đột lợi ích của mô hình người phát hành trả tiền (issuer-pays) và trần xếp hạng quốc gia (sovereign ceiling).
7. `rating-migration-matrices-resolve-the-maturity-paradox-and-reveal-corporate-versus-sovereign-risk-divergence`: Ma trận dịch chuyển xếp hạng theo xích Markov giải quyết nghịch lý rủi ro kỳ hạn và bộc lộ sự phân kỳ cấu trúc giữa doanh nghiệp (hồi quy giá trị trung bình mean-reversion, trạng thái hấp thụ absorbing state, hội tụ rủi ro dài hạn) và quốc gia (không có trạng thái hấp thụ, duy trì phân kỳ rủi ro qua các chu kỳ kinh tế); phân tích áp lực bán tháo cưỡng bức khi rớt chuẩn đầu tư (fallen angels).

### 5 trang cập nhật 2 chiều:
1. `private-credit-selective-defaults-obscure-systemic-banking-fragility`: Bổ sung liên kết tới `default-insolvency-and-bankruptcy-...`, `debt-acceleration-and-cross-default-clauses-...`, và `credit-ratings-represent-ordinal-ranking-scales-...`.
2. `joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause`: Bổ sung liên kết tới `sovereign-debt-operates-as-a-repeat-game-...` và `statutory-subordination-and-bail-in-frameworks-...`.
3. `market-impact-of-collateral-framework-and-leverage-constraints`: Bổ sung liên kết tới `credit-ratings-represent-ordinal-ranking-scales-...` và `rating-migration-matrices-resolve-the-maturity-paradox-...`.
4. `par-par-and-proceeds-asset-swaps-differentiate-upfront-capital-commitments-and-terminal-credit-risks`: Bổ sung liên kết tới `default-insolvency-and-bankruptcy-...` và `debt-acceleration-and-cross-default-clauses-...`.
5. `ted-spreads-measure-interbank-credit-risk-by-shifting-the-entire-underlying-discount-curve`: Bổ sung liên kết tới `statutory-subordination-and-bail-in-frameworks-...` và `rating-migration-matrices-resolve-the-maturity-paradox-...`.

---

## 2. Trạng Thái Hệ Thống & Kiểm Tra Đã Chạy

- **Hook kiểm định**: `python .claude/hooks/validate_wiki_page.py --all` $\rightarrow$ **584 trang quét, 0 lỗi schema, 0 trang mồ côi**.
- **State file**: [`03_state/fixed_income_during.md`](file:///d:/AI/202609%20LLM%20wiki/03_state/fixed_income_during.md) cập nhật `[x]` Ch.24.
- **Index**: [`02_wiki/index.md`](file:///d:/AI/202609%20LLM%20wiki/02_wiki/index.md) cập nhật bảng Sources và phân mục *Rủi ro tín dụng, Thứ bậc nợ & Xếp hạng tín nhiệm (Fixed Income Düring — Ch.24 / Part Four)*.
- **Log**: [`log.md`](file:///d:/AI/202609%20LLM%20wiki/log.md) ghi nhận lượt ingest `[2026-09-23:14-52-10]`.

---

## 3. Bước Tiếp Theo Đề Xuất

1. **Commit & Push Git** (nếu người dùng yêu cầu): Lưu lại mốc hoàn tất Chương 24.
2. **Tiếp tục Part Four — Defaultable Claims (Chương 25–27)**:
   - **Chương 25 (Covered Bonds)** — File `-26.md` (173 dòng): Trái phiếu có bảo đảm, cấu trúc hoàn trả kép (dual recourse), cover pool và khung pháp lý Pfandbriefe.
   - **Chương 26 (Asset-Backed Securities - ABS)** — File `-27.md` (56 dòng): Chứng khoán hóa tài sản, phân tầng rủi ro tín dụng (tranching), cơ chế tăng cường tín dụng (credit enhancement).
   - **Chương 27 (Residential Mortgage-Backed Securities - RMBS)** — File `-28.md` (124 dòng): Chứng khoán thế chấp nhà ở, rủi ro thanh toán trước hạn (prepayment risk), mô hình kỳ hạn trả nợ.
