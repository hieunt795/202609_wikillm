---
title: long-only-fixed-income-portfolios-cannot-achieve-complete-risk-neutrality
type: concept
tags: [long-only, risk-neutrality, portfolio-constraints, duration-sensitivity, fixed-income-risk]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Ràng buộc chỉ mua (long-only constraint), quy định trọng số danh mục phải hoàn toàn dương ($w_i > 0 \ \forall i$), đặt ra một giới hạn toán học mang tính định chế đối với việc triệt tiêu rủi ro danh mục (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.44–46). Để hệ phương trình trung hòa rủi ro $\sum w_i \partial P_i / \partial v_k = 0$ tồn tại nghiệm khả thi dưới ràng buộc tỷ trọng dương nghiêm ngặt, điều kiện cần tất yếu là phải tồn tại ít nhất hai tài sản có độ nhạy trái dấu đối với từng nhân tố định giá $v_k$, tức $\partial P_i / \partial v_k \cdot \partial P_j / \partial v_k < 0$ (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.52–54).

Trong thị trường thu nhập cố định, điều kiện độ nhạy trái chiều này thực tế là bất khả thi đối với các công cụ nợ tiền mặt truyền thống (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.58). Ngoại trừ một số cấu trúc cực kỳ hiếm hoi (như các trái phiếu thả nổi nghịch đảo inverse floaters), hầu như toàn bộ các trái phiếu đều có độ nhạy lãi suất cùng dấu: khi mặt bằng lãi suất tăng, giá trị hiện tại của các dòng tiền coupon và gốc cố định đều giảm xuống (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.58). Do thiếu vắng các tài sản tiền mặt có độ nhạy âm tự nhiên để bù trừ trực tiếp mà không dùng đòn bẩy bán khống, một danh mục trái phiếu chỉ mua thuần túy không bao giờ có thể đạt tới trạng thái hoàn toàn phi rủi ro (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.58).

Đặc tính đồng hướng này của thị trường nợ giải thích vì sao các chiến lược đầu tư phi rủi ro tuyệt đối hoặc danh mục "mọi thời tiết" (all-weather portfolios) bắt buộc phải tích hợp đa dạng các lớp tài sản khác nhau như cổ phiếu và hàng hóa nhằm tìm kiếm các phản ứng ngược chiều trước các cú sốc vĩ mô (fixed_income_during, Ch.35, Risk-Neutral Portfolios, d.58–60). Đối với các quỹ thu nhập cố định thuần túy bị giới hạn bởi ủy thác chỉ mua, mục tiêu quản trị rủi ro không thể là triệt tiêu hoàn toàn rủi ro lãi suất mà chuyển hướng sang tối ưu hóa sai số bám sát (tracking error) so với một chỉ số tham chiếu, dẫn tới kỹ thuật mô phỏng bán phần được trình bày trong [[partial-index-replication-optimizes-tracking-error-against-cash-drag-and-turnover-costs]] và tương tác với các giới hạn phân tích tại [[mean-variance-optimisation-fails-in-fixed-income-due-to-finite-maturity-and-covariance-instability]].
