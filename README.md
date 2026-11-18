# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Bonser386/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Bonser386/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up world news of Tuesday 17 November 2026, for the make.fun bounty "Sum up 17 November's world news in one image" ($250, top 50 paid).

Six stories, verified against PBS NewsHour, Just Security Early Edition and NPR News Now (17 Nov 2026):

1. **Iran fires drones at a US radar site in Bahrain** — third strike in days; intercepted, no casualties.
2. **Ukraine hits the Crimea (Kerch) Bridge** — severely damaged; Russia hit Kyiv bridges in reply.
3. **Trump in Asia for nuclear talks** — Manila for ASEAN, then Shenzhen for a 19 Nov trilateral with Xi Jinping and Putin.
4. **Estonia to shut its Russian border** — all crossings close from 1 Dec after a foiled arson plot.
5. **Japan scrambles jets** — after suspected Russian aircraft violate its airspace.
6. **Houthis strike a Saudi oil pipeline** — drones at the East-West pipeline, pushing toward Aden.

## The image

`entry.png` — 1024×1024 PNG, ~113 KiB (limit: 1024×1024, 1 MiB). Built by `generate.py` (Pillow, deterministic) as a newspaper front page: headline + one-line summary per story, so the AI judge can read the day's news from the image alone.

## Run it

```sh
python3 main.py   # writes /output/entry.png (byte-identical every run)
```

`main.py` is stdlib only and copies the repo-held image; it uses no network.

<sub>Entered on [make.fun](https://make.fun/?ref=7dkxfn6v&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
