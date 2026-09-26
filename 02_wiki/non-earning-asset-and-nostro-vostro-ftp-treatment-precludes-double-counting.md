---
title: non-earning-asset-and-nostro-vostro-ftp-treatment-precludes-double-counting
type: concept
tags: [alm, ftp, cash-management, nostro-vostro, equity-investments, non-earning-assets, double-counting]
sources: [vab_ftp_methodology]
status: stable
last_updated: 2026-09-26
---

Trong cấu trúc bảng cân đối kế toán của ngân hàng, một bộ phận tài sản và công nợ mang tính chất phi thương mại hoặc phục vụ mục tiêu thanh khoản hệ thống như tiền mặt tồn quỹ, tài khoản vãng lai Nostro/Vostro liên ngân hàng, danh mục đầu tư cổ phiếu dài hạn và các tài sản có khác (vab_ftp_methodology, Điều 7, d.984). Nếu hệ thống FTP áp đặt giá chuyển nhượng nội bộ một cách cơ học lên các khoản mục này, ngân hàng sẽ phạm phải sai lầm tính trùng chi phí (double-counting), làm méo mó nghiêm trọng hiệu quả kinh doanh của các đơn vị vận hành (vab_ftp_methodology, Điều 7.1, d.990). Do đó, phương pháp luận FTP thiết lập các nguyên tắc phân loại và loại trừ chuyên biệt nhằm bảo đảm tính nhất quán kinh tế (vab_ftp_methodology, Điều 7.1–7.4, d.986–1025).

Đối với tiền mặt tồn quỹ tại các chi nhánh và phòng giao dịch, ngân hàng phân định rõ hai trạng thái:
- **Tiền mặt trong hạn mức tồn quỹ**: Không tính FTP mua bán vốn với Đơn vị Quản lý Vốn tập trung (CFU) vì tiền mặt thuộc danh mục tài sản thanh khoản cao của ngân hàng và chi phí cơ hội nắm giữ đã được phân bổ trọn vẹn vào giá bán vốn COF thông qua cấu phần phần bù tài sản thanh khoản cao (Liquidity Premium) theo [[regulatory-deposit-insurance-and-statutory-reserves-apportion-into-market-1-cof]] (vab_ftp_methodology, Điều 7.1, d.990);
- **Tiền mặt vượt hạn mức tồn quỹ**: Không tính FTP do đơn vị kinh doanh đã phải chịu chế tài phạt chi phí vượt hạn mức ngân quỹ theo quy định nội bộ của ngân hàng (vab_ftp_methodology, Điều 7.1, d.991).

Đối với các tài khoản Nostro và Vostro liên ngân hàng, cơ chế xử lý phản ánh vai trò thanh khoản đối ứng giữa các tổ chức tín dụng:
- **Tài khoản Nostro (bao gồm tiền gửi không kỳ hạn tại Ngân hàng Nhà nước và tiền gửi tại các tổ chức tín dụng khác)**: Đây là các tài sản thanh khoản cao cốt lõi được tính toán chi phí nắm giữ trong đệm thanh khoản chung, do đó CFU không áp dụng cơ chế mua bán vốn FTP với các đơn vị mở tài khoản (vab_ftp_methodology, Điều 7.2.a, d.997);
- **Tài khoản Vostro (tiền gửi không kỳ hạn của các tổ chức tín dụng khác mở tại ngân hàng)**: Đơn vị kinh doanh thu hút được số dư Vostro được CFU trả lãi theo giá mua vốn VOF Thị trường 2 tương ứng với kỳ hạn qua đêm (Overnight — ON), áp dụng cố định trong suốt thời gian duy trì số dư và phần bù thanh khoản kỳ hạn được ấn định bằng 0 (vab_ftp_methodology, Điều 7.2.b.i–iv, d.1001–1004).

Đối với danh mục đầu tư cổ phiếu, theo quy định tại Điều 103 Luật Các tổ chức tín dụng số 47/2010/QH12 về góp vốn mua cổ phần, các ngân hàng thương mại không được phép kinh doanh cổ phiếu mà chỉ được nắm giữ cho mục đích đầu tư chiến lược dài hạn (vab_ftp_methodology, Điều 7.3, d.1008–1012). CFU tính giá bán vốn COF Thị trường 1 theo [[vof-and-cof-dual-curve-structure-defines-market-1-ftp-pricing]] tương ứng với kỳ hạn nắm giữ dự kiến theo chiến lược kinh doanh; trong trường hợp chưa xác định được kỳ hạn dự kiến cụ thể, ngân hàng áp dụng một trong hai phương án quy ước: tính theo kỳ hạn nhận cổ tức hàng năm ($\ge 1$ năm), hoặc xếp vào dải kỳ hạn trên 5 năm ($\ge 5$ năm) theo thông lệ đầu tư chiến lược, và giữ mức COF cố định trong suốt thời gian nắm giữ danh mục (vab_ftp_methodology, Điều 7.3.i–iii, d.1014–1018).

Đối với các tài sản nợ và tài sản có khác (như tài sản cố định, chi phí chờ phân bổ, các khoản phải thu/phải trả khác), ngân hàng lựa chọn một trong hai phương pháp luận tiếp cận bảng cân đối:
1. **Phương pháp tiếp cận mua bán một phần (Partial Balance Sheet Approach)**: Ngân hàng không tính FTP cho các khoản mục tài sản khác; các tài sản này được coi là tài trợ trực tiếp từ nguồn vốn chủ sở hữu, và phần thặng dư vốn chủ sở hữu còn lại sau khi trừ tài sản khác mới là đối tượng chịu chi phí vốn theo [[ftp-cost-of-equity-apportionment-bridges-raroc-and-surplus-capital]] (vab_ftp_methodology, Điều 7.4, d.1022–1023);
2. **Phương pháp tiếp cận mua bán toàn bộ (Full Balance Sheet Approach)**: CFU xác định tỷ trọng số dư của khoản mục tài sản khác phân bổ trong từng thang kỳ hạn của báo cáo khe hở thanh khoản (liquidity gap), nhân với lãi suất FTP tương ứng của từng kỳ hạn đó, và cộng dồn tích số để xác lập mức giá FTP bình quân sau cùng của danh mục tài sản khác (vab_ftp_methodology, Điều 7.4, d.1024).

Kỹ thuật phân định và loại trừ này giúp hệ thống quản trị của [[vietnam-banking-ftp-governance-centralizes-balance-sheet-risks-via-cfu]] giữ vững tính toàn vẹn kinh tế, triệt tiêu mọi khả năng hạch toán hai lần chi phí thanh khoản và vốn tự có trên toàn hệ thống.
