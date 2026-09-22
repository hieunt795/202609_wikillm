---
title: interest-rate-corridor-symmetric-approach
type: concept
tags: [monetary, central-banking, monetary-policy-implementation, interest-rates, corridor]
sources: [bindseil_monetary_policy]
status: stable
last_updated: 2026-09-21
---

Trong symmetric corridor approach, NHTW cung cấp cả borrowing facility (lãi suất $i_B$) và deposit facility (lãi suất $i_D$) đặt đối xứng quanh lãi suất target $i^* = (i_B + i_D)/2$. NHTW steers lượng dự trữ sao cho xác suất hệ thống cần borrowing facility cuối ngày bằng xác suất cần deposit facility — khi đó lãi suất thị trường liên ngân hàng bằng trung điểm corridor theo arbitrage (bindseil_monetary_policy, Ch.4, §4.2, d.1003–1038).

**Tại sao symmetric thay vì asymmetric**: Trong corridor đối xứng, NHTW chỉ cần biết kỳ vọng của autonomous factors — các moment bậc cao (variance, skewness) của phân phối shock không ảnh hưởng tới lãi suất cân bằng. Trong corridor không đối xứng, NHTW phải điều chỉnh lượng cung thanh khoản mỗi khi variance của shock thay đổi, làm phức tạp dự báo và vận hành (bindseil_monetary_policy, Ch.4, §4.2, d.1081). Đây là lý do Eurosystem và Bank of England trước 2007 áp dụng symmetric corridor: tiết kiệm chi phí vận hành và dự báo.

**Thay đổi lập trường chính sách**: Thực hiện bằng dịch chuyển song song corridor $[i_D, i_B]$ lên hoặc xuống mà **không** thay đổi lượng OMO. Điều này tách biệt quyết định giá (lập trường chính sách) khỏi quyết định lượng (quản lý thanh khoản) — thể hiện [[separation-principle-of-monetary-policy]] ở mức kỹ thuật vận hành.

**Hai biến thể về nguồn OMO**: (i) NHTW nắm outright portfolio (BoE trước 2007: ~33 tỷ GBP) + credit OMO (~47 tỷ GBP); (ii) NHTW chỉ dùng credit OMO (Eurosystem trước 2007: short-term 313 tỷ + longer-term 150 tỷ EUR). Trong cả hai trường hợp, recourse tới standing facilities gần bằng 0, xác nhận đúng điểm cân bằng (bindseil_monetary_policy, Ch.4, §4.2, d.1083–1104).

**Full allotment variant** (§4.3 — ECB từ 10/2008): NHTW cung cấp credit OMO ở fixed rate với full allotment — ngân hàng nhận bất kỳ lượng nào đặt thầu. Ngân hàng đặt thầu sao cho kỳ vọng lãi suất sau allotment = lãi suất OMO. Kỹ thuật này để cho ngân hàng (không phải NHTW) quyết định lượng thanh khoản trong hệ thống. Trong khủng hoảng, ngân hàng đặt thầu vượt mức lý thuyết vì lý do phòng ngừa ("precautionary demand"), khiến lãi suất thị trường thực tế xuống dưới lãi suất OMO — dấu hiệu của stress thanh khoản không có trong mô hình đơn giản (bindseil_monetary_policy, Ch.4, §4.3, d.1106–1135). 

**Phá vỡ tính đối xứng trong khủng hoảng**: Vào ngày 9/8/2007 và trong suốt khủng hoảng tài chính, tính đối xứng lý thuyết này bị phá vỡ hoàn toàn do 4 nguồn phi đối xứng thực tế: sự bất đối xứng giữa cơ chế bình quân dự trữ và thấu chi, rủi ro cạn kiệt tài sản bảo đảm kích hoạt ELA, phần bù kỳ thị (stigma) tại borrowing facility, và rủi ro tín dụng đối tác. Điều này khiến lãi suất qua đêm thực tế vọt lên trên trung điểm hành lang, đòi hỏi NHTW phải bơm thanh khoản thặng dư hoặc nới lỏng haircut để tái lập kiểm soát (chi tiết xem [[effective-corridor-asymmetry-and-stigma-in-overnight-rates]]; bindseil_monetary_policy, Ch.12, §12.2, d.2643–2719).

Vấn đề then chốt trong thiết kế hành lang là xác định [[optimal-width-of-the-interest-rate-corridor|độ rộng tối ưu của hành lang]], cân bằng giữa ổn định lãi suất và duy trì kỷ luật thị trường liên ngân hàng. Ngoài ra, NHTW có thể sử dụng công cụ đệm thanh khoản [[taralac-facility-target-rate-limited-access|Taralac]] để neo lãi suất mà không làm tê liệt giao dịch thị trường tư nhân. Bức tranh toàn diện: [[three-techniques-to-control-short-term-interest-rates]], [[standing-facilities-in-monetary-policy-operations]].
