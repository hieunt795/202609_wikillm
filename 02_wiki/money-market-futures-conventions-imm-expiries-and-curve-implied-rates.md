---
title: money-market-futures-conventions-imm-expiries-and-curve-implied-rates
type: concept
tags: [fixed-income, money-market, futures, term-structure]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-28
---
Hợp đồng tương lai thị trường tiền tệ (money market futures) là các công cụ phái sinh chuẩn hóa niêm yết trên sàn giao dịch tập trung, cho phép các định chế tài chính phòng hộ rủi ro biến động lãi suất ngắn hạn mà không làm phình to bảng cân đối kế toán (fixed_income_during, Ch.13, Money market futures, d.203–210). Tùy thuộc vào loại tiền tệ cơ sở, các hợp đồng này được chuẩn hóa dưới các tên gọi như Eurodollar (nay chuyển tiếp sang SOFR futures tại CME), Euribor futures (tại ICE/Eurex), Short Sterling futures, hoặc Euroyen futures (fixed_income_during, Ch.13, Money market futures, d.205). Các hợp đồng này thường liên kết với lãi suất tiền gửi liên ngân hàng kỳ hạn 3 tháng, với ngày đáo hạn chính thức rơi vào ngày thứ Tư của tuần thứ ba trong các tháng 3, 6, 9, 12 hàng năm (gọi là các ngày IMM - International Monetary Market) (fixed_income_during, Ch.13, Money market futures, d.205).

Cơ chế định giá và yết giá của hợp đồng tương lai thị trường tiền tệ được chuẩn hóa theo chỉ số giá:
$$P = 100 - r$$
trong đó $r$ là mức lãi suất kỳ hạn 3 tháng biểu thị theo tỷ lệ phần trăm (fixed_income_during, Ch.13, Money market futures, d.207). Cấu trúc yết giá này tạo ra mối quan hệ nghịch đảo giữa giá hợp đồng và lãi suất: khi lãi suất thị trường tăng thì giá hợp đồng tương lai giảm, do đó vị thế mua hợp đồng tương lai (long futures) tương đương về mặt kinh tế với việc nhận lãi suất cố định và trả lãi suất thả nổi (tương tự như vị thế bán thỏa thuận lãi suất kỳ hạn - FRA seller) (fixed_income_during, Ch.13, Money market futures, d.209). Biến động giá nhỏ nhất được phép trên sàn giao dịch gọi là một bước giá (tick), thường bằng $0{,}005$ điểm chỉ số (tương đương $0{,}5$ điểm cơ bản) hoặc $0{,}0025$ điểm chỉ số đối với các hợp đồng ngắn (fixed_income_during, Ch.13, Money market futures, d.209). Với quy mô hợp đồng danh nghĩa chuẩn $N = 1.000.000$ USD (hoặc EUR tương đương), giá trị tiền tệ của một tick (tick value - $\Delta V$) cho kỳ hạn 3 tháng (quy ước 90 ngày trên cơ sở act/360) được tính theo công thức:
$$\Delta V = N \times \text{tick size} \times \frac{90}{360} = 1.000.000 \times 0{,}00005 \times 0{,}25 = 12{,}50 \text{ USD}$$
Mỗi biến động 1 điểm cơ bản ($0{,}01$) của hợp đồng do đó tương ứng với khoản lãi/lỗ $25$ USD trên mỗi hợp đồng (fixed_income_during, Ch.13, Money market futures, d.209). Vào ngày đáo hạn cuối cùng, giá thanh toán xác định bởi sở giao dịch (exchange-determined settlement price - EDSP) được chốt chính xác bằng lãi suất ấn định của chỉ số liên ngân hàng ngày hôm đó, và hợp đồng được thanh toán thuần bằng tiền mặt (cash-settled) thông qua cơ chế bù trừ ký quỹ biến đổi cuối cùng (variation margin) (fixed_income_during, Ch.13, Futures trading basics, d.253).

Hệ thống định danh hợp đồng tương lai tuân thủ một chuỗi quy ước mã hóa kết hợp giữa tài sản cơ sở, mã chữ cái của tháng đáo hạn và chữ số của năm đáo hạn (fixed_income_during, Ch.13, Identification of futures contracts, d.211–250). Trên các nhà cung cấp dữ liệu thị trường, mã tài sản cơ sở có thể có sự khác biệt (ví dụ hợp đồng Euribor là ER trên Bloomberg, Eurodollar là ED, trong khi hợp đồng trái phiếu Bund 10 năm của Eurex là FGBL trên Reuters và RX trên Bloomberg) (fixed_income_during, Ch.13, Identification of futures contracts, d.213). Mã chữ cái đại diện cho 12 tháng giao hàng trong năm tuân thủ bảng mã chuẩn quốc tế:
- Tháng 1: F
- Tháng 2: G
- Tháng 3: H
- Tháng 4: J
- Tháng 5: K
- Tháng 6: M
- Tháng 7: N
- Tháng 8: Q
- Tháng 9: U
- Tháng 10: V
- Tháng 11: X
- Tháng 12: Z
Mẹo ghi nhớ các mã này là viết toàn bộ bảng chữ cái bắt đầu từ chữ F và loại bỏ các chữ cái xuất hiện trong từ 'WORSTIPLY' (fixed_income_during, Ch.13, Identification of futures contracts, d.227). Bốn tháng đáo hạn quý chính của chu kỳ IMM tương ứng với bốn ký tự trọng yếu: H (tháng 3), M (tháng 6), U (tháng 9), Z (tháng 12) (fixed_income_during, Ch.13, Identification of futures contracts, d.241).

Để quản lý các chuỗi hợp đồng trải dài theo đường cong kỳ hạn, thị trường chia các hợp đồng đáo hạn trong từng năm thành các gói màu (color packs) (fixed_income_during, Ch.13, Identification of futures contracts, d.217). Bốn hợp đồng đáo hạn trong năm đầu tiên được gọi là nhóm Trắng (whites), năm thứ hai là Đỏ (reds), năm thứ ba là Xanh lục (greens), năm thứ tư là Xanh lam (blues) (theo quy tắc mô hình màu màn hình RGB tổng hợp ra ánh sáng trắng), tiếp theo là Vàng (golds), Tím (purples), Cam, Hồng, Bạc và Đồng (fixed_income_during, Ch.13, Identification of futures contracts, d.217–229). Ví dụ, hợp đồng đáo hạn vào tháng 3 năm thứ hai được gọi là 'red March'. Đối với phân tích chuỗi thời gian, bên cạnh các mã hợp đồng cụ thể (specifics - ví dụ ERM9), các nhà cung cấp dữ liệu xây dựng các chuỗi liên tục theo thứ tự kỳ hạn (serials - ví dụ ER1 cho hợp đồng gần nhất hay front contract, ER2 cho hợp đồng tiếp theo hay back contract) hoặc theo mức độ thanh khoản tích cực nhất (actives - kết thúc bằng ký tự A như RXA) (fixed_income_during, Ch.13, Identification of futures contracts, d.243–245).

Các mức giá giao dịch của chuỗi hợp đồng tương lai thị trường tiền tệ (futures strip) cung cấp thông tin trực tiếp về kỳ vọng lãi suất kỳ hạn của thị trường kéo dài từ 1 đến 2,5 năm tại Châu Âu/Nhật Bản và lên tới 10 năm tại Hoa Kỳ (fixed_income_during, Ch.13, Identification of futures contracts, d.247). Tuy nhiên, do hợp đồng tương lai được thanh toán lãi/lỗ và ký quỹ hàng ngày (daily marking-to-market), trong khi hợp đồng kỳ hạn thuần túy (FRA) chỉ thanh toán một lần tại ngày đáo hạn, lãi suất ngụ ý từ hợp đồng tương lai luôn cao hơn lãi suất kỳ hạn tương đương một lượng gọi là độ lệch lồi (convexity bias) (fixed_income_during, Ch.13, Convexity adjustment, d.255). Sau khi hiệu chỉnh độ lệch lồi, chuỗi hợp đồng tương lai trở thành đầu vào chủ đạo để tái cấu trúc đường cong lãi suất giao ngay theo phương pháp bootstrapping đệ quy được phân tích chi tiết tại [[spot-and-forward-rate-no-arbitrage-mechanics-and-money-market-term-structure-bootstrapping]] và liên kết với các chiến lược giao dịch spread trong [[outright-curve-and-relative-value-bond-trading-strategies]].
