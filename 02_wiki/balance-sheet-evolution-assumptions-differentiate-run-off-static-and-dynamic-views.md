---
title: balance-sheet-evolution-assumptions-differentiate-run-off-static-and-dynamic-views
type: concept
tags: [alm, irrbb, balance-sheet, nii, modeling]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
drives: [net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]
related: [net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]
---

Trong kỹ thuật xây dựng mô hình dự báo [[net-interest-income-forecast-serves-as-baseline-for-prospective-alm-simulations]], sự tiến hóa về quy mô và cấu trúc của các vị thế bảng cân đối khi các khoản tiền gửi, nợ vay hoặc hợp đồng phái sinh đáo hạn được định hình thông qua ba góc nhìn giả định: góc nhìn tất toán dần (*run-off view*), góc nhìn tĩnh (*static view*) và góc nhìn động (*dynamic view*) (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1035).

Góc nhìn tất toán dần (Run-off view) là góc nhìn đơn giản nhất về mặt khái niệm nhưng có lẽ kém thực tế nhất: mô hình giả định mọi vị thế tài sản và nợ khi đến hạn sẽ tự động biến mất và hoàn toàn không được thay thế bằng các hợp đồng kinh doanh mới (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1037). Dưới góc nhìn này, bảng cân đối của ngân hàng liên tục co cụm lại theo thời gian cho tới khi hoạt động với khách hàng không còn (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1037).

Góc nhìn tĩnh (Static view) phổ biến hơn góc nhìn tất toán dần và cũng là yêu cầu quy định đối với báo cáo NII (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1038–1040). Góc nhìn này vận hành trên giả định hoạt động liên tục (*going concern*): toàn bộ các vị thế hợp đồng đáo hạn — ngoại trừ các vị thế phái sinh phòng hộ của ALM — đều được thay thế tức thì bằng các hợp đồng mới tương đương về loại công cụ, khối lượng số dư, kỳ hạn gốc và biên độ thương mại (*commercial margin*) (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1038–1040). Mức lãi suất của các vị thế thay thế được thiết lập dựa trên mặt bằng lãi suất thị trường hiện hành tại thời điểm tái định giá (cộng hoặc trừ biên độ thương mại ban đầu), giữ cho quy mô và cấu trúc bảng cân đối không đổi theo thời gian (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1040).

Góc nhìn động (Dynamic view) là cấp độ mô hình hóa phức tạp nhất, đưa vào các kịch bản thay đổi chủ động trong tương lai dựa trên kế hoạch kinh doanh (*business plan*) của ngân hàng, gồm thay đổi trong kinh doanh với khách hàng, phát hành nợ và các hoạt động khác (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1041). Tata bàn kỹ hơn về góc nhìn động ở phần lập kế hoạch NII, tương ứng với trang [[net-interest-income-planning-integrates-volume-run-off-and-margin-beta-across-horizons]] (tata_bank_alm, Ch.2, Assumptions About the Future Balance Sheet, d.1041).
