---
title: surcharges-for-over-proportional-reliance-on-the-central-bank
type: concept
tags: [chinh-sach-tien-te, ngan-hang-trung-uong, thanh-khoan, nguoi-cho-vay-cuoi-cung]
sources: [bindseil_monetary_policy]
status: draft
last_updated: 2026-09-21
---

**Khái niệm và cơ sở lý luận**: Nhằm giải quyết [[lender-of-last-resort-moral-hazard-and-liquidity-externalities|rủi ro đạo đức và nguy cơ phụ thuộc quá mức vào NHTW]] trong khi vẫn duy trì vai trò cung ứng thanh khoản đàn hồi của [[lender-of-last-resort-foundations-and-bagehot-principles|người cho vay cuối cùng (LOLR)]], Ulrich Bindseil đề xuất khung phụ thu lãi suất lũy tiến dựa trên mức độ vay vốn quá tỷ lệ (over-proportionality surcharge). Cơ chế này hiện đại hóa nguyên lý cổ điển của Walter Bagehot ("cho vay tự do nhưng với lãi suất phạt") bằng cách chuyển hóa lãi suất phạt thành một hàm chi phí tài chính phi tuyến tính gắn liền với quy mô bảng cân đối kế toán của từng ngân hàng, thay vì áp đặt lãi suất phạt đồng loạt làm triệt tiêu khả năng tiếp cận vốn hoặc gây kỳ thị ([[effective-corridor-asymmetry-and-stigma-in-overnight-rates|stigma]]) (bindseil_monetary_policy, Ch.16, §16.3, d.3779–3784).

**Mô hình toán học về phí phụ thu quá tỷ lệ**:
- Gọi $L = \sum L_i$ là tổng quy mô tài sản của toàn hệ thống ngân hàng và $B = \sum B_i$ là tổng quy mô tái cấp vốn từ NHTW.
- Tỷ lệ phụ thuộc bình quân toàn hệ thống (overall proportionality) được định nghĩa là:
  $$P = \frac{B}{L}$$
- Hệ số phụ thuộc riêng lẻ của ngân hàng $i$ (individual proportionality factor) là:
  $$p_i = \frac{B_i}{L_i}$$
- Một ngân hàng được coi là vay vốn đúng tỷ lệ khi $p_i = P$. Nếu ngân hàng $i$ vượt quá ngưỡng phụ thuộc cho phép, NHTW áp đặt khoản phí phụ thu danh nghĩa $\kappa_i = f(P, p_i, B_i)$:
  $$\kappa_i = \begin{cases} 0 & \text{khi } p_i \le aP \\ b(p_i - aP) B_i & \text{khi } p_i > aP \end{cases}$$
  trong đó $a \ge 1$ là tham số vùng đệm miễn trừ (buffer multiplier) và $b > 0$ là hệ số độ dốc phạt lãi suất (bindseil_monetary_policy, Ch.16, §16.3, d.3785–3798).

**Ý nghĩa của vùng đệm miễn trừ ($a \ge 1$)**: Sự hiện diện của tham số $a \ge 1$ có ý nghĩa quyết định đối với việc thực thi chính sách tiền tệ. Do các ngân hàng có mô hình kinh doanh khác nhau và thường xuyên chịu các cú sốc thanh khoản ngẫu nhiên ngắn hạn, nếu NHTW phạt ngay khi $p_i > P$ ($a = 1$), thì trong trạng thái bình thường sẽ luôn có khoảng một nửa hệ thống ngân hàng bị áp phí phụ thu ở biên. Điều này sẽ vô tình tạo ra sự thắt chặt ngoài ý muốn đối với lập trường [[monetary-policy|chính sách tiền tệ]] (monetary policy stance). Vùng đệm $a > 1$ cho phép các biến động thanh khoản thông thường diễn ra tự do mà không làm sai lệch lãi suất điều hành (bindseil_monetary_policy, Ch.16, §16.3, d.3797–3798).

**Tiền lệ lịch sử và sự tương đồng thể chế**: Cơ chế điều tiết dựa trên tỷ lệ phụ thuộc có nguồn gốc sâu xa trong lịch sử ngân hàng trung ương:
- *Cục Dự trữ Liên bang Mỹ (Fed)*: Năm 1919, một số chi nhánh Federal Reserve Bank đã áp dụng biểu lãi suất chiết khấu lũy tiến theo tỷ lệ quy mô vay của từng ngân hàng thành viên (Goldenweiser, 1949).
- *Ngân hàng Liên bang Đức (Bundesbank)*: Áp dụng hệ thống hạn ngạch tái chiết khấu (*Rediskontkontingente*) trong nhiều thập kỷ, gắn trần vay chiết khấu của mỗi ngân hàng với vốn tự có và cấu trúc bảng cân đối.
- *Quỹ Tiền tệ Quốc tế (IMF)*: Áp dụng biểu phí phụ thu (surcharges) đối với các quốc gia thành viên vay vượt quá hạn ngạch (quota) đóng góp (bindseil_monetary_policy, Ch.16, §16.3, d.3781–3782, 3771).

**Hai kịch bản định chuẩn tham số ($a, b$)**: Tùy thuộc vào ưu tiên mục tiêu của NHTW, hai cấu hình tham số có thể được thiết lập:
1. *Kiểm soát phụ thuộc cơ cấu trong thời bình ($a$ thấp, $b$ vừa phải, ví dụ $a = 1{,}1; b = 2\%$)*: Giả định phân phối tỷ lệ vay của các ngân hàng tuân theo phân phối chuẩn $\mathcal{N}(P = 10\%, \sigma_p^2 = 2\%^2)$. Với ngưỡng $aP = 11\%$, có $31\%$ số ngân hàng phải chịu phụ thu với mức phí bình quân toàn hệ thống là $0{,}79\%$. Cơ chế này tạo áp lực kinh tế thúc đẩy các ngân hàng có tỷ lệ vay cao tìm kiếm vốn từ thị trường liên ngân hàng, kéo giảm độ lệch chuẩn $\sigma_p$ từ $2\%$ xuống $1\%$ và làm giảm chi phí phụ thu bình quân xuống $0{,}16\%$. Mức thắt chặt ban đầu có thể được trung hòa bằng cách hạ lãi suất mục tiêu nghiệp vụ.
2. *Rào cản ngăn chặn ỷ lại trong khủng hoảng ($a$ cao, $b$ rất cao, ví dụ $a = 1{,}5; b = 5\%$)*: Cấu hình này hầu như không kích hoạt trong điều kiện bình thường (phí bình quân chỉ $0{,}02\%$), không gây can thiệp vào hoạt động tạo lập thị trường. Nhưng trong khủng hoảng, khi độ phân tán $\sigma_p$ vọt lên $6\%$, phí phụ thu bình quân vọt lên $1{,}61\%$, và nhóm $7\%$ ngân hàng phụ thuộc nhiều nhất vào NHTW sẽ phải chịu mức lãi suất phạt tăng thêm từ $10$ điểm phần trăm trở lên. Điều này tạo động lực cực lớn để các ngân hàng tái cấu trúc thanh khoản và thanh lý tài sản tự nguyện ngay khi khủng hoảng lắng dịu (bindseil_monetary_policy, Ch.16, §16.3, d.3809–3820).

**Các biện pháp bổ trợ hoàn thiện**:
- *Thu phí quản lý và định giá tài sản bảo đảm kém thanh khoản*: NHTW cần thu phí bù đắp chi phí đối với các tài sản phức tạp, kém thanh khoản do ngân hàng đệ trình làm [[central-bank-collateral-framework-design-and-risk-control|tài sản bảo đảm]], nhằm loại bỏ hiện tượng bao cấp chi phí thẩm định rủi ro.
- *Yêu cầu an toàn vốn đối với rủi ro phụ thuộc dự phòng*: Cơ quan giám sát ngân hàng có thể sử dụng chỉ số [[liquidity-regulation-and-central-bank-operations-arbitrage|Khoảng cách tới mất thanh khoản (DTI)]] kết hợp với việc tính toán trước chi phí phụ thu dự kiến từ NHTW trong kịch bản căng thẳng để áp đặt yêu cầu vốn dự phòng bổ sung (capital charges) (bindseil_monetary_policy, Ch.16, §16.3, d.3821–3826).
