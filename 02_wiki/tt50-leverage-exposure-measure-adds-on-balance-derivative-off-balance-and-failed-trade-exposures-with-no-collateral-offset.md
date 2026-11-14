---
title: tt50-leverage-exposure-measure-adds-on-balance-derivative-off-balance-and-failed-trade-exposures-with-no-collateral-offset
type: concept
tags: [vietnam, tt50, leverage-ratio, exposure-measure, off-balance-sheet, failed-trades]
sources: [tt50_2026_sbv]
status: draft
last_updated: 2026-11-14
part_of: [leverage-ratio-lev]
has_part: [tt50-leverage-on-balance-exposure-includes-pledged-and-trust-assets-and-nets-only-qualifying-cash-pools, tt50-leverage-derivative-exposure-is-1-4-times-replacement-cost-plus-potential-future-exposure]
contrasts: [committed-credit-and-liquidity-facilities-run-off-by-counterparty-type-from-5-to-100-percent-in-tt50]
---

Tổng trạng thái rủi ro (exposure measure, EM), mẫu số của [[leverage-ratio-lev|tỷ lệ đòn bẩy]], gồm mọi tài sản trên Báo cáo tình hình tài chính và các cam kết ngoại bảng, cộng theo bốn phần (tt50_2026_sbv, Phụ lục III, mục I khoản 1, d.2182–2196):

$$EM = E_{OnB} + E_{D} + E_{OffB} + E_{US}$$

$E_{OnB}$ là tài sản nội bảng, không gồm công cụ phái sinh và giao dịch chưa tất toán, tính theo [[tt50-leverage-on-balance-exposure-includes-pledged-and-trust-assets-and-nets-only-qualifying-cash-pools]]. $E_D$ là trạng thái phái sinh, tính theo [[tt50-leverage-derivative-exposure-is-1-4-times-replacement-cost-plus-potential-future-exposure]]. $E_{OffB}$ là trạng thái ngoại bảng và $E_{US}$ là trạng thái giao dịch chưa tất toán (failed trades). Giao dịch phái sinh hiểu theo quy định về tỷ lệ an toàn vốn mà ngân hàng đang áp dụng (tt50_2026_sbv, Phụ lục III, mục I khoản 2, d.2198).

Bốn nguyên tắc chung giữ EM ở dạng số gộp (tt50_2026_sbv, Phụ lục III, mục I khoản 4–6, d.2206–2210). EM lấy theo giá trị từng loại tài sản ghi nhận theo chế độ kế toán, chế độ tài chính. Ngân hàng không dùng tài sản bảo đảm, bảo lãnh hay biện pháp giảm thiểu rủi ro tín dụng khác để giảm EM, và không bù trừ tài sản với nợ phải trả, trừ các trường hợp mục II nêu riêng. Tài sản đã được giảm trừ khi tính vốn cấp 1 thì không tính vào EM. Phần chênh lệch giảm do đánh giá lại tài sản không được khấu trừ khỏi EM.

Giao dịch chưa tất toán là giao dịch đã thực hiện thanh toán nhưng chưa hoàn tất việc chấm dứt hợp đồng và dự kiến được kế toán ghi vào khoản mục nội bảng (tt50_2026_sbv, Phụ lục III, mục I khoản 3, d.2200). Phái sinh chưa tất toán tính theo cách của phái sinh; các giao dịch chưa tất toán khác tính như tài sản nội bảng (tt50_2026_sbv, Phụ lục III, mục I khoản 3a–b, d.2202–2204).

Trạng thái ngoại bảng là tổng số dư phần cam kết ngoại bảng của từng khoản phải đòi nhân hệ số chuyển đổi (credit conversion factor, CCF) của nó (tt50_2026_sbv, Phụ lục III, mục II khoản 3, d.2272–2280):

$$E_{OffB} = \sum E_{off_{i}} \times CCF_{i}$$

Cả số dư ngoại bảng và CCF đều lấy theo quy định về tỷ lệ an toàn vốn mà ngân hàng đang áp dụng; TT50 không ghi giá trị CCF, cần ingest thêm Thông tư 41/2016/TT-NHNN hoặc Thông tư 14/2025/TT-NHNN. Phía LCR, cùng các hạn mức cam kết dùng hệ số rút tiền theo loại khách hàng chứ không dùng CCF, xem [[committed-credit-and-liquidity-facilities-run-off-by-counterparty-type-from-5-to-100-percent-in-tt50]].
