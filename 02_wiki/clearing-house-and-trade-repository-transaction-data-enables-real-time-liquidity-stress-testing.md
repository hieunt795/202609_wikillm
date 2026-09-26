---
title: clearing-house-and-trade-repository-transaction-data-enables-real-time-liquidity-stress-testing
type: concept
tags: [liquidity-risk, stress-testing, csd, trade-repository, bcb-brazil, supervisory-stress-testing]
sources: [insights_59]
status: draft
last_updated: 2026-09-26
---

Hạ tầng dữ liệu giao dịch từ trung tâm lưu ký chứng khoán và kho dữ liệu báo cáo giao dịch (CSD and trade repository transaction data) cho phép cơ quan quản lý thực hiện kiểm tra sức chịu đựng thanh khoản ở tần suất hàng ngày (near real-time high-frequency stress testing), thay vì phải phụ thuộc vào các báo cáo giám sát định kỳ hàng tháng hay hàng quý có độ trễ lớn (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.160–185).

Mô hình này được Ngân hàng Trung ương Brazil (Banco Central do Brasil — BCB) triển khai với độ chi tiết cao, khai thác trực tiếp dữ liệu đăng ký hợp đồng và lưu ký tài sản từ các trung tâm thanh toán bù trừ tập trung (CSDs) và cơ sở báo cáo giao dịch (TRs) để theo dõi toàn bộ các vị thế repo, chứng chỉ tiền gửi và các công cụ phái sinh ngoài sàn (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.160–174). Trên cơ sở dữ liệu vi mô này, BCB tính toán Chỉ số Thanh khoản ngắn hạn (Short-term Liquidity Index — IL) trên chân trời 21 ngày làm việc:
$$IL = \frac{\text{Adjusted Liquid Assets}}{\text{Stressed Net Outflows}}$$
trong đó quy mô tài sản thanh khoản được chiết khấu theo mô hình Giá trị chịu rủi ro (VaR 95%, 21 ngày) nhằm phản ánh sát thực rủi ro sụt giảm giá trị tài sản khi thanh lý trong điều kiện thị trường căng thẳng [[simultaneous-funding-and-market-liquidity-stress-drives-exposure-valuation-haircuts]] (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.175–182).

Đặc biệt, việc nắm giữ dữ liệu luồng giao dịch tập trung cho phép BCB định lượng chuẩn xác rủi ro bước vào can thiệp (Step-in Risk) đối với các quỹ đầu tư liên kết (sponsored mutual funds) [[reputational-risk-and-off-balance-sheet-vehicles-mandate-step-in-risk-stress-testing]]: khi các quỹ đầu tư do ngân hàng quản lý bị nhà đầu tư rút vốn ồ ạt, ngân hàng bảo trợ thường chịu áp lực danh tiếng phải mua lại tài sản hoặc cung cấp thanh khoản cứu trợ khẩn cấp (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.180–185). Phương pháp này giúp nâng cấp các công cụ giám sát thanh khoản truyền thống [[basel-iii-liquidity-risk-monitoring-tools-complement-contractual-and-market-oversight]] lên một hệ thống cảnh báo sớm chủ động, đa chiều và cập nhật tức thì [[supervisory-stress-testing-framework-enforces-pillar-2-capital-add-ons-and-common-scenarios]].
