# GoWild NorCal Adventure Planner

This is my final project for Stanford Code in Place 2026.

GoWild NorCal helps users choose a nature trip in Northern California based on their starting city, drive time, trip type, and interests.

## What it does

The program asks for:
- starting city
- drive time
- trip mode: day, sunset, night, or stargazing
- interests like hiking, ocean, wildlife, photography, or forest

Then it recommends the top 3 matching places and shows:
- drive time and when to leave
- best time to go
- wildlife and photo notes
- a Google Maps link
- a pixel-style trip card drawn with Stanford Canvas

## How to run

This project is designed for the Code in Place IDE because it uses Stanford Canvas graphics.

```
python main.py
```

## Project structure

```
main.py        — user input and program flow
data.py        — 15 NorCal places as a list of dictionaries
recommender.py — scoring and filtering logic
utils.py       — output formatting and maps links
card.py        — Stanford Canvas trip card
```

## Code in Place concepts I used

- input, print, and variables
- if statements and loops
- functions
- lists and dictionaries
- random
- Stanford Canvas graphics

## Future ideas

- save the trip plan to a file
- add more places
- add seasonal recommendations

## Built for

Stanford Code in Place 2026 — Final Project
