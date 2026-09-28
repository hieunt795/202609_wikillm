---
title: money-multiplier-mechanics-governs-fractional-reserve-expansion-via-geometric-deposit-lending-series
type: concept
tags: [money-multiplier, fractional-reserve-banking, high-powered-money, bank-run, credit-creation]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-28
---

Cơ chế số nhân tiền tệ (money multiplier) mô tả quy luật toán học và động lực học kế toán chi phối khả năng mở rộng cung tiền của hệ thống ngân hàng dự trữ một phần (fractional-reserve banking) dựa trên một lượng tiền cơ sở hữu hạn (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.88–96).

**Bản chất kinh tế của dự trữ và xung đột động lực:**
- Khác với giấy chứng nhận lưu ký (certificates) bị giới hạn nghiêm ngặt ở tỷ lệ bảo đảm 100% bằng kim loại vật chất, giấy bạc ngân hàng và tiền gửi thanh toán bản chất là nghĩa vụ nợ, do đó về mặt lý thuyết không có giới hạn trần tuyệt đối về số lượng phát hành danh nghĩa (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.90).
- Do người gửi tiền hoặc người nắm giữ giấy bạc có thể xuất trình để đòi rút tiền mặt bất kỳ lúc nào, ngân hàng buộc phải duy trì một lượng tiền mặt vật chất hoặc số dư tại [[central-bank|ngân hàng trung ương]] để đáp ứng các yêu cầu rút tiền này, gọi là dự trữ (reserves) (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.90).
- Hệ thống ngân hàng đối mặt với một xung đột động lực cố hữu:
  - *Động lực sinh lời*: Do tiền dự trữ nằm im không sinh lãi (hoặc lãi suất rất thấp), các chủ ngân hàng luôn có động cơ kinh tế giảm tỷ lệ dự trữ xuống mức tối thiểu có thể để tối đa hóa tài sản sinh lời (cho vay hoặc mua chứng khoán).
  - *Yêu cầu an toàn thận trọng*: Nguyên tắc quản trị rủi ro lại đòi hỏi tỷ lệ dự trữ phải càng lớn càng tốt để đối phó với các đợt rút tiền bất thường.
  - Dù quy mô dự trữ thực tế lớn đến đâu, rủi ro lượng tiền gửi bị yêu cầu rút ra vượt quá quy mô dự trữ sẵn có vẫn luôn tồn tại; hiện tượng này chính là đột biến rút tiền (bank run), đe dọa trực tiếp khả năng thanh toán của ngân hàng trừ khi có sự can thiệp của Người cho vay cứu cánh cuối cùng (lender of last resort) (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.90, chú thích 8).

**Mô hình toán học của chuỗi cấp số nhân tạo tiền:**
- Tầm quan trọng kinh tế của hệ thống ngân hàng không nằm ở việc phát hành giấy bạc mà nằm ở hành vi tái cho vay các khoản tiền gửi: khi ngân hàng giải ngân, nó tạo ra tiền tệ mới bởi vì cả giấy bạc/khoản tiền gửi ban đầu và số tiền vừa cho vay đều đồng thời lưu hành trong nền kinh tế theo [[commercial-banks-create-inside-money-by-extending-credit]] (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.92). Lượng tiền cho vay sau khi bên vay chi tiêu thanh toán sẽ quay trở lại hệ thống ngân hàng dưới dạng khoản tiền gửi mới, tạo tiền đề cho các vòng cho vay kế tiếp (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.92).
- Giả định một khoản tiền gửi ban đầu bằng tiền mặt/specie là $D_0$, và hệ thống ngân hàng duy trì một tỷ lệ dự trữ cố định $r$ (với $0 < r < 1$).
  - Vòng 1: Ngân hàng giữ lại $r D_0$ làm dự trữ và đem số tiền còn lại cho vay:
    $$L_1 = D_0 (1 - r)$$
  - Vòng 2: Người nhận tiền chi tiêu, số tiền $L_1$ được người bán hàng gửi lại vào ngân hàng thành khoản tiền gửi mới $D_1 = L_1 = D_0 (1 - r)$. Ngân hàng giữ lại $r D_1$ làm dự trữ và tiếp tục cho vay:
    $$L_2 = D_1 (1 - r) = D_0 (1 - r)^2$$
  - Vòng $k$: Khoản tiền gửi ở vòng thứ $k$ là $D_k = D_0 (1 - r)^k$, và khoản vay tạo ra là $L_k = D_0 (1 - r)^k$.
- Khi quá trình tái cho vay và tái gửi tiền diễn ra liên tục qua vô hạn vòng ($n \to \infty$), tổng lượng tiền tệ tối đa $M$ (bao gồm tiền gửi ban đầu và toàn bộ các vòng tiền gửi phát sinh) được xác định bằng tổng của một cấp số nhân lùi vô hạn với công bội $q = (1 - r) < 1$:
  $$M = \sum_{k=0}^{\infty} D_0 (1 - r)^k = D_0 \left( \frac{1}{1 - (1 - r)} \right) = \frac{D_0}{r}$$
- Hệ số nhân tiền tệ lý thuyết (monetary multiplier), ký hiệu là $m$, được định nghĩa là tỷ số giữa tổng cung tiền $M$ tạo ra và lượng tiền cơ sở ban đầu $D_0$:
  $$m = \frac{M}{D_0} = \frac{1}{r}$$
- Ví dụ số học: Với khoản tiền gửi ban đầu 10 đồng vàng ($D_0 = 10$) và tỷ lệ dự trữ $r = 10\%$ ($r = 0{,}1$), lượng tiền cho vay vòng 1 là 9 đồng, đưa tổng tiền lưu hành lên 19 đồng; vòng 2 cho vay tiếp $8{,}1$ đồng; khi chuỗi hội tụ, tổng lượng tiền giấy/tiền ghi sổ tối đa được tạo ra trong nền kinh tế đạt mức:
  $$M = \frac{10}{0{,}1} = 100 \text{ đồng}$$
- Do sự gia tăng của lượng tiền kim loại quý cơ sở $D_0$ dẫn đến sự gia tăng gấp $m$ lần tổng cung tiền lưu hành, lượng tiền cơ sở này được gọi là tiền có sức mạnh cao (high-powered money hay base money) (fixed_income_during, Ch.4, The Money Multiplier, file -5, d.96).

**Hạn chế thực tế và tương tác vĩ mô:**
- Trong thực tế, số nhân tiền tệ thực nghiệm thường thấp hơn giá trị lý thuyết $1/r$ do sự rò rỉ tiền mặt ra ngoài lưu thông phi ngân hàng và việc các ngân hàng thương mại chủ động nắm giữ dự trữ dư thừa (excess reserves).
- Mặc dù vậy, mối quan hệ cơ học giữa cung tiền $M$, tiền cơ sở $D_0$ và tỷ lệ dự trữ $r$ vẫn là nền tảng chi phối việc mở rộng tín dụng: tỷ lệ dự trữ đóng vai trò như một chiếc "áo bó" kiểm soát quy mô tạo tiền của hệ thống tư nhân theo [[fiat-money-removes-the-commodity-reserve-straightjacket-from-global-trade-settlement]], và chính sự sụp đổ của số nhân tiền tệ trong các thời kỳ bẫy thanh khoản là nguyên nhân khiến các chương trình nới lỏng định lượng của ngân hàng trung ương không tự động chuyển hóa thành lạm phát theo [[quantitative-easing-compresses-money-multipliers-and-reserve-velocity-decoupling-from-exchange-rate-fundamentals]].
