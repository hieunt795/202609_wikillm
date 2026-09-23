---
title: composite-spline-models-prevent-sub-sovereign-curve-crossings-through-spread-decomposition
type: concept
tags: [yield-curve, sub-sovereign, spline-models, fixed-income]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Việc định giá các phân khúc nợ cận quốc gia như trái phiếu chính quyền địa phương hoặc các cơ quan chính phủ thường gặp trở ngại kỹ thuật khi khớp độc lập hai đường cong spline riêng biệt với trái phiếu chính phủ (fixed_income_during, Ch.19, Composite models, d.298–301). Do các tổ chức cận quốc gia có quy mô phát hành hạn chế và số lượng điểm dữ liệu thưa thớt, các thuật toán spline độc lập dễ rơi vào trạng thái quá khớp, dẫn đến hiện tượng phi lý kinh tế khi đường cong lợi suất cận quốc gia cắt xuống dưới đường cong nợ chính phủ ở một số phân đoạn kỳ hạn (fixed_income_during, Ch.19, Composite models, d.300–301).

Các tổ chức tài chính xử lý khiếm khuyết này bằng mô hình spline hỗn hợp, phân rã hệ số chiết khấu cận quốc gia thành tích số giữa hệ số chiết khấu thị trường cơ sở và hệ số chiết khấu chênh lệch (fixed_income_during, Ch.19, Composite models, d.302–311). Bằng cách cố định đường cong cơ sở từ trái phiếu chính phủ có thanh khoản cao nhất và chỉ ước lượng thành phần chênh lệch bằng một hàm đa thức bậc thấp có ít tham số, mô hình composite đảm bảo đường cong nợ cận quốc gia luôn nằm trên đường cong cơ sở và phản ánh đúng phần bù rủi ro tín dụng (fixed_income_during, Ch.19, Composite models, d.306–314). Phương pháp này cung cấp công cụ định giá chuẩn xác cho các cấu trúc nợ địa phương được phân tích trong [[joint-and-several-sovereign-liability-creates-moral-hazard-prohibited-by-eu-no-bailout-clause]], kế thừa kỹ thuật từ [[parametric-spline-models-trade-off-exact-repricing-against-forward-rate-smoothness]], và củng cố trật tự truyền dẫn giá trong [[fixed-income-price-discovery-transmits-hierarchically-from-liquid-benchmarks-to-illiquid-securities]]. Đồng thời, phương pháp luận phân tách và xếp chồng hệ số chiết khấu này được mở rộng trực tiếp sang mô hình định giá nợ liên kết lạm phát tại [[comprehensive-inflation-models-stack-seasonally-adjusted-inflation-dynamics-onto-nominal-discount-curves|mô hình lạm phát toàn diện xếp chồng động học lạm phát thực lên đường cong danh nghĩa]].
