---
title: reserve-money
type: concept
tags: [monetary-policy]
sources: [imf_macro_accounting]
status: stable
last_updated: 2026-09-25
reviewed: 2026-09-25
reviewed_by: model
---

Tiền dự trữ (reserve money, high-powered money, tiền cơ sở — RM) là nghĩa vụ nợ chính của [[central-bank|nhà chức trách tiền tệ]]: chủ yếu là tiền đã phát hành, giữ trong ngân hàng (tiền mặt trong quỹ) và ngoài ngân hàng (tiền lưu thông), cộng tiền gửi của ngân hàng và phi ngân hàng tại nhà chức trách tiền tệ; tiền gửi của chính phủ và người không cư trú không tính vào RM vì đã được trừ ròng vào tín dụng cho chính phủ và tài sản đối ngoại tương ứng (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4618). Nhà chức trách tiền tệ là bên duy nhất có quyền tạo RM đơn giản bằng cách phát séc trên chính mình (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4622), nên khả năng kiểm soát RM là kênh chính để điều tiết cung tiền và thu [[seigniorage]] (imf_macro_accounting, Ch.5, The Definition and Role of Monetary Authorities, d.4584).

Đồng nhất thức dưới đây là bản rút gọn/phân tích (analytical) của một bảng cân đối vốn chi tiết hơn nhiều theo từng khoản mục cụ thể, xem [[the-typical-monetary-authorities-balance-sheet-itemizes-foreign-assets-and-shows-reserve-money-by-holder]] — bản trình bày dạng bảng của đúng cách nhóm này nằm ở [[the-analytical-monetary-authorities-balance-sheet-groups-items-into-nfa-nda-and-rm]] (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4604). Ràng buộc bảng cân đối của nhà chức trách tiền tệ được tóm gọn trong đồng nhất thức (5.1) (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4626–4629)

$$RM \equiv NFA^* + NCG^* + CDMB^* + CPS^* + OIN^*$$

trong đó $NFA^*$ là tài sản đối ngoại ròng, rộng hơn dự trữ chính thức ròng vì còn gồm các tài sản và nợ đối ngoại khác của nhà chức trách tiền tệ; ví dụ nguồn nêu là ngoại tệ không chuyển đổi được và trái quyền từ hiệp định thanh toán song phương mà một số nền kinh tế chuyển đổi nắm giữ (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4606–4610). $NCG^*$ là [[net-credit-to-government|tín dụng ròng cho chính phủ]], đã trừ tiền gửi chính phủ vì chính phủ vay dễ hơn các khu vực khác nên chi tiêu của chính phủ thường không bị giới hạn bởi số dư tiền gửi (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4612). $CDMB^*$ là tín dụng cho ngân hàng nhận tiền gửi (DMB) và được ghi gộp, tức là tiền gửi của DMB tại nhà chức trách tiền tệ không bị trừ ra; cách ghi này ngược với $NCG^*$, và [[monetary-accounts-net-claims-on-government-but-keep-claims-on-deposit-money-banks-gross]] giải thích vì sao hai khoản được xử lý khác nhau (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4612). $CPS^*$ là trái quyền với các khu vực trong nước khác, chủ yếu là khu vực tư nhưng cũng gồm trái quyền với các tổ chức tài chính khác và doanh nghiệp công; khoản này thường nhỏ vì cho vay hộ gia đình và doanh nghiệp là việc của DMB (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4608, d.4614). $OIN^*$ là [[other-items-net|các khoản mục khác ròng]], nhóm còn lại gồm tài sản hiện vật của ngân hàng trung ương, vốn và quỹ dự trữ, lãi hoặc lỗ, các khoản chưa xếp vào nhóm nào và [[valuation-adjustments-separate-transaction-flows-from-exchange-rate-revaluation-of-stocks|điều chỉnh định giá lại tài sản đối ngoại ròng do tỷ giá biến động]], kể cả lãi hoặc lỗ chưa thực hiện từ các biến động đó (imf_macro_accounting, Ch.5, The Balance Sheet of Monetary Authorities, d.4616).

Ở dạng thay đổi tồn kho (dòng chảy):

$$\Delta RM = \Delta NFA^* + \Delta NCG^* + \Delta CDMB^* + \Delta CPS^* + \Delta OIN^*$$

(imf_macro_accounting, Ch.5, cùng mục, d.4631–4634). Chia đồng nhất thức dòng chảy này cho $RM$ kỳ trước, tốc độ tăng trưởng tiền cơ sở tách thành tổng đóng góp thô của từng khoản mục tài sản:

$$\frac{\Delta RM_t}{RM_{t-1}} = \frac{\Delta NFA^*_t}{RM_{t-1}} + \frac{\Delta NCG^*_t}{RM_{t-1}} + \frac{\Delta CDMB^*_t}{RM_{t-1}} + \frac{\Delta CPS^*_t}{RM_{t-1}} + \frac{\Delta OIN^*_t}{RM_{t-1}}$$

(imf_macro_accounting, Ch.5, cùng mục, d.4636–4639; bản chuyển đổi của nguồn lặp số hạng $CDMB^*$ hai lần, công thức trên bỏ số hạng trùng để khớp năm khoản mục tài sản của (5.1)). Viết lại mỗi số hạng thành tích của tốc độ tăng trưởng riêng của khoản mục đó nhân tỷ trọng khoản mục trong RM kỳ trước, tốc độ tăng RM trở thành tổng có trọng số của tốc độ tăng các khoản mục tài sản, với trọng số là tỷ trọng kỳ trước của từng khoản mục trong RM kỳ trước (imf_macro_accounting, Ch.5, cùng mục, d.4647–4651):

$$\frac{\Delta RM_t}{RM_{t-1}} = \frac{\Delta NFA^*_t}{NFA^*_{t-1}}\cdot\frac{NFA^*_{t-1}}{RM_{t-1}} + \frac{\Delta NCG^*_t}{NCG^*_{t-1}}\cdot\frac{NCG^*_{t-1}}{RM_{t-1}} + \frac{\Delta CDMB^*_t}{CDMB^*_{t-1}}\cdot\frac{CDMB^*_{t-1}}{RM_{t-1}} + \frac{\Delta OIN^*_t}{OIN^*_{t-1}}\cdot\frac{OIN^*_{t-1}}{RM_{t-1}}$$

(imf_macro_accounting, Ch.5, cùng mục, d.4640–4651; bản chuyển đổi của nguồn chỉ có 4 trong 5 khoản mục, thiếu $CPS^*$, và ghi tử số cuối là $\Delta OIN^*_{t-1}$. Công thức trên giữ đúng 4 số hạng, chỉ chuẩn hoá chỉ số thời gian, và không tự thêm số hạng thiếu vì không kiểm được lỗi nằm ở bản chuyển đổi hay bản gốc). Đồng nhất thức dòng chảy (5.2) cho thấy vì sao [[monetizing-the-deficit-creates-high-powered-money-and-inflation|tiền tệ hoá thâm hụt]] tạo ra tiền cơ sở. Khi chính phủ vay nhà chức trách tiền tệ, trái quyền với chính phủ và tiền gửi chính phủ cùng tăng nên $NCG^*$ chưa đổi. Khi chính phủ chi khoản vay đó cho khu vực tư, tiền gửi chính phủ giảm, $NCG^*$ tăng và RM tăng đúng bằng mức đó (imf_macro_accounting, Ch.5, Interpretation of Balance Sheet Changes, d.4671–4675). RM không phải là khối tiền $M$ (tiền mặt ngoài ngân hàng cộng tiền gửi); [[the-money-multiplier-links-reserve-money-to-the-money-supply|số nhân tiền]] cho biết một đơn vị tiền cơ sở tạo ra bao nhiêu đơn vị khối tiền (imf_macro_accounting, Ch.5, The Concept of the Money Multiplier, d.4940–4949).
