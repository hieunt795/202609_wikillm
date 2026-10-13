---
title: lcr-cash-outflows-apply-run-off-and-drawdown-rates-to-four-blocks-of-liabilities-and-commitments
type: analysis
tags: [lcr, basel-iii, liquidity-regulation, cash-outflows]
sources: [basel_lcr]
status: draft
last_updated: 2026-10-13
---

[[total-expected-cash-outflows|Tổng dòng ra dự kiến]] của LCR bằng tổng số dư của từng nhóm nợ phải trả và cam kết ngoại bảng nhân với [[run-off-rate|tỷ lệ run-off]] hoặc tỷ lệ rút của nhóm đó, và chương LCR40 xếp các nhóm thành bốn khối (basel_lcr, LCR40, Definition of total net cash outflows, 40.1, d.709). Vế còn lại của mẫu số nằm ở trang [[lcr-cash-inflows-count-contractual-receivables-by-counterparty-under-a-75-percent-cap]], và phép gộp hai vế ở trang [[lcr-net-outflows-weight-liabilities-by-run-off-rates-and-receivables-by-inflow-rates-under-a-75-percent-cap]].

Khối 1 là tiền gửi bán lẻ, với các tỷ lệ là mức sàn mà từng nước được nâng lên (basel_lcr, LCR40, Cash outflows – Retail deposit run-off, 40.6–40.16, d.748–790):

| Thành phần | Tỷ lệ | Trang |
|---|---|---|
| Phần ổn định | 5%, hoặc 3% khi bảo hiểm tiền gửi đạt thêm ba tiêu chí | [[stable-retail-deposits-run-off-at-5-percent-or-3-percent-under-effective-deposit-insurance]] |
| Các nhóm kém ổn định | tối thiểu 10% | [[lcr-retail-deposits-split-into-stable-and-less-stable-portions-with-run-off-floors]] |
| Có kỳ hạn còn trên 30 ngày, không rút được hoặc rút sớm chịu phạt lớn | loại khỏi dòng ra | [[retail-term-deposits-beyond-30-days-leave-lcr-outflows-unless-withdrawable-without-penalty]] |

Khối 2 là [[unsecured-wholesale-funding|vốn bán buôn không có bảo đảm]], chia theo bên cấp vốn (basel_lcr, LCR40, Cash outflows – unsecured wholesale funding run-off, đề mục các mục và 40.22–40.42, d.810–896):

| Thành phần | Tỷ lệ | Trang |
|---|---|---|
| Doanh nghiệp nhỏ, tổng vốn dưới 1 triệu euro | như tiền gửi bán lẻ | [[small-business-funding-below-eur-1-million-is-treated-as-retail-deposits-in-the-lcr]] |
| Tiền gửi vận hành từ bù trừ, lưu ký, quản lý tiền mặt | 25% | [[operational-deposits]] |
| Tiền gửi trong mạng lưới ngân hàng hợp tác xã | 25% hoặc 100% | [[deposits-within-cooperative-bank-networks-run-off-at-25-percent-under-a-mutual-protection-scheme]] |
| Doanh nghiệp phi tài chính, chính phủ, ngân hàng trung ương, PSE | 40%, hoặc 20% nếu được bảo hiểm đầy đủ | [[non-financial-corporate-and-sovereign-funding-runs-off-at-40-percent-or-20-percent-if-fully-insured]] |
| Tổ chức tài chính, pháp nhân khác, giấy nợ ngân hàng tự phát hành | 100% | [[funding-from-financial-institutions-and-other-legal-entities-runs-off-at-100-percent]] |

Khối 3 là [[secured-funding|tài trợ có bảo đảm]] đáo hạn trong 30 ngày. Tỷ lệ tính trên số tiền huy động và đi theo tài sản bảo đảm, theo bảng ở trang [[secured-funding-run-off-rates-mirror-the-lcr-haircut-of-the-pledged-collateral]] (basel_lcr, LCR40, Secured funding run-off, 40.48, d.944–951):

| Giao dịch đáo hạn | Tỷ lệ |
|---|---|
| Bảo đảm bằng Level 1, hoặc đối tác là ngân hàng trung ương | 0% |
| Bảo đảm bằng Level 2A | 15% |
| Với chính phủ trong nước, PSE hoặc ngân hàng phát triển đa phương, tài sản ngoài Level 1 và 2A | 25% |
| Bảo đảm bằng RMBS thuộc Level 2B | 25% |
| Bảo đảm bằng Level 2B khác | 50% |
| Còn lại | 100% |

Khối 4 là các yêu cầu bổ sung. Phần đầu gồm phái sinh, tài sản bảo đảm và nguồn tài trợ cấu trúc (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.49–40.58, d.955–1066):

| Thành phần | Dòng ra | Trang |
|---|---|---|
| Dòng ra phái sinh ròng | 100% | [[net-derivative-cash-outflows-receive-a-100-percent-factor-in-the-lcr]] |
| Điều khoản hạ xếp hạng, tới 3 bậc | 100% tài sản bảo đảm phải nộp | [[downgrade-triggers-require-liquidity-for-collateral-calls-up-to-a-three-notch-downgrade]] |
| Tài sản bảo đảm không phải Level 1 đã nộp | cộng 20% giá trị | [[non-level-1-collateral-posted-for-derivatives-needs-a-20-percent-hqla-add-on]] |
| Tài sản bảo đảm thừa, đến hạn chưa bị gọi, có thể bị thay | 100% mỗi loại | [[excess-uncalled-and-substitutable-collateral-each-count-as-a-100-percent-lcr-outflow]] |
| Thay đổi định giá phái sinh | dòng tài sản bảo đảm ròng 30 ngày lớn nhất trong 24 tháng | [[market-valuation-changes-on-derivatives-enter-the-lcr-through-a-24-month-look-back]] |
| ABS, covered bond tự phát hành đáo hạn | 100% | [[maturing-own-issued-abs-and-covered-bonds-are-assumed-not-refinanced-in-the-lcr]] |
| ABCP, conduit, SIV: nợ đáo hạn và tài sản có thể bị trả lại | 100% | [[structured-financing-facilities-require-look-through-to-spe-debt-and-liquidity-puts]] |

Phần thứ hai là [[committed-credit-and-liquidity-facilities|hạn mức cam kết]], tính trên phần chưa rút, với ranh giới hai cột ở trang [[a-liquidity-facility-backstops-customer-debt-maturing-within-30-days-while-the-rest-is-a-credit-facility]] (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.64, d.1087–1094). Bảng đầy đủ nằm ở trang [[committed-facility-drawdown-rates-rise-from-5-percent-for-retail-to-100-percent-for-other-legal-entities]]:

| Đối tác | Hạn mức tín dụng | Hạn mức thanh khoản |
|---|---|---|
| Bán lẻ và doanh nghiệp nhỏ | 5% | 5% |
| Doanh nghiệp phi tài chính, khu vực công | 10% | 30% |
| Ngân hàng chịu giám sát an toàn | 40% | 40% |
| Tổ chức tài chính khác | 40% | 100% |
| Pháp nhân khác, SPE, conduit | 100% | 100% |

Phần cuối là các nghĩa vụ còn lại (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.65–40.74, d.1102–1145):

| Thành phần | Dòng ra | Trang |
|---|---|---|
| Nghĩa vụ cho vay theo hợp đồng | 100% với tổ chức tài chính; với khách hàng khác chỉ phần vượt 50% dòng vào từ họ | [[contractual-lending-obligations-count-as-outflows-in-full-for-financials-and-above-half-of-inflows-for-others]] |
| Nghĩa vụ tài trợ tiềm tàng khác | do từng nước quyết định và công bố | [[other-contingent-funding-obligations]] |
| Tài trợ thương mại | 5% hoặc thấp hơn | [[trade-finance-contingent-obligations-may-receive-a-run-off-of-5-percent-or-less]] |
| Bán khống của khách hàng phủ bằng tài sản của khách hàng khác | tối thiểu 50% | [[customer-shorts-covered-by-other-customers-collateral-carry-a-minimum-50-percent-run-off]] |
| Dòng ra theo hợp đồng khác, như cổ tức và lãi | 100%; chi phí hoạt động không tính | [[other-contractual-cash-outflows-receive-a-100-percent-factor-while-operating-costs-are-excluded]] |

Ba quy tắc cắt ngang các khối. Một khoản có thể rơi vào nhiều nhóm chỉ được tính tối đa bằng dòng ra lớn nhất theo hợp đồng của nó (basel_lcr, LCR40, Definition of total net cash outflows, 40.4, d.719). [[options-exercisable-within-30-days-are-assumed-exercised-when-in-the-money-in-the-lcr|Quyền chọn thực hiện được trong 30 ngày được coi là được thực hiện khi có lãi]], và [[delivery-obligations-assume-the-cheapest-to-deliver-asset-on-both-inflow-and-outflow-sides|nghĩa vụ giao tài sản giả định giao loại có giá trị thanh khoản thấp nhất]] (basel_lcr, LCR40, Cash outflows – Additional requirements, 40.49, d.955).

Các bảng trên khớp với phần dòng ra của bảng tóm tắt chuẩn mực, nơi ba mức sàn và trần được ghi gọn thành 10% cho tiền gửi kém ổn định, 50% cho vị thế bán khống của khách hàng và 0–5% cho tài trợ thương mại (basel_lcr, LCR99, 99.1, d.1354–1401).
