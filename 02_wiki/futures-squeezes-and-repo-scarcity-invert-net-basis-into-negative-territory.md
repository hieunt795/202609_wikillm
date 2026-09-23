---
title: "Futures Squeezes and Repo Scarcity Invert Net Basis into Negative Territory"
type: concept
tags:
  - derivatives
  - bond-futures
  - futures-squeeze
  - net-basis
  - repo-scarcity
  - implied-repo-rate
  - market-stress
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Mối quan hệ định giá chặt chẽ giữa hợp đồng tương lai và thị trường trái phiếu giao ngay có thể bị gián đoạn thông qua hai hiện tượng phân ly (decoupling) riêng biệt: sự phân ly giữa giá hợp đồng tương lai và giá kỳ hạn phi trọng tài của trái phiếu rẻ nhất để giao nộp (Cheapest-to-Deliver - CTD), và sự phân ly giữa chính trái phiếu CTD với phần còn lại của đường cong lợi suất giao ngay (fixed_income_during, Ch.28, Sec.28.6, d.419–444). Dạng phân ly thứ hai thường xuyên xảy ra trong các giai đoạn căng thẳng thanh khoản khi giới đầu tư tháo chạy vào công cụ có thanh khoản cao nhất là hợp đồng tương lai, khiến trái phiếu CTD bị biến dạng định giá so với các trái phiếu lân cận trên mô hình đường cong spline [[spline-spread-dispersion-measures-indirect-arbitrage-capacity-without-trading-bias]]. Điển hình là thị trường trái phiếu chính phủ Nhật Bản (JGB), nơi các quỹ đầu tư toàn cầu sử dụng hợp đồng tương lai JGB như một tài sản ủy nhiệm (proxy) để duy trì tỷ trọng bắt buộc trong các chỉ số nợ toàn cầu mà không phải nắm giữ tiền mặt sinh lời âm; hành vi mua phi định giá này tạo ra trạng thái đắt đỏ mang tính cấu trúc (structural richness) của hợp đồng tương lai JGB so với các trái phiếu cơ sở (fixed_income_during, Ch.28, Sec.28.6, d.429–444).

Ngược lại, dạng phân ly thứ nhất — khi hợp đồng tương lai tăng giá vượt trội so với giá trị kỳ hạn của CTD — là biểu hiện điển hình của hiện tượng ép giá hợp đồng tương lai (futures squeeze) (fixed_income_during, Ch.28, Sec.28.7, d.445–466). Do khối lượng vị thế mở (open interest) trên các sàn giao dịch tương lai thường xuyên vượt gấp nhiều lần tổng quy mô lưu hành thực tế của mã trái phiếu CTD, thị trường luôn tiềm ẩn nguy cơ thiếu hụt nguồn cung chứng khoán giao nộp nếu có một định chế lớn kiên quyết yêu cầu nhận chuyển giao vật chất [[futures-delivery-windows-confer-timing-options-governed-by-carry-sign-and-repo-fails-risk]]. Trong thực tế vi cấu trúc, một cuộc ép giá không nhất thiết phải mua đứt toàn bộ trái phiếu trên thị trường giao ngay; thay vào đó, bên thực hiện ép giá gom sạch nguồn cung CTD thông qua thị trường mua lại repo đặc thù (specials repo) [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]]. Khi bên bán khống hợp đồng tương lai không thể mượn được CTD trên thị trường repo để thực hiện nghĩa vụ giao nhận, họ buộc phải đối mặt với lựa chọn giao nộp trái phiếu rẻ thứ nhì (next-to-CTD) với mức chi phí tốn kém hơn nhiều, hoặc chấp nhận tất toán vị thế bán khống hợp đồng tương lai tại mức giá cắt cổ do bên mua áp đặt (fixed_income_during, Ch.28, Sec.28.7, d.451–458).

Tín hiệu kinh tế học rõ ràng nhất phản ánh nguy cơ xảy ra hiện tượng ép giá là sự đảo chiều của chênh lệch giá thuần (Net Basis) của trái phiếu CTD sang vùng giá trị âm:

$$\text{Net Basis}_{\text{CTD}} < 0$$

Trong điều kiện thị trường phi trọng tài bình thường, Net Basis của CTD luôn dương nghiêm ngặt để phản ánh giá trị của quyền chọn hoán đổi chất lượng [[bond-futures-basis-and-implied-repo-rate-quantify-arbitrage-free-cash-and-carry-relationships]]. Khi khả năng ép giá xuất hiện, hợp đồng tương lai tăng giá đột biến khiến Net Basis chuyển sang âm, đồng nghĩa với việc cơ chế kinh doanh chênh lệch giá tiền mặt - kỳ hạn (cash-and-carry) bị tê liệt hoàn toàn (fixed_income_during, Ch.28, Sec.28.7, d.459–462). Đồng thời, mức Net Basis âm này chuyển hóa thành một mức lãi suất mua lại ngụ ý (Implied Repo Rate - IRR) tăng vọt vượt xa lãi suất repo kỳ hạn thông thường trên thị trường. Sự tăng vọt của IRR phản ánh rủi ro thất bại giao nhận trên thị trường repo [[securities-settlement-fails-are-disciplined-by-fails-charges-and-cured-through-repo-or-buy-ins]]: các bên bán thà chấp nhận trả chi phí lãi suất tài trợ rất cao hoặc sử dụng các nguồn vốn vay tín chấp, thậm chí tìm kiếm các cửa sổ tái cấp vốn khẩn cấp của ngân hàng trung ương, còn hơn là chịu các án phạt kỷ luật nặng nề từ việc thất bại giao hàng đối với sở giao dịch phái sinh (fixed_income_during, Ch.28, Sec.28.7, d.461–462).

Dù mang lại tiềm năng lợi nhuận lớn cho bên thực hiện, các chiến dịch ép giá hợp đồng tương lai sở hữu tính chất tự bất ổn định cao (inherently unstable) (fixed_income_during, Ch.28, Sec.28.7, d.463–466). Việc thâu tóm và duy trì một khối lượng trái phiếu giao ngay khổng lồ đòi hỏi năng lực bảng cân đối kế toán cực lớn và đối mặt với các hạn mức vị thế nghiêm ngặt từ cơ quan quản lý và sở giao dịch. Hơn nữa, nếu chiến lược ép giá có sự tham gia của nhiều quỹ đầu cơ cùng lúc, chiến lược này sẽ sụp đổ nhanh chóng do nghịch lý kẻ ăn theo (free-rider problem): định chế đầu tiên bí mật thoát vị thế và thanh lý trái phiếu vào thị trường sẽ hiện thực hóa mức lợi nhuận cao nhất, trong khi việc thanh lý này lập tức kích hoạt sự lao dốc không phanh của giá hợp đồng tương lai và đẩy những bên tham gia còn lại vào cảnh thua lỗ nặng nề (fixed_income_during, Ch.28, Sec.28.7, d.463–464).
