---
type: sources-manifest
last_updated: 2026-09-21
---

Xuất xứ và checksum của các nguồn trong `01_sources/`.

`01_sources/` **không được commit** (xem `.gitignore`): đó là tài liệu của bên thứ ba, kho này chỉ phát hành phần wiki do dự án tự viết. File này ghi đủ thông tin để đối chiếu mọi chú thích vị trí (`00_schema.md` §7.5) và bản đồ chunk trong `03_state/`.

**Chuyển đổi PDF → `.md` nằm ngoài dự án.** Người dùng chạy luồng riêng rồi đặt file `.md` vào `01_sources/`; dự án không chuyển đổi, không ghi công cụ chuyển đổi.

**Giới hạn tái lập.** Chú thích vị trí trỏ tới số dòng của **file `.md` do luồng chuyển đổi bên ngoài tạo ra**, không phải file nhà xuất bản phát hành. OCR lại từ PDF gốc sẽ cho file khác hash và khác số dòng. Vì vậy:
- Hash của file `.md` chỉ xác nhận *đúng bản đang dùng* — đối chiếu được khi có chính file `.md` này.
- Hash của file PDF (khi có) là thứ duy nhất đối chiếu được với bản tự tải, và chỉ khi trùng đúng bản phát hành.

## Source id

`source id` là khoá dùng trong trường `sources:` của trang wiki, trong chú thích §7.5 và làm tên file `03_state/<source id>.md` (§10). Nó tách khỏi tên thư mục vì `01_sources/` không được đổi tên (§3). Nguồn mới dùng snake_case; hai nguồn cũ giữ id đã dùng.

| Source id | Thư mục trong `01_sources/` | Phân loại | State file |
|---|---|---|---|
| `imf_macro_accounting` | `imf_macro_accounting/` | Nguồn dài | `03_state/imf_macro_accounting.md` |
| `Modern Money Mechanics` | `Modern Money Mechanics/` | Nguồn ngắn | — |
| `capitalism_and_freedom` | `Capitalism and Freedom/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `bindseil_monetary_policy` | `bindseil_monetary_policy/` | Nguồn dài | `03_state/bindseil_monetary_policy.md` |
| `cargill_central_bank_policy` | `cargill_central_bank_policy/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `choudhry_principles_of_banking` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `choudhry_analysing_yield_curve` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `choudhry_fixed_income_markets` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `fixed_income_during` | `fixed_income_during/` | Nguồn dài | `03_state/fixed_income_during.md` |
| `tata_bank_alm` | `tata_bank_alm/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |

## imf_macro_accounting

| | |
|---|---|
| Nhan đề | *Macroeconomic Accounting and Analysis in Transition Economies* |
| Tác giả | Abdessatar Ouanes, Subhash Thakur — với đóng góp của Ian Lienert, Philippe Marciniak, Karen Swiderski |
| Xuất bản | International Monetary Fund, tháng 6/1997 — © 1997 International Monetary Fund |
| Phân loại | Nguồn dài (`00_schema.md` §10) |
| Tiến độ ingest | `03_state/imf_macro_accounting.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.md` | 849.006 | 6.065 | `13db03df3dd8e2b2dfdaf352dedc2b9c005700dcd0a86fcaf92063d697182859` |
| `01_sources/imf_macro_accounting/Macroeconomic Accounting and Analysis IMF.pdf` | 13.141.692 | — | `185f77f9524bc162c460eccb357dcbd0342b175e18b3c8593be8e347122e9310` |

File `.md` là bản OCR của PDF (chuyển đổi ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới. File dùng ký tự xuống dòng CRLF và SHA-256 ở trên tính trên đúng các byte đó; công cụ nào đổi sang LF sẽ làm lệch hash dù nội dung và số dòng không đổi (sự cố 2026-09-17, đã khôi phục). Bản OCR có lỗi thật (`Waaes`, `lmbalance`, `tO`, `1 993`…) — đây là lý do lint có tiêu chí *Nhiễu OCR còn sót*.

## Modern Money Mechanics

| | |
|---|---|
| Nhan đề | *Modern Money Mechanics* |
| Xuất bản | Federal Reserve Bank of Chicago |
| File gốc | `frbchi_modernmoneymechanics_1961.pdf`, 31 trang |
| Phân loại | Nguồn ngắn (`00_schema.md` §10) — không cần file trạng thái |
| Tiến độ ingest | Chưa ingest (`02_wiki/index.md` §Sources) |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/Modern Money Mechanics/Modern Money Mechanics.md` | 84.768 | 721 | `c26b222a173146511d25243f4aee44d38ea3806a265e7f076b89496c3af65b38` |

Thư mục còn 16 file phụ do bước OCR sinh ra (`Modern Money Mechanics.json` + 15 ảnh `_page_*.jpeg`) — là vật liệu nguồn, không phải file do agent tạo.

## capitalism_and_freedom

| | |
|---|---|
| Nhan đề | *Capitalism and Freedom* — Fortieth Anniversary Edition, kèm lời tựa mới năm 2002 |
| Tác giả | Milton Friedman, với sự hỗ trợ của Rose D. Friedman |
| Xuất bản | The University of Chicago Press — © 1962, 1982, 2002 |
| Phân loại | Nguồn dài (`00_schema.md` §10) — sách lập luận chính sách |
| Nguồn file | Bản PDF lấy từ PDFDrive (theo tên file), không phải từ nhà xuất bản. Thư mục không kèm PDF. File `.md` chuyển đổi ngoài dự án (có chú thích `MODE: OCR` / `NATIVE_TEXT` theo từng dải trang, 226 trang) |
| Tiến độ ingest | Chưa ingest — state file dựng ở lượt ingest đầu (§10) |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/Capitalism and Freedom/Capitalism and Freedom_ Fortieth Anniversary Edition   ( PDFDrive ).md` | 564.983 | 2.055 | `46c0375575e6b362477e765359f503492e8ed1c8d1e8bfcb47770cb0a9ff64f0` |

Tên file có ba khoảng trắng liền nhau trước `( PDFDrive )` — giữ nguyên khi đặt lại đường dẫn.

## bindseil_monetary_policy

| | |
|---|---|
| Nhan đề | *Monetary Policy Operations and the Financial System* |
| Tác giả | Ulrich Bindseil |
| Xuất bản | Oxford University Press, 2014 — First Edition, © Ulrich Bindseil 2014 |
| Phân loại | Nguồn dài (`00_schema.md` §10) — 1.128 KB / 4.473 dòng |
| Nguồn file | PDF kèm theo; `.md` chuyển đổi ngoài dự án bằng docling |
| Tiến độ ingest | Hoàn tất 100% — `03_state/bindseil_monetary_policy.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.md` | 1.154.791 | 4.473 | `3d51b988c305908b03e91cc3316d4d9cb614c966a729e7c34ab9c41ea904348c` |
| `01_sources/bindseil_monetary_policy/Bindseil_Monetary_Policy_Operations.pdf` | 5.015.231 | — | `4ff712c97ac1fa4bdc5b8e452ff3f3a1e3bc68c6126e0536c350c5e5b68c668e` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới.

## cargill_central_bank_policy

| | |
|---|---|
| Nhan đề | *The Financial System, Financial Regulation and Central Bank Policy* |
| Tác giả | Thomas F. Cargill |
| Xuất bản | Cambridge University Press, 2017 — © Thomas F. Cargill 2017 |
| Phân loại | Nguồn dài (`00_schema.md` §10) — 1.178 KB / 5.623 dòng. Sách giáo khoa |
| Nguồn file | PDF kèm theo; `.md` chuyển đổi ngoài dự án bằng docling |
| Tiến độ ingest | Chưa ingest — state file dựng ở lượt ingest đầu (§10) |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/cargill_central_bank_policy/Cargill_Financial_System_Policy.md` | 1.206.440 | 5.623 | `ddd1ba0e016610ddf09837814ce5b336268f96bc84bb6ec11f99dfe25be9f1e6` |
| `01_sources/cargill_central_bank_policy/Cargill_Financial_System_Policy.pdf` | 14.209.255 | — | `97d04b6d11e71f3b9a2f31d4e79a0c36ac85b145a6261826e489eaf553d606a0` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới. Bản chuyển đổi có lỗi nhận dạng ký tự (`IDustration`, `mustration`, `Thrning`, `Chapter4`).

## choudhry_banking_fixed_income

Một thư mục chứa **ba cuốn sách độc lập** của Moorad Choudhry (John Wiley & Sons, Wiley Finance). Mỗi cuốn một source id riêng vì chú thích §7.5 và bản đồ chunk trỏ tới số dòng của từng file.

| Source id | Nhan đề | Tác giả | Xuất bản | Phân loại |
|---|---|---|---|---|
| `choudhry_principles_of_banking` | *The Principles of Banking*, Second Edition | Moorad Choudhry, với đóng góp của P. Bardaeva, N. Bourne, M. Eichhorn, B. Lubinska, E. Plassmann, P. Thivaios, C. Westcott | John Wiley & Sons, 2023 (bản đầu 2012) — © 2023 Moorad Choudhry | Nguồn dài — 2.602 KB / 14.955 dòng |
| `choudhry_analysing_yield_curve` | *Analysing and Interpreting the Yield Curve*, Second Edition | Moorad Choudhry, với đóng góp của P. Bardaeva, K. Kortanek, K. Liddy, W. Marty, V. Medvedev | John Wiley & Sons, 2019 (bản đầu 2004) — © 2004, 2019 Moorad Choudhry | Nguồn dài — 686 KB / 6.177 dòng |
| `choudhry_fixed_income_markets` | *Fixed Income Markets: Management, Trading, Hedging*, Second Edition | Moorad Choudhry, David Moskovic, Max Wong | John Wiley & Sons Singapore, 2014 (bản đầu 2004) — © 2014 Moorad Choudhry | Nguồn dài — 1.895 KB / 15.414 dòng |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/choudhry_banking_fixed_income/Choudhry_Principles_of_Banking.md` | 2.664.156 | 14.955 | `6739ed32dbe0930f25d7f8ca25fa9e11198a195c7dfad8866a4b3a9148cfa76c` |
| `01_sources/choudhry_banking_fixed_income/Choudhry_Principles_of_Banking.pdf` | 29.079.798 | — | `b34171798ee43f8e6d8c71133bc4950b75af20528c36a039d42e9b39721e1d0e` |
| `01_sources/choudhry_banking_fixed_income/Choudhry_Analysing_Yield_Curve.md` | 702.832 | 6.177 | `fc6ab5123a48ec515f9e5c5a03a6ee859e0a07b702bffdc184618681ad1333e0` |
| `01_sources/choudhry_banking_fixed_income/Choudhry_Analysing_Yield_Curve.pdf` | 11.770.187 | — | `2a606be182b861e8f1c7dfbae1a9469efc023cecdf5f1997d0c09d1dc6cc5c3d` |
| `01_sources/choudhry_banking_fixed_income/Choudhry_Fixed_Income_Markets.md` | 1.940.864 | 15.414 | `0206140c3876b2a3b810f950526a6877e7a08de84568196747fdb6793ad784a8` |
| `01_sources/choudhry_banking_fixed_income/Choudhry_Fixed_Income_Markets.pdf` | 11.691.701 | — | `b884a7f5654da9452e9008cbeccd989d84636c37884d8c29d0a91a469b460d21` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới. Chưa ingest cuốn nào — state file `03_state/<source id>.md` dựng ở lượt ingest đầu của từng cuốn (§10).

## fixed_income_during

| | |
|---|---|
| Nhan đề | *Fixed Income Trading and Risk Management* |
| Tác giả | Alexander Düring |
| Xuất bản | John Wiley & Sons (Wiley Finance), 2021 — © 2021 John Wiley & Sons, Ltd; ISBN 9781119756330 (theo ghi chú người dùng, xem `03_state/fixed_income_during.md`) |
| Phân loại | Nguồn dài (`00_schema.md` §10) — tổng 1.086 KB / 7.300 dòng trên 42 file `.md`; từng file đều dưới ngưỡng |
| Nguồn file | Sách tách thành 42 PDF theo chương, mỗi PDF kèm `.md` chuyển đổi ngoài dự án bằng docling. File `-1` là front matter, `-k` (k = 2…40) là Chương k−1, `-41` Bibliography, `-42` Index |
| Tiến độ ingest | `03_state/fixed_income_during.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/fixed_income_during/Fixed Income - Alexander During-1.md` | 92.441 | 429 | `c0d4b0237bd933c81d04a655e465c2c56a70214eabb559cff787c1a846850648` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-1.pdf` | 957.918 | — | `b322a6e529ee7890462b7e2b918d452741451d7050a603eadc1ccbaea559fd77` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-2.md` | 17.985 | 81 | `6c4ed7d3e11bb623b567f31ee6c93ac817fb3e1ac215082e012f1ccf9eaa4538` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-2.pdf` | 230.232 | — | `c3822d51de6a1ad0de68b5d1ba3f517463023f764ea2081f821ee6cba9b22623` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-3.md` | 24.624 | 115 | `3bec0b9f4a191ba618a8041d11977afb1354ee21571c4837bab2cec11cd69ed0` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-3.pdf` | 231.187 | — | `aca457844e234d3a86dbd31bec5a7cad077bc373996c577ba5c0648455dba751` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-4.md` | 6.843 | 27 | `60d28840c7d8f63e972ef838492a63e2ea437ee8790108215a572247153f12ad` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-4.pdf` | 65.485 | — | `562486676ccef42313e9b63595dc10b7b216f53173474fcd4959d7ec0fdead5f` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-5.md` | 16.679 | 97 | `3d4847c3300b2c4d377e7414d97655d5e63f1645a50dfc9972a9482f33e73868` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-5.pdf` | 301.134 | — | `97dc86f731b7d6870049eea3aa5fac0b8fe78e80ea56b72ed91efb33db3e9837` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-6.md` | 3.967 | 33 | `f28e89125d1747f1408d656daa1d5d53e9dd619eafbd1b8bc2931c6254775da1` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-6.pdf` | 223.073 | — | `4328ae9c8dc7723dace471a28592d28070d9a387eb801d61be2b9ba4033217ba` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-7.md` | 5.094 | 33 | `478be16344146b69c8853def656471a2d2601e80ceede3577c1d19bcfec17b33` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-7.pdf` | 283.456 | — | `9c345ba3bd49c84452dada618f5ca59019333043f065670d762f165086eeac57` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-8.md` | 5.899 | 33 | `5acc90611951bd1f044a734280c45bbc1b88ed1c77e97b0f65be58c021ee221a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-8.pdf` | 72.282 | — | `9d29d0cbabad383280e433b25f999fdb2baf699c2920cdae43c2d61c5f9d19e8` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-9.md` | 5.477 | 33 | `88eb14f8f6e777858da7936e08a61874cec36c24b33f4fd92973983c9460f770` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-9.pdf` | 84.541 | — | `57faf0e6083e152a6fa20d5606a98093b7510dd92cfc32f964938c0dbe49e46e` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-10.md` | 57.444 | 275 | `10750649e850a86c9a17c1caf4dcdd885c4b91ff0c4fb52541258a26cec8ef46` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-10.pdf` | 617.303 | — | `f441cd0634cc30646e3474e6489da488bd3c5d915707b12938d8424214bfb68c` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-11.md` | 15.146 | 109 | `5ac5df0af411c9fbf0c49fd09035fce3454c3826b54afdb18924561a89947cc8` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-11.pdf` | 138.260 | — | `e251f484b1ba98a80d11872f45ed4127585334737edaabda6e56e8a0976a4e5a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-12.md` | 50.255 | 277 | `153f3b4216a931e300a334ae418642853ae415bcb9150e59d871c2ffcc772279` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-12.pdf` | 253.615 | — | `3bb82d1ddcc62df7c1b2b426f3e052b9c61c797b0639061abdd2837ee17df6dc` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-13.md` | 27.140 | 133 | `47ac360ef5c8b48aea2c5b8b7ff56ea3188cd042810277f0b3aa12099601a9b4` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-13.pdf` | 229.056 | — | `a42010e1d569cfb2753c6b1b7a3c88539e9c1875e9a6fc3644b25e1f6cc6c8b7` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-14.md` | 41.041 | 278 | `d42a4609219cbbbfee7359516f2a85fd2b368887c7e595765b524438624d14dd` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-14.pdf` | 249.609 | — | `95d04a6588b9ff93993c7c18a826b1ffd400be4662a9aa5c04f118fbff49390d` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-15.md` | 14.938 | 63 | `9def314ff5e7b0b8a5bb0a9ab81b4d3219a628962f801444d28310297dc22e61` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-15.pdf` | 143.823 | — | `7a77cc43cdd43df0ea211a3da16f3201fe89bb23b40fed6be4df051e5b1b061c` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-16.md` | 13.417 | 107 | `f14cf570d1618e044aff2ce2d90ba605726aa06ff06ed94135dde40469042d75` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-16.pdf` | 190.254 | — | `cd66b7ec719750bb3be3741b93afdb5ce9927025527834e4a7b2bc9e505d4a9d` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-17.md` | 87.745 | 486 | `646b1b7df03ab3ee75d1efe5eb51c17abadb7febb2de661c5137afd7812a9acc` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-17.pdf` | 1.387.249 | — | `26d26a8832a1c579c04839c28944bcb474d0adbb5091c9202f52c6b4ff3f7d67` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-18.md` | 16.667 | 125 | `c76d5156536584526c45584543902d52899426982fd74b83378d31e6ce82ad78` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-18.pdf` | 166.929 | — | `326cd881bbca22a0027def7edb82f669e37f3535c74fff919ed445691776ede8` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-19.md` | 36.557 | 155 | `770de834f0cfcfb8fa2f186651d0a102909c295d8ecae595611cbc9841ff09e6` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-19.pdf` | 622.810 | — | `5c77f96a2f1a4abbee869707b88756a3886152b69194784cfd44aa217dbaa218` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-20.md` | 33.397 | 341 | `45ece24b456e8575b6de92a6727aefd2a4f4d363c1a07267eb36b4174a454558` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-20.pdf` | 891.808 | — | `cc94dca1930c8897da31de25e51a687d875531b6f7d8722ec685b680e0b72b49` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-21.md` | 31.773 | 171 | `f9f83e0fba16de504327775508062ffd3a4cb311f08d72fe4c45e0da2b8ace4f` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-21.pdf` | 625.993 | — | `b54af066b3f4b1164482195f2d7a72e888e7f2629cceb14db32ae4054a94c605` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-22.md` | 7.038 | 39 | `e85b7e3725f87a453d7db4c615fdf38c77445d87adef74b84381daca842551d0` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-22.pdf` | 183.191 | — | `187287bf2bd3cd703d8bdd14d893b50e33ad1a241891003daa3cea1a138019a4` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-23.md` | 12.634 | 83 | `7072619db2f41a6dfe3035bd6fb979f4a55215ed1423528f1e5de5ea0a4b957b` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-23.pdf` | 149.499 | — | `bf46391da77d805e465a2617f5a29a8eec3719c86bb10d1601ef5fb1d91b2735` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-24.md` | 59.864 | 361 | `0060ac39769bd0889247d346bc4cbd0510a52952a1b25bacc581cc7726fe0601` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-24.pdf` | 980.850 | — | `835b067f0327f70213595be16fea0c5d94c49f3de1f66ed9183fe0704c5317f1` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-25.md` | 52.275 | 271 | `497c945ff429c889981e7b9425aec2d3a6d889f3fb29e93bb82ea925811a1271` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-25.pdf` | 330.456 | — | `865502c556510c946eacfdac79b6e8d55692f0a3e144992b9913941d04f42b36` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-26.md` | 33.491 | 172 | `39e59f9e3a0030ead944787540eaa6a22791fbaee3ed102b844730512520cd32` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-26.pdf` | 361.190 | — | `c104b4234e182f82794b107515c5d4dd4690fe57e63c66d431b0f33ab2b5a637` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-27.md` | 12.733 | 55 | `09c180a361b86809e29cfefbc919ba6fb15a69f98332e67476679354d3fe5585` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-27.pdf` | 115.898 | — | `1f001c296b945ac57c31e77f7103bbd9ba4751bd7860a7a7d8062ee03f10ed00` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-28.md` | 24.426 | 123 | `c065b49cb098f232312ee7f6c570e687698ed1c61439269ee049363970f8cd1f` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-28.pdf` | 407.876 | — | `54e6e7d21dd999b0873f925a60a9a3742707c18556e63e792a249601e37cf795` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-29.md` | 81.668 | 500 | `0d9b9a5468e4d806344907acba07cc1b9825dc34d0173a960250a3caa957c5fe` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-29.pdf` | 1.429.585 | — | `cf6d3e4a23d87003635e235f9414815837163ed6d608fd014b0e1842dc05e19b` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-30.md` | 15.987 | 88 | `271ff83a127fc373ebc8901f9ac6631a08839ef3d6611a8ed5e74c1ee379bd37` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-30.pdf` | 142.524 | — | `fac9a46a2c9bf0a9296d537affb82e6c4ce764735086915b011ad364f3fa8d39` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-31.md` | 11.731 | 73 | `c2ee9f31fb5182e76de1f2ee66720282e877074760f2dd3a2435223403596838` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-31.pdf` | 148.069 | — | `2bc878926e8a0f721dd2bb21fb44d156d0079e07cabcad230ab22ca709618b11` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-32.md` | 27.713 | 213 | `4af91859abbccfe6934d3ec305eb36cc86141dd3e47fab10bc541cd043aac5c6` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-32.pdf` | 1.133.676 | — | `14d0e68e2f55616c2257110b65bd0d5431d913072000dc3ff0e0d2b59a9b422a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-33.md` | 12.307 | 103 | `b61086018b8ec21f9f111933219b682e8989a7f7983156f8e29781c8b11a5492` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-33.pdf` | 188.418 | — | `6ba7a12399820b4ecab0ff03325fc51115eca8ef4712ce3d3272e5b43a921a8e` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-34.md` | 13.243 | 125 | `d2cc8cfc4792fd9d7d340a562e7fb2c70a762389647ee9370adb851159bad809` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-34.pdf` | 424.139 | — | `76c3a9302417acc56ccf7fbda13a50e878375c917d1b9ab984929243b1b99077` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-35.md` | 7.067 | 47 | `186418b048484b75ba62d8cc979c7a117bb57e414858ab4a2d974887157b3ec5` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-35.pdf` | 99.176 | — | `c3305563063bbdfacd867aabe0881283434cb9d31001b56bc1c7cd88ed674c0f` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-36.md` | 22.961 | 137 | `c0a412793aade2386ae14b5e1d44d939a5ee5de8d351b9b2bbc25f92434a279a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-36.pdf` | 172.404 | — | `ab57e20c6966f99aa439058b734746bd454a42ddcbc4f862eaa19c9f8bff67f5` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-37.md` | 12.738 | 139 | `5f6a5f25de01e66b50cd0e3584702201217a58e35cfd636649b368896b3b2c9c` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-37.pdf` | 119.882 | — | `f76f445c36a843894b570dd536c11085065a4adec66c7e7018166c33e266628d` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-38.md` | 20.023 | 115 | `56f45fbff9b035d1688e89898b9e6f32ae76007290c9730ec050b9cbfd103dbf` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-38.pdf` | 312.602 | — | `17605ed79a31130a7d422c2b4dce669d2e9dd8a5e9412050c18eff35646f73f5` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-39.md` | 17.589 | 115 | `55bd0d654c49140eabb7061668864a6eb92f9e2c5edf1762fae390350d2abfc4` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-39.pdf` | 355.902 | — | `ef2204e55e9008b97be99fd2a839bfc69d88f7af83da4839806ec6f5ade0755a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-40.md` | 46.359 | 536 | `7122c7c20d71e906c913d41b4af9f28b16608cfe453e49fec2c3d8fa97f62f49` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-40.pdf` | 288.411 | — | `97daa2a800d88d3ef649091500056383092523bee3a09528d050b412c3642aa7` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-41.md` | 10.540 | 99 | `70a962d2559de8de288f8b941905a5632619d451a787fbca5a0597bc52940fa5` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-41.pdf` | 94.591 | — | `29a77755519f3f120577520a7f4cd9ae50390c9a9db7187b4513bc6afec1630a` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-42.md` | 5.451 | 505 | `2fa823ee32ad203a9533c61d55da9caaaa45944e9a07e090dae12e8db5b867a1` |
| `01_sources/fixed_income_during/Fixed Income - Alexander During-42.pdf` | 438.194 | — | `6d7a52cb563c413a06b863a6e0d7f72500040ec8aed0f3495626e49ea0ccfbe7` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới. Ghi chú `_source_note.md` người dùng đặt trong thư mục (ISBN, chia phần, ghi chú PDF có text layer) đã chuyển sang bản kê này và `03_state/fixed_income_during.md` ngày 2026-09-17, file gốc đã xoá theo quyết định của người dùng.

## tata_bank_alm

| | |
|---|---|
| Nhan đề | *Bank Asset-Liability Management: A Guide to Managing Interest Rate Risk in the Banking Book for Practitioners, Regulators, and Supervisors in the EU* |
| Tác giả | Fidelio Tata (International School of Management, Berlin) |
| Xuất bản | Springer Nature Switzerland AG, 2025 — ISBN 978-3-031-80204-1; eBook 978-3-031-80205-8; doi 10.1007/978-3-031-80205-8 |
| Phân loại | Nguồn dài (`00_schema.md` §10) — 439 KB / 3.345 dòng |
| Nguồn file | PDF kèm theo; `.md` chuyển đổi ngoài dự án bằng docling |
| Tiến độ ingest | Chưa ingest — state file dựng ở lượt ingest đầu (§10) |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md` | 449.713 | 3.345 | `cf99b3432c43cb65b509281dd4623d414ff5da90977aa0fbaaaa8a13656e1562` |
| `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.pdf` | 8.647.913 | — | `c41add63953dcf53d2ad64a38fa7f8e21f467c3c1c7faf7db8c6f7ec2179d432` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới.
