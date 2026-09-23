---
title: futures-convexity-adjustment-arises-from-daily-variation-margining-cash-flows
type: concept
tags: [futures, derivatives, convexity, money-market, interest-rates]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Khoản điều chỉnh lồi (convexity adjustment) trên thị trường hợp đồng tương lai ngắn hạn phản ánh sự sai lệch giữa lãi suất hàm ý từ giá hợp đồng tương lai so với kỳ vọng lãi suất thực tế trong tương lai, phát sinh từ cơ chế ký quỹ biến đổi hàng ngày (daily variation margining) (fixed_income_during, Ch.13, Convexity Adjustment, d.271–274). Về mặt lý thuyết thuần túy, hợp đồng tiền gửi có đường giá lồi tự nhiên theo lãi suất (đạo hàm bậc hai dương), trong khi công thức định giá của hợp đồng tương lai thị trường tiền tệ (như Eurodollar hay Euribor futures) có dạng tuyến tính hoàn toàn (fixed_income_during, Ch.13, Convexity Adjustment, d.257–270).

Tuy nhiên trong thực tế giao dịch, nghĩa vụ thanh toán lãi lỗ hàng ngày bằng tiền mặt tạo ra độ lồi thực tế cho vị thế hợp đồng tương lai (fixed_income_during, Ch.13, Convexity Adjustment, d.271). Khi lãi suất thị trường tăng, giá hợp đồng tương lai giảm buộc nhà đầu tư giữ vị thế mua phải nộp thêm tiền ký quỹ và phải huy động vốn tài trợ khoản nộp này ở mức lãi suất cao mới (fixed_income_during, Ch.13, Convexity Adjustment, d.271). Ngược lại, khi lãi suất giảm, nhà đầu tư nhận tiền ký quỹ giải tỏa nhưng chỉ có thể tái đầu tư lượng tiền mặt đó ở mức lãi suất thấp (fixed_income_during, Ch.13, Convexity Adjustment, d.271). Sự bất đối xứng trong việc vay nợ ở lãi suất cao và tái đầu tư ở lãi suất thấp buộc các nhà giao dịch chỉ mua hợp đồng tương lai khi mức lãi suất hàm ý cao hơn kỳ vọng lãi suất thị trường một khoản bù trừ rủi ro (fixed_income_during, Ch.13, Convexity Adjustment, d.273).

Khoản điều chỉnh lồi được tính xấp xỉ bằng $\frac{1}{2}\sigma^2 t^2$, tăng tỷ lệ bậc hai theo thời gian đáo hạn $t$ và độ biến động lãi suất $\sigma$ (fixed_income_during, Ch.13, Convexity Adjustment, d.275–277). Cơ chế này liên kết trực tiếp với [[ccp-waterfall-protects-clearing-houses-through-margining-default-funds-and-mandatory-bidding|thác bảo vệ và cơ chế ký quỹ biến đổi của CCP]], đồng thời giữ vai trò then chốt trong việc xây dựng đường cong chiết khấu chuẩn hóa song hành cùng [[xva-adjustments-reconcile-unmargined-otc-derivatives-with-cleared-market-prices|các khoản điều chỉnh định giá phái sinh xVA]].
