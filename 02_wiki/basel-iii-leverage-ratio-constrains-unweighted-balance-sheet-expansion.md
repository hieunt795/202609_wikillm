---
title: basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion
type: concept
tags: [banking, leverage-ratio, basel-iii, pillar-1, exposure-measure, tier-1-capital, d-sib, regulation]
sources: [sbv_draft_circular_replace_22]
status: stable
last_updated: 2026-09-26
---

Tỷ lệ đòn bẩy (Leverage Ratio - LEV) là chuẩn mực an toàn vĩ mô then chốt thuộc Trụ cột 1 của khung thỏa ước Basel III, được Ngân hàng Nhà nước nội luật hóa nhằm thiết lập một chốt chặn tối hậu độc lập hoàn toàn với việc tính toán trọng số rủi ro (non-risk-based backstop), qua đó ngăn ngừa sự tích tụ đòn bẩy tài chính quá mức trên toàn hệ thống và loại trừ nguy cơ các tổ chức tín dụng tối ưu hóa mô hình rủi ro (risk-weight gaming) để giảm mức vốn yêu cầu luật định (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 8, d.264–286; Phụ lục III, d.1909–1978).

**1. Công thức xác định Tỷ lệ đòn bẩy (LEV) và ngưỡng tối thiểu bắt buộc**

Theo quy định, ngân hàng thương mại và chi nhánh ngân hàng nước ngoài phải duy trì tỷ lệ đòn bẩy riêng lẻ tối thiểu là **3%** theo công thức định lượng (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 8.1–8.2, d.266–275):

$$LEV = \frac{T_1}{EM} \times 100\% \ge 3\%$$

Trong đó:
- $T_1$: Quy mô Vốn cấp 1 (Tier 1 Capital) được xác định chuẩn xác theo quy định tại [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]] (bao gồm Vốn lõi cấp 1 CET1 và Vốn cấp 1 bổ sung AT1 sau khi trừ các khoản giảm trừ bắt buộc).
- $EM$ (Exposure Measure): Tổng trạng thái rủi ro của toàn bộ bảng cân đối tài chính, đo lường quy mô tuyệt đối của ngân hàng mà không áp dụng bất kỳ hệ số trọng số rủi ro (Risk Weight - RW) nào.

**2. Phương pháp xác định Tổng trạng thái rủi ro (Exposure Measure - EM)**

Khác với mẫu số RWA trong tỷ lệ an toàn vốn CAR (vốn nhân chia theo mức độ rủi ro đối tác và tài sản bảo đảm), tổng trạng thái rủi ro $EM$ bao quát toàn bộ tài sản nội bảng, phơi nhiễm phái sinh và cam kết ngoại bảng theo nguyên tắc đo lường thận trọng của Phụ lục III và được phân tích chi tiết tại [[leverage-ratio-exposure-measure-aggregates-on-balance-derivatives-and-off-balance-commitments]] (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục III.I–II, d.1915–1978):
- **Tài sản có nội bảng ($E_{OnB}$)**: Tính toán dựa trên toàn bộ tài sản ghi nhận trên Báo cáo tình hình hoạt động (bao gồm cả tài sản đã chuyển giao quyền sở hữu với mục đích thế chấp trong phái sinh và tài trợ chứng khoán, tài sản ủy thác chịu rủi ro và cho thuê tài chính). Giá trị nội bảng được khấu trừ khoản dự phòng cụ thể và 80% dự phòng chung theo phương pháp tiêu chuẩn: $E_{OnB} = E_{OnB}^* - 80\% \times \text{Dự phòng chung}$. Các khoản mục đã khấu trừ khỏi Vốn cấp 1 sẽ không bị tính trùng vào $EM$. Cơ chế hạch toán gộp tiền mặt (Cash pooling) chỉ được ghi nhận số dư bù trừ ròng trên tài khoản chung khi đáp ứng đầy đủ điều kiện pháp lý nghiêm ngặt không phát sinh rủi ro tài chính riêng lẻ (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục III.II.1, d.1928–1945).
- **Giao dịch sản phẩm phái sinh (Derivative Exposures)**: Áp dụng hệ số khuếch đại 1,4 đối với tổng của chi phí thay thế hiện hành ($RC$) và giá trị phơi nhiễm tương lai tiềm năng ($PFE$) tương thích với chuẩn mực SA-CCR:
  $$\text{Trạng thái phái sinh}_i = 1{,}4 \times (RC_i + PFE_i)$$
  Trong đó chi phí thay thế $RC_i = \max(0, V_i - CVM_{r} + CVM_{p})$ được điều chỉnh theo giá trị ký quỹ biến động bằng tiền mặt (Cash Variation Margin - CVM) đáp ứng điều kiện thanh toán trước khi đáo hạn, kết hợp cơ chế bù trừ song phương Netting theo [[counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure]] (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục III.II.2, d.1946–1969).
- **Cam kết ngoại bảng (Off-Balance Sheet Commitments)**: Chuyển đổi thành trạng thái tương đương nội bảng thông qua hệ số chuyển đổi CCF chuẩn hóa theo [[regulatory-credit-conversion-factors-apportion-off-balance-sheet-contingent-liabilities]]: $\text{Trạng thái ngoại bảng}_i = E_{off,i} \times CCF_i$ (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục III.II.3, d.1970–1978).

**3. Cơ chế hạn chế phân chia cổ tức tiền mặt đối với Ngân hàng có tầm quan trọng hệ thống (D-SIB)**

Nhằm tăng cường năng lực tự hấp thụ tổn thất của các định chế tài chính quy mô lớn, Thông tư đặt ra điều kiện tiên quyết nghiêm ngặt đối với ngân hàng có tầm quan trọng hệ thống (Domestic Systemically Important Banks - D-SIB). Ngân hàng D-SIB chỉ được phép phân chia lợi nhuận bằng tiền mặt cho cổ đông khi duy trì đồng thời cả hai ngưỡng đệm an toàn vốn và đòn bẩy (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 8.3, d.280–284):
1. **Tỷ lệ vốn lõi cấp 1 (CET1)**: Tối thiểu đạt $7\% + \text{Tỷ lệ bộ đệm vốn D-SIB}$ (trong đó 7% bao gồm 4,5% CET1 tối thiểu và 2,5% đệm bảo toàn vốn CCB);
2. **Tỷ lệ đòn bẩy (LEV) riêng lẻ**: Tối thiểu đạt $3\% + 50\% \times \text{Tỷ lệ bộ đệm vốn D-SIB}$.

Quy định này ràng buộc trực tiếp chính sách chi trả cổ tức với kỷ luật duy trì đòn bẩy, buộc các ngân hàng lớn phải tích lũy lợi nhuận giữ lại để củng cố tầng vốn chủ sở hữu khi bảng cân đối mở rộng nhanh.

**4. Ý nghĩa điều tiết vĩ mô và sự bổ trợ với tỷ lệ an toàn vốn (CAR)**

Trong cấu trúc giám sát ngân hàng, tỷ lệ an toàn vốn (CAR) theo [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]] và [[basel-output-floor-and-coverage-ratios-constrain-irb-capital-reductions]] phụ thuộc chặt chẽ vào mức độ nhạy cảm rủi ro của từng loại tài sản. Tuy nhiên, trong các giai đoạn kinh tế tăng trưởng nóng, các tài sản có rủi ro thấp (như trái phiếu chính phủ hoặc cho vay thế chấp nhà ở có LTV thấp) có thể được tích lũy với quy mô khổng lồ mà không đòi hỏi nhiều vốn tự có theo CAR. Khi thị trường đảo chiều hoặc phát sinh rủi ro lãi suất/thanh khoản cực đoan (như bài học từ sự sụp đổ của ngân hàng SVB), tỷ lệ đòn bẩy $LEV$ phát huy vai trò như một mỏ neo giới hạn quy mô tài sản gộp tối đa không quá 33,3 lần vốn Cấp 1 ($1 / 3\%$). Sự kết hợp giữa tỷ lệ an toàn vốn CAR (nhạy cảm rủi ro), tỷ lệ đòn bẩy LEV (chốt chặn quy mô tuyệt đối), tỷ lệ thanh khoản LCR/NSFR và tỷ lệ dư nợ trên huy động [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]] tạo thành mạng lưới an toàn vĩ mô toàn diện cho hệ thống ngân hàng thương mại Việt Nam.

Xem thêm: [[leverage-ratio-exposure-measure-aggregates-on-balance-derivatives-and-off-balance-commitments]], [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]], [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]], [[counterparty-credit-risk-framework-measures-derivative-replacement-cost-and-potential-future-exposure]], [[regulatory-credit-conversion-factors-apportion-off-balance-sheet-contingent-liabilities]], [[basel-output-floor-and-coverage-ratios-constrain-irb-capital-reductions]], [[icaap-framework-determines-economic-capital-and-target-capital-under-stress]].
