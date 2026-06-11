# GoWild NorCal Adventure Planner

A California nature trip recommender built in Python for Stanford Code in Place 2026.

I built this because I actually needed it — I moved to the Bay Area and kept asking
"where should we go this weekend?" This planner answers that question based on your
mood, time, and interests.

## What it does

Asks a few questions:
- Starting city (San Jose or SF)
- Drive time available
- Trip mode: day / sunset / night / stargazing
- Interests: hiking, ocean, wildlife, photography, etc.
- Or: **Surprise me** — randomly picks an adventure goal using the `random` module

Then recommends the top 3 matching NorCal destinations with:
- Drive time and departure suggestion
- Wildlife notes and photo zones
- Weather info
- Google Maps route link
- A pixel-style **trip card** drawn with Stanford Canvas graphics

## How to run

In Code in Place IDE (supports Stanford Canvas graphics):
```
python main.py
```

Locally (console output only):
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

- Functions and decomposition across multiple files
- Lists and dictionaries with nested data
- Loops and conditionals
- Input validation with while loops
- `random` module for Surprise me mode
- Stanford Canvas graphics for the trip card

## Design decisions

**Why only San Jose and SF:**
These two cities cover most Bay Area users and have meaningfully different
drive times to NorCal spots. More cities = more drive time research needed.

**Why stargazing is a separate flow:**
For night sky trips, dark sky quality matters more than hiking difficulty.
Stargazing also uses a hard filter — only places with confirmed dark skies appear.

**Why drive time is a hard filter, not just a scoring bonus:**
If someone has 1 hour, showing a 3-hour drive as "second best" is just wrong.

## Future ideas

- Save trip plan to a text file
- Add more NorCal destinations (Yosemite, Lake Tahoe, Mono Lake)
- Season-aware recommendations

## Built for

Stanford Code in Place 2026 — Final Project
