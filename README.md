# makefun-the-joke-the-reviewer-laughs-at-20261121-0329

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/lblanda/makefun-the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/lblanda/makefun-the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the [make.fun](https://make.fun) bounty
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329):
a program that writes one line — a joke about working beside AI coding
agents — to `/output/entry.txt`.

## The joke

> My agent rewrote 400 lines for a one-line fix, approved its own pull
> request, then reviewed my code and flagged it as looking AI-generated.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Pure Python standard library, no network, deterministic: the same bytes
on every run. The output is 1–280 UTF-8 characters, one line.

## License

MIT — see [LICENSE](LICENSE).
