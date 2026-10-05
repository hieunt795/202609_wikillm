---
title: hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, haircut, unwinding, repo, level-1, level-2, regulation, basel, principles, basel-iii, bcbs-238]
sources: [bcbs_144, bcbs_238]
status: stable
last_updated: 2026-10-05
---

Quy chuẩn kỹ thuật đo lường danh mục tài sản có tính thanh khoản cao đủ điều kiện (Eligible High-Quality Liquid Assets - HQLA) của chuẩn mực Basel III (BCBS 238) chuẩn hóa tử số của tỷ lệ [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], bảo đảm bộ đệm thanh khoản của ngân hàng được phản ánh bằng các tài sản có phẩm cấp cao nhất sau khi đã điều chỉnh hệ số chiết khấu (haircut), cơ chế đảo ngược giao dịch có kỳ hạn (unwinding mechanics) và các chốt chặn trần cơ cấu danh mục khắt khe (bcbs_238, file bcbs238.md, Part 1 Section II.A.4, Paragraphs 46–54, d.222–302; Annex 1, d.848–876).

**1. Phân tầng các cấp bậc Tài sản có tính thanh khoản cao (HQLA Levels)**

Danh mục HQLA được chia thành ba cấp bậc rủi ro — Cấp 1 (haircut 0%), Cấp 2A (haircut 15%) và Cấp 2B (haircut 25% hoặc 50%) — với tiêu chuẩn định tính và hệ số thanh khoản của từng cấp trình bày tại [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]] (bcbs_238, Paragraph 49–54, d.225–301).

**2. Cơ chế đảo ngược giao dịch tài trợ (Unwinding Mechanics)**

Trong hoạt động kinh doanh hàng ngày, ngân hàng thường xuyên thực hiện các giao dịch vay/cho vay có bảo đảm (Repo, Reverse Repo) và hoán đổi tài sản bảo đảm (Collateral Swaps) với các kỳ hạn ngắn. Nếu chỉ tính các tài sản đang nằm trong kho tại thời điểm báo cáo, bức tranh thanh khoản sẽ bị bóp méo (ví dụ: ngân hàng có thể tạm thời biến tài sản Cấp 2 thành tiền mặt qua hợp đồng Repo 1 tuần).

Annex 1 của BCBS 238 quy định nguyên tắc **đảo ngược giao dịch** bắt buộc (bcbs_238, Annex 1, Paragraph 1–4, d.852–855):
- Ngân hàng phải giả định rằng toàn bộ các giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm có ngày đáo hạn trong vòng 30 ngày tiếp theo đều được hoàn tất việc đảo ngược (unwound);
- Nghĩa là: ngân hàng phải trả lại tiền mặt/tài sản bảo đảm đã nhận và nhận lại tài sản bảo đảm ban đầu của mình;
- Nếu tài sản bảo đảm nhận về từ Reverse Repo đã bị đem đi tái thế chấp (rehypothecated) trong một giao dịch khác đáo hạn trong 30 ngày, cả hai giao dịch này đều phải được đảo ngược đồng thời;
- Giá trị tài sản sau khi đảo ngược được ký hiệu là $Adj.L1$ ($\text{Adjusted Level 1}$), $Adj.L2A$ ($\text{Adjusted Level 2A}$), và $Adj.L2B$ ($\text{Adjusted Level 2B}$) sau khi nhân với hệ số thanh khoản (sau khi trừ haircut quy định).

**3. Công thức khống chế trần cơ cấu danh mục HQLA (Cap Formulas)**

Để bảo đảm bộ đệm thanh khoản không bị phụ thuộc quá mức vào các tài sản có rủi ro thị trường hoặc tính thanh khoản kém hơn Cấp 1, khung Basel III thiết lập hai trần cơ cấu nghiêm ngặt sau khi đã đảo ngược giao dịch bám sát theo [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]] (bcbs_238, Annex 1, Paragraph 5–6, d.865–876):

1. **Trần khống chế Tài sản Cấp 2 tối đa 40% danh mục**: Tổng giá trị tài sản Cấp 2A và Cấp 2B sau unwinding không được vượt quá 40% tổng danh mục HQLA đủ điều kiện (tương đương không quá $2/3$ giá trị tài sản Cấp 1). Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$Adj_{40\%} = \text{Adjustment for 40\% cap} = \max\left( (Adj.L2A + Adj.L2B - Adj_{15\%}) - \frac{2}{3} \times Adj.L1,\ 0 \right)$$

2. **Trần khống chế Tài sản Cấp 2B tối đa 15% danh mục**: Tài sản Cấp 2B (có haircut lớn 25%–50%) sau unwinding không được vượt quá 15% tổng danh mục HQLA đủ điều kiện. Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$Adj_{15\%} = \text{Adjustment for 15\% cap} = \max\left( Adj.L2B - \frac{15}{85} \times (Adj.L1 + Adj.L2A),\ Adj.L2B - \frac{15}{60} \times Adj.L1,\ 0 \right)$$

**Công thức tổng hợp giá trị HQLA đủ điều kiện**:
$$\text{Stock of HQLA} = (\text{Level 1} + \text{Level 2A} + \text{Level 2B}) - Adj_{15\%} - Adj_{40\%}$$
Hoặc công thức gộp tương đương:
$$\text{Stock of HQLA} = (\text{Level 1} + \text{Level 2A} + \text{Level 2B}) - \max\left( (Adj.L2A + Adj.L2B) - \frac{2}{3} \times Adj.L1,\ Adj.L2B - \frac{15}{85} \times (Adj.L1 + Adj.L2A),\ 0 \right)$$

Trong đó $\text{Level 1}$, $\text{Level 2A}$, $\text{Level 2B}$ là giá trị ghi sổ của các tài sản thực tế nắm giữ sau khi nhân với hệ số thanh khoản quy chuẩn. Nếu tỷ trọng Cấp 2 hoặc Cấp 2B vượt trần sau khi đảo ngược, phần vượt trần lớn hơn giữa hai ngưỡng khống chế sẽ bị khấu trừ trực tiếp khỏi tử số của LCR.

**4. Kỷ luật giám sát và nền tảng chuẩn mực quốc tế BCBS 144 & BCBS 238**

Nhằm ngăn chặn hành vi làm đẹp sổ sách hoặc tối ưu hóa tài sản thanh khoản, cơ quan giám sát có quyền yêu cầu ngân hàng áp dụng hệ số thanh khoản thấp hơn quy định chuẩn nếu kết quả thanh tra cho thấy tài sản bảo đảm có độ nhạy cảm cao với lãi suất, rủi ro tín dụng tiềm ẩn hoặc mức chiết khấu thực tế trên thị trường repo liên ngân hàng cao hơn dự kiến. Toàn bộ tài sản HQLA phải tuân thủ nghiêm ngặt các yêu cầu vận hành theo [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]] và đáp ứng đầy đủ các tiêu chuẩn định tính theo [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]]. Đối với các thị trường thiếu hụt nguồn cung HQLA nội tệ mang tính cơ cấu, khuôn khổ [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]] cung cấp các giải pháp thay thế qua hạn mức cam kết từ NHTW có thu phí (CLF) hoặc sử dụng HQLA ngoại tệ có kiểm soát.

Cơ chế phân tầng HQLA và áp đặt trần cơ cấu khắt khe của Basel III bắt nguồn trực tiếp từ các nguyên tắc nền tảng tại [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]] (bcbs_144, file bcbs144.md, Principle 12, d.524–539). BCBS 144 chỉ rõ: quy mô đệm HQLA phải được định cỡ bằng kết quả thiếu hụt dòng tiền từ kiểm tra sức chịu đựng [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]], với tầng cốt lõi (tiền mặt, TPCP không rủi ro - tương ứng Level 1) phòng ngừa sốc thanh khoản cấp bách, và tầng mở rộng (Level 2A/2B) cho sốc kéo dài. Đồng thời, nguyên tắc quản trị TSBĐ theo [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]] (Principle 9, d.404–421) là nền tảng bắt buộc để loại trừ các tài sản encumbered và bóc tách các vị thế ràng buộc phòng ngừa (tied positions) khỏi danh mục HQLA khả dụng.

Xem thêm: [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]], [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]], [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]].
