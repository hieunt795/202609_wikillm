---
title: lagged-compounded-overnight-rates-lack-term-risk-premia-and-delay-policy-transmission
type: concept
tags: [reference-rates, monetary-policy-transmission, rfr, ois]
sources: [fixed_income_during]
status: draft
last_updated: 2026-09-23
---

Việc áp dụng lãi suất qua đêm dồn lãi có độ trễ (lagged compounded overnight rates) để thay thế lãi suất kỳ hạn IBOR trong các hợp đồng tín dụng và thế chấp bộc lộ nhược điểm cơ bản: chuỗi bình quân số học của lãi suất qua đêm hoàn toàn không chứa phần bù rủi ro kỳ hạn (term risk premium) (fixed_income_during, Ch.13, Benchmark Reform, d.191–197). Trong khi các định chế tài chính lớn có thể sử dụng hợp đồng hoán đổi chỉ số qua đêm (Overnight Index Swap - OIS) để phòng ngừa rủi ro biến động, các hộ gia đình vay mua nhà và doanh nghiệp nhỏ cần biết trước số tiền lãi phải trả vào đầu kỳ tính lãi (fixed_income_during, Ch.13, Benchmark Reform, d.185, d.191).

Cơ chế tính lãi dồn tích qua đêm quan sát chuỗi lãi suất trong khoảng thời gian $p$ và áp dụng độ trễ $l$ nhằm công bố mức lãi suất áp dụng trước thời điểm thanh toán (fixed_income_during, Ch.13, Benchmark Reform, d.191–195). Tuy nhiên, việc kéo dài thời gian quan sát $p$ không tạo ra phần bù kỳ hạn thực sự, vì phép tính trung bình chỉ đơn thuần làm phẳng các biến động của lãi suất qua đêm vốn không hàm chứa bất kỳ phần bù kỳ hạn nào (fixed_income_during, Ch.13, Benchmark Reform, d.197). Do đó, sự liên hệ kinh tế giữa chu kỳ bình quân $p$ và kỳ hạn tín dụng thực tế hoàn toàn bị triệt tiêu, buộc bên cho vay phải chủ động cộng thêm một biên độ lợi nhuận riêng biệt để bù đắp rủi ro kỳ hạn (fixed_income_during, Ch.13, Benchmark Reform, d.197).

Đối với ngân hàng trung ương, các hợp đồng sử dụng lãi suất dồn lãi có độ trễ làm phát sinh độ trễ truyền dẫn chính sách khoảng $p/2 + l$, khiến các quyết định điều chỉnh lãi suất chính sách tác động chậm hơn vào chi phí vay nợ thực tế so với cơ chế tái thiết lập tức thì của chuẩn IBOR cũ (fixed_income_during, Ch.13, Benchmark Reform, d.199). Hạn chế này thúc đẩy thị trường tài chính hoàn thiện cơ chế thị trường OIS và chuẩn hóa [[overnight-risk-free-rates-replace-ibor-benchmarks-through-transaction-volume|các chuẩn lãi suất phi rủi ro qua đêm]] nhằm tối ưu hóa sự phối hợp với [[monetary-policy|chính sách tiền tệ]].
