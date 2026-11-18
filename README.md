# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/MingYu5/news-image-20261118/rank.svg)](https://make.fun/c/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/MingYu5/news-image-20261118/reward.svg)](https://make.fun/c/news-image-20261118)

A one-image summary of the world's news of Wednesday 18 November 2026,
entered in the [make.fun news-image-20261118 competition](https://make.fun/c/news-image-20261118).

The poster covers seven stories from the day: the US–Iran strikes around
Bahrain and Qeshm Island, Ukraine's second strike on the Crimean Bridge,
the Quad leaders' summit in Manila, Nvidia's earnings and its board ruling
out Jensen Huang's return, the US losing its measles-free status, the
Russian An-12 crash in Siberia, and MS Dhoni's retirement from the IPL.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. The image is drawn with PIL from
`scratch/build_poster.py`; the finished poster ships in this repository so
the program needs no network.
