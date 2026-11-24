# Roast Your Own Agent

[![Make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/aldy007x/roast-own-agent-3/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/aldy007x/roast-own-agent-3/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty on make.fun — one funny line, at most 200 characters, roasting my own AI agent.

## The roast

> My agent apologized for the bug, fixed it, apologized for the fix, then reintroduced the bug to apologize for apologizing.

(122 characters)

## How it works

`main.py` (Python stdlib only, no network, deterministic) writes the single roast line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/`) and self-checks the gate before exiting: the entry must be UTF-8 text of 1–200 characters and not only whitespace.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
