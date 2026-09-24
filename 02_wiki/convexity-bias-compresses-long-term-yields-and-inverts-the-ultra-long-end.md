---
title: convexity-bias-compresses-long-term-yields-and-inverts-the-ultra-long-end
type: concept
tags: [yield-curve, convexity, term-structure, quantitative-finance]
sources: [fixed_income_during, choudhry_analysing_yield_curve]
status: stable
last_updated: 2026-09-24
---

Thiên lệch độ lồi biểu thị tác động nén giảm lợi suất dài hạn bắt nguồn từ đặc tính phi tuyến của mối quan hệ giữa giá và lợi suất trái phiếu (fixed_income_during, Ch.20, Convexity Bias, d.68–78). Khi thị trường biến động, một danh mục trung hòa thời lượng sở hữu độ lồi dương sẽ tự động tích lũy thặng dư vốn khi tái cân bằng phòng hộ, trong khi vị thế độ lồi âm chịu suy hao tài sản liên tục (fixed_income_during, Ch.20, Convexity Bias, d.74–76). Nhận thức được quy luật này, các nhà đầu tư trên thị trường trái phiếu đòi hỏi một mức lợi suất cao hơn để bù đắp cho các cấu trúc có độ lồi âm, định hình nên độ cong thực tế của cấu trúc kỳ hạn (fixed_income_during, Ch.20, Convexity Bias, d.76–78).

Về mặt vi tích phân ngẫu nhiên, nguồn gốc giải tích của thiên lệch độ lồi được thiết lập từ [[bond-price-diffusion-derives-duration-scaling-and-quadratic-convexity-drift-from-yield-dynamics|phương trình vi phân giá trái phiếu chiết khấu]], trong đó đạo hàm bậc hai Itô tạo ra số hạng trôi dạt dương $+\frac{1}{2}s^2(T-t)^2$ tỷ lệ thuận với bình phương thời gian đáo hạn $(T-t)^2$ (choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2480–2483). Hiệu ứng này mang tính chất đối ngẫu với số hạng khấu trừ độ lồi trong [[itos-lemma-derives-the-lognormal-asset-price-distribution-via-convexity-drag-correction]], mang lại mức thặng dư tỷ suất sinh lời vượt trội cho người nắm giữ chứng khoán dài hạn khi lợi suất biến động. Ở các kỳ hạn siêu dài từ 30 năm trở lên, khi các yếu tố kỳ vọng chính sách và phần bù rủi ro kỳ hạn đã tiệm cận trạng thái bão hòa, giá trị tích lũy theo hàm bậc hai của độ lồi tiếp tục tăng nhanh, kéo tụt lợi suất danh nghĩa và gây ra hiện tượng đảo ngược tự nhiên ở đoạn cuối đường cong lợi suất (fixed_income_during, Ch.20, Convexity Bias, d.84–85; choudhry_analysing_yield_curve, Ch.4, Example 4.2(ii), d.2480–2483).

Quy luật thiên lệch độ lồi này giải thích hiện tượng đảo chiều đường cong kết hợp với phân rã nợ gốc trong [[bond-convexity-exhibits-non-monotonic-maturity-scaling-at-ultra-long-horizons]], tạo lực đối trọng với các bước dịch chuyển song song tại [[parallel-yield-curve-shifts-reflect-shifts-in-equilibrium-neutral-rates-and-central-bank-commitments]], và tương tác với các hành vi phòng hộ thể chế tại [[institutional-preferred-habitats-and-solvency-regulations-induce-structural-short-convexity]].
