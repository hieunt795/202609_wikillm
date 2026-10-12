---
title: key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts
type: concept
tags: [duration, key-rate-duration, partial-duration, yield-curve, irrbb]
sources: [tata_bank_alm, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
governs: [interest-rate-gap-risk-stems-from-repricing-timing-mismatches]
contrasts: [modified-duration, modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]
related: [one-factor-term-structure-models-force-perfect-yield-correlation-across-maturities, parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments, supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]
---

Độ nhạy lãi suất điểm then chốt (Key Rate Duration), còn được gọi là độ nhạy cục bộ (partial duration), là thước đo thời lượng không giả định đường cong lợi suất dịch chuyển song song, khác với Macaulay duration và [[modified-duration|modified duration]] (tata_bank_alm, Ch.1, Duration, d.731). Trong khi Macaulay duration — được biểu diễn trực quan như điểm tựa thăng bằng (*fulcrum*) trên đòn bẩy chịu tải các dòng tiền chiết khấu — và modified duration đều giả định ngầm rằng toàn bộ đường cong lợi suất sẽ dịch chuyển song song đồng đều, thì key rate duration không dùng giả định này (tata_bank_alm, Ch.1, Duration, d.721, d.731). Phân tích cấu trúc kỳ hạn chỉ ra rằng giả định song song đòi hỏi toàn bộ các kỳ hạn phải có độ biến động bằng nhau và hệ số tương quan hoàn hảo (+1), cùng điều kiện mà [[one-factor-term-structure-models-force-perfect-yield-correlation-across-maturities|mô hình cấu trúc kỳ hạn một nhân tố]] áp lên các kỳ hạn (choudhry_analysing_yield_curve, Ch.3, The Dynamics of the Yield Curve, d.1843–1844).

Key rate duration đo lường độ nhạy cảm giá của một công cụ tài chính hoặc một danh mục bảng cân đối trước một cú sốc dịch chuyển cô lập tại một điểm kỳ hạn then chốt cụ thể, trong khi giữ nguyên lãi suất tại toàn bộ các điểm kỳ hạn còn lại trên đường cong (tata_bank_alm, Ch.1, Duration, d.731). Độ nhạy cục bộ cho biết phần nào của đường cong lợi suất tác động nhiều nhất tới giá của một công cụ thu nhập cố định (tata_bank_alm, Ch.1, Duration, d.754).

Nó cũng được dùng để ước lượng thay đổi giá khi đường cong dịch chuyển phi song song (*non-parallel shifts*) (tata_bank_alm, Ch.1, Duration, d.754). Các hướng dẫn của Cơ quan Giám sát Ngân hàng Châu Âu (EBA) yêu cầu các tổ chức tín dụng nhận diện [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]] bằng phân tích khe hở theo các dải thời gian, hoặc bằng cách tính độ nhạy cục bộ để xem mức phân tán và tập trung của các khoản lệch giữa các dải (tata_bank_alm, Ch.1, Interest Rate Gap Risk, d.637).

Hai thước đo dùng giả định song song, modified duration và PVBP, nằm ở trang [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]]; trường hợp đường cong dịch chuyển song song nằm ở trang [[parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments|parallel yield curve shifts]]. Bài kiểm tra [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]] có cả kịch bản dốc lên và phẳng đi của đường cong (tata_bank_alm, Ch.5, 5.5.1 IRRBB Assessment, d.2973–2979).
