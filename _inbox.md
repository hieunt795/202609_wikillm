# Inbox

> Vùng capture tạm cho ý tưởng/insight chưa đủ chín thành trang evergreen (`00_schema.md` §11). Tách khỏi `02_wiki/` có chủ đích: trang trong `02_wiki/` phải atomic hợp lệ và bị hook kiểm mỗi lần ghi, ý tưởng dang dở không thoả được luật đó.
>
> Định dạng: mỗi ý 1 gạch đầu dòng kèm ngày — `- [YYYY-MM-DD] <ý tưởng>`. Không frontmatter, không luật trang wiki.
>
> File này nằm **ngoài mạng liên kết**: không `[[wikilink]]` nào trỏ vào, không xuất hiện trong `index.md`.
>
> **Triage mỗi lượt lint.** Mỗi mục có đúng 3 kết cục: nâng thành trang wiki, gộp vào trang đã có, hoặc xoá. Không có kết cục "để đó". Mục tồn quá 3 lượt lint là nợ kỹ thuật — lint báo cáo ở tiêu chí *Nợ inbox*.

- [2026-10-12] wiki thiếu: so với một bản đồ khái niệm ALM 59 mục (ảnh người dùng đưa, không phải nguồn trong `01_sources/`), 18 khái niệm chưa có trang riêng theo tên file. Số trong ngoặc là số trang đang nhắc tới thuật ngữ. Bốn khái niệm đủ ngưỡng (NSFR, Basel III, maturity transformation, trading book) đã có stub ở lint 2026-10-12. Dưới ngưỡng: core deposits (2), ALCO (1), maturity gap (1), intraday liquidity (1), matched funding (0), structural hedge (0), yield curve risk (0), operational deposits (0), ASF (0), RSF (0), liquidity gap (0), survival horizon (0), ILAAP (0). Earnings-at-risk chưa đếm được số trang nhắc. Nơi có thể trả lời, chưa mở kiểm: `basel_lcr` LCR40 cụm A (operational deposits) và LCR30 đoạn 30.26 (intraday liquidity); `01_sources/basel/NSF/` (NSFR, ASF, RSF) và `basel/IRRBB-d368/` (yield curve risk, earnings-at-risk), hai thư mục này chưa kê; các chunk `do` của `tata_bank_alm`.
