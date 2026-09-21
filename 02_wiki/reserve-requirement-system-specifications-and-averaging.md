---
title: reserve-requirement-system-specifications-and-averaging
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, reserve-requirements, money-market]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

Quy chuẩn kỹ thuật của hệ thống [[required-reserves|dự trữ bắt buộc]] và cơ chế bình quân hoá (averaging) quyết định trực tiếp hiệu quả đệm thanh khoản và độ ổn định của lãi suất ngắn hạn trong thị trường tiền tệ (bindseil_monetary_policy, Ch.8, §8.2–8.3, d.1497–1578).

**Cơ sở tính dự trữ và tỷ lệ dự trữ**: Các hệ thống truyền thống thường phân loại nợ phải trả của ngân hàng thành tiền gửi không kỳ hạn, có kỳ hạn và tiết kiệm, áp dụng tỷ lệ cao hơn cho các khoản nợ có tính chất "giống tiền" nhất. Tuy nhiên, xu hướng hiện đại là đơn giản hoá tối đa cơ sở tính (như ECB chỉ áp dụng 1% trên nợ phi-ngân hàng kỳ hạn dưới 2 năm) để giảm chi phí hành chính và tránh hiện tượng ngân hàng cơ cấu lại nợ nhằm lách luật (d.1503, d.1554).

**Độ trễ giữa kỳ tính toán và kỳ duy trì (Contemporaneous vs. Lagged Reserve Accounting)**:
- *Kỳ tính toán đồng thời (Contemporaneous)*: Kỳ xác định nghĩa vụ dự trữ trùng lặp với kỳ duy trì dự trữ. Trường phái tiền tệ từng ủng hộ phương thức này để tăng cường khả năng kiểm soát tiền tệ tức thời (Friedman 1982). Tuy nhiên, phương thức này buộc ngân hàng phải đáp ứng dự trữ trước khi biết chính xác tổng nghĩa vụ của mình, gây hỗn loạn cho công tác quản trị thanh khoản.
- *Kỳ tính toán có độ trễ (Lagged)*: Nghĩa vụ dự trữ được tính dựa trên số dư tiền gửi của một kỳ trong quá khứ và được công bố trước khi kỳ duy trì bắt đầu. Fed từng áp dụng tính đồng thời trước 1968, chuyển sang có độ trễ năm 1968, tái áp dụng đồng thời năm 1984 do áp lực học thuyết, và cuối cùng quay lại vĩnh viễn với chế độ tính có độ trễ vào năm 1998 nhằm giúp bàn giao dịch OMO và các ngân hàng nắm bắt số liệu chính xác tuyệt đối (d.1507–1508).

**Thời điểm đo lường và vấn đề trả lãi**: Khi dự trữ bắt buộc được trả lãi đầy đủ (như tại Eurosystem), ngân hàng không có động lực bóp méo bảng cân đối, cho phép NHTW đo lường cơ sở tính chỉ bằng một ngày chốt sổ (snapshot) duy nhất trong tháng. Ngược lại, khi không được trả lãi (như Bundesbank trước 1999), NHTW phải tính bình quân trên nhiều ngày chốt sổ (4 ngày trải đều trong tháng) để ngăn chặn các thủ thuật làm đẹp sổ sách tạm thời (d.1511–1512).

**Cơ chế bình quân hoá (Reserve averaging) và độ dài tối ưu của kỳ duy trì**: Ngân hàng chỉ cần đảm bảo số dư bình quân cuối ngày trong suốt kỳ duy trì (maintenance period) đạt mức dự trữ bắt buộc. Cơ chế này đóng vai trò như một van điều tiết tự động: ngân hàng sẵn sàng cho vay ra khi lãi suất qua đêm tăng cao và giữ nhiều dự trữ hơn khi lãi suất giảm, giữ cho lãi suất qua đêm tuân theo [[martingale-property-of-overnight-rates-and-reserve-averaging|tính chất Martingale]].
- *Tại sao kỳ duy trì không vượt quá 1 tháng?*: Nếu kỳ duy trì kéo dài (chẳng hạn 1 năm), kỳ vọng về các đợt thay đổi lãi suất chính sách của NHTW trong năm sẽ phá vỡ tính chất Martingale. Khi thị trường kỳ vọng NHTW sắp tăng lãi suất, các ngân hàng sẽ dồn dập vay sớm và tích luỹ dự trữ vượt mức ngay từ đầu kỳ, gây ra hiện tượng méo mó đặt thầu (overbidding) hoặc ồ ạt dùng borrowing facility (d.1575).
- *Cải cách năm 2004 của ECB*: Trong giai đoạn 1999–2003, các quyết định lãi suất của ECB diễn ra giữa kỳ duy trì đã gây bất ổn định cho việc bình quân hoá. Tháng 3/2004, ECB cải tổ mang tính bước ngoặt: đồng bộ hoá ngày bắt đầu kỳ duy trì dự trữ trùng khớp với lịch họp định kỳ của Hội đồng Thống đốc (Governing Council), đảm bảo mọi thay đổi lãi suất chính sách chỉ có hiệu lực từ đầu kỳ duy trì tiếp theo, loại bỏ hoàn toàn kỳ vọng đổi lãi suất trong kỳ (d.1577).

**Điều khoản chuyển tiếp (Carry-over provisions)**: Cho phép ngân hàng kết chuyển một tỷ lệ thiếu hụt hoặc dư thừa dự trữ giới hạn sang kỳ duy trì kế tiếp (ví dụ Fed cho phép chuyển tiếp tối đa 4% nghĩa vụ dự trữ). Quy định này làm giảm áp lực thanh khoản và triệt tiêu biến động lãi suất cực đoan vào ngày chốt sổ cuối cùng của kỳ duy trì (d.1569).

**Xử lý tiền mặt tại quỹ (Vault cash) và mô hình không dự trữ bắt buộc**:
- Fed cho phép khấu trừ tiền mặt tại quỹ (applied vault cash) vào nghĩa vụ dự trữ (Friedman 1960). Ngược lại, Eurosystem và Bundesbank từ chối tính tiền mặt tại quỹ vì không phục vụ chức năng làm đệm thanh khoản liên ngân hàng và nặng tính thủ tục hành chính (d.1527).
- Một số NHTW (như Ngân hàng Trung ương Canada) vận hành hệ thống bình quân hoá thanh khoản thành công mà hoàn toàn không cần áp đặt tỷ lệ dự trữ bắt buộc, bằng cơ chế cho phép ngân hàng thấu chi tài khoản thanh toán cuối ngày miễn là số dư bình quân qua chu kỳ duy trì quanh mức 0 ("averaging around zero") (Clinton 1997; Davies 1998; d.1569).

Xem thêm: [[required-reserves]], [[functions-of-reserve-requirements-in-monetary-policy]], [[martingale-property-of-overnight-rates-and-reserve-averaging]], [[taralac-facility-target-rate-limited-access]].
