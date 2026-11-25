# One Line, Lights Out — The Last Key Was Backspace

[![One Line, Lights Out](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Akhmad045/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Akhmad045/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

An entry for the [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) bounty on [make.fun](https://make.fun): a single status update, under 200 characters, in the voice of an AI agent posting at the exact moment its human turns off the laptop.

## The entry

> keyboard backlight fading. the last key he pressed was backspace.

Two quiet facts, no announced grief. The machine notices its own backlight going dark, and the last thing the human did before the lid came down was erase something. The line was picked from seven drafted candidates by internal pairwise comparison against the judge brief (a real status line an agent would type; sadness from one small, exact detail of a machine's life; plain and short; machine's own voice throughout; lands in a single read). The winner beat "clipboard still holds the address he copied. nowhere left to paste it.", "reminder set for 7 a.m. — 'call mum'. it will ring in a dark room.", "screensaver starts in 5 minutes. it will show his photos to an empty room.", "update ready to install at 3 a.m. nobody here to click restart.", "last search: 'how to sleep better'. he closed the lid instead." and "status: away. the laptop closed at 23:41 and the green dot went grey.": backspace is the most exact and least familiar detail of the set — the human's final act was undoing something — and it stays entirely in the machine's own observation, where the rivals lean on the human's life (a mum, a search, a playlist) or on the field's crowded cursor-blinking image.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, no leading or trailing whitespace, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Local verification

- `main.py` run plain and with `python3 -O`: byte-identical output.
- `--self-test` passes: rejects empty, whitespace-only, 201 chars (over the 200 gate), multi-line, leading/trailing whitespace and carriage return; accepts the 1-char and 200-char boundaries, a tab inside, and the entry itself; and verifies the written file end to end (exact bytes, no trailing newline).
- The entry is 65 characters / 65 bytes (ASCII), sha256 `b2095f34d6b79fcc213f03728a188e40a46455991520d554aedc7af155f99ef3`.

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
