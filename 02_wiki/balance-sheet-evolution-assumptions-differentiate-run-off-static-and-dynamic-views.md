---
title: balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views
type: concept
tags: [alm, irrbb, balance-sheet, nii, modeling]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Trong kỹ thuật xây dựng mô hình dự báo [[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]], sự tiến hóa về quy mô và cấu trúc của các vị thế bảng cân đối khi các khoản tiền gửi, nợ vay hoặc hợp đồng phái sinh đáo hạn được định hình thông qua ba góc nhìn giả định: góc nhìn tất toán dần (*run-off view*), góc nhìn tĩnh (*static view*) và góc nhìn động (*dynamic view*) (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1035).

Góc nhìn tất toán dần (Run-off view) là phương pháp đơn giản nhất về mặt khái niệm nhưng phi thực tế nhất trong kinh doanh ngân hàng: mô hình giả định mọi vị thế tài sản và nợ khi đến hạn sẽ tự động biến mất và hoàn toàn không được thay thế bằng các hợp đồng kinh doanh mới (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1037). Dưới góc nhìn này, bảng cân đối của ngân hàng liên tục co cụm lại theo thời gian cho tới khi hoạt động khách hàng chấm dứt hoàn toàn, chỉ phù hợp cho mục đích thanh lý danh mục hoặc phân tích suy giảm tự nhiên (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1037).

Góc nhìn tĩnh (Static view) là mô hình phổ biến nhất và là chuẩn mực bắt buộc trong các báo cáo giám sát thu nhập lãi thuần của Cơ quan Giám sát Ngân hàng Châu Âu (EBA) (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1038–1040). Góc nhìn này vận hành trên giả định hoạt động liên tục (*going concern*): toàn bộ các vị thế hợp đồng đáo hạn — ngoại trừ các vị thế phái sinh phòng hộ của ALM — đều được thay thế tức thì bằng các hợp đồng mới tương đương về loại công cụ, khối lượng số dư, kỳ hạn gốc và biên độ thương mại (*commercial margin*) (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1038–1040). Mức lãi suất của các vị thế thay thế được thiết lập dựa trên mặt bằng lãi suất thị trường hiện hành tại thời điểm tái định giá (cộng hoặc trừ biên độ thương mại ban đầu), giữ cho quy mô và cấu trúc bảng cân đối không đổi theo thời gian (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1040).

Góc nhìn động (Dynamic view) là cấp độ mô hình hóa phức tạp nhất, đưa vào các kịch bản thay đổi chủ động trong tương lai dựa trên kế hoạch kinh doanh (*business plan*) của ngân hàng, bao gồm tốc độ tăng trưởng tín dụng dự kiến, kế hoạch huy động tiền gửi mới, phát hành trái phiếu thứ cấp hoặc điều chỉnh danh mục đầu tư (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1041). Việc kết hợp góc nhìn tĩnh chuẩn hóa theo quy định và góc nhìn động nội bộ giúp ngân hàng kiểm soát chặt chẽ cả ranh giới tuân thủ theo [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]] lẫn chiến lược tối ưu hóa biên lợi nhuận ròng dài hạn theo [[economic-value-and-earnings-perspectives-complement-each-other-in-alm]].
