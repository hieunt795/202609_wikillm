---
title: unsecured-wholesale-funding-run-off-matrices-calibrate-counterparty-flight-risk
type: concept
tags: [banking, alm, liquidity-risk, lcr, wholesale-funding, unsecured-funding, run-off-rates, corporate-deposits, financial-institutions, basel, basel-iii, bcbs-238]
sources: [bcbs_238]
status: stable
last_updated: 2026-09-26
---

Ma trận xác định tỷ lệ rút vốn nợ bán buôn không bảo đảm (Unsecured Wholesale Funding Run-off Matrices) theo chuẩn mực Basel III (BCBS 238) thiết lập thang đo lượng hóa rủi ro tháo chạy nguồn vốn (flight risk) trong chân trời 30 ngày căng thẳng, phân tầng tỷ lệ rút tiền từ 20% đến 100% dựa trên bản chất tổ chức của bên cung cấp vốn, mức độ nhạy cảm tinh vi đối với lãi suất và khả năng thanh toán của ngân hàng, cũng như sự hiện diện của các cơ chế bảo hiểm tiền gửi hoặc bảo lãnh công quyền (bcbs_238, file bcbs238.md, Part 1 Section II.B.1.ii, Paragraphs 85–111, d.423–482).

**1. Định nghĩa và phạm vi bao quát của Nợ bán buôn không bảo đảm**

Theo chuẩn tắc Basel III, nợ bán buôn không bảo đảm (Unsecured wholesale funding) là toàn bộ các khoản nợ phải trả và nghĩa vụ chung được huy động từ các đối tượng phi tự nhiên (non-natural persons, tức các pháp nhân kinh tế, bao gồm cả doanh nghiệp tư nhân, hộ kinh doanh và công ty hợp danh) mà không được bảo đảm bằng quyền pháp lý đối với các tài sản chỉ định thuộc sở hữu của ngân hàng trong trường hợp phá sản, giải thể hoặc tái cơ cấu (bcbs_238, file bcbs238.md, Paragraph 85, d.425). Các nghĩa vụ phát sinh từ hợp đồng phái sinh được tách riêng sang mục rủi ro bổ sung.

Phạm vi dòng tiền nợ bán buôn tính toán trong cửa sổ 30 ngày của LCR bao gồm (Paragraph 86–87, d.426–427):
- Toàn bộ nguồn vốn mà bên gửi tiền có quyền đòi lại (callable) trong vòng 30 ngày;
- Nguồn vốn có ngày đáo hạn hợp đồng sớm nhất nằm trong vòng 30 ngày (như tiền gửi có kỳ hạn, thương phiếu, chứng chỉ tiền gửi đáo hạn);
- Nguồn vốn không xác định ngày đáo hạn cụ thể;
- **Các quyền chọn mua lại/hoàn trả trước hạn (Call options)**: Toàn bộ nguồn vốn có điều khoản cho phép nhà đầu tư thực hiện quyền rút trước hạn trong 30 ngày. Đối với các quyền chọn thuộc quyền định đoạt của chính ngân hàng, cơ quan giám sát yêu cầu ngân hàng phải tính toán dòng tiền ra nếu thị trường kỳ vọng ngân hàng sẽ mua lại công cụ trước hạn nhằm bảo vệ danh tiếng (reputational factors), vì việc không thực hiện quyền chọn sẽ phát tín hiệu tiêu cực rằng ngân hàng đang kiệt quệ thanh khoản.

**2. Phân tầng Khách hàng doanh nghiệp phi tài chính và Thực thể công quyền (20% hoặc 40%)**

Nhóm đối tác này bao gồm các doanh nghiệp phi tài chính (không thuộc diện doanh nghiệp nhỏ SME), chính phủ trung ương, ngân hàng trung ương, các tổ chức khu vực công (PSEs) và các ngân hàng phát triển đa phương (MDBs) không có mối quan hệ tiền gửi hoạt động theo [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]]. Tỷ lệ rút vốn được phân định qua hai mức chuẩn mực (bcbs_238, file bcbs238.md, Paragraph 107–108, d.470–476):
- **Tỷ lệ rút vốn tiêu chuẩn 40%**: Áp dụng cho phần lớn các khoản tiền gửi phi hoạt động của doanh nghiệp và thực thể công quyền không được bảo hiểm đầy đủ (Paragraph 107). Tỷ lệ 40% phản ánh giả định rằng các doanh nghiệp lớn có bộ phận tài chính chuyên nghiệp sẽ nhanh chóng tái phân bổ dòng tiền nhàn rỗi hoặc chuyển sang các kênh an toàn hơn khi nhận thấy ngân hàng đối mặt với khủng hoảng; tuy nhiên, tốc độ rút tiền số hóa hiện đại có thể đẩy tỷ lệ tháo chạy này lên mức cao hơn nhiều [[digital-deposit-velocity-and-uninsured-deposit-concentration-accelerate-bank-runs]];
- **Tỷ lệ rút vốn ưu đãi 20%**: Được áp dụng khi và chỉ khi **toàn bộ số dư tiền gửi được bảo hiểm đầy đủ** bởi một hệ thống bảo hiểm tiền gửi hiệu quả hoặc được bảo lãnh thanh toán công quyền có giá trị bảo vệ tương đương (Paragraph 108). Sự hiện diện của bảo lãnh công toàn diện giúp triệt tiêu tâm lý hoảng loạn rút vốn của người quản lý tài chính doanh nghiệp.

**3. Phân tầng Định chế tài chính và các Pháp nhân khác (Tỷ lệ rút 100%)**

Khác với khu vực kinh tế thực, các tổ chức thuộc khu vực tài chính có mức độ nhạy cảm rủi ro cực đoan và phản ứng rút vốn tức thì khi xuất hiện bất kỳ dấu hiệu căng thẳng nào. Do đó, BCBS 238 quy định tỷ lệ rút vốn triệt để **100%** đối với toàn bộ nguồn vốn bán buôn không bảo đảm huy động từ (bcbs_238, file bcbs238.md, Paragraph 109, d.479):
- Các định chế tài chính khác: ngân hàng thương mại, ngân hàng đầu tư, công ty chứng khoán, doanh nghiệp bảo hiểm và tái bảo hiểm;
- Các bên nhận ủy thác quản lý tài sản (Fiduciaries, như các quỹ hưu trí, quỹ tương hỗ, quỹ đầu tư tập thể theo Footnote 43, d.488);
- Các bên thụ hưởng (Beneficiaries) theo hợp đồng bảo hiểm, niên kim hoặc quỹ tín thác;
- Các công ty phục vụ mục đích đặc biệt (SPVs/SPEs), quỹ liên kết đầu tư (conduits);
- **Các công ty liên kết của chính ngân hàng (Affiliated entities, Footnote 45, d.492)**: Trừ khi khoản tiền gửi thuộc khuôn khổ quan hệ dịch vụ hoạt động hoặc mạng lưới hợp tác xã, tiền gửi từ các công ty con/công ty liên kết bị giả định rút chạy 100% nhằm phản ánh rào cản chia cắt thanh khoản nội bộ trong khủng hoảng;
- Toàn bộ các pháp nhân kinh tế khác không thuộc diện doanh nghiệp phi tài chính hay thực thể công quyền.

**4. Quy chế đối xử với Giấy tờ có giá và Trái phiếu do ngân hàng phát hành (100% Run-off)**

Toàn bộ các chứng khoán nợ, trái phiếu, kỳ phiếu và chứng chỉ tiền gửi (CDs/CPs) do ngân hàng phát hành đáo hạn trong vòng 30 ngày bắt buộc phải chịu tỷ lệ rút vốn **100%** bất kể người nắm giữ công cụ đó là ai (bcbs_238, file bcbs238.md, Paragraph 110, d.480). Giả định cơ sở là trong điều kiện thị trường đóng băng, ngân hàng sẽ hoàn toàn mất khả năng phát hành công cụ mới để đảo nợ (inability to rollover debt securities).

*Ngoại lệ duy nhất*: Ngân hàng chỉ được miễn trừ tỷ lệ 100% nếu chứng khoán nợ đó được thiết kế và **phát hành độc quyền cho thị trường bán lẻ**, được lưu ký trực tiếp trên các tài khoản bán lẻ (hoặc tài khoản SME đủ điều kiện), và tồn tại các điều khoản hạn chế pháp lý bảo đảm rằng các công cụ này tuyệt đối không thể được mua bán hay chuyển nhượng cho các nhà đầu tư tổ chức bán buôn. Khi đáp ứng đầy đủ điều kiện cách ly này, công cụ nợ mới được hưởng tỷ lệ rút vốn bán lẻ (từ 5% đến 10%+).

**5. Cơ chế tiền gửi trong Mạng lưới Tổ chức tín dụng Hợp tác (25% hoặc 100%)**

Đối với các mô hình mạng lưới ngân hàng hợp tác (cooperative banking networks) bao gồm nhiều tổ chức tín dụng tự chủ pháp lý nhưng liên kết chặt chẽ dưới một thương hiệu chung và có định chế trung tâm (central institution) thực hiện các chức năng điều phối vốn, BCBS 238 đưa ra khung đối xử chuyên biệt (Paragraph 105–106, d.467–469):
- Tiền gửi của các ngân hàng thành viên đặt tại định chế trung tâm được nhận tỷ lệ rút vốn **25%** nếu phát sinh từ: (i) yêu cầu duy trì số dư tiền gửi tối thiểu theo luật định; hoặc (ii) thỏa thuận chia sẻ nhiệm vụ và bảo vệ an toàn thanh khoản lẫn nhau (mutual protection scheme against insolvency);
- Ngược lại, nếu tiền gửi đặt tại định chế trung tâm nhằm mục đích kinh doanh đại lý (correspondent banking) hoặc ngoài các nghĩa vụ luật định trên, ngân hàng trung tâm phải áp dụng tỷ lệ rút vốn **100%**. Khoản tiền gửi này nhận tỷ lệ dòng tiền vào 0% đối với ngân hàng thành viên đi gửi.

**Bảng tổng hợp ma trận tỷ lệ rút vốn nợ bán buôn không bảo đảm**

| Loại hình nguồn vốn bán buôn không bảo đảm | Điều kiện cụ thể / Cơ cấu hợp đồng | Tỷ lệ rút vốn (Run-off) |
|---|---|---|
| **Khách hàng doanh nghiệp nhỏ (SME)** | Quy mô gộp $< 1$ triệu EUR, quản lý như bán lẻ | **5%** (ổn định) / $\ge 10\%$ (kém ổn định) |
| **Tiền gửi hoạt động (Operational)** | Phát sinh từ clearing, custody, cash management | **25%** (hoặc 3%–5% nếu có bảo hiểm) |
| **Mạng lưới ngân hàng hợp tác** | Tiền gửi dự trữ theo luật định hoặc quỹ tương trợ | **25%** (các mục đích khác: 100%) |
| **Doanh nghiệp phi tài chính & Công quyền** | Có bảo hiểm tiền gửi / bảo lãnh công đầy đủ | **20%** |
| **Doanh nghiệp phi tài chính & Công quyền** | Không có bảo hiểm tiền gửi đầy đủ (thông thường) | **40%** |
| **Định chế tài chính, Fiduciaries, SPVs** | Toàn bộ tiền gửi và nguồn vốn phi hoạt động | **100%** |
| **Chứng khoán nợ do ngân hàng phát hành** | Đáo hạn trong 30 ngày (trừ bán lẻ độc quyền) | **100%** |

Xem thêm: [[basel-iii-retail-deposit-run-off-framework-differentiates-stable-and-less-stable-funds]], [[operational-deposits-framework-evaluates-clearing-custody-and-cash-management-stickiness]], [[secured-funding-run-off-mechanics-map-collateral-hierarchy-and-counterparty-profiles]], [[contingent-liquidity-outflow-shocks-quantify-downgrades-derivatives-and-facility-drawdowns]], [[retail-and-wholesale-deposit-run-off-rates-differentiate-short-term-liquidity-outflows]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]].
