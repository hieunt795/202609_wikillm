---
title: ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets
type: concept
tags: [yield-curve, relative-value, butterfly-trades, us-treasury, linear-programming, ancillary-curve, risk-neutrality]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Chiến lược giao dịch Butterfly neo theo trái phiếu phụ trợ (Ancillary-Anchored Butterfly Trades) do Kenneth Kortanek và Vladimir Medvedev đề xuất là phương thức khai thác giá trị tương đối trong môi trường thị trường Kho bạc Hoa Kỳ siêu thanh khoản, nơi các cơ hội kinh doanh chênh lệch giá thuần túy (pure arbitrage) gần như đã bị triệt tiêu hoàn toàn (choudhry_analysing_yield_curve, Ch.13, Sec. "A Proposed Butterfly Trade with the Short Position Stemming from the Ancillary Bond...", d.5150–5244; d.5333–5346). So với thập niên 1990 khi các dị biệt định giá cục bộ giữa các mã trái phiếu thường xuyên xuất hiện với biên độ lớn, thị trường Kho bạc hiện đại sở hữu quy mô vốn khổng lồ và độ hiệu quả thông tin cao, khiến việc tìm kiếm các cơ hội đầu tư giá trị tương đối có tỷ lệ sinh lời trên rủi ro hấp dẫn trở thành một bài toán định lượng phức tạp.

Để bóc tách lợi nhuận trong một thị trường hiệu quả cao, nhà đầu tư không thể lựa chọn tùy tiện các trái phiếu trên đồ thị lợi suất mà cần một mỏ neo định giá chuẩn xác để nhận diện các điểm méo mó vi mô [[ancillary-yield-curves-expand-benchmark-definitions-via-strict-irr-admissibility]]. Cấu trúc vị thế Butterfly của Kortanek và Medvedev được thiết lập dựa trên nguyên tắc:
1. Xác định chân trung tâm (body) từ tập Ancillary: Lựa chọn một mã trái phiếu thuộc tập Ancillary bị định giá quá cao (thị giá đắt so với đường cong lý thuyết) để thực hiện bán khống (short position). Trong nghiên cứu thực nghiệm ngày 18/10/2017, mã trái phiếu coupon 1.25% đáo hạn ngày 31/08/2019 (kỳ hạn 1.868 năm, thị giá bẩn dirty price $99.595) được chọn làm vị thế bán khống $M_1$ với quy mô chuẩn hóa 1,000 đơn vị (choudhry_analysing_yield_curve, Ch.13, d.5144, d.5156).
2. Xác định hai chân cánh (wings) phòng hộ: Lựa chọn hai mã trái phiếu $M_2$ và $M_3$ có cùng ngày đáo hạn 31/08/2019 nhưng mang lãi suất coupon khác biệt (mã $M_2$ coupon 1.00%, thị giá $99.123; mã $M_3$ coupon 1.625%, thị giá $100.350) để mở vị thế mua (long positions).

Để cấu trúc danh mục đạt trạng thái miễn nhiễm hoàn toàn trước các biến động thị trường chung, tỷ trọng của hai chân mua ($M_2, M_3$) được xác định thông qua giải một bài toán quy hoạch tuyến tính (Linear Programming - LP) với hai ràng buộc đẳng thức bất biến:
- Ràng buộc trung hòa tiền mặt (Cash Neutrality): Tổng giá trị vốn mua vào của hai chân cánh phải cân bằng đúng bằng số tiền thu được từ việc bán khống chân trung tâm:
$$P_2 M_2 + P_3 M_3 = P_1 M_1$$
- Ràng buộc trung hòa thời lượng và độ nhạy cảm lãi suất (Duration / BPV Neutrality): Tổng thời lượng tiền mặt của hai chân cánh phải triệt tiêu chính xác thời lượng tiền mặt của chân bán khống:
$$(P_2 \cdot MD_2) M_2 + (P_3 \cdot MD_3) M_3 = (P_1 \cdot MD_1) M_1$$
Do ma trận hệ số của hệ phương trình này là một ma trận vuông không suy biến (non-singular matrix), bài toán quy hoạch tuyến tính sở hữu nghiệm duy nhất độc lập với dạng thức của hàm mục tiêu (choudhry_analysing_yield_curve, Ch.13, d.5162–5170). Nghiệm số tối ưu chỉ ra rằng để phòng hộ hoàn hảo cho vị thế bán khống 1,000 đơn vị $M_1$, nhà đầu tư mua vào đúng $304.491$ đơn vị $M_2$ và $691.709$ đơn vị $M_3$ (tổng khối lượng mua hai cánh đạt $996.200$ đơn vị, Bảng 13.7).

Cấu trúc giao dịch này cô lập triệt để phần bù thặng dư coupon và các dị biệt thanh khoản cục bộ [[excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions]], đồng thời triệt tiêu hoàn toàn rủi ro dịch chuyển song song và rủi ro xoay trục bậc một của đường cong lợi suất [[butterfly-and-condor-trades-exploit-curve-curvature-and-differing-market-quoting-conventions]]. Việc neo chân bán khống vào một mã trái phiếu thuộc tập Ancillary có tính thanh khoản cao và liên kết chặt chẽ với đường cong chuẩn giúp kiểm soát hiệu quả chi phí tài trợ repo và hạn chế rủi ro bị ép giá lãi suất đặc biệt (specialness risk) trong suốt thời gian nắm giữ vị thế [[repo-specialness-and-financing-costs-dictate-the-break-even-hurdle-of-curve-spread-trades]].
