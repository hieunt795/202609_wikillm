---
title: credit-spread-risk-in-the-banking-book-csrbb
type: concept
tags: [csrbb, irrbb, credit-spread, banking-regulation, alm]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Rủi ro chênh lệch tín dụng trên Sổ ngân hàng (Credit Spread Risk arising from the Banking Book — CSRBB), còn được gọi là rủi ro chênh lệch tín dụng từ các hoạt động phi kinh doanh, là một danh mục rủi ro độc lập được tách biệt khỏi [[interest-rate-risk-in-the-banking-book-irrbb]] theo quy định an toàn vĩ mô của Cơ quan Giám sát Ngân hàng Châu Âu (EBA) (tata_bank_alm, Ch.1, Types of Interest Rate Risk, d.628; tata_bank_alm, Ch.1, Credit Spread Risk, d.697). Theo định nghĩa chính thức của EBA, CSRBB là rủi ro chịu sự chi phối bởi các biến động trong giá thị trường đối với rủi ro tín dụng, rủi ro thanh khoản và các đặc tính định giá khác của các công cụ tài chính có rủi ro tín dụng thuộc sổ phi kinh doanh, vốn không được bao quát bởi khuôn khổ IRRBB hay các thước đo rủi ro tín dụng vỡ nợ dự kiến và rủi ro nhảy bậc vỡ nợ (jump-to-default risk) (tata_bank_alm, Ch.1, Credit Spread Risk, d.699).

Điểm khác biệt căn bản giữa IRRBB và CSRBB nằm ở nhân tố kích hoạt biến động: trong khi các mô phỏng kịch bản IRRBB tập trung vào sự dịch chuyển của đường cong lợi suất chuẩn phi rủi ro (risk-free yield curves) bỏ qua các phần bù thanh khoản và rủi ro cụ thể của từng thực thể, thì CSRBB lượng hóa tác động khi biên độ [[credit-spread]] và phần bù thanh khoản thị trường nới rộng ra trên các tài sản và khoản nợ của ngân hàng (tata_bank_alm, Ch.1, Liquidity Risk, d.707). Ngay cả khi mặt bằng lãi suất cơ bản của ngân hàng trung ương không thay đổi, sự xói mòn niềm tin thị trường hoặc gia tăng e ngại rủi ro toàn hệ thống vẫn có thể làm suy giảm nghiêm trọng giá trị kinh tế của ngân hàng thông qua CSRBB.

Fidelio Tata dẫn ra một trường hợp minh họa rõ nét về sự độc lập của CSRBB: một ngân hàng cấu trúc lịch quyền chọn mua lại (call schedule) của các tài sản có thể mua lại hoàn toàn trùng khớp với lịch hoàn trả của các khoản nợ có thể mua lại (tata_bank_alm, Ch.1, Credit Spread Risk, d.701). Tuy nhiên, khi xếp hạng tín nhiệm của chính ngân hàng bị hạ bậc hoặc thị trường định giá rủi ro đối tác tăng lên, các nhà đầu tư nợ sẽ chủ động kích hoạt quyền đòi nợ trước hạn (tata_bank_alm, Ch.1, Credit Spread Risk, d.701). Để bù đắp khoản thanh khoản bị rút đi, ngân hàng buộc phải phát hành nợ mới với mức lợi suất cao hơn đáng kể do phần bù rủi ro tín dụng bị thị trường đẩy lên, dẫn đến sự suy giảm biên lợi nhuận lãi thuần và vốn chủ sở hữu dù đường cong lãi suất chính sách hoàn toàn phẳng (tata_bank_alm, Ch.1, Credit Spread Risk, d.701–702).

Do tính chất trung gian giữa rủi ro lãi suất thị trường và [[liquidity-risk]], các hướng dẫn mới nhất của EBA (EBA/GL/2022/14) bắt buộc các định chế tài chính phải xây dựng một khung quản trị và giám sát CSRBB riêng biệt, có phương pháp luận đo lường độc lập với các bài kiểm tra áp lực IRRBB thông thường theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]].
