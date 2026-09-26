---
title: pillar-3-irrbb-quantitative-disclosure-standards-mandate-table-b-metrics
type: concept
tags: [irrbb, pillar-3, disclosure, table-b, quantitative-metrics, shock-scenarios]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Chuẩn mực công bố thông tin định lượng Trụ cột 3 về IRRBB theo Chuẩn mực BCBS 368 (Nguyên tắc 8, Table B) thiết lập một khuôn mẫu báo cáo cố định (fixed format) bắt buộc mọi ngân hàng phải công bố định kỳ hàng năm mức độ biến động của cả giá trị kinh tế của vốn chủ sở hữu ($\Delta EVE$) và thu nhập lãi thuần ($\Delta NII$) dưới sáu kịch bản sốc lãi suất chuẩn hóa do Ủy ban Basel quy định tại Phụ lục 2 (Annex 2), đối chiếu song song giữa kỳ báo cáo hiện tại ($T$) và kỳ báo cáo liền trước ($T-1$) nhằm bảo đảm tính minh bạch và khả năng so sánh thị trường tuyệt đối (bcbs_368, file d368.md, Section II.1, Principle 8, Table B, d.375–404). Khác với tính linh hoạt của Table A, mẫu biểu Table B áp dụng cấu trúc dữ liệu nghiêm ngặt theo đồng tiền báo cáo (reporting currency), đi kèm phần bình luận thuyết minh bắt buộc giải thích ý nghĩa của các giá trị công bố và nguyên nhân dẫn đến các thay đổi trọng yếu so với kỳ trước (bcbs_368, file d368.md, Table B, d.381–384).

Cấu trúc ma trận định lượng của Table B quy định sáu kịch bản sốc lãi suất tức thì (instantaneous rate shock scenarios) gồm (bcbs_368, file d368.md, Table B, d.385–397):
1. *Dịch chuyển song song đi lên (Parallel up)*: Toàn bộ đường cong lợi suất tăng đồng đều qua mọi kỳ hạn;
2. *Dịch chuyển song song đi xuống (Parallel down)*: Toàn bộ đường cong lợi suất giảm đồng đều qua mọi kỳ hạn (tuân thủ quy định sàn lãi suất âm);
3. *Đường cong dốc hơn (Steepener)*: Lãi suất ngắn hạn giảm trong khi lãi suất dài hạn tăng;
4. *Đường cong phẳng hơn (Flattener)*: Lãi suất ngắn hạn tăng trong khi lãi suất dài hạn giảm;
5. *Lãi suất ngắn hạn tăng (Short rate up)*: Cú sốc tăng lãi suất tập trung vào đầu ngắn hạn của đường cong;
6. *Lãi suất ngắn hạn giảm (Short rate down)*: Cú sốc giảm lãi suất tập trung vào đầu ngắn hạn.

Dưới mỗi kịch bản sốc, ngân hàng phải công bố bốn cột dữ liệu số học: $\Delta EVE$ kỳ $T$, $\Delta EVE$ kỳ $T-1$, $\Delta NII$ kỳ $T$ và $\Delta NII$ kỳ $T-1$ (bcbs_368, file d368.md, Table B, d.385–387). Tại dòng tổng kết, ngân hàng phải xác định mức tổn thất lớn nhất (Maximum loss) của $\Delta EVE$ và $\Delta NII$ trong số sáu kịch bản trên, và đặt trong tương quan so sánh trực tiếp với chỉ tiêu ghi nhớ Vốn tự có cấp 1 (Tier 1 Capital) của cả hai kỳ $T$ và $T-1$ (bcbs_368, file d368.md, Table B, d.394–397). Giá trị tổn thất $\Delta EVE$ tối đa này chính là biến số đầu vào trực tiếp được cơ quan thanh tra giám sát sử dụng để thực thi bài kiểm tra ngân hàng ngoại lệ theo [[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]]: nếu tỷ lệ $\frac{\max |\Delta EVE|}{\text{Tier 1 Capital}} > 15\%$, ngân hàng sẽ lập tức bị phân loại là định chế có rủi ro lãi suất quá mức và phải chịu các chế tài can thiệp sớm (bcbs_368, file d368.md, Principle 12, d.495–496).

Quy tắc đo lường số liệu trong Table B bắt buộc phải tuân thủ nghiêm ngặt hai chuẩn mực phương pháp luận: $\Delta EVE$ phải được tính toán dựa trên [[delta-eve-regulatory-calculation-rules-mandate-run-off-and-equity-exclusion|giả định bảng cân đối tất toán dần (run-off balance sheet)]] và loại trừ vốn tự có; trong khi $\Delta NII$ bắt buộc phải được tính toán dựa trên [[delta-nii-regulatory-calculation-rules-mandate-constant-balance-sheet-and-rolling-horizon|giả định bảng cân đối không đổi (constant balance sheet)]] phản ánh mức chênh lệch thu nhập lãi trong khung thời gian 12 tháng lăn kỳ so với kịch bản cơ sở nội bộ tốt nhất của chính ngân hàng (bcbs_368, file d368.md, Principle 8, d.400–404). Việc bắt buộc áp dụng hệ thống giả định kỹ thuật đồng nhất trong Table B triệt tiêu hoàn toàn khả năng các ngân hàng thao túng số liệu bằng các giả định kinh doanh chủ quan, tạo lập một bức tranh rủi ro minh bạch phục vụ kỷ luật thị trường Trụ cột 3.
