---
title: hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, haircut, unwinding, repo, level-1, level-2, regulation, basel, principles, basel-iii, bcbs-238]
sources: [sbv_draft_circular_replace_22, bcbs_144, bcbs_238]
status: stable
last_updated: 2026-09-26
---

Quy chuẩn kỹ thuật đo lường danh mục tài sản có tính thanh khoản cao đủ điều kiện (Eligible High-Quality Liquid Assets - HQLA) theo Phụ lục I của Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN nội luật hóa nguyên vẹn các công thức định lượng và nguyên lý quản trị từ chuẩn mực Basel III (BCBS 238) nhằm chuẩn hóa tử số của tỷ lệ [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], bảo đảm bộ đệm thanh khoản của ngân hàng được phản ánh bằng các tài sản có phẩm cấp cao nhất sau khi đã điều chỉnh hệ số chiết khấu (haircut), cơ chế đảo ngược giao dịch có kỳ hạn (unwinding mechanics) và các chốt chặn trần cơ cấu danh mục khắt khe (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần A, d.879–1010; bcbs_238, file bcbs238.md, Part 1 Section II.A.4, Paragraphs 46–54, d.222–302; Annex 1, d.848–876).

**1. Phân tầng các cấp bậc Tài sản có tính thanh khoản cao (HQLA Levels)**

Danh mục HQLA được chia thành ba cấp bậc rủi ro với các tiêu chuẩn định tính và hệ số thanh khoản (haircut đối ứng) bám sát tuyệt đối theo [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]] (bcbs_238, Paragraph 49–54, d.225–301; sbv_draft_circular_replace_22, Phụ lục I Phần A.II–IV, d.907–979):

- **Tài sản Cấp 1 (Level 1 Assets) — Hệ số thanh khoản 100% (Haircut 0%)**:
  - Tiền mặt tại quỹ và tiền gửi (bao gồm cả tiền gửi dự trữ bắt buộc) tại Ngân hàng Nhà nước hoặc NHTW sở tại (trong phạm vi được phép rút trong điều kiện căng thẳng);
  - Công cụ nợ của Chính phủ Việt Nam, Trái phiếu Chính phủ Việt Nam, Tín phiếu Ngân hàng Nhà nước phát hành bằng đồng Việt Nam (nằm trong hạn mức [[sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk]]);
  - Công cụ nợ bằng ngoại tệ của Chính phủ Việt Nam hoặc NHTW: được tính vào Cấp 1 nhưng khống chế giá trị tối đa không vượt quá dòng tiền ra ròng của chính loại ngoại tệ đó trong điều kiện căng thẳng theo Paragraph 50(e) của BCBS 238;
  - Chứng khoán do Chính phủ nước ngoài, NHTW nước ngoài, tổ chức công (PSEs), BIS, IMF, ECB, ESM, EFSF hoặc ngân hàng phát triển đa phương phát hành/bảo lãnh có hệ số rủi ro tín dụng 0% theo [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]], niêm yết trên sàn giao dịch và có lịch sử sụt giá tối đa không quá 5% (hoặc không quá 10% theo Basel III) trong các giai đoạn căng thẳng thanh khoản 30 ngày. Tài sản Cấp 1 được đưa vào danh mục mà không bị giới hạn trần tỷ trọng.

- **Tài sản Cấp 2A (Level 2A Assets) — Hệ số thanh khoản 85% (Haircut 15%)**:
  - Chứng khoán của chính phủ, NHTW, tổ chức công (PSEs) hoặc ngân hàng phát triển đa phương có hệ số rủi ro tối đa 20% theo phương pháp tiêu chuẩn, niêm yết và có biên độ sụt giá tối đa không quá 10% trong 30 ngày căng thẳng;
  - Chứng khoán nợ doanh nghiệp (bao gồm thương phiếu plain-vanilla) và trái phiếu có bảo đảm (covered bonds) không do tổ chức tài chính hoặc chính ngân hàng phát hành, có mức xếp hạng tín nhiệm độc lập từ AA- trở lên (hoặc PD nội bộ tương đương) và biên độ sụt giá không quá 10%.

- **Tài sản Cấp 2B (Level 2B Assets) — Haircut 25% hoặc 50%**:
  - *Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS đủ điều kiện)*: áp dụng hệ số thanh khoản **75% (haircut 25%)** với điều kiện được xếp hạng tín nhiệm từ AA trở lên, tỷ lệ LTV bình quân $\le 80\%$, có điều khoản truy đòi đầy đủ (full recourse), bên phát hành tuân thủ quy định duy trì rủi ro (risk retention) và biên độ sụt giá không quá 20%;
  - *Chứng khoán nợ doanh nghiệp xếp hạng từ BBB- đến A+*: áp dụng hệ số thanh khoản **50% (haircut 50%)**, không do định chế tài chính phát hành, biên độ sụt giá không quá 20%;
  - *Cổ phiếu phổ thông đủ điều kiện*: áp dụng hệ số thanh khoản **50% (haircut 50%)**, là cổ phiếu thành phần của chỉ số thị trường trọng yếu (như VN30), thanh toán bù trừ tập trung qua CCP, không do tổ chức tài chính phát hành và có biên độ sụt giá không quá 40% trong 30 ngày căng thẳng;
  - *Chứng khoán chính phủ, PSEs xếp hạng BBB- có hệ số rủi ro $\le 50\%$*: áp dụng hệ số thanh khoản **50% (haircut 50%)**.

**2. Cơ chế đảo ngược giao dịch tài trợ (Unwinding Mechanics)**

Trong hoạt động kinh doanh hàng ngày, ngân hàng thường xuyên thực hiện các giao dịch vay/cho vay có bảo đảm (Repo, Reverse Repo) và hoán đổi tài sản bảo đảm (Collateral Swaps) với các kỳ hạn ngắn. Nếu chỉ tính các tài sản đang nằm trong kho tại thời điểm báo cáo, bức tranh thanh khoản sẽ bị bóp méo (ví dụ: ngân hàng có thể tạm thời biến tài sản Cấp 2 thành tiền mặt qua hợp đồng Repo 1 tuần).

Dự thảo Thông tư NHNN và Annex 1 của BCBS 238 quy định nguyên tắc **đảo ngược giao dịch** bắt buộc (sbv_draft_circular_replace_22, Phụ lục I Phần A.I, d.891–906; bcbs_238, Annex 1, Paragraph 1–4, d.852–855):
- Ngân hàng phải giả định rằng toàn bộ các giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm có ngày đáo hạn trong vòng 30 ngày tiếp theo đều được hoàn tất việc đảo ngược (unwound);
- Nghĩa là: ngân hàng phải trả lại tiền mặt/tài sản bảo đảm đã nhận và nhận lại tài sản bảo đảm ban đầu của mình;
- Nếu tài sản bảo đảm nhận về từ Reverse Repo đã bị đem đi tái thế chấp (rehypothecated) trong một giao dịch khác đáo hạn trong 30 ngày, cả hai giao dịch này đều phải được đảo ngược đồng thời;
- Giá trị tài sản sau khi đảo ngược được ký hiệu là $KĐC.L1$ ($\text{Adjusted Level 1}$), $KĐC.L2A$ ($\text{Adjusted Level 2A}$), và $KĐC.L2B$ ($\text{Adjusted Level 2B}$) sau khi nhân với hệ số thanh khoản (sau khi trừ haircut quy định).

**3. Công thức khống chế trần cơ cấu danh mục HQLA (Cap Formulas)**

Để bảo đảm bộ đệm thanh khoản không bị phụ thuộc quá mức vào các tài sản có rủi ro thị trường hoặc tính thanh khoản kém hơn Cấp 1, khung Basel III và Dự thảo Thông tư thiết lập hai trần cơ cấu nghiêm ngặt sau khi đã đảo ngược giao dịch bám sát theo [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]] (sbv_draft_circular_replace_22, Phụ lục I Phần A.I & Mục V, d.883–890, 1005–1007; bcbs_238, Annex 1, Paragraph 5–6, d.865–876):

1. **Trần khống chế Tài sản Cấp 2 tối đa 40% danh mục**: Tổng giá trị tài sản Cấp 2A và Cấp 2B sau unwinding không được vượt quá 40% tổng danh mục HQLA đủ điều kiện (tương đương không quá $2/3$ giá trị tài sản Cấp 1). Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$KĐC_{40\%} = \text{Adjustment for 40\% cap} = \max\left( (KĐC.L2A + KĐC.L2B - KĐC_{15\%}) - \frac{2}{3} \times KĐC.L1,\ 0 \right)$$

2. **Trần khống chế Tài sản Cấp 2B tối đa 15% danh mục**: Tài sản Cấp 2B (có haircut lớn 25%–50%) sau unwinding không được vượt quá 15% tổng danh mục HQLA đủ điều kiện. Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$KĐC_{15\%} = \text{Adjustment for 15\% cap} = \max\left( KĐC.L2B - \frac{15}{85} \times (KĐC.L1 + KĐC.L2A),\ KĐC.L2B - \frac{15}{60} \times KĐC.L1,\ 0 \right)$$

**Công thức tổng hợp giá trị HQLA đủ điều kiện**:
$$\text{Stock of HQLA} = (\text{Level 1} + \text{Level 2A} + \text{Level 2B}) - KĐC_{15\%} - KĐC_{40\%}$$
Hoặc công thức gộp tương đương:
$$\text{Stock of HQLA} = (\text{Level 1} + \text{Level 2A} + \text{Level 2B}) - \max\left( (KĐC.L2A + KĐC.L2B) - \frac{2}{3} \times KĐC.L1,\ KĐC.L2B - \frac{15}{85} \times (KĐC.L1 + KĐC.L2A),\ 0 \right)$$

Trong đó $\text{Level 1}$, $\text{Level 2A}$, $\text{Level 2B}$ là giá trị ghi sổ của các tài sản thực tế nắm giữ sau khi nhân với hệ số thanh khoản quy chuẩn. Nếu tỷ trọng Cấp 2 hoặc Cấp 2B vượt trần sau khi đảo ngược, phần vượt trần lớn hơn giữa hai ngưỡng khống chế sẽ bị khấu trừ trực tiếp khỏi tử số của LCR.

**4. Kỷ luật giám sát và nền tảng chuẩn mực quốc tế BCBS 144 & BCBS 238**

Nhằm ngăn chặn hành vi làm đẹp sổ sách hoặc tối ưu hóa tài sản thanh khoản, cơ quan giám sát có quyền yêu cầu ngân hàng áp dụng hệ số thanh khoản thấp hơn quy định chuẩn nếu kết quả thanh tra cho thấy tài sản bảo đảm có độ nhạy cảm cao với lãi suất, rủi ro tín dụng tiềm ẩn hoặc mức chiết khấu thực tế trên thị trường repo liên ngân hàng cao hơn dự kiến. Toàn bộ tài sản HQLA phải tuân thủ nghiêm ngặt các yêu cầu vận hành theo [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]] và đáp ứng đầy đủ các tiêu chuẩn định tính theo [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]]. Đối với các thị trường thiếu hụt nguồn cung HQLA nội tệ mang tính cơ cấu, khuôn khổ [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]] cung cấp các giải pháp thay thế qua hạn mức cam kết từ NHTW có thu phí (CLF) hoặc sử dụng HQLA ngoại tệ có kiểm soát.

Cơ chế phân tầng HQLA và áp đặt trần cơ cấu khắt khe của Basel III bắt nguồn trực tiếp từ các nguyên tắc nền tảng tại [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]] (bcbs_144, file bcbs144.md, Principle 12, d.524–539). BCBS 144 chỉ rõ: quy mô đệm HQLA phải được định cỡ bằng kết quả thiếu hụt dòng tiền từ kiểm tra sức chịu đựng [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]], với tầng cốt lõi (tiền mặt, TPCP không rủi ro - tương ứng Level 1) phòng ngừa sốc thanh khoản cấp bách, và tầng mở rộng (Level 2A/2B) cho sốc kéo dài. Đồng thời, nguyên tắc quản trị TSBĐ theo [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]] (Principle 9, d.404–421) là nền tảng bắt buộc để loại trừ các tài sản encumbered và bóc tách các vị thế ràng buộc phòng ngừa (tied positions) khỏi danh mục HQLA khả dụng.

Xem thêm: [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]], [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]], [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]].

