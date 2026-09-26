---
title: f-irb-credit-risk-mitigation-framework-and-purchased-receivables-capital-treatment
type: concept
tags: [an-toan-von, sbv, basel-iii, irb, credit-risk-mitigation]
sources: [sbv_circular_14_2025]
status: draft
last_updated: 2026-09-26
---

Phương pháp xếp hạng nội bộ cơ bản (Foundation Internal Ratings-Based - F-IRB) theo Thông tư 14/2025/TT-NHNN phân định rạch ròi trách nhiệm lượng hóa giữa tổ chức tín dụng và cơ quan quản lý: ngân hàng tự ước tính tham số xác suất vỡ nợ (PD), trong khi các tham số tỷ lệ tổn thất khi vỡ nợ (LGD), giá trị chịu rủi ro tại thời điểm vỡ nợ (EAD) và kỳ hạn hiệu lực (M) được tính toán theo các thuật toán và tham số chuẩn tắc do Ngân hàng Nhà nước ấn định để xác định tài sản có rủi ro tín dụng khách hàng $RWA_{CR}$ (sbv_circular_14_2025, file TT14_1.md, Điều 30, d.805–820).

Kỹ thuật phân bổ LGD cho danh mục tài sản bảo đảm (TSBĐ) đa dạng trong F-IRB được vận hành qua thuật toán bóc tách giá trị phơi nhiễm thành phần bảo đảm và phần không bảo đảm:
- Tổng số dư phơi nhiễm sau bảo lãnh và phái sinh tín dụng được xác định là $E = \text{Dư nợ} - G^* - CD^*$, trong đó phần số dư được bảo đảm bằng TSBĐ thứ $i$ sau hiệu chỉnh là $E_{Si} = C_i^*$ với điều kiện ràng buộc tổng $\sum E_{Si} \le E$, và phần phơi nhiễm không bảo đảm còn lại là $E_u = E - \sum E_{Si}$ (sbv_circular_14_2025, file TT14_1.md, Điều 44, d.1071–1114).
- Tham số LGD bình quân gia quyền của toàn bộ khoản nợ được tổng hợp theo công thức:
  $$LGD^* = \sum_{i} \left(\frac{E_{Si}}{E} \times LGD_{Si}\right) + \frac{E_u}{E} \times LGD_u$$
  trong đó $LGD_u$ là LGD áp dụng cho phần nợ không bảo đảm ($LGD_u = 45\%$ cho khoản nợ doanh nghiệp cao cấp không bảo đảm; $LGD_u = 75\%$ cho khoản nợ thứ cấp), còn $LGD_{Si}$ và hệ số hiệu chỉnh $H_{Ci}$ được phân tầng theo 3 nhóm TSBĐ đủ điều kiện:
  + TSBĐ tài chính chuẩn (tiền mặt, vàng, trái phiếu chính phủ): $LGD_{Si} = 0\%$, hệ số hiệu chỉnh $H_c$ xác định theo phương pháp tiêu chuẩn.
  + TSBĐ bất động sản đủ tiêu chuẩn: $LGD_{Si} = 20\%$, hệ số hiệu chỉnh $H_{Ci} = 40\%$.
  + TSBĐ hữu hình khác (máy móc, thiết bị, nguyên vật liệu, thành phẩm, hàng tồn kho có thị trường giao dịch): $LGD_{Si} = 25\%$, hệ số hiệu chỉnh $H_{Ci} = 50\%$ (sbv_circular_14_2025, file TT14_1.md, Điều 44, d.1071–1114).
- Giá trị TSBĐ thứ $i$ được ghi nhận sau hiệu chỉnh ($C_i^*$) tích hợp chiết khấu chênh lệch tiền tệ và khấu trừ không khớp kỳ hạn:
  $$C_i^* = C_i \times (1 - H_{Ci} - H_{fxci}) \times \frac{t_i - 0{,}25}{T - 0{,}25}$$
  với hệ số hiệu chỉnh độ lệch tiền tệ cố định $H_{fxci} = 8\%$; thời hạn hiệu lực khoản vay $T = \min(5\text{ năm}, \text{thời hạn còn lại của khoản nợ tính theo năm})$; thời hạn hiệu lực TSBĐ $t_i = \min(T, \text{thời hạn còn lại của TSBĐ})$; và nếu $t_i \le 0{,}25$ năm (dưới 3 tháng) thì TSBĐ bị loại bỏ hoàn toàn ($C_i^* = 0$) (sbv_circular_14_2025, file TT14_1.md, Điều 44, d.1071–1114).

Kỹ thuật thay thế tham số (Substitution Approach) đối với bảo lãnh của bên thứ ba và sản phẩm phái sinh tín dụng (CDS) cho phép chuyển giao mức độ rủi ro của bên vay sang bên bảo lãnh hoặc bên bán bảo hiểm:
- Điều kiện tiên quyết: bên bảo lãnh hoặc bên phát hành phái sinh tín dụng phải có tham số $PD_{\text{guarantor}} < PD_{\text{borrower}}$; trường hợp đối tác bảo lãnh không áp dụng IRB, ngân hàng được quyền chuyển phần được bảo lãnh sang tính theo phương pháp tiêu chuẩn [[standardized-credit-risk-weights-and-asset-classification-hierarchy-govern-regulatory-capital]] hoặc giữ nguyên IRB nhưng không được giảm thiểu rủi ro (sbv_circular_14_2025, file TT14_1.md, Điều 45, d.1115–1145) (sbv_circular_14_2025, file TT14_1.md, Điều 46, d.1146–1170).
- Phân rã tham số rủi ro: phần giá trị khoản nợ được bảo lãnh sau hiệu chỉnh ($G_l^*$ hoặc $CD_n^*$) được áp dụng cặp tham số $PD, LGD$ của bên bảo lãnh/bên bán phái sinh; đặc biệt, nếu bên bảo lãnh có sử dụng TSBĐ hợp lệ thì được phép áp dụng $LGD_{Si}$ của TSBĐ đó (20% cho BĐS, 25% cho thiết bị hàng tồn kho) thay cho LGD của bên bảo lãnh; phần giá trị nợ còn lại giữ nguyên tham số của bên vay (sbv_circular_14_2025, file TT14_1.md, Điều 45, d.1115–1145).
- Công thức giá trị bảo lãnh và phái sinh tín dụng sau hiệu chỉnh áp dụng chiết khấu lệch tiền tệ $H_{fx} = 8\%$ và chiết khấu chênh lệch kỳ hạn tương tự như TSBĐ (sbv_circular_14_2025, file TT14_1.md, Điều 45, d.1115–1145) (sbv_circular_14_2025, file TT14_1.md, Điều 46, d.1146–1170); cơ chế này cũng được mở rộng cho danh mục bán lẻ nhằm giảm thiểu rủi ro qua bảo lãnh bên thứ ba (sbv_circular_14_2025, file TT14_1.md, Điều 52, d.1297–1313).

Quy chuẩn đo lường EAD và M của khoản nợ doanh nghiệp khống chế dư địa tùy biến tham số của ngân hàng:
- Giá trị chịu rủi ro tại thời điểm vỡ nợ (EAD) tích hợp bù trừ số dư tiền gửi nội bảng:
  $$EAD = \max(0, EAD_{\text{on}} - L \times (1 - H_{fxl})) + EAD_{\text{off}} \times CCF$$
  trong đó $L$ là số dư nợ phải trả nội bảng đủ điều kiện bù trừ, và hệ số chuyển đổi cam kết ngoại bảng CCF áp dụng theo Điều 10 của phương pháp chuẩn hóa (sbv_circular_14_2025, file TT14_1.md, Điều 47, d.1171–1187).
- Tham số kỳ hạn hiệu lực M của khoản phải đòi doanh nghiệp trong F-IRB được ấn định mặc định cố định $M = 2{,}5\text{ năm}$ để đưa vào hàm tính RWA theo [[asymptotic-single-risk-factor-model-derives-corporate-irb-risk-weighted-assets]] (sbv_circular_14_2025, file TT14_1.md, Điều 48, d.1188–1193).
- Ngược lại, đối với danh mục bán lẻ trong A-IRB theo [[retail-irb-portfolio-risk-weights-calibrate-mortgage-revolving-and-other-retail-correlations]], ngân hàng phải tự ước tính EAD theo từng phân khúc nhóm đồng nhất dựa trên chuỗi dữ liệu tham chiếu tối thiểu 5 năm liên tục, kiểm soát các điều kiện rút thêm hạn mức khi khách hàng suy giảm chất lượng tín dụng (sbv_circular_14_2025, file TT14_1.md, Điều 53, d.1314–1335).

Khuôn khổ vốn đối với Khoản mua lại khoản phải thu (Purchased Receivables) thiết lập cấu trúc tính toán hai thành phần rủi ro độc lập (sbv_circular_14_2025, file TT14_1.md, Điều 54, d.1336–1351):
$$RWA_{PR} = RWA_{DfR} + RWA_{DR}$$
trong đó:
- Cấu phần Rủi ro vỡ nợ (Default Risk - $RWA_{DfR}$): đo lường nguy cơ bên có nghĩa vụ thanh toán khoản phải thu không thể thực hiện nghĩa vụ; đối với khoản mua lại khoản phải thu doanh nghiệp, ngân hàng áp dụng quy trình F-IRB với PD ước tính, $LGD = 45\%$ và $M = 2{,}5\text{ năm}$; đối với bán lẻ, ngân hàng ước tính PD, LGD, EAD theo nhóm gộp và phải loại bỏ mọi giả định về quyền truy đòi hoặc bảo lãnh từ bên bán (sbv_circular_14_2025, file TT14_1.md, Điều 55, d.1352–1356) (sbv_circular_14_2025, file TT14_1.md, Điều 56, d.1357–1362).
- Cấu phần Rủi ro giảm giá trị (Dilution Risk - $RWA_{DR}$): đo lường nguy cơ số dư khoản phải thu bị sụt giảm theo các thỏa thuận thương mại ngầm định hoặc công khai giữa bên bán và người mua (như trả lại hàng lỗi, tranh chấp chất lượng sản phẩm, chiết khấu thanh toán sớm); rủi ro này chỉ được miễn trừ khi hợp đồng cơ sở không có thỏa thuận giảm giá trị hoặc thời hạn thỏa thuận đã kết thúc trước thời điểm mua lại (sbv_circular_14_2025, file TT14_1.md, Điều 57, d.1363–1371).
- Tham số chuẩn hóa bắt buộc cho Dilution Risk: tỷ lệ tổn thất dự kiến trong vòng 1 năm ($EL_{DR}$) được gán trực tiếp làm tham số xác suất $PD_{DR} = EL_{DR}$; tham số tổn thất ấn định tuyệt đối $LGD_{DR} = 100\%$ do toàn bộ giá trị tranh chấp/chiết khấu thương mại bị xóa bỏ hoàn toàn khỏi nghĩa vụ thanh toán; kỳ hạn ấn định $M = 2{,}5\text{ năm}$ (hoặc rút xuống 1 năm nếu khoản phải thu được thanh lý dứt điểm trong 1 năm); giá trị RWA được tính bằng cách đưa các tham số này vào hàm ASRF Doanh nghiệp (sbv_circular_14_2025, file TT14_1.md, Điều 58, d.1372–1383).
- Biện pháp giảm thiểu rủi ro cho Purchased Receivables: cho phép ngân hàng sử dụng bảo lãnh bên thứ ba hoặc CDS để phòng ngừa riêng biệt cho Default Risk, hoặc riêng biệt cho Dilution Risk, hoặc cả hai thông qua cơ chế thay thế tham số tương ứng (sbv_circular_14_2025, file TT14_1.md, Điều 59, d.1384–1391).

Toàn bộ hệ thống kỹ thuật đo lường và giảm thiểu rủi ro này phụ thuộc trực tiếp vào tính chuẩn mực của kiến trúc mô hình và quy trình kiểm định được điều chỉnh bởi [[irb-system-design-operational-standards-and-pillar-3-disclosures]].
