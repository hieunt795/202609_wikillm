---
title: basel-iii-lcr-master-factor-matrix-and-comprehensive-calibration-architecture
type: concept
tags: [basel, basel-iii, lcr, liquidity, hqla, factor-matrix, run-off-rates, inflow-rates, haircuts, unwinding-mechanics, cap-formulas, master-calibration, bcbs-238, regulation]
sources: [bcbs_238]
status: draft
last_updated: 2026-09-26
---

Kiến trúc hiệu chỉnh tổng thể và ma trận tham số chuẩn tắc của Tỷ lệ Khả năng Chi trả theo Basel III (BCBS 238, Annex 1 & Annex 4) thiết lập một hệ thống toán học hoàn chỉnh tích hợp toàn bộ các tỷ lệ chiết khấu tài sản (haircuts), hệ số rút vốn dòng tiền ra (run-off rates), hệ số thu hồi dòng tiền vào (inflow rates), cơ chế hoàn trả giao dịch tài trợ có bảo đảm ngắn hạn (unwinding mechanics) và các chốt chặn trần cơ cấu danh mục nhằm xác định chính xác tỷ lệ đệm thanh khoản phòng vệ trong 30 ngày khủng hoảng gay gắt (bcbs_238, file bcbs238.md, Annex 1 & Annex 4, d.848–876, 1180–1263). Bằng cách tổng hợp toàn diện các tham số định lượng được phân bổ rải rác trong các chương chuyên môn, ma trận chuẩn tắc này đóng vai trò là kim chỉ nam điều tiết vĩ mô cho khối quản trị cân đối tài sản - nợ (ALM) và cơ quan thanh tra giám sát toàn cầu khi đánh giá tính tuân thủ của các tổ chức tín dụng.

**1. Ma trận tham số chuẩn tắc toàn diện của Basel III LCR (Annex 4)**

Toàn bộ các hệ số định lượng của chuẩn mực LCR được quy chuẩn hóa trong bảng ma trận tổng hợp tại Annex 4 (bcbs_238, file bcbs238.md, Annex 4, d.1186–1263):

**A. Danh mục Tài sản có tính thanh khoản cao (Stock of HQLA)**
- **Tài sản Cấp 1 (Level 1 Assets) — Haircut 0% (Hệ số công nhận 100%)**: Tiền mặt, tiền gửi dự trữ khả dụng tại NHTW, chứng khoán thị trường do chính phủ/NHTW/MDBs/PSEs phát hành thỏa mãn trọng số rủi ro 0%, và nợ chính phủ/NHTW bằng đồng bản tệ của các quốc gia không có trọng số rủi ro 0% (nhưng chỉ được tính để bù đắp dòng tiền ra ròng bằng chính đồng bản tệ đó);
- **Tài sản Cấp 2A (Level 2A Assets) — Haircut 15% (Hệ số công nhận 85%)**: Chứng khoán chính phủ/PSEs/MDBs có trọng số rủi ro 20%, trái phiếu doanh nghiệp phi tài chính và trái phiếu có bảo đảm (covered bonds) đủ điều kiện có xếp hạng tín nhiệm tối thiểu AA-;
- **Tài sản Cấp 2B (Level 2B Assets)**:
  - *Chứng khoán bảo đảm bằng thế chấp nhà ở (Eligible RMBS)*: **Haircut 25% (Hệ số công nhận 75%)**;
  - *Trái phiếu doanh nghiệp đủ chuẩn (xếp hạng từ A+ đến BBB-)*: **Haircut 50% (Hệ số công nhận 50%)**;
  - *Cổ phiếu phổ thông đủ chuẩn (chỉ số bluechip chính)*: **Haircut 50% (Hệ số công nhận 50%)**.

**B. Dòng tiền ra dự kiến (Expected Cash Outflows)**
- **Tiền gửi bán lẻ (Retail Deposits)**:
  - *Tiền gửi ổn định (đạt 4 tiêu chuẩn bảo hiểm nghiêm ngặt)*: **3%**;
  - *Tiền gửi ổn định thông thường*: **5%**;
  - *Tiền gửi kém ổn định*: **10%** (hoặc cao hơn theo quyết định quốc gia);
  - *Tiền gửi có kỳ hạn còn lại trên 30 ngày (không thể rút trước hạn hoặc chịu phạt mất toàn bộ lãi)*: **0%**;
- **Nguồn vốn bán buôn không có bảo đảm (Unsecured Wholesale Funding)**:
  - *Tiền gửi doanh nghiệp nhỏ (SME)*: Ổn định **5%**, kém ổn định **10%**;
  - *Tiền gửi hoạt động (Operational deposits: clearing, custody, cash management)*: **25%** (nếu được bảo hiểm toàn bộ: **5%**);
  - *Tiền gửi mạng lưới ngân hàng hợp tác*: **25%**;
  - *Doanh nghiệp lớn phi tài chính, Chính phủ, NHTW, MDBs, PSEs*: **40%** (nếu được bảo hiểm toàn bộ: **20%**);
  - *Định chế tài chính và các pháp nhân khác*: **100%**;
- **Nguồn tài trợ có bảo đảm (Secured Funding / Repo)**:
  - *Giao dịch với NHTW hoặc bảo đảm bằng Tài sản Cấp 1*: **0%**;
  - *Bảo đảm bằng Tài sản Cấp 2A*: **15%**;
  - *Bảo đảm bằng tài sản phi Cấp 1/2A với đối tác là Chính phủ, MDBs, PSEs*: **25%**;
  - *Bảo đảm bằng RMBS Cấp 2B*: **25%**;
  - *Bảo đảm bằng Tài sản Cấp 2B khác*: **50%**;
  - *Bảo đảm bằng tài sản phi HQLA*: **100%**;
- **Yêu cầu thanh khoản gia tăng và Cam kết ngoại bảng**:
  - *Cú sốc hạ 3 bậc xếp hạng tín nhiệm*: **100%** giá trị dòng tiền/TSBĐ bổ sung theo hợp đồng;
  - *Biến động thị trường danh mục phái sinh*: Giá trị tuyệt đối của **dòng tiền ký quỹ ròng lớn nhất trong 30 ngày của 24 tháng trước** (Lookback Approach);
  - *Biến động TSBĐ phi Cấp 1 ký quỹ phái sinh*: **20%**;
  - *TSBĐ dư thừa hoặc nghĩa vụ nộp thêm chưa đòi*: **100%**;
  - *Mất nguồn tài trợ từ các cấu trúc nợ đáo hạn (ABCP, Conduits, SPVs)*: **100%**;
  - *Rút hạn mức tín dụng cam kết (Credit Facilities)*: Bán lẻ/SME **5%**, Doanh nghiệp phi tài chính/Sovereign/PSE **10%**, Ngân hàng **40%**, Định chế tài chính khác **40%**, Pháp nhân khác **100%**;
  - *Rút hạn mức thanh khoản cam kết (Liquidity Facilities)*: Bán lẻ/SME **5%**, Doanh nghiệp phi tài chính/Sovereign/PSE **30%**, Ngân hàng **40%**, Định chế tài chính khác **100%**, Conduits/SPVs **100%**;
  - *Cam kết tài trợ thương mại (Trade Finance)*: **0% đến 5%** (chuẩn mực 3%);
  - *Vị thế bán khống của khách hàng che bằng TSBĐ khách hàng khác (phi Cấp 1/2)*: **50%**;
  - *Dòng tiền ra ròng từ phái sinh*: **100%**;
  - *Dòng tiền ra hợp đồng khác*: **100%**.

**C. Dòng tiền vào dự kiến (Expected Cash Inflows)**
- **Cho vay có bảo đảm đáo hạn (Reverse Repo / Securities Borrowing)**:
  - *Bảo đảm bằng Tài sản Cấp 1*: **0%**;
  - *Bảo đảm bằng Tài sản Cấp 2A*: **15%**;
  - *Bảo đảm bằng RMBS Cấp 2B*: **25%**;
  - *Bảo đảm bằng Tài sản Cấp 2B khác*: **50%**;
  - *Cho vay ký quỹ (Margin loans) bảo đảm bằng tài sản phi HQLA*: **50%**;
  - *Bảo đảm bằng tài sản phi HQLA khác*: **100%**;
  - *Ngoại lệ*: Nếu TSBĐ nhận về được tái sử dụng (rehypothecated) để che chắn vị thế bán khống kéo dài quá 30 ngày: **0%** cho mọi loại tài sản;
- **Các dòng tiền vào bị loại trừ (0% Inflow)**:
  - *Hạn mức cam kết tín dụng/thanh khoản nhận được*: **0%**;
  - *Tiền gửi hoạt động gửi tại các định chế khác hoặc ngân hàng hợp tác trung ương*: **0%**;
- **Dòng tiền thu hồi theo đối tác**:
  - *Khách hàng cá nhân và SME*: **50%** (giả định cho vay mới 50%);
  - *Doanh nghiệp lớn phi tài chính, Chính phủ, MDBs, PSEs*: **50%**;
  - *Định chế tài chính và NHTW*: **100%** (không cho vay mới);
  - *Chứng khoán phi HQLA đáo hạn $\le 30$ ngày*: **100%**;
- **Dòng tiền vào phái sinh ròng**: **100%** (tính ròng trừ nghĩa vụ TSBĐ nếu bảo đảm bằng HQLA).

**2. Kiến trúc cân bằng toán học tổng thể của LCR (Annex 1 & Annex 4)**

Sự tương tác đồng bộ giữa cơ chế đảo ngược giao dịch tài trợ có bảo đảm ngắn hạn (unwinding of SFTs $\le 30$ ngày), công thức khống chế trần tài sản Cấp 2/Cấp 2B và trần dòng tiền vào 75% tạo thành hệ phương trình cân bằng thanh khoản khép kín của Basel III (bcbs_238, file bcbs238.md, Annex 1 & 4, d.863–876, 1262–1263):

**Bước 1: Mô phỏng đảo ngược SFT để xác định HQLA điều chỉnh (Adjusted Assets)**:
$$\text{Adjusted Level 1} = \text{Level 1} + \text{Unwind Level 1 SFT Outflows} - \text{Unwind Level 1 SFT Inflows}$$
$$\text{Adjusted Level 2A} = \text{Level 2A} + \text{Unwind Level 2A SFT Outflows} - \text{Unwind Level 2A SFT Inflows}$$
$$\text{Adjusted Level 2B} = \text{Level 2B} + \text{Unwind Level 2B SFT Outflows} - \text{Unwind Level 2B SFT Inflows}$$

**Bước 2: Xác định các khoản điều chỉnh vượt trần (Cap Adjustments)**:
$$\text{Adjustment for 15\% cap} = \max\left(\text{Adjusted L2B} - \frac{15}{85}\left(\text{Adjusted L1} + \text{Adjusted L2A}\right),\ \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\ 0\right)$$
$$\text{Adjustment for 40\% cap} = \max\left(\left(\text{Adjusted L2A} + \text{Adjusted L2B} - \text{Adjustment for 15\% cap}\right) - \frac{2}{3}\text{Adjusted L1},\ 0\right)$$

**Bước 3: Xác định Lượng HQLA được công nhận (Stock of HQLA)**:
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - \text{Adjustment for 15\% cap} - \text{Adjustment for 40\% cap}$$

**Bước 4: Áp dụng Chốt chặn Trần Dòng tiền vào 75% để xác định Dòng tiền ra ròng**:
$$\text{Total Net Cash Outflows} = \text{Total Cash Outflows} - \min\left(\text{Total Cash Inflows},\ 0{,}75 \times \text{Total Cash Outflows}\right)$$

**Bước 5: Thẩm định Tỷ lệ LCR cuối cùng**:
$$\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total Net Cash Outflows}} \ge 100\%$$

Kiến trúc toán học này triệt tiêu hoàn toàn khả năng các ngân hàng thao túng thanh khoản thông qua các giao dịch kỹ thuật trên thị trường tiền tệ ngắn hạn, gắn kết mật thiết với các tỷ lệ an toàn cấu trúc dài hạn tại [[basel-iii-net-stable-funding-ratio-nsfr-enforces-structural-funding-stability]] và trần đòn bẩy không trọng số rủi ro tại [[basel-iii-leverage-ratio-constrains-unweighted-balance-sheet-expansion]].

Xem thêm: [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]], [[hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions]], [[basel-iii-cash-inflows-and-75-percent-cap-framework-safeguards-minimum-hqla-buffer]], [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk]], [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[secured-lending-and-counterparty-cash-inflow-matrices-calibrate-rehypothecation-risk]], [[basel-iii-liquidity-risk-monitoring-tools-complement-contractual-and-market-oversight]], [[alternative-liquidity-approaches-eligibility-assessment-principles-and-governance]].
