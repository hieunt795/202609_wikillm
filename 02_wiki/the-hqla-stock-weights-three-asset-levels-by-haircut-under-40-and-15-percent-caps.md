---
title: the-hqla-stock-weights-three-asset-levels-by-haircut-under-40-and-15-percent-caps
type: analysis
tags: [lcr, basel-iii, liquidity-regulation, hqla]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-13
---

Tử số của [[liquidity-coverage-ratio-lcr|LCR]] là kho [[high-quality-liquid-assets-hqla|HQLA]], tính bằng cách nhân giá trị thị trường của từng tài sản với hệ số của cấp tài sản đó rồi áp hai trần tỷ trọng (basel_lcr, LCR99, 99.1, d.1341–1353). Bảng tóm tắt của chuẩn mực ghi hệ số giữ lại, tức 100% trừ [[haircut]]:

| Cấp | Thành phần | Hệ số | Haircut | Trần trong kho | Trang |
|---|---|---|---|---|---|
| Level 1 | Tiền xu, tiền giấy | 100% | 0% | không trần | [[level-1-assets]] |
| | Dự trữ tại ngân hàng trung ương đủ điều kiện | 100% | 0% | | |
| | Chứng khoán chính phủ, ngân hàng trung ương, PSE, ngân hàng phát triển đa phương, trọng số 0% | 100% | 0% | | |
| | Nợ nội tệ của chính phủ hoặc ngân hàng trung ương có trọng số rủi ro khác 0% | 100% | 0% | | |
| Level 2A | Chứng khoán chính phủ, ngân hàng trung ương, PSE, ngân hàng phát triển đa phương, trọng số 20% | 85% | 15% | Level 2 tối đa 40% | [[level-2a-assets]] |
| | Trái phiếu doanh nghiệp từ AA− | 85% | 15% | | |
| | Covered bond từ AA− | 85% | 15% | | |
| Level 2B | RMBS đủ điều kiện | 75% | 25% | Level 2B tối đa 15% | [[level-2b-assets]] |
| | Trái phiếu doanh nghiệp từ A+ tới BBB− | 50% | 50% | | |
| | Cổ phiếu phổ thông đủ điều kiện | 50% | 50% | | |
| | Nợ chính phủ, ngân hàng trung ương, PSE từ BBB−, ngoài Level 1 và 2A | 50% | 50% | | |

Cột hệ số và hai trần lấy từ bảng tóm tắt (basel_lcr, LCR99, 99.1, d.1345–1353). Level 1 không chịu haircut và không có trần (basel_lcr, LCR30, Level 1 assets, 30.40, d.239); Level 2A chịu 15% (basel_lcr, LCR30, Level 2 assets, 30.43, d.279); Level 2B chỉ được tính khi cơ quan giám sát cho phép (basel_lcr, LCR30, Level 2B assets, 30.44, d.314). ⚠️ Conflict: về ngưỡng dưới của trái phiếu doanh nghiệp Level 2B, chương LCR30 ghi xếp hạng tối thiểu BBB− (basel_lcr, LCR30, Level 2B assets, 30.45, d.325–332), còn bảng tóm tắt ghi "từ A+ tới BBB" (basel_lcr, LCR99, 99.1, d.1352); bảng trên theo LCR30. Cơ quan giám sát còn có thể tính vào Level 2B phần chưa rút của [[restricted-use-committed-liquidity-facility-rclf|hạn mức thanh khoản cam kết dùng hạn chế]] của ngân hàng trung ương (basel_lcr, LCR30, Level 2B assets, 30.46, d.381).

Hai trần được tính sau haircut, theo công thức ở trang [[level-2-assets-are-capped-at-40-percent-and-level-2b-at-15-percent-of-the-hqla-stock]], trên [[adjusted-hqla-amounts-unwind-secured-transactions-maturing-within-30-days|số đã tháo ngược các giao dịch có bảo đảm đáo hạn trong 30 ngày]] (basel_lcr, LCR30, Definition of HQLA, 30.34, d.220).

Trước khi được xếp cấp, một tài sản qua ba cửa: có [[hqla-eligibility-rests-on-four-fundamental-and-three-market-related-characteristics|bốn đặc tính cơ bản và ba đặc tính thị trường]], đạt [[hqla-operational-requirements|các yêu cầu vận hành]], và [[unencumbered-assets|không bị ràng buộc]] (basel_lcr, LCR30, Definition of HQLA, 30.30, d.212). Kho còn chịu hai quy tắc về thành phần. Trong từng cấp, kho phải đa dạng theo loại tài sản, đợt phát hành, tổ chức phát hành và đồng tiền, trừ nợ chính phủ nước nhà, dự trữ và chứng khoán ngân hàng trung ương, và tiền mặt (basel_lcr, LCR30, Diversification of the stock of HQLA, 30.29, d.208). Tài sản mất tư cách HQLA, ví dụ do bị hạ xếp hạng, được ở lại kho thêm 30 ngày lịch để ngân hàng kịp điều chỉnh (basel_lcr, LCR30, Operational requirements, 30.28, d.204).

Hai ngoại lệ đổi thành phần của kho. Ở đồng tiền thiếu Level 1, [[alternative-liquidity-approaches|ba phương án thanh khoản thay thế]] cho tính hạn mức cam kết của ngân hàng trung ương, HQLA ngoại tệ, hoặc Level 2A vượt trần 40% với haircut tối thiểu 20%, trong [[usage-of-alternative-liquidity-approaches-is-capped-as-a-share-of-the-required-hqla-in-the-currency|một trần sử dụng do cơ quan giám sát đặt]] (basel_lcr, LCR31, Introduction, 31.3, d.418–421). Với ngân hàng tuân thủ Shari'ah, [[sharia-compliant-banks-may-count-products-such-as-sukuk-as-alternative-hqla-at-supervisory-discretion|cơ quan giám sát được công nhận sản phẩm như Sukuk là HQLA thay thế]] (basel_lcr, LCR30, Treatment of Shari'ah compliant banks, 30.47, d.393).

Kho HQLA được đặt cạnh mẫu số ở trang [[lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap]], và toàn cảnh quy tắc thanh khoản ở trang [[bank-liquidity-rules-pair-a-stressed-30-day-hqla-buffer-with-ratio-limits-on-funding-structure]].
