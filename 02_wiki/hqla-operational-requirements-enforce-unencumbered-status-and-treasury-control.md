---
title: hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, operational-requirements, unencumbered-assets, treasury, collateral-pool, bcbs-238]
sources: [bcbs_238]
status: draft
last_updated: 2026-09-26
---

Yêu cầu vận hành đối với tài sản có tính thanh khoản cao (Operational Requirements for HQLA) theo chuẩn mực Basel III (BCBS 238) thiết lập các chuẩn tắc quản trị và tác nghiệp bắt buộc nhằm bảo đảm toàn bộ tài sản được ghi nhận vào tử số của tỷ lệ [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]] luôn ở trạng thái không bị ràng buộc pháp lý (unencumbered) và nằm dưới quyền định đoạt trực tiếp, liên tục của bộ phận quản lý thanh khoản (Treasury/ALM) để có thể chuyển đổi ngay lập tức thành tiền mặt trong vòng 30 ngày căng thẳng mà không gặp bất kỳ trở ngại nào (bcbs_238, file bcbs238.md, Part 1 Section II.A.2–3, Paragraphs 28–44, d.188–218).

**1. Mục đích và nguyên lý của các yêu cầu vận hành**

Ủy ban Basel chỉ rõ: việc một tài sản tài chính đáp ứng đầy đủ các tiêu chuẩn định tính, xếp hạng tín nhiệm hay hệ số rủi ro tín dụng là điều kiện cần nhưng chưa đủ để được tính vào bộ đệm thanh khoản. Nếu một tài sản trên sổ sách có phẩm cấp cao nhưng ngân hàng bị hạn chế về mặt pháp lý, hợp đồng, tác nghiệp hoặc năng lực hệ thống khiến bộ phận quản lý thanh khoản không thể bán đứt hoặc thế chấp vay vốn trong chu kỳ thanh toán tiêu chuẩn (standard settlement period), tài sản đó hoàn toàn vô giá trị trong việc cứu trợ thanh khoản khẩn cấp (Paragraph 28–29, 32, d.190, 194).

Do đó, các yêu cầu vận hành đóng vai trò là bộ lọc tác nghiệp loại bỏ các tài sản bị kẹt (trapped assets), tài sản bị phong tỏa hoặc tài sản thuộc các mảng kinh doanh tự doanh khỏi danh mục HQLA đủ chuẩn.

**2. Tiêu chuẩn tài sản không bị ràng buộc (Unencumbered Status)**

Khái niệm "không bị ràng buộc" (unencumbered) được định nghĩa là trạng thái tài sản hoàn toàn tự do khỏi các hạn chế về pháp lý, quy định quản lý, hợp đồng hoặc tác nghiệp đối với khả năng thanh lý, bán, chuyển nhượng hoặc chuyển giao của ngân hàng (bcbs_238, file bcbs238.md, Paragraph 31, d.193):
- **Cấm thế chấp và bảo lãnh chéo**: Tài sản tính vào HQLA không được đem cầm cố, thế chấp (dù rõ ràng hay ngầm định) để bảo đảm, hỗ trợ tín dụng cho bất kỳ giao dịch tài chính nào khác, và không được dùng để dự phòng trang trải các chi phí hoạt động thường nhật của ngân hàng (như tiền lương, chi phí thuê trụ sở);
- **Điều kiện đối với tài sản nhận từ giao dịch Reverse Repo**: Tài sản nhận về từ các hợp đồng mua lại đảo ngược (Reverse Repo) và các giao dịch tài trợ chứng khoán (SFT) chỉ được tính vào HQLA nếu chúng đang thực tế nằm tại ngân hàng, chưa bị đem đi tái thế chấp (rehypothecated), và ngân hàng có toàn quyền sở hữu hợp pháp và hợp đồng để định đoạt;
- **Tài sản ký gửi sẵn tại Ngân hàng Trung ương/Tổ chức công**: Các tài sản đủ điều kiện HQLA đã được ký gửi, ký quỹ trước (pre-positioned hoặc deposited) tại ngân hàng trung ương hoặc tổ chức công (PSE) nhưng **chưa sử dụng** để vay vốn hoặc làm bảo đảm cho các khoản cấp tín dụng vẫn được công nhận là unencumbered và được tính vào kho HQLA (Paragraph 31, d.193).

**3. Quy tắc giải tỏa tài sản trong Pool bảo đảm hỗn hợp tại NHTW (Collateral Pool Allocation Rule - Footnote 9)**

Trong thực tiễn quản lý kho quỹ, các ngân hàng thương mại thường ký gửi một danh mục tài sản bảo đảm hỗn hợp (collateral pool) bao gồm cả tài sản Cấp 1, Cấp 2 và tài sản phi HQLA tại ngân hàng trung ương để sẵn sàng cho các nghiệp vụ thị trường mở hoặc thấu chi thanh toán. Khi một giao dịch vay vốn phát sinh mà NHTW không chỉ định đích danh loại chứng khoán cụ thể nào bị phong tỏa làm tài sản bảo đảm, BCBS 238 thiết lập nguyên tắc phân bổ mang tính bảo vệ tối đa cho ngân hàng (Footnote 9, d.197):
- Ngân hàng được phép giả định rằng các tài sản trong pool bị ràng buộc (encumbered) theo thứ tự ưu tiên từ **tính thanh khoản thấp nhất đến cao nhất**;
- Trình tự phong tỏa giả định:
  $$\text{Tài sản không đủ điều kiện HQLA (phi HQLA)} \longrightarrow \text{Tài sản Cấp 2B} \longrightarrow \text{Tài sản Cấp 2A} \longrightarrow \text{Tài sản Cấp 1}$$
- Cơ chế phân bổ này bảo đảm các tài sản có phẩm cấp cao nhất (Level 1 và Level 2A) luôn là những tài sản cuối cùng bị coi là encumbered, từ đó tối đa hóa giá trị danh mục HQLA khả dụng được tính vào tử số LCR, miễn là tuân thủ các quy định riêng về tập trung và đa dạng hóa của NHTW.

**4. Quyền kiểm soát độc quyền của Bộ phận Quản lý Thanh khoản (Treasury/ALM Control)**

Toàn bộ kho tài sản HQLA phải nằm dưới sự kiểm soát trực tiếp và toàn quyền của chức năng quản lý thanh khoản ngân hàng (Treasurer hoặc bộ phận ALM) (bcbs_238, file bcbs238.md, Paragraph 33, d.195):
- Bộ phận Treasury phải có thẩm quyền liên tục, năng lực pháp lý và tác nghiệp để thanh lý hoặc repo bất kỳ tài sản nào trong kho tại bất kỳ thời điểm nào trong suốt 30 ngày căng thẳng;
- Bằng chứng kiểm soát được xác lập qua hai phương thức: (i) duy trì tài sản trong một pool dự phòng thanh khoản riêng biệt (segregated liquidity pool) do Treasury quản lý với mục đích duy nhất là làm nguồn vốn dự phòng khẩn cấp; hoặc (ii) chứng minh được Treasury có thể thanh lý tài sản mà số tiền thu được hoàn toàn sẵn sàng phục vụ thanh khoản mà không xung đột trực tiếp với chiến lược kinh doanh hoặc quản trị rủi ro;
- *Ngăn chặn xung đột phòng ngừa rủi ro*: Một tài sản không được đưa vào HQLA nếu việc bán tài sản đó trong 30 ngày (mà không có tài sản thay thế) sẽ hủy bỏ một vị thế phòng ngừa rủi ro (hedge), từ đó tạo ra một vị thế rủi ro mở (open risk position) vi phạm các hạn mức rủi ro nội bộ của ngân hàng.

**5. Kiểm tra định kỳ khả năng chuyển đổi thành tiền mặt (Periodic Monetisation Testing)**

Ngân hàng không được phép nắm giữ thụ động danh mục HQLA trên sổ sách. Nhằm bảo đảm tính khả thi tác nghiệp, ngân hàng bắt buộc phải định kỳ thực hiện các giao dịch bán thực tế hoặc giao dịch repo trên thị trường với một tỷ lệ đại diện tài sản trong kho (bcbs_238, file bcbs238.md, Paragraph 30, d.192). Hoạt động kiểm tra định kỳ này nhằm:
- Kiểm tra thực tế khả năng tiếp cận thị trường và độ trễ khớp lệnh;
- Đánh giá hiệu quả của quy trình vận hành thanh lý nội bộ;
- Xác nhận tính sẵn sàng của tài sản tại các tổ chức lưu ký;
- Triệt tiêu "hiệu ứng phát tín hiệu tiêu cực" (stigmatisation risk): nếu một ngân hàng chưa bao giờ bán tài sản hoặc repo trên thị trường mà đột ngột thực hiện khối lượng lớn trong khủng hoảng, thị trường sẽ suy đoán ngân hàng đang bên bờ vực phá sản. Giao dịch định kỳ giúp thị trường coi các lệnh bán này là hoạt động nghiệp vụ bình thường.

**6. Xử lý phòng ngừa rủi ro thị trường, rào cản chuyển giao và thời gian ân hạn 30 ngày**

BCBS 238 quy định cụ thể các khía cạnh tác nghiệp chuyên sâu:
- **Phòng ngừa rủi ro thị trường và dòng tiền đóng vị thế sớm (Hedging treatment)**: Ngân hàng được phép phòng ngừa rủi ro lãi suất hoặc rủi ro thị trường cho HQLA. Tuy nhiên, giá trị thị trường của tài sản HQLA phải được điều chỉnh giảm trừ tương ứng với dòng tiền ra tiềm tàng nếu hợp đồng phái sinh phòng ngừa đó bị đóng trước hạn (close-out cash outflow) khi bán tài sản (Paragraph 34, d.201);
- **Rào cản chuyển giao thanh khoản giữa các pháp nhân (Transfer restrictions)**: HQLA nằm tại các công ty con hoặc chi nhánh nước ngoài chỉ được tính vào LCR hợp nhất của ngân hàng mẹ tối đa bằng mức dòng tiền ra ròng của chính đơn vị đó. Phần thặng dư HQLA chỉ được hợp nhất nếu ngân hàng chứng minh được tài sản có thể chuyển giao tự do về công ty mẹ trong khủng hoảng mà không bị cản trở bởi các rào cản pháp lý, kiểm soát ngoại hối, thuế hoặc chế tài giám sát sở tại theo [[cross-border-supervisory-cooperation-and-crisis-information-sharing-contain-contagion]] (Paragraph 36–37, d.203–204);
- **Thời gian ân hạn 30 ngày đối với tài sản bị rớt hạng (30-day Grace Period)**: Nhằm giảm thiểu hiệu ứng vách đá (cliff effects) khi một chứng khoán HQLA đột ngột bị hạ bậc tín nhiệm dẫn tới không còn đủ chuẩn HQLA, ngân hàng được phép tiếp tục giữ tài sản đó trong danh mục HQLA thêm **30 ngày dương lịch** kể từ ngày bị hạ bậc để có đủ thời gian tái cấu trúc hoặc tìm tài sản thay thế mà không làm gãy đổ tỷ lệ LCR tức thì (Paragraph 43, d.213);
- **Đa dạng hóa danh mục HQLA**: Ngân hàng phải thiết lập chính sách và hạn mức nội bộ để phân tán rủi ro tập trung theo loại công cụ, tổ chức phát hành và đồng tiền (ngoại trừ trái phiếu chính phủ nội tệ, tiền mặt và dự trữ tại NHTW) theo quy định tại Paragraph 44 (d.217).

Xem thêm: [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]], [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]], [[cross-border-supervisory-cooperation-and-crisis-information-sharing-contain-contagion]], [[contingency-funding-plan-establishes-crisis-governance-and-operational-escalation-frameworks]].
