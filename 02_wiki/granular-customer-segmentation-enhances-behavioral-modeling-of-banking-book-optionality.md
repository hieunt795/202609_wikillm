---
title: granular-customer-segmentation-enhances-behavioral-modeling-of-banking-book-optionality
type: concept
tags: [alm, behavioral-economics, deposits, irrbb, model-governance, supervision]
sources: [tata_bank_alm]
status: stable
last_updated: 2026-10-12
reviewed: 2026-10-12
reviewed_by: model
part_of: [behavioral-alm-models-customer-irrbb-optionality-and-asymmetric-interbank-competition]
related: [interest-rate-risk-in-the-banking-book-irrbb, silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs, supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb, deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]
---

Theo nguồn, các ngân hàng vẫn đang trong quá trình đưa mô hình hành vi vào quản trị rủi ro lãi suất và thanh khoản trong ALM (tata_bank_alm, Ch.6, §6.5, d.3192); phần lãi suất thuộc [[interest-rate-risk-in-the-banking-book-irrbb|IRRBB]], và các giả định hành vi nền nằm ở trang [[behavioral-alm-models-customer-irrbb-optionality-and-asymmetric-interbank-competition]]. Một cách làm phổ biến là chia nền khách hàng thành các nhóm chi tiết hơn theo yếu tố riêng của khách hàng, như địa vị kinh tế xã hội, lịch sử vay, địa lý, thu nhập ròng hoặc tuổi (tata_bank_alm, Ch.6, §6.5, d.3194). Việc phân khúc và gom cụm có thể dùng thuật toán phân loại, thường dựa trên dữ liệu lớn và phân tích nâng cao (tata_bank_alm, Ch.6, §6.5, d.3244).

Nguồn dẫn Soulellis (2017) về năm yếu tố phân biệt dùng để mô hình hóa hành vi số dư tiền gửi (tata_bank_alm, Ch.6, §6.5, d.3194–3201): số dư ban đầu khi mở; có hay không lãi suất khuyến mãi hoặc lãi suất giới thiệu; độ sâu và thời gian của quan hệ giữa khách hàng với ngân hàng; tuổi của khách hàng; và kênh mở tài khoản, chẳng hạn trực tuyến hay tại chi nhánh. Sau khi phân khúc, từng nhóm có mô hình hành vi được hiệu chuẩn riêng theo hành vi quan sát được trong nhóm (tata_bank_alm, Ch.6, §6.5, d.3203). Các mô hình cần được điều chỉnh, hiệu chuẩn và kiểm định ngược liên tục theo thay đổi của thị trường, sự kiện vĩ mô, sản phẩm mới, mức am hiểu của khách hàng, chiến lược của đối thủ và diễn biến bảng cân đối (tata_bank_alm, Ch.6, §6.5, d.3203).

Cơ quan quản lý và giám sát mới gần đây bắt đầu chú ý tới khía cạnh hành vi của IRRBB và ALM, và vụ sụp đổ của [[silicon-valley-bank-collapse-epitomizes-unhedged-duration-mismatches-and-uninsured-deposit-runs|Silicon Valley Bank]] năm 2023 làm việc này gấp hơn (tata_bank_alm, Ch.6, §6.5, d.3205). Nguồn dẫn báo cáo Barr (2023): cơ quan giám sát đã phát triển các cách tiếp cận dựa trên khoa học hành vi, dùng dữ liệu về thái độ và chuẩn mực của tổ chức liên quan tới các yếu tố như chủ quan, tự tin quá mức, chú trọng ngắn hạn và thiếu phản biện hiệu quả, để lộ ra các điểm mù của tổ chức (tata_bank_alm, Ch.6, §6.5, d.3207) (tata_bank_alm, Ch.6, §6.5, d.3245); trang [[supervisory-and-governance-failures-in-interest-rate-risk-management-lessons-from-svb]] ghi các thất bại đó ở SVB. Mức chi tiết tới từng khách hàng nằm ở trang [[deep-alm-and-advanced-analytics-enable-real-time-customer-level-balance-sheet-steering]].
