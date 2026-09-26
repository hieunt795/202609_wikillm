---
title: "Funds Transfer Pricing as an IRRBB Risk Transfer and Steering Mechanism"
tags:
  - concept
  - alm
  - irrbb
  - ftp
  - maturity-transformation
  - risk-transfer
  - bcbs-368
---

Định giá Chuyển nhượng Vốn Nội bộ (Funds Transfer Pricing - FTP) dưới lăng kính BCBS 368 không chỉ là một công cụ kế toán quản trị phân bổ chi phí mà là cơ chế cốt lõi để cô lập, điều chuyển và tập trung hóa toàn bộ rủi ro lãi suất (Maturity mismatch risk, Basis risk, Option risk) từ các đơn vị kinh doanh tiền tuyến về Treasury/ALM desk, bảo đảm các đơn vị kinh doanh chỉ chịu trách nhiệm về biên thương mại và rủi ro tín dụng trong khi rủi ro thị trường được quản trị và kiểm soát tập trung (bcbs_368, file d368.md, Principle 3, d.153–168; Annex 1.2.6 & 1.3, d.900–925).

**1. Cơ chế Tách biệt Rủi ro và Bảo toàn Biên độ Thương mại (Commercial Margin)**

Trong mô hình ngân hàng truyền thống, rủi ro hoán đổi kỳ hạn nảy sinh tự nhiên từ hoạt động kinh doanh: Đơn vị Kinh doanh Tín dụng (Lending BU) giải ngân các khoản vay dài hạn lãi suất cố định, trong khi Đơn vị Kinh doanh Nguồn vốn (Deposit BU) huy động các khoản tiền gửi ngắn hạn lãi suất thả nổi. Nếu không có hệ thống FTP kỳ hạn tương ứng (Matched-Maturity FTP):
- Biên lãi thuần ($NIM$) của các chi nhánh sẽ hoàn toàn phụ thuộc vào chu kỳ lãi suất vĩ mô thay vì hiệu quả khai thác khách hàng. Khi lãi suất thị trường tăng cao, chi phí huy động vốn đội lên sẽ xóa sạch lợi nhuận của chi nhánh cho vay dài hạn, mặc dù cán bộ tín dụng đã thẩm định rủi ro tín dụng xuất sắc.
- Ngược lại, chi nhánh huy động vốn sẽ vô tình được hưởng lợi giả tạo khi lãi suất tăng mà không xuất phát từ nỗ lực cạnh tranh thực tế.

Hệ thống FTP xử lý triệt để xung đột này bằng cách thiết lập Treasury đóng vai trò là ngân hàng nội bộ trung tâm (Internal Bank):
- **Phía Tài sản (Khoản vay cố định 5 năm, lãi suất hợp đồng $8{,}0\%$):** Lending BU "bán" khoản vay này cho Treasury tại mức lãi suất FTP kỳ hạn 5 năm tương ứng (ví dụ: $6{,}2\%$). Biên lợi nhuận cho vay $\text{Margin}_{\text{Lend}} = 8{,}0\% - 6{,}2\% = 1{,}8\%$ được cố định xuyên suốt 5 năm, hoàn toàn miễn nhiễm với biến động của thị trường.
- **Phía Nguồn vốn (Khoản tiền gửi 6 tháng, lãi suất huy động $4{,}0\%$):** Deposit BU "chuyển giao" nguồn vốn cho Treasury tại mức lãi suất FTP kỳ hạn 6 tháng (ví dụ: $4{,}8\%$). Biên lợi nhuận huy động $\text{Margin}_{\text{Dep}} = 4{,}8\% - 4{,}0\% = 0{,}8\%$ được bảo toàn.
- **Tại Treasury Desk:** Treasury ghi nhận dòng tiền nhận từ Lending BU ($6{,}2\%$) và trả cho Deposit BU ($4{,}8\%$), tạo ra Biên chênh lệch kỳ hạn chuyển đổi (Maturity Transformation Spread) $= 6{,}2\% - 4{,}8\% = 1{,}4\%$. 

Toàn bộ rủi ro không khớp kỳ hạn (repricing gap risk) và rủi ro giá trị kinh tế ($\Delta EVE$) được tập trung trọn vẹn tại Treasury. Treasury sẽ quyết định thực hiện phòng hộ vĩ mô ([[macro-hedging-and-micro-hedging-strategies-in-the-banking-book]]) thông qua các công cụ phái sinh ngoài thị trường liên ngân hàng hoặc duy trì trạng thái mở trong giới hạn khẩu vị rủi ro do HĐQT phê duyệt.

**2. Bóc tách Đa thành phần của Đường cong FTP (Multi-Component FTP)**

Hệ thống FTP chuẩn mực cao theo khuyến nghị của BCBS 368 không sử dụng một đường cong lãi suất đơn lẻ mà bóc tách giá chuyển nhượng thành bốn cấu phần rủi ro vi mô độc lập:

$$\text{FTP}_{\text{Asset}} = R_{\text{Base}}(T) + LP(T) + BS(T) + OC_{\text{Prepayment}}$$

$$\text{FTP}_{\text{Liability}} = R_{\text{Base}}(T) + LP(T) - OC_{\text{Withdrawal}}$$

Trong đó:
- $R_{\text{Base}}(T)$: Lãi suất phi rủi ro chuẩn (Benchmark / Risk-Free Rate) tại kỳ hạn khớp dòng tiền $T$.
- $LP(T)$: Phần bù thanh khoản kỳ hạn (Term Liquidity Premium), bù đắp chi phí huy động nguồn vốn dài hạn phòng ngừa rủi ro tắc nghẽn thanh khoản theo chuẩn Basel III ([[basel-iii-liquidity-coverage-ratio-lcr-mandates-short-term-resilience-buffers]]).
- $BS(T)$: Phần bù rủi ro cơ sở (Basis Spread), định giá phần chênh lệch giữa các chỉ số lãi suất tham chiếu (ví dụ: chênh lệch giữa SOFR và lãi suất liên ngân hàng không bảo đảm).
- $OC_{\text{Prepayment}}$ và $OC_{\text{Withdrawal}}$: Phí quyền chọn hành vi (Behavioural Option Charges). Đối với các khoản vay cho phép khách hàng trả nợ trước hạn không phạt, Treasury áp thêm một khoản phụ phí $OC_{\text{Prepayment}}$ (ví dụ: $+20 \text{ bps}$) vào giá vốn cấp cho chi nhánh. Chi phí này tạo lập nguồn ngân sách để Treasury mua các hợp đồng Swaption hoặc Cap/Floor trên thị trường phái sinh nhằm triệt tiêu trạng thái độ lồi âm ([[effective-duration-and-effective-convexity-for-banking-book-optionalities]]).

**3. Cơ chế Định giá FTP cho Tiền gửi Không Kỳ hạn (NMDs)**

Tiền gửi không kỳ hạn (CASA) là cấu phần nhạy cảm bậc nhất trên bảng cân đối kế toán ngân hàng. Do không có kỳ hạn pháp lý xác định, việc định giá FTP cho NMDs theo lãi suất qua đêm (Overnight rate) là một sai lầm nghiêm trọng, khiến chi nhánh bị thiệt thòi và không có động lực giữ chân nguồn vốn chi phí thấp ổn định.

Treasury khắc phục điều này bằng việc gắn giá FTP của NMDs với Danh mục Mô phỏng hành vi ([[replicating-portfolio-optimization-methodology-for-nmds-and-equity]]):
- Dựa trên chuỗi số liệu lịch sử 5–10 năm, danh mục NMDs được phân rã thành Cấu phần biến động (Non-core / Volatile) và Cấu phần lõi ổn định (Core).
- Cấu phần phi lõi được định giá FTP theo lãi suất thị trường tiền tệ ngắn hạn ($1\text{M}$ hoặc Overnight).
- Cấu phần lõi được phân bổ vào các dải kỳ hạn trung và dài hạn (tái đầu tư cuốn chiếu $1$ đến $5$ năm theo các trần quy định của Basel 368 Bảng 2). Giá FTP trả cho chi nhánh huy động là lợi suất bình quân gia quyền của danh mục mô phỏng ($R^{\text{rep}}$).
- Cơ chế này tạo ra một "tấm đệm thu nhập" mượt mà cho chi nhánh, đồng thời điều chuyển rủi ro rút vốn và rủi ro định giá lại dài hạn về cho Treasury quản trị.

**4. Điều hướng Chiến lược Bảng Cân đối và Thanh tra Giám sát SREP**

Dưới góc độ Principle 3 và Principle 10 của BCBS 368:
- **Công cụ Điều hướng (Balance Sheet Steering):** ALCO và Ban điều hành sử dụng biểu giá FTP như một công cụ điều tiết hành vi kinh doanh linh hoạt. Khi bài kiểm tra ngoại lai ([[supervisory-outlier-test-mandates-fifteen-percent-tier-one-capital-threshold]]) cảnh báo rủi ro $\Delta EVE$ đang tiệm cận trần $15\%$ Vốn cấp 1 do danh mục tài sản quá dài hạn, Treasury có thể chủ động nâng biểu lãi suất FTP cho vay dài hạn để hạn chế chi nhánh tăng trưởng sản phẩm này, đồng thời giảm giá FTP huy động dài hạn để khuyến khích hút tiền gửi kỳ hạn lớn.
- **Thanh tra Giám sát SREP:** Cơ quan giám sát thẩm định chặt chẽ tính minh bạch và khách quan của hệ thống FTP. Nghiêm cấm các trường hợp "trợ giá chéo" phi thị trường hoặc các thỏa thuận định giá ưu đãi ngầm nhằm làm đẹp kết quả kinh doanh của các đơn vị chiến lược, bởi sự méo mó trong FTP sẽ phá vỡ toàn bộ kỷ luật định giá rủi ro và làm tê liệt hệ thống cảnh báo sớm IRRBB của ngân hàng.
