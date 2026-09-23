---
title: "Bond Relative Value Metrics Select Reference Curves Aligned with Instrument Hedging Practices"
type: concept
tags:
  - trading
  - bond-trading
  - relative-value
  - curve-spreads
  - hedging-practices
  - ssa-bonds
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Định giá giá trị tương đối của từng mã trái phiếu đơn lẻ (bond relative value) đòi hỏi việc vượt qua các hạn chế căn bản của thước đo lợi suất đáo hạn (yield to maturity) vốn ngầm giả định một cấu trúc kỳ hạn phẳng không thực tế [[yield-to-maturity-assumes-a-flat-term-structure-and-uniform-reinvestment-rates]]. Để bóc tách chính xác mức độ đắt hay rẻ của một chứng khoán so với thị trường, các bàn giao dịch sử dụng các hệ thống chênh lệch đường cong (curve spreads) chuyên biệt (fixed_income_during, Ch.32, Sec.32.1, d.14–19). Khi đối mặt với nhiều loại chênh lệch khả dĩ trên các đường cong tham chiếu khác nhau, nguyên tắc vàng mang tính quyết định là: thước đo chênh lệch hợp lý nhất cho một trái phiếu là thước đo được xây dựng dựa trên chính đường cong phản ánh công cụ phòng hộ rủi ro thực tế thông thường của trái phiếu đó (fixed_income_during, Ch.32, Sec.32.1, d.18–19).

Sự phân hóa công cụ phòng hộ định hình cấu trúc lựa chọn thước đo chênh lệch cho từng phân khúc nợ cụ thể (fixed_income_during, Ch.32, Sec.32.1, d.20–27):
1. Trái phiếu chính phủ: do được phòng hộ trực tiếp bằng các trái phiếu chính phủ lân cận hoặc hợp đồng tương lai cùng nhà phát hành, chênh lệch Z-spread (hoặc spline spread) đo lường trên đường cong spline chính phủ là thước đo giá trị tương đối tự nhiên hàng đầu [[z-spreads-isolate-cash-flow-relative-value-across-full-zero-discount-curves]];
2. Trái phiếu cận quốc gia, siêu quốc gia và cơ quan phát hành (SSA bonds): các công cụ này thường được phòng hộ bằng trái phiếu chính phủ. Mặc dù chênh lệch G-spread trên trái phiếu chuẩn thường được sử dụng phổ biến, G-spread lại không thể so sánh trực tiếp giữa các trái phiếu tham chiếu các benchmark khác nhau và không điều chỉnh cho độ lệch thời lượng; do đó, Z-spread trên mô hình spline phức hợp (composite spline) mang lại độ chuẩn xác vượt trội [[composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition]]. Tại khu vực đồng Euro, phần lớn trái phiếu SSA được giao dịch và phòng hộ dựa trên đường cong trái phiếu chính phủ Pháp (OAT) thay vì đường cong Bund của Đức;
3. Trái phiếu doanh nghiệp xếp hạng cao và trái phiếu có bảo đảm (Covered bonds): do tập quán thị trường sử dụng hợp đồng hoán đổi lãi suất làm công cụ phòng hộ rủi ro thời lượng, chênh lệch hoán đổi nội suy (I-spread) hoặc biên độ hoán đổi tài sản (asset swap spread) trên đường cong swap là lựa chọn tối ưu [[interpolated-i-spreads-trade-off-execution-liquidity-against-curve-hedging-precision]];
4. Tín dụng doanh nghiệp có rủi ro cao: do đường cong tín dụng dốc và biến động mạnh, việc định giá phải dựa trên các mô hình tích hợp đường cong phi rủi ro với chênh lệch hợp đồng hoán đổi rủi ro vỡ nợ (CDS).

Một khiếm khuyết mang tính hệ thống của các mô hình đường cong spline truyền thống là việc chúng được hiệu chỉnh hoàn toàn dựa trên giá giao ngay mà không tính đến diễn biến của lãi suất mua lại repo (fixed_income_during, Ch.32, Sec.32.1, d.28–29). Mô hình spline do đó bỏ qua phần giá trị kinh tế bổ sung rất lớn phát sinh từ việc cho vay chứng khoán trên thị trường repo đặc thù (specials repo) đối với các mã trái phiếu khan hiếm, cũng như chi phí đắt đỏ khi phải bán khống các tài sản này [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]]. Về mặt lý thuyết, việc hiệu chỉnh spline trên giá kỳ hạn có tính lãi suất repo sẽ giải quyết được sai lệch này, nhưng sự thiếu minh bạch của thị trường repo kỳ hạn dài khiến phương pháp này hiếm khi được thực thi trong thực tế.

Các nhà giao dịch chuyên nghiệp phân biệt rõ ràng giữa hai tầng nhận thức: sai lệch định giá vi mô tạm thời (temporary misalignment) và giá trị đầu tư cơ bản dài hạn (fundamental value) (fixed_income_during, Ch.32, Sec.32.1, d.30–32). Việc quan sát thấy một trái phiếu ngân hàng tái thiết Đức KfW giao dịch ở mức cao hơn 2 điểm cơ bản so với đường cong spline KfW chỉ xác nhận rằng mã trái phiếu đó đang rẻ hơn tương đối so với các trái phiếu KfW khác trong ngắn hạn để thiết lập vị thế giao dịch chênh lệch [[bond-relative-value-strategies-combine-directional-spreads-with-multi-contract-futures-hedging]]. Nhận định này hoàn toàn không đồng nghĩa với việc trái phiếu đó là một khoản đầu tư hấp dẫn dài hạn, vì quyết định đầu tư cơ bản bắt buộc phải xem xét sự tương quan với các tài sản thay thế trong toàn khu vực, triển vọng cung cầu phát hành mới, và cấu trúc dòng tiền vĩ mô của toàn hệ thống.
