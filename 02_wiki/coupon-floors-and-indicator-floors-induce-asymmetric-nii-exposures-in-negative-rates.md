---
title: coupon-floors-and-indicator-floors-induce-asymmetric-nii-exposures-in-negative-rates
type: concept
tags: [alm, coupon-floor, indicator-floor, negative-rates, nii, embedded-options]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Trong môi trường chính sách lãi suất âm theo [[zero-lower-bound-interest-rate-floors-distort-banking-book-margins-under-nirp]], việc quản trị rủi ro thu nhập lãi thuần NII phụ thuộc mang tính quyết định vào việc phân định hai cấu trúc sàn lãi suất độc lập: sàn lãi suất danh nghĩa (Coupon Floor) và sàn chỉ số tham chiếu (Indicator Floor) (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429). Hai loại sàn này tạo ra cơ chế truyền dẫn dòng tiền hoàn toàn trái ngược khi lãi suất thị trường lao dốc (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429–2431):

1. **Sàn lãi suất danh nghĩa (Coupon Floor)**: Quy định lãi suất thực trả của hợp đồng không được phép giảm xuống dưới 0%:
$$r_{customer} = \max(r_I + x; 0\%)$$
Trong đó $r_I$ là chỉ số lãi suất tham chiếu thả nổi (như EURIBOR) và $x$ là biên độ lãi suất (*spread*). Ở cấu trúc này, chỉ số $r_I$ hoàn toàn có thể nhận giá trị âm miễn là phần bù $x$ đủ lớn để tổng lãi suất không âm; tuy nhiên, khi $r_I$ âm càng sâu, phần bù biên độ $x$ của ngân hàng bị xói mòn tương ứng và khách hàng không nhận được đầy đủ mức biên kỳ vọng. Điển hình của Coupon Floor là các tài khoản tiết kiệm bán lẻ được pháp luật bảo vệ quyền lợi người tiêu dùng (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429);
2. **Sàn chỉ số tham chiếu (Indicator Floor)**: Chặn cứng bản thân chỉ số thị trường cơ sở ở mốc 0% trước khi cộng thêm biên độ:
$$r_{customer} = \max(r_I; 0\%) + x$$
Tại đây, biên độ margin $x$ được bảo vệ tuyệt đối ngay cả khi lãi suất thị trường giảm sâu vào vùng âm. Cấu trúc Indicator Floor xuất hiện phổ biến trong các hợp đồng cấp tín dụng cho khách hàng doanh nghiệp được thiết kế điều khoản bảo vệ bên cho vay (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2429).

Tác động kinh tế của sàn lãi suất 0% phụ thuộc vào việc nó được gắn vào tài sản hay nguồn vốn nợ (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2433). Coupon Floor là bất lợi đối với bên nguồn vốn (hạn chế khả năng ngân hàng thu phí lãi âm trên tiền gửi), nhưng lại có lợi đối với bên tài sản (ngăn ngừa ngân hàng phải trả lãi ngược cho người đi vay) (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2433).

Mối hiểm họa lớn nhất đối với bảng cân đối phát sinh khi xảy ra sự bất đối xứng chéo giữa hai bên bảng cân đối kế toán (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2435; tata_bank_alm, Ch.3, Notes, d.2512):
Giả sử ngân hàng giải ngân tài sản ở mức $r_I + x$ và tài trợ bằng nguồn vốn cùng mức $r_I + x$. Trong điều kiện thông thường, thu nhập lãi thuần bằng 0 ($NII = 0$) tại mọi mức lãi suất. Tuy nhiên, nếu phía tài sản chịu **Coupon Floor** trong khi phía nguồn vốn nợ chịu **Indicator Floor**, công thức NII biến thành:
$$NII = \max(r_I + x; 0) - [\max(r_I; 0) + x]$$
Khi chỉ số thị trường $r_I$ rơi vào vùng âm:
- Khi $r_I > 0$: $NII = (r_I + x) - (r_I + x) = 0$;
- Khi $-x \le r_I \le 0$: $NII = (r_I + x) - (0 + x) = r_I \le 0$;
- Khi $r_I < -x$: $NII = 0 - (0 + x) = -x < 0$ (tata_bank_alm, Ch.3, Notes, d.2512).

Trong tình huống bất đối xứng này, NII của ngân hàng **không bao giờ có thể dương và bắt buộc phải chịu lỗ ròng (NII âm)** khi lãi suất thị trường rơi xuống dưới 0% (tata_bank_alm, Ch.3, Notes, d.2512). Ngược lại, nếu ngân hàng khéo léo đàm phán được Indicator Floor bên tài sản và Coupon Floor bên nợ, ngân hàng sẽ thu được siêu lợi nhuận phòng hộ trong môi trường NIRP (tata_bank_alm, Ch.3, 0% Interest Rate Floor, d.2435).

Cơ chế floor bất đối xứng tạo thành một cấu phần trọng yếu trong [[interest-rate-option-risk-combines-automatic-and-embedded-behavioural-options]] và [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]], đòi hỏi bộ phận ALM phải tích hợp vào mô phỏng đa kịch bản theo [[net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]], đồng thời định giá sòng phẳng thông qua các khoản phụ phí điều chỉnh quyền chọn trên đường cong chuyển giao vốn theo [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]].
