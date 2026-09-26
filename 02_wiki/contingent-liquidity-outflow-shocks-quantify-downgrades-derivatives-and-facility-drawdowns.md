---
title: contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns
type: concept
tags: [banking, alm, liquidity-risk, lcr, contingent-outflows, credit-facilities, liquidity-facilities, downgrade-triggers, lookback-approach, derivatives, basel, basel-iii, bcbs-238]
sources: [bcbs_238]
status: stable
last_updated: 2026-09-26
---

Khuôn khổ lượng hóa các cú sốc dòng tiền tiềm tàng từ cam kết ngoại bảng và rủi ro gia tăng (Contingent Liquidity Outflow Shocks) theo chuẩn mực Basel III (BCBS 238) thiết lập hệ thống tham số định lượng chi tiết nhằm mô phỏng các rò rỉ thanh khoản đột ngột phát sinh từ các điều khoản hạ bậc xếp hạng tín nhiệm độc lập (3-notch downgrade), các nghĩa vụ ký quỹ phái sinh theo phương pháp hồi cứu lịch sử 24 tháng, và sự kích hoạt rút vốn ồ ạt từ các hạn mức tín dụng và thanh khoản đã cam kết chưa sử dụng (bcbs_238, file bcbs238.md, Part 1 Section II.B.1.iv, Paragraphs 116–141, d.507–570).

**1. Rủi ro dòng tiền từ các hợp đồng phái sinh và thỏa thuận bù trừ (Derivatives Outflows)**

Trong kịch bản căng thẳng 30 ngày của LCR, dòng tiền ra ròng từ các hợp đồng phái sinh phải chịu hệ số tính toán **100%** (bcbs_238, file bcbs238.md, Paragraph 116, d.509):
- Ngân hàng tính toán dòng tiền vào và dòng tiền ra theo hợp đồng dựa trên các mô hình định giá hiện hành;
- **Nguyên tắc bù trừ ròng (Net basis)**: Dòng tiền chỉ được phép bù trừ ròng (dòng tiền vào bù trừ dòng tiền ra) theo từng đối tác khi và chỉ khi tồn tại một thỏa thuận bù trừ song phương chuẩn tắc có hiệu lực pháp lý (Master Netting Agreement như ISDA Master Agreement);
- Các quyền chọn (Options) được giả định là sẽ được bên mua quyền thực hiện (exercised) nếu quyền chọn đang ở trạng thái có lãi (in the money);
- *Bù trừ tài sản bảo đảm HQLA (Paragraph 117, d.510)*: Nếu nghĩa vụ thanh toán phái sinh được bảo đảm bằng tài sản HQLA, dòng tiền ra được tính sau khi trừ đi tài sản bảo đảm hoặc dòng tiền vào nhận về theo hợp đồng, với điều kiện ngân hàng có đầy đủ năng lực pháp lý và tác nghiệp để tái sử dụng tài sản bảo đảm đó nhằm tránh tính trùng lặp.

**2. Cú sốc hạ bậc xếp hạng tín nhiệm lên đến 3 bậc (3-Notch Downgrade Trigger)**

Một trong những giả định căng thẳng nghiêm ngặt nhất của Basel III là việc mô phỏng tác động dây chuyền khi uy tín tín dụng của chính ngân hàng bị sụt giảm nghiêm trọng (bcbs_238, file bcbs238.md, Paragraph 118, d.511):
- Trong thực tiễn thị trường, nhiều hợp đồng phái sinh, giao dịch tài trợ và thỏa thuận tín dụng quốc tế có lồng ghép các "điều khoản kích hoạt hạ bậc" (downgrade triggers), quy định rằng nếu ngân hàng bị các tổ chức xếp hạng tín nhiệm (như Moody's, S&P, Fitch) hạ bậc tín nhiệm, đối tác có quyền yêu cầu ngân hàng phải nộp thêm tài sản bảo đảm, hoàn trả trước hạn các khoản vay hoặc rút vốn khẩn cấp;
- Chuẩn mực LCR bắt buộc ngân hàng phải giả định rằng tổ chức của mình bị **hạ bậc tín nhiệm dài hạn lên đến và bao gồm 3 bậc (up to and including a 3-notch downgrade)** (ví dụ từ AA- xuống A-, hoặc từ A xuống BBB);
- Ngân hàng phải tính toán **100% khối lượng tài sản bảo đảm bổ sung phải ký quỹ** hoặc các dòng tiền mặt phải hoàn trả trước hạn do cú sốc hạ 3 bậc tín nhiệm này kích hoạt trên toàn bộ danh mục hợp đồng hiện hữu, bao gồm cả việc mất quyền tái thế chấp (rehypothecation rights) đối với tài sản bảo đảm nhận từ khách hàng.

**3. Lượng hóa biến động định giá TSBĐ và Phương pháp Hồi cứu lịch sử 24 tháng (Lookback Approach)**

Nhằm dự phòng cho các biến động bất lợi của thị trường tài chính làm xói mòn giá trị tài sản bảo đảm hoặc mở rộng phơi nhiễm phái sinh, BCBS 238 áp dụng hai cơ chế lượng hóa bắt buộc:
1. **Dự phòng biến động giá TSBĐ phi Cấp 1 đã ký quỹ (20% Haircut Shock)**:
   - Khi ngân hàng sử dụng tài sản bảo đảm để ký quỹ phái sinh, nếu tài sản đó là tiền mặt hoặc công cụ nợ Cấp 1 có hệ số rủi ro 0%, ngân hàng không phải trích lập thêm HQLA dự phòng (Paragraph 119, d.512);
   - Tuy nhiên, nếu ngân hàng nộp tài sản bảo đảm bằng các công cụ phi Cấp 1 (Cấp 2A, Cấp 2B hoặc tài sản khác), ngân hàng bắt buộc phải bổ sung thêm vào dòng tiền ra dự kiến một khoản bằng **20% giá trị của toàn bộ số tài sản bảo đảm phi Cấp 1 đã nộp** (net với tài sản nhận về có quyền tái sử dụng), nhằm bù đắp rủi ro tài sản bị sụt giá buộc ngân hàng phải nộp thêm ký quỹ;
2. **Phương pháp Hồi cứu lịch sử 24 tháng (Historical Lookback Approach, Paragraph 123, d.519)**:
   - Để dự phòng dòng tiền ký quỹ bổ sung phát sinh do biến động giá trị thị trường (mark-to-market) của danh mục phái sinh, ngân hàng phải rà soát toàn bộ lịch sử biến động trong **24 tháng gần nhất**;
   - Xác định dòng chuyển dịch tài sản bảo đảm ròng tuyệt đối lớn nhất trong khoảng thời gian 30 ngày từng diễn ra trong 24 tháng đó ($\text{Largest absolute net 30-day collateral flow realized during the preceding 24 months}$);
   - Giá trị cực đại này bắt buộc phải được đưa vào dòng tiền ra của LCR như một khoản dự phòng rủi ro biến động định giá phái sinh trong 30 ngày tới.

Ngoài ra, ngân hàng phải tính toán dòng tiền ra 100% đối với: (i) tài sản bảo đảm dư thừa không tách biệt mà đối tác có quyền đòi lại bất kỳ lúc nào (Paragraph 120); (ii) tài sản bảo đảm theo hợp đồng mà đối tác chưa yêu cầu nộp (Paragraph 121); và (iii) các hợp đồng cho phép đối tác thay thế TSBĐ HQLA bằng non-HQLA mà không cần ngân hàng đồng ý (Paragraph 122).

**4. Ma trận tỷ lệ rút vốn từ Hạn mức cam kết tín dụng và thanh khoản (Committed Facilities)**

Các hạn mức tín dụng và thanh khoản đã cam kết ngoại bảng (committed facilities) đại diện cho quyền rút vốn đơn phương của khách hàng khi thị trường biến động. Phần hạn mức cam kết chưa sử dụng (undrawn portion, sau khi đã bù trừ tài sản bảo đảm HQLA đối tác nộp theo Paragraph 127) phải chịu ma trận tỷ lệ rút vốn (drawdown rates) phân tầng theo đối tác (bcbs_238, file bcbs238.md, Paragraph 126–131, d.534–547):

- **Khách hàng bán lẻ và Doanh nghiệp nhỏ (SME)**: Giả định tỷ lệ rút vốn là **5%** đối với cả hạn mức tín dụng và hạn mức thanh khoản;
- **Doanh nghiệp phi tài chính, Chính phủ, NHTW, PSEs và MDBs**:
  - Hạn mức tín dụng đã cam kết (Committed credit facilities): Tỷ lệ rút **10%**;
  - Hạn mức thanh khoản đã cam kết (Committed liquidity facilities): Tỷ lệ rút **30%**;
  - *Phân định giữa Hạn mức tín dụng và Hạn mức thanh khoản (Paragraph 128, d.536)*: Hạn mức thanh khoản là hạn mức dự phòng dùng để tái cấp vốn cho các khoản nợ của khách hàng đáo hạn trong 30 ngày khi khách hàng không đảo nợ được trên thị trường (như bảo lãnh phát hành thương phiếu ABCP). Các hạn mức vốn lưu động thông thường (revolving credit) phục vụ sản xuất kinh doanh được phân loại là hạn mức tín dụng (credit facilities);
- **Các ngân hàng chịu sự giám sát an toàn (Banks subject to prudential supervision)**: Tỷ lệ rút vốn là **40%** cho cả hạn mức tín dụng và thanh khoản;
- **Các định chế tài chính khác (Công ty chứng khoán, bảo hiểm, fiduciaries)**:
  - Hạn mức tín dụng đã cam kết: Tỷ lệ rút **40%**;
  - Hạn mức thanh khoản đã cam kết: Tỷ lệ rút triệt để **100%**;
- **Các pháp nhân khác (SPEs, Conduits, SPVs cấu trúc)**: Tỷ lệ rút triệt để **100%** cho cả hạn mức tín dụng và thanh khoản.

**5. Nghĩa vụ hợp đồng cho vay và Cam kết tài trợ thương mại**

- **Nghĩa vụ giải ngân hợp đồng cho vay trong 30 ngày (Contractual lending obligations)**:
  - Nghĩa vụ cho vay đối với định chế tài chính: Áp dụng tỷ lệ dòng tiền ra **100%** (Paragraph 132, d.548);
  - Nghĩa vụ cho vay đối với khách hàng bán lẻ và doanh nghiệp phi tài chính: Nếu tổng nghĩa vụ giải ngân theo hợp đồng vượt quá **50%** tổng dòng tiền vào hợp đồng thu nợ từ chính nhóm khách hàng này trong 30 ngày, phần giá trị chênh lệch vượt quá 50% đó bắt buộc phải báo cáo là dòng tiền ra chịu tỷ lệ **100%** (Paragraph 133, d.549–559);
- **Cam kết tài trợ thương mại (Trade Finance Instruments)**:
  - Áp dụng tỷ lệ rút vốn ưu đãi thấp từ **3% đến 5%** (hoặc $\le 5\%$ do cơ quan quản lý ấn định) đối với các công cụ ngoại bảng gắn liền trực tiếp với dòng luân chuyển hàng hóa và cung ứng dịch vụ thực tế (Thư tín dụng L/C chứng từ, nhờ thu chứng từ, bộ chứng từ nhập khẩu/xuất khẩu và bảo lãnh nhận hàng shipping guarantees theo Paragraph 138, d.565–567);
  - Các khoản cam kết cho vay tài trợ xuất nhập khẩu trực tiếp không thuộc diện này và phải áp dụng tỷ lệ rút vốn hạn mức tín dụng (10%–100%).

**Bảng tổng hợp tham số dòng tiền ra ngoại bảng và rủi ro gia tăng**

| Danh mục cam kết ngoại bảng / Rủi ro gia tăng | Cơ sở xác định / Tính chất hợp đồng | Tỷ lệ dòng tiền ra |
|---|---|---|
| **Dòng tiền phái sinh ròng (Derivatives Net)** | Bù trừ ròng theo Master Netting Agreement | **100%** |
| **Cú sốc hạ 3 bậc tín nhiệm (3-Notch Downgrade)** | Ký quỹ bổ sung / Hoàn trả hợp đồng kích hoạt | **100%** |
| **Biến động giá TSBĐ phái sinh phi Cấp 1** | Áp dụng trên giá trị TSBĐ phi Cấp 1 đã ký quỹ | **20%** |
| **Biến động định giá phái sinh (Lookback)** | Dòng chuyển TSBĐ ròng cực đại 30 ngày trong 24 tháng | **100% giá trị cực đại** |
| **Hạn mức cam kết Bán lẻ & Doanh nghiệp nhỏ** | Undrawn credit & liquidity facilities | **5%** |
| **Hạn mức cam kết Doanh nghiệp phi tài chính / CP** | Credit facilities: **10%** \| Liquidity facilities: **30%** | **10% / 30%** |
| **Hạn mức cam kết Ngân hàng thương mại** | Undrawn credit & liquidity facilities | **40%** |
| **Hạn mức cam kết Định chế tài chính khác** | Credit facilities: **40%** \| Liquidity facilities: **100%** | **40% / 100%** |
| **Hạn mức cam kết SPVs, Conduits, SPEs** | Undrawn credit & liquidity facilities | **100%** |
| **Cam kết tài trợ thương mại (Trade Finance)** | L/C chứng từ, nhờ thu, bảo lãnh nhận hàng | **3%–5%** |

Xem thêm: [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]], [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], [[contingent-liquidity-outflows-and-credit-facility-drawdowns-stress-test-off-balance-commitments]], [[contingent-liquidity-risk-framework-mandates-asymmetric-spv-treatment-and-commitment-modeling]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]].
