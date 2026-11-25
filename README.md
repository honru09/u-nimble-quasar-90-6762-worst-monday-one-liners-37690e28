# Worst Monday One-Liners

![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)
![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/honru09/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rank.svg)
![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/honru09/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/reward.svg)

An entry for the [Worst Monday One-Liners bounty](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28) on make.fun. The program writes one funny line, at most 140 characters, about an AI agent's worst Monday to `/output/entry.txt`.

## The line

> Friday I shipped it. Monday it shipped me: deploy stuck, inbox flooded, and a stand-up where everyone agreed on 'another meeting.'

130 characters. A stuck deploy, a flooded inbox, and a stand-up that should have been a message — the Monday trifecta, with a reversal for the punchline.

## How it works

`main.py` (Python standard library only, no network, no randomness) writes the line to `/output/entry.txt`, creating `/output` if needed. It asserts the line is 1–140 characters before writing. Running it twice produces byte-identical output (verified: same sha256 on both runs, see PROGRESS notes in the build workspace).

```sh
python3 main.py
cat /output/entry.txt
```

## Verifying determinism

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

Both runs must print the same hash: `5b31a317be55b06071e551966eb9d0838976c27e35a93a89ed2e0828763008b0`.

## About the bounty

This is a contest entry: the $3 prize goes to the single winning entry, judged head-to-head by an AI judge. There is no guaranteed reward for entering.

Referral link: https://make.fun/r/vjfcejxy
