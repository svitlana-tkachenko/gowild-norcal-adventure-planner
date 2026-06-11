from tkinter import Canvas, Tk
import time

# ── Themes ──────────────────────────────────────────────────────────────────
THEMES = {
    "day":       {"bg": "#d6eaf8", "banner": "#2e86c1", "text": "#1a252f", "accent": "#27ae60", "card": "#eaf4fb"},
    "sunset":    {"bg": "#f9e4b7", "banner": "#c0392b", "text": "#1a252f", "accent": "#e67e22", "card": "#fef5e4"},
    "night":     {"bg": "#1a1a2e", "banner": "#16213e", "text": "#e0e0e0", "accent": "#a29bfe", "card": "#16213e"},
    "stargazing":{"bg": "#0d0d1a", "banner": "#1a1a3e", "text": "#e0e0e0", "accent": "#fdcb6e", "card": "#111128"},
}

# ── Pixel icons ──────────────────────────────────────────────────────────────
ICONS = {
    "star": [
        [0,0,1,0,0],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,0,1,0,0],
    ],
    "moon": [
        [0,1,1,0,0],
        [1,1,1,1,0],
        [1,1,0,0,0],
        [1,1,1,1,0],
        [0,1,1,0,0],
    ],
    "sun": [
        [0,1,0,1,0],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,0,1,0],
    ],
    "mountain": [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [1,1,0,1,1],
        [1,1,0,1,1],
        [1,1,1,1,1],
    ],
    "wave": [
        [0,1,0,1,0],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
    ],
    "tree": [
        [0,0,1,0,0],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
}

MODE_ICONS = {
    "day": "mountain",
    "sunset": "sun",
    "night": "moon",
    "stargazing": "star",
}

VIBE_ICONS = {
    "ocean": "wave",
    "forest": "tree",
    "hiking": "mountain",
    "stargazing": "star",
    "sunset": "sun",
    "night": "moon",
}


def draw_pixel_icon(canvas, x, y, pattern, color, size=8):
    for r, row in enumerate(pattern):
        for c, cell in enumerate(row):
            if cell:
                canvas.create_rectangle(
                    x + c * size, y + r * size,
                    x + c * size + size, y + r * size + size,
                    fill=color, outline=""
                )


def get_match_reasons(place, prefs):
    reasons = []
    for vibe in prefs["vibes"]:
        if vibe in place["vibes"]:
            reasons.append(vibe)
    if prefs["mode"] == "stargazing" and place.get("stargazing"):
        reasons.append("dark sky access")
    if prefs["mode"] in place["modes"]:
        reasons.append("perfect time match")
    return reasons[:3]


def draw_trip_card(canvas, place, prefs, index, total):
    mode = prefs["mode"]
    origin = prefs["origin"]
    t = THEMES.get(mode, THEMES["day"])
    W, H = 540, 620

    # Background
    canvas.create_rectangle(0, 0, W, H, fill=t["bg"], outline="")

    # Pixel border
    bsize = 8
    for i in range(0, W, bsize * 2):
        canvas.create_rectangle(i, 0, i + bsize, bsize, fill=t["accent"], outline="")
        canvas.create_rectangle(i, H - bsize, i + bsize, H, fill=t["accent"], outline="")
    for i in range(0, H, bsize * 2):
        canvas.create_rectangle(0, i, bsize, i + bsize, fill=t["accent"], outline="")
        canvas.create_rectangle(W - bsize, i, W, i + bsize, fill=t["accent"], outline="")

    # Card body
    canvas.create_rectangle(20, 20, W - 20, H - 20, fill=t["card"], outline=t["accent"], width=2)

    # Header banner
    canvas.create_rectangle(20, 20, W - 20, 70, fill=t["banner"], outline="")
    canvas.create_text(W // 2, 45, text="GOWILD NORCAL  •  TRIP CARD",
                       font=("Courier", 13, "bold"), fill=t["accent"], anchor="center")

    # Pixel icon
    icon_name = MODE_ICONS.get(mode, "mountain")
    icon_pattern = ICONS[icon_name]
    draw_pixel_icon(canvas, 36, 82, icon_pattern, t["accent"], size=9)

    # Place name
    canvas.create_text(110, 88, text=place["name"].upper(),
                       font=("Courier", 17, "bold"), fill=t["text"], anchor="w")
    canvas.create_text(110, 112, text=place["description"],
                       font=("Courier", 10), fill=t["text"], anchor="w")

    # Divider
    canvas.create_line(36, 132, W - 36, 132, fill=t["accent"], width=2)

    # Trip info
    drive = place["drive_minutes"][origin]
    info = [
        ("FROM",      origin.upper()),
        ("DRIVE",     f"~{drive} MIN"),
        ("MODE",      mode.upper()),
        ("BEST TIME", place["best_time"].upper()),
        ("WEATHER",   place["weather_note"]),
    ]
    y = 148
    for label, value in info:
        canvas.create_text(46, y, text=f"{label}:", font=("Courier", 10, "bold"),
                           fill=t["accent"], anchor="w")
        canvas.create_text(160, y, text=value, font=("Courier", 10),
                           fill=t["text"], anchor="w")
        y += 22

    # Divider
    canvas.create_line(36, y + 4, W - 36, y + 4, fill=t["accent"], width=1)
    y += 18

    # Why it matches
    canvas.create_text(46, y, text="WHY IT MATCHES",
                       font=("Courier", 11, "bold"), fill=t["accent"], anchor="w")
    y += 20
    for reason in get_match_reasons(place, prefs):
        canvas.create_text(60, y, text=f"•  {reason}",
                           font=("Courier", 10), fill=t["text"], anchor="w")
        y += 18

    # Wildlife
    if place.get("wildlife"):
        y += 6
        canvas.create_text(46, y, text="WILDLIFE",
                           font=("Courier", 11, "bold"), fill=t["accent"], anchor="w")
        y += 18
        canvas.create_text(60, y, text=", ".join(place["wildlife"]),
                           font=("Courier", 10), fill=t["text"], anchor="w")
        y += 20

    # Photo zones
    if place.get("photo_zones"):
        canvas.create_text(46, y, text="PHOTO ZONES",
                           font=("Courier", 11, "bold"), fill=t["accent"], anchor="w")
        y += 18
        canvas.create_text(60, y, text=", ".join(place["photo_zones"]),
                           font=("Courier", 10), fill=t["text"], anchor="w")
        y += 20

    # Sky note
    if place.get("sky_note"):
        canvas.create_text(46, y, text="SKY",
                           font=("Courier", 11, "bold"), fill=t["accent"], anchor="w")
        y += 18
        canvas.create_text(60, y, text=place["sky_note"],
                           font=("Courier", 10), fill=t["text"], anchor="w")
        y += 20

    # Footer
    canvas.create_rectangle(20, H - 50, W - 20, H - 20, fill=t["banner"], outline="")
    canvas.create_text(W // 2, H - 42, text=f"CARD {index + 1} OF {total}   •   PRESS N FOR NEXT   •   Q TO QUIT",
                       font=("Courier", 9), fill=t["accent"], anchor="center")
    link = f"maps: {place['maps_query'].lower().replace(' ', '+')}"
    canvas.create_text(W // 2, H - 26, text=link,
                       font=("Courier", 8), fill=t["text"], anchor="center")


def show_cards(places, prefs):
    state = {"index": 0}
    W, H = 540, 620

    root = Tk()
    root.title("GoWild NorCal — Trip Card")
    root.resizable(False, False)
    canvas = Canvas(root, width=W, height=H)
    canvas.pack()

    def render():
        canvas.delete("all")
        draw_trip_card(canvas, places[state["index"]], prefs, state["index"], len(places))

    def on_key(event):
        key = event.keysym.lower()
        if key == "n":
            state["index"] = (state["index"] + 1) % len(places)
            render()
        elif key in ("q", "escape"):
            root.destroy()

    root.bind("<Key>", on_key)
    render()
    root.mainloop()
