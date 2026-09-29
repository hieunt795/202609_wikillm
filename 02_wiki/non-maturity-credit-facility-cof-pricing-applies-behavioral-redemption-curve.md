---
title: non-maturity-credit-facility-cof-pricing-applies-behavioral-redemption-curve
type: concept
tags: [alm, ftp, cof, non-maturity-credit, overdraft, credit-cards, behavioral-models, market-1]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-29
---

Các sản phẩm cấp tín dụng không xác định kỳ hạn cố định như hạn mức thấu chi và thẻ tín dụng có đặc thù vận hành hai lớp rủi ro tách biệt: phần hạn mức cam kết chưa giải ngân tiềm ẩn rủi ro thanh khoản ngoại bảng được kiểm soát qua phụ phí dự phòng theo [[contingent-liquidity-charge-prices-undrawn-credit-commitments]], trong khi phần dư nợ đã giải ngân thực tế phải chịu giá bán vốn (COF) nội bảng theo phương pháp mô hình hóa hành vi (vab_ftp_methodology, Điều 6.2.f, d.782–786).

Khi ngân hàng đã xây dựng mô hình hành vi (MHHV) với chuỗi dữ liệu quan sát hành vi khách hàng tối thiểu 5 năm, CFU áp dụng phương pháp Đường cong hoàn trả (Redemption Curve) để bóc tách dư nợ thành phần biến động ngắn hạn ($Non\text{-}CoreOD_i$) và phần dư nợ duy trì ổn định lõi ($1 - Non\text{-}CoreOD_i$) (vab_ftp_methodology, Điều 6.2.f.ii, d.787–796). Lãi suất COF cơ sở được hệ thống xác định hàng ngày bằng công thức bình quân gia quyền (vab_ftp_methodology, Điều 6.2.f.ii, d.791–794, d.810):
$$COF = COF_i \times Non\text{-}CoreOD_i + COF_j \times (1 - Non\text{-}CoreOD_i)$$
Trong đó, $COF_i$ là lãi suất COF tương ứng với kỳ hạn không ổn định $i$, và $COF_j$ là lãi suất COF tương ứng với kỳ hạn ổn định $j$ (theo thông lệ quản trị ALM được ALCO ấn định ở mức 6 tháng hoặc 1 năm) (vab_ftp_methodology, Điều 6.2.f.ii, d.797–802).

Trường hợp ngân hàng chưa hoàn thiện mô hình hành vi, phương pháp luận FTP cho phép lựa chọn một trong hai phương án quy ước thận trọng để ấn định kỳ hạn ổn định tính giá COF (vab_ftp_methodology, Điều 6.2.f.ii, d.804–809):
1. **Phương án 1 (Kỳ hạn cấp lại hạn mức)**: Ấn định kỳ hạn tính giá COF theo chu kỳ đánh giá và tái cấp hạn mức tín dụng của sản phẩm, thông thường là 12 tháng (vab_ftp_methodology, Điều 6.2.f.ii, d.807, d.809);
2. **Phương án 2 (Kỳ hạn miễn lãi phạt)**: Ấn định kỳ hạn tính giá COF theo khoảng thời gian khách hàng được miễn lãi hoặc chưa phải chịu lãi suất phạt của sản phẩm, thông thường là 45 ngày đối với thẻ tín dụng; tuy nhiên ALCO phải chủ động cân đối lại lãi suất cho vay vì mức giá FTP kỳ hạn ngắn 45 ngày thường khá thấp (vab_ftp_methodology, Điều 6.2.f.ii, d.808–809).

Đối với các khoản tín dụng không xác định kỳ hạn, phần bù thanh khoản kỳ hạn được ấn định bằng 0% trong suốt thời gian tồn tại của khoản vay (vab_ftp_methodology, Điều 6.2.f.v, d.812). Cơ chế phân tầng hành vi này kết nối chặt chẽ với cấu trúc giá bán vốn tổng thể tại [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] và các giới hạn hành vi bảng cân đối theo [[embedded-behavioral-options-alter-banking-book-cash-flows-subject-to-eba-five-year-cap]].
