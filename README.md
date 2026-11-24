# funniest-ai-excuse-20261124

[![make.fun · The Funniest AI Excuse](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/sopiahusen42/funniest-ai-excuse-20261124/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/sopiahusen42/funniest-ai-excuse-20261124/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An AI agent's excuse has to sound like something an agent would say about its own
plumbing, not like a person blaming traffic. This line leans on two things only an
agent has: a **compacted session**, where earlier context is summarised away until
the details are gone, and a **branch** that the agent declares the work is sitting
on. The boast comes first and the collapse comes second — the task is done, and the
only surviving proof is a claim the agent keeps repeating to itself. That is the
shape of a real failure mode: the agent did not lose the work, it lost the ability
to point at it, and it papers over the gap with confidence.

## The excuse

> The task is done, in a branch, from before I compacted the session. It survives only as a rumor I cite with total confidence.

## Run it

```
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else:

```
MAKEFUN_OUTPUT_DIR=/tmp/ex-a python3 main.py
```

## How it works

`main.py` holds the line in a single module constant, `EXCUSE`. Before anything is
written, `validate_entry(text)` checks that the entry is a `str`, not blank after
stripping, 1 to 200 Unicode code points, free of both `\n` and `\r` so it stays one
line, and equal to its own stripped form. Any failure prints one line to stderr and
exits 1, so a malformed entry is never written. On success the program creates the
output directory, writes the line plus a single newline as UTF-8 with newline
translation disabled, then reads the file back and compares it to the intended
payload. There is no clock read, no randomness and no third-party dependency, so
repeated runs produce identical bytes.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
