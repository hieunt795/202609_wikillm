---
title: replicating-portfolio-optimization-methodology-for-nmds-and-equity
type: concept
tags: [banking, alm, irrbb, replicating-portfolio, nmds, equity-modeling, optimization-algorithm, margin-stability, bcbs-368]
sources: [bcbs_368]
status: stable
last_updated: 2026-09-26
---

Phương pháp luận tối ưu hóa danh mục mô phỏng đối với tiền gửi không kỳ hạn và vốn tự có (Replicating Portfolio Optimization Methodology for NMDs and Equity) thiết lập thuật toán phân bổ tỷ trọng đầu tư cuốn chiếu liên tục nhằm tối thiểu hóa phương sai của biên lãi thuần (margin volatility) hoặc bảo vệ thu nhập ổn định theo Chuẩn mực BCBS 368 của Ủy ban Basel (bcbs_368, file d368.md, Annex 1.3.4–3.5, d.970–987; Footnote 38).

Trong quản trị ALM, tiền gửi không kỳ hạn (NMDs) và vốn chủ sở hữu (Equity) không có kỳ hạn đáo hạn theo hợp đồng xác định. Nếu ngân hàng coi toàn bộ nguồn vốn này là ngắn hạn qua đêm, thu nhập lãi thuần (NII) sẽ biến động dữ dội theo lãi suất thị trường; ngược lại, nếu gán kỳ hạn quá dài, ngân hàng sẽ gánh chịu rủi ro sụt giảm giá trị kinh tế ($\Delta EVE$) khổng lồ khi lãi suất tăng vọt. Kỹ thuật danh mục mô phỏng (Replicating Portfolio) là công cụ toán học chuẩn mực để giải quyết bài toán cân bằng này.

**Mục tiêu tài chính của Danh mục mô phỏng**

Mục tiêu cốt lõi của danh mục mô phỏng là chuyển hóa một nguồn vốn không kỳ hạn có quy mô $V_t$ và chi phí trả lãi $r_t^{\text{deposit}}$ thành một danh mục các tài sản lãi suất cố định đầu tư tái tục liên tục với các tỷ trọng trọng số $\{w_k\}$ trên các kỳ hạn $\{T_k\}$ sao cho (Annex 1.3.4, d.974; Footnote 38, d.1002):
- Lãi suất tạo ra từ danh mục mô phỏng ($R_t^{\text{rep}}$) bám sát sự biến động của chi phí trả lãi tiền gửi $r_t^{\text{deposit}}$ cộng thêm một biên độ lợi nhuận mục tiêu ổn định $\mu$;
- Triệt tiêu tối đa độ nhạy cảm của thu nhập lãi thuần trước các bước nhảy bất ngờ của lãi suất chính sách;
- Duy trì cấu trúc thời lượng ổn định trong dài hạn mà không đòi hỏi chi phí tái cân đối danh mục quá lớn.

**Thuật toán tối ưu hóa toán học (Mathematical Optimization Formulation)**

Ngân hàng lựa chọn một tập hợp các kỳ hạn đầu tư chuẩn $k \in \{1, 2, \dots, K\}$ (ví dụ: qua đêm, 1 tháng, 3 tháng, 6 tháng, 1 năm, 2 năm, 3 năm, 5 năm, 7 năm, 10 năm) với các vector lợi suất bình quân động tương ứng $\bar{Y}_t(T_k)$. Lợi suất tổng hợp của danh mục mô phỏng tại thời điểm $t$ được định nghĩa:

$$R_t^{\text{rep}} = \sum_{k=1}^K w_k \cdot \bar{Y}_t(T_k)$$

Bài toán tối ưu hóa nhằm tìm kiếm vector tỷ trọng tối ưu $\{w_k^*\}$ giải quyết hàm mục tiêu tối thiểu hóa phương sai chênh lệch lãi suất (Minimize Margin Variance):

$$\min_{\{w_k\}} \frac{1}{T} \sum_{t=1}^T \left( R_t^{\text{rep}} - r_t^{\text{deposit}} - \mu \right)^2 = \min_{\{w_k\}} \frac{1}{T} \sum_{t=1}^T \left( \sum_{k=1}^K w_k \cdot \bar{Y}_t(T_k) - r_t^{\text{deposit}} - \mu \right)^2$$

kết hợp với hệ thống các ràng buộc pháp lý và kỹ thuật chặt chẽ:
1. *Ràng buộc không bán khống (No short selling)*:
   $$w_k \ge 0, \quad \forall k \in \{1, \dots, K\}$$
2. *Ràng buộc bảo toàn ngân sách (Full allocation)*:
   $$\sum_{k=1}^K w_k = 1$$
3. *Ràng buộc trần kỳ hạn bình quân chuẩn hóa Basel (Table 2 Caps Constraint)*:
   Kỳ hạn bình quân gia quyền của danh mục mô phỏng đối với tiền gửi lõi bắt buộc không được vượt quá các ngưỡng trần quy chuẩn của BCBS 368 Bảng 2:
   $$\bar{T}_{\text{rep}} = \sum_{k=1}^K w_k \cdot T_k \le T_{\text{cap}}$$
   với $T_{\text{cap}} = 5{,}0$ năm cho Bán lẻ giao dịch, $4{,}5$ năm cho Bán lẻ phi giao dịch, và $4{,}0$ năm cho Bán buôn (Paragraph 115).
4. *Ràng buộc phần đệm thanh khoản qua đêm (Overnight liquidity buffer)*:
   Tỷ trọng phân bổ vào dải qua đêm $w_1$ (kỳ hạn $T_1 = 0{,}0028$ năm) bắt buộc phải lớn hơn hoặc bằng tỷ lệ tiền gửi phi lõi (non-core ratio) tối thiểu: $w_1 \ge 10\%$ cho bán lẻ giao dịch, $w_1 \ge 30\%$ cho bán lẻ phi giao dịch, và $w_1 \ge 50\%$ cho bán buôn.

**Cơ chế vận hành tái đầu tư cuốn chiếu liên tục (Rolling Reinvestment)**

Để duy trì các tỷ trọng tối ưu $\{w_k^*\}$ mà không làm biến động thời lượng của sổ ngân hàng theo thời gian, ALCO áp dụng cơ chế đầu tư cuốn chiếu (Footnote 38, d.1002):
- Đối với một cấu phần kỳ hạn $M$ tháng có tỷ trọng $w_M$, ngân hàng chia nhỏ phần vốn này thành $M$ phần bằng nhau;
- Mỗi tháng, chính xác $1/M$ quy mô của cấu phần đó sẽ đáo hạn và được ngân hàng tự động tái đầu tư vào một công cụ lãi suất cố định kỳ hạn $M$ tháng mới phát hành;
- *Cơ chế bình quân động*: Tại bất kỳ thời điểm nào, lợi suất nhận được từ cấu phần $M$ tháng này là mức bình quân số học của các mức lãi suất $M$ tháng trong suốt $M$ tháng vừa qua:

$$\bar{Y}_t(M) = \frac{1}{M} \sum_{s=0}^{M-1} Y_{t-s}(M)$$

Kỹ thuật này tạo ra một bộ lọc làm mịn (smoothing filter) hoàn hảo, triệt tiêu mọi biến động cục bộ của thị trường tiền tệ và đem lại dòng tiền lãi dự đoán được tuyệt đối cho ngân hàng.

**Rủi ro Tracking Error và Chi phí tái cân đối danh mục**

Mặc dù mang lại sự ổn định cao cho NII, mô hình danh mục mô phỏng tiềm ẩn các rủi ro kỹ thuật:
- *Rủi ro lệch pha bám sát (Tracking Error Risk)*: Xảy ra khi hệ số chuyển dịch lãi suất thực tế của tiền gửi (pass-through beta) thay đổi đột ngột do áp lực cạnh tranh gay gắt hoặc khi chính sách tiền tệ đảo chiều nhanh, khiến chi phí tiền gửi tăng nhanh hơn mức lãi suất bình quân động mà danh mục mô phỏng tạo ra.
- *Rủi ro tháo chạy số dư (Volume Outflow Risk)*: Khi tổng số dư tiền gửi NMDs sụt giảm thực tế, quy mô nguồn vốn tài trợ bị co hẹp trong khi danh mục tài sản mô phỏng vẫn duy trì kỳ hạn dài. Ngân hàng rơi vào trạng thái thừa phòng hộ (over-hedged), buộc phải bán tháo tài sản trước hạn hoặc thực hiện các hợp đồng hoán đổi trả lãi cố định (payer interest rate swaps) để đóng trạng thái, gánh chịu chi phí giao dịch và tổn thất vốn thực tế.

Mô hình tối ưu hóa danh mục mô phỏng này kết nối chặt chẽ với [[equity-endowment-effect-and-replicating-portfolio-in-alm]], định hình các tham số phân bổ dòng tiền trong [[standardised-nmd-categorisation-and-core-deposit-caps-framework]] và cung cấp cơ sở để giải thích sự biến thiên thu nhập trong [[delta-nii-regulatory-calculation-rules-mandate-constant-balance-sheet-and-rolling-horizon]].
