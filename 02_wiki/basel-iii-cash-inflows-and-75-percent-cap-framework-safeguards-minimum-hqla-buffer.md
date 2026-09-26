---
title: basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer
type: concept
tags: [basel, basel-iii, lcr, liquidity, liquidity-risk, cash-inflows, inflow-cap, net-cash-outflows, hqla, bcbs-238, regulation]
sources: [bcbs_238]
status: stable
last_updated: 2026-09-26
---

Khung đo lường dòng tiền vào và trần khống chế 75% theo chuẩn mực Basel III (BCBS 238, Paragraph 142–144) quy định rằng ngân hàng chỉ được phép ghi nhận các dòng tiền vào theo hợp đồng từ các phơi nhiễm đang thực hiện bình thường, đồng thời giới hạn mức bù trừ tối đa của dòng tiền vào ở mức 75% tổng dòng tiền ra dự kiến nhằm cưỡng chế ngân hàng luôn phải duy trì một lượng đệm tài sản thanh khoản cao (HQLA) tự thân tối thiểu bằng 25% tổng dòng tiền ra (bcbs_238, file bcbs238.md, Paragraph 142–144, d.580–585). Quy định này triệt tiêu rủi ro đạo đức khi các ngân hàng cố tình cấu trúc các hợp đồng tài trợ phái sinh hoặc kỳ hạn ngắn nhằm thổi phồng dòng tiền vào ảo để hạ thấp nghĩa vụ dự trữ thanh khoản thực tế trong 30 ngày khủng hoảng nghiêm trọng.

**1. Tiêu chuẩn ghi nhận dòng tiền vào hợp đồng hợp lệ (Paragraph 142, 151–152, 160)**

Để một khoản tiền vào được tính toán trong mẫu số của [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], khoản mục đó bắt buộc phải thỏa mãn đồng thời các điều kiện khắt khe về tính hợp đồng và khả năng thực thi thực tế (bcbs_238, file bcbs238.md, Paragraph 142, d.582):

- **Tính hợp đồng và trạng thái hoạt động bình thường (Fully Performing)**: Ngân hàng chỉ được tính các dòng tiền vào (gồm cả nợ gốc và các khoản thanh toán lãi) phát sinh theo hợp đồng trong vòng 30 ngày từ các phơi nhiễm đang hoạt động tốt mà ngân hàng không có bất kỳ căn cứ nào để dự đoán sẽ vỡ nợ hoặc chậm trả trong chân trời 30 ngày. Các khoản nợ xấu, nợ quá hạn hoặc nợ tái cơ cấu có dấu hiệu suy giảm khả năng thanh toán bị loại bỏ hoàn toàn (0% inflow);
- **Loại trừ tuyệt đối dòng tiền vào tiềm năng (Contingent Inflows)**: Dòng tiền vào tiềm năng phát sinh từ các hạn mức tín dụng cam kết hoặc thanh khoản cam kết mà ngân hàng được cấp tại các định chế khác bị áp hệ số 0% theo [[secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk]], nhằm ngăn ngừa rủi ro lây lan hệ thống (contagion risk);
- **Nguyên tắc thời điểm thận trọng nhất (Latest Possible Date)**: Dòng tiền thu hồi nợ chỉ được ghi nhận vào ngày muộn nhất có thể căn cứ theo các quyền hợp đồng sẵn có của đối tác (Paragraph 151). Đối với các hạn mức tín dụng quay vòng (revolving credit), giả định rằng khoản vay hiện hữu được gia hạn và phần hạn mức còn lại được xử lý như cam kết ngoại bảng;
- **Xử lý khoản vay không xác định kỳ hạn (Open Maturity)**: Các khoản vay không quy định kỳ hạn đáo hạn cụ thể (non-defined/open maturity loans) hoàn toàn không được tính dòng tiền vào, ngoại trừ các khoản thanh toán tối thiểu theo hợp đồng về gốc, phí hoặc lãi đến hạn trong 30 ngày (Paragraph 152);
- **Loại trừ doanh thu phi tài chính (Non-Financial Revenues)**: Toàn bộ dòng tiền vào từ các hoạt động kinh doanh phi tài chính (doanh thu bán hàng hóa, cung cấp dịch vụ phi ngân hàng, cho thuê tài sản phi tài chính...) không được đưa vào tính toán LCR (Paragraph 160, d.633).

**2. Cơ chế trần dòng tiền vào 75% và sự bảo đảm đệm HQLA tối thiểu 25% (Paragraph 144)**

Trong các cuộc khủng hoảng thanh khoản lịch sử, các dòng tiền vào dự kiến trên hợp đồng thường bị đình trệ, tranh chấp pháp lý hoặc không thể thu hồi kịp thời do đối tác phá sản dây chuyền. Nhằm ngăn ngừa ngân hàng phụ thuộc hoàn toàn vào dòng tiền vào để đáp ứng nhu cầu rút tiền, Basel III thiết lập cơ chế trần khống chế dòng tiền vào (Cap on Total Inflows) tại Paragraph 144 (bcbs_238, file bcbs238.md, Paragraph 144, d.584):

- **Quy tắc trần bù trừ 75%**: Tổng số dòng tiền vào được phép sử dụng để bù trừ dòng tiền ra bị khống chế tối đa bằng 75% tổng dòng tiền ra dự kiến:
$$\text{Allowable Inflows} = \min\left(\text{Total Expected Cash Inflows},\ 0{,}75 \times \text{Total Expected Cash Outflows}\right)$$
- **Công thức xác định Dòng tiền ra ròng tổng thể (Total Net Cash Outflows)**:
$$\text{Total Net Cash Outflows} = \text{Total Expected Cash Outflows} - \min\left(\text{Total Expected Cash Inflows},\ 0{,}75 \times \text{Total Expected Cash Outflows}\right)$$
$$\text{Total Net Cash Outflows} = \max\left(\text{Total Expected Cash Outflows} - \text{Total Expected Cash Inflows},\ 0{,}25 \times \text{Total Expected Cash Outflows}\right)$$
- **Hệ quả kinh tế bắt buộc — Tấm đệm sàn HQLA 25%**:
Ngay cả trong trường hợp một ngân hàng có vị thế dòng tiền vào hợp đồng rất lớn vượt quá dòng tiền ra ($\text{Total Inflows} \ge \text{Total Outflows}$), thì dòng tiền ra ròng của ngân hàng vẫn bị ấn định ở mức sàn tối thiểu:
$$\text{Total Net Cash Outflows} \ge 0{,}25 \times \text{Total Expected Cash Outflows}$$
Do chuẩn mực yêu cầu $\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total Net Cash Outflows}} \ge 100\%$, ngân hàng bắt buộc phải nắm giữ một danh mục tài sản thanh khoản cao không bị ràng buộc (unencumbered [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]]) thực tế có giá trị tối thiểu bằng 25% tổng dòng tiền ra:
$$\text{Stock of HQLA} \ge 0{,}25 \times \text{Total Expected Cash Outflows}$$
Cơ chế này ngăn chặn tình trạng "ngân hàng không có đệm thanh khoản" (zero-buffer banks) trên thị trường tiền tệ.

**3. Công thức tổng thể hoàn chỉnh của Tỷ lệ Khả năng Chi trả (LCR)**

Kết hợp cơ chế trần tài sản Cấp 2, trần Cấp 2B và unwinding SFT $\le 30$ ngày tại [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]] với trần dòng tiền vào 75%, tỷ lệ LCR được xác định theo công thức chuẩn hóa tuyệt đối:

$$\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total Net Cash Outflows}} = \frac{\text{Level 1} + \text{Level 2A} + \text{Level 2B} - \text{Adjustment for 15\% cap} - \text{Adjustment for 40\% cap}}{\text{Total Outflows} - \min\left(\text{Total Inflows},\ 0{,}75 \times \text{Total Outflows}\right)} \ge 100\%$$

Trong đó:
- Tử số là quy mô HQLA sau khi đã khấu trừ chiết khấu (haircuts) và loại trừ phần vượt trần thông qua mô phỏng hoàn trả toàn bộ các giao dịch tài trợ có bảo đảm ngắn hạn;
- Mẫu số phản ánh chênh lệch dòng tiền chịu áp lực sau khi đã áp dụng đầy đủ ma trận hệ số rút tiền đối với tiền gửi bán lẻ ([[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]]), tiền gửi hoạt động ([[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]]), nợ bán buôn ([[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]]), tài trợ có bảo đảm ([[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]]), cam kết ngoại bảng ([[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]]) và khấu trừ dòng tiền vào hợp lệ bị khống chế trần 75%.

**4. Giám sát mức độ tập trung dòng tiền vào bán buôn (Paragraph 143)**

Bên cạnh giới hạn toán học 75%, Basel III đặt ra yêu cầu giám sát định tính và hạn mức nội bộ đối với rủi ro tập trung dòng tiền vào (Concentration of Expected Inflows). Ngân hàng và cơ quan thanh tra giám sát phải thường xuyên phân tích cơ cấu dòng tiền vào theo từng đối tác bán buôn trọng yếu (wholesale counterparties) nhằm đảm bảo vị thế thanh khoản không bị phụ thuộc quá mức vào dòng tiền hồi hương từ một hoặc một nhóm nhỏ đối tác tài chính (bcbs_238, file bcbs238.md, Paragraph 143, d.583). Nếu một đối tác bán buôn lớn gặp khủng hoảng thanh khoản cục bộ hoặc mất khả năng chi trả, dòng tiền vào của ngân hàng sẽ bị tắc nghẽn, đẩy ngân hàng vào nguy cơ cạn kiệt thanh khoản tức thì. Yêu cầu này liên kết trực tiếp với công cụ giám sát tập trung nguồn vốn tại [[funding-diversification-and-market-access-testing-mitigate-wholesale-refinancing-freezes]].

Xem thêm: [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[consolidated-lcr-cross-border-framework-regulates-home-host-discretion-and-trapped-liquidity]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[funding-diversification-and-market-access-testing-mitigate-wholesale-refinancing-freezes]].
