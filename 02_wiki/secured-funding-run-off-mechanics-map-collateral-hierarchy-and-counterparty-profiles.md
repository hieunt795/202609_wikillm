---
title: secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles
type: concept
tags: [banking, alm, liquidity-risk, lcr, secured-funding, repo, run-off-rates, collateral-hierarchy, haircuts, basel, basel-iii, bcbs-238]
sources: [bcbs_238]
status: draft
last_updated: 2026-09-26
---

Cơ chế xác định tỷ lệ rút vốn tài trợ có bảo đảm (Secured Funding Run-off Mechanics) theo chuẩn mực Basel III (BCBS 238) thiết lập ma trận định lượng dòng tiền ra phát sinh từ các giao dịch tài trợ chứng khoán ngắn hạn (Repo, hoán đổi tài sản bảo đảm và các vị thế bán khống) đáo hạn trong vòng 30 ngày, phản ánh sự suy giảm khả năng tái cấp vốn có bảo đảm thông qua việc ánh xạ trực tiếp thứ bậc phẩm cấp thanh khoản của tài sản thế chấp đối ứng với độ tin cậy của từng nhóm đối tác giao dịch (bcbs_238, file bcbs238.md, Part 1 Section II.B.1.iii, Paragraphs 112–115, d.483–506).

**1. Định nghĩa và nguyên tắc đo lường Dòng tiền tài trợ có bảo đảm**

Theo quy định tại Paragraph 112 của BCBS 238, tài trợ có bảo đảm (Secured funding) là các khoản nợ phải trả và nghĩa vụ chung được bảo đảm bằng quyền pháp lý đối với các tài sản chỉ định thuộc quyền sở hữu của ngân hàng đi vay trong trường hợp phá sản, giải thể, thanh lý hoặc xử lý tái cơ cấu (d.485). Trong khuôn khổ chuẩn mực LCR, các công cụ tài chính sau bắt buộc phải được xử lý như tài trợ có bảo đảm (Paragraph 113, d.494):
- Hợp đồng mua lại chứng khoán (Repurchase agreements - Repo);
- Hợp đồng hoán đổi tài sản bảo đảm (Collateral swaps) đáo hạn trong 30 ngày;
- Giao dịch cho khách hàng vay chứng khoán để phục vụ các vị thế bán khống (Customer short positions) không xác định ngày đáo hạn hợp đồng cụ thể.

*Nguyên tắc đo lường giá trị dòng tiền ra*: Khối lượng dòng tiền ra dự kiến được tính toán dựa trên **số tiền thực tế mà ngân hàng đã huy động được** thông qua giao dịch tài trợ (the amount of funds raised through the transaction), chứ tuyệt đối không tính dựa trên mệnh giá hay giá trị thị trường của danh mục tài sản bảo đảm nằm dưới (Paragraph 113, d.494).

**2. Tương quan hữu cơ giữa Hệ số chiết khấu (Haircut) và Tỷ lệ rút vốn (Run-off)**

Triết lý nền tảng của Basel III trong việc định cỡ tỷ lệ rút vốn tài trợ có bảo đảm dựa trên nguyên lý: trong một cuộc khủng hoảng thị trường nghiêm trọng, khả năng tái tục (roll-over) các hợp đồng tài trợ ngắn hạn phụ thuộc hoàn toàn vào niềm tin của bên cho vay đối với tính thanh khoản của tài sản bảo đảm (Paragraph 113–114, d.486, 496):
- Nếu tài sản bảo đảm là tài sản Cấp 1 tối thượng (Level 1 assets), thị trường repo vẫn duy trì khả năng thanh khoản tuyệt đối và đối tác sẵn sàng tái tục 100% hợp đồng, dẫn tới tỷ lệ mất vốn tài trợ bằng **0%**;
- Đối với các tài sản Cấp 2, sự suy giảm khả năng tài trợ sẵn có (reduction in funding availability) được ấn định **bằng đúng tỷ lệ chiết khấu (haircut) quy chuẩn** áp dụng cho chính loại tài sản đó trong danh mục HQLA: tài sản Cấp 2A có haircut 15% thì tỷ lệ rút vốn repo là **15%**; tài sản Cấp 2B RMBS có haircut 25% thì tỷ lệ rút vốn là **25%**; và các tài sản Cấp 2B khác có haircut 50% thì tỷ lệ rút vốn là **50%**;
- Đối với các tài sản phi HQLA (chứng khoán nợ rủi ro cao, cổ phiếu ngoài rổ chỉ số chính, khoản vay thế chấp), thị trường tài trợ liên ngân hàng tư nhân sẽ đóng băng hoàn toàn, dẫn tới tỷ lệ mất nguồn tài trợ lên tới **100%**.

**3. Ma trận tỷ lệ rút vốn tài trợ có bảo đảm chi tiết theo BCBS 238**

Theo bảng chuẩn hóa tại Paragraph 115 của BCBS 238 (d.497–505), các giao dịch tài trợ có bảo đảm đáo hạn trong vòng 30 ngày calendar chịu các tỷ lệ rút vốn sau:

1. **Tỷ lệ rút vốn 0% (Không sụt giảm khả năng tài trợ)**:
   - Giao dịch được bảo đảm bằng **Tài sản Cấp 1 (Level 1 assets)** bất kể đối tác giao dịch là ai;
   - Toàn bộ các giao dịch tài trợ có bảo đảm đáo hạn với **Ngân hàng Trung ương sở tại (Domestic Central Bank)**, bất kể tài sản thế chấp là loại nào. Giả định này phản ánh vai trò của NHTW như là người cho vay cứu cánh cuối cùng không cắt giảm tài trợ repo với hệ thống ngân hàng trong khủng hoảng;

2. **Tỷ lệ rút vốn 15%**:
   - Giao dịch được bảo đảm bằng **Tài sản Cấp 2A (Level 2A assets)** (chứng khoán công quyền rủi ro 20%, trái phiếu doanh nghiệp và covered bonds xếp hạng AA- trở lên);

3. **Tỷ lệ rút vốn 25%**:
   - Giao dịch tài trợ có bảo đảm với **Chính phủ chủ quyền nội địa, Ngân hàng phát triển đa phương (MDBs), hoặc Tổ chức khu vực công (PSEs nội địa có hệ số rủi ro $\le 20\%$)** được bảo đảm bằng tài sản khác ngoài Cấp 1 và Cấp 2A. Cơ chế ưu đãi 25% này ghi nhận thực tế rằng các thực thể công quyền nội địa sẽ không rút vốn đột ngột khỏi hệ thống ngân hàng trong thời kỳ căng thẳng thị trường (Paragraph 114, d.496). Cần lưu ý: tỷ lệ ưu đãi này chỉ áp dụng cho các giao dịch hiện hữu đang dư nợ, không áp dụng cho hạn mức vay chưa sử dụng;
   - Giao dịch được bảo đảm bằng **Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS) đủ điều kiện Cấp 2B**;

4. **Tỷ lệ rút vốn 50%**:
   - Giao dịch được bảo đảm bằng **các tài sản Cấp 2B khác** (trái phiếu doanh nghiệp xếp hạng BBB- đến A+, cổ phiếu phổ thông thuộc chỉ số thị trường chính);

5. **Tỷ lệ rút vốn 100% (Mất toàn bộ nguồn tài trợ)**:
   - Toàn bộ các giao dịch tài trợ có bảo đảm đáo hạn khác không thuộc các trường hợp trên, bao gồm:
     - Thế chấp bằng tài sản phi HQLA với các định chế tài chính tư nhân (ngân hàng, quỹ đầu tư, công ty chứng khoán);
     - Giao dịch trong đó ngân hàng sử dụng danh mục tài sản tự doanh của chính mình để đáp ứng các vị thế bán khống của khách hàng (customer short positions covered by bank's own inventory).

**Bảng tổng hợp tiêu chuẩn rút vốn tài trợ có bảo đảm**

| Danh mục giao dịch tài trợ có bảo đảm đáo hạn $\le 30$ ngày | Tài sản bảo đảm cơ sở | Đối tác giao dịch | Tỷ lệ rút vốn (Run-off) |
|---|---|---|---|
| Hợp đồng Repo / Collateral Swap | Tài sản Cấp 1 (Level 1) | Mọi đối tác | **0%** |
| Hợp đồng Repo / Tái cấp vốn | Bất kỳ loại tài sản nào | Ngân hàng Trung ương sở tại | **0%** |
| Hợp đồng Repo / Collateral Swap | Tài sản Cấp 2A (Level 2A) | Mọi đối tác | **15%** |
| Hợp đồng Repo đặc cách công quyền | Tài sản phi Cấp 1 / 2A | Sovereign, MDB, PSE nội địa ($\text{RW} \le 20\%$) | **25%** |
| Hợp đồng Repo / Collateral Swap | RMBS đủ chuẩn Cấp 2B | Mọi đối tác | **25%** |
| Hợp đồng Repo / Collateral Swap | Cổ phiếu / TP Doanh nghiệp Cấp 2B | Mọi đối tác | **50%** |
| Hợp đồng Repo phi HQLA / Short positions | Tài sản phi HQLA (non-HQLA) | Định chế tài chính, đối tác khác | **100%** |

Xem thêm: [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]].
