from graphics import Canvas

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 850

BG = "wheat"
CARD = "white"
TEXT = "black"
MUTED = "gray"
ACCENT = "darkgreen"
LINE = "lightgray"


def get_match_reasons(place, prefs):
    reasons = []
    for vibe in prefs["vibes"]:
        if vibe in place["vibes"] and len(reasons) < 3:
            reasons.append(vibe)
    if prefs["mode"] == "stargazing" and place.get("stargazing") and len(reasons) < 3:
        reasons.append("dark sky")
    if prefs["mode"] in place["modes"] and len(reasons) < 3:
        reasons.append("time match")
    return reasons


def draw_text(canvas, x, y, text, size, color, anchor="w"):
    canvas.create_text(x, y, text=text, font=f"Helvetica {size}",
                       color=color, anchor=anchor)


def draw_section(canvas, y, title, content):
    """Draws a label and value on the same line, returns new Y position."""
    draw_text(canvas, 130, y, title, 12, ACCENT)
    draw_text(canvas, 260, y, content, 12, TEXT)
    return y + 30


def draw_trip_card(canvas, place, prefs):
    origin = prefs["origin"]
    mode = prefs["mode"]

    # Background
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, BG)

    # Card (Stanford Canvas doesn't support outline= so we draw border manually)
    canvas.create_rectangle(100, 70, 600, 780, CARD)
    canvas.create_rectangle(100, 70, 600, 76, ACCENT)
    canvas.create_rectangle(100, 774, 600, 780, ACCENT)
    canvas.create_rectangle(100, 70, 106, 780, ACCENT)
    canvas.create_rectangle(594, 70, 600, 780, ACCENT)

    # Header
    canvas.create_text(350, 115, text="GOWILD NORCAL",
                       font="Helvetica 20 bold", color=TEXT, anchor="center")
    canvas.create_text(350, 145, text="ADVENTURE CARD",
                       font="Helvetica 12", color=MUTED, anchor="center")
    canvas.create_line(130, 175, 570, 175, LINE)

    # Place name and description
    draw_text(canvas, 130, 220, place["name"].upper(), 18, TEXT)
    draw_text(canvas, 130, 250, place["description"], 11, MUTED)

    # Basic info block
    y = 315
    y = draw_section(canvas, y, "MODE", mode.upper())
    y = draw_section(canvas, y, "DRIVE", f"~{place['drive_minutes'][origin]} MIN")
    y = draw_section(canvas, y, "FROM", origin.upper())
    y = draw_section(canvas, y, "BEST", place["best_time"].upper())

    y += 20
    canvas.create_line(130, y, 570, y, LINE)
    y += 30

    # Why it matches
    draw_text(canvas, 130, y, "WHY IT MATCHES", 13, ACCENT)
    y += 30
    for reason in get_match_reasons(place, prefs):
        draw_text(canvas, 150, y, f"- {reason}", 11, TEXT)
        y += 25

    y += 15

    # Wildlife
    if place.get("wildlife"):
        draw_text(canvas, 130, y, "WILDLIFE", 13, ACCENT)
        y += 28
        draw_text(canvas, 150, y, ", ".join(place["wildlife"]), 11, TEXT)
        y += 40

    # Photo spots
    if place.get("photo_zones"):
        draw_text(canvas, 130, y, "PHOTO SPOTS", 13, ACCENT)
        y += 28
        draw_text(canvas, 150, y, ", ".join(place["photo_zones"]), 11, TEXT)

    # Footer
    canvas.create_line(130, 720, 570, 720, LINE)
    canvas.create_text(350, 750,
                       text="GO OUTSIDE / TOUCH GRASS / TAKE PHOTOS",
                       font="Helvetica 10", color=MUTED, anchor="center")


def show_cards(places, prefs):
    if not places:
        return
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_trip_card(canvas, places[0], prefs)
    canvas.mainloop()
