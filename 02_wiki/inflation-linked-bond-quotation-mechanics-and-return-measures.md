---
title: inflation-linked-bond-quotation-mechanics-and-return-measures
type: concept
tags: [fixed-income, inflation-linked-bonds, real-yield, breakeven-inflation]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-28
---
Trái phiếu liên kết lạm phát (inflation-linked bonds hay linkers, điển hình là TIPS của Mỹ, OATi/OAT€i của Pháp) là công cụ nợ bảo vệ sức mua thực tế của nhà đầu tư trước sự gia tăng của mức giá chung (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.80–99). Về mặt quy ước thị trường quốc tế, trái phiếu liên kết lạm phát hầu hết được yết giá theo giá sạch thực tế (clean real price), loại trừ cả phần lãi tích dồn lẫn phần tích lũy lạm phát kể từ ngày phát hành (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.82). Quy ước này đảm bảo rằng mức giá yết của trái phiếu không bị thay đổi bởi dòng thời gian trôi qua hay bởi các biến động hàng tháng của chỉ số giá tiêu dùng (CPI) (ngoại trừ thị trường trái phiếu Gilt liên kết lạm phát của Vương quốc Anh theo truyền thống từng yết giá gộp cả lạm phát tích lũy) (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.82).

Để chuyển đổi từ mức giá sạch thực tế $P_{\text{clean, real}}$ sang số tiền thanh toán thực tế mà bên mua phải trả tại ngày thanh toán $t$, thị trường sử dụng hệ số chỉ số hóa (indexation ratio - $IR(t)$):
$$IR(t) = \frac{\text{CPI}(t)}{\text{CPI}_{\text{base}}}$$
trong đó $\text{CPI}(t)$ là chỉ số lạm phát tham chiếu áp dụng cho ngày thanh toán (thường được nội suy tuyến tính với độ trễ 3 tháng để đảm bảo tính xác định trước khi thanh toán), và $\text{CPI}_{\text{base}}$ là chỉ số lạm phát tại ngày bắt đầu tính lãi của trái phiếu (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.84). Giá danh nghĩa (nominal price) của trái phiếu bằng giá thực tế nhân với hệ số chỉ số hóa:
$$P_{\text{nominal}}(t) = P_{\text{real}}(t) \times IR(t)$$
Giá hóa đơn (invoice price / settlement consideration) thực tế thanh toán trên mỗi đơn vị mệnh giá cơ sở là tổng của giá sạch thực tế và lãi tích dồn thực tế $AI_{\text{real}}$, sau đó nhân với hệ số chỉ số hóa $IR(t)$:
$$P_{\text{invoice}}(t) = (P_{\text{clean, real}} + AI_{\text{real}}) \times IR(t)$$
trong đó lãi tích dồn thực tế $AI_{\text{real}}$ được tính toán theo quy tắc đếm ngày thông thường áp dụng trên lãi suất coupon thực tế danh nghĩa của trái phiếu (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.88–92). Đối với các cấu trúc trái phiếu liên kết lạm phát dạng lãi suất thả nổi (FRN-style, ví dụ như dòng trái phiếu CCT€ của Ý), giá hóa đơn được thanh toán trực tiếp từ giá sạch cộng lãi tích dồn, nhưng lãi tích dồn được tính dựa trên coupon thả nổi đã bao hàm thành phần bù lạm phát (fixed_income_during, Ch.23, Quotation of index-linked bonds, d.94–98).

Đo lường mức sinh lời của trái phiếu liên kết lạm phát đối mặt với thách thức lớn: lạm phát tương lai là một biến số ngẫu nhiên không thể dự báo hoàn hảo, khiến các dòng tiền coupon danh nghĩa được tái đầu tư trở nên bất định (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.202–213). Giải pháp chuẩn tắc của thị trường là trừu tượng hóa yếu tố lạm phát và định nghĩa lợi suất thực (real yield - $\rho$) (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.206). Lợi suất thực $\rho$ được xác định bằng cách giải phương trình cân bằng giữa giá bẩn thực tế hiện hành với toàn bộ các dòng coupon thực và mệnh giá thực (giả định bằng 100 không đổi) chiết khấu theo tỷ suất $\rho$:
$$P_{\text{dirty, real}} = \sum_{i=1}^n \frac{C_{\text{real}}}{(1 + \rho)^{t_i}} + \frac{100}{(1 + \rho)^{t_n}}$$
Về mặt mô hình hóa toán học, một trái phiếu TIPS có thể được xem xét tương đương như một trái phiếu phát hành bằng ngoại tệ (foreign currency bond analogy) (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.208). Trong phép so sánh tương quan này:
- Lợi suất thực $\rho$ của TIPS đóng vai trò tương tự như lợi suất của một trái phiếu chính phủ Nhật Bản (JGB) được tính toán theo đồng Yên nội tệ trên thị trường Tokyo (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.208).
- Lợi suất danh nghĩa $r$ của trái phiếu Kho bạc Mỹ thông thường đóng vai trò như lợi suất danh nghĩa của đồng tiền cơ sở USD (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.208).
- Biến động tỷ giá USD/JPY tương đương với tốc độ thay đổi của chỉ số lạm phát $IR(t)$ (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.208).
Cả hai thước đo lợi suất này không đại diện cho tổng mức sinh lời danh nghĩa thực tế cuối cùng của nhà đầu tư, bởi vì rủi ro tỷ giá (đối với JGB) hay rủi ro lạm phát (đối với TIPS) sẽ tạo thêm một cấu phần sinh lời bổ sung (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.208). Trong điều kiện thị trường hiệu quả và định giá trung lập với rủi ro, kỳ vọng lợi suất danh nghĩa của một trái phiếu liên kết lạm phát được giả định bằng đúng lợi suất của trái phiếu danh nghĩa tương đương có cùng kỳ hạn (fixed_income_during, Ch.23, RETURN MEASURES OF INFLATION-LINKED BONDS, d.210).

Lợi suất thực $\rho$ và lợi suất danh nghĩa $r$ là hai đầu vào quyết định để tính toán tỷ lệ lạm phát hòa vốn (breakeven inflation - $\pi_{\text{BEI}}$), tức là mức lạm phát trung bình hàng năm khiến cho tỷ suất sinh lời nội bộ của việc đầu tư vào trái phiếu liên kết lạm phát bằng đúng tỷ suất sinh lời của trái phiếu danh nghĩa cùng kỳ hạn (fixed_income_during, Ch.23, Breakeven inflation, d.216–224):
1. **Phương pháp xấp xỉ tuyến tính Fisher**:
$$\pi_{\text{BEI}} = r - \rho$$
Phương pháp này dựa trên giả định đơn giản rằng lãi suất danh nghĩa là tổng của lãi suất thực và lạm phát kỳ vọng, tuy nhiên nó bỏ qua hiệu ứng ghép lãi chéo (fixed_income_during, Ch.23, Breakeven inflation, d.220).
2. **Phương pháp điểm hoán đổi ngoại hối (FX Forward Points / Compounded Breakeven)**:
Dựa trên phép suy rộng tương quan ngoại hối, mối quan hệ chính xác không trọng tài có dạng:
$$1 + r = (1 + \rho)(1 + \pi_{\text{BEI}}) \iff \pi_{\text{BEI}} = \frac{1 + r}{1 + \rho} - 1 = \frac{r - \rho}{1 + \rho}$$
Công thức này khử hoàn toàn sai số ghép lãi và là công cụ giao dịch cốt lõi trong các chiến lược hoán đổi lạm phát (inflation swaps) và phòng hộ nợ công được liên kết với [[outright-curve-and-relative-value-bond-trading-strategies]].
