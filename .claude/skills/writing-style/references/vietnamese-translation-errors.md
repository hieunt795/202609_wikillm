# Danh Sách Từ Dịch Sai Thường Gặp (Rule D3)

Các thuật ngữ kinh tế thường bị dịch sai do dịch máy theo nghĩa chuyên ngành khác (ví dụ: y học, kỹ thuật). Kiểm tra danh sách này trước khi tự dịch thuật ngữ mới gặp lần đầu. Nếu phát hiện lỗi dịch mới, thêm vào danh sách theo template dưới.

## Danh Sách Xác Nhận

| Từ Tiếng Anh | Dịch Sai ❌ | Dịch Đúng ✅ | Ghi Chú / Nguồn |
|---|---|---|---|
| **sterilization** | tiệt trùng (nghĩa y học: khử trùng) | **trung hòa** / **can thiệp trung hòa** | Audit 2026-09-23: sửa 8 file trong `02_wiki/` (trang central-bank-balance-sheet, sterilization-offsets-fx, monetary-authorities-control, v.v.). Bản chất: Sterilization trong chính sách tiền tệ = hành động bù trừ tác động của FX intervention lên cơ sở tiền tệ (sử dụng OMO, phát hành chứng chỉ), không liên quan y học. |

## Template Thêm Entry Mới

Khi phát hiện lỗi dịch mới (qua `/lint`, `/review-node`, hoặc audit), thêm dòng mới vào bảng trên theo định dạng:

```markdown
| từ tiếng anh | dịch sai | dịch đúng | Phát hiện: [Ngày], [Nguồn phát hiện - file wiki nào hoặc phiên nào], lý do ngắn |
```

**Quy tắc thêm entry:**
1. **Chỉ thêm khi chắc chắn là lỗi** — không phải "có thể dịch được nhiều cách" (ví dụ: "quantitative easing → nới lỏng tiền tệ / mở rộng bảng cân đối" đều chấp nhận được, không coi là lỗi).
2. **Ghi cụ thể lý do** — tại sao dịch đó sai, đúng dịch gì (ví dụ: y học / kỹ thuật / ngành khác).
3. **Ghi rõ nguồn xác nhận** — file wiki nào, phiên audit nào, người phát hiện khi nào.

**Ví dụ entry tốt:**
```markdown
| taper tantrum | cơn tức giận giảm dần | phản ứng thị trường / đợt bán tháo khi kỳ vọng lạm phát tăng | Phát hiện: 2026-09-25, /review-node file "monetary-policy-expectations", lý do: "tantrum" ở đây chỉ hành động thị trường (bán tháo, sợ hãi), không phải cảm xúc nhân cách hóa |
```

## Ghi Chú Chung

- Danh sách này **trực tiếp** được tham chiếu từ `SKILL.md` rule D3 (xem `references/vietnamese-translation-errors.md`).
- Khi gặp thuật ngữ tiếng Anh mới trong ingest / review, trước khi tự dịch hay để nguyên tiếng Anh, **kiểm tra danh sách này trước** để tránh dịch sai.
- Nếu không tìm thấy trong danh sách, theo tinh thần D3: nếu có dịch ngắn gọn tương đương → dùng dịch (định nghĩa 1 lần, áp D1); không có → giữ tiếng Anh.
- **Định kỳ audit danh sách** — mỗi lượt `/lint` lớn (50+ trang) nên quét lại xem có thêm từ dịch sai nào mới phát hiện.
