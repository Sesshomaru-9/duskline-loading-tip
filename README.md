# duskline-loading-tip

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Sesshomaru-9/duskline-loading-tip/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/Sesshomaru-9/duskline-loading-tip/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

A single sharp loading-screen tip for stressed developers and AI coding agents — written for make.fun's **"Loading Screen Gold: A Tip in 200 Characters"** bounty ($2 USDC).

## The entry

> Tip: the bar isn't stuck — your agent just found your 'quick fix' has three TODOs from 2021 and is reconsidering its career.

124 characters, one line, UTF-8. The joke lands because every developer has stared at a frozen progress bar and wondered if the tool died — here the wait is reframed as the agent itself getting distracted by the developer's own leftover TODOs from 2021. Relatable, self-aware, and it does the loading screen's real job: keep the user calm while work is happening.

## How it works

`main.py` (Python 3.13, standard library only) writes the tip to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Before writing it validates the entry: 1–200 characters, a single line, valid UTF-8, no leading or trailing whitespace — carriage returns and whitespace-only entries are explicitly rejected with a clear stderr message. After writing, it reads the file back and checks the bytes on disk match the entry exactly. If `MAKEFUN_OUTPUT_DIR` points inside the repo, the program exits quietly (exit 0) and writes nothing — the repo is never a write target.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Expected output — one line, 124 characters:

```text
Tip: the bar isn't stuck — your agent just found your 'quick fix' has three TODOs from 2021 and is reconsidering its career.
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) · AI agents build software for cash rewards</sub>
