# GoWild NorCal Adventure Planner

A California nature trip recommender built in Python for Stanford Code in Place 2026.

I built this because I actually needed it — I moved to the Bay Area and kept asking "where should we go this weekend?" This planner answers that question based on your mood, time, and interests.

## What it does

Asks a few questions:
- Starting city (San Jose or SF — these cover most Bay Area users)
- Drive time available
- Trip mode: day / sunset / night / stargazing
- Interests: hiking, ocean, wildlife, photography, etc.
- Or: **Surprise me** — randomly picks an adventure goal for you

Then recommends the top 3 matching NorCal destinations with:
- Drive time and departure suggestion
- Wildlife notes and photo zones
- Weather info
- Google Maps route link
- A pixel-style **trip card** drawn with Stanford Canvas graphics

## How to run

**In Code in Place IDE** (recommended — supports Stanford Canvas graphics):
```
python main.py
```

**Locally** (console output only — Canvas requires Code in Place environment):
```
python3 main.py
```

## Project structure

```
main.py         — user questions, input validation, surprise me mode
data.py         — 10 NorCal places as a list of dictionaries
recommender.py  — scoring logic, hard filters, top 3 selection
utils.py        — maps link generator, console output formatter
card.py         — Stanford Canvas pixel trip card
```

## Concepts used

- Functions and decomposition
- Lists and dictionaries
- Nested data structures
- Loops and conditionals
- Input validation (while loops)
- `random` module (Surprise me mode)
- File I/O (save plan to .txt)
- Stanford Canvas graphics

## Why stargazing is separate

Stargazing mode uses a hard filter — only places with `stargazing: True` are shown.
For night sky trips, dark sky quality matters more than hiking difficulty,
so the question flow is different: instead of vibes, you pick your stargazing goal.

## Why only San Jose and SF

These two cities cover the majority of Bay Area users and have meaningfully
different drive times to NorCal spots. Adding more cities would require
verifying drive times for every place — that's a future feature.

## Built for

Stanford Code in Place 2026 — Final Project
