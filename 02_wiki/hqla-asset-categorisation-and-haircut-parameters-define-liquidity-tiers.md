---
title: hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, haircut, level-1, level-2a, level-2b, covered-bonds, rmbs, equities, basel, basel-iii, bcbs-238]
sources: [bcbs_238]
status: draft
last_updated: 2026-09-26
---

Hệ thống phân tầng tài sản có tính thanh khoản cao và các tham số tỷ lệ chiết khấu (HQLA Asset Categorisation and Haircut Parameters) theo chuẩn mực Basel III (BCBS 238) thiết lập thang đo lượng hóa chi tiết nhằm phân định ba cấp bậc chất lượng thanh khoản — Cấp 1 (Level 1, haircut 0%), Cấp 2A (Level 2A, haircut 15%) và Cấp 2B (Level 2B, haircut 25%–50%) — dựa trên chất lượng tín dụng của tổ chức phát hành, tính đơn giản của cấu trúc nợ, chiều sâu thanh khoản thứ cấp và biên độ suy giảm giá trị thị trường lịch sử trong các giai đoạn khủng hoảng (bcbs_238, file bcbs238.md, Part 1 Section II.A.4, Paragraphs 45–54, d.219–302).

**1. Cấu trúc ba tầng thanh khoản và vai trò của tỷ lệ chiết khấu (Haircut)**

Tỷ lệ chiết khấu (haircut) áp dụng cho từng loại tài sản HQLA phản ánh mức độ giảm giá kỳ vọng (haircut bảo toàn vốn) nếu ngân hàng buộc phải thanh lý tài sản hoặc đem thế chấp trong một giao dịch repo khẩn cấp trong chân trời 30 ngày chịu stress (bcbs_238, file bcbs238.md, Paragraph 48–54, d.224–301). Giá trị được tính vào bộ đệm thanh khoản là giá trị thị trường hiện hành nhân với hệ số thanh khoản đối ứng:
$$\text{Giá trị HQLA sau haircut} = \text{Giá trị thị trường} \times (1 - \text{Tỷ lệ Haircut})$$
Tài sản Cấp 1 đại diện cho các công cụ có tính thanh khoản tối thượng, không bị áp đặt tỷ lệ chiết khấu và được phép đưa vào danh mục mà không chịu giới hạn trần tỷ trọng. Ngược lại, các tài sản Cấp 2 mang tính biến động cao hơn, phải áp dụng haircut và bị khống chế trần tỷ trọng nghiêm ngặt theo [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]].

**2. Tài sản Cấp 1 (Level 1 Assets) — Hệ số thanh khoản 100% (Haircut 0%)**

Tài sản Cấp 1 có thể chiếm tỷ trọng không giới hạn trong kho HQLA (Paragraph 49, d.226). Các tài sản này chỉ bao gồm (Paragraph 50, d.227–248):
- **Tiền giấy và tiền xu (Coins and banknotes)**: Tiền mặt tại quỹ có thanh khoản tức thì tuyệt đối;
- **Dự trữ tại Ngân hàng Trung ương (Central bank reserves)**: Bao gồm tiền gửi qua đêm và tiền gửi dự trữ bắt buộc, trong phạm vi các quy chế và chính sách của NHTW sở tại cho phép ngân hàng được rút ra sử dụng trong thời kỳ căng thẳng thanh khoản (Footnote 12–13, d.239–241). Các khoản tiền gửi có kỳ hạn tại NHTW chỉ được tính nếu hợp đồng cho phép rút theo yêu cầu hoặc được phép thế chấp để vay tự động;
- **Chứng khoán công cụ nợ có hệ số rủi ro tín dụng 0% theo Basel II Standardised Approach**:
  - Do các chính phủ chủ quyền, ngân hàng trung ương, tổ chức khu vực công (PSEs), Ngân hàng Thanh toán Quốc tế (BIS), Quỹ Tiền tệ Quốc tế (IMF), Ngân hàng Trung ương Châu Âu (ECB), Cộng đồng Châu Âu (EC) hoặc các ngân hàng phát triển đa phương (MDBs) phát hành hoặc bảo lãnh thanh toán đầy đủ;
  - Được giao dịch trên thị trường mua bán đứt hoặc repo có quy mô lớn, chiều sâu giao dịch cao và mức độ tập trung thấp;
  - Có lịch sử chứng minh là nguồn thanh khoản tin cậy trong khủng hoảng;
  - **Quy tắc loại trừ nghĩa vụ của định chế tài chính (Footnote 16, d.247)**: Công cụ không được là nghĩa vụ nợ của một tổ chức tài chính hoặc bất kỳ công ty liên kết nào của tổ chức tài chính đó. Theo đó, các chứng khoán do ngân hàng thương mại phát hành dù được chính phủ bảo lãnh thanh toán (government-guaranteed bank debt trong khủng hoảng 2008) vẫn **bị loại trừ hoàn toàn khỏi HQLA** vì về bản chất nghĩa vụ nợ nguyên thủy vẫn gắn liền với rủi ro của định chế tài chính;
- **Trái phiếu chính phủ/NHTW bằng đồng nội tệ tại quốc gia có rủi ro phi 0%**: Đối với các quốc gia mà công cụ nợ chính phủ có hệ số rủi ro lớn hơn 0% theo Basel II, trái phiếu chính phủ hoặc chứng khoán NHTW phát hành bằng đồng nội tệ tại quốc gia phát sinh rủi ro thanh khoản hoặc tại quốc gia nguyên quán của ngân hàng vẫn được đặc cách xếp vào Cấp 1 (Paragraph 50.d, d.235);
- **Trái phiếu chính phủ/NHTW bằng ngoại tệ tại quốc gia có rủi ro phi 0%**: Được đặc cách tính vào Cấp 1 nhưng **bị khống chế trần giá trị tối đa** không vượt quá quy mô tổng dòng tiền ra ròng chịu căng thẳng của chính loại ngoại tệ đó phát sinh từ hoạt động của ngân hàng tại quốc gia sở tại (Paragraph 50.e, d.248).

**3. Tài sản Cấp 2A (Level 2A Assets) — Hệ số thanh khoản 85% (Haircut 15%)**

Tài sản Cấp 2A bị áp dụng tỷ lệ chiết khấu cố định 15% trên giá trị thị trường và phải đáp ứng một trong hai nhóm điều kiện (bcbs_238, file bcbs238.md, Paragraph 51–52, d.250–271):
- **Chứng khoán công quyền có hệ số rủi ro tín dụng 20%**: Chứng khoán khả nhượng do chính phủ, NHTW, tổ chức công (PSEs) hoặc ngân hàng phát triển đa phương phát hành/bảo lãnh có hệ số rủi ro tín dụng 20% theo Basel II Standardised Approach, giao dịch trên thị trường sâu rộng và có biên độ sụt giảm giá tối đa không quá 10% (hoặc mức tăng haircut không quá 10 điểm phần trăm) trong khoảng thời gian 30 ngày chịu stress thanh khoản lịch sử;
- **Chứng khoán nợ doanh nghiệp chất lượng cao và Trái phiếu có bảo đảm (Covered Bonds)**:
  - *Đối với chứng khoán nợ doanh nghiệp (bao gồm thương phiếu)*: Phải là các công cụ nợ đơn giản (plain-vanilla), không do định chế tài chính hoặc công ty liên kết phát hành;
  - *Đối với trái phiếu có bảo đảm (Covered bonds)*: Là trái phiếu được bảo đảm bằng danh mục tài sản thế chấp theo luật định bảo vệ nhà đầu tư ưu tiên (Footnote 20, d.267), không do chính ngân hàng hoặc công ty liên kết của ngân hàng phát hành;
  - *Xếp hạng tín nhiệm*: Được xếp hạng tín nhiệm dài hạn từ **AA- trở lên** bởi tổ chức ECAI được công nhận (hoặc xếp hạng ngắn hạn tương đương, hoặc đánh giá nội bộ có xác suất vỡ nợ PD tương ứng mức AA-);
  - *Tính thanh khoản*: Được giao dịch trên thị trường sôi động, và có lịch sử sụt giảm giá tối đa không quá 10% trong giai đoạn 30 ngày stress.

**4. Tài sản Cấp 2B (Level 2B Assets) — Haircut 25% hoặc 50%**

Tài sản Cấp 2B là nhóm tài sản bổ sung được Ủy ban Basel đưa vào theo quyết định thận trọng của cơ quan giám sát từng quốc gia (Paragraph 53, d.273). Khi được chấp thuận, tài sản Cấp 2B phải chịu mức haircut lớn và kiểm soát chặt chẽ (Paragraph 54, d.275–301):
- **Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS đủ điều kiện) — Haircut 25%**:
  - Không do chính ngân hàng hoặc các công ty liên kết phát hành, và danh mục tài sản thế chấp cơ sở không do ngân hàng khởi tạo (no self-originated RMBS);
  - Xếp hạng tín nhiệm dài hạn từ **AA trở lên** (hoặc ngắn hạn tương đương);
  - Danh mục tài sản cơ sở bị giới hạn nghiêm ngặt chỉ bao gồm các khoản cho vay thế chấp nhà ở dân cư, tuyệt đối **không chứa các sản phẩm cấu trúc phức tạp** (structured products);
  - Các khoản vay thế chấp cơ sở phải là khoản vay có quyền truy đòi đầy đủ (full recourse loans, tức người vay chịu trách nhiệm vô hạn với phần thâm hụt sau xử lý tài sản);
  - Tỷ lệ dư nợ trên giá trị tài sản bảo đảm (Loan-to-Value - LTV) bình quân tại thời điểm phát hành không vượt quá **80%**;
  - Tuân thủ quy định duy trì tỷ lệ rủi ro của tổ chức phát hành (risk retention regulations);
  - Biên độ sụt giảm giá tối đa không quá 20% (hoặc mức tăng haircut không quá 20 điểm phần trăm) trong 30 ngày stress lịch sử;
- **Chứng khoán nợ doanh nghiệp trung bình (Corporate Debt BBB- đến A+) — Haircut 50%**:
  - Không do định chế tài chính phát hành;
  - Xếp hạng tín nhiệm độc lập dài hạn trong khoảng từ **BBB- đến A+** (hoặc PD nội bộ tương đương);
  - Thuộc loại nợ đơn giản (plain-vanilla), niêm yết trên thị trường sâu rộng và mức sụt giá lịch sử không vượt quá 20% trong 30 ngày stress;
- **Cổ phiếu phổ thông đủ điều kiện (Common Equity Shares) — Haircut 50%**:
  - Không phải là cổ phiếu do định chế tài chính hoặc công ty liên kết phát hành;
  - Được giao dịch trên sàn giao dịch tập trung và được thanh toán bù trừ thông qua đối tác bù trừ trung tâm (CCP);
  - Là cổ phiếu thành phần của **chỉ số thị trường chứng khoán chính (major stock index)** tại quốc gia nguyên quán hoặc quốc gia phát sinh rủi ro thanh khoản do cơ quan giám sát sở tại chỉ định;
  - Được định danh bằng đồng nội tệ của quốc gia sở tại;
  - Có thị trường mua bán đứt và repo sôi động, và có lịch sử sụt giá tối đa không quá **40%** (hoặc tăng haircut không quá 40 điểm phần trăm) trong 30 ngày stress.

**5. Bảng tổng hợp tham số phân tầng HQLA theo BCBS 238**

| Phân tầng HQLA | Loại tài sản đủ chuẩn | Tiêu chí tín nhiệm / Cấu trúc | Mức sụt giá tối đa (30-day stress) | Tỷ lệ Haircut | Giới hạn trần cơ cấu |
|---|---|---|---|---|---|
| **Level 1** | Tiền mặt, Dự trữ NHTW khả dụng, Công cụ nợ rủi ro 0% (Sovereign/CB/PSE/MDB), Trái phiếu chính phủ nội tệ phi 0% | RW = 0% theo Basel II; không liên quan nợ định chế tài chính | Không áp dụng | **0%** | **Không giới hạn** |
| **Level 2A** | Công cụ nợ rủi ro 20% (Sovereign/CB/PSE/MDB), Corporate debt & Covered bonds | Xếp hạng $\ge$ AA-; plain-vanilla; không do bank/công ty liên kết phát hành | $\le 10\%$ | **15%** | Nằm trong trần Level 2 tối đa 40% |
| **Level 2B (RMBS)** | Chứng khoán bảo đảm bằng thế chấp nhà ở | Xếp hạng $\ge$ AA; LTV $\le 80\%$; full recourse; risk retention; không structured | $\le 20\%$ | **25%** | Trần riêng Level 2B $\le 15\%$; trần Level 2 $\le 40\%$ |
| **Level 2B (Corporate)** | Chứng khoán nợ doanh nghiệp plain-vanilla | Xếp hạng từ BBB- đến A+; không do định chế tài chính phát hành | $\le 20\%$ | **50%** | Trần riêng Level 2B $\le 15\%$; trần Level 2 $\le 40\%$ |
| **Level 2B (Equity)** | Cổ phiếu phổ thông | Thuộc Major Stock Index; thanh toán qua CCP; bằng đồng nội tệ; phi tài chính | $\le 40\%$ | **50%** | Trần riêng Level 2B $\le 15\%$; trần Level 2 $\le 40\%$ |

Xem thêm: [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]], [[sovereign-bond-holding-ceilings-and-interbank-equity-limits-contain-concentration-risk]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]].
