# GoWild NorCal Adventure Planner

A California nature trip recommender built in Python.

## What it does

Asks the user a few questions:
- Starting location (San Jose or San Francisco)
- Available drive time
- Trip mode (day, sunset, night, stargazing)
- Interests (hiking, ocean, wildlife, photography, etc.)
- Difficulty preference

Then recommends the top 3 matching destinations with drive time, wildlife notes, photo zones, weather info, and a Google Maps link.

## How to run

```bash
python main.py
```

## Project structure

```
main.py         — user input and output
data.py         — all places as a list of dictionaries
recommender.py  — scoring logic and top 3 selection
utils.py        — maps link generator and result formatter
```

## Built for

Stanford Code in Place 2026 — Final Project
