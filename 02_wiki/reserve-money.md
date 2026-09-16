---
title: reserve-money
type: concept
tags: [monetary-policy]
sources: [imf_macro_accounting]
status: stable
last_updated: 2026-09-16
---

Tiền dự trữ (reserve money, high-powered money, tiền cơ sở — RM) là nghĩa vụ nợ chính của [[central-bank|nhà chức trách tiền tệ]]: chủ yếu là tiền đã phát hành, giữ trong ngân hàng (tiền mặt trong quỹ) và ngoài ngân hàng (tiền lưu thông), cộng tiền gửi của ngân hàng và phi ngân hàng tại nhà chức trách tiền tệ; tiền gửi của chính phủ và người không cư trú không tính vào RM vì đã được trừ ròng vào tín dụng cho chính phủ và tài sản đối ngoại tương ứng (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4593–4609). Nhà chức trách tiền tệ là bên duy nhất có quyền tạo RM đơn giản bằng cách phát séc trên chính mình, nên khả năng kiểm soát RM là kênh chính để điều tiết cung tiền và thu [[seigniorage]].

Đồng nhất thức dưới đây là bản rút gọn/phân tích (analytical) của một bảng cân đối vốn chi tiết hơn nhiều theo từng khoản mục cụ thể, xem [[the-typical-monetary-authorities-balance-sheet-itemizes-foreign-assets-and-shows-reserve-money-by-holder]] — bản trình bày dạng bảng của đúng cách nhóm này nằm ở [[the-analytical-monetary-authorities-balance-sheet-groups-items-into-nfa-nda-and-rm]]. Ràng buộc bảng cân đối của nhà chức trách tiền tệ được tóm gọn trong đồng nhất thức

$$RM \equiv NFA^* + NCG^* + CDMB^* + CPS^* + OIN^*$$

trong đó $NFA^*$ là tài sản đối ngoại ròng (rộng hơn khái niệm dự trữ chính thức — còn gồm cả tài sản ngoại tệ không quy đổi được hay phát sinh từ hiệp định thanh toán song phương), $NCG^*$ là [[net-credit-to-government|tín dụng ròng cho chính phủ]] (trừ tiền gửi chính phủ, vì chính phủ tiếp cận tín dụng dễ hơn khu vực khác nên chi tiêu của chính phủ không bị ràng buộc bởi số dư tiền gửi), $CDMB^*$ là tín dụng cho ngân hàng nhận tiền gửi, $CPS^*$ là tín dụng cho khu vực tư (thường không đáng kể vì cho vay tư nhân chủ yếu là việc của DMB), — khoản tín dụng này được giữ ở dạng gộp chứ không trừ tiền gửi của DMB, khác hẳn cách xử lý $NCG^*$, xem [[monetary-accounts-net-claims-on-government-but-keep-claims-on-deposit-money-banks-gross]] — và $OIN^*$ là [[other-items-net|khoản mục khác]] ròng — gồm tài sản vật chất của nhà chức trách tiền tệ, vốn và quỹ dự trữ, lợi nhuận/lỗ, và đặc biệt là [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks|điều chỉnh định giá lại tài sản đối ngoại ròng do biến động tỷ giá]] (imf_macro_accounting, Ch.5, cùng mục, d.4602–4627).

Ở dạng thay đổi tồn kho (dòng chảy):

$$\Delta RM = \Delta NFA^* + \Delta NCG^* + \Delta CDMB^* + \Delta CPS^* + \Delta OIN^*$$

(imf_macro_accounting, Ch.5, cùng mục, d.4631–4634). Chia đồng nhất thức dòng chảy này cho $RM$ kỳ trước, tốc độ tăng trưởng tiền cơ sở tách thành tổng đóng góp thô của từng khoản mục tài sản:

$$\frac{\Delta RM_t}{RM_{t-1}} = \frac{\Delta NFA^*_t}{RM_{t-1}} + \frac{\Delta NCG^*_t}{RM_{t-1}} + \frac{\Delta CDMB^*_t}{RM_{t-1}} + \frac{\Delta CPS^*_t}{RM_{t-1}} + \frac{\Delta OIN^*_t}{RM_{t-1}}$$

(imf_macro_accounting, Ch.5, cùng mục, d.4636–4639 — nguồn OCR lặp số hạng $CDMB^*$ hai lần, bản trên bỏ trùng theo đúng bốn khoản mục tài sản của (5.1)). Viết lại mỗi số hạng thành tích của tốc độ tăng trưởng riêng của khoản mục đó nhân tỷ trọng khoản mục trong RM kỳ trước, cho biết khoản mục nào đang thực sự đẩy tiền cơ sở tăng hay giảm — không chỉ đóng góp bao nhiêu mà còn vì bản thân nó tăng nhanh hay vì tỷ trọng nó lớn:

$$\frac{\Delta RM_t}{RM_{t-1}} = \frac{\Delta NFA^*_t}{NFA^*_{t-1}}\cdot\frac{NFA^*_{t-1}}{RM_{t-1}} + \frac{\Delta NCG^*_t}{NCG^*_{t-1}}\cdot\frac{NCG^*_{t-1}}{RM_{t-1}} + \frac{\Delta CDMB^*_t}{CDMB^*_{t-1}}\cdot\frac{CDMB^*_{t-1}}{RM_{t-1}} + \frac{\Delta OIN^*_t}{OIN^*_{t-1}}\cdot\frac{OIN^*_{t-1}}{RM_{t-1}}$$

(imf_macro_accounting, Ch.5, cùng mục, d.4640–4645 — nguồn bị mất số hạng $CPS^*$ do lỗi OCR; chỉ còn 4/5 khoản mục, không tự suy diễn số hạng thiếu). Đây là công cụ phân rã dùng trong [[monetizing-the-deficit-creates-high-powered-money-and-inflation|phân tích tiền tệ hoá thâm hụt]] và trong chương trình tài chính của IMF để theo dõi nguồn gốc mở rộng tiền tệ. Bản thân RM không phải khối tiền lưu hành trong nền kinh tế — [[the-money-multiplier-links-reserve-money-to-the-money-supply|số nhân tiền]] mới là cầu nối biến một đơn vị tiền cơ sở thành một bội số tương ứng của khối tiền.
