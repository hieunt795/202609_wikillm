---
title: basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, basel, basel-iii, stress-testing, buffer-usability, banking-supervision, bcbs-238]
sources: [bcbs_238]
status: stable
last_updated: 2026-09-26
---

Khuôn khổ Tỷ lệ khả năng chi trả (Liquidity Coverage Ratio - LCR) theo chuẩn mực Basel III (BCBS 238) thiết lập tiêu chuẩn an toàn thanh khoản ngắn hạn tối thiểu bắt buộc trên phạm vi toàn cầu, yêu cầu các ngân hàng thương mại hoạt động quốc tế phải nắm giữ một lượng tài sản có tính thanh khoản cao không bị ràng buộc (unencumbered High-Quality Liquid Assets - HQLA) đủ khả năng tự chuyển đổi thành tiền mặt tại thị trường tư nhân nhằm bù đắp toàn bộ dòng tiền rút ròng trong kịch bản căng thẳng thanh khoản kết hợp nghiêm trọng kéo dài 30 ngày dương lịch (bcbs_238, file bcbs238.md, Introduction & Part 1 Section I–II, Paragraphs 1–22, d.71–156).

**1. Bối cảnh ra đời và mục tiêu chiến lược của chuẩn mực LCR**

Trong giai đoạn đầu của cuộc khủng hoảng tài chính toàn cầu bùng nổ năm 2007, nhiều định chế tài chính quốc tế dù vẫn duy trì tỷ lệ an toàn vốn (Capital Adequacy Ratio) ở mức cao theo quy chuẩn nhưng vẫn rơi vào tình trạng mất khả năng thanh toán nghiêm trọng do những sơ hở trong quản trị rủi ro thanh khoản nguồn vốn và sự phụ thuộc quá mức vào các thị trường tài trợ bán buôn ngắn hạn chi phí thấp (bcbs_238, file bcbs238.md, Paragraph 2, d.74). Sự đảo chiều đột ngột của điều kiện thị trường cho thấy thanh khoản có thể bốc hơi trong chớp mắt và tình trạng đóng băng thị trường có thể kéo dài dai dẳng, buộc các ngân hàng trung ương phải can thiệp khẩn cấp trên quy mô chưa từng có để giải cứu hệ thống tiền tệ và các định chế riêng lẻ.

Nhằm khắc phục triệt để các lỗ hổng này, Ủy ban Basel ban hành bộ nguyên tắc nền tảng [[bcbs-sound-principles-establish-foundational-liquidity-risk-management-and-supervisory-mandates]] (BCBS 144) vào năm 2008, và sau đó chính thức chuẩn hóa thành hai tỷ lệ an toàn thanh khoản tối thiểu thuộc hiệp ước Basel III:
- **Tỷ lệ khả năng chi trả (LCR)**: Định cỡ và bắt buộc duy trì bộ đệm thanh khoản ngắn hạn đủ khả năng chống chịu độc lập trong chân trời 30 ngày dương lịch chịu căng thẳng cực đoan;
- **Tỷ lệ nguồn vốn ổn định ròng (NSFR)**: Định hướng cơ cấu kỳ hạn bền vững giữa tài sản và nguồn vốn tài trợ trong khoảng thời gian 1 năm nhằm ngăn ngừa mất cân đối thanh khoản cấu trúc dài hạn theo [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]].

Mục tiêu cốt lõi của LCR là bảo đảm ngân hàng có đủ tài sản HQLA để duy trì khả năng thanh toán độc lập tối thiểu cho đến Ngày thứ 30 của cuộc khủng hoảng. Chân trời 30 ngày này là khoảng thời gian bản lề cho phép Ban điều hành ngân hàng và cơ quan thanh tra giám sát kích hoạt kế hoạch tài trợ dự phòng [[contingency-funding-plan-establishes-crisis-governance-and-operational-escalation-frameworks]] hoặc tiến hành xử lý, tái cấu trúc ngân hàng một cách trật tự, đồng thời tạo điều kiện để ngân hàng trung ương đánh giá tình hình và đưa ra các quyết sách can thiệp hệ thống cần thiết (bcbs_238, file bcbs238.md, Paragraph 16, d.107).

**2. Kịch bản căng thẳng thanh khoản kết hợp 30 ngày (Combined Stress Scenario)**

Khác với các giả định đơn tuyến, kịch bản căng thẳng thanh khoản 30 ngày làm cơ sở định cỡ LCR là một kịch bản kết hợp chặt chẽ giữa cú sốc mang tính đặc thù ngân hàng (idiosyncratic shock) và cú sốc mang tính toàn hệ thống (market-wide shock), mô phỏng lại các áp lực thanh khoản dữ dội nhất từng diễn ra trong cuộc khủng hoảng 2007–2008 (bcbs_238, file bcbs238.md, Paragraph 19–20, d.135–143):
- **Sự sụt giảm tiền gửi bán lẻ**: Một tỷ lệ nhất định người gửi tiền cá nhân thực hiện rút tiền gửi không kỳ hạn và có kỳ hạn trước hạn (retail run-off);
- **Đóng băng thị trường tài trợ bán buôn không bảo đảm**: Ngân hàng mất một phần hoặc toàn bộ khả năng tiếp cận và tái cấp vốn nguồn tiền gửi, phát hành thương phiếu (CP) và chứng chỉ tiền gửi (CD) từ các định chế tài chính và khách hàng doanh nghiệp;
- **Suy giảm khả năng tài trợ ngắn hạn có bảo đảm**: Thị trường giao dịch mua bán lại (Repo) ngắn hạn bị thắt chặt, các đối tác từ chối tái tục hợp đồng hoặc áp dụng tỷ lệ chiết khấu (haircut) cao hơn đối với tài sản bảo đảm;
- **Áp lực dòng tiền do hạ bậc xếp hạng tín nhiệm (Rating Downgrade Trigger)**: Tổ chức xếp hạng tín nhiệm hạ bậc xếp hạng tín nhiệm độc lập của ngân hàng lên đến và bao gồm 3 bậc (up to and including three notches), kích hoạt các điều khoản bổ sung ký quỹ tài sản bảo đảm và hoàn trả trước hạn các hợp đồng huy động vốn cam kết;
- **Biến động thị trường phái sinh gia tăng**: Biến động giá tài sản cơ sở làm mở rộng mức độ phơi nhiễm tiềm tàng tương lai (PFE), buộc ngân hàng phải nộp thêm tài sản bảo đảm (margin calls) cho các đối tác phái sinh theo phương pháp hồi cố lịch sử 24 tháng;
- **Rút vốn ồ ạt từ các cam kết ngoại bảng**: Khách hàng doanh nghiệp và các định chế tài chính kích hoạt rút vốn đột biến từ các hạn mức tín dụng và hạn mức thanh khoản đã cam kết chưa sử dụng;
- **Nghĩa vụ phi hợp đồng nhằm bảo vệ danh tiếng**: Ngân hàng phải chịu áp lực mua lại nợ đã phát hành, hỗ trợ thanh khoản cho các công cụ đầu tư cấu trúc (SIV/SPEs) hoặc chi trả cho các cam kết tài trợ thương mại để duy trì niềm tin thị trường.

Ủy ban Basel nhấn mạnh kịch bản 30 ngày của LCR chỉ là chuẩn mực giám sát tối thiểu (regulatory floor). Các tổ chức tín dụng bắt buộc phải chủ động xây dựng các kịch bản kiểm tra sức chịu đựng thanh khoản nội bộ với chân trời dài hơn và các giả định khắc nghiệt hơn phù hợp với mô hình kinh doanh cụ thể theo [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]].

**3. Lộ trình thực thi phân kỳ (Phase-in Arrangements)**

Nhằm tạo điều kiện để hệ thống ngân hàng thương mại quốc tế từng bước củng cố bộ đệm thanh khoản một cách trật tự, tránh tạo ra những biến động tiêu cực làm thắt chặt dòng vốn tín dụng tài trợ cho nền kinh tế thực, Ủy ban Basel đã ban hành lộ trình áp dụng phân kỳ đối với tỷ lệ LCR từ năm 2015 đến năm 2019 (bcbs_238, file bcbs238.md, Paragraph 8–10, d.82–90):
- **Từ ngày 01 tháng 01 năm 2015**: Ngưỡng LCR tối thiểu đạt **60%**;
- **Từ ngày 01 tháng 01 năm 2016**: Ngưỡng LCR tối thiểu đạt **70%**;
- **Từ ngày 01 tháng 01 năm 2017**: Ngưỡng LCR tối thiểu đạt **80%**;
- **Từ ngày 01 tháng 01 năm 2018**: Ngưỡng LCR tối thiểu đạt **90%**;
- **Từ ngày 01 tháng 01 năm 2019 trở đi**: Chính thức áp dụng ngưỡng đầy đủ **100%**.

Các quốc gia riêng lẻ hoặc các nền kinh tế đang tiếp nhận các chương trình hỗ trợ tái cơ cấu vĩ mô có thể linh hoạt điều chỉnh tiến độ áp dụng nội địa nhưng không được nới lỏng các chuẩn tắc an toàn cơ bản (Paragraph 11, d.93).

**4. Nguyên tắc cốt lõi: Khả năng sử dụng đệm HQLA trong điều kiện căng thẳng (Buffer Usability under Stress)**

Một trong những đóng góp mang tính nguyên lý quan trọng nhất của BCBS 238 là việc tái khẳng định và thiết lập cơ chế **Khả năng sử dụng đệm HQLA** (bcbs_238, file bcbs238.md, Paragraph 11 & 17–18, d.85, 108–132):
- **Bản chất của bộ đệm thanh khoản**: Đệm HQLA được tích lũy trong điều kiện hoạt động bình thường không phải để đóng băng bất khả xâm phạm trên bảng cân đối kế toán, mà mục đích cốt lõi là để **sử dụng khi xảy ra căng thẳng thanh khoản**. Trong các giai đoạn khủng hoảng tài chính, ngân hàng hoàn toàn được phép chuyển đổi HQLA thành tiền mặt để bù đắp dòng tiền thiếu hụt, chấp nhận để tỷ lệ LCR giảm xuống dưới ngưỡng tối thiểu 100% (hoặc dưới ngưỡng tối thiểu theo lộ trình);
- **Hiểm họa nghịch chu kỳ (Procyclicality Risk)**: Nếu các cơ quan quản lý vi mô cứng nhắc ép buộc ngân hàng phải luôn duy trì LCR trên 100% ngay giữa tâm bão khủng hoảng, các ngân hàng sẽ buộc phải tích trữ tiền mặt, từ chối giải ngân các hạn mức cam kết, ngừng gia hạn cho vay liên ngân hàng và đẩy mạnh bán tháo tài sản kém thanh khoản (fire-sales). Hành vi phòng vệ cục bộ này sẽ tạo ra hiệu ứng dây chuyền tiêu cực, làm co thắt thanh khoản thị trường và bóp nghẹt dòng tín dụng của toàn bộ nền kinh tế thực;
- **Phản ứng giám sát linh hoạt và tương xứng (Proportionate Supervisory Response)**: Cơ quan giám sát không tự động áp đặt các biện pháp trừng phạt tức thì khi ngân hàng vi phạm ngưỡng LCR 100% do sử dụng HQLA đối phó stress, mà phải tiến hành đánh giá toàn diện bối cảnh:
  1. *Nguyên nhân sụt giảm*: Phân tích việc sụt giảm là do ngân hàng chủ động kích hoạt kho HQLA, do mất khả năng đảo nợ hay do khách hàng rút vốn đột biến;
  2. *Bản chất của cú sốc*: Xác định rõ cú sốc bắt nguồn từ nguyên nhân nội tại của chính ngân hàng (firm-specific shock) hay do khủng hoảng lan truyền toàn hệ thống (system-wide shock);
  3. *Quy mô, thời gian và tần suất*: Mức độ sụt giảm HQLA nghiêm trọng đến đâu và dự kiến kéo dài bao lâu;
  4. *Kế hoạch khôi phục*: Tối thiểu ngân hàng phải trình nộp bản tự đánh giá vị thế thanh khoản, làm rõ các động lực dẫn tới thâm hụt LCR, giải trình các biện pháp đã và sẽ thực hiện, cùng dự báo thời gian cần thiết để tái thiết bộ đệm thanh khoản;
  5. *Lộ trình tái tạo bộ đệm trật tự*: Trong trường hợp căng thẳng diện rộng, cơ quan giám sát và ngân hàng phải thảo luận về lộ trình phục hồi thanh khoản được thực thi dần dần qua một khoảng thời gian thích hợp nhằm tránh gây áp lực dồn nén ngược lại hệ thống tài chính.

Xem thêm: [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[bcbs-sound-principles-establish-foundational-liquidity-risk-management-and-supervisory-mandates]], [[multi-scenario-liquidity-stress-testing-integrates-behavioral-shocks-and-informs-capital-planning]], [[contingency-funding-plan-establishes-crisis-governance-and-operational-escalation-frameworks]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]].
