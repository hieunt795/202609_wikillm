---
title: key-rate-duration-isolates-interest-rate-sensitivity-to-non-parallel-yield-curve-shifts
type: concept
tags: [duration, key-rate-duration, partial-duration, yield-curve, irrbb]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-09-23
---

Độ nhạy lãi suất điểm then chốt (Key Rate Duration), còn được gọi là độ nhạy cục bộ (partial duration), là một bước phát triển kỹ thuật quan trọng nhằm khắc phục giả định hạn chế của các thước đo độ nhạy truyền thống như Macaulay duration và modified duration (tata_bank_alm, Ch.1, Duration, d.731). Trong khi Macaulay duration — được biểu diễn trực quan như điểm tựa thăng bằng (*fulcrum*) trên đòn bẩy chịu tải các dòng tiền chiết khấu — và modified duration đều giả định ngầm rằng toàn bộ đường cong lợi suất sẽ dịch chuyển song song đồng đều, thì key rate duration loại bỏ hoàn toàn giả định phi thực tế này (tata_bank_alm, Ch.1, Duration, d.721; tata_bank_alm, Ch.1, Duration, d.731).

Key rate duration đo lường độ nhạy cảm giá của một công cụ tài chính hoặc một danh mục bảng cân đối trước một cú sốc dịch chuyển cô lập tại một điểm kỳ hạn then chốt cụ thể (chẳng hạn như kỳ hạn 3 tháng, 1 năm, 2 năm, 5 năm hoặc 10 năm), trong khi giữ nguyên lãi suất tại toàn bộ các điểm kỳ hạn còn lại trên đường cong (tata_bank_alm, Ch.1, Duration, d.731). Bằng cách bóc tách độ nhạy thành một véc-tơ các hệ số cục bộ, thước đo này cho phép bộ phận ALM nhận diện chính xác phân đoạn nào trên đường cong lợi suất tạo ra tác động rủi ro lớn nhất đối với giá trị kinh tế của ngân hàng (tata_bank_alm, Ch.1, Duration, d.754).

Trong quản trị rủi ro lãi suất hiện đại, key rate duration đóng vai trò then chốt trong việc lượng hóa các cú sốc biến dạng đường cong phi song song (*non-parallel shifts*), bao gồm các hiện tượng dốc hóa (steepener), phẳng hóa (flattener) hoặc biến đổi độ cong (curvature) (tata_bank_alm, Ch.1, Duration, d.754). Các hướng dẫn của Cơ quan Giám sát Ngân hàng Châu Âu (EBA) yêu cầu các tổ chức tín dụng phải sử dụng độ nhạy cục bộ để nhận diện bản chất phi song song của [[interest-rate-gap-risk-stems-from-repricing-timing-mismatches]], qua đó đánh giá mức độ phân tán và tập trung rủi ro của các khe hở tái định giá phân bổ dọc theo các dải thời gian (tata_bank_alm, Ch.1, Interest Rate Gap Risk, d.637).

Thước đo này bổ khuyết toàn diện cho [[modified-duration-and-pvbp-measure-investor-interest-rate-risk-across-differing-capital-bases]], cung cấp cơ sở dữ liệu định lượng chính xác để ngân hàng vượt qua các bài kiểm tra áp lực đường cong phi tuyến trong khuôn khổ [[supervisory-outlier-test-applies-six-interest-rate-shock-scenarios-against-tier-one-capital]].
