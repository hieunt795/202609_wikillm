---
title: interbank-tenor-ladder-and-deal-ticket-standardization-enforce-internal-treasury-transfers
type: concept
tags: [alm, ftp, tenor-ladder, deal-tickets, treasury-transfers, profit-center, money-market]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-26
---

Trong công tác điều hòa nguồn vốn nội bộ giữa Đơn vị Quản lý Vốn tập trung (CFU) và Khối Quản lý & Kinh doanh Vốn (Treasury), việc thiết lập kỷ luật thị trường đòi hỏi phải lượng hóa các giao dịch chuyển nhượng vốn nội bộ thông qua các định dạng chứng từ pháp lý và thang kỳ hạn chuẩn mực không khác biệt so với các giao dịch mua bán trên thị trường liên ngân hàng bên ngoài theo [[treasury-business-unit-ftp-governance-balances-desk-level-and-net-portfolio-transfers]] (vab_ftp_methodology, Mẫu biểu 03–07, d.1930–2118). Khung tiêu chuẩn hóa này bao gồm ba trụ cột tác nghiệp cốt lõi: bảng thang kỳ hạn chuẩn, phiếu mua bán vốn nội bộ (Deal Ticket), và báo cáo kết quả kinh doanh phân tách theo từng trung tâm lợi nhuận (Profit Center) (vab_ftp_methodology, Mẫu biểu 03, d.1932; Mẫu biểu 06, d.2068; Mẫu biểu 07, d.2099).

Trụ cột thứ nhất là Thang kỳ hạn mua bán vốn chuẩn trên Thị trường 2 (Mẫu biểu MB03), được phân chia thành 21 dải kỳ hạn kỹ thuật dựa trên số ngày thực tế của giao dịch nhằm bảo đảm mọi thỏa thuận vay mượn vốn giữa Treasury và CFU đều có điểm neo định giá chính xác theo [[interbank-market-2-ftp-curve-construction-relies-on-peer-quotes-and-vnibor]] (vab_ftp_methodology, Mẫu biểu 03, d.1932–1956):
- Dải siêu ngắn: Qua đêm (Overnight — ON) áp dụng cho các giao dịch có số ngày $\le 3$ ngày; 1 tuần ($3 < \text{ngày} \le 10$); 2 tuần ($10 < \text{ngày} \le 17$); 3 tuần ($17 < \text{ngày} \le 24$);
- Dải ngắn hạn: 1 tháng ($24 < \text{ngày} \le 35$); 2 tháng ($35 < \text{ngày} \le 64$); 3 tháng ($64 < \text{ngày} \le 94$); 6 tháng ($94 < \text{ngày} \le 186$); 9 tháng ($186 < \text{ngày} \le 278$);
- Dải trung và dài hạn: 12 tháng ($278 < \text{ngày} \le 365$); tiếp nối là các nấc 13, 14, 15, 18, 24, 36, 48, 60, 72, 84 tháng và kéo dài tối đa đến 120 tháng ($2554 < \text{ngày} \le 4014$) (vab_ftp_methodology, Mẫu biểu 03, d.1945–1956).
Việc phân chia khoảng ngày chặt chẽ triệt tiêu hoàn toàn sự tùy tiện trong việc xếp kỳ hạn, ngăn ngừa việc chọn kỳ hạn để trục lợi chênh lệch lãi suất FTP.

Trụ cột thứ hai là Phiếu mua bán vốn nội bộ trên Thị trường 2 (Mẫu biểu MB06), đóng vai trò là hợp đồng kinh tế nội bộ ràng buộc trách nhiệm pháp lý giữa hai bên giao dịch (vab_ftp_methodology, Mẫu biểu 06, d.2068–2094). Mỗi phiếu giao dịch bắt buộc phải định danh chính xác bên mua và bên bán vốn theo từng Profit Center (Khối QL&KDV hay CFU), đồng thời xác định đầy đủ 7 tham số cốt lõi: số tiền mua bán vốn bằng số và bằng chữ; mức lãi suất chuyển nhượng theo quy ước tính lãi thực tế trên 365 ngày (act/365); kỳ hạn giao dịch (số ngày); ngày giao dịch; ngày giá trị bắt đầu tính lãi; ngày đến hạn hoàn trả vốn; và mục đích giao dịch cụ thể (như cân đối nguồn vốn kinh doanh hoặc tài trợ thanh khoản) (vab_ftp_methodology, Mẫu biểu 06.1–2, d.2070–2088). Phiếu giao dịch chỉ có giá trị hiệu lực kế toán khi có đủ bốn chữ ký kiểm soát chéo: người lập phiếu và cấp duyệt phiếu của Khối QL&KDV, cùng với chữ ký xác nhận của cán bộ CFU và chữ ký phê duyệt cuối cùng của Trưởng bộ phận quản lý FTP theo [[two-tier-ftp-operational-workflows-govern-market-1-and-market-2-cycles]] (vab_ftp_methodology, Mẫu biểu 06.3, d.2090–2094).

Trụ cột thứ ba là Báo cáo tổng hợp mua bán vốn nội bộ trên Thị trường 2 (Mẫu biểu MB07), cho phép Hội đồng ALCO đo lường độc lập kết quả kinh doanh của từng bàn tự doanh trực thuộc Khối Treasury (vab_ftp_methodology, Mẫu biểu 07, d.2099–2107). Báo cáo phân rã thu nhập lãi thuần (NII) và biên lãi thuần (NIM) thành bốn dòng tài khoản độc lập:
1. Bàn Thị trường tiền tệ (Money Market — MM);
2. Bàn Kinh doanh Ngoại hối (FX Desk);
3. Bàn Kinh doanh Trái phiếu (Bond Desk);
4. Toàn bộ Khối QL&KDV tổng hợp (vab_ftp_methodology, Mẫu biểu 07, d.2101–2106).

Nhờ hệ thống chứng từ và thang kỳ hạn chuẩn hóa này, mô hình quản trị của [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]] chuyển hóa các luồng vốn vô hình trong nội bộ thành các giao dịch có thể kiểm toán, đo lường và quy trách nhiệm rõ ràng, bảo đảm tính công bằng tuyệt đối trong việc đánh giá hiệu quả kinh doanh của các đơn vị tạo lập doanh thu.
