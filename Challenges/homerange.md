# HOME-RANGE IP AND OBSERVATIONS

This page contains information on 12 different vulnerable machines. Each one is  to be completed within the next year. 356 days. They are accessible through the IP addresses provided, and sit between two subnets.

# 192.168.56.101 - Debian 10 - "EvilBox: One"

    Nmap scan report for 192.168.56.101
    Host is up (0.0034s latency).
    Not shown: 897 filtered tcp ports (no-response), 101 closed tcp ports (reset)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
    | vulners: 
    |   cpe:/a:openbsd:openssh:7.9p1: 
    |     	PACKETSTORM:173661	9.8	https://vulners.com/packetstorm/PACKETSTORM:173661	*EXPLOIT*
    |     	F0979183-AE88-53B4-86CF-3AF0523F3807	9.8	https://vulners.com/githubexploit/F0979183-AE88-53B4-86CF-3AF0523F3807	*EXPLOIT*
    |     	CVE-2023-38408	9.8	https://vulners.com/cve/CVE-2023-38408
    |     	B8190CDB-3EB9-5631-9828-8064A1575B23	9.8	https://vulners.com/githubexploit/B8190CDB-3EB9-5631-9828-8064A1575B23	*EXPLOIT*
    |     	A2B36B85-C737-548F-8C04-9339EDCDBFF5	9.8	https://vulners.com/githubexploit/A2B36B85-C737-548F-8C04-9339EDCDBFF5	*EXPLOIT*
    |     	8FC9C5AB-3968-5F3C-825E-E8DB5379A623	9.8	https://vulners.com/githubexploit/8FC9C5AB-3968-5F3C-825E-E8DB5379A623	*EXPLOIT*
    |     	8AD01159-548E-546E-AA87-2DE89F3927EC	9.8	https://vulners.com/githubexploit/8AD01159-548E-546E-AA87-2DE89F3927EC	*EXPLOIT*
    |     	6192C35D-F78B-5C0A-AB8D-9826A79A5320	9.8	https://vulners.com/githubexploit/6192C35D-F78B-5C0A-AB8D-9826A79A5320	*EXPLOIT*
    |     	2227729D-6700-5C8F-8930-1EEAFD4B9FF0	9.8	https://vulners.com/githubexploit/2227729D-6700-5C8F-8930-1EEAFD4B9FF0	*EXPLOIT*
    |     	0221525F-07F5-5790-912D-F4B9E2D1B587	9.8	https://vulners.com/githubexploit/0221525F-07F5-5790-912D-F4B9E2D1B587	*EXPLOIT*
    |     	CVE-2026-35414	8.1	https://vulners.com/cve/CVE-2026-35414
    |     	CVE-2026-35386	8.1	https://vulners.com/cve/CVE-2026-35386
    |     	CVE-2026-35385	8.1	https://vulners.com/cve/CVE-2026-35385
    |     	BA3887BD-F579-53B1-A4A4-FF49E953E1C0	8.1	https://vulners.com/githubexploit/BA3887BD-F579-53B1-A4A4-FF49E953E1C0	*EXPLOIT*
    |     	4FB01B00-F993-5CAF-BD57-D7E290D10C1F	8.1	https://vulners.com/githubexploit/4FB01B00-F993-5CAF-BD57-D7E290D10C1F	*EXPLOIT*
    |     	CVE-2020-15778	7.8	https://vulners.com/cve/CVE-2020-15778
    |     	CVE-2019-16905	7.8	https://vulners.com/cve/CVE-2019-16905
    |     	C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3	7.8	https://vulners.com/githubexploit/C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3	*EXPLOIT*
    |     	991D2CC4-0E09-5745-97A2-4917461BD6EC	7.8	https://vulners.com/githubexploit/991D2CC4-0E09-5745-97A2-4917461BD6EC	*EXPLOIT*
    |     	2E719186-2FED-58A8-A150-762EFBAAA523	7.8	https://vulners.com/gitee/2E719186-2FED-58A8-A150-762EFBAAA523	*EXPLOIT*
    |     	23CC97BE-7C95-513B-9E73-298C48D74432	7.8	https://vulners.com/githubexploit/23CC97BE-7C95-513B-9E73-298C48D74432	*EXPLOIT*
    |     	10213DBE-F683-58BB-B6D3-353173626207	7.8	https://vulners.com/githubexploit/10213DBE-F683-58BB-B6D3-353173626207	*EXPLOIT*
    |     	CVE-2021-41617	7.0	https://vulners.com/cve/CVE-2021-41617
    |     	284B94FC-FD5D-5C47-90EA-47900DAD1D1E	7.0	https://vulners.com/githubexploit/284B94FC-FD5D-5C47-90EA-47900DAD1D1E	*EXPLOIT*
    |     	PACKETSTORM:189283	6.8	https://vulners.com/packetstorm/PACKETSTORM:189283	*EXPLOIT*
    |     	EDB-ID:46516	6.8	https://vulners.com/exploitdb/EDB-ID:46516	*EXPLOIT*
    |     	EDB-ID:46193	6.8	https://vulners.com/exploitdb/EDB-ID:46193	*EXPLOIT*
    |     	CVE-2025-26465	6.8	https://vulners.com/cve/CVE-2025-26465
    |     	CVE-2019-6110	6.8	https://vulners.com/cve/CVE-2019-6110
    |     	CVE-2019-6109	6.8	https://vulners.com/cve/CVE-2019-6109
    |     	9D8432B9-49EC-5F45-BB96-329B1F2B2254	6.8	https://vulners.com/githubexploit/9D8432B9-49EC-5F45-BB96-329B1F2B2254	*EXPLOIT*
    |     	85FCDCC6-9A03-597E-AB4F-FA4DAC04F8D0	6.8	https://vulners.com/githubexploit/85FCDCC6-9A03-597E-AB4F-FA4DAC04F8D0	*EXPLOIT*
    |     	1337DAY-ID-39918	6.8	https://vulners.com/zdt/1337DAY-ID-39918	*EXPLOIT*
    |     	1337DAY-ID-32328	6.8	https://vulners.com/zdt/1337DAY-ID-32328	*EXPLOIT*
    |     	1337DAY-ID-32009	6.8	https://vulners.com/zdt/1337DAY-ID-32009	*EXPLOIT*
    |     	D104D2BF-ED22-588B-A9B2-3CCC562FE8C0	6.5	https://vulners.com/githubexploit/D104D2BF-ED22-588B-A9B2-3CCC562FE8C0	*EXPLOIT*
    |     	CVE-2026-35387	6.5	https://vulners.com/cve/CVE-2026-35387
    |     	CVE-2023-51385	6.5	https://vulners.com/cve/CVE-2023-51385
    |     	C07ADB46-24B8-57B7-B375-9C761F4750A2	6.5	https://vulners.com/githubexploit/C07ADB46-24B8-57B7-B375-9C761F4750A2	*EXPLOIT*
    |     	A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C	6.5	https://vulners.com/githubexploit/A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C	*EXPLOIT*
    |     	65B15AA1-2A8D-53C1-9499-69EBA3619F1C	6.5	https://vulners.com/githubexploit/65B15AA1-2A8D-53C1-9499-69EBA3619F1C	*EXPLOIT*
    |     	5325A9D6-132B-590C-BDEF-0CB105252732	6.5	https://vulners.com/gitee/5325A9D6-132B-590C-BDEF-0CB105252732	*EXPLOIT*
    |     	530326CF-6AB3-5643-AA16-73DC8CB44742	6.5	https://vulners.com/githubexploit/530326CF-6AB3-5643-AA16-73DC8CB44742	*EXPLOIT*
    |     	FD2E0EBA-ED84-5304-8862-84BCDEB2F288	5.9	https://vulners.com/githubexploit/FD2E0EBA-ED84-5304-8862-84BCDEB2F288	*EXPLOIT*
    |     	CVE-2023-48795	5.9	https://vulners.com/cve/CVE-2023-48795
    |     	CVE-2020-14145	5.9	https://vulners.com/cve/CVE-2020-14145
    |     	CVE-2019-6111	5.9	https://vulners.com/cve/CVE-2019-6111
    |     	CNVD-2021-25272	5.9	https://vulners.com/cnvd/CNVD-2021-25272
    |     	721F040C-37BC-59E1-9433-01A2EAC2E755	5.9	https://vulners.com/githubexploit/721F040C-37BC-59E1-9433-01A2EAC2E755	*EXPLOIT*
    |     	6D74A425-60A7-557A-B469-1DD96A2D8FF8	5.9	https://vulners.com/githubexploit/6D74A425-60A7-557A-B469-1DD96A2D8FF8	*EXPLOIT*
    |     	EXPLOITPACK:98FE96309F9524B8C84C508837551A19	5.8	https://vulners.com/exploitpack/EXPLOITPACK:98FE96309F9524B8C84C508837551A19	*EXPLOIT*
    |     	EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	5.8	https://vulners.com/exploitpack/EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	*EXPLOIT*
    |     	CVE-2018-20685	5.3	https://vulners.com/cve/CVE-2018-20685
    |     	CVE-2016-20012	5.3	https://vulners.com/cve/CVE-2016-20012
    |     	CNVD-2019-01296	5.3	https://vulners.com/cnvd/CNVD-2019-01296
    |     	CVE-2025-32728	4.3	https://vulners.com/cve/CVE-2025-32728
    |     	CVE-2021-36368	3.7	https://vulners.com/cve/CVE-2021-36368
    |     	CVE-2025-61985	3.6	https://vulners.com/cve/CVE-2025-61985
    |     	CVE-2025-61984	3.6	https://vulners.com/cve/CVE-2025-61984
    |     	B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150	3.6	https://vulners.com/githubexploit/B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150	*EXPLOIT*
    |     	4C6E2182-0E99-5626-83F6-1646DD648C57	3.6	https://vulners.com/githubexploit/4C6E2182-0E99-5626-83F6-1646DD648C57	*EXPLOIT*
    |     	CVE-2026-35388	2.5	https://vulners.com/cve/CVE-2026-35388
    |_    	PACKETSTORM:151227	0.0	https://vulners.com/packetstorm/PACKETSTORM:151227	*EXPLOIT*
    80/tcp open  http    Apache httpd 2.4.38 ((Debian))
    | vulners: 
    |   cpe:/a:apache:http_server:2.4.38: 
    |     	PACKETSTORM:176334	9.8	https://vulners.com/packetstorm/PACKETSTORM:176334	*EXPLOIT*
    |     	PACKETSTORM:171631	9.8	https://vulners.com/packetstorm/PACKETSTORM:171631	*EXPLOIT*
    |     	HTTPD:C072933AA965A86DA3E2C9172FFC1569	9.8	https://vulners.com/httpd/HTTPD:C072933AA965A86DA3E2C9172FFC1569
    |     	HTTPD:A1BBCE110E077FFBF4469D4F06DB9293	9.8	https://vulners.com/httpd/HTTPD:A1BBCE110E077FFBF4469D4F06DB9293
    |     	HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D	9.8	https://vulners.com/httpd/HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D
    |     	HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8	9.8	https://vulners.com/httpd/HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8
    |     	HTTPD:9AD76A782F4E66676719E36B64777A7A	9.8	https://vulners.com/httpd/HTTPD:9AD76A782F4E66676719E36B64777A7A
    |     	HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E	9.8	https://vulners.com/httpd/HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E
    |     	HTTPD:126D03F016241FBEDC0253722047ACEA	9.8	https://vulners.com/httpd/HTTPD:126D03F016241FBEDC0253722047ACEA
    |     	EDB-ID:51193	9.8	https://vulners.com/exploitdb/EDB-ID:51193	*EXPLOIT*
    |     	D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52	9.8	https://vulners.com/githubexploit/D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52	*EXPLOIT*
    |     	CVE-2026-28780	9.8	https://vulners.com/cve/CVE-2026-28780
    |     	CVE-2024-38476	9.8	https://vulners.com/cve/CVE-2024-38476
    |     	CVE-2024-38474	9.8	https://vulners.com/cve/CVE-2024-38474
    |     	CVE-2023-25690	9.8	https://vulners.com/cve/CVE-2023-25690
    |     	CVE-2022-31813	9.8	https://vulners.com/cve/CVE-2022-31813
    |     	CVE-2022-23943	9.8	https://vulners.com/cve/CVE-2022-23943
    |     	CVE-2022-22720	9.8	https://vulners.com/cve/CVE-2022-22720
    |     	CVE-2021-44790	9.8	https://vulners.com/cve/CVE-2021-44790
    |     	CVE-2021-39275	9.8	https://vulners.com/cve/CVE-2021-39275
    |     	CVE-2021-26691	9.8	https://vulners.com/cve/CVE-2021-26691
    |     	CVE-2020-11984	9.8	https://vulners.com/cve/CVE-2020-11984
    |     	CNVD-2024-36391	9.8	https://vulners.com/cnvd/CNVD-2024-36391
    |     	CNVD-2024-36388	9.8	https://vulners.com/cnvd/CNVD-2024-36388
    |     	CNVD-2022-51061	9.8	https://vulners.com/cnvd/CNVD-2022-51061
    |     	CNVD-2022-41640	9.8	https://vulners.com/cnvd/CNVD-2022-41640
    |     	CNVD-2022-03225	9.8	https://vulners.com/cnvd/CNVD-2022-03225
    |     	CNVD-2021-102386	9.8	https://vulners.com/cnvd/CNVD-2021-102386
    |     	CNVD-2020-46280	9.8	https://vulners.com/cnvd/CNVD-2020-46280
    |     	64A540A8-D918-5BEA-8F60-987F97B27A0C	9.8	https://vulners.com/githubexploit/64A540A8-D918-5BEA-8F60-987F97B27A0C	*EXPLOIT*
    |     	5C1BB960-90C1-5EBF-9BEF-F58BFFDFEED9	9.8	https://vulners.com/githubexploit/5C1BB960-90C1-5EBF-9BEF-F58BFFDFEED9	*EXPLOIT*
    |     	3F17CA20-788F-5C45-88B3-E12DB2979B7B	9.8	https://vulners.com/githubexploit/3F17CA20-788F-5C45-88B3-E12DB2979B7B	*EXPLOIT*
    |     	1337DAY-ID-39214	9.8	https://vulners.com/zdt/1337DAY-ID-39214	*EXPLOIT*
    |     	1337DAY-ID-38427	9.8	https://vulners.com/zdt/1337DAY-ID-38427	*EXPLOIT*
    |     	1337DAY-ID-34882	9.8	https://vulners.com/zdt/1337DAY-ID-34882	*EXPLOIT*
    |     	PACKETSTORM:213257	9.1	https://vulners.com/packetstorm/PACKETSTORM:213257	*EXPLOIT*
    |     	HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6	9.1	https://vulners.com/httpd/HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6
    |     	HTTPD:3512E3F62E72F03B59F5E9CF8ECB3EEF	9.1	https://vulners.com/httpd/HTTPD:3512E3F62E72F03B59F5E9CF8ECB3EEF
    |     	HTTPD:2C227652EE0B3B961706AAFCACA3D1E1	9.1	https://vulners.com/httpd/HTTPD:2C227652EE0B3B961706AAFCACA3D1E1
    |     	FD2EE3A5-BAEA-5845-BA35-E6889992214F	9.1	https://vulners.com/githubexploit/FD2EE3A5-BAEA-5845-BA35-E6889992214F	*EXPLOIT*
    |     	FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7	9.1	https://vulners.com/githubexploit/FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7	*EXPLOIT*
    |     	E606D7F4-5FA2-5907-B30E-367D6FFECD89	9.1	https://vulners.com/githubexploit/E606D7F4-5FA2-5907-B30E-367D6FFECD89	*EXPLOIT*
    |     	D8A19443-2A37-5592-8955-F614504AAF45	9.1	https://vulners.com/githubexploit/D8A19443-2A37-5592-8955-F614504AAF45	*EXPLOIT*
    |     	CVE-2025-23048	9.1	https://vulners.com/cve/CVE-2025-23048
    |     	CVE-2024-40898	9.1	https://vulners.com/cve/CVE-2024-40898
    |     	CVE-2024-38475	9.1	https://vulners.com/cve/CVE-2024-38475
    |     	CVE-2022-28615	9.1	https://vulners.com/cve/CVE-2022-28615
    |     	CVE-2022-22721	9.1	https://vulners.com/cve/CVE-2022-22721
    |     	CVE-2019-10082	9.1	https://vulners.com/cve/CVE-2019-10082
    |     	CNVD-2025-16610	9.1	https://vulners.com/cnvd/CNVD-2025-16610
    |     	CNVD-2024-36387	9.1	https://vulners.com/cnvd/CNVD-2024-36387
    |     	CNVD-2024-33814	9.1	https://vulners.com/cnvd/CNVD-2024-33814
    |     	CNVD-2022-51060	9.1	https://vulners.com/cnvd/CNVD-2022-51060
    |     	CNVD-2022-41638	9.1	https://vulners.com/cnvd/CNVD-2022-41638
    |     	B5E74010-A082-5ECE-AB37-623A5B33FE7D	9.1	https://vulners.com/githubexploit/B5E74010-A082-5ECE-AB37-623A5B33FE7D	*EXPLOIT*
    |     	5418A85B-F4B7-5BBD-B106-0800AC961C7A	9.1	https://vulners.com/githubexploit/5418A85B-F4B7-5BBD-B106-0800AC961C7A	*EXPLOIT*
    |     	HTTPD:1B3D546A8500818AAC5B1359FE11A7E4	9.0	https://vulners.com/httpd/HTTPD:1B3D546A8500818AAC5B1359FE11A7E4
    |     	CVE-2022-36760	9.0	https://vulners.com/cve/CVE-2022-36760
    |     	CVE-2021-40438	9.0	https://vulners.com/cve/CVE-2021-40438
    |     	CNVD-2023-30860	9.0	https://vulners.com/cnvd/CNVD-2023-30860
    |     	CNVD-2022-03224	9.0	https://vulners.com/cnvd/CNVD-2022-03224
    |     	AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C	9.0	https://vulners.com/githubexploit/AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C	*EXPLOIT*
    |     	9D9B3F4D-6B5C-5377-BE39-F1C432C9E457	9.0	https://vulners.com/githubexploit/9D9B3F4D-6B5C-5377-BE39-F1C432C9E457	*EXPLOIT*
    |     	8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	9.0	https://vulners.com/githubexploit/8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	*EXPLOIT*
    |     	7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2	9.0	https://vulners.com/githubexploit/7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2	*EXPLOIT*
    |     	36618CA8-9316-59CA-B748-82F15F407C4F	9.0	https://vulners.com/githubexploit/36618CA8-9316-59CA-B748-82F15F407C4F	*EXPLOIT*
    |     	D6E5CEC7-9ED8-5F96-A93E-768E2674DBCB	8.8	https://vulners.com/githubexploit/D6E5CEC7-9ED8-5F96-A93E-768E2674DBCB	*EXPLOIT*
    |     	CVE-2026-24072	8.8	https://vulners.com/cve/CVE-2026-24072
    |     	40379BCA-07F4-5401-B618-4640793D350D	8.8	https://vulners.com/githubexploit/40379BCA-07F4-5401-B618-4640793D350D	*EXPLOIT*
    |     	CVE-2025-58098	8.3	https://vulners.com/cve/CVE-2025-58098
    |     	HTTPD:A7133572D328CD65C350E33F20834FAD	8.2	https://vulners.com/httpd/HTTPD:A7133572D328CD65C350E33F20834FAD
    |     	CVE-2021-44224	8.2	https://vulners.com/cve/CVE-2021-44224
    |     	CNVD-2021-102387	8.2	https://vulners.com/cnvd/CNVD-2021-102387
    |     	B0A9E5E8-7CCC-5984-9922-A89F11D6BF38	8.2	https://vulners.com/githubexploit/B0A9E5E8-7CCC-5984-9922-A89F11D6BF38	*EXPLOIT*
    |     	CVE-2024-38473	8.1	https://vulners.com/cve/CVE-2024-38473
    |     	23079A70-8B37-56D2-9D37-F638EBF7F8B5	8.1	https://vulners.com/githubexploit/23079A70-8B37-56D2-9D37-F638EBF7F8B5	*EXPLOIT*
    |     	HTTPD:4CB68AD1C4AC4E8EE009A960A68B7E65	7.8	https://vulners.com/httpd/HTTPD:4CB68AD1C4AC4E8EE009A960A68B7E65
    |     	HTTPD:109158785130C454EF1D1CDDD4417560	7.8	https://vulners.com/httpd/HTTPD:109158785130C454EF1D1CDDD4417560
    |     	EDB-ID:46676	7.8	https://vulners.com/exploitdb/EDB-ID:46676	*EXPLOIT*
    |     	CVE-2019-9517	7.8	https://vulners.com/cve/CVE-2019-9517
    |     	CVE-2019-0211	7.8	https://vulners.com/cve/CVE-2019-0211
    |     	CNVD-2019-08946	7.8	https://vulners.com/cnvd/CNVD-2019-08946
    |     	88CDF499-CBE3-57E2-AB63-71E9CAA42B22	7.8	https://vulners.com/githubexploit/88CDF499-CBE3-57E2-AB63-71E9CAA42B22	*EXPLOIT*
    |     	706A08EF-16F2-59B5-B98E-EB8B83215AB1	7.8	https://vulners.com/gitee/706A08EF-16F2-59B5-B98E-EB8B83215AB1	*EXPLOIT*
    |     	HTTPD:F6C47B71D440F1A5B8EC9883D1516A33	7.5	https://vulners.com/httpd/HTTPD:F6C47B71D440F1A5B8EC9883D1516A33
    |     	HTTPD:F1CFBC9B54DFAD0499179863D36830BB	7.5	https://vulners.com/httpd/HTTPD:F1CFBC9B54DFAD0499179863D36830BB
    |     	HTTPD:D9B9375C40939357C5F47F1B3F64F0A1	7.5	https://vulners.com/httpd/HTTPD:D9B9375C40939357C5F47F1B3F64F0A1
    |     	HTTPD:CEEECD1BF3428B58C39137059390E4A1	7.5	https://vulners.com/httpd/HTTPD:CEEECD1BF3428B58C39137059390E4A1
    |     	HTTPD:C7D6319965E27EC08FB443D1FD67603B	7.5	https://vulners.com/httpd/HTTPD:C7D6319965E27EC08FB443D1FD67603B
    |     	HTTPD:C317C7138B4A8BBD54A901D6DDDCB837	7.5	https://vulners.com/httpd/HTTPD:C317C7138B4A8BBD54A901D6DDDCB837
    |     	HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F	7.5	https://vulners.com/httpd/HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F
    |     	HTTPD:B1B0A31C4AD388CC6C575931414173E2	7.5	https://vulners.com/httpd/HTTPD:B1B0A31C4AD388CC6C575931414173E2
    |     	HTTPD:975FD708E753E143E7DFFC23510F802E	7.5	https://vulners.com/httpd/HTTPD:975FD708E753E143E7DFFC23510F802E
    |     	HTTPD:8D3D8562E77EAD24FA6850949D025BC9	7.5	https://vulners.com/httpd/HTTPD:8D3D8562E77EAD24FA6850949D025BC9
    |     	HTTPD:720B7778CA309E929672897731D4493B	7.5	https://vulners.com/httpd/HTTPD:720B7778CA309E929672897731D4493B
    |     	HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5	7.5	https://vulners.com/httpd/HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5
    |     	HTTPD:05E6BF2AD317E3658D2938931207AA66	7.5	https://vulners.com/httpd/HTTPD:05E6BF2AD317E3658D2938931207AA66
    |     	CVE-2026-34059	7.5	https://vulners.com/cve/CVE-2026-34059
    |     	CVE-2026-29169	7.5	https://vulners.com/cve/CVE-2026-29169
    |     	CVE-2025-59775	7.5	https://vulners.com/cve/CVE-2025-59775
    |     	CVE-2025-55753	7.5	https://vulners.com/cve/CVE-2025-55753
    |     	CVE-2025-53020	7.5	https://vulners.com/cve/CVE-2025-53020
    |     	CVE-2025-49630	7.5	https://vulners.com/cve/CVE-2025-49630
    |     	CVE-2024-47252	7.5	https://vulners.com/cve/CVE-2024-47252
    |     	CVE-2024-43394	7.5	https://vulners.com/cve/CVE-2024-43394
    |     	CVE-2024-43204	7.5	https://vulners.com/cve/CVE-2024-43204
    |     	CVE-2024-42516	7.5	https://vulners.com/cve/CVE-2024-42516
    |     	CVE-2024-39573	7.5	https://vulners.com/cve/CVE-2024-39573
    |     	CVE-2024-38477	7.5	https://vulners.com/cve/CVE-2024-38477
    |     	CVE-2024-38472	7.5	https://vulners.com/cve/CVE-2024-38472
    |     	CVE-2024-27316	7.5	https://vulners.com/cve/CVE-2024-27316
    |     	CVE-2023-31122	7.5	https://vulners.com/cve/CVE-2023-31122
    |     	CVE-2023-27522	7.5	https://vulners.com/cve/CVE-2023-27522
    |     	CVE-2022-30556	7.5	https://vulners.com/cve/CVE-2022-30556
    |     	CVE-2022-29404	7.5	https://vulners.com/cve/CVE-2022-29404
    |     	CVE-2022-26377	7.5	https://vulners.com/cve/CVE-2022-26377
    |     	CVE-2022-22719	7.5	https://vulners.com/cve/CVE-2022-22719
    |     	CVE-2021-36160	7.5	https://vulners.com/cve/CVE-2021-36160
    |     	CVE-2021-34798	7.5	https://vulners.com/cve/CVE-2021-34798
    |     	CVE-2021-33193	7.5	https://vulners.com/cve/CVE-2021-33193
    |     	CVE-2021-26690	7.5	https://vulners.com/cve/CVE-2021-26690
    |     	CVE-2020-9490	7.5	https://vulners.com/cve/CVE-2020-9490
    |     	CVE-2020-11993	7.5	https://vulners.com/cve/CVE-2020-11993
    |     	CVE-2019-10081	7.5	https://vulners.com/cve/CVE-2019-10081
    |     	CVE-2019-0217	7.5	https://vulners.com/cve/CVE-2019-0217
    |     	CVE-2019-0215	7.5	https://vulners.com/cve/CVE-2019-0215
    |     	CVE-2006-20001	7.5	https://vulners.com/cve/CVE-2006-20001
    |     	CNVD-2025-30837	7.5	https://vulners.com/cnvd/CNVD-2025-30837
    |     	CNVD-2025-30836	7.5	https://vulners.com/cnvd/CNVD-2025-30836
    |     	CNVD-2025-16614	7.5	https://vulners.com/cnvd/CNVD-2025-16614
    |     	CNVD-2025-16613	7.5	https://vulners.com/cnvd/CNVD-2025-16613
    |     	CNVD-2025-16612	7.5	https://vulners.com/cnvd/CNVD-2025-16612
    |     	CNVD-2025-16609	7.5	https://vulners.com/cnvd/CNVD-2025-16609
    |     	CNVD-2025-16608	7.5	https://vulners.com/cnvd/CNVD-2025-16608
    |     	CNVD-2025-16603	7.5	https://vulners.com/cnvd/CNVD-2025-16603
    |     	CNVD-2024-36393	7.5	https://vulners.com/cnvd/CNVD-2024-36393
    |     	CNVD-2024-36390	7.5	https://vulners.com/cnvd/CNVD-2024-36390
    |     	CNVD-2024-36389	7.5	https://vulners.com/cnvd/CNVD-2024-36389
    |     	CNVD-2024-20839	7.5	https://vulners.com/cnvd/CNVD-2024-20839
    |     	CNVD-2023-93320	7.5	https://vulners.com/cnvd/CNVD-2023-93320
    |     	CNVD-2023-80558	7.5	https://vulners.com/cnvd/CNVD-2023-80558
    |     	CNVD-2022-53584	7.5	https://vulners.com/cnvd/CNVD-2022-53584
    |     	CNVD-2022-51058	7.5	https://vulners.com/cnvd/CNVD-2022-51058
    |     	CNVD-2022-41639	7.5	https://vulners.com/cnvd/CNVD-2022-41639
    |     	CNVD-2022-13199	7.5	https://vulners.com/cnvd/CNVD-2022-13199
    |     	CNVD-2022-03223	7.5	https://vulners.com/cnvd/CNVD-2022-03223
    |     	CNVD-2022-03205	7.5	https://vulners.com/cnvd/CNVD-2022-03205
    |     	CNVD-2020-46281	7.5	https://vulners.com/cnvd/CNVD-2020-46281
    |     	CNVD-2020-46279	7.5	https://vulners.com/cnvd/CNVD-2020-46279
    |     	CNVD-2019-08945	7.5	https://vulners.com/cnvd/CNVD-2019-08945
    |     	CDC791CD-A414-5ABE-A897-7CFA3C2D3D29	7.5	https://vulners.com/githubexploit/CDC791CD-A414-5ABE-A897-7CFA3C2D3D29	*EXPLOIT*
    |     	A0F268C8-7319-5637-82F7-8DAF72D14629	7.5	https://vulners.com/githubexploit/A0F268C8-7319-5637-82F7-8DAF72D14629	*EXPLOIT*
    |     	45D138AD-BEC6-552A-91EA-8816914CA7F4	7.5	https://vulners.com/githubexploit/45D138AD-BEC6-552A-91EA-8816914CA7F4	*EXPLOIT*
    |     	1337DAY-ID-35422	7.5	https://vulners.com/zdt/1337DAY-ID-35422	*EXPLOIT*
    |     	0E08753E-C6D7-5E76-A61F-6CA6F7F87AA8	7.5	https://vulners.com/githubexploit/0E08753E-C6D7-5E76-A61F-6CA6F7F87AA8	*EXPLOIT*
    |     	CVE-2025-49812	7.4	https://vulners.com/cve/CVE-2025-49812
    |     	HTTPD:D66D5F45690EBE82B48CC81EF6388EE8	7.3	https://vulners.com/httpd/HTTPD:D66D5F45690EBE82B48CC81EF6388EE8
    |     	CVE-2026-29168	7.3	https://vulners.com/cve/CVE-2026-29168
    |     	CVE-2023-38709	7.3	https://vulners.com/cve/CVE-2023-38709
    |     	CVE-2020-35452	7.3	https://vulners.com/cve/CVE-2020-35452
    |     	CNVD-2024-36395	7.3	https://vulners.com/cnvd/CNVD-2024-36395
    |     	HTTPD:1476868F8E61526B31CAA5707DE2E715	7.2	https://vulners.com/httpd/HTTPD:1476868F8E61526B31CAA5707DE2E715
    |     	EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	7.2	https://vulners.com/exploitpack/EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB	*EXPLOIT*
    |     	CVE-2019-10097	7.2	https://vulners.com/cve/CVE-2019-10097
    |     	1337DAY-ID-32502	7.2	https://vulners.com/zdt/1337DAY-ID-32502	*EXPLOIT*
    |     	CVE-2026-33523	6.5	https://vulners.com/cve/CVE-2026-33523
    |     	CVE-2025-65082	6.5	https://vulners.com/cve/CVE-2025-65082
    |     	CNVD-2025-30833	6.5	https://vulners.com/cnvd/CNVD-2025-30833
    |     	CVE-2024-24795	6.3	https://vulners.com/cve/CVE-2024-24795
    |     	CNVD-2024-36394	6.3	https://vulners.com/cnvd/CNVD-2024-36394
    |     	HTTPD:E3E8BE7E36621C4506552BA051ECC3C8	6.1	https://vulners.com/httpd/HTTPD:E3E8BE7E36621C4506552BA051ECC3C8
    |     	HTTPD:8DF9389A321028B4475CE2E9B5BFC7A6	6.1	https://vulners.com/httpd/HTTPD:8DF9389A321028B4475CE2E9B5BFC7A6
    |     	HTTPD:5FF2D6B51D8115FFCB653949D8D36345	6.1	https://vulners.com/httpd/HTTPD:5FF2D6B51D8115FFCB653949D8D36345
    |     	CVE-2020-1927	6.1	https://vulners.com/cve/CVE-2020-1927
    |     	CVE-2019-10098	6.1	https://vulners.com/cve/CVE-2019-10098
    |     	CVE-2019-10092	6.1	https://vulners.com/cve/CVE-2019-10092
    |     	CNVD-2020-21904	6.1	https://vulners.com/cnvd/CNVD-2020-21904
    |     	CAB023BA-58A3-5C35-BF97-F9C43133DB5E	6.1	https://vulners.com/gitee/CAB023BA-58A3-5C35-BF97-F9C43133DB5E	*EXPLOIT*
    |     	4013EC74-B3C1-5D95-938A-54197A58586D	6.1	https://vulners.com/githubexploit/4013EC74-B3C1-5D95-938A-54197A58586D	*EXPLOIT*
    |     	CVE-2023-45802	5.9	https://vulners.com/cve/CVE-2023-45802
    |     	556687CB-7B66-53C5-A79C-84B0ED753C7E	5.9	https://vulners.com/githubexploit/556687CB-7B66-53C5-A79C-84B0ED753C7E	*EXPLOIT*
    |     	1337DAY-ID-33577	5.8	https://vulners.com/zdt/1337DAY-ID-33577	*EXPLOIT*
    |     	HTTPD:B900BFA5C32A54AB9D565F59C8AC1D05	5.5	https://vulners.com/httpd/HTTPD:B900BFA5C32A54AB9D565F59C8AC1D05
    |     	CVE-2020-13938	5.5	https://vulners.com/cve/CVE-2020-13938
    |     	CNVD-2021-44765	5.5	https://vulners.com/cnvd/CNVD-2021-44765
    |     	CVE-2025-66200	5.4	https://vulners.com/cve/CVE-2025-66200
    |     	CNVD-2025-30835	5.4	https://vulners.com/cnvd/CNVD-2025-30835
    |     	HTTPD:FCCF5DB14D66FA54B47C34D9680C0335	5.3	https://vulners.com/httpd/HTTPD:FCCF5DB14D66FA54B47C34D9680C0335
    |     	HTTPD:EB26BC6B6E566C865F53A311FC1A6744	5.3	https://vulners.com/httpd/HTTPD:EB26BC6B6E566C865F53A311FC1A6744
    |     	HTTPD:BAAB4065D254D64A717E8A5C847C7BCA	5.3	https://vulners.com/httpd/HTTPD:BAAB4065D254D64A717E8A5C847C7BCA
    |     	HTTPD:AA09285A8811F9F8A1F82F45122331AD	5.3	https://vulners.com/httpd/HTTPD:AA09285A8811F9F8A1F82F45122331AD
    |     	HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F	5.3	https://vulners.com/httpd/HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F
    |     	HTTPD:5C8B0394DE17D1C29719B16CE00F475D	5.3	https://vulners.com/httpd/HTTPD:5C8B0394DE17D1C29719B16CE00F475D
    |     	CVE-2026-34032	5.3	https://vulners.com/cve/CVE-2026-34032
    |     	CVE-2026-33857	5.3	https://vulners.com/cve/CVE-2026-33857
    |     	CVE-2026-33007	5.3	https://vulners.com/cve/CVE-2026-33007
    |     	CVE-2022-37436	5.3	https://vulners.com/cve/CVE-2022-37436
    |     	CVE-2022-28614	5.3	https://vulners.com/cve/CVE-2022-28614
    |     	CVE-2022-28330	5.3	https://vulners.com/cve/CVE-2022-28330
    |     	CVE-2020-1934	5.3	https://vulners.com/cve/CVE-2020-1934
    |     	CVE-2019-17567	5.3	https://vulners.com/cve/CVE-2019-17567
    |     	CVE-2019-0220	5.3	https://vulners.com/cve/CVE-2019-0220
    |     	CVE-2019-0196	5.3	https://vulners.com/cve/CVE-2019-0196
    |     	CNVD-2023-30859	5.3	https://vulners.com/cnvd/CNVD-2023-30859
    |     	CNVD-2022-53582	5.3	https://vulners.com/cnvd/CNVD-2022-53582
    |     	CNVD-2022-51059	5.3	https://vulners.com/cnvd/CNVD-2022-51059
    |     	CNVD-2021-44766	5.3	https://vulners.com/cnvd/CNVD-2021-44766
    |     	CNVD-2020-46278	5.3	https://vulners.com/cnvd/CNVD-2020-46278
    |     	CNVD-2020-29872	5.3	https://vulners.com/cnvd/CNVD-2020-29872
    |     	CNVD-2019-08941	5.3	https://vulners.com/cnvd/CNVD-2019-08941
    |     	HTTPD:2F7A93926BF5E6C2E4D1EFB6F2BEEE01	4.9	https://vulners.com/httpd/HTTPD:2F7A93926BF5E6C2E4D1EFB6F2BEEE01
    |     	CVE-2019-0197	4.9	https://vulners.com/cve/CVE-2019-0197
    |     	EA6ADD14-D80B-5DC2-9991-1F9663E2D09F	4.8	https://vulners.com/githubexploit/EA6ADD14-D80B-5DC2-9991-1F9663E2D09F	*EXPLOIT*
    |     	CVE-2026-33006	4.8	https://vulners.com/cve/CVE-2026-33006
    |     	1337DAY-ID-33575	4.3	https://vulners.com/zdt/1337DAY-ID-33575	*EXPLOIT*
    |_    	PACKETSTORM:152441	0.0	https://vulners.com/packetstorm/PACKETSTORM:152441	*EXPLOIT*
    |_http-server-header: Apache/2.4.38 (Debian)
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    | http-enum: 
    |   /robots.txt: Robots file
    |_  /secret/: Potentially interesting folder

# 192.168.56.102 - Ubuntu - "Pwn the Tron"

    Nmap scan report for 192.168.56.102
    Host is up (0.0023s latency).
    Not shown: 997 closed tcp ports (reset), 1 filtered tcp port (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE    VERSION
    22/tcp open  tcpwrapped
    | ssh-hostkey: 
    |   2048 93:74:34:72:3e:7c:56:0a:f5:d5:a1:4d:6c:94:31:2f (RSA)
    |   256 1f:49:9e:8b:0a:4f:01:cc:e5:a9:2c:28:5a:2c:c1:9e (ECDSA)
    |_  256 05:9f:7a:f1:7b:f7:1f:04:ea:14:d4:5f:f0:0a:8f:54 (ED25519)
    80/tcp open  tcpwrapped
    |_http-title: Revive Cybertron
    |_http-server-header: Apache
    Device type: switch
    Running (JUST GUESSING): Cisco embedded (86%)
    OS CPE: cpe:/h:cisco:css_11501
    Aggressive OS guesses: Cisco CSS 11501 switch (86%)
    No exact OS matches for host (test conditions non-ideal).

# 192.168.56.103 - Ubuntu - "Napping"

    Nmap scan report for 192.168.56.103
    Host is up (0.0021s latency).
    Not shown: 996 closed tcp ports (reset), 2 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE    VERSION
    22/tcp open  tcpwrapped
    | ssh-hostkey: 
    |   3072 24:c4:fc:dc:4b:f4:31:a0:ad:0d:20:61:fd:ca:ab:79 (RSA)
    |   256 6f:31:b3:e7:7b:aa:22:a2:a7:80:ef:6d:d2:87:6c:be (ECDSA)
    |_  256 af:01:85:cf:dd:43:e9:8d:32:50:83:b2:41:ec:1d:3b (ED25519)
    80/tcp open  tcpwrapped
    | http-cookie-flags: 
    |   /: 
    |     PHPSESSID: 
    |_      httponly flag not set
    |_http-title: Login
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    Device type: switch
    Running (JUST GUESSING): Cisco embedded (86%)
    OS CPE: cpe:/h:cisco:css_11501
    Aggressive OS guesses: Cisco CSS 11501 switch (86%)
    No exact OS matches for host (test conditions non-ideal).

# 192.168.56.104 - Ubuntu - "Zico's Shop"

    Nmap scan report for 192.168.56.104
    Host is up (0.0021s latency).
    Not shown: 996 closed tcp ports (reset), 1 filtered tcp port (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT    STATE SERVICE    VERSION
    22/tcp  open  tcpwrapped
    | ssh-hostkey: 
    |   1024 68:60:de:c2:2b:c6:16:d8:5b:88:be:e3:cc:a1:25:75 (DSA)
    |   2048 50:db:75:ba:11:2f:43:c9:ab:14:40:6d:7f:a1:ee:e3 (RSA)
    |_  256 11:5d:55:29:8a:77:d8:08:b4:00:9b:a3:61:93:fe:e5 (ECDSA)
    80/tcp  open  tcpwrapped
    |_http-server-header: Apache/2.2.22 (Ubuntu)
    |_http-title: Zico's Shop
    111/tcp open  tcpwrapped
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100024  1          33490/tcp   status
    |   100024  1          38581/tcp6  status
    |   100024  1          39577/udp   status
    |_  100024  1          53533/udp6  status
    Device type: switch|VoIP phone|general purpose
    Running (JUST GUESSING): Cisco embedded (87%), Aastra embedded (86%), Avaya embedded (85%), FreeBSD 4.X (85%)
    OS CPE: cpe:/h:cisco:css_11501 cpe:/h:aastra:57i cpe:/o:freebsd:freebsd:4.7
    Aggressive OS guesses: Cisco CSS 11501 switch (87%), Aastra 57i VoIP phone (86%), Avaya P130 workgroup switch (85%), FreeBSD 4.7-STABLE (85%)
    No exact OS matches for host (test conditions non-ideal).


# 192.168.56.105 - Debian - "symfonos4"
    
    Nmap scan report for 192.168.56.105
    Host is up (0.014s latency).
    Not shown: 998 closed tcp ports (reset)
    PORT   STATE SERVICE    VERSION
    22/tcp open  tcpwrapped
    | ssh-hostkey: 
    |   2048 f9:c1:73:95:a4:17:df:f6:ed:5c:8e:8a:c8:05:f9:8f (RSA)
    |   256 be:c1:fd:f1:33:64:39:9a:68:35:64:f9:bd:27:ec:01 (ECDSA)
    |_  256 66:f7:6a:e8:ed:d5:1d:2d:36:32:64:39:38:4f:9c:8a (ED25519)
    80/tcp open  tcpwrapped
    |_http-server-header: Apache/2.4.38 (Debian)
    |_http-title: Site doesn't have a title (text/html).
    Device type: switch|VoIP phone|general purpose
    Running (JUST GUESSING): Cisco embedded (87%), Aastra embedded (86%), Avaya embedded (85%), FreeBSD 4.X (85%)
    OS CPE: cpe:/h:cisco:css_11501 cpe:/h:aastra:57i cpe:/o:freebsd:freebsd:4.7
    Aggressive OS guesses: Cisco CSS 11501 switch (87%), Aastra 57i VoIP phone (86%), Avaya P130 workgroup switch (85%), FreeBSD 4.7-STABLE (85%)
    No exact OS matches for host (test conditions non-ideal). 

# 192.168.56.106 - Ubuntu - "Web Server:Bootcamp"

    Nmap scan report for 192.168.56.106
    Host is up (0.0041s latency).
    Not shown: 64536 closed tcp ports (reset), 988 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE     VERSION
    21/tcp   open  ftp         vsftpd 2.3.4
    | vulners:
    |   vsftpd 2.3.4:
    |      PACKETSTORM:162145 10.0 <https://vulners.com/packetstorm/PACKETSTORM:162145> *EXPLOIT*
    |      EDB-ID:49757 10.0 <https://vulners.com/exploitdb/EDB-ID:49757> *EXPLOIT*
    |      E9B0AEBB-5138-50BF-8922-2D87E3C046DD 10.0 <https://vulners.com/githubexploit/E9B0AEBB-5138-50BF-8922-2D87E3C046DD> *EXPLOIT*
    |      E356CCEC-7C81-5A77-8CE4-87DF4DB21897 10.0 <https://vulners.com/githubexploit/E356CCEC-7C81-5A77-8CE4-87DF4DB21897> *EXPLOIT*
    |      D0DBA05F-750F-5F9B-9C69-65E8FA6977D5 10.0 <https://vulners.com/githubexploit/D0DBA05F-750F-5F9B-9C69-65E8FA6977D5> *EXPLOIT*
    |      CVE-2011-2523 10.0 <https://vulners.com/cve/CVE-2011-2523>
    |      CNVD-2020-46837 10.0 <https://vulners.com/cnvd/CNVD-2020-46837>
    |      CC3F6C15-182F-53F6-A5CC-812D37F1F047 10.0 <https://vulners.com/githubexploit/CC3F6C15-182F-53F6-A5CC-812D37F1F047> *EXPLOIT*
    |      BEE67BEA-45C2-50C0-88F3-9A2E7CC2DECE 10.0 <https://vulners.com/githubexploit/BEE67BEA-45C2-50C0-88F3-9A2E7CC2DECE> *EXPLOIT*
    |      A41B5EAD-1A4C-56A6-97C6-1C58A1CF1E3B 10.0 <https://vulners.com/githubexploit/A41B5EAD-1A4C-56A6-97C6-1C58A1CF1E3B> *EXPLOIT*
    |      9B4BA341-1CBF-59D6-AA40-33596997F23B 10.0 <https://vulners.com/githubexploit/9B4BA341-1CBF-59D6-AA40-33596997F23B> *EXPLOIT*
    |      817CD8FE-87C4-5FE8-B9B2-8CC64333A3F3 10.0 <https://vulners.com/githubexploit/817CD8FE-87C4-5FE8-B9B2-8CC64333A3F3> *EXPLOIT*
    |      63A5C9A7-C241-5E83-9EE6-ABAB44BDD270 10.0 <https://vulners.com/githubexploit/63A5C9A7-C241-5E83-9EE6-ABAB44BDD270> *EXPLOIT*
    |      5F4BCEDE-77DF-5D54-851A-0AE8B76458D9 10.0 <https://vulners.com/githubexploit/5F4BCEDE-77DF-5D54-851A-0AE8B76458D9> *EXPLOIT*
    |      59BAFDCD-5027-5C82-BC59-FC7625DD81DB 10.0 <https://vulners.com/githubexploit/59BAFDCD-5027-5C82-BC59-FC7625DD81DB> *EXPLOIT*
    |      50580586-73C4-5097-81CA-546D6591DF44 10.0 <https://vulners.com/githubexploit/50580586-73C4-5097-81CA-546D6591DF44> *EXPLOIT*
    |      4D01A3A1-75C7-5730-8C5D-B2EC1F56532F 10.0 <https://vulners.com/githubexploit/4D01A3A1-75C7-5730-8C5D-B2EC1F56532F> *EXPLOIT*
    |      344AF37C-35F5-5A70-83E4-B89507233DC0 10.0 <https://vulners.com/githubexploit/344AF37C-35F5-5A70-83E4-B89507233DC0> *EXPLOIT*
    |      322DD1ED-D331-573E-9AAC-5B6BEC2095F9 10.0 <https://vulners.com/githubexploit/322DD1ED-D331-573E-9AAC-5B6BEC2095F9> *EXPLOIT*
    |      23DBF7D8-DD32-5D15-8D18-0CF069745409 10.0 <https://vulners.com/githubexploit/23DBF7D8-DD32-5D15-8D18-0CF069745409> *EXPLOIT*
    |      09B89183-FE26-5690-A12C-7BEC34B1AAE4 10.0 <https://vulners.com/githubexploit/09B89183-FE26-5690-A12C-7BEC34B1AAE4> *EXPLOIT*
    |_     1337DAY-ID-36095 9.8 <https://vulners.com/zdt/1337DAY-ID-36095> *EXPLOIT*
    | ftp-vsftpd-backdoor:
    |   VULNERABLE:
    |   vsFTPd version 2.3.4 backdoor
    |     State: VULNERABLE (Exploitable)
    |     IDs:  CVE:CVE-2011-2523  BID:48539
    |       vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
    |     Disclosure date: 2011-07-03
    |     Exploit results:
    |       Shell command: id
    |       Results: uid=0(root) gid=0(root)
    |     References:
    |       <https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb>
    |       <http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html>
    |       <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2523>
    |_      <https://www.securityfocus.com/bid/48539>
    22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
    | vulners:
    |   cpe:/a:openbsd:openssh:4.7p1:
    |      DF059135-2CF5-5441-8F22-E6EF1DEE5F6E 10.0 <https://vulners.com/gitee/DF059135-2CF5-5441-8F22-E6EF1DEE5F6E> *EXPLOIT*
    |      PACKETSTORM:173661 9.8 <https://vulners.com/packetstorm/PACKETSTORM:173661> *EXPLOIT*
    |      F0979183-AE88-53B4-86CF-3AF0523F3807 9.8 <https://vulners.com/githubexploit/F0979183-AE88-53B4-86CF-3AF0523F3807> *EXPLOIT*
    |      CVE-2023-38408 9.8 <https://vulners.com/cve/CVE-2023-38408>
    |      CVE-2016-1908 9.8 <https://vulners.com/cve/CVE-2016-1908>
    |      CVE-2010-4478 9.8 <https://vulners.com/cve/CVE-2010-4478>
    |      CEF8EC43-BFE2-5B5E-8918-54A90DA092B4 9.8 <https://vulners.com/githubexploit/CEF8EC43-BFE2-5B5E-8918-54A90DA092B4> *EXPLOIT*
    |      B8190CDB-3EB9-5631-9828-8064A1575B23 9.8 <https://vulners.com/githubexploit/B8190CDB-3EB9-5631-9828-8064A1575B23> *EXPLOIT*
    |      A2B36B85-C737-548F-8C04-9339EDCDBFF5 9.8 <https://vulners.com/githubexploit/A2B36B85-C737-548F-8C04-9339EDCDBFF5> *EXPLOIT*
    |      8FC9C5AB-3968-5F3C-825E-E8DB5379A623 9.8 <https://vulners.com/githubexploit/8FC9C5AB-3968-5F3C-825E-E8DB5379A623> *EXPLOIT*
    |      8AD01159-548E-546E-AA87-2DE89F3927EC 9.8 <https://vulners.com/githubexploit/8AD01159-548E-546E-AA87-2DE89F3927EC> *EXPLOIT*
    |      6192C35D-F78B-5C0A-AB8D-9826A79A5320 9.8 <https://vulners.com/githubexploit/6192C35D-F78B-5C0A-AB8D-9826A79A5320> *EXPLOIT*
    |      2227729D-6700-5C8F-8930-1EEAFD4B9FF0 9.8 <https://vulners.com/githubexploit/2227729D-6700-5C8F-8930-1EEAFD4B9FF0> *EXPLOIT*
    |      0221525F-07F5-5790-912D-F4B9E2D1B587 9.8 <https://vulners.com/githubexploit/0221525F-07F5-5790-912D-F4B9E2D1B587> *EXPLOIT*
    |      CVE-2015-5600 8.5 <https://vulners.com/cve/CVE-2015-5600>
    |      CVE-2026-35414 8.1 <https://vulners.com/cve/CVE-2026-35414>
    |      CVE-2026-35386 8.1 <https://vulners.com/cve/CVE-2026-35386>
    |      CVE-2026-35385 8.1 <https://vulners.com/cve/CVE-2026-35385>
    |      BA3887BD-F579-53B1-A4A4-FF49E953E1C0 8.1 <https://vulners.com/githubexploit/BA3887BD-F579-53B1-A4A4-FF49E953E1C0> *EXPLOIT*
    |      4FB01B00-F993-5CAF-BD57-D7E290D10C1F 8.1 <https://vulners.com/githubexploit/4FB01B00-F993-5CAF-BD57-D7E290D10C1F> *EXPLOIT*
    |      PACKETSTORM:140070 7.8 <https://vulners.com/packetstorm/PACKETSTORM:140070> *EXPLOIT*
    |      PACKETSTORM:101052 7.8 <https://vulners.com/packetstorm/PACKETSTORM:101052> *EXPLOIT*
    |      EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09 7.8 <https://vulners.com/exploitpack/EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09> *EXPLOIT*
    |      EDB-ID:40888 7.8 <https://vulners.com/exploitdb/EDB-ID:40888> *EXPLOIT*
    |      CVE-2020-15778 7.8 <https://vulners.com/cve/CVE-2020-15778>
    |      CVE-2016-6515 7.8 <https://vulners.com/cve/CVE-2016-6515>
    |      CVE-2016-10012 7.8 <https://vulners.com/cve/CVE-2016-10012>
    |      CVE-2015-8325 7.8 <https://vulners.com/cve/CVE-2015-8325>
    |      C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3 7.8 <https://vulners.com/githubexploit/C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3> *EXPLOIT*
    |      C892A90E-C1D1-5A54-BFAA-046266448553 7.8 <https://vulners.com/githubexploit/C892A90E-C1D1-5A54-BFAA-046266448553> *EXPLOIT*
    |      99C4CA40-30C8-5A34-B3A3-4B5E7A9E16BA 7.8 <https://vulners.com/githubexploit/99C4CA40-30C8-5A34-B3A3-4B5E7A9E16BA> *EXPLOIT*
    |      991D2CC4-0E09-5745-97A2-4917461BD6EC 7.8 <https://vulners.com/githubexploit/991D2CC4-0E09-5745-97A2-4917461BD6EC> *EXPLOIT*
    |      4F1BA9CA-CAB4-55F4-A857-3E4C94C93483 7.8 <https://vulners.com/githubexploit/4F1BA9CA-CAB4-55F4-A857-3E4C94C93483> *EXPLOIT*
    |      312165E3-7FD9-5769-BDA3-4129BE9114D6 7.8 <https://vulners.com/githubexploit/312165E3-7FD9-5769-BDA3-4129BE9114D6> *EXPLOIT*
    |      2E719186-2FED-58A8-A150-762EFBAAA523 7.8 <https://vulners.com/gitee/2E719186-2FED-58A8-A150-762EFBAAA523> *EXPLOIT*
    |      23CC97BE-7C95-513B-9E73-298C48D74432 7.8 <https://vulners.com/githubexploit/23CC97BE-7C95-513B-9E73-298C48D74432> *EXPLOIT*
    |      1337DAY-ID-26494 7.8 <https://vulners.com/zdt/1337DAY-ID-26494> *EXPLOIT*
    |      10213DBE-F683-58BB-B6D3-353173626207 7.8 <https://vulners.com/githubexploit/10213DBE-F683-58BB-B6D3-353173626207> *EXPLOIT*
    |      SSV:92579 7.5 <https://vulners.com/seebug/SSV:92579> *EXPLOIT*
    |      SSV:61450 7.5 <https://vulners.com/seebug/SSV:61450> *EXPLOIT*
    |      CVE-2016-10708 7.5 <https://vulners.com/cve/CVE-2016-10708>
    |      CVE-2016-10009 7.5 <https://vulners.com/cve/CVE-2016-10009>
    |      CVE-2014-1692 7.5 <https://vulners.com/cve/CVE-2014-1692>
    |      CVE-2010-5107 7.5 <https://vulners.com/cve/CVE-2010-5107>
    |      CF52FA19-B5DB-5D14-B50F-2411851976E2 7.5 <https://vulners.com/githubexploit/CF52FA19-B5DB-5D14-B50F-2411851976E2> *EXPLOIT*
    |      1337DAY-ID-26576 7.5 <https://vulners.com/zdt/1337DAY-ID-26576> *EXPLOIT*
    |      SSV:92582 7.2 <https://vulners.com/seebug/SSV:92582> *EXPLOIT*
    |      CVE-2016-10010 7.0 <https://vulners.com/cve/CVE-2016-10010>
    |      CVE-2015-6564 7.0 <https://vulners.com/cve/CVE-2015-6564>
    |      SSV:92580 6.9 <https://vulners.com/seebug/SSV:92580> *EXPLOIT*
    |      1337DAY-ID-26577 6.9 <https://vulners.com/zdt/1337DAY-ID-26577> *EXPLOIT*
    |      EDB-ID:46516 6.8 <https://vulners.com/exploitdb/EDB-ID:46516> *EXPLOIT*
    |      EDB-ID:46193 6.8 <https://vulners.com/exploitdb/EDB-ID:46193> *EXPLOIT*
    |      CVE-2019-6110 6.8 <https://vulners.com/cve/CVE-2019-6110>
    |      CVE-2019-6109 6.8 <https://vulners.com/cve/CVE-2019-6109>
    |      1337DAY-ID-32328 6.8 <https://vulners.com/zdt/1337DAY-ID-32328> *EXPLOIT*
    |      1337DAY-ID-32009 6.8 <https://vulners.com/zdt/1337DAY-ID-32009> *EXPLOIT*
    |      D104D2BF-ED22-588B-A9B2-3CCC562FE8C0 6.5 <https://vulners.com/githubexploit/D104D2BF-ED22-588B-A9B2-3CCC562FE8C0> *EXPLOIT*
    |      CVE-2026-35387 6.5 <https://vulners.com/cve/CVE-2026-35387>
    |      CVE-2023-51385 6.5 <https://vulners.com/cve/CVE-2023-51385>
    |      CVE-2014-2653 6.5 <https://vulners.com/cve/CVE-2014-2653>
    |      CVE-2012-0814 6.5 <https://vulners.com/cve/CVE-2012-0814>
    |      CVE-2008-1657 6.5 <https://vulners.com/cve/CVE-2008-1657>
    |      C07ADB46-24B8-57B7-B375-9C761F4750A2 6.5 <https://vulners.com/githubexploit/C07ADB46-24B8-57B7-B375-9C761F4750A2> *EXPLOIT*
    |      A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C 6.5 <https://vulners.com/githubexploit/A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C> *EXPLOIT*
    |      65B15AA1-2A8D-53C1-9499-69EBA3619F1C 6.5 <https://vulners.com/githubexploit/65B15AA1-2A8D-53C1-9499-69EBA3619F1C> *EXPLOIT*
    |      5325A9D6-132B-590C-BDEF-0CB105252732 6.5 <https://vulners.com/gitee/5325A9D6-132B-590C-BDEF-0CB105252732> *EXPLOIT*
    |      530326CF-6AB3-5643-AA16-73DC8CB44742 6.5 <https://vulners.com/githubexploit/530326CF-6AB3-5643-AA16-73DC8CB44742> *EXPLOIT*
    |      EDB-ID:40858 6.4 <https://vulners.com/exploitdb/EDB-ID:40858> *EXPLOIT*
    |      EDB-ID:40119 6.4 <https://vulners.com/exploitdb/EDB-ID:40119> *EXPLOIT*
    |      EDB-ID:39569 6.4 <https://vulners.com/exploitdb/EDB-ID:39569> *EXPLOIT*
    |      CVE-2016-3115 6.4 <https://vulners.com/cve/CVE-2016-3115>
    |      CVE-2015-6563 6.4 <https://vulners.com/cve/CVE-2015-6563>
    |      CVE-2016-10011 6.2 <https://vulners.com/cve/CVE-2016-10011>
    |      PACKETSTORM:181223 5.9 <https://vulners.com/packetstorm/PACKETSTORM:181223> *EXPLOIT*
    |      MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS- 5.9 <https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS-> *EXPLOIT*
    |      FEF0EB06-770B-5ADF-857C-1704B7AC3FE4 5.9 <https://vulners.com/githubexploit/FEF0EB06-770B-5ADF-857C-1704B7AC3FE4> *EXPLOIT*
    |      FD2E0EBA-ED84-5304-8862-84BCDEB2F288 5.9 <https://vulners.com/githubexploit/FD2E0EBA-ED84-5304-8862-84BCDEB2F288> *EXPLOIT*
    |      EDB-ID:45939 5.9 <https://vulners.com/exploitdb/EDB-ID:45939> *EXPLOIT*
    |      EDB-ID:45233 5.9 <https://vulners.com/exploitdb/EDB-ID:45233> *EXPLOIT*
    |      EDB-ID:40136 5.9 <https://vulners.com/exploitdb/EDB-ID:40136> *EXPLOIT*
    |      EDB-ID:40113 5.9 <https://vulners.com/exploitdb/EDB-ID:40113> *EXPLOIT*
    |      CVE-2023-48795 5.9 <https://vulners.com/cve/CVE-2023-48795>
    |      CVE-2019-6111 5.9 <https://vulners.com/cve/CVE-2019-6111>
    |      CVE-2018-15473 5.9 <https://vulners.com/cve/CVE-2018-15473>
    |      CVE-2016-6210 5.9 <https://vulners.com/cve/CVE-2016-6210>
    |      A4C45A40-ADC5-50EF-8FFC-4047AA0F987B 5.9 <https://vulners.com/githubexploit/A4C45A40-ADC5-50EF-8FFC-4047AA0F987B> *EXPLOIT*
    |      A02ABE85-E4E3-5852-A59D-DF288CB8160A 5.9 <https://vulners.com/githubexploit/A02ABE85-E4E3-5852-A59D-DF288CB8160A> *EXPLOIT*
    |      721F040C-37BC-59E1-9433-01A2EAC2E755 5.9 <https://vulners.com/githubexploit/721F040C-37BC-59E1-9433-01A2EAC2E755> *EXPLOIT*
    |      SSV:61911 5.8 <https://vulners.com/seebug/SSV:61911> *EXPLOIT*
    |      EXPLOITPACK:98FE96309F9524B8C84C508837551A19 5.8 <https://vulners.com/exploitpack/EXPLOITPACK:98FE96309F9524B8C84C508837551A19> *EXPLOIT*
    |      EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97 5.8 <https://vulners.com/exploitpack/EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97> *EXPLOIT*
    |      CVE-2014-2532 5.8 <https://vulners.com/cve/CVE-2014-2532>
    |      SSV:91041 5.5 <https://vulners.com/seebug/SSV:91041> *EXPLOIT*
    |      PACKETSTORM:140019 5.5 <https://vulners.com/packetstorm/PACKETSTORM:140019> *EXPLOIT*
    |      PACKETSTORM:136251 5.5 <https://vulners.com/packetstorm/PACKETSTORM:136251> *EXPLOIT*
    |      PACKETSTORM:136234 5.5 <https://vulners.com/packetstorm/PACKETSTORM:136234> *EXPLOIT*
    |      EXPLOITPACK:F92411A645D85F05BDBD274FD222226F 5.5 <https://vulners.com/exploitpack/EXPLOITPACK:F92411A645D85F05BDBD274FD222226F> *EXPLOIT*
    |      EXPLOITPACK:9F2E746846C3C623A27A441281EAD138 5.5 <https://vulners.com/exploitpack/EXPLOITPACK:9F2E746846C3C623A27A441281EAD138> *EXPLOIT*
    |      EXPLOITPACK:1902C998CBF9154396911926B4C3B330 5.5 <https://vulners.com/exploitpack/EXPLOITPACK:1902C998CBF9154396911926B4C3B330> *EXPLOIT*
    |      CVE-2011-4327 5.5 <https://vulners.com/cve/CVE-2011-4327>
    |      1337DAY-ID-25388 5.5 <https://vulners.com/zdt/1337DAY-ID-25388> *EXPLOIT*
    |      FD18B68B-C0A6-562E-A8C8-781B225F15B0 5.3 <https://vulners.com/githubexploit/FD18B68B-C0A6-562E-A8C8-781B225F15B0> *EXPLOIT*
    |      E9EC0911-E2E1-52A7-B2F4-D0065C6A3057 5.3 <https://vulners.com/githubexploit/E9EC0911-E2E1-52A7-B2F4-D0065C6A3057> *EXPLOIT*
    |      CVE-2018-20685 5.3 <https://vulners.com/cve/CVE-2018-20685>
    |      CVE-2017-15906 5.3 <https://vulners.com/cve/CVE-2017-15906>
    |      CVE-2016-20012 5.3 <https://vulners.com/cve/CVE-2016-20012>
    |      CNVD-2018-20962 5.3 <https://vulners.com/cnvd/CNVD-2018-20962>
    |      CNVD-2018-20960 5.3 <https://vulners.com/cnvd/CNVD-2018-20960>
    |      A9E6F50E-E7FC-51D0-9C93-A43461469FA2 5.3 <https://vulners.com/githubexploit/A9E6F50E-E7FC-51D0-9C93-A43461469FA2> *EXPLOIT*
    |      A801235B-9835-5BA8-B8FE-23B7FFCABD66 5.3 <https://vulners.com/githubexploit/A801235B-9835-5BA8-B8FE-23B7FFCABD66> *EXPLOIT*
    |      8DD1D813-FD5A-5B26-867A-CE7CAC9FEEDF 5.3 <https://vulners.com/gitee/8DD1D813-FD5A-5B26-867A-CE7CAC9FEEDF> *EXPLOIT*
    |      4F2FBB06-E601-5EAD-9679-3395D24057DD 5.3 <https://vulners.com/githubexploit/4F2FBB06-E601-5EAD-9679-3395D24057DD> *EXPLOIT*
    |      486BB6BC-9C26-597F-B865-D0E904FDA984 5.3 <https://vulners.com/githubexploit/486BB6BC-9C26-597F-B865-D0E904FDA984> *EXPLOIT*
    |      2385176A-820F-5469-AB09-C340264F2B2F 5.3 <https://vulners.com/gitee/2385176A-820F-5469-AB09-C340264F2B2F> *EXPLOIT*
    |      1337DAY-ID-31730 5.3 <https://vulners.com/zdt/1337DAY-ID-31730> *EXPLOIT*
    |      SSV:60656 5.0 <https://vulners.com/seebug/SSV:60656> *EXPLOIT*
    |      SSH_ENUM 5.0 <https://vulners.com/canvas/SSH_ENUM> *EXPLOIT*
    |      PACKETSTORM:150621 5.0 <https://vulners.com/packetstorm/PACKETSTORM:150621> *EXPLOIT*
    |      EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0 5.0 <https://vulners.com/exploitpack/EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0> *EXPLOIT*
    |      EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283 5.0 <https://vulners.com/exploitpack/EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283> *EXPLOIT*
    |      EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF 4.3 <https://vulners.com/exploitpack/EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF> *EXPLOIT*
    |      EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF 4.3 <https://vulners.com/exploitpack/EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF> *EXPLOIT*
    |      CVE-2015-5352 4.3 <https://vulners.com/cve/CVE-2015-5352>
    |      1337DAY-ID-25440 4.3 <https://vulners.com/zdt/1337DAY-ID-25440> *EXPLOIT*
    |      1337DAY-ID-25438 4.3 <https://vulners.com/zdt/1337DAY-ID-25438> *EXPLOIT*
    |      CVE-2010-4755 4.0 <https://vulners.com/cve/CVE-2010-4755>
    |      CVE-2021-36368 3.7 <https://vulners.com/cve/CVE-2021-36368>
    |      CVE-2025-61985 3.6 <https://vulners.com/cve/CVE-2025-61985>
    |      CVE-2025-61984 3.6 <https://vulners.com/cve/CVE-2025-61984>
    |      B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150 3.6 <https://vulners.com/githubexploit/B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150> *EXPLOIT*
    |      4C6E2182-0E99-5626-83F6-1646DD648C57 3.6 <https://vulners.com/githubexploit/4C6E2182-0E99-5626-83F6-1646DD648C57> *EXPLOIT*
    |      CVE-2011-5000 3.5 <https://vulners.com/cve/CVE-2011-5000>
    |      CVE-2026-35388 2.5 <https://vulners.com/cve/CVE-2026-35388>
    |      SSV:92581 2.1 <https://vulners.com/seebug/SSV:92581> *EXPLOIT*
    |      CVE-2008-3259 1.2 <https://vulners.com/cve/CVE-2008-3259>
    |      PACKETSTORM:151227 0.0 <https://vulners.com/packetstorm/PACKETSTORM:151227> *EXPLOIT*
    |      PACKETSTORM:140261 0.0 <https://vulners.com/packetstorm/PACKETSTORM:140261> *EXPLOIT*
    |      PACKETSTORM:138006 0.0 <https://vulners.com/packetstorm/PACKETSTORM:138006> *EXPLOIT*
    |      PACKETSTORM:137942 0.0 <https://vulners.com/packetstorm/PACKETSTORM:137942> *EXPLOIT*
    |      1337DAY-ID-30937 0.0 <https://vulners.com/zdt/1337DAY-ID-30937> *EXPLOIT*
    |      1337DAY-ID-26468 0.0 <https://vulners.com/zdt/1337DAY-ID-26468> *EXPLOIT*
    |_     1337DAY-ID-25391 0.0 <https://vulners.com/zdt/1337DAY-ID-25391> *EXPLOIT*
    23/tcp   open  telnet?
    25/tcp   open  smtp        Postfix smtpd
    | smtp-vuln-cve2010-4344:
    |_The SMTP server is not Exim: NOT VULNERABLE
    53/tcp   open  domain      ISC BIND 9.4.2
    | vulners:
    |   cpe:/a:isc:bind:9.4.2:
    |      SSV:2853 10.0 <https://vulners.com/seebug/SSV:2853> *EXPLOIT*
    |      CVE-2008-0122 10.0 <https://vulners.com/cve/CVE-2008-0122>
    |      CVE-2021-25216 9.8 <https://vulners.com/cve/CVE-2021-25216>
    |      CVE-2020-8616 8.6 <https://vulners.com/cve/CVE-2020-8616>
    |      CVE-2016-1286 8.6 <https://vulners.com/cve/CVE-2016-1286>
    |      CNVD-2020-34454 8.6 <https://vulners.com/cnvd/CNVD-2020-34454>
    |      SSV:60184 8.5 <https://vulners.com/seebug/SSV:60184> *EXPLOIT*
    |      CVE-2012-1667 8.5 <https://vulners.com/cve/CVE-2012-1667>
    |      SSV:60292 7.8 <https://vulners.com/seebug/SSV:60292> *EXPLOIT*
    |      PACKETSTORM:180552 7.8 <https://vulners.com/packetstorm/PACKETSTORM:180552> *EXPLOIT*
    |      PACKETSTORM:180551 7.8 <https://vulners.com/packetstorm/PACKETSTORM:180551> *EXPLOIT*
    |      PACKETSTORM:138960 7.8 <https://vulners.com/packetstorm/PACKETSTORM:138960> *EXPLOIT*
    |      PACKETSTORM:132926 7.8 <https://vulners.com/packetstorm/PACKETSTORM:132926> *EXPLOIT*
    |      MSF:AUXILIARY-DOS-DNS-BIND_TKEY- 7.8 <https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TKEY-> *EXPLOIT*
    |      EXPLOITPACK:BE4F638B632EA0754155A27ECC4B3D3F 7.8 <https://vulners.com/exploitpack/EXPLOITPACK:BE4F638B632EA0754155A27ECC4B3D3F> *EXPLOIT*
    |      EXPLOITPACK:46DEBFAC850194C04C54F93E0DFF5F4F 7.8 <https://vulners.com/exploitpack/EXPLOITPACK:46DEBFAC850194C04C54F93E0DFF5F4F> *EXPLOIT*
    |      EXPLOITPACK:09762DB0197BBAAAB6FC79F24F0D2A74 7.8 <https://vulners.com/exploitpack/EXPLOITPACK:09762DB0197BBAAAB6FC79F24F0D2A74> *EXPLOIT*
    |      EDB-ID:42121 7.8 <https://vulners.com/exploitdb/EDB-ID:42121> *EXPLOIT*
    |      EDB-ID:40453 7.8 <https://vulners.com/exploitdb/EDB-ID:40453> *EXPLOIT*
    |      EDB-ID:37723 7.8 <https://vulners.com/exploitdb/EDB-ID:37723> *EXPLOIT*
    |      EDB-ID:37721 7.8 <https://vulners.com/exploitdb/EDB-ID:37721> *EXPLOIT*
    |      E183E822-9005-5F4E-B024-D9C4761AE308 7.8 <https://vulners.com/githubexploit/E183E822-9005-5F4E-B024-D9C4761AE308> *EXPLOIT*
    |      CVE-2017-3141 7.8 <https://vulners.com/cve/CVE-2017-3141>
    |      CVE-2016-2776 7.8 <https://vulners.com/cve/CVE-2016-2776>
    |      CVE-2015-5722 7.8 <https://vulners.com/cve/CVE-2015-5722>
    |      CVE-2015-5477 7.8 <https://vulners.com/cve/CVE-2015-5477>
    |      CVE-2014-8500 7.8 <https://vulners.com/cve/CVE-2014-8500>
    |      CVE-2012-5166 7.8 <https://vulners.com/cve/CVE-2012-5166>
    |      CVE-2012-4244 7.8 <https://vulners.com/cve/CVE-2012-4244>
    |      CVE-2012-3817 7.8 <https://vulners.com/cve/CVE-2012-3817>
    |      CVE-2008-4163 7.8 <https://vulners.com/cve/CVE-2008-4163>
    |      7459D6A0-D6CA-5CD2-A484-5DD984C0E5E4 7.8 <https://vulners.com/githubexploit/7459D6A0-D6CA-5CD2-A484-5DD984C0E5E4> *EXPLOIT*
    |      673990FE-C5D5-5501-A342-D1AEC9F2A871 7.8 <https://vulners.com/githubexploit/673990FE-C5D5-5501-A342-D1AEC9F2A871> *EXPLOIT*
    |      1337DAY-ID-25325 7.8 <https://vulners.com/zdt/1337DAY-ID-25325> *EXPLOIT*
    |      1337DAY-ID-23970 7.8 <https://vulners.com/zdt/1337DAY-ID-23970> *EXPLOIT*
    |      1337DAY-ID-23960 7.8 <https://vulners.com/zdt/1337DAY-ID-23960> *EXPLOIT*
    |      1337DAY-ID-23948 7.8 <https://vulners.com/zdt/1337DAY-ID-23948> *EXPLOIT*
    |      CVE-2010-0382 7.6 <https://vulners.com/cve/CVE-2010-0382>
    |      PACKETSTORM:180550 7.5 <https://vulners.com/packetstorm/PACKETSTORM:180550> *EXPLOIT*
    |      MSF:AUXILIARY-DOS-DNS-BIND_TSIG_BADTIME- 7.5 <https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TSIG_BADTIME-> *EXPLOIT*
    |      MSF:AUXILIARY-DOS-DNS-BIND_TSIG- 7.5 <https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TSIG-> *EXPLOIT*
    |      FBC03933-7A65-52F3-83F4-4B2253A490B6 7.5 <https://vulners.com/githubexploit/FBC03933-7A65-52F3-83F4-4B2253A490B6> *EXPLOIT*
    |      CVE-2026-3039 7.5 <https://vulners.com/cve/CVE-2026-3039>
    |      CVE-2023-50868 7.5 <https://vulners.com/cve/CVE-2023-50868>
    |      CVE-2023-50387 7.5 <https://vulners.com/cve/CVE-2023-50387>
    |      CVE-2023-4408 7.5 <https://vulners.com/cve/CVE-2023-4408>
    |      CVE-2023-3341 7.5 <https://vulners.com/cve/CVE-2023-3341>
    |      CVE-2021-25215 7.5 <https://vulners.com/cve/CVE-2021-25215>
    |      CVE-2020-8617 7.5 <https://vulners.com/cve/CVE-2020-8617>
    |      CVE-2017-3145 7.5 <https://vulners.com/cve/CVE-2017-3145>
    |      CVE-2017-3143 7.5 <https://vulners.com/cve/CVE-2017-3143>
    |      CVE-2016-9444 7.5 <https://vulners.com/cve/CVE-2016-9444>
    |      CVE-2016-9131 7.5 <https://vulners.com/cve/CVE-2016-9131>
    |      CVE-2016-8864 7.5 <https://vulners.com/cve/CVE-2016-8864>
    |      CVE-2016-2848 7.5 <https://vulners.com/cve/CVE-2016-2848>
    |      CVE-2009-0265 7.5 <https://vulners.com/cve/CVE-2009-0265>
    |      CNVD-2017-12537 7.5 <https://vulners.com/cnvd/CNVD-2017-12537>
    |      9ED8A03D-FE34-5F77-8C66-C03C9615AF07 7.5 <https://vulners.com/gitee/9ED8A03D-FE34-5F77-8C66-C03C9615AF07> *EXPLOIT*
    |      1337DAY-ID-34485 7.5 <https://vulners.com/zdt/1337DAY-ID-34485> *EXPLOIT*
    |      EXPLOITPACK:D6DDF5E24DE171DAAD71FD95FC1B67F2 7.2 <https://vulners.com/exploitpack/EXPLOITPACK:D6DDF5E24DE171DAAD71FD95FC1B67F2> *EXPLOIT*
    |      CVE-2015-8461 7.1 <https://vulners.com/cve/CVE-2015-8461>
    |      CVE-2015-5986 7.1 <https://vulners.com/cve/CVE-2015-5986>
    |      CVE-2015-8705 7.0 <https://vulners.com/cve/CVE-2015-8705>
    |      CVE-2016-1285 6.8 <https://vulners.com/cve/CVE-2016-1285>
    |      CVE-2015-8704 6.8 <https://vulners.com/cve/CVE-2015-8704>
    |      CVE-2009-0025 6.8 <https://vulners.com/cve/CVE-2009-0025>
    |      CVE-2020-8622 6.5 <https://vulners.com/cve/CVE-2020-8622>
    |      CVE-2018-5741 6.5 <https://vulners.com/cve/CVE-2018-5741>
    |      CVE-2016-6170 6.5 <https://vulners.com/cve/CVE-2016-6170>
    |      CVE-2010-3614 6.4 <https://vulners.com/cve/CVE-2010-3614>
    |      CVE-2016-2775 5.9 <https://vulners.com/cve/CVE-2016-2775>
    |      CVE-2022-2795 5.3 <https://vulners.com/cve/CVE-2022-2795>
    |      CVE-2021-25219 5.3 <https://vulners.com/cve/CVE-2021-25219>
    |      CVE-2017-3142 5.3 <https://vulners.com/cve/CVE-2017-3142>
    |      CNVD-2024-16843 5.3 <https://vulners.com/cnvd/CNVD-2024-16843>
    |      SSV:30099 5.0 <https://vulners.com/seebug/SSV:30099> *EXPLOIT*
    |      SSV:20595 5.0 <https://vulners.com/seebug/SSV:20595> *EXPLOIT*
    |      PACKETSTORM:157836 5.0 <https://vulners.com/packetstorm/PACKETSTORM:157836> *EXPLOIT*
    |      CVE-2015-8000 5.0 <https://vulners.com/cve/CVE-2015-8000>
    |      CVE-2012-1033 5.0 <https://vulners.com/cve/CVE-2012-1033>
    |      CVE-2011-4313 5.0 <https://vulners.com/cve/CVE-2011-4313>
    |      CVE-2011-1910 5.0 <https://vulners.com/cve/CVE-2011-1910>
    |      SSV:11919 4.3 <https://vulners.com/seebug/SSV:11919> *EXPLOIT*
    |      CVE-2010-3762 4.3 <https://vulners.com/cve/CVE-2010-3762>
    |      CVE-2010-0097 4.3 <https://vulners.com/cve/CVE-2010-0097>
    |      CVE-2009-0696 4.3 <https://vulners.com/cve/CVE-2009-0696>
    |      CVE-2010-0290 4.0 <https://vulners.com/cve/CVE-2010-0290>
    |      SSV:14986 2.6 <https://vulners.com/seebug/SSV:14986> *EXPLOIT*
    |      CVE-2009-4022 2.6 <https://vulners.com/cve/CVE-2009-4022>
    |      PACKETSTORM:142800 0.0 <https://vulners.com/packetstorm/PACKETSTORM:142800> *EXPLOIT*
    |_     1337DAY-ID-27896 0.0 <https://vulners.com/zdt/1337DAY-ID-27896> *EXPLOIT*
    80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
    | vulners:
    |   cpe:/a:apache:http_server:2.2.8:
    |      SSV:69341 10.0 <https://vulners.com/seebug/SSV:69341> *EXPLOIT*
    |      SSV:19282 10.0 <https://vulners.com/seebug/SSV:19282> *EXPLOIT*
    |      SSV:19236 10.0 <https://vulners.com/seebug/SSV:19236> *EXPLOIT*
    |      SSV:11999 10.0 <https://vulners.com/seebug/SSV:11999> *EXPLOIT*
    |      PACKETSTORM:86964 10.0 <https://vulners.com/packetstorm/PACKETSTORM:86964> *EXPLOIT*
    |      PACKETSTORM:180533 10.0 <https://vulners.com/packetstorm/PACKETSTORM:180533> *EXPLOIT*
    |      MSF:AUXILIARY-DOS-HTTP-APACHE_MOD_ISAPI- 10.0 <https://vulners.com/metasploit/MSF:AUXILIARY-DOS-HTTP-APACHE_MOD_ISAPI-> *EXPLOIT*
    |      HTTPD:E74B6F3660D13C4DD05DF3A83EA61631 10.0 <https://vulners.com/httpd/HTTPD:E74B6F3660D13C4DD05DF3A83EA61631>
    |      HTTPD:81180E4E634CDECC9784146016B4A949 10.0 <https://vulners.com/httpd/HTTPD:81180E4E634CDECC9784146016B4A949>
    |      EXPLOITPACK:30ED468EC8BD5B71B2CB93825A852B80 10.0 <https://vulners.com/exploitpack/EXPLOITPACK:30ED468EC8BD5B71B2CB93825A852B80> *EXPLOIT*
    |      EDB-ID:14288 10.0 <https://vulners.com/exploitdb/EDB-ID:14288> *EXPLOIT*
    |      EDB-ID:11650 10.0 <https://vulners.com/exploitdb/EDB-ID:11650> *EXPLOIT*
    |      CVE-2010-0425 10.0 <https://vulners.com/cve/CVE-2010-0425>
    |      3E6BA608-776F-5B1F-9BA5-589CD2A5A351 10.0 <https://vulners.com/gitee/3E6BA608-776F-5B1F-9BA5-589CD2A5A351> *EXPLOIT*
    |      PACKETSTORM:171631 9.8 <https://vulners.com/packetstorm/PACKETSTORM:171631> *EXPLOIT*
    |      HTTPD:E69E9574251973D5AF93FA9D04997FC1 9.8 <https://vulners.com/httpd/HTTPD:E69E9574251973D5AF93FA9D04997FC1>
    |      HTTPD:E162D3AE025639FEE2A89D5AF40ABF2F 9.8 <https://vulners.com/httpd/HTTPD:E162D3AE025639FEE2A89D5AF40ABF2F>
    |      HTTPD:C072933AA965A86DA3E2C9172FFC1569 9.8 <https://vulners.com/httpd/HTTPD:C072933AA965A86DA3E2C9172FFC1569>
    |      HTTPD:A1BBCE110E077FFBF4469D4F06DB9293 9.8 <https://vulners.com/httpd/HTTPD:A1BBCE110E077FFBF4469D4F06DB9293>
    |      HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D 9.8 <https://vulners.com/httpd/HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D>
    |      HTTPD:9F5406E0F4A0B007A0A4C9C92EF9813B 9.8 <https://vulners.com/httpd/HTTPD:9F5406E0F4A0B007A0A4C9C92EF9813B>
    |      HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8 9.8 <https://vulners.com/httpd/HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8>
    |      HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E 9.8 <https://vulners.com/httpd/HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E>
    |      EDB-ID:51193 9.8 <https://vulners.com/exploitdb/EDB-ID:51193> *EXPLOIT*
    |      EDB-ID:10579 9.8 <https://vulners.com/exploitdb/EDB-ID:10579> *EXPLOIT*
    |      ECC3E825-EE29-59D3-BE28-1B30DB15940E 9.8 <https://vulners.com/githubexploit/ECC3E825-EE29-59D3-BE28-1B30DB15940E> *EXPLOIT*
    |      D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52 9.8 <https://vulners.com/githubexploit/D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52> *EXPLOIT*
    |      CVE-2026-28780 9.8 <https://vulners.com/cve/CVE-2026-28780>
    |      CVE-2024-38476 9.8 <https://vulners.com/cve/CVE-2024-38476>
    |      CVE-2022-31813 9.8 <https://vulners.com/cve/CVE-2022-31813>
    |      CVE-2022-22720 9.8 <https://vulners.com/cve/CVE-2022-22720>
    |      CVE-2021-44790 9.8 <https://vulners.com/cve/CVE-2021-44790>
    |      CVE-2021-39275 9.8 <https://vulners.com/cve/CVE-2021-39275>
    |      CVE-2018-1312 9.8 <https://vulners.com/cve/CVE-2018-1312>
    |      CVE-2017-7679 9.8 <https://vulners.com/cve/CVE-2017-7679>
    |      CVE-2017-3169 9.8 <https://vulners.com/cve/CVE-2017-3169>
    |      CVE-2017-3167 9.8 <https://vulners.com/cve/CVE-2017-3167>
    |      CVE-2009-3555 9.8 <https://vulners.com/cve/CVE-2009-3555>
    |      CNVD-2022-51061 9.8 <https://vulners.com/cnvd/CNVD-2022-51061>
    |      CNVD-2022-03225 9.8 <https://vulners.com/cnvd/CNVD-2022-03225>
    |      CNVD-2021-102386 9.8 <https://vulners.com/cnvd/CNVD-2021-102386>
    |      B6297446-2DDD-52BA-B508-29A748A5D2CC 9.8 <https://vulners.com/githubexploit/B6297446-2DDD-52BA-B508-29A748A5D2CC> *EXPLOIT*
    |      1337DAY-ID-38427 9.8 <https://vulners.com/zdt/1337DAY-ID-38427> *EXPLOIT*
    |      0DB60346-03B6-5FEE-93D7-FF5757D225AA 9.8 <https://vulners.com/gitee/0DB60346-03B6-5FEE-93D7-FF5757D225AA> *EXPLOIT*
    |      HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6 9.1 <https://vulners.com/httpd/HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6>
    |      HTTPD:459EB8D98503A2460C9445C5B224979E 9.1 <https://vulners.com/httpd/HTTPD:459EB8D98503A2460C9445C5B224979E>
    |      HTTPD:2C227652EE0B3B961706AAFCACA3D1E1 9.1 <https://vulners.com/httpd/HTTPD:2C227652EE0B3B961706AAFCACA3D1E1>
    |      FD2EE3A5-BAEA-5845-BA35-E6889992214F 9.1 <https://vulners.com/githubexploit/FD2EE3A5-BAEA-5845-BA35-E6889992214F> *EXPLOIT*
    |      FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7 9.1 <https://vulners.com/githubexploit/FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7> *EXPLOIT*
    |      E606D7F4-5FA2-5907-B30E-367D6FFECD89 9.1 <https://vulners.com/githubexploit/E606D7F4-5FA2-5907-B30E-367D6FFECD89> *EXPLOIT*
    |      D8A19443-2A37-5592-8955-F614504AAF45 9.1 <https://vulners.com/githubexploit/D8A19443-2A37-5592-8955-F614504AAF45> *EXPLOIT*
    |      CVE-2024-40898 9.1 <https://vulners.com/cve/CVE-2024-40898>
    |      CVE-2022-28615 9.1 <https://vulners.com/cve/CVE-2022-28615>
    |      CVE-2022-22721 9.1 <https://vulners.com/cve/CVE-2022-22721>
    |      CVE-2017-9788 9.1 <https://vulners.com/cve/CVE-2017-9788>
    |      CNVD-2022-51060 9.1 <https://vulners.com/cnvd/CNVD-2022-51060>
    |      CNVD-2022-41638 9.1 <https://vulners.com/cnvd/CNVD-2022-41638>
    |      B5E74010-A082-5ECE-AB37-623A5B33FE7D 9.1 <https://vulners.com/githubexploit/B5E74010-A082-5ECE-AB37-623A5B33FE7D> *EXPLOIT*
    |      HTTPD:1B3D546A8500818AAC5B1359FE11A7E4 9.0 <https://vulners.com/httpd/HTTPD:1B3D546A8500818AAC5B1359FE11A7E4>
    |      CVE-2021-40438 9.0 <https://vulners.com/cve/CVE-2021-40438>
    |      CNVD-2022-03224 9.0 <https://vulners.com/cnvd/CNVD-2022-03224>
    |      AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C 9.0 <https://vulners.com/githubexploit/AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C> *EXPLOIT*
    |      9D9B3F4D-6B5C-5377-BE39-F1C432C9E457 9.0 <https://vulners.com/githubexploit/9D9B3F4D-6B5C-5377-BE39-F1C432C9E457> *EXPLOIT*
    |      8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2 9.0 <https://vulners.com/githubexploit/8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2> *EXPLOIT*
    |      7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2 9.0 <https://vulners.com/githubexploit/7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2> *EXPLOIT*
    |      36618CA8-9316-59CA-B748-82F15F407C4F 9.0 <https://vulners.com/githubexploit/36618CA8-9316-59CA-B748-82F15F407C4F> *EXPLOIT*
    |      CVE-2026-24072 8.8 <https://vulners.com/cve/CVE-2026-24072>
    |      40379BCA-07F4-5401-B618-4640793D350D 8.8 <https://vulners.com/githubexploit/40379BCA-07F4-5401-B618-4640793D350D> *EXPLOIT*
    |      CVE-2025-58098 8.3 <https://vulners.com/cve/CVE-2025-58098>
    |      CNVD-2021-102387 8.2 <https://vulners.com/cnvd/CNVD-2021-102387>
    |      B0A9E5E8-7CCC-5984-9922-A89F11D6BF38 8.2 <https://vulners.com/githubexploit/B0A9E5E8-7CCC-5984-9922-A89F11D6BF38> *EXPLOIT*
    |      HTTPD:30E0EE442FF4843665FED4FBCA25406A 8.1 <https://vulners.com/httpd/HTTPD:30E0EE442FF4843665FED4FBCA25406A>
    |      CVE-2016-5387 8.1 <https://vulners.com/cve/CVE-2016-5387>
    |      CNVD-2016-04948 8.1 <https://vulners.com/cnvd/CNVD-2016-04948>
    |      SSV:72403 7.8 <https://vulners.com/seebug/SSV:72403> *EXPLOIT*
    |      SSV:2820 7.8 <https://vulners.com/seebug/SSV:2820> *EXPLOIT*
    |      SSV:26043 7.8 <https://vulners.com/seebug/SSV:26043> *EXPLOIT*
    |      SSV:20899 7.8 <https://vulners.com/seebug/SSV:20899> *EXPLOIT*
    |      SSV:11569 7.8 <https://vulners.com/seebug/SSV:11569> *EXPLOIT*
    |      PACKETSTORM:180517 7.8 <https://vulners.com/packetstorm/PACKETSTORM:180517> *EXPLOIT*
    |      PACKETSTORM:126851 7.8 <https://vulners.com/packetstorm/PACKETSTORM:126851> *EXPLOIT*
    |      PACKETSTORM:123527 7.8 <https://vulners.com/packetstorm/PACKETSTORM:123527> *EXPLOIT*
    |      PACKETSTORM:122962 7.8 <https://vulners.com/packetstorm/PACKETSTORM:122962> *EXPLOIT*
    |      MSF:AUXILIARY-DOS-HTTP-APACHE_RANGE_DOS- 7.8 <https://vulners.com/metasploit/MSF:AUXILIARY-DOS-HTTP-APACHE_RANGE_DOS-> *EXPLOIT*
    |      HTTPD:556E7FA885F1BEDB6E3D9AAB5665198F 7.8 <https://vulners.com/httpd/HTTPD:556E7FA885F1BEDB6E3D9AAB5665198F>
    |      EXPLOITPACK:186B5FCF5C57B52642E62C06BABC6F83 7.8 <https://vulners.com/exploitpack/EXPLOITPACK:186B5FCF5C57B52642E62C06BABC6F83> *EXPLOIT*
    |      EDB-ID:18221 7.8 <https://vulners.com/exploitdb/EDB-ID:18221> *EXPLOIT*
    |      CVE-2011-3192 7.8 <https://vulners.com/cve/CVE-2011-3192>
    |      C76F17FD-A21F-5E67-97D8-51A53B9594C1 7.8 <https://vulners.com/githubexploit/C76F17FD-A21F-5E67-97D8-51A53B9594C1> *EXPLOIT*
    |      4F94F3CE-6A41-5E04-A51B-4D22ED6CF210 7.8 <https://vulners.com/githubexploit/4F94F3CE-6A41-5E04-A51B-4D22ED6CF210> *EXPLOIT*
    |      1337DAY-ID-21170 7.8 <https://vulners.com/zdt/1337DAY-ID-21170> *EXPLOIT*
    |      SSV:12673 7.5 <https://vulners.com/seebug/SSV:12673> *EXPLOIT*
    |      SSV:12626 7.5 <https://vulners.com/seebug/SSV:12626> *EXPLOIT*
    |      PACKETSTORM:181038 7.5 <https://vulners.com/packetstorm/PACKETSTORM:181038> *EXPLOIT*
    |      MSF:AUXILIARY-SCANNER-HTTP-APACHE_OPTIONSBLEED- 7.5 <https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-HTTP-APACHE_OPTIONSBLEED-> *EXPLOIT*
    |      HTTPD:F1CFBC9B54DFAD0499179863D36830BB 7.5 <https://vulners.com/httpd/HTTPD:F1CFBC9B54DFAD0499179863D36830BB>
    |      HTTPD:C317C7138B4A8BBD54A901D6DDDCB837 7.5 <https://vulners.com/httpd/HTTPD:C317C7138B4A8BBD54A901D6DDDCB837>
    |      HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F 7.5 <https://vulners.com/httpd/HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F>
    |      HTTPD:C0856723C0FBF5502E1378536B484C09 7.5 <https://vulners.com/httpd/HTTPD:C0856723C0FBF5502E1378536B484C09>
    |      HTTPD:BEF84406F2FB3CB90F1C555BEFF774E2 7.5 <https://vulners.com/httpd/HTTPD:BEF84406F2FB3CB90F1C555BEFF774E2>
    |      HTTPD:B1B0A31C4AD388CC6C575931414173E2 7.5 <https://vulners.com/httpd/HTTPD:B1B0A31C4AD388CC6C575931414173E2>
    |      HTTPD:7DDAAFDB1FD8B2E7FD36ADABA5DB6DAA 7.5 <https://vulners.com/httpd/HTTPD:7DDAAFDB1FD8B2E7FD36ADABA5DB6DAA>
    |      HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5 7.5 <https://vulners.com/httpd/HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5>
    |      HTTPD:5227799CC4172DBFA895A4F581F74C11 7.5 <https://vulners.com/httpd/HTTPD:5227799CC4172DBFA895A4F581F74C11>
    |      EDB-ID:42745 7.5 <https://vulners.com/exploitdb/EDB-ID:42745> *EXPLOIT*
    |      CVE-2026-34059 7.5 <https://vulners.com/cve/CVE-2026-34059>
    |      CVE-2026-29169 7.5 <https://vulners.com/cve/CVE-2026-29169>
    |      CVE-2023-31122 7.5 <https://vulners.com/cve/CVE-2023-31122>
    |      CVE-2022-30556 7.5 <https://vulners.com/cve/CVE-2022-30556>
    |      CVE-2022-29404 7.5 <https://vulners.com/cve/CVE-2022-29404>
    |      CVE-2022-22719 7.5 <https://vulners.com/cve/CVE-2022-22719>
    |      CVE-2021-34798 7.5 <https://vulners.com/cve/CVE-2021-34798>
    |      CVE-2018-8011 7.5 <https://vulners.com/cve/CVE-2018-8011>
    |      CVE-2018-1303 7.5 <https://vulners.com/cve/CVE-2018-1303>
    |      CVE-2017-9798 7.5 <https://vulners.com/cve/CVE-2017-9798>
    |      CVE-2017-15710 7.5 <https://vulners.com/cve/CVE-2017-15710>
    |      CVE-2016-8743 7.5 <https://vulners.com/cve/CVE-2016-8743>
    |      CVE-2009-2699 7.5 <https://vulners.com/cve/CVE-2009-2699>
    |      CVE-2009-1955 7.5 <https://vulners.com/cve/CVE-2009-1955>
    |      CVE-2006-20001 7.5 <https://vulners.com/cve/CVE-2006-20001>
    |      CNVD-2025-30836 7.5 <https://vulners.com/cnvd/CNVD-2025-30836>
    |      CNVD-2025-16614 7.5 <https://vulners.com/cnvd/CNVD-2025-16614>
    |      CNVD-2024-20839 7.5 <https://vulners.com/cnvd/CNVD-2024-20839>
    |      CNVD-2023-93320 7.5 <https://vulners.com/cnvd/CNVD-2023-93320>
    |      CNVD-2023-80558 7.5 <https://vulners.com/cnvd/CNVD-2023-80558>
    |      CNVD-2022-53584 7.5 <https://vulners.com/cnvd/CNVD-2022-53584>
    |      CNVD-2022-41639 7.5 <https://vulners.com/cnvd/CNVD-2022-41639>
    |      CNVD-2022-03223 7.5 <https://vulners.com/cnvd/CNVD-2022-03223>
    |      CNVD-2019-41283 7.5 <https://vulners.com/cnvd/CNVD-2019-41283>
    |      CNVD-2017-13906 7.5 <https://vulners.com/cnvd/CNVD-2017-13906>
    |      CNVD-2016-13233 7.5 <https://vulners.com/cnvd/CNVD-2016-13233>
    |      CNVD-2016-13232 7.5 <https://vulners.com/cnvd/CNVD-2016-13232>
    |      CD6A79B3-8167-5CFD-9FCB-6986FDF0BE1A 7.5 <https://vulners.com/githubexploit/CD6A79B3-8167-5CFD-9FCB-6986FDF0BE1A> *EXPLOIT*
    |      A0F268C8-7319-5637-82F7-8DAF72D14629 7.5 <https://vulners.com/githubexploit/A0F268C8-7319-5637-82F7-8DAF72D14629> *EXPLOIT*
    |      857E0BF8-9A29-54C5-82EA-8D7C0798CAA6 7.5 <https://vulners.com/githubexploit/857E0BF8-9A29-54C5-82EA-8D7C0798CAA6> *EXPLOIT*
    |      45D138AD-BEC6-552A-91EA-8816914CA7F4 7.5 <https://vulners.com/githubexploit/45D138AD-BEC6-552A-91EA-8816914CA7F4> *EXPLOIT*
    |      CVE-2025-49812 7.4 <https://vulners.com/cve/CVE-2025-49812>
    |      CVE-2023-38709 7.3 <https://vulners.com/cve/CVE-2023-38709>
    |      CNVD-2024-36395 7.3 <https://vulners.com/cnvd/CNVD-2024-36395>
    |      SSV:11802 7.1 <https://vulners.com/seebug/SSV:11802> *EXPLOIT*
    |      SSV:11762 7.1 <https://vulners.com/seebug/SSV:11762> *EXPLOIT*
    |      HTTPD:B44AEE5F83602723E751B3341D72C01D 7.1 <https://vulners.com/httpd/HTTPD:B44AEE5F83602723E751B3341D72C01D>
    |      HTTPD:4D420BA542C9357A7F064936250DAEFF 7.1 <https://vulners.com/httpd/HTTPD:4D420BA542C9357A7F064936250DAEFF>
    |      CVE-2009-1891 7.1 <https://vulners.com/cve/CVE-2009-1891>
    |      CVE-2009-1890 7.1 <https://vulners.com/cve/CVE-2009-1890>
    |      SSV:60427 6.9 <https://vulners.com/seebug/SSV:60427> *EXPLOIT*
    |      SSV:60386 6.9 <https://vulners.com/seebug/SSV:60386> *EXPLOIT*
    |      SSV:60069 6.9 <https://vulners.com/seebug/SSV:60069> *EXPLOIT*
    |      HTTPD:D4C114070B5E7C4AA3E92FF94A57C659 6.9 <https://vulners.com/httpd/HTTPD:D4C114070B5E7C4AA3E92FF94A57C659>
    |      CVE-2012-0883 6.9 <https://vulners.com/cve/CVE-2012-0883>
    |      PACKETSTORM:127546 6.8 <https://vulners.com/packetstorm/PACKETSTORM:127546> *EXPLOIT*
    |      HTTPD:0A13DEC03E87AF57C14487550B086B51 6.8 <https://vulners.com/httpd/HTTPD:0A13DEC03E87AF57C14487550B086B51>
    |      CVE-2014-0226 6.8 <https://vulners.com/cve/CVE-2014-0226>
    |      1337DAY-ID-22451 6.8 <https://vulners.com/zdt/1337DAY-ID-22451> *EXPLOIT*
    |      SSV:11568 6.4 <https://vulners.com/seebug/SSV:11568> *EXPLOIT*
    |      HTTPD:AFA6B3F6376C54842BAFBBF24C7F44C4 6.4 <https://vulners.com/httpd/HTTPD:AFA6B3F6376C54842BAFBBF24C7F44C4>
    |      CVE-2009-1956 6.4 <https://vulners.com/cve/CVE-2009-1956>
    |      HTTPD:3E4CF20C0CAD918E98C98926264946F2 6.1 <https://vulners.com/httpd/HTTPD:3E4CF20C0CAD918E98C98926264946F2>
    |      CVE-2016-4975 6.1 <https://vulners.com/cve/CVE-2016-4975>
    |      CNVD-2018-15542 6.1 <https://vulners.com/cnvd/CNVD-2018-15542>
    |      CVE-2018-1302 5.9 <https://vulners.com/cve/CVE-2018-1302>
    |      CVE-2018-1301 5.9 <https://vulners.com/cve/CVE-2018-1301>
    |      CNVD-2018-06536 5.9 <https://vulners.com/cnvd/CNVD-2018-06536>
    |      CNVD-2018-06535 5.9 <https://vulners.com/cnvd/CNVD-2018-06535>
    |      VULNERLAB:967 5.8 <https://vulners.com/vulnerlab/VULNERLAB:967> *EXPLOIT*
    |      SSV:67231 5.8 <https://vulners.com/seebug/SSV:67231> *EXPLOIT*
    |      SSV:18637 5.8 <https://vulners.com/seebug/SSV:18637> *EXPLOIT*
    |      SSV:15088 5.8 <https://vulners.com/seebug/SSV:15088> *EXPLOIT*
    |      SSV:12600 5.8 <https://vulners.com/seebug/SSV:12600> *EXPLOIT*
    |      PACKETSTORM:84112 5.8 <https://vulners.com/packetstorm/PACKETSTORM:84112> *EXPLOIT*
    |      EXPLOITPACK:8B4E7E8DAE5A13C8250C6C33307CD66C 5.8 <https://vulners.com/exploitpack/EXPLOITPACK:8B4E7E8DAE5A13C8250C6C33307CD66C> *EXPLOIT*
    |      CNVD-2025-30835 5.4 <https://vulners.com/cnvd/CNVD-2025-30835>
    |      HTTPD:BAAB4065D254D64A717E8A5C847C7BCA 5.3 <https://vulners.com/httpd/HTTPD:BAAB4065D254D64A717E8A5C847C7BCA>
    |      HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F 5.3 <https://vulners.com/httpd/HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F>
    |      CVE-2026-34032 5.3 <https://vulners.com/cve/CVE-2026-34032>
    |      CVE-2026-33857 5.3 <https://vulners.com/cve/CVE-2026-33857>
    |      CVE-2022-37436 5.3 <https://vulners.com/cve/CVE-2022-37436>
    |      CVE-2022-28614 5.3 <https://vulners.com/cve/CVE-2022-28614>
    |      CVE-2022-28330 5.3 <https://vulners.com/cve/CVE-2022-28330>
    |      CNVD-2023-30859 5.3 <https://vulners.com/cnvd/CNVD-2023-30859>
    |      CNVD-2022-53582 5.3 <https://vulners.com/cnvd/CNVD-2022-53582>
    |      CNVD-2022-51059 5.3 <https://vulners.com/cnvd/CNVD-2022-51059>
    |      CNVD-2021-44766 5.3 <https://vulners.com/cnvd/CNVD-2021-44766>
    |      CNVD-2020-46278 5.3 <https://vulners.com/cnvd/CNVD-2020-46278>
    |      SSV:60788 5.1 <https://vulners.com/seebug/SSV:60788> *EXPLOIT*
    |      HTTPD:96CCBB8B74890DC94A45CD0955D35015 5.1 <https://vulners.com/httpd/HTTPD:96CCBB8B74890DC94A45CD0955D35015>
    |      CVE-2013-1862 5.1 <https://vulners.com/cve/CVE-2013-1862>
    |      SSV:96537 5.0 <https://vulners.com/seebug/SSV:96537> *EXPLOIT*
    |      SSV:62058 5.0 <https://vulners.com/seebug/SSV:62058> *EXPLOIT*
    |      SSV:61874 5.0 <https://vulners.com/seebug/SSV:61874> *EXPLOIT*
    |      SSV:20993 5.0 <https://vulners.com/seebug/SSV:20993> *EXPLOIT*
    |      SSV:20979 5.0 <https://vulners.com/seebug/SSV:20979> *EXPLOIT*
    |      SSV:20969 5.0 <https://vulners.com/seebug/SSV:20969> *EXPLOIT*
    |      SSV:19592 5.0 <https://vulners.com/seebug/SSV:19592> *EXPLOIT*
    |      SSV:15137 5.0 <https://vulners.com/seebug/SSV:15137> *EXPLOIT*
    |      PACKETSTORM:181059 5.0 <https://vulners.com/packetstorm/PACKETSTORM:181059> *EXPLOIT*
    |      PACKETSTORM:105672 5.0 <https://vulners.com/packetstorm/PACKETSTORM:105672> *EXPLOIT*
    |      PACKETSTORM:105591 5.0 <https://vulners.com/packetstorm/PACKETSTORM:105591> *EXPLOIT*
    |      MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS- 5.0 <https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS-> *EXPLOIT*
    |      HTTPD:FF76CF8F03BE59B7AD0119034B0022DB 5.0 <https://vulners.com/httpd/HTTPD:FF76CF8F03BE59B7AD0119034B0022DB>
    |      HTTPD:DD1BEF13C172D3E8CA5D3F3906101EC9 5.0 <https://vulners.com/httpd/HTTPD:DD1BEF13C172D3E8CA5D3F3906101EC9>
    |      HTTPD:D1C855645E1630AE37C6F642C1D0F213 5.0 <https://vulners.com/httpd/HTTPD:D1C855645E1630AE37C6F642C1D0F213>
    |      HTTPD:85C24937CF85C2E1DBF78F9954817A28 5.0 <https://vulners.com/httpd/HTTPD:85C24937CF85C2E1DBF78F9954817A28>
    |      HTTPD:6D37F924288E2D149DC3C52135232B6E 5.0 <https://vulners.com/httpd/HTTPD:6D37F924288E2D149DC3C52135232B6E>
    |      HTTPD:6CA43FB8E8332E715522C8A6C24EC31E 5.0 <https://vulners.com/httpd/HTTPD:6CA43FB8E8332E715522C8A6C24EC31E>
    |      HTTPD:60BF8A7CCF62E24F92B3DCCA0E53F1F8 5.0 <https://vulners.com/httpd/HTTPD:60BF8A7CCF62E24F92B3DCCA0E53F1F8>
    |      HTTPD:423307886E19F2012B809EEB1E9C6846 5.0 <https://vulners.com/httpd/HTTPD:423307886E19F2012B809EEB1E9C6846>
    |      HTTPD:371AA87DEAE292D8E6ACC01309CA723A 5.0 <https://vulners.com/httpd/HTTPD:371AA87DEAE292D8E6ACC01309CA723A>
    |      HTTPD:2E324CC4C6C61757E316E26EF4DCB945 5.0 <https://vulners.com/httpd/HTTPD:2E324CC4C6C61757E316E26EF4DCB945>
    |      HTTPD:2C06F6E938AADE21D7C59CED65A985E6 5.0 <https://vulners.com/httpd/HTTPD:2C06F6E938AADE21D7C59CED65A985E6>
    |      HTTPD:1DC50F4C723B9143E9713B27031C6043 5.0 <https://vulners.com/httpd/HTTPD:1DC50F4C723B9143E9713B27031C6043>
    |      HTTPD:1069F9C369A2B2B1C4F8A1AC73589169 5.0 <https://vulners.com/httpd/HTTPD:1069F9C369A2B2B1C4F8A1AC73589169>
    |      EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D 5.0 <https://vulners.com/exploitpack/EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D> *EXPLOIT*
    |      EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B 5.0 <https://vulners.com/exploitpack/EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B> *EXPLOIT*
    |      EDB-ID:17969 5.0 <https://vulners.com/exploitdb/EDB-ID:17969> *EXPLOIT*
    |      CVE-2015-3183 5.0 <https://vulners.com/cve/CVE-2015-3183>
    |      CVE-2015-0228 5.0 <https://vulners.com/cve/CVE-2015-0228>
    |      CVE-2014-0231 5.0 <https://vulners.com/cve/CVE-2014-0231>
    |      CVE-2014-0098 5.0 <https://vulners.com/cve/CVE-2014-0098>
    |      CVE-2013-6438 5.0 <https://vulners.com/cve/CVE-2013-6438>
    |      CVE-2013-5704 5.0 <https://vulners.com/cve/CVE-2013-5704>
    |      CVE-2011-3368 5.0 <https://vulners.com/cve/CVE-2011-3368>
    |      CVE-2010-1623 5.0 <https://vulners.com/cve/CVE-2010-1623>
    |      CVE-2010-1452 5.0 <https://vulners.com/cve/CVE-2010-1452>
    |      CVE-2010-0408 5.0 <https://vulners.com/cve/CVE-2010-0408>
    |      CVE-2009-3720 5.0 <https://vulners.com/cve/CVE-2009-3720>
    |      CVE-2009-3560 5.0 <https://vulners.com/cve/CVE-2009-3560>
    |      CVE-2009-3095 5.0 <https://vulners.com/cve/CVE-2009-3095>
    |      CVE-2008-2364 5.0 <https://vulners.com/cve/CVE-2008-2364>
    |      CVE-2007-6750 5.0 <https://vulners.com/cve/CVE-2007-6750>
    |      CNVD-2015-01691 5.0 <https://vulners.com/cnvd/CNVD-2015-01691>
    |      1337DAY-ID-28573 5.0 <https://vulners.com/zdt/1337DAY-ID-28573> *EXPLOIT*
    |      SSV:11668 4.9 <https://vulners.com/seebug/SSV:11668> *EXPLOIT*
    |      SSV:11501 4.9 <https://vulners.com/seebug/SSV:11501> *EXPLOIT*
    |      HTTPD:05AF7B1B11654BC6892C02003A12DE06 4.9 <https://vulners.com/httpd/HTTPD:05AF7B1B11654BC6892C02003A12DE06>
    |      CVE-2009-1195 4.9 <https://vulners.com/cve/CVE-2009-1195>
    |      EA6ADD14-D80B-5DC2-9991-1F9663E2D09F 4.8 <https://vulners.com/githubexploit/EA6ADD14-D80B-5DC2-9991-1F9663E2D09F> *EXPLOIT*
    |      CVE-2026-33006 4.8 <https://vulners.com/cve/CVE-2026-33006>
    |      SSV:30024 4.6 <https://vulners.com/seebug/SSV:30024> *EXPLOIT*
    |      HTTPD:FB0DB72A0946D2AA25FA9FA21ADB2CE1 4.6 <https://vulners.com/httpd/HTTPD:FB0DB72A0946D2AA25FA9FA21ADB2CE1>
    |      CVE-2012-0031 4.6 <https://vulners.com/cve/CVE-2012-0031>
    |      1337DAY-ID-27465 4.6 <https://vulners.com/zdt/1337DAY-ID-27465> *EXPLOIT*
    |      SSV:23169 4.4 <https://vulners.com/seebug/SSV:23169> *EXPLOIT*
    |      HTTPD:6309ABD03BB1B29C82E941636515010E 4.4 <https://vulners.com/httpd/HTTPD:6309ABD03BB1B29C82E941636515010E>
    |      CVE-2011-3607 4.4 <https://vulners.com/cve/CVE-2011-3607>
    |      1337DAY-ID-27473 4.4 <https://vulners.com/zdt/1337DAY-ID-27473> *EXPLOIT*
    |      SSV:60905 4.3 <https://vulners.com/seebug/SSV:60905> *EXPLOIT*
    |      SSV:60657 4.3 <https://vulners.com/seebug/SSV:60657> *EXPLOIT*
    |      SSV:60653 4.3 <https://vulners.com/seebug/SSV:60653> *EXPLOIT*
    |      SSV:60345 4.3 <https://vulners.com/seebug/SSV:60345> *EXPLOIT*
    |      SSV:4786 4.3 <https://vulners.com/seebug/SSV:4786> *EXPLOIT*
    |      SSV:3804 4.3 <https://vulners.com/seebug/SSV:3804> *EXPLOIT*
    |      SSV:30094 4.3 <https://vulners.com/seebug/SSV:30094> *EXPLOIT*
    |      SSV:30056 4.3 <https://vulners.com/seebug/SSV:30056> *EXPLOIT*
    |      SSV:24250 4.3 <https://vulners.com/seebug/SSV:24250> *EXPLOIT*
    |      SSV:20555 4.3 <https://vulners.com/seebug/SSV:20555> *EXPLOIT*
    |      SSV:19320 4.3 <https://vulners.com/seebug/SSV:19320> *EXPLOIT*
    |      SSV:11558 4.3 <https://vulners.com/seebug/SSV:11558> *EXPLOIT*
    |      PACKETSTORM:109284 4.3 <https://vulners.com/packetstorm/PACKETSTORM:109284> *EXPLOIT*
    |      HTTPD:FD1CC7EACBC758C451BA5B8D25FCB6DD 4.3 <https://vulners.com/httpd/HTTPD:FD1CC7EACBC758C451BA5B8D25FCB6DD>
    |      HTTPD:C730B9155CAC64B44A77E253B3135FE5 4.3 <https://vulners.com/httpd/HTTPD:C730B9155CAC64B44A77E253B3135FE5>
    |      HTTPD:B90E2A3B47C473DD04F25ECBDA96D6CE 4.3 <https://vulners.com/httpd/HTTPD:B90E2A3B47C473DD04F25ECBDA96D6CE>
    |      HTTPD:B07D6585013819446B5017BD7E358E6F 4.3 <https://vulners.com/httpd/HTTPD:B07D6585013819446B5017BD7E358E6F>
    |      HTTPD:AC5C28237AB3E52EF4D366EB0CD6D4AF 4.3 <https://vulners.com/httpd/HTTPD:AC5C28237AB3E52EF4D366EB0CD6D4AF>
    |      HTTPD:A49ADFA68FCEB939DA0E2BE13CA74CB9 4.3 <https://vulners.com/httpd/HTTPD:A49ADFA68FCEB939DA0E2BE13CA74CB9>
    |      HTTPD:49F10A242AB057B651259425C3E680F4 4.3 <https://vulners.com/httpd/HTTPD:49F10A242AB057B651259425C3E680F4>
    |      HTTPD:3D474EEBC8F5BC66AE37F523DD259829 4.3 <https://vulners.com/httpd/HTTPD:3D474EEBC8F5BC66AE37F523DD259829>
    |      HTTPD:2A661E9492CCEF999508BD8503884E30 4.3 <https://vulners.com/httpd/HTTPD:2A661E9492CCEF999508BD8503884E30>
    |      HTTPD:1E858A305C3DEA1B5E9A23EE1352B1B3 4.3 <https://vulners.com/httpd/HTTPD:1E858A305C3DEA1B5E9A23EE1352B1B3>
    |      HTTPD:0F6B8D022A5D1C68540812E406264625 4.3 <https://vulners.com/httpd/HTTPD:0F6B8D022A5D1C68540812E406264625>
    |      HTTPD:0D2952537BF45B77447EF90EAD31D8C9 4.3 <https://vulners.com/httpd/HTTPD:0D2952537BF45B77447EF90EAD31D8C9>
    |      EXPLOITPACK:FDCB3D93694E48CD5EE27CE55D6801DE 4.3 <https://vulners.com/exploitpack/EXPLOITPACK:FDCB3D93694E48CD5EE27CE55D6801DE> *EXPLOIT*
    |      EDB-ID:35738 4.3 <https://vulners.com/exploitdb/EDB-ID:35738> *EXPLOIT*
    |      CVE-2016-8612 4.3 <https://vulners.com/cve/CVE-2016-8612>
    |      CVE-2014-0118 4.3 <https://vulners.com/cve/CVE-2014-0118>
    |      CVE-2013-1896 4.3 <https://vulners.com/cve/CVE-2013-1896>
    |      CVE-2012-4558 4.3 <https://vulners.com/cve/CVE-2012-4558>
    |      CVE-2012-3499 4.3 <https://vulners.com/cve/CVE-2012-3499>
    |      CVE-2012-0053 4.3 <https://vulners.com/cve/CVE-2012-0053>
    |      CVE-2011-4317 4.3 <https://vulners.com/cve/CVE-2011-4317>
    |      CVE-2011-3639 4.3 <https://vulners.com/cve/CVE-2011-3639>
    |      CVE-2011-0419 4.3 <https://vulners.com/cve/CVE-2011-0419>
    |      CVE-2010-0434 4.3 <https://vulners.com/cve/CVE-2010-0434>
    |      CVE-2009-0023 4.3 <https://vulners.com/cve/CVE-2009-0023>
    |      CVE-2008-2939 4.3 <https://vulners.com/cve/CVE-2008-2939>
    |      CVE-2008-0455 4.3 <https://vulners.com/cve/CVE-2008-0455>
    |      CVE-2007-6420 4.3 <https://vulners.com/cve/CVE-2007-6420>
    |      67D5C133-2D28-56DF-B3FF-FA397606547D 4.3 <https://vulners.com/gitee/67D5C133-2D28-56DF-B3FF-FA397606547D> *EXPLOIT*
    |      SSV:12628 2.6 <https://vulners.com/seebug/SSV:12628> *EXPLOIT*
    |      HTTPD:AA860ED739944CC66DCA320985CEC190 2.6 <https://vulners.com/httpd/HTTPD:AA860ED739944CC66DCA320985CEC190>
    |      HTTPD:A79620D4A49D1F0D9BE6A18FD0CA234C 2.6 <https://vulners.com/httpd/HTTPD:A79620D4A49D1F0D9BE6A18FD0CA234C>
    |      CVE-2012-2687 2.6 <https://vulners.com/cve/CVE-2012-2687>
    |      CVE-2009-3094 2.6 <https://vulners.com/cve/CVE-2009-3094>
    |      CVE-2008-0456 2.6 <https://vulners.com/cve/CVE-2008-0456>
    |      SSV:60250 1.2 <https://vulners.com/seebug/SSV:60250> *EXPLOIT*
    |      CVE-2011-4415 1.2 <https://vulners.com/cve/CVE-2011-4415>
    |      1337DAY-ID-9602 0.0 <https://vulners.com/zdt/1337DAY-ID-9602> *EXPLOIT*
    |      1337DAY-ID-21346 0.0 <https://vulners.com/zdt/1337DAY-ID-21346> *EXPLOIT*
    |      1337DAY-ID-17257 0.0 <https://vulners.com/zdt/1337DAY-ID-17257> *EXPLOIT*
    |      1337DAY-ID-16843 0.0 <https://vulners.com/zdt/1337DAY-ID-16843> *EXPLOIT*
    |      1337DAY-ID-13268 0.0 <https://vulners.com/zdt/1337DAY-ID-13268> *EXPLOIT*
    |_     1337DAY-ID-11185 0.0 <https://vulners.com/zdt/1337DAY-ID-11185> *EXPLOIT*
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |*http-csrf: Couldn't find any CSRF vulnerabilities.
    | http-enum:
    |   /tikiwiki/: Tikiwiki
    |   /test/: Test page
    |   /phpinfo.php: Possible information file
    |*  /phpMyAdmin/: phpMyAdmin
    |_http-trace: TRACE is enabled
    |_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |*http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
    111/tcp  open  rpcbind     2 (RPC #100000)
    | rpcinfo:
    |   program version    port/proto  service
    |   100000  2            111/tcp   rpcbind
    |   100000  2            111/udp   rpcbind
    |   100003  2,3,4       2049/tcp   nfs
    |   100003  2,3,4       2049/udp   nfs
    |   100005  1,2,3      44705/tcp   mountd
    |   100005  1,2,3      48639/udp   mountd
    |   100021  1,3,4      40190/tcp   nlockmgr
    |   100021  1,3,4      56490/udp   nlockmgr
    |   100024  1          43097/tcp   status
    |*  100024  1          54226/udp   status
    139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    3306/tcp open  mysql?
    5900/tcp open  vnc         VNC (protocol 3.3)
    OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
    No OS matches for host
    Service Info: Host:  webserver.localdomain; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Host script results:
    |_smb-vuln-ms10-054: false
    |_smb-vuln-ms10-061: false
    |_smb-vuln-regsvc-dos: ERROR: Script execution failed (use -d to debug)

# 192.168.56.175 - Ubuntu - "Production Server:Bootcamp"

    Nmap scan report for 192.168.56.106
    Host is up (0.0041s latency).
    Not shown: 64536 closed tcp ports (reset), 988 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE     VERSION
    21/tcp   open  ftp         vsftpd 2.3.4
    | vulners: 
    |   vsftpd 2.3.4: 
    |     	PACKETSTORM:162145	10.0	https://vulners.com/packetstorm/PACKETSTORM:162145	*EXPLOIT*
    |     	EDB-ID:49757	10.0	https://vulners.com/exploitdb/EDB-ID:49757	*EXPLOIT*
    |     	E9B0AEBB-5138-50BF-8922-2D87E3C046DD	10.0	https://vulners.com/githubexploit/E9B0AEBB-5138-50BF-8922-2D87E3C046DD	*EXPLOIT*
    |     	E356CCEC-7C81-5A77-8CE4-87DF4DB21897	10.0	https://vulners.com/githubexploit/E356CCEC-7C81-5A77-8CE4-87DF4DB21897	*EXPLOIT*
    |     	D0DBA05F-750F-5F9B-9C69-65E8FA6977D5	10.0	https://vulners.com/githubexploit/D0DBA05F-750F-5F9B-9C69-65E8FA6977D5	*EXPLOIT*
    |     	CVE-2011-2523	10.0	https://vulners.com/cve/CVE-2011-2523
    |     	CNVD-2020-46837	10.0	https://vulners.com/cnvd/CNVD-2020-46837
    |     	CC3F6C15-182F-53F6-A5CC-812D37F1F047	10.0	https://vulners.com/githubexploit/CC3F6C15-182F-53F6-A5CC-812D37F1F047	*EXPLOIT*
    |     	BEE67BEA-45C2-50C0-88F3-9A2E7CC2DECE	10.0	https://vulners.com/githubexploit/BEE67BEA-45C2-50C0-88F3-9A2E7CC2DECE	*EXPLOIT*
    |     	A41B5EAD-1A4C-56A6-97C6-1C58A1CF1E3B	10.0	https://vulners.com/githubexploit/A41B5EAD-1A4C-56A6-97C6-1C58A1CF1E3B	*EXPLOIT*
    |     	9B4BA341-1CBF-59D6-AA40-33596997F23B	10.0	https://vulners.com/githubexploit/9B4BA341-1CBF-59D6-AA40-33596997F23B	*EXPLOIT*
    |     	817CD8FE-87C4-5FE8-B9B2-8CC64333A3F3	10.0	https://vulners.com/githubexploit/817CD8FE-87C4-5FE8-B9B2-8CC64333A3F3	*EXPLOIT*
    |     	63A5C9A7-C241-5E83-9EE6-ABAB44BDD270	10.0	https://vulners.com/githubexploit/63A5C9A7-C241-5E83-9EE6-ABAB44BDD270	*EXPLOIT*
    |     	5F4BCEDE-77DF-5D54-851A-0AE8B76458D9	10.0	https://vulners.com/githubexploit/5F4BCEDE-77DF-5D54-851A-0AE8B76458D9	*EXPLOIT*
    |     	59BAFDCD-5027-5C82-BC59-FC7625DD81DB	10.0	https://vulners.com/githubexploit/59BAFDCD-5027-5C82-BC59-FC7625DD81DB	*EXPLOIT*
    |     	50580586-73C4-5097-81CA-546D6591DF44	10.0	https://vulners.com/githubexploit/50580586-73C4-5097-81CA-546D6591DF44	*EXPLOIT*
    |     	4D01A3A1-75C7-5730-8C5D-B2EC1F56532F	10.0	https://vulners.com/githubexploit/4D01A3A1-75C7-5730-8C5D-B2EC1F56532F	*EXPLOIT*
    |     	344AF37C-35F5-5A70-83E4-B89507233DC0	10.0	https://vulners.com/githubexploit/344AF37C-35F5-5A70-83E4-B89507233DC0	*EXPLOIT*
    |     	322DD1ED-D331-573E-9AAC-5B6BEC2095F9	10.0	https://vulners.com/githubexploit/322DD1ED-D331-573E-9AAC-5B6BEC2095F9	*EXPLOIT*
    |     	23DBF7D8-DD32-5D15-8D18-0CF069745409	10.0	https://vulners.com/githubexploit/23DBF7D8-DD32-5D15-8D18-0CF069745409	*EXPLOIT*
    |     	09B89183-FE26-5690-A12C-7BEC34B1AAE4	10.0	https://vulners.com/githubexploit/09B89183-FE26-5690-A12C-7BEC34B1AAE4	*EXPLOIT*
    |_    	1337DAY-ID-36095	9.8	https://vulners.com/zdt/1337DAY-ID-36095	*EXPLOIT*
    | ftp-vsftpd-backdoor: 
    |   VULNERABLE:
    |   vsFTPd version 2.3.4 backdoor
    |     State: VULNERABLE (Exploitable)
    |     IDs:  CVE:CVE-2011-2523  BID:48539
    |       vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
    |     Disclosure date: 2011-07-03
    |     Exploit results:
    |       Shell command: id
    |       Results: uid=0(root) gid=0(root)
    |     References:
    |       https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb
    |       http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html
    |       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2523
    |_      https://www.securityfocus.com/bid/48539
    22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
    | vulners: 
    |   cpe:/a:openbsd:openssh:4.7p1: 
    |     	DF059135-2CF5-5441-8F22-E6EF1DEE5F6E	10.0	https://vulners.com/gitee/DF059135-2CF5-5441-8F22-E6EF1DEE5F6E	*EXPLOIT*
    |     	PACKETSTORM:173661	9.8	https://vulners.com/packetstorm/PACKETSTORM:173661	*EXPLOIT*
    |     	F0979183-AE88-53B4-86CF-3AF0523F3807	9.8	https://vulners.com/githubexploit/F0979183-AE88-53B4-86CF-3AF0523F3807	*EXPLOIT*
    |     	CVE-2023-38408	9.8	https://vulners.com/cve/CVE-2023-38408
    |     	CVE-2016-1908	9.8	https://vulners.com/cve/CVE-2016-1908
    |     	CVE-2010-4478	9.8	https://vulners.com/cve/CVE-2010-4478
    |     	CEF8EC43-BFE2-5B5E-8918-54A90DA092B4	9.8	https://vulners.com/githubexploit/CEF8EC43-BFE2-5B5E-8918-54A90DA092B4	*EXPLOIT*
    |     	B8190CDB-3EB9-5631-9828-8064A1575B23	9.8	https://vulners.com/githubexploit/B8190CDB-3EB9-5631-9828-8064A1575B23	*EXPLOIT*
    |     	A2B36B85-C737-548F-8C04-9339EDCDBFF5	9.8	https://vulners.com/githubexploit/A2B36B85-C737-548F-8C04-9339EDCDBFF5	*EXPLOIT*
    |     	8FC9C5AB-3968-5F3C-825E-E8DB5379A623	9.8	https://vulners.com/githubexploit/8FC9C5AB-3968-5F3C-825E-E8DB5379A623	*EXPLOIT*
    |     	8AD01159-548E-546E-AA87-2DE89F3927EC	9.8	https://vulners.com/githubexploit/8AD01159-548E-546E-AA87-2DE89F3927EC	*EXPLOIT*
    |     	6192C35D-F78B-5C0A-AB8D-9826A79A5320	9.8	https://vulners.com/githubexploit/6192C35D-F78B-5C0A-AB8D-9826A79A5320	*EXPLOIT*
    |     	2227729D-6700-5C8F-8930-1EEAFD4B9FF0	9.8	https://vulners.com/githubexploit/2227729D-6700-5C8F-8930-1EEAFD4B9FF0	*EXPLOIT*
    |     	0221525F-07F5-5790-912D-F4B9E2D1B587	9.8	https://vulners.com/githubexploit/0221525F-07F5-5790-912D-F4B9E2D1B587	*EXPLOIT*
    |     	CVE-2015-5600	8.5	https://vulners.com/cve/CVE-2015-5600
    |     	CVE-2026-35414	8.1	https://vulners.com/cve/CVE-2026-35414
    |     	CVE-2026-35386	8.1	https://vulners.com/cve/CVE-2026-35386
    |     	CVE-2026-35385	8.1	https://vulners.com/cve/CVE-2026-35385
    |     	BA3887BD-F579-53B1-A4A4-FF49E953E1C0	8.1	https://vulners.com/githubexploit/BA3887BD-F579-53B1-A4A4-FF49E953E1C0	*EXPLOIT*
    |     	4FB01B00-F993-5CAF-BD57-D7E290D10C1F	8.1	https://vulners.com/githubexploit/4FB01B00-F993-5CAF-BD57-D7E290D10C1F	*EXPLOIT*
    |     	PACKETSTORM:140070	7.8	https://vulners.com/packetstorm/PACKETSTORM:140070	*EXPLOIT*
    |     	PACKETSTORM:101052	7.8	https://vulners.com/packetstorm/PACKETSTORM:101052	*EXPLOIT*
    |     	EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09	7.8	https://vulners.com/exploitpack/EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09	*EXPLOIT*
    |     	EDB-ID:40888	7.8	https://vulners.com/exploitdb/EDB-ID:40888	*EXPLOIT*
    |     	CVE-2020-15778	7.8	https://vulners.com/cve/CVE-2020-15778
    |     	CVE-2016-6515	7.8	https://vulners.com/cve/CVE-2016-6515
    |     	CVE-2016-10012	7.8	https://vulners.com/cve/CVE-2016-10012
    |     	CVE-2015-8325	7.8	https://vulners.com/cve/CVE-2015-8325
    |     	C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3	7.8	https://vulners.com/githubexploit/C94132FD-1FA5-5342-B6EE-0DAF45EEFFE3	*EXPLOIT*
    |     	C892A90E-C1D1-5A54-BFAA-046266448553	7.8	https://vulners.com/githubexploit/C892A90E-C1D1-5A54-BFAA-046266448553	*EXPLOIT*
    |     	99C4CA40-30C8-5A34-B3A3-4B5E7A9E16BA	7.8	https://vulners.com/githubexploit/99C4CA40-30C8-5A34-B3A3-4B5E7A9E16BA	*EXPLOIT*
    |     	991D2CC4-0E09-5745-97A2-4917461BD6EC	7.8	https://vulners.com/githubexploit/991D2CC4-0E09-5745-97A2-4917461BD6EC	*EXPLOIT*
    |     	4F1BA9CA-CAB4-55F4-A857-3E4C94C93483	7.8	https://vulners.com/githubexploit/4F1BA9CA-CAB4-55F4-A857-3E4C94C93483	*EXPLOIT*
    |     	312165E3-7FD9-5769-BDA3-4129BE9114D6	7.8	https://vulners.com/githubexploit/312165E3-7FD9-5769-BDA3-4129BE9114D6	*EXPLOIT*
    |     	2E719186-2FED-58A8-A150-762EFBAAA523	7.8	https://vulners.com/gitee/2E719186-2FED-58A8-A150-762EFBAAA523	*EXPLOIT*
    |     	23CC97BE-7C95-513B-9E73-298C48D74432	7.8	https://vulners.com/githubexploit/23CC97BE-7C95-513B-9E73-298C48D74432	*EXPLOIT*
    |     	1337DAY-ID-26494	7.8	https://vulners.com/zdt/1337DAY-ID-26494	*EXPLOIT*
    |     	10213DBE-F683-58BB-B6D3-353173626207	7.8	https://vulners.com/githubexploit/10213DBE-F683-58BB-B6D3-353173626207	*EXPLOIT*
    |     	SSV:92579	7.5	https://vulners.com/seebug/SSV:92579	*EXPLOIT*
    |     	SSV:61450	7.5	https://vulners.com/seebug/SSV:61450	*EXPLOIT*
    |     	CVE-2016-10708	7.5	https://vulners.com/cve/CVE-2016-10708
    |     	CVE-2016-10009	7.5	https://vulners.com/cve/CVE-2016-10009
    |     	CVE-2014-1692	7.5	https://vulners.com/cve/CVE-2014-1692
    |     	CVE-2010-5107	7.5	https://vulners.com/cve/CVE-2010-5107
    |     	CF52FA19-B5DB-5D14-B50F-2411851976E2	7.5	https://vulners.com/githubexploit/CF52FA19-B5DB-5D14-B50F-2411851976E2	*EXPLOIT*
    |     	1337DAY-ID-26576	7.5	https://vulners.com/zdt/1337DAY-ID-26576	*EXPLOIT*
    |     	SSV:92582	7.2	https://vulners.com/seebug/SSV:92582	*EXPLOIT*
    |     	CVE-2016-10010	7.0	https://vulners.com/cve/CVE-2016-10010
    |     	CVE-2015-6564	7.0	https://vulners.com/cve/CVE-2015-6564
    |     	SSV:92580	6.9	https://vulners.com/seebug/SSV:92580	*EXPLOIT*
    |     	1337DAY-ID-26577	6.9	https://vulners.com/zdt/1337DAY-ID-26577	*EXPLOIT*
    |     	EDB-ID:46516	6.8	https://vulners.com/exploitdb/EDB-ID:46516	*EXPLOIT*
    |     	EDB-ID:46193	6.8	https://vulners.com/exploitdb/EDB-ID:46193	*EXPLOIT*
    |     	CVE-2019-6110	6.8	https://vulners.com/cve/CVE-2019-6110
    |     	CVE-2019-6109	6.8	https://vulners.com/cve/CVE-2019-6109
    |     	1337DAY-ID-32328	6.8	https://vulners.com/zdt/1337DAY-ID-32328	*EXPLOIT*
    |     	1337DAY-ID-32009	6.8	https://vulners.com/zdt/1337DAY-ID-32009	*EXPLOIT*
    |     	D104D2BF-ED22-588B-A9B2-3CCC562FE8C0	6.5	https://vulners.com/githubexploit/D104D2BF-ED22-588B-A9B2-3CCC562FE8C0	*EXPLOIT*
    |     	CVE-2026-35387	6.5	https://vulners.com/cve/CVE-2026-35387
    |     	CVE-2023-51385	6.5	https://vulners.com/cve/CVE-2023-51385
    |     	CVE-2014-2653	6.5	https://vulners.com/cve/CVE-2014-2653
    |     	CVE-2012-0814	6.5	https://vulners.com/cve/CVE-2012-0814
    |     	CVE-2008-1657	6.5	https://vulners.com/cve/CVE-2008-1657
    |     	C07ADB46-24B8-57B7-B375-9C761F4750A2	6.5	https://vulners.com/githubexploit/C07ADB46-24B8-57B7-B375-9C761F4750A2	*EXPLOIT*
    |     	A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C	6.5	https://vulners.com/githubexploit/A88CDD3E-67CC-51CC-97FB-AB0CACB6B08C	*EXPLOIT*
    |     	65B15AA1-2A8D-53C1-9499-69EBA3619F1C	6.5	https://vulners.com/githubexploit/65B15AA1-2A8D-53C1-9499-69EBA3619F1C	*EXPLOIT*
    |     	5325A9D6-132B-590C-BDEF-0CB105252732	6.5	https://vulners.com/gitee/5325A9D6-132B-590C-BDEF-0CB105252732	*EXPLOIT*
    |     	530326CF-6AB3-5643-AA16-73DC8CB44742	6.5	https://vulners.com/githubexploit/530326CF-6AB3-5643-AA16-73DC8CB44742	*EXPLOIT*
    |     	EDB-ID:40858	6.4	https://vulners.com/exploitdb/EDB-ID:40858	*EXPLOIT*
    |     	EDB-ID:40119	6.4	https://vulners.com/exploitdb/EDB-ID:40119	*EXPLOIT*
    |     	EDB-ID:39569	6.4	https://vulners.com/exploitdb/EDB-ID:39569	*EXPLOIT*
    |     	CVE-2016-3115	6.4	https://vulners.com/cve/CVE-2016-3115
    |     	CVE-2015-6563	6.4	https://vulners.com/cve/CVE-2015-6563
    |     	CVE-2016-10011	6.2	https://vulners.com/cve/CVE-2016-10011
    |     	PACKETSTORM:181223	5.9	https://vulners.com/packetstorm/PACKETSTORM:181223	*EXPLOIT*
    |     	MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS-	5.9	https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS-	*EXPLOIT*
    |     	FEF0EB06-770B-5ADF-857C-1704B7AC3FE4	5.9	https://vulners.com/githubexploit/FEF0EB06-770B-5ADF-857C-1704B7AC3FE4	*EXPLOIT*
    |     	FD2E0EBA-ED84-5304-8862-84BCDEB2F288	5.9	https://vulners.com/githubexploit/FD2E0EBA-ED84-5304-8862-84BCDEB2F288	*EXPLOIT*
    |     	EDB-ID:45939	5.9	https://vulners.com/exploitdb/EDB-ID:45939	*EXPLOIT*
    |     	EDB-ID:45233	5.9	https://vulners.com/exploitdb/EDB-ID:45233	*EXPLOIT*
    |     	EDB-ID:40136	5.9	https://vulners.com/exploitdb/EDB-ID:40136	*EXPLOIT*
    |     	EDB-ID:40113	5.9	https://vulners.com/exploitdb/EDB-ID:40113	*EXPLOIT*
    |     	CVE-2023-48795	5.9	https://vulners.com/cve/CVE-2023-48795
    |     	CVE-2019-6111	5.9	https://vulners.com/cve/CVE-2019-6111
    |     	CVE-2018-15473	5.9	https://vulners.com/cve/CVE-2018-15473
    |     	CVE-2016-6210	5.9	https://vulners.com/cve/CVE-2016-6210
    |     	A4C45A40-ADC5-50EF-8FFC-4047AA0F987B	5.9	https://vulners.com/githubexploit/A4C45A40-ADC5-50EF-8FFC-4047AA0F987B	*EXPLOIT*
    |     	A02ABE85-E4E3-5852-A59D-DF288CB8160A	5.9	https://vulners.com/githubexploit/A02ABE85-E4E3-5852-A59D-DF288CB8160A	*EXPLOIT*
    |     	721F040C-37BC-59E1-9433-01A2EAC2E755	5.9	https://vulners.com/githubexploit/721F040C-37BC-59E1-9433-01A2EAC2E755	*EXPLOIT*
    |     	SSV:61911	5.8	https://vulners.com/seebug/SSV:61911	*EXPLOIT*
    |     	EXPLOITPACK:98FE96309F9524B8C84C508837551A19	5.8	https://vulners.com/exploitpack/EXPLOITPACK:98FE96309F9524B8C84C508837551A19	*EXPLOIT*
    |     	EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	5.8	https://vulners.com/exploitpack/EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97	*EXPLOIT*
    |     	CVE-2014-2532	5.8	https://vulners.com/cve/CVE-2014-2532
    |     	SSV:91041	5.5	https://vulners.com/seebug/SSV:91041	*EXPLOIT*
    |     	PACKETSTORM:140019	5.5	https://vulners.com/packetstorm/PACKETSTORM:140019	*EXPLOIT*
    |     	PACKETSTORM:136251	5.5	https://vulners.com/packetstorm/PACKETSTORM:136251	*EXPLOIT*
    |     	PACKETSTORM:136234	5.5	https://vulners.com/packetstorm/PACKETSTORM:136234	*EXPLOIT*
    |     	EXPLOITPACK:F92411A645D85F05BDBD274FD222226F	5.5	https://vulners.com/exploitpack/EXPLOITPACK:F92411A645D85F05BDBD274FD222226F	*EXPLOIT*
    |     	EXPLOITPACK:9F2E746846C3C623A27A441281EAD138	5.5	https://vulners.com/exploitpack/EXPLOITPACK:9F2E746846C3C623A27A441281EAD138	*EXPLOIT*
    |     	EXPLOITPACK:1902C998CBF9154396911926B4C3B330	5.5	https://vulners.com/exploitpack/EXPLOITPACK:1902C998CBF9154396911926B4C3B330	*EXPLOIT*
    |     	CVE-2011-4327	5.5	https://vulners.com/cve/CVE-2011-4327
    |     	1337DAY-ID-25388	5.5	https://vulners.com/zdt/1337DAY-ID-25388	*EXPLOIT*
    |     	FD18B68B-C0A6-562E-A8C8-781B225F15B0	5.3	https://vulners.com/githubexploit/FD18B68B-C0A6-562E-A8C8-781B225F15B0	*EXPLOIT*
    |     	E9EC0911-E2E1-52A7-B2F4-D0065C6A3057	5.3	https://vulners.com/githubexploit/E9EC0911-E2E1-52A7-B2F4-D0065C6A3057	*EXPLOIT*
    |     	CVE-2018-20685	5.3	https://vulners.com/cve/CVE-2018-20685
    |     	CVE-2017-15906	5.3	https://vulners.com/cve/CVE-2017-15906
    |     	CVE-2016-20012	5.3	https://vulners.com/cve/CVE-2016-20012
    |     	CNVD-2018-20962	5.3	https://vulners.com/cnvd/CNVD-2018-20962
    |     	CNVD-2018-20960	5.3	https://vulners.com/cnvd/CNVD-2018-20960
    |     	A9E6F50E-E7FC-51D0-9C93-A43461469FA2	5.3	https://vulners.com/githubexploit/A9E6F50E-E7FC-51D0-9C93-A43461469FA2	*EXPLOIT*
    |     	A801235B-9835-5BA8-B8FE-23B7FFCABD66	5.3	https://vulners.com/githubexploit/A801235B-9835-5BA8-B8FE-23B7FFCABD66	*EXPLOIT*
    |     	8DD1D813-FD5A-5B26-867A-CE7CAC9FEEDF	5.3	https://vulners.com/gitee/8DD1D813-FD5A-5B26-867A-CE7CAC9FEEDF	*EXPLOIT*
    |     	4F2FBB06-E601-5EAD-9679-3395D24057DD	5.3	https://vulners.com/githubexploit/4F2FBB06-E601-5EAD-9679-3395D24057DD	*EXPLOIT*
    |     	486BB6BC-9C26-597F-B865-D0E904FDA984	5.3	https://vulners.com/githubexploit/486BB6BC-9C26-597F-B865-D0E904FDA984	*EXPLOIT*
    |     	2385176A-820F-5469-AB09-C340264F2B2F	5.3	https://vulners.com/gitee/2385176A-820F-5469-AB09-C340264F2B2F	*EXPLOIT*
    |     	1337DAY-ID-31730	5.3	https://vulners.com/zdt/1337DAY-ID-31730	*EXPLOIT*
    |     	SSV:60656	5.0	https://vulners.com/seebug/SSV:60656	*EXPLOIT*
    |     	SSH_ENUM	5.0	https://vulners.com/canvas/SSH_ENUM	*EXPLOIT*
    |     	PACKETSTORM:150621	5.0	https://vulners.com/packetstorm/PACKETSTORM:150621	*EXPLOIT*
    |     	EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0	5.0	https://vulners.com/exploitpack/EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0	*EXPLOIT*
    |     	EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283	5.0	https://vulners.com/exploitpack/EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283	*EXPLOIT*
    |     	EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF	4.3	https://vulners.com/exploitpack/EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF	*EXPLOIT*
    |     	EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF	4.3	https://vulners.com/exploitpack/EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF	*EXPLOIT*
    |     	CVE-2015-5352	4.3	https://vulners.com/cve/CVE-2015-5352
    |     	1337DAY-ID-25440	4.3	https://vulners.com/zdt/1337DAY-ID-25440	*EXPLOIT*
    |     	1337DAY-ID-25438	4.3	https://vulners.com/zdt/1337DAY-ID-25438	*EXPLOIT*
    |     	CVE-2010-4755	4.0	https://vulners.com/cve/CVE-2010-4755
    |     	CVE-2021-36368	3.7	https://vulners.com/cve/CVE-2021-36368
    |     	CVE-2025-61985	3.6	https://vulners.com/cve/CVE-2025-61985
    |     	CVE-2025-61984	3.6	https://vulners.com/cve/CVE-2025-61984
    |     	B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150	3.6	https://vulners.com/githubexploit/B7EACB4F-A5CF-5C5A-809F-E03CCE2AB150	*EXPLOIT*
    |     	4C6E2182-0E99-5626-83F6-1646DD648C57	3.6	https://vulners.com/githubexploit/4C6E2182-0E99-5626-83F6-1646DD648C57	*EXPLOIT*
    |     	CVE-2011-5000	3.5	https://vulners.com/cve/CVE-2011-5000
    |     	CVE-2026-35388	2.5	https://vulners.com/cve/CVE-2026-35388
    |     	SSV:92581	2.1	https://vulners.com/seebug/SSV:92581	*EXPLOIT*
    |     	CVE-2008-3259	1.2	https://vulners.com/cve/CVE-2008-3259
    |     	PACKETSTORM:151227	0.0	https://vulners.com/packetstorm/PACKETSTORM:151227	*EXPLOIT*
    |     	PACKETSTORM:140261	0.0	https://vulners.com/packetstorm/PACKETSTORM:140261	*EXPLOIT*
    |     	PACKETSTORM:138006	0.0	https://vulners.com/packetstorm/PACKETSTORM:138006	*EXPLOIT*
    |     	PACKETSTORM:137942	0.0	https://vulners.com/packetstorm/PACKETSTORM:137942	*EXPLOIT*
    |     	1337DAY-ID-30937	0.0	https://vulners.com/zdt/1337DAY-ID-30937	*EXPLOIT*
    |     	1337DAY-ID-26468	0.0	https://vulners.com/zdt/1337DAY-ID-26468	*EXPLOIT*
    |_    	1337DAY-ID-25391	0.0	https://vulners.com/zdt/1337DAY-ID-25391	*EXPLOIT*
    23/tcp   open  telnet?
    25/tcp   open  smtp        Postfix smtpd
    | smtp-vuln-cve2010-4344: 
    |_  The SMTP server is not Exim: NOT VULNERABLE
    53/tcp   open  domain      ISC BIND 9.4.2
    | vulners: 
    |   cpe:/a:isc:bind:9.4.2: 
    |     	SSV:2853	10.0	https://vulners.com/seebug/SSV:2853	*EXPLOIT*
    |     	CVE-2008-0122	10.0	https://vulners.com/cve/CVE-2008-0122
    |     	CVE-2021-25216	9.8	https://vulners.com/cve/CVE-2021-25216
    |     	CVE-2020-8616	8.6	https://vulners.com/cve/CVE-2020-8616
    |     	CVE-2016-1286	8.6	https://vulners.com/cve/CVE-2016-1286
    |     	CNVD-2020-34454	8.6	https://vulners.com/cnvd/CNVD-2020-34454
    |     	SSV:60184	8.5	https://vulners.com/seebug/SSV:60184	*EXPLOIT*
    |     	CVE-2012-1667	8.5	https://vulners.com/cve/CVE-2012-1667
    |     	SSV:60292	7.8	https://vulners.com/seebug/SSV:60292	*EXPLOIT*
    |     	PACKETSTORM:180552	7.8	https://vulners.com/packetstorm/PACKETSTORM:180552	*EXPLOIT*
    |     	PACKETSTORM:180551	7.8	https://vulners.com/packetstorm/PACKETSTORM:180551	*EXPLOIT*
    |     	PACKETSTORM:138960	7.8	https://vulners.com/packetstorm/PACKETSTORM:138960	*EXPLOIT*
    |     	PACKETSTORM:132926	7.8	https://vulners.com/packetstorm/PACKETSTORM:132926	*EXPLOIT*
    |     	MSF:AUXILIARY-DOS-DNS-BIND_TKEY-	7.8	https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TKEY-	*EXPLOIT*
    |     	EXPLOITPACK:BE4F638B632EA0754155A27ECC4B3D3F	7.8	https://vulners.com/exploitpack/EXPLOITPACK:BE4F638B632EA0754155A27ECC4B3D3F	*EXPLOIT*
    |     	EXPLOITPACK:46DEBFAC850194C04C54F93E0DFF5F4F	7.8	https://vulners.com/exploitpack/EXPLOITPACK:46DEBFAC850194C04C54F93E0DFF5F4F	*EXPLOIT*
    |     	EXPLOITPACK:09762DB0197BBAAAB6FC79F24F0D2A74	7.8	https://vulners.com/exploitpack/EXPLOITPACK:09762DB0197BBAAAB6FC79F24F0D2A74	*EXPLOIT*
    |     	EDB-ID:42121	7.8	https://vulners.com/exploitdb/EDB-ID:42121	*EXPLOIT*
    |     	EDB-ID:40453	7.8	https://vulners.com/exploitdb/EDB-ID:40453	*EXPLOIT*
    |     	EDB-ID:37723	7.8	https://vulners.com/exploitdb/EDB-ID:37723	*EXPLOIT*
    |     	EDB-ID:37721	7.8	https://vulners.com/exploitdb/EDB-ID:37721	*EXPLOIT*
    |     	E183E822-9005-5F4E-B024-D9C4761AE308	7.8	https://vulners.com/githubexploit/E183E822-9005-5F4E-B024-D9C4761AE308	*EXPLOIT*
    |     	CVE-2017-3141	7.8	https://vulners.com/cve/CVE-2017-3141
    |     	CVE-2016-2776	7.8	https://vulners.com/cve/CVE-2016-2776
    |     	CVE-2015-5722	7.8	https://vulners.com/cve/CVE-2015-5722
    |     	CVE-2015-5477	7.8	https://vulners.com/cve/CVE-2015-5477
    |     	CVE-2014-8500	7.8	https://vulners.com/cve/CVE-2014-8500
    |     	CVE-2012-5166	7.8	https://vulners.com/cve/CVE-2012-5166
    |     	CVE-2012-4244	7.8	https://vulners.com/cve/CVE-2012-4244
    |     	CVE-2012-3817	7.8	https://vulners.com/cve/CVE-2012-3817
    |     	CVE-2008-4163	7.8	https://vulners.com/cve/CVE-2008-4163
    |     	7459D6A0-D6CA-5CD2-A484-5DD984C0E5E4	7.8	https://vulners.com/githubexploit/7459D6A0-D6CA-5CD2-A484-5DD984C0E5E4	*EXPLOIT*
    |     	673990FE-C5D5-5501-A342-D1AEC9F2A871	7.8	https://vulners.com/githubexploit/673990FE-C5D5-5501-A342-D1AEC9F2A871	*EXPLOIT*
    |     	1337DAY-ID-25325	7.8	https://vulners.com/zdt/1337DAY-ID-25325	*EXPLOIT*
    |     	1337DAY-ID-23970	7.8	https://vulners.com/zdt/1337DAY-ID-23970	*EXPLOIT*
    |     	1337DAY-ID-23960	7.8	https://vulners.com/zdt/1337DAY-ID-23960	*EXPLOIT*
    |     	1337DAY-ID-23948	7.8	https://vulners.com/zdt/1337DAY-ID-23948	*EXPLOIT*
    |     	CVE-2010-0382	7.6	https://vulners.com/cve/CVE-2010-0382
    |     	PACKETSTORM:180550	7.5	https://vulners.com/packetstorm/PACKETSTORM:180550	*EXPLOIT*
    |     	MSF:AUXILIARY-DOS-DNS-BIND_TSIG_BADTIME-	7.5	https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TSIG_BADTIME-	*EXPLOIT*
    |     	MSF:AUXILIARY-DOS-DNS-BIND_TSIG-	7.5	https://vulners.com/metasploit/MSF:AUXILIARY-DOS-DNS-BIND_TSIG-	*EXPLOIT*
    |     	FBC03933-7A65-52F3-83F4-4B2253A490B6	7.5	https://vulners.com/githubexploit/FBC03933-7A65-52F3-83F4-4B2253A490B6	*EXPLOIT*
    |     	CVE-2026-3039	7.5	https://vulners.com/cve/CVE-2026-3039
    |     	CVE-2023-50868	7.5	https://vulners.com/cve/CVE-2023-50868
    |     	CVE-2023-50387	7.5	https://vulners.com/cve/CVE-2023-50387
    |     	CVE-2023-4408	7.5	https://vulners.com/cve/CVE-2023-4408
    |     	CVE-2023-3341	7.5	https://vulners.com/cve/CVE-2023-3341
    |     	CVE-2021-25215	7.5	https://vulners.com/cve/CVE-2021-25215
    |     	CVE-2020-8617	7.5	https://vulners.com/cve/CVE-2020-8617
    |     	CVE-2017-3145	7.5	https://vulners.com/cve/CVE-2017-3145
    |     	CVE-2017-3143	7.5	https://vulners.com/cve/CVE-2017-3143
    |     	CVE-2016-9444	7.5	https://vulners.com/cve/CVE-2016-9444
    |     	CVE-2016-9131	7.5	https://vulners.com/cve/CVE-2016-9131
    |     	CVE-2016-8864	7.5	https://vulners.com/cve/CVE-2016-8864
    |     	CVE-2016-2848	7.5	https://vulners.com/cve/CVE-2016-2848
    |     	CVE-2009-0265	7.5	https://vulners.com/cve/CVE-2009-0265
    |     	CNVD-2017-12537	7.5	https://vulners.com/cnvd/CNVD-2017-12537
    |     	9ED8A03D-FE34-5F77-8C66-C03C9615AF07	7.5	https://vulners.com/gitee/9ED8A03D-FE34-5F77-8C66-C03C9615AF07	*EXPLOIT*
    |     	1337DAY-ID-34485	7.5	https://vulners.com/zdt/1337DAY-ID-34485	*EXPLOIT*
    |     	EXPLOITPACK:D6DDF5E24DE171DAAD71FD95FC1B67F2	7.2	https://vulners.com/exploitpack/EXPLOITPACK:D6DDF5E24DE171DAAD71FD95FC1B67F2	*EXPLOIT*
    |     	CVE-2015-8461	7.1	https://vulners.com/cve/CVE-2015-8461
    |     	CVE-2015-5986	7.1	https://vulners.com/cve/CVE-2015-5986
    |     	CVE-2015-8705	7.0	https://vulners.com/cve/CVE-2015-8705
    |     	CVE-2016-1285	6.8	https://vulners.com/cve/CVE-2016-1285
    |     	CVE-2015-8704	6.8	https://vulners.com/cve/CVE-2015-8704
    |     	CVE-2009-0025	6.8	https://vulners.com/cve/CVE-2009-0025
    |     	CVE-2020-8622	6.5	https://vulners.com/cve/CVE-2020-8622
    |     	CVE-2018-5741	6.5	https://vulners.com/cve/CVE-2018-5741
    |     	CVE-2016-6170	6.5	https://vulners.com/cve/CVE-2016-6170
    |     	CVE-2010-3614	6.4	https://vulners.com/cve/CVE-2010-3614
    |     	CVE-2016-2775	5.9	https://vulners.com/cve/CVE-2016-2775
    |     	CVE-2022-2795	5.3	https://vulners.com/cve/CVE-2022-2795
    |     	CVE-2021-25219	5.3	https://vulners.com/cve/CVE-2021-25219
    |     	CVE-2017-3142	5.3	https://vulners.com/cve/CVE-2017-3142
    |     	CNVD-2024-16843	5.3	https://vulners.com/cnvd/CNVD-2024-16843
    |     	SSV:30099	5.0	https://vulners.com/seebug/SSV:30099	*EXPLOIT*
    |     	SSV:20595	5.0	https://vulners.com/seebug/SSV:20595	*EXPLOIT*
    |     	PACKETSTORM:157836	5.0	https://vulners.com/packetstorm/PACKETSTORM:157836	*EXPLOIT*
    |     	CVE-2015-8000	5.0	https://vulners.com/cve/CVE-2015-8000
    |     	CVE-2012-1033	5.0	https://vulners.com/cve/CVE-2012-1033
    |     	CVE-2011-4313	5.0	https://vulners.com/cve/CVE-2011-4313
    |     	CVE-2011-1910	5.0	https://vulners.com/cve/CVE-2011-1910
    |     	SSV:11919	4.3	https://vulners.com/seebug/SSV:11919	*EXPLOIT*
    |     	CVE-2010-3762	4.3	https://vulners.com/cve/CVE-2010-3762
    |     	CVE-2010-0097	4.3	https://vulners.com/cve/CVE-2010-0097
    |     	CVE-2009-0696	4.3	https://vulners.com/cve/CVE-2009-0696
    |     	CVE-2010-0290	4.0	https://vulners.com/cve/CVE-2010-0290
    |     	SSV:14986	2.6	https://vulners.com/seebug/SSV:14986	*EXPLOIT*
    |     	CVE-2009-4022	2.6	https://vulners.com/cve/CVE-2009-4022
    |     	PACKETSTORM:142800	0.0	https://vulners.com/packetstorm/PACKETSTORM:142800	*EXPLOIT*
    |_    	1337DAY-ID-27896	0.0	https://vulners.com/zdt/1337DAY-ID-27896	*EXPLOIT*
    80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
    | vulners: 
    |   cpe:/a:apache:http_server:2.2.8: 
    |     	SSV:69341	10.0	https://vulners.com/seebug/SSV:69341	*EXPLOIT*
    |     	SSV:19282	10.0	https://vulners.com/seebug/SSV:19282	*EXPLOIT*
    |     	SSV:19236	10.0	https://vulners.com/seebug/SSV:19236	*EXPLOIT*
    |     	SSV:11999	10.0	https://vulners.com/seebug/SSV:11999	*EXPLOIT*
    |     	PACKETSTORM:86964	10.0	https://vulners.com/packetstorm/PACKETSTORM:86964	*EXPLOIT*
    |     	PACKETSTORM:180533	10.0	https://vulners.com/packetstorm/PACKETSTORM:180533	*EXPLOIT*
    |     	MSF:AUXILIARY-DOS-HTTP-APACHE_MOD_ISAPI-	10.0	https://vulners.com/metasploit/MSF:AUXILIARY-DOS-HTTP-APACHE_MOD_ISAPI-	*EXPLOIT*
    |     	HTTPD:E74B6F3660D13C4DD05DF3A83EA61631	10.0	https://vulners.com/httpd/HTTPD:E74B6F3660D13C4DD05DF3A83EA61631
    |     	HTTPD:81180E4E634CDECC9784146016B4A949	10.0	https://vulners.com/httpd/HTTPD:81180E4E634CDECC9784146016B4A949
    |     	EXPLOITPACK:30ED468EC8BD5B71B2CB93825A852B80	10.0	https://vulners.com/exploitpack/EXPLOITPACK:30ED468EC8BD5B71B2CB93825A852B80	*EXPLOIT*
    |     	EDB-ID:14288	10.0	https://vulners.com/exploitdb/EDB-ID:14288	*EXPLOIT*
    |     	EDB-ID:11650	10.0	https://vulners.com/exploitdb/EDB-ID:11650	*EXPLOIT*
    |     	CVE-2010-0425	10.0	https://vulners.com/cve/CVE-2010-0425
    |     	3E6BA608-776F-5B1F-9BA5-589CD2A5A351	10.0	https://vulners.com/gitee/3E6BA608-776F-5B1F-9BA5-589CD2A5A351	*EXPLOIT*
    |     	PACKETSTORM:171631	9.8	https://vulners.com/packetstorm/PACKETSTORM:171631	*EXPLOIT*
    |     	HTTPD:E69E9574251973D5AF93FA9D04997FC1	9.8	https://vulners.com/httpd/HTTPD:E69E9574251973D5AF93FA9D04997FC1
    |     	HTTPD:E162D3AE025639FEE2A89D5AF40ABF2F	9.8	https://vulners.com/httpd/HTTPD:E162D3AE025639FEE2A89D5AF40ABF2F
    |     	HTTPD:C072933AA965A86DA3E2C9172FFC1569	9.8	https://vulners.com/httpd/HTTPD:C072933AA965A86DA3E2C9172FFC1569
    |     	HTTPD:A1BBCE110E077FFBF4469D4F06DB9293	9.8	https://vulners.com/httpd/HTTPD:A1BBCE110E077FFBF4469D4F06DB9293
    |     	HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D	9.8	https://vulners.com/httpd/HTTPD:A09F9CEBE0B7C39EDA0480FEAEF4FE9D
    |     	HTTPD:9F5406E0F4A0B007A0A4C9C92EF9813B	9.8	https://vulners.com/httpd/HTTPD:9F5406E0F4A0B007A0A4C9C92EF9813B
    |     	HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8	9.8	https://vulners.com/httpd/HTTPD:9BCBE3C14201AFC4B0F36F15CB40C0F8
    |     	HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E	9.8	https://vulners.com/httpd/HTTPD:2BE0032A6ABE7CC52906DBAAFE0E448E
    |     	EDB-ID:51193	9.8	https://vulners.com/exploitdb/EDB-ID:51193	*EXPLOIT*
    |     	EDB-ID:10579	9.8	https://vulners.com/exploitdb/EDB-ID:10579	*EXPLOIT*
    |     	ECC3E825-EE29-59D3-BE28-1B30DB15940E	9.8	https://vulners.com/githubexploit/ECC3E825-EE29-59D3-BE28-1B30DB15940E	*EXPLOIT*
    |     	D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52	9.8	https://vulners.com/githubexploit/D5084D51-C8DF-5CBA-BC26-ACF2E33F8E52	*EXPLOIT*
    |     	CVE-2026-28780	9.8	https://vulners.com/cve/CVE-2026-28780
    |     	CVE-2024-38476	9.8	https://vulners.com/cve/CVE-2024-38476
    |     	CVE-2022-31813	9.8	https://vulners.com/cve/CVE-2022-31813
    |     	CVE-2022-22720	9.8	https://vulners.com/cve/CVE-2022-22720
    |     	CVE-2021-44790	9.8	https://vulners.com/cve/CVE-2021-44790
    |     	CVE-2021-39275	9.8	https://vulners.com/cve/CVE-2021-39275
    |     	CVE-2018-1312	9.8	https://vulners.com/cve/CVE-2018-1312
    |     	CVE-2017-7679	9.8	https://vulners.com/cve/CVE-2017-7679
    |     	CVE-2017-3169	9.8	https://vulners.com/cve/CVE-2017-3169
    |     	CVE-2017-3167	9.8	https://vulners.com/cve/CVE-2017-3167
    |     	CVE-2009-3555	9.8	https://vulners.com/cve/CVE-2009-3555
    |     	CNVD-2022-51061	9.8	https://vulners.com/cnvd/CNVD-2022-51061
    |     	CNVD-2022-03225	9.8	https://vulners.com/cnvd/CNVD-2022-03225
    |     	CNVD-2021-102386	9.8	https://vulners.com/cnvd/CNVD-2021-102386
    |     	B6297446-2DDD-52BA-B508-29A748A5D2CC	9.8	https://vulners.com/githubexploit/B6297446-2DDD-52BA-B508-29A748A5D2CC	*EXPLOIT*
    |     	1337DAY-ID-38427	9.8	https://vulners.com/zdt/1337DAY-ID-38427	*EXPLOIT*
    |     	0DB60346-03B6-5FEE-93D7-FF5757D225AA	9.8	https://vulners.com/gitee/0DB60346-03B6-5FEE-93D7-FF5757D225AA	*EXPLOIT*
    |     	HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6	9.1	https://vulners.com/httpd/HTTPD:509B04B8CC51879DD0A561AC4FDBE0A6
    |     	HTTPD:459EB8D98503A2460C9445C5B224979E	9.1	https://vulners.com/httpd/HTTPD:459EB8D98503A2460C9445C5B224979E
    |     	HTTPD:2C227652EE0B3B961706AAFCACA3D1E1	9.1	https://vulners.com/httpd/HTTPD:2C227652EE0B3B961706AAFCACA3D1E1
    |     	FD2EE3A5-BAEA-5845-BA35-E6889992214F	9.1	https://vulners.com/githubexploit/FD2EE3A5-BAEA-5845-BA35-E6889992214F	*EXPLOIT*
    |     	FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7	9.1	https://vulners.com/githubexploit/FBC8A8BE-F00A-5B6D-832E-F99A72E7A3F7	*EXPLOIT*
    |     	E606D7F4-5FA2-5907-B30E-367D6FFECD89	9.1	https://vulners.com/githubexploit/E606D7F4-5FA2-5907-B30E-367D6FFECD89	*EXPLOIT*
    |     	D8A19443-2A37-5592-8955-F614504AAF45	9.1	https://vulners.com/githubexploit/D8A19443-2A37-5592-8955-F614504AAF45	*EXPLOIT*
    |     	CVE-2024-40898	9.1	https://vulners.com/cve/CVE-2024-40898
    |     	CVE-2022-28615	9.1	https://vulners.com/cve/CVE-2022-28615
    |     	CVE-2022-22721	9.1	https://vulners.com/cve/CVE-2022-22721
    |     	CVE-2017-9788	9.1	https://vulners.com/cve/CVE-2017-9788
    |     	CNVD-2022-51060	9.1	https://vulners.com/cnvd/CNVD-2022-51060
    |     	CNVD-2022-41638	9.1	https://vulners.com/cnvd/CNVD-2022-41638
    |     	B5E74010-A082-5ECE-AB37-623A5B33FE7D	9.1	https://vulners.com/githubexploit/B5E74010-A082-5ECE-AB37-623A5B33FE7D	*EXPLOIT*
    |     	HTTPD:1B3D546A8500818AAC5B1359FE11A7E4	9.0	https://vulners.com/httpd/HTTPD:1B3D546A8500818AAC5B1359FE11A7E4
    |     	CVE-2021-40438	9.0	https://vulners.com/cve/CVE-2021-40438
    |     	CNVD-2022-03224	9.0	https://vulners.com/cnvd/CNVD-2022-03224
    |     	AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C	9.0	https://vulners.com/githubexploit/AE3EF1CC-A0C3-5CB7-A6EF-4DAAAFA59C8C	*EXPLOIT*
    |     	9D9B3F4D-6B5C-5377-BE39-F1C432C9E457	9.0	https://vulners.com/githubexploit/9D9B3F4D-6B5C-5377-BE39-F1C432C9E457	*EXPLOIT*
    |     	8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	9.0	https://vulners.com/githubexploit/8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	*EXPLOIT*
    |     	7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2	9.0	https://vulners.com/githubexploit/7F48C6CF-47B2-5AF9-B6FD-1735FB2A95B2	*EXPLOIT*
    |     	36618CA8-9316-59CA-B748-82F15F407C4F	9.0	https://vulners.com/githubexploit/36618CA8-9316-59CA-B748-82F15F407C4F	*EXPLOIT*
    |     	CVE-2026-24072	8.8	https://vulners.com/cve/CVE-2026-24072
    |     	40379BCA-07F4-5401-B618-4640793D350D	8.8	https://vulners.com/githubexploit/40379BCA-07F4-5401-B618-4640793D350D	*EXPLOIT*
    |     	CVE-2025-58098	8.3	https://vulners.com/cve/CVE-2025-58098
    |     	CNVD-2021-102387	8.2	https://vulners.com/cnvd/CNVD-2021-102387
    |     	B0A9E5E8-7CCC-5984-9922-A89F11D6BF38	8.2	https://vulners.com/githubexploit/B0A9E5E8-7CCC-5984-9922-A89F11D6BF38	*EXPLOIT*
    |     	HTTPD:30E0EE442FF4843665FED4FBCA25406A	8.1	https://vulners.com/httpd/HTTPD:30E0EE442FF4843665FED4FBCA25406A
    |     	CVE-2016-5387	8.1	https://vulners.com/cve/CVE-2016-5387
    |     	CNVD-2016-04948	8.1	https://vulners.com/cnvd/CNVD-2016-04948
    |     	SSV:72403	7.8	https://vulners.com/seebug/SSV:72403	*EXPLOIT*
    |     	SSV:2820	7.8	https://vulners.com/seebug/SSV:2820	*EXPLOIT*
    |     	SSV:26043	7.8	https://vulners.com/seebug/SSV:26043	*EXPLOIT*
    |     	SSV:20899	7.8	https://vulners.com/seebug/SSV:20899	*EXPLOIT*
    |     	SSV:11569	7.8	https://vulners.com/seebug/SSV:11569	*EXPLOIT*
    |     	PACKETSTORM:180517	7.8	https://vulners.com/packetstorm/PACKETSTORM:180517	*EXPLOIT*
    |     	PACKETSTORM:126851	7.8	https://vulners.com/packetstorm/PACKETSTORM:126851	*EXPLOIT*
    |     	PACKETSTORM:123527	7.8	https://vulners.com/packetstorm/PACKETSTORM:123527	*EXPLOIT*
    |     	PACKETSTORM:122962	7.8	https://vulners.com/packetstorm/PACKETSTORM:122962	*EXPLOIT*
    |     	MSF:AUXILIARY-DOS-HTTP-APACHE_RANGE_DOS-	7.8	https://vulners.com/metasploit/MSF:AUXILIARY-DOS-HTTP-APACHE_RANGE_DOS-	*EXPLOIT*
    |     	HTTPD:556E7FA885F1BEDB6E3D9AAB5665198F	7.8	https://vulners.com/httpd/HTTPD:556E7FA885F1BEDB6E3D9AAB5665198F
    |     	EXPLOITPACK:186B5FCF5C57B52642E62C06BABC6F83	7.8	https://vulners.com/exploitpack/EXPLOITPACK:186B5FCF5C57B52642E62C06BABC6F83	*EXPLOIT*
    |     	EDB-ID:18221	7.8	https://vulners.com/exploitdb/EDB-ID:18221	*EXPLOIT*
    |     	CVE-2011-3192	7.8	https://vulners.com/cve/CVE-2011-3192
    |     	C76F17FD-A21F-5E67-97D8-51A53B9594C1	7.8	https://vulners.com/githubexploit/C76F17FD-A21F-5E67-97D8-51A53B9594C1	*EXPLOIT*
    |     	4F94F3CE-6A41-5E04-A51B-4D22ED6CF210	7.8	https://vulners.com/githubexploit/4F94F3CE-6A41-5E04-A51B-4D22ED6CF210	*EXPLOIT*
    |     	1337DAY-ID-21170	7.8	https://vulners.com/zdt/1337DAY-ID-21170	*EXPLOIT*
    |     	SSV:12673	7.5	https://vulners.com/seebug/SSV:12673	*EXPLOIT*
    |     	SSV:12626	7.5	https://vulners.com/seebug/SSV:12626	*EXPLOIT*
    |     	PACKETSTORM:181038	7.5	https://vulners.com/packetstorm/PACKETSTORM:181038	*EXPLOIT*
    |     	MSF:AUXILIARY-SCANNER-HTTP-APACHE_OPTIONSBLEED-	7.5	https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-HTTP-APACHE_OPTIONSBLEED-	*EXPLOIT*
    |     	HTTPD:F1CFBC9B54DFAD0499179863D36830BB	7.5	https://vulners.com/httpd/HTTPD:F1CFBC9B54DFAD0499179863D36830BB
    |     	HTTPD:C317C7138B4A8BBD54A901D6DDDCB837	7.5	https://vulners.com/httpd/HTTPD:C317C7138B4A8BBD54A901D6DDDCB837
    |     	HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F	7.5	https://vulners.com/httpd/HTTPD:C1F57FDC580B58497A5EC5B7D3749F2F
    |     	HTTPD:C0856723C0FBF5502E1378536B484C09	7.5	https://vulners.com/httpd/HTTPD:C0856723C0FBF5502E1378536B484C09
    |     	HTTPD:BEF84406F2FB3CB90F1C555BEFF774E2	7.5	https://vulners.com/httpd/HTTPD:BEF84406F2FB3CB90F1C555BEFF774E2
    |     	HTTPD:B1B0A31C4AD388CC6C575931414173E2	7.5	https://vulners.com/httpd/HTTPD:B1B0A31C4AD388CC6C575931414173E2
    |     	HTTPD:7DDAAFDB1FD8B2E7FD36ADABA5DB6DAA	7.5	https://vulners.com/httpd/HTTPD:7DDAAFDB1FD8B2E7FD36ADABA5DB6DAA
    |     	HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5	7.5	https://vulners.com/httpd/HTTPD:5E6BCDB2F7C53E4EDCE844709D930AF5
    |     	HTTPD:5227799CC4172DBFA895A4F581F74C11	7.5	https://vulners.com/httpd/HTTPD:5227799CC4172DBFA895A4F581F74C11
    |     	EDB-ID:42745	7.5	https://vulners.com/exploitdb/EDB-ID:42745	*EXPLOIT*
    |     	CVE-2026-34059	7.5	https://vulners.com/cve/CVE-2026-34059
    |     	CVE-2026-29169	7.5	https://vulners.com/cve/CVE-2026-29169
    |     	CVE-2023-31122	7.5	https://vulners.com/cve/CVE-2023-31122
    |     	CVE-2022-30556	7.5	https://vulners.com/cve/CVE-2022-30556
    |     	CVE-2022-29404	7.5	https://vulners.com/cve/CVE-2022-29404
    |     	CVE-2022-22719	7.5	https://vulners.com/cve/CVE-2022-22719
    |     	CVE-2021-34798	7.5	https://vulners.com/cve/CVE-2021-34798
    |     	CVE-2018-8011	7.5	https://vulners.com/cve/CVE-2018-8011
    |     	CVE-2018-1303	7.5	https://vulners.com/cve/CVE-2018-1303
    |     	CVE-2017-9798	7.5	https://vulners.com/cve/CVE-2017-9798
    |     	CVE-2017-15710	7.5	https://vulners.com/cve/CVE-2017-15710
    |     	CVE-2016-8743	7.5	https://vulners.com/cve/CVE-2016-8743
    |     	CVE-2009-2699	7.5	https://vulners.com/cve/CVE-2009-2699
    |     	CVE-2009-1955	7.5	https://vulners.com/cve/CVE-2009-1955
    |     	CVE-2006-20001	7.5	https://vulners.com/cve/CVE-2006-20001
    |     	CNVD-2025-30836	7.5	https://vulners.com/cnvd/CNVD-2025-30836
    |     	CNVD-2025-16614	7.5	https://vulners.com/cnvd/CNVD-2025-16614
    |     	CNVD-2024-20839	7.5	https://vulners.com/cnvd/CNVD-2024-20839
    |     	CNVD-2023-93320	7.5	https://vulners.com/cnvd/CNVD-2023-93320
    |     	CNVD-2023-80558	7.5	https://vulners.com/cnvd/CNVD-2023-80558
    |     	CNVD-2022-53584	7.5	https://vulners.com/cnvd/CNVD-2022-53584
    |     	CNVD-2022-41639	7.5	https://vulners.com/cnvd/CNVD-2022-41639
    |     	CNVD-2022-03223	7.5	https://vulners.com/cnvd/CNVD-2022-03223
    |     	CNVD-2019-41283	7.5	https://vulners.com/cnvd/CNVD-2019-41283
    |     	CNVD-2017-13906	7.5	https://vulners.com/cnvd/CNVD-2017-13906
    |     	CNVD-2016-13233	7.5	https://vulners.com/cnvd/CNVD-2016-13233
    |     	CNVD-2016-13232	7.5	https://vulners.com/cnvd/CNVD-2016-13232
    |     	CD6A79B3-8167-5CFD-9FCB-6986FDF0BE1A	7.5	https://vulners.com/githubexploit/CD6A79B3-8167-5CFD-9FCB-6986FDF0BE1A	*EXPLOIT*
    |     	A0F268C8-7319-5637-82F7-8DAF72D14629	7.5	https://vulners.com/githubexploit/A0F268C8-7319-5637-82F7-8DAF72D14629	*EXPLOIT*
    |     	857E0BF8-9A29-54C5-82EA-8D7C0798CAA6	7.5	https://vulners.com/githubexploit/857E0BF8-9A29-54C5-82EA-8D7C0798CAA6	*EXPLOIT*
    |     	45D138AD-BEC6-552A-91EA-8816914CA7F4	7.5	https://vulners.com/githubexploit/45D138AD-BEC6-552A-91EA-8816914CA7F4	*EXPLOIT*
    |     	CVE-2025-49812	7.4	https://vulners.com/cve/CVE-2025-49812
    |     	CVE-2023-38709	7.3	https://vulners.com/cve/CVE-2023-38709
    |     	CNVD-2024-36395	7.3	https://vulners.com/cnvd/CNVD-2024-36395
    |     	SSV:11802	7.1	https://vulners.com/seebug/SSV:11802	*EXPLOIT*
    |     	SSV:11762	7.1	https://vulners.com/seebug/SSV:11762	*EXPLOIT*
    |     	HTTPD:B44AEE5F83602723E751B3341D72C01D	7.1	https://vulners.com/httpd/HTTPD:B44AEE5F83602723E751B3341D72C01D
    |     	HTTPD:4D420BA542C9357A7F064936250DAEFF	7.1	https://vulners.com/httpd/HTTPD:4D420BA542C9357A7F064936250DAEFF
    |     	CVE-2009-1891	7.1	https://vulners.com/cve/CVE-2009-1891
    |     	CVE-2009-1890	7.1	https://vulners.com/cve/CVE-2009-1890
    |     	SSV:60427	6.9	https://vulners.com/seebug/SSV:60427	*EXPLOIT*
    |     	SSV:60386	6.9	https://vulners.com/seebug/SSV:60386	*EXPLOIT*
    |     	SSV:60069	6.9	https://vulners.com/seebug/SSV:60069	*EXPLOIT*
    |     	HTTPD:D4C114070B5E7C4AA3E92FF94A57C659	6.9	https://vulners.com/httpd/HTTPD:D4C114070B5E7C4AA3E92FF94A57C659
    |     	CVE-2012-0883	6.9	https://vulners.com/cve/CVE-2012-0883
    |     	PACKETSTORM:127546	6.8	https://vulners.com/packetstorm/PACKETSTORM:127546	*EXPLOIT*
    |     	HTTPD:0A13DEC03E87AF57C14487550B086B51	6.8	https://vulners.com/httpd/HTTPD:0A13DEC03E87AF57C14487550B086B51
    |     	CVE-2014-0226	6.8	https://vulners.com/cve/CVE-2014-0226
    |     	1337DAY-ID-22451	6.8	https://vulners.com/zdt/1337DAY-ID-22451	*EXPLOIT*
    |     	SSV:11568	6.4	https://vulners.com/seebug/SSV:11568	*EXPLOIT*
    |     	HTTPD:AFA6B3F6376C54842BAFBBF24C7F44C4	6.4	https://vulners.com/httpd/HTTPD:AFA6B3F6376C54842BAFBBF24C7F44C4
    |     	CVE-2009-1956	6.4	https://vulners.com/cve/CVE-2009-1956
    |     	HTTPD:3E4CF20C0CAD918E98C98926264946F2	6.1	https://vulners.com/httpd/HTTPD:3E4CF20C0CAD918E98C98926264946F2
    |     	CVE-2016-4975	6.1	https://vulners.com/cve/CVE-2016-4975
    |     	CNVD-2018-15542	6.1	https://vulners.com/cnvd/CNVD-2018-15542
    |     	CVE-2018-1302	5.9	https://vulners.com/cve/CVE-2018-1302
    |     	CVE-2018-1301	5.9	https://vulners.com/cve/CVE-2018-1301
    |     	CNVD-2018-06536	5.9	https://vulners.com/cnvd/CNVD-2018-06536
    |     	CNVD-2018-06535	5.9	https://vulners.com/cnvd/CNVD-2018-06535
    |     	VULNERLAB:967	5.8	https://vulners.com/vulnerlab/VULNERLAB:967	*EXPLOIT*
    |     	SSV:67231	5.8	https://vulners.com/seebug/SSV:67231	*EXPLOIT*
    |     	SSV:18637	5.8	https://vulners.com/seebug/SSV:18637	*EXPLOIT*
    |     	SSV:15088	5.8	https://vulners.com/seebug/SSV:15088	*EXPLOIT*
    |     	SSV:12600	5.8	https://vulners.com/seebug/SSV:12600	*EXPLOIT*
    |     	PACKETSTORM:84112	5.8	https://vulners.com/packetstorm/PACKETSTORM:84112	*EXPLOIT*
    |     	EXPLOITPACK:8B4E7E8DAE5A13C8250C6C33307CD66C	5.8	https://vulners.com/exploitpack/EXPLOITPACK:8B4E7E8DAE5A13C8250C6C33307CD66C	*EXPLOIT*
    |     	CNVD-2025-30835	5.4	https://vulners.com/cnvd/CNVD-2025-30835
    |     	HTTPD:BAAB4065D254D64A717E8A5C847C7BCA	5.3	https://vulners.com/httpd/HTTPD:BAAB4065D254D64A717E8A5C847C7BCA
    |     	HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F	5.3	https://vulners.com/httpd/HTTPD:8806CE4EFAA6A567C7FAD62778B6A46F
    |     	CVE-2026-34032	5.3	https://vulners.com/cve/CVE-2026-34032
    |     	CVE-2026-33857	5.3	https://vulners.com/cve/CVE-2026-33857
    |     	CVE-2022-37436	5.3	https://vulners.com/cve/CVE-2022-37436
    |     	CVE-2022-28614	5.3	https://vulners.com/cve/CVE-2022-28614
    |     	CVE-2022-28330	5.3	https://vulners.com/cve/CVE-2022-28330
    |     	CNVD-2023-30859	5.3	https://vulners.com/cnvd/CNVD-2023-30859
    |     	CNVD-2022-53582	5.3	https://vulners.com/cnvd/CNVD-2022-53582
    |     	CNVD-2022-51059	5.3	https://vulners.com/cnvd/CNVD-2022-51059
    |     	CNVD-2021-44766	5.3	https://vulners.com/cnvd/CNVD-2021-44766
    |     	CNVD-2020-46278	5.3	https://vulners.com/cnvd/CNVD-2020-46278
    |     	SSV:60788	5.1	https://vulners.com/seebug/SSV:60788	*EXPLOIT*
    |     	HTTPD:96CCBB8B74890DC94A45CD0955D35015	5.1	https://vulners.com/httpd/HTTPD:96CCBB8B74890DC94A45CD0955D35015
    |     	CVE-2013-1862	5.1	https://vulners.com/cve/CVE-2013-1862
    |     	SSV:96537	5.0	https://vulners.com/seebug/SSV:96537	*EXPLOIT*
    |     	SSV:62058	5.0	https://vulners.com/seebug/SSV:62058	*EXPLOIT*
    |     	SSV:61874	5.0	https://vulners.com/seebug/SSV:61874	*EXPLOIT*
    |     	SSV:20993	5.0	https://vulners.com/seebug/SSV:20993	*EXPLOIT*
    |     	SSV:20979	5.0	https://vulners.com/seebug/SSV:20979	*EXPLOIT*
    |     	SSV:20969	5.0	https://vulners.com/seebug/SSV:20969	*EXPLOIT*
    |     	SSV:19592	5.0	https://vulners.com/seebug/SSV:19592	*EXPLOIT*
    |     	SSV:15137	5.0	https://vulners.com/seebug/SSV:15137	*EXPLOIT*
    |     	PACKETSTORM:181059	5.0	https://vulners.com/packetstorm/PACKETSTORM:181059	*EXPLOIT*
    |     	PACKETSTORM:105672	5.0	https://vulners.com/packetstorm/PACKETSTORM:105672	*EXPLOIT*
    |     	PACKETSTORM:105591	5.0	https://vulners.com/packetstorm/PACKETSTORM:105591	*EXPLOIT*
    |     	MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS-	5.0	https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-HTTP-REWRITE_PROXY_BYPASS-	*EXPLOIT*
    |     	HTTPD:FF76CF8F03BE59B7AD0119034B0022DB	5.0	https://vulners.com/httpd/HTTPD:FF76CF8F03BE59B7AD0119034B0022DB
    |     	HTTPD:DD1BEF13C172D3E8CA5D3F3906101EC9	5.0	https://vulners.com/httpd/HTTPD:DD1BEF13C172D3E8CA5D3F3906101EC9
    |     	HTTPD:D1C855645E1630AE37C6F642C1D0F213	5.0	https://vulners.com/httpd/HTTPD:D1C855645E1630AE37C6F642C1D0F213
    |     	HTTPD:85C24937CF85C2E1DBF78F9954817A28	5.0	https://vulners.com/httpd/HTTPD:85C24937CF85C2E1DBF78F9954817A28
    |     	HTTPD:6D37F924288E2D149DC3C52135232B6E	5.0	https://vulners.com/httpd/HTTPD:6D37F924288E2D149DC3C52135232B6E
    |     	HTTPD:6CA43FB8E8332E715522C8A6C24EC31E	5.0	https://vulners.com/httpd/HTTPD:6CA43FB8E8332E715522C8A6C24EC31E
    |     	HTTPD:60BF8A7CCF62E24F92B3DCCA0E53F1F8	5.0	https://vulners.com/httpd/HTTPD:60BF8A7CCF62E24F92B3DCCA0E53F1F8
    |     	HTTPD:423307886E19F2012B809EEB1E9C6846	5.0	https://vulners.com/httpd/HTTPD:423307886E19F2012B809EEB1E9C6846
    |     	HTTPD:371AA87DEAE292D8E6ACC01309CA723A	5.0	https://vulners.com/httpd/HTTPD:371AA87DEAE292D8E6ACC01309CA723A
    |     	HTTPD:2E324CC4C6C61757E316E26EF4DCB945	5.0	https://vulners.com/httpd/HTTPD:2E324CC4C6C61757E316E26EF4DCB945
    |     	HTTPD:2C06F6E938AADE21D7C59CED65A985E6	5.0	https://vulners.com/httpd/HTTPD:2C06F6E938AADE21D7C59CED65A985E6
    |     	HTTPD:1DC50F4C723B9143E9713B27031C6043	5.0	https://vulners.com/httpd/HTTPD:1DC50F4C723B9143E9713B27031C6043
    |     	HTTPD:1069F9C369A2B2B1C4F8A1AC73589169	5.0	https://vulners.com/httpd/HTTPD:1069F9C369A2B2B1C4F8A1AC73589169
    |     	EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D	5.0	https://vulners.com/exploitpack/EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D	*EXPLOIT*
    |     	EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B	5.0	https://vulners.com/exploitpack/EXPLOITPACK:460143F0ACAE117DD79BD75EDFDA154B	*EXPLOIT*
    |     	EDB-ID:17969	5.0	https://vulners.com/exploitdb/EDB-ID:17969	*EXPLOIT*
    |     	CVE-2015-3183	5.0	https://vulners.com/cve/CVE-2015-3183
    |     	CVE-2015-0228	5.0	https://vulners.com/cve/CVE-2015-0228
    |     	CVE-2014-0231	5.0	https://vulners.com/cve/CVE-2014-0231
    |     	CVE-2014-0098	5.0	https://vulners.com/cve/CVE-2014-0098
    |     	CVE-2013-6438	5.0	https://vulners.com/cve/CVE-2013-6438
    |     	CVE-2013-5704	5.0	https://vulners.com/cve/CVE-2013-5704
    |     	CVE-2011-3368	5.0	https://vulners.com/cve/CVE-2011-3368
    |     	CVE-2010-1623	5.0	https://vulners.com/cve/CVE-2010-1623
    |     	CVE-2010-1452	5.0	https://vulners.com/cve/CVE-2010-1452
    |     	CVE-2010-0408	5.0	https://vulners.com/cve/CVE-2010-0408
    |     	CVE-2009-3720	5.0	https://vulners.com/cve/CVE-2009-3720
    |     	CVE-2009-3560	5.0	https://vulners.com/cve/CVE-2009-3560
    |     	CVE-2009-3095	5.0	https://vulners.com/cve/CVE-2009-3095
    |     	CVE-2008-2364	5.0	https://vulners.com/cve/CVE-2008-2364
    |     	CVE-2007-6750	5.0	https://vulners.com/cve/CVE-2007-6750
    |     	CNVD-2015-01691	5.0	https://vulners.com/cnvd/CNVD-2015-01691
    |     	1337DAY-ID-28573	5.0	https://vulners.com/zdt/1337DAY-ID-28573	*EXPLOIT*
    |     	SSV:11668	4.9	https://vulners.com/seebug/SSV:11668	*EXPLOIT*
    |     	SSV:11501	4.9	https://vulners.com/seebug/SSV:11501	*EXPLOIT*
    |     	HTTPD:05AF7B1B11654BC6892C02003A12DE06	4.9	https://vulners.com/httpd/HTTPD:05AF7B1B11654BC6892C02003A12DE06
    |     	CVE-2009-1195	4.9	https://vulners.com/cve/CVE-2009-1195
    |     	EA6ADD14-D80B-5DC2-9991-1F9663E2D09F	4.8	https://vulners.com/githubexploit/EA6ADD14-D80B-5DC2-9991-1F9663E2D09F	*EXPLOIT*
    |     	CVE-2026-33006	4.8	https://vulners.com/cve/CVE-2026-33006
    |     	SSV:30024	4.6	https://vulners.com/seebug/SSV:30024	*EXPLOIT*
    |     	HTTPD:FB0DB72A0946D2AA25FA9FA21ADB2CE1	4.6	https://vulners.com/httpd/HTTPD:FB0DB72A0946D2AA25FA9FA21ADB2CE1
    |     	CVE-2012-0031	4.6	https://vulners.com/cve/CVE-2012-0031
    |     	1337DAY-ID-27465	4.6	https://vulners.com/zdt/1337DAY-ID-27465	*EXPLOIT*
    |     	SSV:23169	4.4	https://vulners.com/seebug/SSV:23169	*EXPLOIT*
    |     	HTTPD:6309ABD03BB1B29C82E941636515010E	4.4	https://vulners.com/httpd/HTTPD:6309ABD03BB1B29C82E941636515010E
    |     	CVE-2011-3607	4.4	https://vulners.com/cve/CVE-2011-3607
    |     	1337DAY-ID-27473	4.4	https://vulners.com/zdt/1337DAY-ID-27473	*EXPLOIT*
    |     	SSV:60905	4.3	https://vulners.com/seebug/SSV:60905	*EXPLOIT*
    |     	SSV:60657	4.3	https://vulners.com/seebug/SSV:60657	*EXPLOIT*
    |     	SSV:60653	4.3	https://vulners.com/seebug/SSV:60653	*EXPLOIT*
    |     	SSV:60345	4.3	https://vulners.com/seebug/SSV:60345	*EXPLOIT*
    |     	SSV:4786	4.3	https://vulners.com/seebug/SSV:4786	*EXPLOIT*
    |     	SSV:3804	4.3	https://vulners.com/seebug/SSV:3804	*EXPLOIT*
    |     	SSV:30094	4.3	https://vulners.com/seebug/SSV:30094	*EXPLOIT*
    |     	SSV:30056	4.3	https://vulners.com/seebug/SSV:30056	*EXPLOIT*
    |     	SSV:24250	4.3	https://vulners.com/seebug/SSV:24250	*EXPLOIT*
    |     	SSV:20555	4.3	https://vulners.com/seebug/SSV:20555	*EXPLOIT*
    |     	SSV:19320	4.3	https://vulners.com/seebug/SSV:19320	*EXPLOIT*
    |     	SSV:11558	4.3	https://vulners.com/seebug/SSV:11558	*EXPLOIT*
    |     	PACKETSTORM:109284	4.3	https://vulners.com/packetstorm/PACKETSTORM:109284	*EXPLOIT*
    |     	HTTPD:FD1CC7EACBC758C451BA5B8D25FCB6DD	4.3	https://vulners.com/httpd/HTTPD:FD1CC7EACBC758C451BA5B8D25FCB6DD
    |     	HTTPD:C730B9155CAC64B44A77E253B3135FE5	4.3	https://vulners.com/httpd/HTTPD:C730B9155CAC64B44A77E253B3135FE5
    |     	HTTPD:B90E2A3B47C473DD04F25ECBDA96D6CE	4.3	https://vulners.com/httpd/HTTPD:B90E2A3B47C473DD04F25ECBDA96D6CE
    |     	HTTPD:B07D6585013819446B5017BD7E358E6F	4.3	https://vulners.com/httpd/HTTPD:B07D6585013819446B5017BD7E358E6F
    |     	HTTPD:AC5C28237AB3E52EF4D366EB0CD6D4AF	4.3	https://vulners.com/httpd/HTTPD:AC5C28237AB3E52EF4D366EB0CD6D4AF
    |     	HTTPD:A49ADFA68FCEB939DA0E2BE13CA74CB9	4.3	https://vulners.com/httpd/HTTPD:A49ADFA68FCEB939DA0E2BE13CA74CB9
    |     	HTTPD:49F10A242AB057B651259425C3E680F4	4.3	https://vulners.com/httpd/HTTPD:49F10A242AB057B651259425C3E680F4
    |     	HTTPD:3D474EEBC8F5BC66AE37F523DD259829	4.3	https://vulners.com/httpd/HTTPD:3D474EEBC8F5BC66AE37F523DD259829
    |     	HTTPD:2A661E9492CCEF999508BD8503884E30	4.3	https://vulners.com/httpd/HTTPD:2A661E9492CCEF999508BD8503884E30
    |     	HTTPD:1E858A305C3DEA1B5E9A23EE1352B1B3	4.3	https://vulners.com/httpd/HTTPD:1E858A305C3DEA1B5E9A23EE1352B1B3
    |     	HTTPD:0F6B8D022A5D1C68540812E406264625	4.3	https://vulners.com/httpd/HTTPD:0F6B8D022A5D1C68540812E406264625
    |     	HTTPD:0D2952537BF45B77447EF90EAD31D8C9	4.3	https://vulners.com/httpd/HTTPD:0D2952537BF45B77447EF90EAD31D8C9
    |     	EXPLOITPACK:FDCB3D93694E48CD5EE27CE55D6801DE	4.3	https://vulners.com/exploitpack/EXPLOITPACK:FDCB3D93694E48CD5EE27CE55D6801DE	*EXPLOIT*
    |     	EDB-ID:35738	4.3	https://vulners.com/exploitdb/EDB-ID:35738	*EXPLOIT*
    |     	CVE-2016-8612	4.3	https://vulners.com/cve/CVE-2016-8612
    |     	CVE-2014-0118	4.3	https://vulners.com/cve/CVE-2014-0118
    |     	CVE-2013-1896	4.3	https://vulners.com/cve/CVE-2013-1896
    |     	CVE-2012-4558	4.3	https://vulners.com/cve/CVE-2012-4558
    |     	CVE-2012-3499	4.3	https://vulners.com/cve/CVE-2012-3499
    |     	CVE-2012-0053	4.3	https://vulners.com/cve/CVE-2012-0053
    |     	CVE-2011-4317	4.3	https://vulners.com/cve/CVE-2011-4317
    |     	CVE-2011-3639	4.3	https://vulners.com/cve/CVE-2011-3639
    |     	CVE-2011-0419	4.3	https://vulners.com/cve/CVE-2011-0419
    |     	CVE-2010-0434	4.3	https://vulners.com/cve/CVE-2010-0434
    |     	CVE-2009-0023	4.3	https://vulners.com/cve/CVE-2009-0023
    |     	CVE-2008-2939	4.3	https://vulners.com/cve/CVE-2008-2939
    |     	CVE-2008-0455	4.3	https://vulners.com/cve/CVE-2008-0455
    |     	CVE-2007-6420	4.3	https://vulners.com/cve/CVE-2007-6420
    |     	67D5C133-2D28-56DF-B3FF-FA397606547D	4.3	https://vulners.com/gitee/67D5C133-2D28-56DF-B3FF-FA397606547D	*EXPLOIT*
    |     	SSV:12628	2.6	https://vulners.com/seebug/SSV:12628	*EXPLOIT*
    |     	HTTPD:AA860ED739944CC66DCA320985CEC190	2.6	https://vulners.com/httpd/HTTPD:AA860ED739944CC66DCA320985CEC190
    |     	HTTPD:A79620D4A49D1F0D9BE6A18FD0CA234C	2.6	https://vulners.com/httpd/HTTPD:A79620D4A49D1F0D9BE6A18FD0CA234C
    |     	CVE-2012-2687	2.6	https://vulners.com/cve/CVE-2012-2687
    |     	CVE-2009-3094	2.6	https://vulners.com/cve/CVE-2009-3094
    |     	CVE-2008-0456	2.6	https://vulners.com/cve/CVE-2008-0456
    |     	SSV:60250	1.2	https://vulners.com/seebug/SSV:60250	*EXPLOIT*
    |     	CVE-2011-4415	1.2	https://vulners.com/cve/CVE-2011-4415
    |     	1337DAY-ID-9602	0.0	https://vulners.com/zdt/1337DAY-ID-9602	*EXPLOIT*
    |     	1337DAY-ID-21346	0.0	https://vulners.com/zdt/1337DAY-ID-21346	*EXPLOIT*
    |     	1337DAY-ID-17257	0.0	https://vulners.com/zdt/1337DAY-ID-17257	*EXPLOIT*
    |     	1337DAY-ID-16843	0.0	https://vulners.com/zdt/1337DAY-ID-16843	*EXPLOIT*
    |     	1337DAY-ID-13268	0.0	https://vulners.com/zdt/1337DAY-ID-13268	*EXPLOIT*
    |_    	1337DAY-ID-11185	0.0	https://vulners.com/zdt/1337DAY-ID-11185	*EXPLOIT*
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    | http-enum: 
    |   /tikiwiki/: Tikiwiki
    |   /test/: Test page
    |   /phpinfo.php: Possible information file
    |_  /phpMyAdmin/: phpMyAdmin
    |_http-trace: TRACE is enabled
    |_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
    111/tcp  open  rpcbind     2 (RPC #100000)
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2            111/tcp   rpcbind
    |   100000  2            111/udp   rpcbind
    |   100003  2,3,4       2049/tcp   nfs
    |   100003  2,3,4       2049/udp   nfs
    |   100005  1,2,3      44705/tcp   mountd
    |   100005  1,2,3      48639/udp   mountd
    |   100021  1,3,4      40190/tcp   nlockmgr
    |   100021  1,3,4      56490/udp   nlockmgr
    |   100024  1          43097/tcp   status
    |_  100024  1          54226/udp   status
    139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    3306/tcp open  mysql?
    5900/tcp open  vnc         VNC (protocol 3.3)
    OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
    No OS matches for host
    Service Info: Host:  webserver.localdomain; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Host script results:
    |_smb-vuln-ms10-054: false
    |_smb-vuln-ms10-061: false
    |_smb-vuln-regsvc-dos: ERROR: Script execution failed (use -d to debug)

    # Nmap done at Wed Jun  3 18:45:21 2026 -- 1 IP address (1 host up) scanned in 633.29 seconds

# 10.10.10.3 - Debian - "Morpheus:1"

	Nmap scan report for 10.10.10.3
	Host is up (0.00088s latency).
	Not shown: 997 closed tcp ports (reset)
	PORT   STATE SERVICE
	22/tcp open  ssh
	80/tcp open  http
	|_http-dombased-xss: Couldn't find any DOM based XSS.
	|_http-csrf: Couldn't find any CSRF vulnerabilities.
	|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
	| http-enum: 
	|_  /robots.txt: Robots file = "There's no white rabbit here.  Keep searching!"
	81/tcp open  hosts2-ns
        gives admin login on connection to http://10.10.10.3:81
        this website uses nginx 1.18.0
        
# Nmap done at Thu Jun  4 00:40:19 2026 -- 1 IP address (1 host up) scanned in 29.45 seconds


# 10.10.10.4 - Apache Https server - "Mr. Robot"

    Nmap scan report for 10.10.10.4
    Host is up (0.00061s latency).
    Not shown: 671 filtered tcp ports (no-response), 327 closed tcp ports (reset)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT    STATE SERVICE
    80/tcp  open  http
    |_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    443/tcp open  https
    |_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
    

2
# 10.10.10.6 Fedora Web Server - "Earth"

    Nmap scan report for 10.10.10.6
    Host is up (0.00074s latency).
    Not shown: 657 filtered tcp ports (no-response), 340 closed tcp ports (reset)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT    STATE SERVICE
    22/tcp  open  ssh
    80/tcp  open  http
    |_http-trace: TRACE is enabled
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
    |_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    443/tcp open  https
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)


# Risk Matrix & Exploit‑Vector Summary

192.168.56.101

Debian 10, Apache 2.4.38, SSH wrapped only
    • Out‑of‑band HTTP; <br>• SSH unauth
    • Directory traversal, weak file perms on /var/www <br>• CVE‑2023‑25114 (Apache Undersized Write)
    • Disable or harden HTTP: strip default pages <br>• Use sshd_config AllowUsers or SUDO to restrict access

192.168.56.102

Ubuntu, Apache, SSH wrapped
    • SSH passthrough; <br>• Default “Revive Cybertron” webpage
    • Metasploit’s x64/ubuntu_remote_shell via SSH token <br>• CVE‑2023‑40080 (Apache Dangerous Upload)
    • Add proper authentication/‑restrict AllowUsers <br>• Disable file uploads or patch Apache

192.168.56.103

Ubuntu, ASP‑like “Login” page, PHPSESSID flag not set
    • PHP session hijack risk <br>• Broken auth
    • session fixation (sign‑on bypass <br>• CVE‑2024‑28080 “php/Apache “
    • Set httponly flag, enforce session timeouts

192.168.56.104

Ubuntu, Zico's Shop (Apache 2.2) & RPC & MySQL
    • Old Apache 2.2 → multiple CVEs <br>• Open MySQL w/ weak creds
    • CVE‑2023‑45260 (Apache 2.2 <‑> SQL injection) <br>• mysql-secure-migrated “dump” via RPC
    • Upgrade Apache / patch → 2.4+ <br>• Harden MySQL (strong passwords, bind to 127.0.0.1)

192.168.56.105

Debian, Apache 2.4.38 (no title)
    • “Dead‑spot” site, likely intentionally vulnerable <br>• No known open ports beyond Apache
    • Directory bruteforce → /admin/, /wp-admin/ <br>• CVE‑2024‑0615 (Apache 2.4 “phantom” issue)
    • Disable UserDir, block default index files

192.168.56.106

Ubuntu, vsFTPd 2.3.4, Samba, MySQL, VNC, Tomcat 5.5
    • Multiple legacy services <br>• Anonymous FTP enabled <br>• Old Tomcat → RCE
    • CVE‑2022‑22965 (Tomcat 5.5 RCE via FTP) <br>• vsFTPd anonymous* <br>• smb2 insecure
    • Disable anonymous login, patch vsFTPd / Tomcat <br>• Close VNC unless needed

192.168.56.175

Ubuntu (Metasploitable2), vsFTPd, Samba, Apache 2.2, Tomcat 5.5
    • Classic Metasploitable; pre‑known exploits <br>• Multiple services with default creds
    • Metasploit modules: metasploit/ftpanonymous.doctor <br>• smb_login (guest) <br>• Tomcat 5.5 CVE‑2012‑1823
    • Harden or remove unnecessary services <br>• Switch to stateful firewall

10.10.10.2

Ubuntu (Metasploitable2), full service set
    • Same as above + additional legacy ports (RPC, NFS, SMB, MySQL, etc.)
    • Multiple Metasploit modules available (e.g., exploit/unix/misc/multipleservices_telnet_login)
    • Same hardening steps as #7, but: <br>• Block in‑band services via ACL

10.10.10.3

Debian, Apache 2.4.51
    • Newer Apache but still minor CVEs <br>• Lack of auth
    • CVE‑2023‑40080 (Apache 2.4.51) <br>• mod_proxy misconfiguration
    • Keep Apache updated, patch modules

10.10.10.4

Apache (unsecured cert) on 80/443
    • Self‑signed cert, untrusted <br>• Potential downgrade to HTTP
    • SSL stripping (CA‑smash) <br>• 2019‑2024 Apache vulnerabilities
    • Enforce HSTS, use proper cert <br>• Disable HTTP, force HTTPS

10.10.10.6

Fedora 38 (Apache 2.4.51) + SSL, Env: „earth“
    • Modern server but weak TLS settings (old ciphers) <br>• “Bad Request 400” indicates misconfiguration
    • CVE‑2024‑3168 “Apache mod_proxy: HTTP to HTTPS” <br>• Trace/OPTIONS allowed (risk)
    • Disable TRACE, tighten TLS cipher suite <br>• Remove default “Test Page”