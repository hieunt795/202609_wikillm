---
title: secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk
type: concept
tags: [basel, basel-iii, lcr, liquidity, liquidity-risk, cash-inflows, reverse-repo, secured-lending, rehypothecation, short-positions, committed-facilities, operational-deposits, bcbs-238, regulation]
sources: [bcbs_238]
status: draft
last_updated: 2026-09-26
---

Ma trận dòng tiền vào từ cho vay có bảo đảm và phân tầng đối tác theo chuẩn Basel III (BCBS 238, Paragraph 145–160) thiết lập các hệ số thu hồi dòng tiền dự kiến dựa trên phẩm cấp tài sản bảo đảm, tình trạng tái cầm cố (rehypothecation), mục tiêu duy trì tín dụng đối với nền kinh tế thực và kỷ luật cô lập rủi ro lây lan liên ngân hàng (bcbs_238, file bcbs238.md, Paragraph 145–160, d.586–634). Bằng cách đối xử bất đối xứng giữa dòng tiền từ các định chế tài chính (được phép thu hồi 100%) với dòng tiền từ khách hàng bán lẻ và doanh nghiệp phi tài chính (chỉ được ghi nhận 50% do giả định ngân hàng phải tiếp tục cho vay đảo nợ), khung pháp lý bảo vệ dòng vốn tín dụng chảy vào nền kinh tế đồng thời phản ánh chính xác rủi ro đóng băng thanh khoản của các giao dịch tái tài trợ trên thị trường phái sinh và Repo.

**1. Ma trận dòng tiền vào từ giao dịch cho vay có bảo đảm và Reverse Repo (Paragraph 145 & Bảng Paragraph 148)**

Đối với các giao dịch cho vay có bảo đảm (Secured Lending), bao gồm các giao dịch mua lại đảo ngược (Reverse Repo) và đi vay chứng khoán (Securities Borrowing) đáo hạn trong vòng 30 ngày, hệ số dòng tiền vào (Inflow Rate) phản ánh mức độ tiền mặt thu hồi ròng tương ứng với chiết khấu (haircut) của tài sản bảo đảm nhận về (bcbs_238, file bcbs238.md, Paragraph 145, d.588):

- **Reverse Repo bảo đảm bằng Tài sản Cấp 1 (Level 1 Assets) — Hệ số dòng tiền vào 0%**: Ngân hàng giả định sẽ tiếp tục gia hạn (rollover) 100% các hợp đồng này để giữ lại tài sản Cấp 1 có tính thanh khoản cao nhất, do đó không làm phát sinh dòng tiền vào bằng tiền mặt;
- **Reverse Repo bảo đảm bằng Tài sản Cấp 2A (Level 2A Assets) — Hệ số dòng tiền vào 15%**: Khi hợp đồng đáo hạn và được tái đàm phán hoặc giải tỏa, ngân hàng ghi nhận dòng tiền vào tương đương mức chiết khấu 15% của tài sản Cấp 2A theo [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]];
- **Reverse Repo bảo đảm bằng Chứng khoán thế chấp nhà ở đủ điều kiện (Eligible RMBS Cấp 2B) — Hệ số dòng tiền vào 25%**: Thu hồi dòng tiền vào bằng đúng mức chiết khấu 25% của RMBS Cấp 2B;
- **Reverse Repo bảo đảm bằng Tài sản Cấp 2B khác — Hệ số dòng tiền vào 50%**: Ghi nhận dòng tiền vào tương ứng mức chiết khấu 50% (trái phiếu doanh nghiệp hạng BBB- hoặc cổ phiếu phổ thông đủ chuẩn);
- **Cho vay ký quỹ đòn bẩy giao dịch (Margin Lending) bảo đảm bằng tài sản phi HQLA — Hệ số dòng tiền vào tối đa 50%**: Nhằm phản ánh sự đồng bộ với ma trận rút vốn tài trợ có bảo đảm tại [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], các khoản cho vay margin đối với khách hàng giao dịch chứng khoán chỉ được ghi nhận tối đa 50% dòng tiền vào theo hợp đồng;
- **Reverse Repo bảo đảm bằng tài sản phi HQLA khác — Hệ số dòng tiền vào 100%**: Trong điều kiện căng thẳng, ngân hàng được giả định sẽ không gia hạn hợp đồng đối với các tài sản kém thanh khoản và sẽ thu hồi lại 100% tiền mặt.

**2. Ngoại lệ tái sử dụng tài sản bảo đảm (Rehypothecation) và vị thế bán khống (Paragraph 146–147)**

Quy tắc dòng tiền vào tại Paragraph 145 sẽ bị vô hiệu hóa hoàn toàn nếu tài sản bảo đảm nhận được đã bị đem đi tái cầm cố hoặc bán khống (bcbs_238, file bcbs238.md, Paragraph 146–147, d.589–590):

- **Tài sản bảo đảm dùng để che chắn vị thế bán khống kéo dài quá 30 ngày — Hệ số dòng tiền vào 0%**: Nếu tài sản bảo đảm nhận được từ reverse repo, vay chứng khoán hoặc hoán đổi TSBĐ đáo hạn trong 30 ngày đã được tái sử dụng (re-used/rehypothecated) để che chắn cho các vị thế bán khống (short positions) kéo dài quá 30 ngày, ngân hàng **bắt buộc phải áp hệ số dòng tiền vào 0%** cho mọi loại tài sản (kể cả Level 2 hoặc phi HQLA). Lý do kinh tế: Ngân hàng buộc phải tiếp tục gia hạn hợp đồng tài trợ có bảo đảm hoặc chi tiền mặt mua lại chứng khoán trên thị trường để duy trì vị thế bù đắp bán khống;
- **Khái niệm vị thế bán khống (Short Positions)**: Bao gồm cả trường hợp ngân hàng bán khống chứng khoán trực tiếp trong sổ tự doanh/hedging và trường hợp bán khống trong sổ repo đối ứng (matched repo book — tức là ngân hàng đi vay một chứng khoán kỳ hạn ngắn và cho vay lại chứng khoán đó với kỳ hạn dài hơn);
- **Xử lý vị thế bán khống của chính ngân hàng**: Nếu vị thế bán khống được che chắn bằng hợp đồng vay chứng khoán không bảo đảm (unsecured borrowing), hợp đồng này bị giả định sẽ rút vốn toàn bộ, tạo ra dòng tiền ra 100% theo [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]]. Ngược lại, nếu được che chắn bằng giao dịch SFT có bảo đảm, giả định vị thế duy trì ổn định và chịu dòng tiền ra 0%;
- **Kỷ luật quản trị tài sản bảo đảm (Paragraph 148)**: Ngân hàng phải quản trị tài sản bảo đảm sao cho luôn sẵn sàng hoàn trả TSBĐ bất cứ khi nào đối tác quyết định không gia hạn giao dịch reverse repo, đặc biệt đối với tài sản phi HQLA, tuân thủ chặt chẽ [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]].

**3. Phân tầng dòng tiền vào theo nhóm đối tác và nghĩa vụ tiếp tục cấp tín dụng (Paragraph 150–157)**

Đối với các khoản cho vay và giao dịch khác (ngoài reverse repo), dòng tiền vào được xác định theo đặc tính hành vi của từng nhóm đối tác (bcbs_238, file bcbs238.md, Paragraph 150–155, d.609–625):

- **Khách hàng cá nhân và Doanh nghiệp nhỏ (Retail & Small Business Inflows) — Dòng tiền vào ròng 50%**: Giả định ngân hàng nhận được 100% dòng tiền gốc và lãi đến hạn theo hợp đồng từ các khoản nợ đang thực hiện tốt, nhưng ngân hàng bắt buộc phải tiếp tục giải ngân cấp tín dụng mới tương đương 50% số tiền thu hồi được để duy trì mối quan hệ khách hàng và không làm gián đoạn thanh khoản bán lẻ. Kết quả là dòng tiền vào ròng được ghi nhận là $100\% \times (1 - 0{,}5) = 50\%$ (Paragraph 153);
- **Doanh nghiệp lớn phi tài chính, Chính phủ, NHTW và PSEs — Dòng tiền vào ròng 50%**: Tương tự như khách hàng bán lẻ, ngân hàng được giả định phải tiếp tục gia hạn hoặc cho vay mới 50% dòng tiền thu hồi đối với các tập đoàn phi tài chính và khu vực công quyền để duy trì chức năng cung cấp tín dụng cho nền kinh tế, dẫn đến dòng tiền vào ròng được công nhận là 50% (Paragraph 154);
- **Định chế tài chính và NHTW (Financial Institutions & Central Banks) — Dòng tiền vào ròng 100%**: Ngân hàng được giả định sẽ ngừng cấp tín dụng mới (0% loan extension) cho các đối tác tài chính trong khủng hoảng, do đó được phép ghi nhận toàn bộ 100% dòng tiền gốc và lãi thu hồi từ các ngân hàng khác và NHTW vào dòng tiền vào;
- **Chứng khoán đáo hạn trong 30 ngày (Securities Inflows)**: Các chứng khoán phi HQLA đáo hạn trong vòng 30 ngày được xếp vào nhóm định chế tài chính và hưởng hệ số dòng tiền vào 100% (Paragraph 155). Các chứng khoán Cấp 1 và Cấp 2 đáo hạn trong vòng 30 ngày được tính trực tiếp vào lượng HQLA sẵn có (Stock of HQLA) theo các điều kiện vận hành tại [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]].

**4. Vùng cấm ghi nhận dòng tiền vào (Zero-Inflow Buckets)**

Basel III thiết lập ba nhóm khoản mục tuyệt đối không được ghi nhận bất kỳ dòng tiền vào nào (0% Inflow Factor) nhằm ngăn ngừa sự méo mó cấu trúc thanh khoản (bcbs_238, file bcbs238.md, Paragraph 149, 156–157, d.605, 626–627):

- **Hạn mức cam kết tín dụng và thanh khoản nhận được (Committed Facilities) — Hệ số dòng tiền vào 0%**: Toàn bộ hạn mức tín dụng cam kết, hạn mức thanh khoản cam kết hoặc các hạn mức dự phòng mà ngân hàng được các tổ chức tài chính khác cấp cho mục đích tự thân đều **bị áp hệ số dòng tiền vào 0%** (Paragraph 149). Mục đích: Triệt tiêu nguy cơ lây lan rủi ro thanh khoản từ ngân hàng này sang ngân hàng khác, đồng thời phản ánh thực tế rằng trong khủng hoảng hệ thống, các ngân hàng cam kết sẽ viện dẫn các điều khoản vi phạm hợp đồng (Material Adverse Change) hoặc chấp nhận rủi ro pháp lý/danh tiếng để từ chối giải ngân nhằm bảo toàn thanh khoản của chính họ;
- **Tiền gửi hoạt động gửi tại các định chế tài chính khác (Operational Deposits Placed) — Hệ số dòng tiền vào 0%**: Các khoản tiền gửi mà ngân hàng gửi tại các tổ chức tín dụng khác nhằm mục đích duy trì các dịch vụ thanh toán bù trừ (clearing), lưu ký (custody) và quản lý tiền mặt (cash management) bị ấn định hệ số dòng tiền vào 0% (Paragraph 156). Do ngân hàng bắt buộc phải duy trì số dư này để tiếp tục vận hành hệ thống thanh toán hàng ngày, số tiền này hoàn toàn bị "khóa chặt" và không thể rút về để bù đắp các nghĩa vụ thanh khoản khác;
- **Tiền gửi tại tổ chức tập trung của mạng lưới ngân hàng hợp tác (Cooperative Banking Networks) — Hệ số dòng tiền vào 0%**: Tiền gửi của các ngân hàng thành viên gửi tại ngân hàng trung ương đầu mối của hệ thống hợp tác xã bị giả định phải duy trì cố định phục vụ nghĩa vụ mạng lưới (Paragraph 157).

**5. Dòng tiền vào từ phái sinh (Derivatives Cash Inflows — Paragraph 158–159)**

Dòng tiền vào ròng từ danh mục hợp đồng phái sinh được ghi nhận với hệ số **100%** (Paragraph 158). Việc tính toán dòng tiền phái sinh phải tuân thủ nguyên tắc bù trừ ròng (netting) theo hợp đồng khung Master Netting Agreement. Trường hợp các hợp đồng phái sinh được bảo đảm bằng tài sản thanh khoản cao (HQLA), dòng tiền vào phải được tính ròng sau khi đã trừ đi các nghĩa vụ ký quỹ bằng tiền mặt hoặc TSBĐ hợp đồng mà ngân hàng phải nộp, nhằm ngăn ngừa việc tính trùng dòng tiền và bảo đảm tính toàn vẹn của lượng HQLA theo [[basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer]].

Xem thêm: [[basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer]], [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]].
