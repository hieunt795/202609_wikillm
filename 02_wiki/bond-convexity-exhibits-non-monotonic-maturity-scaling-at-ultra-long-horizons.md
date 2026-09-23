---
title: bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons
type: concept
tags: [convexity, interest-rate-risk, bond-market]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Độ lồi trái phiếu phản ánh đạo hàm bậc hai của giá bẩn theo lợi suất, lượng hóa độ cong phi tuyến của đường cong giá - lợi suất nhằm hiệu chỉnh sai số cho phép xấp xỉ thời lượng (fixed_income_during, Ch.16, Convexity, d.405–412). Khi phân rã cấu trúc rủi ro theo kỳ hạn, độ lồi đóng góp bởi các khối dòng tiền coupon tăng đều đặn, nhưng phần độ lồi phát sinh từ nợ gốc lại biến thiên phi đơn điệu: đạt đỉnh ở kỳ hạn khoảng 30 năm và suy giảm rõ rệt ở kỳ hạn 40 năm (fixed_income_during, Ch.16, Bond Value Decomposition, d.441–445). Sự đảo chiều này diễn ra do ở kỳ hạn siêu dài, hệ số chiết khấu hiện giá suy giảm theo hàm mũ bắt đầu lấn át mức tăng bậc hai của thời gian đáo hạn, khiến giá trị hiện tại của nợ gốc gần như bị triệt tiêu (fixed_income_during, Ch.16, Bond Value Decomposition, d.443–445).

Mô hình độ lồi truyền thống còn bộc lộ khiếm khuyết khi giả định toàn bộ đường cong lợi suất dịch chuyển song song với biên độ biến động như nhau trên mọi kỳ hạn (fixed_income_during, Ch.16, Convexity, d.415–424). Trên thị trường thực tế, lãi suất ngắn hạn có độ biến động cao hơn nhiều so với lợi suất dài hạn, khiến thước đo độ lồi truyền thống phóng đại mức độ rủi ro lãi suất thực tế của các trái phiếu có kỳ hạn rất dài (fixed_income_during, Ch.16, Convexity, d.421–424). Nhận thức về sự phi tuyến của độ lồi kết nối trực tiếp với cơ chế điều chỉnh dòng tiền ký quỹ hàng ngày trong [[futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows]], đồng thời giải thích hiện tượng [[convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end|thiên lệch độ lồi đè nén lợi suất kỳ hạn dài và gây đảo ngược đoạn siêu dài]] trên đường cong lợi suất. Ngoài ra, sự phi tuyến này cung cấp góc nhìn sâu hơn về tốc độ tái định giá danh mục nợ công theo phân tích tại [[financial-market-duration-repricing-executes-monetary-tightening-on-central-banks-behalf]].
