---
title: breakeven-inflation-rates-incorporate-hedging-horizons-and-short-term-carry-noise
type: concept
tags: [breakeven-inflation, inflation-expectations, carry, energy-prices, market-microstructure]
sources: [fixed_income_during, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Lạm phát hòa vốn là tỷ lệ lạm phát khiến tỷ suất sinh lời nội bộ của trái phiếu liên kết lạm phát bằng đúng tỷ suất sinh lời của trái phiếu danh nghĩa cùng kỳ hạn (fixed_income_during, Ch.23, Breakeven Inflation, d.216). Mặc dù về mặt lý thuyết, lạm phát hòa vốn thường được coi là thước đo phản ánh kỳ vọng lạm phát dài hạn, trong thực tế chỉ số này bị chi phối bởi cấu trúc thị trường, chân trời phòng hộ và các cú sốc chi phí mang ngắn hạn (fixed_income_during, Ch.23, Price Formation in Inflation-Linked Markets, d.184–196; Breakeven Inflation, d.254–258).

Cơ chế truyền dẫn này xuất phát từ sự tương tác giữa thị trường trái phiếu tiền mặt và thị trường hoán đổi lạm phát (fixed_income_during, Ch.23, Price Formation in Inflation-Linked Markets, d.192–196). Thị trường trái phiếu có khối lượng lưu hành cố định trong khi nhu cầu hấp thụ của nhà đầu tư biến động theo chu kỳ; các nhà giao dịch đầu cơ chịu ràng buộc nghiêm ngặt về hạn mức cắt lỗ, khiến họ không thể nắm giữ các vị thế dài hạn thuần túy dựa trên kỳ vọng xa (fixed_income_during, Ch.23, Price Formation in Inflation-Linked Markets, d.192). Để phòng hộ, các bàn giao dịch mua trái phiếu liên kết lạm phát, trả lãi cố định trên thị trường swap danh nghĩa và trả lạm phát trên thị trường hoán đổi lạm phát (fixed_income_during, Ch.23, Price Formation in Inflation-Linked Markets, d.192).

Hành vi phòng hộ này khiến các hợp đồng hoán đổi lạm phát kỳ hạn xa (tiêu biểu như 5Yx5Y forward) bị lây nhiễm tính mùa vụ và biến động giá năng lượng ngắn hạn, mặc dù các chỉ số kỳ hạn xa không có lý do cơ bản để biến động theo chu kỳ giá dầu (fixed_income_during, Ch.23, Price Formation in Inflation-Linked Markets, d.186, 196–200). Chênh lệch phát sinh giữa kỳ vọng thuần túy và tỷ suất thị trường cấu thành phần bù rủi ro lạm phát, tạo độ lệch đáng kể khi cơ quan quản lý sử dụng breakeven rate để đo lường kỳ vọng lạm phát trong [[expected-inflation-is-measured-through-surveys-econometric-models-and-tips-spreads]] và kết nối với chi phí tài trợ carry tại [[real-short-rates-and-inflation-forecasts-determine-the-arbitrage-free-carry-of-inflation-linked-bonds]].

Bên cạnh yếu tố cấu trúc vi mô, Choudhry chỉ ra giới hạn lý thuyết cốt lõi của thước đo breakeven truyền thống: việc so sánh đơn giản giữa lợi suất đáo hạn danh nghĩa và thực chỉ cung cấp mức lạm phát kỳ vọng trung bình gộp từ hiện tại đến ngày đáo hạn, làm phẳng hoàn toàn cấu trúc thời gian của lạm phát (choudhry_analysing_yield_curve, Ch.7, The Real Term Structure of Interest Rates, d.3358–3364). Để bóc tách kỳ vọng lạm phát biên không bị nhiễu theo từng năm riêng biệt trong tương lai, thị trường chuyển đổi sang xây dựng cấu trúc kỳ hạn lạm phát tức thời tại [[implied-forward-inflation-curves-isolate-marginal-inflation-expectations-via-fisher-identity]], đồng thời xử lý triệt để sai số dòng tiền do độ trễ chỉ số hóa tại [[indexation-lags-require-iterative-consistency-procedures-in-real-term-structure-estimation]].

