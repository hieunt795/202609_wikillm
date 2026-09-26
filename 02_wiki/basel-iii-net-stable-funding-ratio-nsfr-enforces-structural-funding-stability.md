---
title: basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability
type: concept
tags: [banking, alm, liquidity-risk, nsfr, asf, rsf, basel-iii, funding-stability, derivatives, regulation]
sources: [sbv_draft_circular_replace_22]
status: draft
last_updated: 2026-09-26
---

Tỷ lệ nguồn vốn ổn định ròng (Net Stable Funding Ratio - NSFR) là chuẩn mực điều hành cấu trúc thanh khoản trung và dài hạn cốt lõi của hiệp ước Basel III, được Ngân hàng Nhà nước nội luật hóa tại Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN nhằm thiết lập kỷ luật tài trợ bền vững, buộc các ngân hàng thương mại và chi nhánh ngân hàng nước ngoài phải tài trợ các tài sản dài hạn và hoạt động ngoại bảng bằng các nguồn vốn có tính ổn định tương thích trong chân trời một năm (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 22–26, d.580–706; Phụ lục II, d.1714–1908).

Khác với tỷ lệ khả năng chi trả ngắn hạn [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]] (tập trung vào bộ đệm tài sản thanh khoản cao 30 ngày), NSFR giải quyết triệt để rủi ro chênh lệch kỳ hạn cơ cấu (structural maturity mismatch), ngăn chặn tình trạng phụ thuộc quá mức vào nguồn vốn ngắn hạn bán buôn để tài trợ cho tăng trưởng tín dụng trung dài hạn.

**1. Công thức xác định Tỷ lệ NSFR và lộ trình thực thi**

Tỷ lệ nguồn vốn ổn định ròng được định nghĩa bằng tỷ lệ phần trăm giữa Nguồn vốn ổn định sẵn có (Available Stable Funding - $ASF$) và Nguồn vốn ổn định yêu cầu (Required Stable Funding - $RSF$) (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 22.1, d.581–589):

$$NSFR = \frac{ASF}{RSF} \times 100\% \ge \text{Ngưỡng tối thiểu luật định}$$

Phạm vi theo dõi là tỷ lệ NSFR riêng lẻ tính theo Đồng Việt Nam (bao gồm cả số dư VND và các ngoại tệ quy đổi sang VND theo tỷ giá quy chuẩn). Báo cáo NSFR được thực hiện định kỳ hàng tháng trong 15 ngày đầu tiên của tháng tiếp theo cho thời điểm cuối ngày của tháng liền kề trước (Điều 22.4, d.592–599).

**Lộ trình áp dụng tỷ lệ NSFR riêng lẻ** (Điều 22.2, d.590–597):
- Từ năm 2028: tối thiểu đạt **90%**;
- Từ năm 2029: tối thiểu đạt **95%**;
- Từ năm 2030 trở đi: áp dụng chuẩn mực trọn vẹn **100%**.

Đối với các ngân hàng đã tự nguyện áp dụng sớm và đạt NSFR từ 100% trở lên, Thông tư dành riêng cơ chế miễn trừ hoàn toàn tỷ lệ tối đa nguồn vốn ngắn hạn cho vay trung dài hạn (MTLL) theo [[regulatory-liquidity-transition-rules-govern-dual-track-migration-from-mtll-to-lcr-nsfr]].

**2. Đo lường Nguồn vốn ổn định sẵn có (Available Stable Funding - ASF)**

Nguồn vốn ổn định sẵn có đo lường quy mô vốn chủ sở hữu và các khoản nợ phải trả được kỳ vọng là nguồn tài trợ đáng tin cậy trong vòng 1 năm (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 23, d.605–630):

$$ASF = \sum \left(\text{Giá trị ghi sổ các thành phần nguồn vốn}_i \times \text{Hệ số } ASF_i\right)$$

Hệ số $ASF$ phân bổ từ 0% đến 100% phản ánh mức độ gắn bó của dòng tiền theo ma trận chi tiết tại [[asf-and-rsf-factor-matrices-calibrate-nsfr-structural-funding-requirements]] (sbv_draft_circular_replace_22, Phụ lục II Phần A, d.1718–1750):
- **Hệ số ASF 100%**: Vốn tự có Cấp 1 và Cấp 2 đủ điều kiện theo [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]]; nợ thứ cấp và công cụ vốn có kỳ hạn còn lại từ 1 năm trở lên; các khoản nợ và tiền gửi từ khách hàng bán buôn/doanh nghiệp có kỳ hạn còn lại từ 1 năm trở lên;
- **Hệ số ASF 95% / 90%**: Tiền gửi không kỳ hạn và tiền gửi có kỳ hạn dưới 1 năm của khách hàng cá nhân và doanh nghiệp nhỏ và vừa (SME) có tính ổn định cao (được bảo hiểm tiền gửi hoặc có quan hệ giao dịch lâu năm theo quy tắc định giá tại [[deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles]]);
- **Hệ số ASF 50%**: Nguồn tài trợ ngắn hạn (kỳ hạn dưới 1 năm) từ các doanh nghiệp phi tài chính lớn, tiền gửi hoạt động (operational deposits);
- **Hệ số ASF 0%**: Nguồn tài trợ không có bảo đảm từ các tổ chức tín dụng khác và định chế tài chính có kỳ hạn dưới 6 tháng; trạng thái nợ phái sinh ròng; các khoản tiền gửi biến động bị hạn chế sử dụng.

**Các giả định kỳ hạn và hành vi bắt buộc khi tính ASF** (Điều 23.4, d.621–629):
1. **Quyền chọn mua của nhà đầu tư (Call option)**: Phải giả định nhà đầu tư sẽ thực hiện quyền đòi lại tiền tại thời điểm sớm nhất có thể theo hợp đồng;
2. **Không tính thời gian gia hạn nợ**: Bỏ qua quyền chọn gia hạn của ngân hàng, trừ khi có bằng chứng chắc chắn;
3. **Kỳ vọng thị trường về thanh toán trước hạn**: Nếu việc không mua lại trái phiếu trước hạn có thể làm tổn hại uy tín thanh khoản của ngân hàng, kỳ hạn phải được tính lùi về thời điểm thị trường kỳ vọng.

**3. Đo lường Nguồn vốn ổn định yêu cầu (Required Stable Funding - RSF)**

Nguồn vốn ổn định yêu cầu đo lường quy mô tài sản nội bảng và các cam kết ngoại bảng đòi hỏi phải được tài trợ bằng nguồn vốn bền vững (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 24, d.631–662):

$$RSF = \sum \left(\text{Giá trị ghi sổ các tài sản và cam kết}_j \times \text{Hệ số } RSF_j\right)$$

Nguyên tắc xác định hệ số $RSF$:
- Giá trị ghi sổ nội bảng của các khoản cấp tín dụng được xác định sau khi **đã khấu trừ dự phòng cụ thể** (nhưng chưa trừ dự phòng chung);
- Tài sản có tính thanh khoản cao (HQLA) không bị ràng buộc áp dụng hệ số $RSF$ rất thấp (0% đối với tiền mặt, dự trữ NHTW và TPCP ngắn hạn; 5%–15% đối với trái phiếu chính phủ dài hạn);
- Các khoản cho vay đối với nền kinh tế thực có kỳ hạn còn lại dưới 1 năm áp dụng hệ số $RSF = 50\%$; các khoản vay trung dài hạn (kỳ hạn trên 1 năm) có trọng số rủi ro tín dụng $\le 35\%$ theo phương pháp tiêu chuẩn [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]] áp hệ số $RSF = 65\%$, còn các khoản vay thương mại thông thường và bất động sản có rủi ro cao áp hệ số $RSF = 85\%$ hoặc $100\%$;
- **Tài sản có quyền chọn và trả góp**: Đối với các khoản vay trả góp, phần dư nợ gốc đến hạn trong vòng 1 năm được tách riêng và xếp vào nhóm kỳ hạn dưới 1 năm. Nếu hợp đồng có ngày rà soát định kỳ (review date) để quyết định gia hạn, ngày rà soát đó được coi là ngày đáo hạn (Điều 24.5, d.651–656).

**Cơ chế điều tiết đặc biệt theo chính sách tiền tệ** (Điều 24.6, d.657–660):
- Khi Ngân hàng Nhà nước thực hiện nghiệp vụ hút thanh khoản (qua tín phiếu hoặc thị trường mở OMO), TCTD được phép **giảm tối đa 50% hệ số RSF** áp dụng đối với các khoản phải thu từ NHNN có kỳ hạn còn lại từ 6 tháng trở lên;
- Khi NHNN cung cấp thanh khoản tái cấp vốn, TCTD áp dụng hệ số $RSF$ đối với tài sản bảo đảm bằng với tài sản tương đương không bị ràng buộc, bảo đảm chính sách tiền tệ truyền dẫn thông suốt mà không làm ngân hàng bị áp lực vi phạm NSFR.

**4. Quy tắc xử lý giao dịch Phái sinh trong NSFR**

Quy định tại Điều 25 thiết lập chuẩn mực đo lường phái sinh đồng bộ với hiệp ước Basel III (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 25, d.663–695):
- **Bù trừ song phương (Netting)**: Giá trị tài sản phái sinh (MTM dương) và nợ phái sinh (MTM âm) được bù trừ ròng nếu đáp ứng đầy đủ điều kiện hợp đồng khung netting hợp pháp;
- **Ký quỹ biến động bằng tiền mặt (Cash Variation Margin - CVM)**: Chỉ các khoản tiền mặt ký quỹ đáp ứng tiêu chuẩn thanh toán trước hạn (pre-settlement payment) — được thanh toán hàng ngày để triệt tiêu toàn bộ rủi ro MTM và bên nhận được toàn quyền sử dụng tiền — mới được khấu trừ khỏi tài sản phái sinh;
- **Nguyên tắc so sánh trạng thái ròng**:
  - Nếu $\text{Nợ phái sinh NSFR} > \text{Tài sản phái sinh NSFR}$: Phần chênh lệch dương được tính vào $ASF$ nhưng áp dụng hệ số **$ASF = 0\%$** (không coi phái sinh âm là nguồn vốn ổn định);
  - Nếu $\text{Tài sản phái sinh NSFR} > \text{Nợ phái sinh NSFR}$: Phần chênh lệch dương bắt buộc phải tính vào $RSF$ và áp dụng hệ số tối đa **$RSF = 100\%$** (buộc ngân hàng phải dùng 100% nguồn vốn ổn định để tài trợ cho phơi nhiễm phái sinh ròng).

**5. Cơ chế xử lý Cặp tài sản và nợ phải trả phụ thuộc lẫn nhau (Interdependent Assets & Liabilities)**

Dự thảo quy định cơ chế miễn trừ đặc thù cho các nghiệp vụ chuyển tiếp thuần túy (Pass-through) tại Điều 26 (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 26, d.696–706):
- **Điều kiện khắt khe**: Nguồn vốn huy động được chỉ định duy nhất để tài trợ cho một tài sản cụ thể và không thể chuyển hướng; ngân hàng không phải thanh toán cho chủ nợ nếu chưa thu hồi được từ con nợ; kỳ hạn, lịch thanh toán gốc lãi trùng khớp hoàn toàn; ngân hàng không chịu bất kỳ rủi ro tín dụng hay thanh khoản nào;
- **Ưu đãi quy chuẩn**: Cặp tài sản và nợ phụ thuộc đủ điều kiện được áp dụng đồng thời **$ASF = 0\%$** và **$RSF = 0\%$**, hoàn toàn trung hòa tác động lên tỷ lệ NSFR;
- **Chế tài vi phạm nghiêm khắc**: Nếu NHNN phát hiện ngân hàng lợi dụng cơ chế này khi không thỏa mãn điều kiện thực tế, ngân hàng sẽ bị tước quyền áp dụng $ASF=0\% / RSF=0\%$ cho toàn bộ các cặp nghiệp vụ khác trên toàn hệ thống.

**6. Mối liên kết với Quản trị Cân đối Bảng tài sản (ALM) và Hệ thống FTP**

Chỉ số NSFR là động lực kỹ thuật trực tiếp định hình đường cong định giá điều chuyển vốn nội bộ (FTP). Khối ALM lượng hóa chi phí tuân thủ NSFR bằng cách áp phụ phí thanh khoản kỳ hạn dài $\Delta Spread_{long}$ đối với các tài sản có hệ số $RSF$ cao (như tín dụng doanh nghiệp dài hạn, phái sinh không bảo đảm) và cấp điểm thưởng cho các nguồn huy động có $ASF \ge 95\%$ theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]]. Khi kết hợp cùng [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]] và [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]], NSFR tạo nên bộ khung điều hành cấu trúc thanh khoản toàn diện, bảo vệ bảng cân đối ngân hàng trước các cú sốc rút tiền hoặc đóng băng thị trường vốn.

Xem thêm: [[asf-and-rsf-factor-matrices-calibrate-nsfr-structural-funding-requirements]], [[pillar-3-liquidity-disclosure-standards-mandate-qualitative-and-quantitative-market-transparency]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[regulatory-liquidity-transition-rules-govern-dual-track-migration-from-mtll-to-lcr-nsfr]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[deposit-product-vof-pricing-rules-accommodate-installment-and-nonterm-profiles]], [[funds-transfer-pricing-curve-decomposes-into-pure-interest-rate-and-liquidity-spreads]], [[counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure]], [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]], [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]].
