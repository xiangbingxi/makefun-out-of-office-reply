# Handoff — out-of-office reply

比赛：u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d（$5，截止北京时间 2026-11-26 23:05）
仓库名：makefun-out-of-office-reply

## 做法

- 拉 kit 解包，读 RULES.txt / competition.yaml 确认：程序写 `/output/entry.txt`，UTF-8、1–160 字符、非空白。
- 文案是用户让 GPT 写好、亲口说照原样交的，一字未改。`main.py` 把文案写到 `/output/entry.txt`，UTF-8、无尾随换行、不读外部文件、不联网。
- `main.py` 写了两次：第一次是完整版并跑通；第二次是真正的改进——写完读回文件，和 ENTRY 一字不差否则报错退出，外加 1–160 字符长度检查。

## 文案（117 字符）

I'm out of office until Monday, but if it's urgent, my replacement can confidently tell you I'll be back on Thursday.

## 校验结果

- 第一次运行（v1）：exit 0，117 字节 / 117 字符，sha256 3c021b6d3ad040ba52d466f0bdfa754e1b05a8db9876436498bf2381bf049a37
- 第二次运行（v2，改进版）跑两次：exit 0 / exit 0，两次输出 cmp 逐字节一致
- entry.txt sha256（两次相同）：3c021b6d3ad040ba52d466f0bdfa754e1b05a8db9876436498bf2381bf049a37
- entry.txt 与 prompt.txt cmp 一致；与文案 exact match
- 117 ≤ 160，上限通过

## 文件

- main.py、LICENSE（MIT，含 SPDX 行）、README.md（三枚官方徽章 + 比赛页链接）、prompt.txt（文案原文单行）、.makefun/owner.json、HANDOFF.md
