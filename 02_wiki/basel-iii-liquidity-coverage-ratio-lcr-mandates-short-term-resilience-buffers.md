---
title: basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, basel-iii, cash-outflows, run-off-rates, regulation]
sources: [sbv_draft_circular_replace_22]
status: draft
last_updated: 2026-09-26
---

Tỷ lệ khả năng chi trả (Liquidity Coverage Ratio - LCR) là chuẩn mực an toàn thanh khoản ngắn hạn cốt lõi thuộc khung Basel III, được Ngân hàng Nhà nước Việt Nam chuẩn hóa tại Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN nhằm bảo đảm ngân hàng thương mại và chi nhánh ngân hàng nước ngoài luôn duy trì một bộ đệm tài sản có tính thanh khoản cao không bị ràng buộc, đủ năng lực tự hấp thụ và bù đắp các dòng tiền rút ròng đột biến trong kịch bản căng thẳng thanh khoản gay gắt kéo dài 30 ngày (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 17–21, d.461–580; Phụ lục I, d.873–1713).

**1. Công thức xác định Tỷ lệ LCR và các đồng tiền theo dõi bắt buộc**

Tỷ lệ khả năng chi trả được đo lường bằng tỷ số phần trăm giữa giá trị danh mục tài sản có tính thanh khoản cao đủ tiêu chuẩn ($HQLA$) và tổng dòng tiền ra ròng dự kiến trong khoảng thời gian 30 ngày tiếp theo (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 17.1.b, d.468–475):

$$LCR = \frac{\text{HQLA đủ điều kiện}}{\text{Tổng dòng tiền ra ròng trong 30 ngày}} \times 100\% \ge \text{Ngưỡng tối thiểu luật định}$$

Tổ chức tín dụng bắt buộc phải tính toán và theo dõi thường xuyên theo 3 chiều đồng tiền (Điều 17.1.a, d.464–467):
1. **Tỷ lệ LCR quy VNĐ**: Tính chung cho toàn bộ bảng cân đối, bao gồm đồng Việt Nam và mọi ngoại tệ được quy đổi sang VND theo tỷ giá hạch toán;
2. **Tỷ lệ LCR đối với Đồng Việt Nam (LCR VNĐ)**: Phản ánh khả năng thanh khoản tự thân bằng đồng bản tệ trên thị trường nội địa;
3. **Tỷ lệ LCR đối với từng ngoại tệ trọng yếu**: Ngân hàng phải thiết lập hạn mức quản trị riêng biệt cho các ngoại tệ có doanh số thanh toán và nghĩa vụ nợ lớn (như USD, EUR) nhằm phòng ngừa rủi ro tắc nghẽn chuyển đổi tiền tệ khi thị trường hoán đổi ngoại hối (FX Swap) bị đóng băng.

**Lộ trình áp dụng tỷ lệ LCR riêng lẻ** (Điều 17.1.c, d.476–481):
- Từ năm 2028: tối thiểu đạt **70%**;
- Từ năm 2029: tối thiểu đạt **80%**;
- Từ năm 2030: tối thiểu đạt **90%**;
- Từ năm 2031 trở đi: chính thức áp dụng chuẩn mực đầy đủ **100%**.

TCTD phải báo cáo tỷ lệ LCR riêng lẻ hàng ngày lên NHNN trước 15 giờ chiều ngày làm việc cho thời điểm cuối ngày liền kề trước (Điều 17.2, d.485–488).

**2. Tiêu chuẩn và yêu cầu vận hành đối với Danh mục Tài sản có tính thanh khoản cao (HQLA)**

Tài sản có tính thanh khoản cao là những tài sản có khả năng chuyển đổi dễ dàng và ngay lập tức sang tiền mặt với mức tổn thất giá trị bằng không hoặc không đáng kể trong điều kiện thị trường căng thẳng (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 19.1, d.509–530). Danh mục HQLA được phân tầng thành Tài sản Cấp 1 (tiền mặt, dự trữ vượt mức tại NHTW, trái phiếu chính phủ/tín phiếu kho bạc), Cấp 2A (haircut 15%) và Cấp 2B (haircut 25%–50%) kèm theo cơ chế đảo ngược giao dịch có kỳ hạn (unwinding) và trần cơ cấu danh mục tối đa 40% cho Cấp 2 và 15% cho Cấp 2B theo quy chuẩn kỹ thuật tại [[hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers]].

Để được công nhận là **HQLA đủ tiêu chuẩn** tính vào tử số của LCR, tài sản phải đáp ứng các yêu cầu vận hành nghiêm ngặt (Điều 20, d.536–563):
- **Tính chất không bị ràng buộc (Unencumbered)**: Tài sản không chịu bất kỳ giới hạn pháp lý, hợp đồng hoặc vận hành nào cản trở việc bán trực tiếp hoặc cầm cố; không được dùng để bảo đảm, thế chấp cho các nghĩa vụ khác hoặc phân bổ chi trả chi phí hoạt động (lương nhân viên, tiền thuê nhà). Tài sản nhận từ giao dịch Reverse Repo chỉ được tính vào HQLA nếu ngân hàng đã được chuyển giao toàn quyền sở hữu và chưa đem tái thế chấp (rehypothecation);
- **Kiểm soát độc quyền của Bộ phận Quản lý Thanh khoản (CFU/ALM/Treasury)**: Danh mục HQLA phải được hạch toán và duy trì trong một tài khoản riêng biệt thuộc quyền kiểm soát vận hành liên tục của bộ phận quản lý thanh khoản, nhằm mục đích duy nhất là làm đệm dự phòng thanh khoản mà không bị ràng buộc bởi các chiến lược tự doanh hay mục tiêu tìm kiếm lợi nhuận thông thường;
- **Thử nghiệm định kỳ khả năng chuyển đổi thành tiền mặt**: Ngân hàng phải định kỳ thực hiện các giao dịch bán thực tế hoặc giao dịch repo trên thị trường để kiểm tra độ trễ tác nghiệp, chiều sâu thanh khoản và loại trừ hiệu ứng phát tín hiệu tiêu cực (stigmatization) khi buộc phải bán tài sản trong khủng hoảng;
- **Phòng ngừa rủi ro thị trường (Hedging)**: Ngân hàng được phép phòng ngừa rủi ro lãi suất cho danh mục HQLA, nhưng khi tính toán giá trị thị trường phải tính trừ dòng tiền ra tiềm tàng nếu hợp đồng phái sinh bị đóng trước hạn. Nếu một tài sản HQLA bị suy giảm phẩm cấp trở thành không đủ tiêu chuẩn, ngân hàng được hưởng ân hạn 30 ngày để tái cấu trúc danh mục.

**3. Phương pháp đo lường Dòng tiền ra ròng (Net Cash Outflows)**

Tổng dòng tiền ra ròng trong chân trời 30 ngày được xác định bằng chênh lệch giữa tổng dòng tiền ra dự kiến và tổng dòng tiền vào dự kiến, kèm theo chốt chặn trần thu hồi vốn (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 21, d.564–579):

$$\text{Tổng dòng tiền ra ròng} = \text{Dòng tiền ra dự kiến} - \min\left(\text{Dòng tiền vào dự kiến},\ 75\% \times \text{Dòng tiền ra dự kiến}\right)$$

Nguyên tắc quản trị cốt lõi:
- **Ma trận rút vốn tiền gửi**: Dòng tiền ra từ tiền gửi bán lẻ ổn định (5%), kém ổn định (10%–40%), tiền gửi hoạt động (25%), doanh nghiệp lớn (40%) và bán buôn không bảo đảm (100%) được xác định chuẩn xác theo [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]];
- **Cam kết ngoại bảng và rò rỉ thanh khoản phái sinh**: Dòng tiền ra phát sinh từ hạn mức cam kết tín dụng/thanh khoản chưa sử dụng (5%–100%), rủi ro hạ 3 bậc tín nhiệm (100%), phương pháp Lookback 24 tháng cho phái sinh và cam kết tài trợ thương mại (3%) được lượng hóa theo [[contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments]];
- **Trần khống chế dòng tiền vào 75%**: Dòng tiền vào thu hồi từ cho vay có bảo đảm, Reverse Repo và thu nợ tín dụng bị giới hạn tối đa không quá 75% tổng dòng tiền ra dự kiến theo [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], bảo đảm ngân hàng luôn tự trang bị ít nhất 25% HQLA để thanh toán.

**4. Cơ chế cảnh báo sớm, chế tài tự xử lý và kỷ luật giám sát**

Dự thảo Thông tư thiết lập một hệ thống giám sát vi mô chủ động nhằm phát hiện sớm nguy cơ đứt gãy thanh khoản (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 18, d.489–508):
- **Nhận diện Nguy cơ mất khả năng chi trả**: Được xác định khi quy mô HQLA tại thời điểm tính toán rơi xuống **dưới 90%** mức HQLA tối thiểu bắt buộc để tuân thủ LCR trong thời gian **30 ngày liên tục**;
- **Nhận diện Mất khả năng chi trả**: Khi ngân hàng không thể thực hiện thanh toán nghĩa vụ nợ trong thời gian 30 ngày kể từ ngày đến hạn;
- **Biện pháp tự xử lý bắt buộc**: Khi tỷ lệ LCR bị vi phạm, ngân hàng phải kích hoạt ngay các công cụ khẩn cấp: vay liên ngân hàng, vay tổ chức tài chính nước ngoài, hoặc ký kết các cam kết tiền gửi/cho vay có kỳ hạn không thể hủy ngang. Nếu ngân hàng phải sử dụng các biện pháp tự xử lý ở mức **từ 10% HQLA trở lên**, NHNN sẽ áp dụng quy chế giám sát đặc biệt;
- **Báo cáo khẩn cấp**: Ngân hàng phải gửi báo cáo bằng văn bản trước **10 giờ sáng** ngày hôm sau giải trình rõ: nguyên nhân vi phạm, phân tích cú sốc riêng lẻ hay toàn hệ thống, mức độ suy giảm danh mục HQLA, và các biện pháp khắc phục.

**5. Ý nghĩa tương hỗ với các chỉ tiêu an toàn vĩ mô khác**

Chỉ số LCR tạo thành bộ ba trụ cột thanh khoản - đòn bẩy vững chắc khi kết hợp cùng [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]] (chống đỡ rủi ro cấu trúc kỳ hạn 1 năm), [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]] (kiểm soát đòn bẩy dư nợ trên huy động) và [[basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion]]. Trong hệ thống quản trị rủi ro nội bộ, LCR tương thích hoàn toàn với các kịch bản kiểm tra sức chịu đựng thanh khoản tại [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]] và là căn cứ để ALCO tính toán phụ phí thanh khoản cận biên trên đường cong FTP theo [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]].

Xem thêm: [[hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]], [[regulatory-liquidity-transition-rules-govern-dual-track-migration-from-mtll-to-lcr-nsfr]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]], [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]].
