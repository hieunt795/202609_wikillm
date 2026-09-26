---
title: contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement
type: concept
tags: [banking, alm, liquidity-risk, lcr, cash-inflows, inflow-cap, reverse-repo, counterparty-haircuts, net-cash-outflows, regulation]
sources: [sbv_draft_circular_replace_22]
status: draft
last_updated: 2026-09-26
---

Quy tắc đo lường dòng tiền vào theo hợp đồng và chốt chặn trần thu hồi vốn theo Phụ lục I của Dự thảo Thông tư thay thế Thông tư 22/2019/TT-NHNN thiết lập các nguyên tắc thận trọng nhằm ngăn ngừa việc tổ chức tín dụng phóng đại khả năng thu hồi vốn để làm giảm mẫu số dòng tiền ra ròng trong tỷ lệ [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]]. Bằng cách áp dụng các hệ số thu tiền (inflow rates) có chiết khấu theo loại đối tác, loại trừ hoàn toàn các nguồn thu mang tính điều kiện và áp đặt trần khống chế dòng tiền vào tối đa không quá 75% tổng dòng tiền ra dự kiến, quy chuẩn bảo đảm ngân hàng luôn duy trì một lượng đệm HQLA tự thân tối thiểu để phòng thủ độc lập trước các cú sốc thanh khoản (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần C, d.1496–1617).

**1. Nguyên tắc ghi nhận dòng tiền vào dự kiến (Phần C.I)**

Dòng tiền vào chỉ được ghi nhận từ các quyền đòi hợp đồng hợp pháp (bao gồm cả gốc, lãi và phí đến hạn) phát sinh trong khoảng thời gian 30 ngày tiếp theo (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần C.I, d.1498–1509):
- **Điều kiện loại trừ nợ xấu**: Chỉ ghi nhận các khoản phải thu còn trong hạn từ các khách hàng không thuộc diện vỡ nợ theo quy định về an toàn vốn của [[standardized-approach-credit-risk-weights-and-exposure-measurement-govern-regulatory-rwa]]. Các khoản nợ xấu hoặc nợ quá hạn bị loại bỏ hoàn toàn khỏi dòng tiền vào;
- **Cấm ghi nhận dòng tiền vào mang tính điều kiện (Contingent Inflows)**: Các khoản hạn mức tín dụng hoặc hạn mức thanh khoản mà ngân hàng được cấp bởi Ngân hàng Nhà nước, ngân hàng mẹ hoặc các tổ chức tín dụng khác nhưng chưa rút vốn **bắt buộc phải áp dụng hệ số thu tiền 0%** (Mục III, d.1535). Quy tắc này triệt tiêu giả định sai lầm rằng ngân hàng có thể dựa vào việc đi vay ngân hàng bạn khi toàn bộ thị trường đang khủng hoảng thanh khoản;
- **Nguyên tắc không tính trùng lặp với HQLA**: Các chứng khoán hoặc tài sản sinh lời đã được tính vào danh mục HQLA Cấp 1, Cấp 2A hoặc Cấp 2B của [[hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers]] thì dòng tiền thu hồi gốc lãi liên quan không được ghi nhận vào dòng tiền vào;
- **Khoản vay không xác định kỳ hạn**: Các khoản cho vay không có kỳ hạn cố định hoặc hạn mức tín dụng quay vòng không được tính vào dòng tiền vào, trừ phần nghĩa vụ thanh toán tối thiểu theo hợp đồng trong 30 ngày (như khoản thanh toán tối thiểu của thẻ tín dụng).

**2. Dòng tiền vào từ Cho vay có bảo đảm và Hợp đồng mua lại đảo ngược (Reverse Repo — Mục II)**

Đối với các khoản cho vay có bảo đảm và giao dịch Reverse Repo đáo hạn trong vòng 30 ngày, hệ số thu tiền được thiết kế đối xứng với hệ số chiết khấu haircut của tài sản bảo đảm mà ngân hàng đang nắm giữ (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần C.II, d.1510–1532):

| Tài sản bảo đảm nhận từ giao dịch Reverse Repo / Cho vay | Hệ số thu tiền | Lý do kinh tế |
|---|---|---|
| Tài sản Cấp 1 (TPCP, Tín phiếu NHNN) | **0%** | Ngân hàng được giả định sẽ tiếp tục tái ký (rollover) giao dịch để duy trì việc nắm giữ tài sản Cấp 1 hoặc phải hoàn trả tài sản khi đối tác thanh toán |
| Tài sản Cấp 2A (TPCP RW 20%, TPDN hạng AA-) | **15%** | Thu tiền bằng đúng mức chiết khấu 15% của tài sản Cấp 2A |
| Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS Cấp 2B) | **25%** | Thu tiền bằng đúng mức chiết khấu 25% của RMBS |
| Tài sản Cấp 2B khác (TPDN BBB-, Cổ phiếu bluechip) | **50%** | Thu tiền bằng đúng mức chiết khấu 50% |
| Cho vay ký quỹ chứng khoán (Margin loans) | **50%** | Giả định ngân hàng chỉ thu hồi được 50% số dư nợ cho vay margin khi thị trường chứng khoán giảm mạnh |
| Tài sản tài chính khác không thuộc HQLA | **100%** | Ngân hàng thu hồi toàn bộ 100% tiền mặt và trả lại tài sản kém thanh khoản cho đối tác |

**3. Dòng tiền vào theo phân loại đối tác giao dịch (Mục IV)**

Đối với các khoản cấp tín dụng không có bảo đảm hoặc có bảo đảm bằng tài sản phi tài chính (bất động sản, máy móc), hệ số thu tiền phản ánh áp lực kinh doanh và năng lực trả nợ của từng nhóm đối tác (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Phụ lục I Phần C.IV, d.1537–1572):
- **Khách hàng cá nhân và Doanh nghiệp nhỏ và vừa (SME) — Hệ số thu tiền 50%**: Giả định rằng trong điều kiện bình thường cũng như căng thẳng, để duy trì mối quan hệ kinh doanh và tránh đẩy người vay vào tình trạng kiệt quệ tài chính, ngân hàng bắt buộc phải giải ngân tái tài trợ (rollover) ít nhất 50% dư nợ đến hạn, nên chỉ thực thu ròng 50%;
- **Doanh nghiệp lớn phi tài chính, Chính phủ, PSEs và MDBs — Hệ số thu tiền 50%**: Tương tự, ngân hàng chỉ được tính thu tiền tối đa 50% dư nợ nợ gốc và lãi đến hạn từ các tập đoàn lớn;
- **Các tổ chức tài chính và Ngân hàng Nhà nước — Hệ số thu tiền 100%**: Các khoản tiền gửi liên ngân hàng có kỳ hạn đến hạn hoặc các khoản cho vay liên ngân hàng Thị trường 2 được ghi nhận thu hồi 100% tiền mặt;
- **Tiền gửi hoạt động đặt tại ngân hàng khác**: Áp dụng hệ số thu tiền **0%** (vì ngân hàng bắt buộc phải duy trì số dư này để tiếp tục dịch vụ thanh toán bù trừ, lưu ký của chính mình). Chỉ phần số dư vượt mức hoạt động thực tế có thể rút tự do mới được ghi nhận thu tiền 100%;
- **Dòng tiền vào từ phái sinh**: Ghi nhận 100% dòng tiền vào ròng theo thỏa thuận bù trừ Master Netting Agreement (Mục V, d.1575).

**4. Chốt chặn Trần khống chế Dòng tiền vào 75% (The 75% Inflow Cap)**

Chốt chặn có ý nghĩa điều tiết an toàn vĩ mô quan trọng nhất trong công thức đo lường dòng tiền ra ròng là việc giới hạn tổng dòng tiền vào không được vượt quá **75% tổng dòng tiền ra dự kiến** (sbv_draft_circular_replace_22, file 10_DTTT_thay_the_Thong_tu_22_260421_37a8.md, Điều 21.2, d.568–573; Phụ lục I Phần C, d.1616):

$$\text{Dòng tiền vào được công nhận} = \min\left(\text{Tổng dòng tiền vào dự kiến},\ 75\% \times \text{Tổng dòng tiền ra dự kiến}\right)$$

Do đó, mẫu số của tỷ lệ LCR luôn thỏa mãn:
$$\text{Dòng tiền ra ròng} = \text{Dòng tiền ra dự kiến} - \text{Dòng tiền vào được công nhận} \ge 25\% \times \text{Dòng tiền ra dự kiến}$$

**Ý nghĩa quản trị rủi ro thanh khoản**:
- Chốt chặn 75% ngăn ngừa tuyệt đối chiến lược "khớp kỳ hạn hoàn hảo trên giấy" (matched-maturity game), trong đó một ngân hàng có thể bố trí lịch thu nợ tín dụng trùng khít 100% với lịch trả tiền gửi nhằm đưa dòng tiền ra ròng về bằng 0 để không phải nắm giữ bất kỳ tài sản HQLA nào;
- Trong một cuộc hoảng loạn thanh khoản thực tế, dòng tiền vào theo hợp đồng rất dễ bị đình trệ do khách hàng chậm trả nợ hoặc phá sản dây chuyền. Trần khống chế 75% buộc mọi ngân hàng thương mại bất kể quy mô **phải luôn luôn tự trang bị một lượng HQLA tối thiểu bằng 25% tổng dòng tiền ra dự kiến**, tạo đệm an toàn tự phòng hộ độc lập không phụ thuộc vào hành vi trả nợ của bên ngoài;
- Quy chuẩn này tạo ra mối gắn kết chặt chẽ với quy tắc định giá chi phí cơ hội vốn trên đường cong FTP tại [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]] và khuôn khổ quản trị thanh khoản nội bộ tại [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]].

Xem thêm: [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[hqla-eligibility-and-unwinding-haircut-mechanics-calibrate-liquidity-buffers]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments]], [[regulatory-lcr-and-nsfr-constraints-impose-marginal-funding-costs-on-ftp]], [[liquidity-risk-management-framework-mandates-cash-flow-gaps-and-contingency-funding-plans]], [[loan-to-deposit-ratio-ldr-regulates-structural-banking-leverage-and-funding-capacity]].
