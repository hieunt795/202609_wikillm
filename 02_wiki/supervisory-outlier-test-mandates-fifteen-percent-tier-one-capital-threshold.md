---
title: supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold
type: concept
tags: [irrbb, outlier-test, tier-1-capital, srep, supervisory-benchmark, bcbs-368]
sources: [bcbs_368]
status: draft
last_updated: 2026-09-26
---

Chuẩn mực kiểm tra ngoại lệ giám sát (Supervisory Outlier Test — SOT) theo Chuẩn mực BCBS 368 (Nguyên tắc 12) bắt buộc cơ quan thanh tra giám sát phải công bố công khai tiêu chí định lượng nhận diện các ngân hàng có rủi ro lãi suất ngoại lệ (Outlier Banks), trong đó thiết lập ngưỡng cảnh báo cưỡng chế bắt buộc: mức suy giảm giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) tối đa dưới sáu kịch bản sốc lãi suất chuẩn hóa của Phụ lục 2 không được vượt quá **15% Vốn tự có cấp 1 (Tier 1 Capital)** của ngân hàng (bcbs_368, file d368.md, Section II.2, Principle 12, d.493–498). Đây là một bước thắt chặt an toàn vĩ mô mang tính bước ngoặt so với Nguyên tắc Basel 2004 trước đó: Basel II 2004 áp dụng ngưỡng 20% trên Tổng vốn tự có (Total Regulatory Capital gồm cả Vốn cấp 2), trong khi BCBS 368 hạ thấp ngưỡng xuống 15% đồng thời thu hẹp mẫu số chỉ còn Vốn cấp 1 (loại bỏ toàn bộ nợ thứ cấp và trái phiếu chuyển đổi cấp 2 kém phẩm chất), biến bài kiểm tra SOT thành một bộ lọc an toàn vốn khắt khe hơn đáng kể (bcbs_368, file d368.md, Principle 12, d.495–496).

Về mặt công thức chuẩn tắc, tiêu chí nhận diện ngân hàng ngoại lệ bắt buộc của BCBS 368 được biểu diễn:
$$\text{Outlier Indicator} = \frac{\max_{k \in \{1,\dots,6\}} \left| \Delta EVE_k \right|}{\text{Tier 1 Capital}} > 15\%$$
trong đó $k$ là một trong sáu kịch bản sốc lãi suất chuẩn hóa quy định tại Annex 2 (gồm Parallel up, Parallel down, Steepener, Flattener, Short rate up, Short rate down), và $\Delta EVE_k$ được tính toán nhất quán theo [[delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion|quy tắc kỹ thuật Trụ cột 3]] (áp dụng giả định bảng cân đối run-off, loại trừ vốn tự có, chiết khấu theo đường cong phi rủi ro) (bcbs_368, file d368.md, Principle 12, d.495–496).

Bên cạnh ngưỡng bắt buộc 15% Tier 1 Capital, BCBS 368 (Đoạn 89) cho phép cơ quan thanh tra giám sát quốc gia ban hành thêm các bài kiểm tra ngoại lệ bổ sung với điều kiện các bài kiểm tra này có mức độ nghiêm ngặt tối thiểu tương đương:
- *Bài kiểm tra theo vốn cấp 1 cốt lõi (CET1 Capital)* hoặc theo thặng dư vốn tự có vượt trên mức yêu cầu tối thiểu của Trụ cột 1;
- *Bài kiểm tra ngoại lệ theo thu nhập lãi thuần ($\Delta NII$)*: Đánh giá xem mức suy giảm thu nhập lãi dưới các kịch bản sốc có khiến ngân hàng thâm hụt lợi nhuận nghiêm trọng đến mức không đủ khả năng duy trì hoạt động kinh doanh bình thường hoặc buộc phải cắt giảm chi trả cổ tức hay không (bcbs_368, file d368.md, Principle 12, d.497, d.511).

Khi một ngân hàng bị định danh là Outlier Bank, cơ quan giám sát sẽ tiến hành thanh tra toàn diện mức độ nhạy cảm của bảng cân đối kế toán (bcbs_368, file d368.md, Principle 12, d.501–508). Thanh tra viên sẽ đánh giá đặc biệt rủi ro của các tài sản ghi nhận theo giá trị hợp lý (mark-to-market), đồng thời ước tính tác động tiềm tàng nếu toàn bộ các vị thế trên sổ ngân hàng đang hạch toán theo giá gốc phân bổ (historical cost như các khoản cho vay khách hàng hoặc trái phiếu HTM) buộc phải phản ánh theo giá thị trường (lỗ ngầm định embedded losses) (bcbs_368, file d368.md, Principle 12, d.503). Đồng thời, cơ quan giám sát sẽ bóc tách mức độ hợp lý của các giả định hành vi nhạy cảm: việc đưa vào biên độ thương mại, tính ổn định của [[non-maturity-deposit-behavioural-modelling-governs-core-and-non-core-segmentation-under-irrbb|tiền gửi không kỳ hạn NMDs]], và quyền chọn trả nợ trước hạn CPR để xác định xem ngân hàng có đang sử dụng các giả định lạc quan thái quá nhằm che giấu trạng thái rủi ro thực tế hay không (bcbs_368, file d368.md, Principle 12, d.503).
