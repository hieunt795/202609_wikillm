---
title: hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, haircut, unwinding, repo, level-1, level-2, regulation]
sources: [sbv_draft_circular_replace_22]
status: draft
last_updated: 2026-09-26
---

Quy chuẩn kỹ thuật đo lường danh mục tài sản có tính thanh khoản cao đủ điều kiện (Eligible High-Quality Liquid Assets - HQLA) theo Phụ lục I của Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN thiết lập các công thức định lượng chi tiết nhằm chuẩn hóa tử số của tỷ lệ [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], bảo đảm bộ đệm thanh khoản của ngân hàng được phản ánh bằng các tài sản có phẩm cấp cao nhất sau khi đã điều chỉnh hệ số chiết khấu (haircut), cơ chế đảo ngược giao dịch có kỳ hạn (unwinding mechanics) và các chốt chặn trần cơ cấu danh mục theo đúng hiệp ước Basel III (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần A, d.879–1010).

**1. Phân tầng các cấp bậc Tài sản có tính thanh khoản cao (HQLA Levels)**

Danh mục HQLA được chia thành ba cấp bậc rủi ro với các tiêu chuẩn định tính và hệ số thanh khoản (haircut đối ứng) khác nhau (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần A.II–IV, d.907–979):

- **Tài sản Cấp 1 (Level 1 Assets) — Hệ số thanh khoản 100% (Haircut 0%)**:
  - Tiền mặt tại quỹ và tiền gửi (bao gồm cả tiền gửi dự trữ bắt buộc) tại Ngân hàng Nhà nước;
  - Công cụ nợ của Chính phủ Việt Nam, Trái phiếu Chính phủ Việt Nam, Tín phiếu Ngân hàng Nhà nước phát hành bằng đồng Việt Nam (nằm trong hạn mức [[sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk]]);
  - Công cụ nợ bằng ngoại tệ của Chính phủ Việt Nam hoặc NHTW: được tính vào Cấp 1 nhưng khống chế giá trị tối đa không vượt quá dòng tiền ra ròng của chính loại ngoại tệ đó trong điều kiện căng thẳng;
  - Chứng khoán do Chính phủ nước ngoài, NHTW nước ngoài, tổ chức công (PSEs), BIS, IMF, ECB, ESM, EFSF hoặc ngân hàng phát triển đa phương phát hành/bảo lãnh có hệ số rủi ro tín dụng 0% theo [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]], niêm yết trên sàn giao dịch và có lịch sử sụt giá tối đa không quá 5% trong các giai đoạn căng thẳng thanh khoản 30 ngày. Tài sản Cấp 1 được đưa vào danh mục mà không bị giới hạn trần tỷ trọng.

- **Tài sản Cấp 2A (Level 2A Assets) — Hệ số thanh khoản 85% (Haircut 15%)**:
  - Chứng khoán của chính phủ, NHTW, tổ chức công (PSEs) hoặc ngân hàng phát triển đa phương có hệ số rủi ro tối đa 20% theo phương pháp tiêu chuẩn, niêm yết và có biên độ sụt giá tối đa không quá 10% trong 30 ngày căng thẳng;
  - Chứng khoán nợ doanh nghiệp (bao gồm thương phiếu) và trái phiếu có bảo đảm (covered bonds) không do tổ chức tài chính phát hành, có mức xếp hạng tín nhiệm độc lập từ AA- trở lên (hoặc PD nội bộ tương đương) và biên độ sụt giá không quá 10%.

- **Tài sản Cấp 2B (Level 2B Assets) — Haircut 25% hoặc 50%**:
  - *Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS đủ điều kiện)*: áp dụng hệ số thanh khoản **75% (haircut 25%)** với điều kiện được xếp hạng tín nhiệm từ AA trở lên, tỷ lệ LTV bình quân $\le 80\%$, có điều khoản truy đòi đầy đủ (full recourse), bên phát hành tuân thủ quy định duy trì rủi ro (risk retention) và biên độ sụt giá không quá 20%;
  - *Chứng khoán nợ doanh nghiệp xếp hạng từ BBB- đến A+*: áp dụng hệ số thanh khoản **50% (haircut 50%)**, không do định chế tài chính phát hành, biên độ sụt giá không quá 20%;
  - *Cổ phiếu phổ thông đủ điều kiện*: áp dụng hệ số thanh khoản **50% (haircut 50%)**, là cổ phiếu thành phần của chỉ số thị trường trọng yếu (như VN30), thanh toán bù trừ tập trung, không do tổ chức tài chính phát hành và có biên độ sụt giá không quá 40% trong 30 ngày căng thẳng;
  - *Chứng khoán chính phủ, PSEs xếp hạng BBB- có hệ số rủi ro $\le 50\%$*: áp dụng hệ số thanh khoản **50% (haircut 50%)**.

**2. Cơ chế đảo ngược giao dịch tài trợ (Unwinding Mechanics)**

Trong hoạt động kinh doanh hàng ngày, ngân hàng thường xuyên thực hiện các giao dịch vay/cho vay có bảo đảm (Repo, Reverse Repo) và hoán đổi tài sản bảo đảm (Collateral Swaps) với các kỳ hạn ngắn. Nếu chỉ tính các tài sản đang nằm trong kho tại thời điểm báo cáo, bức tranh thanh khoản sẽ bị bóp méo (ví dụ: ngân hàng có thể tạm thời biến tài sản Cấp 2 thành tiền mặt qua hợp đồng Repo 1 tuần).

Dự thảo quy định nguyên tắc **đảo ngược giao dịch** bắt buộc (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần A.I, d.891–906):
- Ngân hàng phải giả định rằng toàn bộ các giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm có ngày đáo hạn trong vòng 30 ngày tiếp theo đều được hoàn tất việc đảo ngược (unwound);
- Nghĩa là: ngân hàng phải trả lại tiền mặt/tài sản bảo đảm đã nhận và nhận lại tài sản bảo đảm ban đầu của mình;
- Nếu tài sản bảo đảm nhận về từ Reverse Repo đã bị đem đi tái thế chấp (rehypothecated) trong một giao dịch khác đáo hạn trong 30 ngày, cả hai giao dịch này đều phải được đảo ngược đồng thời;
- Giá trị tài sản sau khi đảo ngược được ký hiệu là $KĐC.L1$, $KĐC.L2A$, và $KĐC.L2B$ (sau khi nhân với hệ số thanh khoản tương ứng).

**3. Công thức khống chế trần cơ cấu danh mục HQLA (Cap Formulas)**

Để bảo đảm bộ đệm thanh khoản không bị phụ thuộc quá mức vào các tài sản có rủi ro thị trường hoặc tính thanh khoản kém hơn Cấp 1, khung Basel III nội luật hóa hai trần cơ cấu nghiêm ngặt sau khi đã đảo ngược giao dịch (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần A.I & Mục V, d.883–890, 1005–1007):

1. **Trần khống chế Tài sản Cấp 2 tối đa 40% danh mục**: Tổng giá trị tài sản Cấp 2A và Cấp 2B sau unwinding không được vượt quá 40% tổng danh mục HQLA đủ điều kiện (tương đương không quá $2/3$ giá trị tài sản Cấp 1). Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$KĐC_{40\%} = \max\left( (KĐC.L2A + KĐC.L2B) - \frac{2}{3} \times KĐC.L1,\ 0 \right)$$

2. **Trần khống chế Tài sản Cấp 2B tối đa 15% danh mục**: Tài sản Cấp 2B (có haircut lớn 25%–50%) sau unwinding không được vượt quá 15% tổng danh mục HQLA đủ điều kiện. Phần giá trị vượt trần bị loại trừ được tính bằng:
   $$KĐC_{15\%} = \max\left( KĐC.L2B - \frac{15}{85} \times (KĐC.L1 + KĐC.L2A),\ KĐC.L2B - \frac{15}{60} \times KĐC.L1,\ 0 \right)$$

**Công thức tổng hợp giá trị HQLA đủ điều kiện**:
$$\text{HQLA đủ điều kiện} = (\text{Level 1} + \text{Level 2A} + \text{Level 2B}) - \max\left(KĐC_{15\%},\ KĐC_{40\%}\right)$$

Trong đó $\text{Level 1}$, $\text{Level 2A}$, $\text{Level 2B}$ là giá trị ghi sổ của các tài sản thực tế nắm giữ sau khi nhân với hệ số thanh khoản quy chuẩn. Nếu tỷ trọng Cấp 2 hoặc Cấp 2B vượt trần sau khi đảo ngược, phần vượt trần lớn hơn giữa hai ngưỡng khống chế sẽ bị khấu trừ trực tiếp khỏi tử số của LCR.

**4. Kỷ luật giám sát và thẩm quyền can thiệp của Ngân hàng Nhà nước**

Nhằm ngăn chặn hành vi làm đẹp sổ sách hoặc tối ưu hóa tài sản thanh khoản, NHNN có quyền yêu cầu ngân hàng áp dụng hệ số thanh khoản thấp hơn quy định chuẩn nếu kết quả thanh tra cho thấy tài sản bảo đảm có độ nhạy cảm cao với lãi suất, rủi ro tín dụng tiềm ẩn hoặc mức chiết khấu thực tế trên thị trường repo liên ngân hàng cao hơn dự kiến (Phụ lục I Phần A.II.2, d.910). Các tài sản HQLA bị ràng buộc pháp lý (encumbered) hoặc dùng để phục vụ các vị thế kinh doanh tự doanh mà không thuộc quyền kiểm soát của bộ phận thanh khoản ALM/Treasury đều bị loại trừ hoàn toàn theo yêu cầu vận hành của [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]].

Xem thêm: [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]].
