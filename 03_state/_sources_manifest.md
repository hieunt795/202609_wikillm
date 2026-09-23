---
type: sources-manifest
last_updated: 2026-09-23
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
| `cargill_central_bank_policy` | `cargill_central_bank_policy/` | Nguồn dài | `03_state/cargill_central_bank_policy.md` |
| `choudhry_principles_of_banking` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `choudhry_analysing_yield_curve` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `choudhry_fixed_income_markets` | `choudhry_banking_fixed_income/` | Nguồn dài | chưa dựng — tạo ở lượt ingest đầu (§10) |
| `fixed_income_during` | `fixed_income_during/` | Nguồn dài | `03_state/fixed_income_during.md` |
| `tata_bank_alm` | `tata_bank_alm/` | Nguồn dài | `03_state/tata_bank_alm.md` |
| `clippings` | `Clippings/` | Nguồn dài | `03_state/clippings.md` |

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
| Tiến độ ingest | Đang ingest dở — `03_state/cargill_central_bank_policy.md` |

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
| Tiến độ ingest | Hoàn tất 100% — `03_state/fixed_income_during.md` |

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
| Tiến độ ingest | Đang ingest dở — `03_state/tata_bank_alm.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.md` | 449.713 | 3.345 | `cf99b3432c43cb65b509281dd4623d414ff5da90977aa0fbaaaa8a13656e1562` |
| `01_sources/tata_bank_alm/Tata_Bank_ALM_2025.pdf` | 8.647.913 | — | `c41add63953dcf53d2ad64a38fa7f8e21f467c3c1c7faf7db8c6f7ec2179d432` |

File `.md` do docling chuyển đổi từ PDF (frontmatter `extractor: docling`, ngoài dự án) và là bản mà mọi chú thích vị trí trỏ tới.

## clippings

| | |
|---|---|
| Nhan đề | *Macro & Banking Web Clippings* — Tuyển tập bài viết phân tích vĩ mô, ALM ngân hàng thương mại, điều hành bảng cân đối NHTW và thị trường tiền tệ |
| Tác giả | Nhiều tác giả (Nguyễn Khánh / Hedge Academy, Federal Reserve Bank of New York, Federal Reserve Board, Bank for International Settlements, Gianluca Benigno, cùng các tác giả Substack) |
| Xuất bản | 2026 — Thu thập trực tiếp từ các cổng thông tin chuyên ngành và tài liệu nghiên cứu ngân hàng trung ương |
| Phân loại | Nguồn dài (`00_schema.md` §10) — 882 KB / 6.684 dòng trên 82 file `.md` |
| Nguồn file | Bài viết định dạng `.md` thu thập qua web clipper, lưu trữ nguyên bản trong thư mục nguồn `01_sources/Clippings/` |
| Tiến độ ingest | Đang ingest dở — `03_state/clippings.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/Clippings/5.2%, big problem Not at all.md` | 13,092 | 72 | `3624f5f4b7bf99691dc31ca5abde857d38b88960e302e3bf38682525e37b6dae` |
| `01_sources/Clippings/A Framework for Understanding the U.S. Treasury Repo Market.md` | 10,633 | 84 | `b542010ce08892ca3bb8307df27faa8620d133929a6ffb8e37ca619f832f4c5b` |
| `01_sources/Clippings/ALM P3 Cân nguồn Cân Tỷ lệ.md` | 1,426 | 19 | `a28230a28d16eeae9e44ca690eb8d28be500fa0c51615771a18012179139e9a7` |
| `01_sources/Clippings/ALM P5 – Bước đầu hiểu về sự phức tạp giữa Tây vs Ta trong ALM.md` | 7,034 | 41 | `dacfb2ff95d3ebb3430f350c472a324b0c93dff550dddcde09d4feb7386ebed3` |
| `01_sources/Clippings/ALM P6 – Hành vi nguồn vốn trên Thị trường 1 Khi mô hình hóa trở thành “fake”.md` | 6,788 | 55 | `db41e5cad7b91350c7537bea3dbbe3d3d0143bf7df997412e36c18e1286a06ba` |
| `01_sources/Clippings/ALM Part 4 Hiểu hành vi nguồn tiền.md` | 5,774 | 39 | `bc6f8ccc55330499371690e98d97fc235a00662fb7f5d3d6ef3fd4e103bc9c5f` |
| `01_sources/Clippings/Bạn muốn nghiên cứu về chính sách tiền tệ.md` | 2,442 | 29 | `d1ad7622fcf2da3699d4266203f8ccc0ae19bafbfed094849732d880e32651dc` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý P2 Nuôi Zombie kiểu Trung.md` | 12,234 | 81 | `4e00de7ff70addd562d1a5d8815f5a325fbee6c6cb14bdde8931e83514936731` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý P3 Nhìn chung phải có negotiate.md` | 15,625 | 59 | `22bbc93d340081574ffe69dbe2a5bdbe357ff709e0417882db0311dbc2c07509` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý.md` | 12,623 | 45 | `5ac7b5ac49323af055dc509ac139324a21909e50ebed8c5222644437c28ebaa3` |
| `01_sources/Clippings/Central Bank Commentary (July-26) Federal Reserve, Bank of Japan and Bank of England.md` | 31,219 | 189 | `f9e80af0cdf7170fd81ef0e593aac74faa29e57e4fbc3b08a947d60577a73e43` |
| `01_sources/Clippings/Chi phí vốn VND - Lý do tại sao lại lớn.md` | 6,126 | 149 | `a57d6a9e3dc58b8a901f9b429e0d0349533510c5c58eaaaef52ab5ba1b10a522` |
| `01_sources/Clippings/China August-26 CPI Inflation Report.md` | 15,463 | 105 | `eef1d6428fd3106ba9b6cd6621c1932ab0fd907461280cee00746fb0ab7eed1a` |
| `01_sources/Clippings/China July-26 CPI Inflation Report.md` | 15,471 | 105 | `c7b2eef16b9f9ef58ddd5c9a022510637e3b47649e0b2395b920ab4fdb3ed257` |
| `01_sources/Clippings/Chính sách hành lang lãi suất của SBV so với bản gốc.md` | 3,945 | 43 | `180da21ec963d34968a576ae69d72e5684ad659a84f9626eb06e5f506203044a` |
| `01_sources/Clippings/Cost of Funds USD vs VND Cách nhìn toàn diện.md` | 2,592 | 19 | `a961335183c85e61b21696e4a47880d147606a44eb11c3b66e717cc20431f67b` |
| `01_sources/Clippings/Cách nhìn hệ thống cần phải thay đổi-P2 Họp toàn Bug.md` | 4,479 | 41 | `3c0cb2f770a2309eef654b8c7bcdf6e269add7dde19ea72d53d3ad712acf7481` |
| `01_sources/Clippings/Cách nhìn hệ thống cần phải thay đổi.md` | 4,513 | 31 | `a53f2c3d6a554c94021f79e440dc247d6b23f2c6cf048aac4259bf5603e716da` |
| `01_sources/Clippings/Cân dòng tiền – Khái niệm đầu tiên về cân đối- ALM P1.md` | 6,907 | 35 | `040363615eca411b7d38342d196040b550c6cd602952b24c99ba0b7b4461bcdf` |
| `01_sources/Clippings/Cân nguồn – Phần tiếp theo Cân kỳ hạn.md` | 6,566 | 49 | `1a704fb139e858a41bcd923a862bfe94f18536479a532621f3fc02433dbb1d26` |
| `01_sources/Clippings/DTTT thay thế TT22.md` | 2,802 | 45 | `11a8f25692b40f0fd69bcd37ad473557b47e973d690786632a39a93359d00097` |
| `01_sources/Clippings/Debt Structure sau 5y hay 10y vẫn thế cả.md` | 8,630 | 27 | `3a6d5cd0c109771417b287e919d79b0b1b1838952eb0f495e11be18d46c42749` |
| `01_sources/Clippings/FED nâng lãi suất không còn đáng sợ như trước.md` | 4,087 | 31 | `cd32ecea69744a3765eeb995f836a8962402067086fedf39815403a4a3857b93` |
| `01_sources/Clippings/FOMC An Almost Certain Hike.md` | 10,752 | 117 | `8a67fb3fa441314f1d4c7ddd9f145c288bbdce0348484e072c66da3ff80ed234` |
| `01_sources/Clippings/Fed thực sự khổ.md` | 3,491 | 29 | `6e391f13a969e4120a4a83b3be355ba9481be2f0765529498180ccd7d95debb7` |
| `01_sources/Clippings/Gần 2 thập kỷ bị FED và UST ...lùa gà-P1.md` | 18,285 | 82 | `4a071de49989a70d2296e54503886d3af1987da09c8745434e82d001e6cdb7c3` |
| `01_sources/Clippings/Gần 2 thập kỷ bị FED và UST... lùa gà - P2.md` | 15,766 | 177 | `e5fc1e3510f8b6073526e3be218088796e43cf427ff29e4fa9c66192e1fe583c` |
| `01_sources/Clippings/Hiểu đúng về can thiệp UST buyback.md` | 5,270 | 49 | `30f4dc339d6c04103cc079ab2404352186efda53a2c0fb5e984ae189b67dabb5` |
| `01_sources/Clippings/Japan August-26 CPI Inflation Report.md` | 15,953 | 94 | `ff61dcf6fb3fe01e5368187e8dcfcc7e1a32415d0ebf49f5e5a6f46a0ee90317` |
| `01_sources/Clippings/Japan July-26 CPI Inflation Report.md` | 14,403 | 94 | `fda0418dc023076ae33da792a2d29bd8039bc89138cd70e3f195d6005788e1d6` |
| `01_sources/Clippings/Japan as a creditor nation- Cái kết không thể tránh khỏi sau hàng 2 thập kỷ QE.md` | 16,319 | 143 | `7efd69721788a8053e959b58a37e8c135927e72e711cf474be72f4f9ec167454` |
| `01_sources/Clippings/Khi nào lãi suất mới giảm Đánh giá lại các giả định sau hai tháng 6-82026 1.md` | 10,493 | 105 | `1fd6c06f1095691faf1248a2bf8686ad0ddd370ed5a79df72e59575041d6a711` |
| `01_sources/Clippings/Khi nào lãi suất mới giảm Đánh giá lại các giả định sau hai tháng 6-82026.md` | 10,493 | 105 | `1fd6c06f1095691faf1248a2bf8686ad0ddd370ed5a79df72e59575041d6a711` |
| `01_sources/Clippings/Khi thị trường quyết luôn hộ FED.md` | 14,875 | 79 | `25dfdbed2e92b31e2ad0394981c3ec0c054388dfa9459b161dc1b56e26299d5b` |
| `01_sources/Clippings/Khác biệt trong tiếp cận topdonw vs bottomup.md` | 3,624 | 69 | `11e1fc10b69b01de824f597ada46453dd4161e540fb735e2b08d5887da551390` |
| `01_sources/Clippings/Kể cả muốn BĐS giảm cũng cần rất nhiều tiền – Lan man.md` | 7,184 | 90 | `39e0ecc36b33ae836079ddb6bf643567a1e2e38562ce6e69a3d6701e7239faf3` |
| `01_sources/Clippings/Kể cả muốn BĐS giảm cũng cần rất nhiều tiền- Lan man.md` | 6,749 | 33 | `e169f80e509c6afeb924f6bc0333b3b577d0af44181e76f5d1a2a6abbce7a4dc` |
| `01_sources/Clippings/Lãi suất chưa thể hạ Nhấn mạnh lại điểm nghẽn từ TT1. LDR không giải quyết được vấn đề.md` | 11,192 | 43 | `96d47ed3cb4d47c0d0b648088b689489824c28e7b17f539b5c0ae4e80c58025d` |
| `01_sources/Clippings/Market Update Thị trường tiếp tục đòi hỏi một nền ls cao hơn.md` | 2,917 | 29 | `838a0c188a774537e64f24210c84849c623838fbbb200476924434497e490a08` |
| `01_sources/Clippings/Multi mismatch on BS.md` | 11,495 | 117 | `4d0bdc974625aeebc87be07a004e9c1f92b9adb81934cc4461ea39655c423ef5` |
| `01_sources/Clippings/Multi-Mismatch on BS part II.md` | 10,355 | 147 | `fa55c7fbe10dcd29ea8564cb8c8e4c9568d1342d6febf9bca6b7531eeebc7288` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part II Thị trường quá tập trung vào information mà không quan tâm fundamental.md` | 4,553 | 27 | `ba4ed3d30ff26b9e90127952bf94db259d3ea180a07d86ec3561a718904c5b2b` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part III Có hay không thì cần tập trung vẫn là fundamentals 1.md` | 6,005 | 33 | `96338326fb92b62768f6e5d79b8c9b8eba13ff870ec0c19c5d86435ec418b019` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part III Có hay không thì cần tập trung vẫn là fundamentals.md` | 6,005 | 33 | `c87361527d94e6a1a4409dae524c5b18bd0254a00452391e41c25bd2963e7695` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Thị trường có thể “lật mặt” nhanh hơn cả NYC.md` | 8,072 | 47 | `df8c782df5aa42f02200126b7cc1aeec7be1f3ec8791c55d7663ebb7d54bb2e8` |
| `01_sources/Clippings/Ngân hàng Nhà nước không cần “lãi” — mà cần thực hiện mục tiêu chính sách.md` | 8,468 | 109 | `97154da8298b6f0de0276e1f9aef5dc5c2d6fe18668c07dd70513a5fb1c4ee37` |
| `01_sources/Clippings/Ngân hàng có thực sự sẵn sàng sử dụng thanh khoản khi khủng hoảng xảy ra.md` | 6,913 | 43 | `49d5b0fbb3a20d1b91db0c34b5e14d5e51048fb689bd4d4f519b5f2b1f1095a3` |
| `01_sources/Clippings/Nhìn đi cũng nên nhìn lại- Chúng ta kỳ vọng hơi quá đáng. Update cuối tuần 15.08.md` | 2,521 | 31 | `cc6d30247d442f581cb6e8ee0d330f0983835c3707a0618c8c5415a166d1c99d` |
| `01_sources/Clippings/P1 Fed Hold có thể trở thành rủi ro lớn hơn đối với U.S. Treasuries.md` | 9,256 | 55 | `a2e9515bc61eeccd9e579af9fa2013e7a54cd58dcda75dfbb85fd474aec344ae` |
| `01_sources/Clippings/P2 Giữ cũng được vẫn hợp lý Fed Hold — Khi lạm phát xuất phát từ phía cung.md` | 5,089 | 43 | `93711bd6e96b479b2c015743330acffd1c13fffab7f17d6cf27f76d0e6c3a299` |
| `01_sources/Clippings/QE và QT  Không phải là 2 quá trình trái ngược nhau.md` | 4,851 | 29 | `84abf878610e93b11226f3c293eed6096c7d4a0c666a3ccfc63268ec3e1d7997` |
| `01_sources/Clippings/Repo Markets and the Fed’s Balance Sheet Implications for Monetary Policy Implementation.md` | 39,022 | 224 | `3df30b72cb146f7997f87dc0059c472f4104d7b923695fce1af142c5091aee4b` |
| `01_sources/Clippings/Sai lầm tiếp theo của SBV- COF VND có thể lớn hơn rất nhiều.md` | 5,588 | 40 | `47f35930f9889b963cadfac2c3d31083926c004384c9849c19782630191964d2` |
| `01_sources/Clippings/Say after me Treasury buybacks are not YCC.md` | 16,203 | 74 | `afd30b4c9c76dd1a35986b6dc726f9338da46f2ee19dfc473b8d32a181a067e2` |
| `01_sources/Clippings/Seasonal errors.md` | 16,158 | 80 | `bc5b78eef5e071189f0f3f3ad741ae78c754d175025b35de85efc344f565dfbb` |
| `01_sources/Clippings/Some thoughts on Asia FX and rates—Fed, AI, oil, and differentiation.md` | 21,060 | 112 | `01a4d23e74de2b7e8fee0919d06e24be4fed23726e043dd0456643e1025fa905` |
| `01_sources/Clippings/Some thoughts on Yen intervention.md` | 5,670 | 48 | `4d631a205114d55697ce85bdca2f38b4510e71df51f1a80779a54f70d0d201ba` |
| `01_sources/Clippings/Sự phức tạp của cân đối và vận hành nội sinh- Cách nhìn hệ thống cần thay đổi.md` | 4,188 | 39 | `2902ed3e26556a0b940d83186bc699955f90b821962ecf6d7464e3c9f3930d11` |
| `01_sources/Clippings/The Fed Has a Target, But No Roadmap.md` | 5,267 | 43 | `faddd1181a5ad849d44f40efa8e8b07e02faef31a05529f7697ecc7fb631b14d` |
| `01_sources/Clippings/The Hidden Defaults of Private Credit What the Numbers Don’t Show.md` | 14,756 | 54 | `aba18d8ca4957c15870d19010465f5a3692c0338016ed5279a584c465dc2762b` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part I.md` | 18,944 | 134 | `fd841c2347f0cd96d5e45d58ea0f1690abb6ac7679e8d13657d52bf6ccea6d13` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part II Update.md` | 8,967 | 64 | `e3c0a2227e4ab38565b5dbb3adbf6c6e00c8a46fd97846559b1395ddc4e848b0` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part II.md` | 17,589 | 146 | `c765179c0a7adbe789f46f2fc8dff49166f4cc347199d94e9780a1bbc070119b` |
| `01_sources/Clippings/Tiến gần hơn tới CNY Carry trade kiểu Trung.md` | 9,125 | 39 | `ef9c6476f3b54089e2d3a5833ef829152498cfc1485df6be99cf9a989dfa4459` |
| `01_sources/Clippings/Từ cổ chí kim, ngân hàng luôn dùng nguồn vốn ngắn hạn để xây dựng hệ thống, dù là 10 năm hay 100 năm.md` | 4,483 | 51 | `aa03af0dc85aac258bced56bb9c50b478db2fa9b40cbf854ca69e5a882712113` |
| `01_sources/Clippings/US July-26 CPI Inflation Report.md` | 12,174 | 93 | `bfcefad1149f8cdd20dc552375b154b9a610b06b92db139999df5c5637319995` |
| `01_sources/Clippings/USDJPY reached.md` | 3,695 | 27 | `05db02b7856dc3c38cba09e3f784beb2a2bf3475f6dc57ec794399f86efcf88f` |
| `01_sources/Clippings/Update- Global Macro- Thế giới không thiếu tiền. Thế giới đang thiếu một nơi để tiền đi vào mà không tạo ra một vấn đề mới.md` | 9,507 | 165 | `1f7181f952ec7720cf27e7ac646bf26098640ca4751bed1311162a3f5b2e80c0` |
| `01_sources/Clippings/Việt Nam phát hành TP USD 7% có ok.md` | 7,511 | 71 | `c9e82e511309351eadf5d7e8e3b751dfe2502fa6b51b67239de51225b7007a35` |
| `01_sources/Clippings/Vượt ra ngoài SLR Liệu cải cách quy định có thể mở rộng khả năng hấp thụ U.S. Treasuries dài hạn của hệ thống ngân hàng.md` | 24,118 | 463 | `da19fe46c9d3807e0a1d57dd120bc7031a4909ec52392842739cc6c6849c870b` |
| `01_sources/Clippings/Vấn đề chi phí vay- ngày càng tăng khi Vay Offshore.md` | 3,017 | 47 | `1246a4158f4e93b665273295d45581583ad373763b12bf815b831c5f2b02026f` |
| `01_sources/Clippings/Warsh’s Reaction-Function Guidance.md` | 27,146 | 136 | `9f7af242aa11de35294909739c86f8824e05a94ec96985d2b7bb91f68d94f43a` |
| `01_sources/Clippings/What Treasury Yields, SOFR, and TIPS are telling us.md` | 11,641 | 70 | `636c11146d28234fa75adbdb99730a6bf067b59a2c369a40495296e869ae3fda` |
| `01_sources/Clippings/What will be scarce.md` | 37,574 | 168 | `1b07485cc3c50981102948b8050ee14a6daec2112e8ded74320515a625d3cf73` |
| `01_sources/Clippings/XAUUSD vs XAUVND  2 tài sản trái ngược.md` | 10,516 | 100 | `5ee17c52619879e2001845a8f2795b16d11ae6f36417dba887b46f7d1ea0dade` |
| `01_sources/Clippings/Xauusd-Xauvnd-USTYield-VND Deposit Rate.md` | 3,023 | 25 | `1c2db19a974288ea76e0842a1e77e0f8f2c627defec27c36f33b097ea0e46745` |
| `01_sources/Clippings/Xu hướng de-regulation là tất yếu.md` | 3,898 | 66 | `4facb798039a774a2107d82d53089e4801a72dadd661df597082757ad1990d5f` |
| `01_sources/Clippings/Yen-tervention.md` | 16,165 | 70 | `dee2a4c8a46cca3a276d754816158b890321ab6bb255cd9b6d657e2cf4c491d0` |
| `01_sources/Clippings/Yields climb, yet risk appetite holds firm.md` | 48,099 | 280 | `48c882faaeb9ecaec38c6014cbc2874594ead65bf81fcbfc8ec5f14ea96adc4f` |
| `01_sources/Clippings/Ý nghĩa của việc can thiệp chủ động Buy Spot trong điều hành.md` | 9,060 | 87 | `306a6087243f3d2a948cc90d294af54a64c5391153dcae4a3376d5e588fe5517` |
| `01_sources/Clippings/Điểm yếu trong phân tích Top-down – Phần 1.md` | 12,251 | 187 | `4de132826ec4ee4802a4e9dd8a13199751bc26b5365d98a72f0f8534490597c0` |
| `01_sources/Clippings/Điểm yếu trong phân tích Topdown-P2- Không thể thiếu BottomUp.md` | 4,244 | 36 | `5285bed6bdc62bacd44e14d45542894672d491ef99279fd0b2b824c974ffd47d` |

## clippings

| | |
|---|---|
| Nhan đề | *Macro & Banking Web Clippings* — Tuyển tập bài viết phân tích vĩ mô, ALM ngân hàng thương mại, điều hành bảng cân đối NHTW và thị trường tiền tệ |
| Tác giả | Nhiều tác giả (Nguyễn Khánh / Hedge Academy, Federal Reserve Bank of New York, Federal Reserve Board, Bank for International Settlements, Gianluca Benigno, cùng các tác giả Substack) |
| Xuất bản | 2026 — Thu thập trực tiếp từ các cổng thông tin chuyên ngành và tài liệu nghiên cứu ngân hàng trung ương |
| Phân loại | Nguồn dài (`00_schema.md` §10) — 882 KB / 6.684 dòng trên 82 file `.md` |
| Nguồn file | Bài viết định dạng `.md` thu thập qua web clipper, lưu trữ nguyên bản trong thư mục nguồn `01_sources/Clippings/` |
| Tiến độ ingest | Đang ingest dở — `03_state/clippings.md` |

| Đường dẫn | Bytes | Dòng | SHA-256 |
|---|---|---|---|
| `01_sources/Clippings/5.2%, big problem Not at all.md` | 13.092 | 72 | `3624f5f4b7bf99691dc31ca5abde857d38b88960e302e3bf38682525e37b6dae` |
| `01_sources/Clippings/A Framework for Understanding the U.S. Treasury Repo Market.md` | 10.633 | 84 | `b542010ce08892ca3bb8307df27faa8620d133929a6ffb8e37ca619f832f4c5b` |
| `01_sources/Clippings/ALM P3 Cân nguồn Cân Tỷ lệ.md` | 1.426 | 19 | `a28230a28d16eeae9e44ca690eb8d28be500fa0c51615771a18012179139e9a7` |
| `01_sources/Clippings/ALM P5 – Bước đầu hiểu về sự phức tạp giữa Tây vs Ta trong ALM.md` | 7.034 | 41 | `dacfb2ff95d3ebb3430f350c472a324b0c93dff550dddcde09d4feb7386ebed3` |
| `01_sources/Clippings/ALM P6 – Hành vi nguồn vốn trên Thị trường 1 Khi mô hình hóa trở thành “fake”.md` | 6.788 | 55 | `db41e5cad7b91350c7537bea3dbbe3d3d0143bf7df997412e36c18e1286a06ba` |
| `01_sources/Clippings/ALM Part 4 Hiểu hành vi nguồn tiền.md` | 5.774 | 39 | `bc6f8ccc55330499371690e98d97fc235a00662fb7f5d3d6ef3fd4e103bc9c5f` |
| `01_sources/Clippings/Bạn muốn nghiên cứu về chính sách tiền tệ.md` | 2.442 | 29 | `d1ad7622fcf2da3699d4266203f8ccc0ae19bafbfed094849732d880e32651dc` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý P2 Nuôi Zombie kiểu Trung.md` | 12.234 | 81 | `4e00de7ff70addd562d1a5d8815f5a325fbee6c6cb14bdde8931e83514936731` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý P3 Nhìn chung phải có negotiate.md` | 15.625 | 59 | `22bbc93d340081574ffe69dbe2a5bdbe357ff709e0417882db0311dbc2c07509` |
| `01_sources/Clippings/CNY Carry Trade không hẳn là vô lý.md` | 12.623 | 45 | `5ac7b5ac49323af055dc509ac139324a21909e50ebed8c5222644437c28ebaa3` |
| `01_sources/Clippings/Central Bank Commentary (July-26) Federal Reserve, Bank of Japan and Bank of England.md` | 31.219 | 189 | `f9e80af0cdf7170fd81ef0e593aac74faa29e57e4fbc3b08a947d60577a73e43` |
| `01_sources/Clippings/Chi phí vốn VND - Lý do tại sao lại lớn.md` | 6.126 | 149 | `a57d6a9e3dc58b8a901f9b429e0d0349533510c5c58eaaaef52ab5ba1b10a522` |
| `01_sources/Clippings/China August-26 CPI Inflation Report.md` | 15.463 | 105 | `eef1d6428fd3106ba9b6cd6621c1932ab0fd907461280cee00746fb0ab7eed1a` |
| `01_sources/Clippings/China July-26 CPI Inflation Report.md` | 15.471 | 105 | `c7b2eef16b9f9ef58ddd5c9a022510637e3b47649e0b2395b920ab4fdb3ed257` |
| `01_sources/Clippings/Chính sách hành lang lãi suất của SBV so với bản gốc.md` | 3.945 | 43 | `180da21ec963d34968a576ae69d72e5684ad659a84f9626eb06e5f506203044a` |
| `01_sources/Clippings/Cost of Funds USD vs VND Cách nhìn toàn diện.md` | 2.592 | 19 | `a961335183c85e61b21696e4a47880d147606a44eb11c3b66e717cc20431f67b` |
| `01_sources/Clippings/Cách nhìn hệ thống cần phải thay đổi-P2 Họp toàn Bug.md` | 4.479 | 41 | `3c0cb2f770a2309eef654b8c7bcdf6e269add7dde19ea72d53d3ad712acf7481` |
| `01_sources/Clippings/Cách nhìn hệ thống cần phải thay đổi.md` | 4.513 | 31 | `a53f2c3d6a554c94021f79e440dc247d6b23f2c6cf048aac4259bf5603e716da` |
| `01_sources/Clippings/Cân dòng tiền – Khái niệm đầu tiên về cân đối- ALM P1.md` | 6.907 | 35 | `040363615eca411b7d38342d196040b550c6cd602952b24c99ba0b7b4461bcdf` |
| `01_sources/Clippings/Cân nguồn – Phần tiếp theo Cân kỳ hạn.md` | 6.566 | 49 | `1a704fb139e858a41bcd923a862bfe94f18536479a532621f3fc02433dbb1d26` |
| `01_sources/Clippings/DTTT thay thế TT22.md` | 2.802 | 45 | `11a8f25692b40f0fd69bcd37ad473557b47e973d690786632a39a93359d00097` |
| `01_sources/Clippings/Debt Structure sau 5y hay 10y vẫn thế cả.md` | 8.630 | 27 | `3a6d5cd0c109771417b287e919d79b0b1b1838952eb0f495e11be18d46c42749` |
| `01_sources/Clippings/FED nâng lãi suất không còn đáng sợ như trước.md` | 4.087 | 31 | `cd32ecea69744a3765eeb995f836a8962402067086fedf39815403a4a3857b93` |
| `01_sources/Clippings/FOMC An Almost Certain Hike.md` | 10.752 | 117 | `8a67fb3fa441314f1d4c7ddd9f145c288bbdce0348484e072c66da3ff80ed234` |
| `01_sources/Clippings/Fed thực sự khổ.md` | 3.491 | 29 | `6e391f13a969e4120a4a83b3be355ba9481be2f0765529498180ccd7d95debb7` |
| `01_sources/Clippings/Gần 2 thập kỷ bị FED và UST ...lùa gà-P1.md` | 18.285 | 82 | `4a071de49989a70d2296e54503886d3af1987da09c8745434e82d001e6cdb7c3` |
| `01_sources/Clippings/Gần 2 thập kỷ bị FED và UST... lùa gà - P2.md` | 15.766 | 177 | `e5fc1e3510f8b6073526e3be218088796e43cf427ff29e4fa9c66192e1fe583c` |
| `01_sources/Clippings/Hiểu đúng về can thiệp UST buyback.md` | 5.270 | 49 | `30f4dc339d6c04103cc079ab2404352186efda53a2c0fb5e984ae189b67dabb5` |
| `01_sources/Clippings/Japan August-26 CPI Inflation Report.md` | 15.953 | 94 | `ff61dcf6fb3fe01e5368187e8dcfcc7e1a32415d0ebf49f5e5a6f46a0ee90317` |
| `01_sources/Clippings/Japan July-26 CPI Inflation Report.md` | 14.403 | 94 | `fda0418dc023076ae33da792a2d29bd8039bc89138cd70e3f195d6005788e1d6` |
| `01_sources/Clippings/Japan as a creditor nation- Cái kết không thể tránh khỏi sau hàng 2 thập kỷ QE.md` | 16.319 | 143 | `7efd69721788a8053e959b58a37e8c135927e72e711cf474be72f4f9ec167454` |
| `01_sources/Clippings/Khi nào lãi suất mới giảm Đánh giá lại các giả định sau hai tháng 6-82026 1.md` | 10.493 | 105 | `1fd6c06f1095691faf1248a2bf8686ad0ddd370ed5a79df72e59575041d6a711` |
| `01_sources/Clippings/Khi nào lãi suất mới giảm Đánh giá lại các giả định sau hai tháng 6-82026.md` | 10.493 | 105 | `1fd6c06f1095691faf1248a2bf8686ad0ddd370ed5a79df72e59575041d6a711` |
| `01_sources/Clippings/Khi thị trường quyết luôn hộ FED.md` | 14.875 | 79 | `25dfdbed2e92b31e2ad0394981c3ec0c054388dfa9459b161dc1b56e26299d5b` |
| `01_sources/Clippings/Khác biệt trong tiếp cận topdonw vs bottomup.md` | 3.624 | 69 | `11e1fc10b69b01de824f597ada46453dd4161e540fb735e2b08d5887da551390` |
| `01_sources/Clippings/Kể cả muốn BĐS giảm cũng cần rất nhiều tiền – Lan man.md` | 7.184 | 90 | `39e0ecc36b33ae836079ddb6bf643567a1e2e38562ce6e69a3d6701e7239faf3` |
| `01_sources/Clippings/Kể cả muốn BĐS giảm cũng cần rất nhiều tiền- Lan man.md` | 6.749 | 33 | `e169f80e509c6afeb924f6bc0333b3b577d0af44181e76f5d1a2a6abbce7a4dc` |
| `01_sources/Clippings/Lãi suất chưa thể hạ Nhấn mạnh lại điểm nghẽn từ TT1. LDR không giải quyết được vấn đề.md` | 11.192 | 43 | `96d47ed3cb4d47c0d0b648088b689489824c28e7b17f539b5c0ae4e80c58025d` |
| `01_sources/Clippings/Market Update Thị trường tiếp tục đòi hỏi một nền ls cao hơn.md` | 2.917 | 29 | `838a0c188a774537e64f24210c84849c623838fbbb200476924434497e490a08` |
| `01_sources/Clippings/Multi mismatch on BS.md` | 11.495 | 117 | `4d0bdc974625aeebc87be07a004e9c1f92b9adb81934cc4461ea39655c423ef5` |
| `01_sources/Clippings/Multi-Mismatch on BS part II.md` | 10.355 | 147 | `fa55c7fbe10dcd29ea8564cb8c8e4c9568d1342d6febf9bca6b7531eeebc7288` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part II Thị trường quá tập trung vào information mà không quan tâm fundamental.md` | 4.553 | 27 | `ba4ed3d30ff26b9e90127952bf94db259d3ea180a07d86ec3561a718904c5b2b` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part III Có hay không thì cần tập trung vẫn là fundamentals 1.md` | 6.005 | 33 | `96338326fb92b62768f6e5d79b8c9b8eba13ff870ec0c19c5d86435ec418b019` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Part III Có hay không thì cần tập trung vẫn là fundamentals.md` | 6.005 | 33 | `c87361527d94e6a1a4409dae524c5b18bd0254a00452391e41c25bd2963e7695` |
| `01_sources/Clippings/Mặt trái của việc không có Forward Guidance Thị trường có thể “lật mặt” nhanh hơn cả NYC.md` | 8.072 | 47 | `df8c782df5aa42f02200126b7cc1aeec7be1f3ec8791c55d7663ebb7d54bb2e8` |
| `01_sources/Clippings/Ngân hàng Nhà nước không cần “lãi” — mà cần thực hiện mục tiêu chính sách.md` | 8.468 | 109 | `97154da8298b6f0de0276e1f9aef5dc5c2d6fe18668c07dd70513a5fb1c4ee37` |
| `01_sources/Clippings/Ngân hàng có thực sự sẵn sàng sử dụng thanh khoản khi khủng hoảng xảy ra.md` | 6.913 | 43 | `49d5b0fbb3a20d1b91db0c34b5e14d5e51048fb689bd4d4f519b5f2b1f1095a3` |
| `01_sources/Clippings/Nhìn đi cũng nên nhìn lại- Chúng ta kỳ vọng hơi quá đáng. Update cuối tuần 15.08.md` | 2.521 | 31 | `cc6d30247d442f581cb6e8ee0d330f0983835c3707a0618c8c5415a166d1c99d` |
| `01_sources/Clippings/P1 Fed Hold có thể trở thành rủi ro lớn hơn đối với U.S. Treasuries.md` | 9.256 | 55 | `a2e9515bc61eeccd9e579af9fa2013e7a54cd58dcda75dfbb85fd474aec344ae` |
| `01_sources/Clippings/P2 Giữ cũng được vẫn hợp lý Fed Hold — Khi lạm phát xuất phát từ phía cung.md` | 5.089 | 43 | `93711bd6e96b479b2c015743330acffd1c13fffab7f17d6cf27f76d0e6c3a299` |
| `01_sources/Clippings/QE và QT  Không phải là 2 quá trình trái ngược nhau.md` | 4.851 | 29 | `84abf878610e93b11226f3c293eed6096c7d4a0c666a3ccfc63268ec3e1d7997` |
| `01_sources/Clippings/Repo Markets and the Fed’s Balance Sheet Implications for Monetary Policy Implementation.md` | 39.022 | 224 | `3df30b72cb146f7997f87dc0059c472f4104d7b923695fce1af142c5091aee4b` |
| `01_sources/Clippings/Sai lầm tiếp theo của SBV- COF VND có thể lớn hơn rất nhiều.md` | 5.588 | 40 | `47f35930f9889b963cadfac2c3d31083926c004384c9849c19782630191964d2` |
| `01_sources/Clippings/Say after me Treasury buybacks are not YCC.md` | 16.203 | 74 | `afd30b4c9c76dd1a35986b6dc726f9338da46f2ee19dfc473b8d32a181a067e2` |
| `01_sources/Clippings/Seasonal errors.md` | 16.158 | 80 | `bc5b78eef5e071189f0f3f3ad741ae78c754d175025b35de85efc344f565dfbb` |
| `01_sources/Clippings/Some thoughts on Asia FX and rates—Fed, AI, oil, and differentiation.md` | 21.060 | 112 | `01a4d23e74de2b7e8fee0919d06e24be4fed23726e043dd0456643e1025fa905` |
| `01_sources/Clippings/Some thoughts on Yen intervention.md` | 5.670 | 48 | `4d631a205114d55697ce85bdca2f38b4510e71df51f1a80779a54f70d0d201ba` |
| `01_sources/Clippings/Sự phức tạp của cân đối và vận hành nội sinh- Cách nhìn hệ thống cần thay đổi.md` | 4.188 | 39 | `2902ed3e26556a0b940d83186bc699955f90b821962ecf6d7464e3c9f3930d11` |
| `01_sources/Clippings/The Fed Has a Target, But No Roadmap.md` | 5.267 | 43 | `faddd1181a5ad849d44f40efa8e8b07e02faef31a05529f7697ecc7fb631b14d` |
| `01_sources/Clippings/The Hidden Defaults of Private Credit What the Numbers Don’t Show.md` | 14.756 | 54 | `aba18d8ca4957c15870d19010465f5a3692c0338016ed5279a584c465dc2762b` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part I.md` | 18.944 | 134 | `fd841c2347f0cd96d5e45d58ea0f1690abb6ac7679e8d13657d52bf6ccea6d13` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part II Update.md` | 8.967 | 64 | `e3c0a2227e4ab38565b5dbb3adbf6c6e00c8a46fd97846559b1395ddc4e848b0` |
| `01_sources/Clippings/The Return of Nonlinear Inflation Part II.md` | 17.589 | 146 | `c765179c0a7adbe789f46f2fc8dff49166f4cc347199d94e9780a1bbc070119b` |
| `01_sources/Clippings/Tiến gần hơn tới CNY Carry trade kiểu Trung.md` | 9.125 | 39 | `ef9c6476f3b54089e2d3a5833ef829152498cfc1485df6be99cf9a989dfa4459` |
| `01_sources/Clippings/Từ cổ chí kim, ngân hàng luôn dùng nguồn vốn ngắn hạn để xây dựng hệ thống, dù là 10 năm hay 100 năm.md` | 4.483 | 51 | `aa03af0dc85aac258bced56bb9c50b478db2fa9b40cbf854ca69e5a882712113` |
| `01_sources/Clippings/US July-26 CPI Inflation Report.md` | 12.174 | 93 | `bfcefad1149f8cdd20dc552375b154b9a610b06b92db139999df5c5637319995` |
| `01_sources/Clippings/USDJPY reached.md` | 3.695 | 27 | `05db02b7856dc3c38cba09e3f784beb2a2bf3475f6dc57ec794399f86efcf88f` |
| `01_sources/Clippings/Update- Global Macro- Thế giới không thiếu tiền. Thế giới đang thiếu một nơi để tiền đi vào mà không tạo ra một vấn đề mới.md` | 9.507 | 165 | `1f7181f952ec7720cf27e7ac646bf26098640ca4751bed1311162a3f5b2e80c0` |
| `01_sources/Clippings/Việt Nam phát hành TP USD 7% có ok.md` | 7.511 | 71 | `c9e82e511309351eadf5d7e8e3b751dfe2502fa6b51b67239de51225b7007a35` |
| `01_sources/Clippings/Vượt ra ngoài SLR Liệu cải cách quy định có thể mở rộng khả năng hấp thụ U.S. Treasuries dài hạn của hệ thống ngân hàng.md` | 24.118 | 463 | `da19fe46c9d3807e0a1d57dd120bc7031a4909ec52392842739cc6c6849c870b` |
| `01_sources/Clippings/Vấn đề chi phí vay- ngày càng tăng khi Vay Offshore.md` | 3.017 | 47 | `1246a4158f4e93b665273295d45581583ad373763b12bf815b831c5f2b02026f` |
| `01_sources/Clippings/Warsh’s Reaction-Function Guidance.md` | 27.146 | 136 | `9f7af242aa11de35294909739c86f8824e05a94ec96985d2b7bb91f68d94f43a` |
| `01_sources/Clippings/What Treasury Yields, SOFR, and TIPS are telling us.md` | 11.641 | 70 | `636c11146d28234fa75adbdb99730a6bf067b59a2c369a40495296e869ae3fda` |
| `01_sources/Clippings/What will be scarce.md` | 37.574 | 168 | `1b07485cc3c50981102948b8050ee14a6daec2112e8ded74320515a625d3cf73` |
| `01_sources/Clippings/XAUUSD vs XAUVND  2 tài sản trái ngược.md` | 10.516 | 100 | `5ee17c52619879e2001845a8f2795b16d11ae6f36417dba887b46f7d1ea0dade` |
| `01_sources/Clippings/Xauusd-Xauvnd-USTYield-VND Deposit Rate.md` | 3.023 | 25 | `1c2db19a974288ea76e0842a1e77e0f8f2c627defec27c36f33b097ea0e46745` |
| `01_sources/Clippings/Xu hướng de-regulation là tất yếu.md` | 3.898 | 66 | `4facb798039a774a2107d82d53089e4801a72dadd661df597082757ad1990d5f` |
| `01_sources/Clippings/Yen-tervention.md` | 16.165 | 70 | `dee2a4c8a46cca3a276d754816158b890321ab6bb255cd9b6d657e2cf4c491d0` |
| `01_sources/Clippings/Yields climb, yet risk appetite holds firm.md` | 48.099 | 280 | `48c882faaeb9ecaec38c6014cbc2874594ead65bf81fcbfc8ec5f14ea96adc4f` |
| `01_sources/Clippings/Ý nghĩa của việc can thiệp chủ động Buy Spot trong điều hành.md` | 9.060 | 87 | `306a6087243f3d2a948cc90d294af54a64c5391153dcae4a3376d5e588fe5517` |
| `01_sources/Clippings/Điểm yếu trong phân tích Top-down – Phần 1.md` | 12.251 | 187 | `4de132826ec4ee4802a4e9dd8a13199751bc26b5365d98a72f0f8534490597c0` |
| `01_sources/Clippings/Điểm yếu trong phân tích Topdown-P2- Không thể thiếu BottomUp.md` | 4.244 | 36 | `5285bed6bdc62bacd44e14d45542894672d491ef99279fd0b2b824c974ffd47d` |
