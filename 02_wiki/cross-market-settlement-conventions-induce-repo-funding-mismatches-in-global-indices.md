---
title: cross-market-settlement-conventions-induce-repo-funding-mismatches-in-global-indices
type: concept
tags: [settlement-conventions, cross-market, repo-financing, global-bond-indices, cash-flow-mismatch]
sources: [fixed_income_during]
status: stable
last_updated: 2026-09-23
---

Việc xây dựng và sao chép các chỉ số trái phiếu toàn cầu đối mặt với sự phân mảnh cố hữu về quy ước thanh toán giữa các thị trường tiền tệ quốc gia (fixed_income_during, Ch.34, Bond Index Principles, d.40). Khi một quỹ đầu tư tái phân bổ vốn giữa các khu vực địa lý, sự lệch pha về chu kỳ thanh toán giao dịch (settlement cycle) tạo ra khoảng trống tài trợ tiền mặt tức thời (fixed_income_during, Ch.34, Bond Index Principles, d.40–44). Điển hình, khi một nhà quản lý bán danh mục trái phiếu chính phủ Nhật Bản (JGB) có chu kỳ thanh toán T+2 để chuyển dịch sang mua trái phiếu Kho bạc Hoa Kỳ (UST) thanh toán theo chu kỳ T+0 hoặc T+1, số tiền bán JGB thu về qua giao dịch hoán đổi ngoại hối (cũng thanh toán T+2) sẽ không sẵn sàng kịp thời để thanh toán nhánh mua UST (fixed_income_during, Ch.34, Bond Index Principles, d.40–44).

Để duy trì tính nhất quán toán học trong việc tính toán lợi suất danh mục tổng thể, các nhà cung cấp chỉ số trái phiếu toàn cầu lựa chọn giải pháp quy ước hóa bằng cách giả định toàn bộ các thị trường thành viên đều thanh toán tại T+0 (fixed_income_during, Ch.34, Bond Index Principles, d.44). Mặc dù giả định đơn giản hóa này khiến hầu hết các dữ liệu phái sinh về giá trái phiếu bị sai lệch kỹ thuật so với thực tế của từng quốc gia riêng lẻ, nó cung cấp một chuẩn đối chuẩn đồng nhất cho các danh mục đa tiền tệ (fixed_income_during, Ch.34, Bond Index Principles, d.44).

Trong hoạt động thực thi thực tế, các nhà quản lý quỹ buộc phải khắc phục sự lệch pha chu kỳ này thông qua các thỏa thuận giao dịch phi tiêu chuẩn hoặc thị trường repo (fixed_income_during, Ch.34, Bond Index Principles, d.44). Bàn giao dịch có thể thương thảo mua UST theo ngày thanh toán chậm T+2, trong đó nhà tạo lập thị trường sẽ nắm giữ và tài trợ lô trái phiếu đó trên thị trường repo trong 1 đến 2 ngày trước khi chuyển giao chính thức cho quỹ (fixed_income_during, Ch.34, Bond Index Principles, d.44). Sự chuyển đổi chi phí ma sát thanh toán thành chi phí tài trợ repo phản ánh tính phụ thuộc mật thiết của thanh khoản danh mục vào cơ chế vay mượn có bảo đảm được phân tích trong [[general-collateral-and-specials-repo-separate-cash-driven-from-collateral-driven-financing]], đồng thời tương tác với cấu trúc chu kỳ thanh toán chuẩn hóa tại [[delivery-versus-payment-eliminates-herstatt-risk-through-intermediary-settlement-cycles]].
