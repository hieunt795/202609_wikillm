---
title: basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, basel, basel-iii, cash-outflows, run-off-rates, regulation, bcbs-238]
sources: [sbv_draft_circular_replace_22, bcbs_238]
status: stable
last_updated: 2026-09-26
---

Tỷ lệ khả năng chi trả (Liquidity Coverage Ratio - LCR) là chuẩn mực an toàn thanh khoản ngắn hạn cốt lõi thuộc hiệp ước Basel III (BCBS 238), được Ngân hàng Nhà nước Việt Nam chuẩn hóa tại Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN nhằm bảo đảm ngân hàng thương mại và chi nhánh ngân hàng nước ngoài luôn duy trì một bộ đệm tài sản có tính thanh khoản cao không bị ràng buộc (HQLA), đủ năng lực tự hấp thụ và bù đắp các dòng tiền rút ròng đột biến trong kịch bản căng thẳng thanh khoản kết hợp gay gắt kéo dài 30 ngày dương lịch (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 17–21, d.461–580; Phụ lục I, d.873–1713; bcbs_238, file bcbs238.md, Introduction & Part 1 Section I–II, Paragraphs 1–22, d.71–156).

**1. Công thức xác định Tỷ lệ LCR và các đồng tiền theo dõi bắt buộc**

Tỷ lệ khả năng chi trả được đo lường bằng tỷ số phần trăm giữa giá trị danh mục tài sản có tính thanh khoản cao đủ tiêu chuẩn ($HQLA$) và tổng dòng tiền ra ròng dự kiến trong khoảng thời gian 30 ngày tiếp theo (bcbs_238, Paragraph 17, 22, d.108, 145; sbv_draft_circular_replace_22, Điều 17.1.b, d.468–475):

$$LCR = \frac{\text{Giá trị danh mục HQLA trong điều kiện căng thẳng}}{\text{Tổng dòng tiền ra ròng trong 30 ngày dương lịch}} \times 100\% \ge \text{Ngưỡng tối thiểu luật định}$$

Tổ chức tín dụng bắt buộc phải tính toán và theo dõi thường xuyên theo 3 chiều đồng tiền (Điều 17.1.a, d.464–467; bcbs_238, Paragraph 42, 209–213, d.212, 794–817):
1. **Tỷ lệ LCR quy VNĐ**: Tính chung cho toàn bộ bảng cân đối, bao gồm đồng Việt Nam và mọi ngoại tệ được quy đổi sang VND theo tỷ giá hạch toán;
2. **Tỷ lệ LCR đối với Đồng Việt Nam (LCR VNĐ)**: Phản ánh khả năng thanh khoản tự thân bằng đồng bản tệ trên thị trường nội địa;
3. **Tỷ lệ LCR đối với từng ngoại tệ trọng yếu (Significant Currencies)**: Ngân hàng phải thiết lập hạn mức quản trị riêng biệt cho các ngoại tệ chiếm từ 5% tổng nợ phải trả trở lên (như USD, EUR) nhằm phòng ngừa rủi ro tắc nghẽn chuyển đổi tiền tệ khi thị trường hoán đổi ngoại hối (FX Swap) bị đóng băng trong khủng hoảng.

**Lộ trình áp dụng chuẩn mực LCR**:
- *Lộ trình quốc tế theo Basel III (BCBS 238, Paragraph 8–10, d.82–90)*: Bắt đầu từ 01/01/2015 ở mức 60%, tăng dần mỗi năm 10% (2016: 70%, 2017: 80%, 2018: 90%) và đạt chuẩn mực đầy đủ **100% vào ngày 01/01/2019**;
- *Lộ trình nội luật hóa tại Việt Nam (sbv_draft_circular_replace_22, Điều 17.1.c, d.476–481)*: Từ năm 2028 tối thiểu đạt **70%**; từ 2029 đạt **80%**; từ 2030 đạt **90%**; và từ năm 2031 trở đi chính thức áp dụng chuẩn mực đầy đủ **100%**.

TCTD phải báo cáo tỷ lệ LCR riêng lẻ hàng ngày lên NHNN trước 15 giờ chiều ngày làm việc cho thời điểm cuối ngày liền kề trước (Điều 17.2, d.485–488).

**2. Tiêu chuẩn và yêu cầu vận hành đối với Danh mục Tài sản có tính thanh khoản cao (HQLA)**

Tài sản có tính thanh khoản cao là những tài sản có khả năng chuyển đổi dễ dàng và ngay lập tức sang tiền mặt với mức tổn thất giá trị bằng không hoặc không đáng kể trong điều kiện thị trường căng thẳng theo [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]] (bcbs_238, Paragraph 24–27, d.157–187; sbv_draft_circular_replace_22, Điều 19.1, d.509–530). Danh mục HQLA được phân tầng thành Tài sản Cấp 1 (tiền mặt, dự trữ vượt mức tại NHTW, trái phiếu chính phủ/tín phiếu kho bạc), Cấp 2A (haircut 15%) và Cấp 2B (haircut 25%–50%) theo [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], kèm theo cơ chế đảo ngược giao dịch có kỳ hạn (unwinding) và trần cơ cấu danh mục tối đa 40% cho Cấp 2 và 15% cho Cấp 2B theo [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]].

Để được công nhận là **HQLA đủ tiêu chuẩn** tính vào tử số của LCR, tài sản phải đáp ứng các yêu cầu vận hành nghiêm ngặt theo [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]] (bcbs_238, Paragraph 28–44, d.188–218; sbv_draft_circular_replace_22, Điều 20, d.536–563):
- **Tính chất không bị ràng buộc (Unencumbered)**: Không chịu bất kỳ giới hạn pháp lý, hợp đồng hoặc vận hành nào cản trở việc bán trực tiếp hoặc cầm cố; không được dùng để bảo đảm, thế chấp cho các nghĩa vụ khác hoặc phân bổ chi trả chi phí hoạt động (lương nhân viên, tiền thuê nhà). Nếu ngân hàng ký gửi một pool tài sản thế chấp hỗn hợp tại NHTW, quy tắc phân bổ giả định phong tỏa theo thứ tự từ thanh khoản thấp nhất đến cao nhất (Footnote 9: phi HQLA $\to$ Level 2B $\to$ Level 2A $\to$ Level 1) nhằm bảo vệ tối đa HQLA unencumbered;
- **Kiểm soát độc quyền của Bộ phận Quản lý Thanh khoản (Treasury/ALM)**: Danh mục HQLA phải được duy trì trong một tài khoản riêng biệt thuộc quyền kiểm soát vận hành liên tục của Treasury, sẵn sàng monetise mọi lúc trong 30 ngày mà không xung đột với các vị thế phòng ngừa rủi ro (hedging);
- **Thử nghiệm định kỳ khả năng chuyển đổi thành tiền mặt**: Ngân hàng phải định kỳ thực hiện các giao dịch bán thực tế hoặc giao dịch repo trên thị trường để kiểm tra độ trễ tác nghiệp, chiều sâu thanh khoản và loại trừ hiệu ứng phát tín hiệu tiêu cực (stigmatization);
- **Phòng ngừa rủi ro và thời gian ân hạn 30 ngày**: Cho phép hedge rủi ro thị trường nhưng phải trừ dòng tiền ra nếu hợp đồng phái sinh bị đóng trước hạn. Nếu một tài sản HQLA bị tụt hạng tín nhiệm không còn đủ tiêu chuẩn, ngân hàng được hưởng thời gian ân hạn 30 ngày để tái cấu trúc danh mục. Đối với các quốc gia thiếu hụt HQLA nội tệ mang tính cơ cấu, cơ chế [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]] cho phép áp dụng hạn mức cam kết từ NHTW có thu phí (CLF) hoặc sử dụng HQLA ngoại tệ có kiểm soát.

**3. Phương pháp đo lường Dòng tiền ra ròng (Net Cash Outflows) và Trần khống chế 75%**

Tổng dòng tiền ra ròng trong chân trời 30 ngày được xác định bằng chênh lệch giữa tổng dòng tiền ra dự kiến và tổng dòng tiền vào dự kiến, kèm theo chốt chặn trần thu hồi vốn bắt buộc theo [[basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer]] (bcbs_238, Paragraph 69, 144, d.374–376, 584; sbv_draft_circular_replace_22, Điều 21, d.564–579):

$$\text{Tổng dòng tiền ra ròng} = \text{Dòng tiền ra dự kiến} - \min\left(\text{Dòng tiền vào dự kiến},\ 75\% \times \text{Dòng tiền ra dự kiến}\right)$$

Nguyên tắc định lượng chuyên sâu theo Basel III:
- **Ma trận rút vốn tiền gửi**: Dòng tiền ra từ tiền gửi bán lẻ ổn định (3%–5%), kém ổn định (10%–40%), tiền gửi hoạt động (25%), doanh nghiệp lớn (20%–40%) và bán buôn không bảo đảm (100%) được xác định chuẩn xác theo [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]] và [[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]];
- **Tài trợ có bảo đảm và Cam kết ngoại bảng**: Lượng hóa rút vốn Repo theo phân tầng TSBĐ tại [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], kết hợp các cú sốc rút hạn mức cam kết tín dụng/thanh khoản (5%–100%), hạ 3 bậc tín nhiệm (100%), Lookback phái sinh 24 tháng và tài trợ thương mại (3%–5%) tại [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]];
- **Dòng tiền vào và Trần khống chế 75%**: Dòng tiền vào thu hồi từ cho vay có bảo đảm, Reverse Repo và thu nợ tín dụng theo [[secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk]] bị giới hạn tối đa không quá 75% tổng dòng tiền ra dự kiến, cưỡng chế ngân hàng luôn duy trì ít nhất 25% HQLA tự thân để thanh toán nghĩa vụ;
- **Quản trị LCR hợp nhất xuyên biên giới và Loại trừ thanh khoản bị giam lỏng**: Áp dụng chuẩn mực tại [[consolidated-lcr-cross-border-framework-regulates-home-host-discretion-and-trapped-liquidity]], tập đoàn quốc tế phải áp dụng quy tắc Home - Host (bắt buộc dùng host run-off rate cho tiền gửi bán lẻ bản địa) và loại bỏ hoàn toàn phần HQLA thặng dư bị giam lỏng (trapped liquidity) do rào cản kiểm soát ngoại hối hoặc ring-fencing khỏi LCR hợp nhất.

**4. Nguyên tắc sử dụng đệm HQLA trong khủng hoảng và Kỷ luật giám sát**

Một nguyên tắc cốt lõi được khẳng định tại [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]] (bcbs_238, Paragraph 11 & 17–18, d.85, 108–132) là: **trong điều kiện căng thẳng tài chính, ngân hàng hoàn toàn được phép sử dụng đệm HQLA, chấp nhận để tỷ lệ LCR giảm xuống dưới 100%**. Việc ép buộc cứng nhắc ngân hàng duy trì 100% trong khủng hoảng sẽ gây ra tính nghịch chu kỳ (procyclicality), buộc các ngân hàng phải bán tháo tài sản và thắt chặt tín dụng, làm trầm trọng thêm sự đóng băng thanh khoản của hệ thống.

Cơ quan thanh tra giám sát áp dụng phản ứng linh hoạt và tương xứng:
- Phân biệt rõ giữa cú sốc mang tính riêng lẻ (idiosyncratic) và khủng hoảng mang tính toàn hệ thống (market-wide);
- Tại Việt Nam, Điều 18 Thông tư quy định: nếu HQLA rơi xuống **dưới 90%** mức tối thiểu trong **30 ngày liên tục** (nguy cơ mất khả năng chi trả), hoặc ngân hàng phải sử dụng các biện pháp tự xử lý (vay liên ngân hàng, cam kết không hủy ngang) ở mức **từ 10% HQLA trở lên**, ngân hàng phải gửi văn bản giải trình trước **10 giờ sáng** ngày hôm sau và chịu sự giám sát tăng cường của NHNN;
- Trong khủng hoảng hệ thống diện rộng, cơ quan giám sát và ngân hàng sẽ thống nhất một lộ trình tái thiết bộ đệm thanh khoản được thực hiện từng bước qua thời gian để tránh gây tổn thương đến sự ổn định tài chính vĩ mô.

**5. Ý nghĩa tương hỗ với các chỉ tiêu an toàn vĩ mô khác**

Chỉ số LCR tạo thành bộ ba trụ cột thanh khoản - đòn bẩy vững chắc khi kết hợp cùng [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]] (chống đỡ rủi ro cấu trúc kỳ hạn 1 năm), [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]] (kiểm soát đòn bẩy dư nợ trên huy động) và [[basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion]]. Trong hệ thống quản trị rủi ro nội bộ, LCR tương thích hoàn toàn với các kịch bản kiểm tra sức chịu đựng thanh khoản tại [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]] và là căn cứ để ALCO tính toán phụ phí thanh khoản cận biên trên đường cong FTP theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]].

Xem thêm: [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer]], [[secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk]], [[consolidated-lcr-cross-border-framework-regulates-home-host-discretion-and-trapped-liquidity]], [[hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]], [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]], [[regulatory-liquidity-transition-rules-govern-dual-track-migration-from-mtll-to-lcr-nsfr]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]], [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]].
