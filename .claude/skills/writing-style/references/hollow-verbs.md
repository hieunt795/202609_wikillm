# Danh Sách Từ Sáo Rỗng & Quota (Rule B1)

## Danh Sách Từ Cấm

Mỗi từ/cụm dưới đây bị hạn chế **tối đa 3 lần/từ** trong phạm vi tính (xem mục Phạm Vi Tính). Thay bằng từ đồng nghĩa thường trong danh sách "Thay Thế Gợi Ý".

| Từ Cấm | Thay Thế Gợi Ý | Ví Dụ |
|---|---|---|
| dẫn đến hệ quả là | do đó, vì vậy, kết quả là, từ đó | "Lãi suất cao tăng chi phí vay. Từ đó, đầu tư suy giảm." |
| bộc lộ | thể hiện, phản ánh, xuất hiện | "Áp lực thanh khoản phản ánh qua lãi suất repo tăng." |
| kích hoạt | thúc đẩy, gây ra, làm nảy sinh | "Sợ hãi thanh khoản gây ra bán tháo tài sản." |
| thể hiện rõ nét | rõ ràng, rõ, hiển thị | "Đây rõ ràng là tác động chính của chính sách." |
| triệt tiêu | loại bỏ, làm mất, vô hiệu hóa | "NHNN hành động để loại bỏ tác động của FX intervention." |
| bào mòn | suy giảm, giảm, làm yếu đi | "Lạm phát giảm giá trị thực của tiền tệ." |
| vô hiệu hóa | loại bỏ, triệt tiêu, làm mất hiệu lực | "Chính sách này loại bỏ tác động của intervention." |
| ép buộc | buộc, bắt buộc, yêu cầu | "Lãi suất cao yêu cầu nhà đầu tư điều chỉnh vị thế." |
| phá hủy | làm tổn hại, suy giảm, phá vỡ | "Khủng hoảng thanh khoản tạo suy giảm trong tín dụng." |
| thiết lập | lập, tạo, đưa vào | "Quy trình mới được tạo ra để quản lý rủi ro." |

## Phạm Vi Tính Quota

Rule B1 áp dụng theo **phạm vi cụ thể**; không cộng dồn trên toàn tài liệu:

### Trang Wiki
- Mỗi file `.md` trong `02_wiki/` được tính **riêng lẻ**.
- Tối đa 3 lần/từ sáo trong 1 trang.
- Nếu trang dài > 1500 từ, có thể chịu 4 lần nhưng nên xem xét tách trang (rule nếu trang quá dài, có thể phải tách để giữ tính nguyên tử — xem `00_schema.md`).

**Ví dụ:**
- Trang "Lãi suất": 3 lần "dẫn đến hệ quả là" được. Lần thứ 4 phải sửa thành "do đó" hoặc "vì vậy".
- Trang "Lạm phát": 3 lần "dẫn đến hệ quả là" được (riêng trang này). Không cộng với trang "Lãi suất".

### Báo Cáo / Tài Liệu Dài
- Mỗi **section / chapter** (thường ~500–800 từ) tính **riêng** theo phạm vi B1.
- **Intro / Executive Summary** tính là 1 section riêng.
- **Không cộng dồn** trên toàn báo cáo.

**Ví dụ:**
- Báo cáo 50 trang:
  - Intro: 3 lần "dẫn đến hệ quả là" được
  - Chapter 1: 3 lần "dẫn đến hệ quả là" được (riêng chapter)
  - Chapter 2: 3 lần "dẫn đến hệ quả là" được (riêng chapter)
  - Tổng cộng có thể 9 lần, nhưng **mỗi phần không vượt 3 lần**

### Ingest Lượt Lớn (50+ trang)
- Tính quota **theo từng trang wiki**, không cộng dồn trên toàn bộ nguồn.
- Khi merge/consolidate nhiều trang thành 1: tính lại quota trên trang mới.

**Ví dụ:**
- Ingest 50 trang từ bộ sách X: Kiểm tra từng trang riêng (trang 1 tối đa 3, trang 2 tối đa 3, ...), không kiểm tra "toàn bộ 50 trang tối đa 3".

## Ngoại Lệ

### Trang Glossary / Định Nghĩa Thuần Túy
- Nếu trang là **liệt kê định nghĩa, bảng kỳ hạn, hay profile tham khảo** (không phán tích), có thể **miễn rule B1** — trang không phân tích nhân-quả nên không áp B1.

### Từ Sáo Rõ Ràng Súc Tích Hơn Thay Thế
- Khi từ sáo rõ ràng **súc tích hơn từ thay thế** (ví dụ: "dẫn đến hệ quả là" = 5 từ vs. "do đó" = 2 từ, nhưng trong ngữ cảnh cụ thể "dẫn đến hệ quả là" ghi rõ hơn quan hệ nhân-quả phức tạp):
  - Có thể **tăng lên 4 lần** trong trang/section đó.
  - **Nhưng phải nêu lý do khi review** (ví dụ ghi chú: "từ sáo này thích hợp vì nó nhấn mạnh chuỗi nhân-quả hai tầng").
  - Người review quyết định chấp nhận hay bắt tối giản lại.

## Ghi Chú

- Rule B1 không phải "cấm hoàn toàn" mà là "hạn chế" để tránh lạm dụng làm văn bản trở nên sáo rỗng, giây cổ.
- Mục đích: Bắt buộc người viết tìm từ khác hơn, lành mạnh hơn, khi viết quá nhiều lần cùng cụm.
- Khi không chắc phạm vi tính, hãy hỏi reviewer hoặc xem lại `SKILL.md` rule B1 lần cuối.
