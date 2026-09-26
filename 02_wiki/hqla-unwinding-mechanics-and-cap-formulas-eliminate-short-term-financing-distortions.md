---
title: hqla-unwinding-mechanics-and-cap-formulas-eliminate-short-term-financing-distortions
type: concept
tags: [banking, alm, liquidity-risk, lcr, hqla, unwinding, cap-formulas, repo, securities-financing, haircuts, basel, basel-iii, bcbs-238]
sources: [bcbs_238]
status: stable
last_updated: 2026-09-26
---

Cơ chế đảo ngược giao dịch tài trợ ngắn hạn và công thức khống chế trần cơ cấu danh mục HQLA (HQLA Unwinding Mechanics and Cap Formulas) theo chuẩn mực Basel III (BCBS 238) thiết lập các công thức toán học định lượng chuẩn xác nhằm loại bỏ triệt để hiện tượng bóp méo thanh khoản sổ sách phát sinh từ các giao dịch tài trợ có bảo đảm ngắn hạn, bảo đảm rằng bộ đệm thanh khoản của ngân hàng không phụ thuộc quá mức vào các tài sản có phẩm cấp thấp hơn Cấp 1 sau khi đã kiểm soát nghiêm ngặt trần 40% đối với tài sản Cấp 2 và trần 15% đối với tài sản Cấp 2B (bcbs_238, file bcbs238.md, Part 1 Section II.A.4, Paragraphs 46–48, d.222–224; Annex 1, Paragraphs 1–6, d.848–876).

**1. Bản chất và sự cần thiết của Cơ chế đảo ngược kỳ hạn (Unwinding Mechanics)**

Trong hoạt động kho quỹ thường nhật, các ngân hàng thương mại liên tục tham gia các giao dịch tài trợ chứng khoán ngắn hạn (Securities Financing Transactions - SFTs), bao gồm:
- **Tài trợ có bảo đảm (Secured funding / Repo)**: Vay tiền mặt bằng cách thế chấp tài sản;
- **Cho vay có bảo đảm (Secured lending / Reverse repo)**: Cho vay tiền mặt và nhận về tài sản bảo đảm;
- **Hoán đổi tài sản bảo đảm (Collateral swaps)**: Hoán đổi một loại chứng khoán này lấy một loại chứng khoán khác có phẩm cấp thanh khoản khác nhau.

Nếu quy định giám sát chỉ đo lường cơ cấu tài sản đang hiện diện vật lý trong kho tại thời điểm báo cáo (Day 0), ngân hàng có thể dễ dàng thực hiện hành vi "làm đẹp sổ sách" (window dressing). Ví dụ: một ngân hàng nắm giữ quá nhiều tài sản Cấp 2 có thể thực hiện một hợp đồng Repo kỳ hạn 7 ngày để tạm thời đổi tài sản Cấp 2 lấy tiền mặt (tài sản Cấp 1), từ đó nhân tạo hạ tỷ trọng Cấp 2 xuống dưới trần 40% tại ngày chốt số liệu. Khi hợp đồng Repo đáo hạn sau 7 ngày, tiền mặt bị rút đi và tài sản Cấp 2 quay trở lại, khiến cấu trúc thanh khoản thực tế bị vỡ vụn ngay giữa chu kỳ stress 30 ngày (Annex 1, Paragraph 1–4, d.852–855).

Để ngăn chặn thủ thuật này, BCBS 238 bắt buộc ngân hàng phải **đảo ngược toàn bộ (unwind)** các giao dịch SFT và hoán đổi TSBĐ có ngày đáo hạn hợp đồng trong vòng **30 ngày calendar tiếp theo** có liên quan đến việc hoán đổi tài sản HQLA:
- Ngân hàng phải giả định hoàn trả lại toàn bộ tiền mặt hoặc tài sản bảo đảm đã nhận và nhận lại toàn bộ tài sản bảo đảm ban đầu của mình;
- Nếu tài sản bảo đảm nhận về đã bị đem đi tái thế chấp (rehypothecated) trong một giao dịch khác đáo hạn trong 30 ngày, toàn bộ chuỗi giao dịch liên quan đều phải được đảo ngược đồng thời;
- Toàn bộ các tỷ lệ chiết khấu quy định (haircuts: 15% cho Cấp 2A, 25% hoặc 50% cho Cấp 2B) phải được áp dụng đầy đủ **trước khi** đưa vào công thức tính toán trần.

**2. Xác định các đại lượng tài sản sau khi đảo ngược (Adjusted Amounts)**

Các biến số đầu vào sau khi đảo ngược giao dịch được xác định như sau (bcbs_238, file bcbs238.md, Annex 1, Paragraph 4, d.855):
- $\text{Level 1}$, $\text{Level 2A}$, $\text{Level 2B}$: Giá trị thị trường thực tế của các tài sản đang nắm giữ tại ngày báo cáo, sau khi đã nhân với hệ số thanh khoản quy chuẩn (tức Cấp 1 nhân $100\%$, Cấp 2A nhân $85\%$, Cấp 2B nhân $75\%$ hoặc $50\%$);
- $\text{Adjusted Level 1}$: Khối lượng tài sản Cấp 1 (bao gồm cả tiền mặt) thu được sau khi đã đảo ngược toàn bộ các giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi TSBĐ kỳ hạn $\le 30$ ngày liên quan đến HQLA và Level 1;
- $\text{Adjusted Level 2A}$: Khối lượng tài sản Cấp 2A sau khi đã đảo ngược các giao dịch tương ứng và áp dụng haircut 15%;
- $\text{Adjusted Level 2B}$: Khối lượng tài sản Cấp 2B sau khi đã đảo ngược các giao dịch tương ứng và áp dụng haircut 25% hoặc 50%.

**3. Cơ sở logic toán học của các tỷ lệ trần 40% và 15%**

Quy định chuẩn mực Basel III thiết lập hai mức trần cơ cấu tối đa trong tổng danh mục HQLA:
1. **Trần Cấp 2 tối đa 40% danh mục**:
   - Nếu tổng HQLA bao gồm tối đa $40\%$ là Cấp 2 (Level 2A + Level 2B), thì phần còn lại dành cho Cấp 1 tối thiểu phải chiếm $60\%$;
   - Tỷ số tương quan giới hạn giữa Cấp 2 và Cấp 1 là:
     $$\frac{\text{Cấp 2}}{\text{Cấp 1}} \le \frac{40\%}{60\%} = \frac{2}{3}$$
   - Do đó, khối lượng tài sản Cấp 2 tối đa được phép công nhận không được vượt quá **hai phần ba ($\frac{2}{3}$)** khối lượng tài sản Cấp 1 sau điều chỉnh;
2. **Trần Cấp 2B tối đa 15% danh mục**:
   - Tài sản Cấp 2B bị giới hạn tối đa không quá $15\%$ tổng danh mục HQLA, đồng nghĩa phần danh mục còn lại gồm Cấp 1 và Cấp 2A phải chiếm tối thiểu $85\%$;
   - Tỷ số tương quan giới hạn là:
     $$\frac{\text{Cấp 2B}}{\text{Cấp 1} + \text{Cấp 2A}} \le \frac{15\%}{85\%} = \frac{15}{85}$$
   - Trường hợp đặc biệt khi trần 40% của Cấp 2 bị chạm và ngân hàng không nắm giữ tài sản Cấp 2A (hoặc Cấp 2A rất nhỏ), thì tỷ lệ Cấp 2B tối đa trên Cấp 1 sẽ là:
     $$\frac{\text{Cấp 2B}}{\text{Cấp 1}} \le \frac{15\%}{60\%} = \frac{15}{60} = \frac{1}{4}$$

**4. Hệ thống công thức toán học chính xác tuyệt đối theo Annex 1**

Theo quy định tại Paragraph 5 của Annex 1 (bcbs_238, file bcbs238.md, d.865–872), giá trị của danh mục tài sản thanh khoản cao hợp lệ ($\text{Stock of HQLA}$) được xác định qua trình tự 3 công thức toán học nghiêm ngặt:

**Bước 1: Tính toán Phần điều chỉnh vượt trần 15% của Cấp 2B ($\text{Adjustment for 15\% cap}$)**
$$\text{Adjustment for 15\% cap} = \max\left( \text{Adjusted Level 2B} - \frac{15}{85} \times (\text{Adjusted Level 1} + \text{Adjusted Level 2A}),\ \text{Adjusted Level 2B} - \frac{15}{60} \times \text{Adjusted Level 1},\ 0 \right)$$

**Bước 2: Tính toán Phần điều chỉnh vượt trần 40% của Cấp 2 ($\text{Adjustment for 40\% cap}$)**
Phần tài sản Cấp 2B đã bị khấu trừ do vượt trần 15% ở Bước 1 sẽ được loại bỏ trước khi tính toán trần 40% nhằm tránh việc phạt trùng lặp hai lần:
$$\text{Adjustment for 40\% cap} = \max\left( \left(\text{Adjusted Level 2A} + \text{Adjusted Level 2B} - \text{Adjustment for 15\% cap}\right) - \frac{2}{3} \times \text{Adjusted Level 1},\ 0 \right)$$

**Bước 3: Xác định Giá trị danh mục HQLA hợp lệ tính vào tử số LCR**
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - \text{Adjustment for 15\% cap} - \text{Adjustment for 40\% cap}$$

**5. Công thức gộp tương đương (Alternative Combined Formula)**

Tại Paragraph 6 của Annex 1 (bcbs_238, file bcbs238.md, d.873–876), Ủy ban Basel cung cấp một công thức toán học gộp tương đương hoàn toàn về mặt đại số:
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - \max\left( (\text{Adjusted Level 2A} + \text{Adjusted Level 2B}) - \frac{2}{3} \times \text{Adjusted Level 1},\ \text{Adjusted Level 2B} - \frac{15}{85} \times (\text{Adjusted Level 1} + \text{Adjusted Level 2A}),\ 0 \right)$$

Công thức gộp này chỉ ra rằng: phần giá trị tài sản bị loại trừ khỏi kho HQLA chính là giá trị lớn nhất (maximum) giữa:
1. Mức vượt trần 40% của toàn bộ tài sản Cấp 2 so với $\frac{2}{3}$ tài sản Cấp 1 điều chỉnh;
2. Mức vượt trần 15% của tài sản Cấp 2B so với $\frac{15}{85}$ tổng tài sản Cấp 1 và Cấp 2A điều chỉnh;
3. Số 0 (khi cả hai trần đều không bị vi phạm).

**6. Minh họa tính toán số học thực tế**

Giả sử một ngân hàng thương mại sau khi unwind toàn bộ các giao dịch SFT kỳ hạn $\le 30$ ngày và nhân các hệ số haircut quy chuẩn có các giá trị điều chỉnh như sau:
- $\text{Adjusted Level 1} = 100$ triệu USD;
- $\text{Adjusted Level 2A} = 50$ triệu USD;
- $\text{Adjusted Level 2B} = 40$ triệu USD;
- Giá trị thực tế nắm giữ chưa unwind: $\text{Level 1} = 100$, $\text{Level 2A} = 50$, $\text{Level 2B} = 40$.

Áp dụng quy trình tính toán:
1. *Kiểm tra trần 15%*:
   - $\frac{15}{85} \times (\text{Adjusted Level 1} + \text{Adjusted Level 2A}) = \frac{15}{85} \times (100 + 50) = \frac{15}{85} \times 150 \approx 26{,}47$ triệu USD;
   - $\frac{15}{60} \times \text{Adjusted Level 1} = \frac{15}{60} \times 100 = 25{,}00$ triệu USD;
   - $\text{Adjustment for 15\% cap} = \max(40 - 26{,}47;\ 40 - 25{,}00;\ 0) = \max(13{,}53;\ 15{,}00;\ 0) = 15{,}00$ triệu USD;
2. *Kiểm tra trần 40%*:
   - Tổng Cấp 2 còn lại sau khi trừ trần 15%: $(50 + 40 - 15{,}00) = 75{,}00$ triệu USD;
   - Mức tối đa $\frac{2}{3} \times \text{Adjusted Level 1} = \frac{2}{3} \times 100 \approx 66{,}67$ triệu USD;
   - $\text{Adjustment for 40\% cap} = \max(75{,}00 - 66{,}67;\ 0) = 8{,}33$ triệu USD;
3. *Giá trị kho HQLA hợp lệ*:
   $$\text{Stock of HQLA} = 100 + 50 + 40 - 15{,}00 - 8{,}33 = 166{,}67 \text{ triệu USD}$$
   - *Kiểm tra lại cơ cấu*: Cấp 1 chiếm $100 / 166{,}67 = 60{,}0\%$; Cấp 2 được công nhận là $66{,}67 / 166{,}67 = 40{,}0\%$; trong đó Cấp 2B là $(40 - 15) = 25$ triệu USD, chiếm đúng $25 / 166{,}67 = 15{,}0\%$. Toàn bộ tỷ lệ cơ cấu đạt mức trần tuyệt đối theo luật định.

Xem thêm: [[basel-iii-lcr-short-term-liquidity-stress-framework-and-buffer-usability]], [[hqla-fundamental-and-market-characteristics-govern-asset-liquidity-qualification]], [[hqla-operational-requirements-enforce-unencumbered-status-and-treasury-control]], [[hqla-asset-categorisation-and-haircut-parameters-define-liquidity-tiers]], [[alternative-liquidity-approaches-ala-resolve-jurisdictional-hqla-structural-deficits]], [[contractual-cash-inflow-caps-and-counterparty-haircuts-govern-net-lcr-measurement]], [[collateral-management-framework-differentiates-encumbered-assets-and-monitors-tied-positions]], [[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]].
