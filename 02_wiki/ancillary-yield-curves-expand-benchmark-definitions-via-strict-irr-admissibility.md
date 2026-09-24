---
title: ancillary-yield-curves-expand-benchmark-definitions-via-strict-irr-admissibility
type: concept
tags: [yield-curve, term-structure, us-treasury, benchmark-curve, ancillary-curve, irr-admissibility, relative-value]
sources: [choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Đường cong phụ trợ (Ancillary Yield Curve) do Kenneth Kortanek và Vladimir Medvedev phát triển là phương pháp bóc tách cấu trúc kỳ hạn nâng cao trên thị trường Kho bạc Hoa Kỳ, mở rộng định nghĩa truyền thống về các chứng khoán chuẩn (benchmarks) thông qua tiêu chí sàng lọc dung nạp sai số tỷ suất sinh lời nội bộ (IRR) nghiêm ngặt (choudhry_analysing_yield_curve, Ch.13, Sec. "Identifying Relative Value in the US Treasury Market: Acquiring New Benchmark Definitions from an Ancillary Yield Curve", d.4948–4953; d.5061–5137). Trong thực tiễn thị trường tài chính, khái niệm "trái phiếu chuẩn" thường bị giới hạn vào một số ít kỳ hạn phát hành mới nhất định (on-the-run) như 2 năm, 5 năm, 10 năm và 30 năm. Tuy nhiên, cách tiếp cận thu hẹp này bỏ qua lượng thông tin phong phú chứa đựng trong hơn 300 mã trái phiếu, tín phiếu và kỳ phiếu kho bạc giao dịch đồng thời trên thị trường.

Để khắc phục nghịch lý giữa nhu cầu bao quát toàn bộ thị trường và yêu cầu độ chính xác định giá, Kortanek và Medvedev thiết lập cơ chế trích xuất đồng thời hai đường cong có tính chất hòa nhập hình học (coalescing yield curves):
1. Đường cong Chuẩn (Benchmark Curve): Được ước lượng trên toàn bộ tập dữ liệu thị trường gồm khoảng 291 đến 310 công cụ nợ chính phủ (bao gồm toàn bộ tín phiếu T-bills và các trái phiếu/kỳ phiếu có kỳ hạn trên 1 năm sau khi đã loại trừ các mã sắp đáo hạn dưới 1 năm).
2. Đường cong Phụ trợ (Ancillary Curve): Được trích xuất từ một tập hợp con tinh giản gồm toàn bộ 33 tín phiếu T-bills kết hợp với các trái phiếu và kỳ phiếu thỏa mãn điều kiện dung nạp sai số định giá tối thiểu.

Tiêu chuẩn dung nạp (admissibility criterion) đòi hỏi mỗi trái phiếu được lựa chọn phải có tỷ suất sinh lời nội bộ được tính bằng giải thuật Newton-Raphson (Newton-Raphson IRR) bám sát mức lợi suất chào mua công bố trên thị trường (Ask Yield / Bond Equivalent Yield) với sai lệch không vượt quá 1 điểm cơ bản ($0.010\%$):
$$|\text{IRR}_{\text{Newton}} - \text{AskYld}_{\text{WSJ}}| \le 0.010\%$$
Trong dữ liệu thực nghiệm ngày 18/10/2017, thuật toán sàng lọc đã chọn ra đúng 29 mã trái phiếu đạt chuẩn từ tổng số 258 trái phiếu/kỳ phiếu lưu hành, hợp thành tập mẫu Ancillary gồm 62 công cụ (choudhry_analysing_yield_curve, Ch.13, d.5136–5141).

Mặc dù sử dụng số lượng công cụ ít hơn đáng kể so với tập mẫu toàn diện, đường cong Ancillary đạt chỉ số sai số phần trăm tuyệt đối trung bình (Mean Absolute Percentage Error - MAPE) là $0.0061\%$, vượt trội rõ rệt so với mức sai số $0.0329\%$ của Benchmark Curve (choudhry_analysing_yield_curve, Ch.13, d.5148–5149). Việc đường cong Ancillary hòa nhập hoàn hảo về mặt thị giác với đường cong Benchmark trong khi sở hữu độ chính xác định giá cao hơn gấp năm lần chứng minh rằng các chứng khoán thuộc tập Ancillary có mối liên kết cấu trúc chặt chẽ và chuẩn xác hơn với đường cong lợi suất thực chất của nền kinh tế. Phát kiến này mở rộng định nghĩa về trái phiếu chuẩn sang các kỳ hạn phi truyền thống (chẳng hạn trái phiếu 2.5 năm thay vì chỉ cố định ở 2 năm), cung cấp mỏ neo định giá vững chắc để nhận diện các cơ hội giá trị tương đối cục bộ [[excess-yield-spreads-isolate-local-relative-value-across-coupon-and-liquidity-dimensions]], thiết lập các tỷ trọng giao dịch spread miễn nhiễm rủi ro định hướng [[bpv-weighted-yield-spread-trading-immunizes-first-order-directional-risk-under-strict-stop-loss-governance]], và triển khai các chiến lược giao dịch butterfly tối ưu hóa [[ancillary-anchored-butterfly-trades-isolate-relative-value-in-hyper-liquid-treasury-markets]].
