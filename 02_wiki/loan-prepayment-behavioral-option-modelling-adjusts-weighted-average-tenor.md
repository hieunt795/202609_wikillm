---
title: loan-prepayment-behavioral-option-modelling-adjusts-weighted-average-tenor
type: concept
tags: [alm, ftp, cof, prepayment-options, behavioral-models, wat, cpr, embedded-options, market-1]
sources: [vab_ftp_methodology]
status: draft
last_updated: 2026-09-27
---

Quyền chọn trả nợ trước hạn (prepayment option) cho phép bên vay đơn phương thanh toán một phần hoặc toàn bộ số dư nợ gốc trước ngày đáo hạn thỏa thuận, làm co hẹp thời lượng thực tế của tài sản có và đẩy rủi ro tái đầu tư bất lợi về phía ngân hàng khi mặt bằng lãi suất thị trường sụt giảm (vab_ftp_methodology, Điều 6.3.b, d.962–965). Để ngăn chặn tình trạng bốc hơi phần bù thanh khoản kỳ hạn mà khối Treasury đã cam kết tài trợ, phương pháp luận FTP triển khai kỹ thuật mô hình hóa hành vi nhằm điều chỉnh lại Kỳ hạn hiệu lực (Weighted Average Tenor — WAT) dùng để ấn định giá bán vốn (COF) (vab_ftp_methodology, Điều 6.3.b.i, d.965).

Khi ngân hàng ứng dụng mô hình hành vi (MHHV) tất toán trước hạn dựa trên tỷ lệ trả nợ trước hạn có điều kiện (CPR), CFU thực hiện tái dự phóng toàn bộ cấu trúc dòng tiền hoàn vốn của khoản vay bao gồm cả các dòng tiền trả nợ định kỳ theo lịch trình và các dòng tiền trả trước ước tính (vab_ftp_methodology, Điều 6.3.b.i, d.965, d.977–978). Kỳ hạn hiệu lực điều chỉnh hành vi được tính toán theo phương pháp bình quân gia quyền (vab_ftp_methodology, Điều 6.3.b.i, d.965–974):
$$WAT_{\text{hành vi}} = \frac{\sum_{i=1}^N (P_i \times T_i)}{\sum_{i=1}^N P_i}$$
trong đó $N$ là tổng số lượt dòng tiền trả theo lịch và dòng tiền trả trước ước tính, $P_i$ là số dư gốc hoàn trả tương ứng trong lần thứ $i$, và $T_i$ là khoảng thời gian tính bằng số ngày từ ngày giải ngân đến ngày thanh toán lần thứ $i$ (vab_ftp_methodology, Điều 6.3.b.i, d.977–979). Mức lãi suất COF cơ sở được xác lập theo kỳ hạn hiệu lực $WAT_{\text{hành vi}}$ đã rút ngắn này và áp dụng từ ngày giải ngân ban đầu (vab_ftp_methodology, Điều 6.3.b.ii, d.981–982).

Trường hợp ngân hàng chưa xây dựng mô hình hành vi trả trước hạn, CFU áp dụng nguyên tắc thận trọng bằng cách ấn định giá COF cơ sở đối ứng trực tiếp theo kỳ hạn gốc pháp lý ban đầu của khoản vay theo [[straight-term-bullet-loan-cof-pricing-decomposes-repricing-and-term-risk]] hoặc kỳ hạn hiệu lực danh nghĩa của [[amortizing-loan-cof-pricing-applies-weighted-average-tenor]] (vab_ftp_methodology, Điều 6.3.b.i, d.980). Dưới góc độ quản trị rủi ro lãi suất trên sổ ngân hàng theo chuẩn mực quốc tế BCBS 368 tại [[standardised-loan-prepayment-modelling-and-cpr-multipliers]], tỷ lệ trả trước hạn cơ sở $CPR_0$ chịu các hệ số nhân từ 1,3 đến 1,6 lần khi xảy ra kịch bản lãi suất giảm mạnh, đòi hỏi hệ thống phụ phí quyền chọn tại [[contingency-liquidity-and-embedded-optionality-require-specialized-ftp-add-ons]] phải tích hợp phí phạt trả nợ trước hạn để bù đắp chi phí hủy bỏ các công cụ phòng hộ thị trường.
