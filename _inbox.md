# Inbox

> Vùng capture tạm cho ý tưởng/insight chưa đủ chín thành trang evergreen (`00_schema.md` §11). Tách khỏi `02_wiki/` có chủ đích: trang trong `02_wiki/` phải atomic hợp lệ và bị hook kiểm mỗi lần ghi, ý tưởng dang dở không thoả được luật đó.
>
> Định dạng: mỗi ý 1 gạch đầu dòng kèm ngày — `- [YYYY-MM-DD] <ý tưởng>`. Không frontmatter, không luật trang wiki.
>
> File này nằm **ngoài mạng liên kết**: không `[[wikilink]]` nào trỏ vào, không xuất hiện trong `index.md`.
>
> **Triage mỗi lượt lint.** Mỗi mục có đúng 3 kết cục: nâng thành trang wiki, gộp vào trang đã có, hoặc xoá. Không có kết cục "để đó". Mục tồn quá 3 lượt lint là nợ kỹ thuật — lint báo cáo ở tiêu chí *Nợ inbox*.

- [2026-09-25] Lệch nội tại trong imf_macro_accounting: Ch.1 d.524 nói trượt chủ động giảm lạm phát "không hy sinh sức cạnh tranh", Ch.4 d.4069 nói trượt chủ động "chấp nhận mất một phần sức cạnh tranh". Hai trang polands-exchange-rate-experience-yields-five-policy-lessons và the-rate-of-crawl-… chép đúng từng chỗ nên mâu thuẫn nhau. Cùng một nguồn nên không đánh ⚠️ Conflict; xử lý khi /ingest Ch.1 (đang [ ]).
- [2026-10-10] Văn bản quy phạm pháp luật (TT50/2026): các lượt ingest thử dùng ngoại lệ ngoài schema — mỗi điều một node, giữ nguyên văn kèm diễn giải, đọc `.docx` thay `.md`. Ngoại lệ này ngược §5 và §7 luật 4, chưa ghi ở đâu. Quyết khi ingest lại TT50/2026: thêm lớp nguồn riêng ở §10 hay ingest như nguồn thường.
- [2026-10-10] `03_state/_sources_manifest.md` có hai mục `## clippings` gần như trùng nhau (bảng đầu ghi số byte bằng dấu phẩy nên `--verify-sources` không đọc, bảng sau mới là bảng có hiệu lực). Lint 2026-10-10 thấy khi đăng ký nguồn, chưa gộp vì ngoài mã đã duyệt.
- [2026-10-10] nfa-nda-offset-mechanism-under-quasi-fiscal-and-fixed-exchange-rate: link nhãn "trần NDA" trỏ tới the-policy-anchor-decides-whether-net-foreign-assets-are-autonomous-on-the-central-bank-balance-sheet, trang này không nói về trần NDA. Cần trang đích đúng hoặc bỏ link.
