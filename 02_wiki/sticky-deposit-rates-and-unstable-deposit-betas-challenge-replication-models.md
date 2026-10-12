---
title: sticky-deposit-rates-and-unstable-deposit-betas-challenge-replication-models
type: analysis
tags: [alm, deposit-beta, sticky-rates, pass-through, duration-shortening, svb, replication-critique]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
has_part: [deposit-beta]
analogous: [interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]
related: [replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches, behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales, non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles, dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]
---

Mô hình tái tạo ở trang [[replicating-portfolios-model-non-maturity-deposits-via-vintage-run-off-tranches]] có người phê phán: nguồn nêu có bằng chứng rằng nó khớp kém với hành vi lãi suất trong điều kiện thị trường hiện tại (tata_bank_alm, Ch.2, Criticism, d.2043). Việc mô hình hóa tiền gửi không kỳ hạn (NMD) khó vì lãi suất người gửi nhận thường không đi sát thay đổi của mặt bằng lãi suất thị trường (tata_bank_alm, Ch.2, Criticism, d.2045). Lãi suất do ngân hàng đặt, gọi là lãi suất chỉ định (*administered rates*), chỉ liên hệ lỏng với lãi suất thị trường (tata_bank_alm, Ch.2, Criticism, d.2045). Một phần lý do là lãi suất tiền gửi ở mức độ nào đó là lãi suất chính sách: ngân hàng chỉ định lãi suất tài khoản với chủ đích quản khối lượng tiền gửi giữ lại (tata_bank_alm, Ch.2, Criticism, d.2049).

Nguồn dẫn Hoffmann và cộng sự (2023): thay đổi của lãi suất thị trường chỉ truyền một phần sang lãi suất tiền gửi thanh toán, 9% trong ngắn hạn và 29% trong dài hạn (tata_bank_alm, Ch.2, Criticism, d.2045) (tata_bank_alm, Ch.2, Notes, d.2134). Ngân hàng chậm điều chỉnh lãi suất tiền gửi, nên lãi suất tiền gửi dính (*sticky*) (tata_bank_alm, Ch.2, Criticism, d.2045). Jarrow và Van Deventer (1998) giải thích chênh lệch giữa lãi suất thị trường và lãi suất tiền gửi qua đêm bằng lập luận phân khúc thị trường: chỉ ngân hàng, không phải nhà đầu tư cá nhân, phát hành được tiền gửi qua đêm, nên tiền gửi qua đêm tương đương một hoán đổi lãi suất exotic có gốc phụ thuộc lịch sử lãi suất thị trường (tata_bank_alm, Ch.2, Criticism, d.2047).

[[deposit-beta|Deposit beta]] đo thay đổi của lãi suất tiền gửi so với thay đổi của lãi suất phi rủi ro phù hợp quan sát được trên thị trường (tata_bank_alm, Ch.2, Criticism, d.2055):
$$\beta_{deposit} = \frac{\Delta r_{deposit}}{\Delta r_{market}}$$
Nguồn hồi quy lãi suất tiền gửi khách hàng bình quân của các ngân hàng châu Âu theo lãi suất phi rủi ro 3 tháng, đo bằng lợi suất trái phiếu chính phủ khu vực euro xếp hạng AAA, trên ba giai đoạn (tata_bank_alm, Ch.2, Criticism, d.2059). Deposit beta ước khoảng 21% trong 2014–2017 khi lãi suất giảm, dưới 3% trong 2017–2021 khi lãi suất âm, và trên 20% từ 2023 khi lãi suất tăng trở lại (tata_bank_alm, Ch.2, Criticism, d.2059).

Độ nhạy của lãi suất tiền gửi với lãi suất thị trường ngắn hạn có vẻ đã tăng trong thập kỷ qua (tata_bank_alm, Ch.2, Criticism, d.2055). Acharya và cộng sự (2023) ghi nhận rằng khi lãi suất của các sản phẩm thay thế gần với tiền gửi ngân hàng, như quỹ thị trường tiền tệ, tăng mạnh trong năm 2022, áp lực cạnh tranh giành vốn lên các ngân hàng, tức deposit beta, tăng theo cách chưa gặp ít nhất từ 2008 (tata_bank_alm, Ch.2, Criticism, d.2055) (tata_bank_alm, Ch.2, References, d.2142).

Duration ước lượng tương đối dài của danh mục cuốn chiếu chủ yếu bắt nguồn từ môi trường lãi suất thấp của những năm gần đây: khối lượng tiền gửi ít thay đổi vì khách hàng không có động lực chi phí cơ hội để rút, và lãi suất tiền gửi kẹt ở 0% (tata_bank_alm, Ch.2, Criticism, d.2063). Khi lãi suất thị trường tăng thêm, nguồn dự kiến duration ngắn lại vì tiền gửi bớt dính và khối lượng giảm; hiệu ứng rõ hơn ở ngân hàng có khách hàng nhạy với chi phí cơ hội (tata_bank_alm, Ch.2, Criticism, d.2063). Nguồn coi việc chọn chân trời mô phỏng có lẽ là yếu tố chi phối lớn nhất của ước lượng duration (tata_bank_alm, Ch.2, Criticism, d.2063).

Nguồn dùng cụm "tương quan không hoàn hảo" cho quan hệ giữa lãi suất tiền gửi và lãi suất thị trường (tata_bank_alm, Ch.2, Criticism, d.2049); trang [[interest-rate-basis-risk-arises-from-imperfect-correlation-between-benchmarks]] định nghĩa loại rủi ro đến từ tương quan không hoàn hảo giữa các lãi suất tham chiếu. Trang [[behavioral-modeling-of-tt1-liabilities-distorts-when-banks-actively-intervene-on-pricing-and-sales]] nêu trường hợp ngân hàng can thiệp vào giá ở Thị trường 1 Việt Nam. Sản phẩm mà mô hình tái tạo áp vào nằm ở trang [[non-maturity-products-decouple-liquidity-profiles-from-interest-rate-profiles]], và cách xử lý thay đổi khối lượng nằm ở trang [[dynamic-replication-hedges-deposit-volume-fluctuations-at-prevailing-market-rates]].
