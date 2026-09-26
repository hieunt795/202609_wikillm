---
title: icaap-framework-determines-economic-capital-and-target-capital-under-stress
type: concept
tags: [banking, icaap, economic-capital, target-capital, stress-testing, pillar-2, raroc, regulation, basel, principles]
sources: [sbv_circular_83_2025, bcbs_144, bcbs_368]
status: stable
last_updated: 2026-09-26
---

Quy trình đánh giá nội bộ về mức đủ vốn (Internal Capital Adequacy Assessment Process - ICAAP) là cấu phần trung tâm của Trụ cột 2 Basel, yêu cầu ngân hàng thương mại phải chủ động lượng hóa toàn diện các rủi ro trọng yếu trong cả điều kiện hoạt động bình thường và kịch bản có diễn biến bất lợi (stress scenario), từ đó xác định vốn kinh tế (Economic Capital - $C_E$), vốn mục tiêu (Target Capital - $C_{Target}$), đối chiếu với vốn tự có dự kiến ($C_A$) trong tầm nhìn chiến lược 3 đến 5 năm nhằm đảm bảo tính bền vững của bảng cân đối kế toán (sbv_circular_83_2025, file TT83.md, Điều 59–63, d.996–1063; Phụ lục III, d.1423–1519; Phụ lục VI, d.1845–1928).

**1. Khung thời gian và quy trình sáu bước thực hiện ICAAP**

Ngân hàng phải thực hiện đánh giá nội bộ mức đủ vốn định kỳ tối thiểu hằng năm hoặc đột xuất (khi môi trường vĩ mô hoặc chiến lược kinh doanh có biến động lớn làm suy giảm an toàn vốn) cho chu kỳ tối thiểu 3 năm nhưng không quá 5 năm tiếp theo thông qua 6 bước tuần tự (sbv_circular_83_2025, file TT83.md, Điều 59.2, d.1004–1011):
- Bước 1: Đo lường rủi ro đối với tất cả các loại rủi ro trọng yếu và xác định tổng tài sản tính theo rủi ro trong kịch bản bình thường ($RWA_E^*$) cùng vốn kinh tế tương ứng theo kế hoạch kinh doanh.
- Bước 2: Kiểm tra sức chịu đựng về vốn (Capital Stress Testing) theo [[sound-stress-testing-governance-mandates-board-involvement-and-actionable-integration]] và [[firm-wide-stress-testing-integrates-multi-risk-dimensions-and-concentration-risk]] để xác định tổng tài sản tính theo rủi ro trong kịch bản có diễn biến bất lợi và lượng hóa mức tăng tài sản rủi ro ($\Delta RWA_B$).
- Bước 3: Xác định mức vốn mục tiêu ($C_{Target}$) và dự phóng quy mô vốn tự có dự kiến ($C_A$).
- Bước 4: Lập kế hoạch vốn (Capital Planning) bao gồm phương án phân bổ vốn, chính sách cổ tức và phương án dự phòng tăng vốn.
- Bước 5: Giám sát liên tục mức đủ vốn, thiết lập ngưỡng cảnh báo sớm và điều chỉnh kế hoạch vốn khi phát sinh độ lệch.
- Bước 6: Rà soát độc lập toàn diện quy trình đánh giá nội bộ về mức đủ vốn.

**2. Công thức xác định Vốn kinh tế ($C_E$) và các cấu phần RWA trọng yếu**

Theo chuẩn mực Phụ lục VI Thông tư 83, Vốn kinh tế ($C_E$) không chỉ bù đắp các rủi ro luật định thuộc Trụ cột 1 mà còn tích hợp phần vốn đệm dự phòng cho kịch bản căng thẳng bất lợi (sbv_circular_83_2025, file TT83.md, Phụ lục VI.I.1, d.1853–1862):

$$C_E = RWA_E^* \times CAR_{Target} + \Delta RWA_B \times CAR_R$$

Trong đó:
- $CAR_{Target}$: Tỷ lệ an toàn vốn mục tiêu do Hội đồng quản trị xác định trong [[risk-appetite-framework-and-capital-targets-anchor-multi-year-risk-strategy]] (luôn cao hơn sàn luật định).
- $CAR_R$: Tỷ lệ an toàn vốn tối thiểu theo quy định của Ngân hàng Nhà nước (hiện hành tối thiểu 8% theo [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]]).
- $\Delta RWA_B$: Giá trị chênh lệch dương giữa Tổng tài sản tính theo rủi ro trong kịch bản có diễn biến bất lợi ($RWA_{Adverse}$) và kịch bản bình thường ($RWA_{Normal}$): $\Delta RWA_B = \max(0, RWA_{Adverse} - RWA_{Normal})$.
- $RWA_E^*$: Tổng tài sản tính theo rủi ro trong kịch bản hoạt động bình thường, bao quát toàn diện 6 cấu phần rủi ro trọng yếu (sbv_circular_83_2025, file TT83.md, Phụ lục VI.I.1.d, d.1866–1877):

$$RWA_E^* = RWA_{CR} + RWA_{OR} + RWA_{MR} + RWA_{IRRBB} + RWA_{COR} + RWA_{OMR}$$

Các cấu phần rủi ro được định nghĩa kỹ thuật như sau:
- $RWA_{CR}$: Tổng tài sản tính theo rủi ro tín dụng theo chuẩn mực luật định của NHNN (phương pháp chuẩn hóa SA hoặc phương pháp IRB).
- $RWA_{OR}, RWA_{MR}$: Vốn yêu cầu quy đổi của rủi ro hoạt động và rủi ro thị trường (vốn yêu cầu nhân nghịch đảo hệ số 12,5).
- $RWA_{IRRBB}$: Tổng tài sản rủi ro từ rủi ro lãi suất trên sổ ngân hàng do ngân hàng tự mô hình hóa; theo Chuẩn mực BCBS 368 (Nguyên tắc 9) và [[irrbb-capital-allocation-framework-differentiates-economic-capital-from-earnings-buffers]], việc phân bổ vốn nội bộ cho IRRBB bắt buộc phải kết hợp song trùng: dự phòng vốn kinh tế để bù đắp rủi ro suy giảm giá trị kinh tế ($\Delta EVE$) và thiết lập đệm vốn (capital buffer) cho rủi ro suy giảm thu nhập lãi thuần ($\Delta NII$), đồng thời phải tính đến chín nhân tố bắt buộc bao gồm chi phí phòng hộ, lỗ ngầm định (embedded losses) và rủi ro phân bổ vốn giữa các thực thể pháp lý thành viên; chậm nhất từ ngày 01/01/2028 tại Việt Nam bắt buộc phải tính toán dựa trên mức suy giảm giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) theo hướng dẫn chi tiết tại [[irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios]] (bcbs_368, file d368.md, Principle 9, d.405–426; sbv_circular_83_2025, file TT83.md, Phụ lục VI.I.1.iv, d.1906).
- $RWA_{OMR}$: Tổng tài sản tính theo các rủi ro trọng yếu khác do ngân hàng tự nhận dạng (như rủi ro chiến lược, rủi ro danh tiếng, rủi ro pháp lý/tuân thủ); lưu ý rủi ro thanh khoản được kiểm soát qua khe hở dòng tiền và kế hoạch dự phòng (CFP) nên không quy đổi thành RWA trong công thức vốn kinh tế.
- $RWA_{COR}$: Tổng tài sản tính theo rủi ro tập trung, bao gồm tập trung tín dụng ($RWA1_{COR}$) và tập trung danh mục tự doanh ($RWA2_{COR}$). Trong đó, mức rủi ro tập trung tín dụng không được thấp hơn sàn chuẩn hóa kỹ thuật $RWA1^*_{COR}$ (sbv_circular_83_2025, file TT83.md, Phụ lục VI.I.1.iii, d.1882–1905):

$$RWA1^*_{COR} = 12{,}5 \times \left( \sum \max(0, E_i - A \times C) + \sum \max(0, E_j - B \times C) \right)$$

Với $E_i$ là tổng dư nợ cấp tín dụng đối với một khách hàng (không gồm khoản có trọng số rủi ro 0% hoặc đã giảm trừ vốn); $E_j$ là dư nợ đối với một khách hàng và người có liên quan; $C$ là vốn tự có. Các tỷ lệ trần vốn tự có tương ứng $A$ và $B$ siết chặt dần theo lộ trình chuyển tiếp:
- Từ 01/07/2026: $A = 8{,}7\%$; $B = 16{,}8\%$.
- Từ 01/01/2027: $A = 8{,}0\%$; $B = 15{,}2\%$.
- Từ 01/01/2028: $A = 7{,}3\%$; $B = 13{,}6\%$.
- Từ 01/01/2029: $A = 6{,}5\%$; $B = 12{,}0\%$.

**3. Xác định Vốn mục tiêu ($C_{Target}$) và Vốn tự có dự kiến ($C_A$)**

Vốn mục tiêu ($C_{Target}$) của ngân hàng là giá trị lớn hơn giữa Vốn luật định ($C_R$) và Vốn kinh tế ($C_E$) (sbv_circular_83_2025, file TT83.md, Phụ lục VI.I.2, d.1908–1916):

$$C_{Target} = \max(C_R, C_E)$$

Trong đó $C_R = RWA \times CAR_R$ là mức vốn tự có tối thiểu bắt buộc để tuân thủ Trụ cột 1. Vốn mục tiêu đóng vai trò là "chân đế vốn" tối thiểu ngân hàng phải duy trì để bảo toàn hoạt động kinh doanh trước các cú sốc vĩ mô.

Vốn tự có dự kiến ($C_A$) là mức vốn tự có nội sinh được xác định trên cơ sở kế hoạch kinh doanh 3 đến 5 năm tới với 4 giả định cơ sở nghiêm ngặt (sbv_circular_83_2025, file TT83.md, Phụ lục VI.II, d.1917–1925):
1. Không tính đến kế hoạch tăng vốn mới từ phát hành cổ phiếu hoặc trái phiếu thứ cấp;
2. Không phát sinh nghĩa vụ bổ sung vốn cho công ty con, công ty liên kết hoặc các khoản đầu tư góp vốn, mua cổ phần;
3. Tỷ lệ chi trả cổ tức giả định bằng tỷ lệ chia cổ tức bình quân thực tế của 3 năm tài chính gần nhất;
4. Toàn bộ phần lợi nhuận sau thuế giữ lại sau khi trích lập các quỹ và chia cổ tức được bổ sung vào vốn tự có.

Định kỳ đối chiếu chênh lệch giữa nguồn vốn dự kiến và nhu cầu vốn mục tiêu: $\Delta C = C_A - C_{Target}$.
- Trường hợp thặng dư ($\Delta C \ge 0$): Ngân hàng đủ năng lực tự tài trợ cho tăng trưởng tài sản rủi ro và được phép thực hiện kế hoạch phân phối lợi nhuận, chia cổ tức.
- Trường hợp thiếu hụt ($\Delta C < 0$): Ngân hàng phải lập tức kích hoạt phương án tăng vốn cụ thể trong kế hoạch vốn (lộ trình huy động vốn Cấp 1, phát hành trái phiếu Cấp 2, giảm tỷ lệ chi trả cổ tức bằng tiền mặt hoặc tái cơ cấu danh mục tài sản rủi ro cao) (sbv_circular_83_2025, file TT83.md, Điều 61.1.a, d.1024–1026).

**4. Phân bổ vốn kinh tế, định giá theo rủi ro (RAROC) và giám sát độc lập**

Kế hoạch vốn do Hội đồng quản trị/Hội đồng thành viên phê duyệt theo đề xuất của Tổng giám đốc. Vốn mục tiêu được phân bổ chi tiết cho từng loại rủi ro trọng yếu để làm cơ sở thiết lập hệ số hạn mức rủi ro danh mục tại [[credit-risk-governance-mandates-portfolio-limits-and-problem-credit-containment]] và cơ chế tính toán định giá chuyển nhượng vốn tại [[ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital]].

Hiệu quả sử dụng vốn trên toàn hàng và từng khối kinh doanh được đo lường thông qua Tỷ suất sinh lời trên vốn có điều chỉnh rủi ro (Risk-Adjusted Return on Capital - RAROC) (sbv_circular_83_2025, file TT83.md, Phụ lục VI.III, d.1926–1928):

$$RAROC = \frac{\text{Lợi nhuận trước thuế}}{C_E}$$

Chỉ tiêu RAROC được đưa vào khẩu vị rủi ro và hệ thống KPI quản trị để gắn kết giữa chi phí vốn kinh tế với quyết định cấp tín dụng và tự doanh tài chính.

**Yêu cầu rà soát độc lập quy trình ICAAP và chế tài vốn thanh khoản SREP**: Quy trình đánh giá nội bộ mức đủ vốn phải được rà soát định kỳ tối thiểu hằng năm hoặc đột xuất bởi một **bộ phận hoàn toàn độc lập** với bộ phận xây dựng và thực thi ICAAP. Nội dung rà soát tập trung vào: tính hợp lý của cấu trúc tổ chức, tính nhất quán giữa khẩu vị rủi ro và kế hoạch kinh doanh, tính đầy đủ và chính xác của dữ liệu đầu vào, tính logic của các giả định kiểm tra sức chịu đựng, tính khả thi của phương án tăng vốn và việc tuân thủ các kiến nghị của cơ quan thanh tra giám sát ngân hàng (sbv_circular_83_2025, file TT83.md, Điều 62, d.1035–1045).

Đáng chú ý, mặc dù rủi ro thanh khoản được quản lý thông qua chênh lệch dòng tiền và kế hoạch dự phòng (CFP) nên không quy đổi thành RWA trong công thức vốn kinh tế, nhưng theo chuẩn mực BCBS 144 Nguyên tắc 16 tại [[supervisory-early-remedial-actions-mandate-liquidity-gap-reductions-and-capital-add-ons]] và quy trình đánh giá giám sát SREP tại [[supervisory-liquidity-review-process-evaluates-governance-stress-testing-and-cushion-adequacy]], cơ quan giám sát có thẩm quyền áp đặt **phụ phí vốn tự có bắt buộc (Supervisory Capital Add-on)** trực tiếp lên $C_{Target}$ nếu ngân hàng bộc lộ khiếm khuyết nghiêm trọng trong quản trị thanh khoản hoặc thiếu hụt đệm HQLA unencumbered (bcbs_144, file bcbs144.md, Principle 16, d.607). Vị thế vốn tự có dồi dàu theo ICAAP chính là chốt chặn niềm tin cốt lõi giúp ngân hàng duy trì năng lực tiếp cận các nguồn tài trợ thanh khoản từ thị trường trong các thời kỳ căng thẳng.

Xem thêm: [[supervisory-early-remedial-actions-mandate-liquidity-gap-reductions-and-capital-add-ons]], [[supervisory-liquidity-review-process-evaluates-governance-stress-testing-and-cushion-adequacy]], [[risk-appetite-framework-and-capital-targets-anchor-multi-year-risk-strategy]], [[three-tier-capital-adequacy-framework-sets-minimum-car-tier-1-and-cet1-thresholds]], [[ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital]], [[credit-risk-governance-mandates-portfolio-limits-and-problem-credit-containment]], [[irrbb-delta-eve-and-nii-standardized-measurement-governs-rate-shock-scenarios]], [[risk-based-internal-audit-framework-enforces-third-line-oversight-and-governance]], [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]].

