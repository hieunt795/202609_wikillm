---
title: cash-flow-survival-period-metrics-identify-initial-liquidity-exhaustion-thresholds
type: concept
tags: [liquidity-risk, stress-testing, survival-horizon, ecb-ssm, lcr]
sources: [insights_59]
status: draft
last_updated: 2026-09-26
---

Chỉ số chân trời sinh tồn theo dòng tiền (cash-flow survival period metric) là thước đo định lượng trong kiểm tra sức chịu đựng thanh khoản giám sát nhằm xác định chính xác số ngày hoặc tuần mà một tổ chức tín dụng có thể duy trì hoạt động thanh toán trước khi vùng đệm thanh khoản khả dụng bị cạn kiệt hoàn toàn dưới một kịch bản áp lực định trước (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.246–260).

Về mặt toán học, chỉ số thời gian sinh tồn ($T_{\text{survival}}$) được xác định tại thời điểm đầu tiên mà dòng tiền ròng tích lũy (Cumulative Net Cash Flow — $CNCF_t$) chuyển sang giá trị âm:
$$CNCF_t = HQLA_0^{\text{adj}} + \sum_{k=1}^t \left( \text{Inflows}_k^{\text{adj}} - \text{Outflows}_k^{\text{adj}} \right)$$
$$T_{\text{survival}} = \min \{ t \ge 1 \mid CNCF_t < 0 \}$$
trong đó $HQLA_0^{\text{adj}}$ là quy mô tài sản thanh khoản cao ban đầu đã trừ đi mức chiết khấu áp lực (haircuts, ví dụ mức chiết khấu 5% đối với trái phiếu chính phủ trong mô hình của ECB/SSM), $\text{Inflows}_k^{\text{adj}}$ là dòng tiền vào theo hợp đồng có tính đến khả năng đối tác vỡ nợ, và $\text{Outflows}_k^{\text{adj}}$ là dòng tiền ra tích hợp các giả định rút tiền gửi (run-off rates) cùng việc giải ngân các cam kết ngoại bảng (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.248–254).

Trong khi chỉ số [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]] giới hạn chân trời quan sát cố định trong 30 ngày theo tỷ lệ phần trăm tĩnh, thước đo thời gian sinh tồn do ECB/SSM áp dụng mở rộng chân trời lên tới 6 tháng hoặc 1 năm, vận hành trên nguyên tắc [[static-balance-sheet-assumption-in-liquidity-stress-testing-isolates-first-round-shocks]] để tìm ra "điểm gãy" thanh khoản tự nhiên của từng ngân hàng (insights_59, Section 4, Sector-wide stress tests for liquidity risk, d.207–212, d.250). Thước đo này trực tiếp hiện thực hóa khẩu vị rủi ro thanh khoản được hội đồng quản trị phê chuẩn [[board-approved-liquidity-risk-tolerance-aligns-business-strategy-with-stress-survival-horizons]], giúp cơ quan giám sát xếp hạng thứ tự ưu tiên can thiệp đối với các ngân hàng có thời gian sinh tồn dưới ngưỡng an toàn tối thiểu và kiểm định năng lực bảo vệ của [[unencumbered-high-quality-liquid-asset-cushion-insures-against-stress-cash-flow-deficits]].
