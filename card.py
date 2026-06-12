from graphics import Canvas

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 850

THEMES = {
    "day": {
        "bg": "lightblue",
        "card": "white",
        "banner": "blue",
        "text": "black",
        "accent": "green",
        "icon": "yellow"
    },
    "sunset": {
        "bg": "orange",
        "card": "white",
        "banner": "red",
        "text": "black",
        "accent": "brown",
        "icon": "yellow"
    },
    "night": {
        "bg": "black",
        "card": "blue",
        "banner": "black",
        "text": "white",
        "accent": "purple",
        "icon": "yellow"
    },
    "stargazing": {
        "bg": "black",
        "card": "blue",
        "banner": "purple",
        "text": "white",
        "accent": "yellow",
        "icon": "white"
    }
}


def get_match_reasons(place, prefs):
    reasons = []
    for vibe in prefs["vibes"]:
        if vibe in place["vibes"]:
            reasons.append(vibe)
    if prefs["mode"] == "stargazing" and place.get("stargazing"):
        reasons.append("dark sky access")
    if prefs["mode"] in place["modes"]:
        reasons.append("good time match")
    return reasons[:3]


def draw_pixel_star(canvas, x, y, color):
    s = 6
    canvas.create_rectangle(x + s, y, x + 2*s, y + s, color)
    canvas.create_rectangle(x, y + s, x + 3*s, y + 2*s, color)
    canvas.create_rectangle(x + s, y + 2*s, x + 2*s, y + 3*s, color)


def draw_moon(canvas, x, y, color):
    canvas.create_rectangle(x, y, x+12, y+12, color)
    canvas.create_rectangle(x+12, y+12, x+24, y+24, color)
    canvas.create_rectangle(x+12, y+24, x+24, y+36, color)
    canvas.create_rectangle(x, y+36, x+12, y+48, color)


def draw_sun(canvas, x, y, color):
    canvas.create_rectangle(x, y, x+45, y+45, color)


def draw_tree(canvas, x, y, color):
    canvas.create_rectangle(x+18, y+45, x+30, y+75, "brown")
    canvas.create_rectangle(x, y+25, x+48, y+45, color)
    canvas.create_rectangle(x+8, y+10, x+40, y+30, color)


def draw_mountains(canvas, theme):
    canvas.create_line(170, 350, 260, 275, theme["accent"])
    canvas.create_line(260, 275, 350, 350, theme["accent"])
    canvas.create_line(310, 350, 410, 285, theme["accent"])
    canvas.create_line(410, 285, 540, 350, theme["accent"])
    canvas.create_rectangle(90, 350, 610, 365, theme["accent"])


def draw_background(canvas, theme):
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, theme["bg"])


def draw_card_frame(canvas, theme):
    canvas.create_rectangle(55, 55, 645, 795, theme["card"])
    canvas.create_rectangle(55, 55, 645, 75, theme["accent"])
    canvas.create_rectangle(55, 775, 645, 795, theme["accent"])
    canvas.create_rectangle(55, 55, 75, 795, theme["accent"])
    canvas.create_rectangle(625, 55, 645, 795, theme["accent"])


def draw_header(canvas, place, theme):
    canvas.create_rectangle(75, 80, 625, 150, theme["banner"])
    canvas.create_text(350, 105, text="GOWILD NORCAL", font="Courier 18",
                       color=theme["accent"], anchor="center")
    canvas.create_text(350, 132, text="PIXEL TRIP CARD", font="Courier 13",
                       color=theme["text"], anchor="center")
    canvas.create_text(90, 185, text=place["name"].upper(), font="Courier 22",
                       color=theme["text"], anchor="w")
    canvas.create_text(90, 215, text=place["description"], font="Courier 12",
                       color=theme["accent"], anchor="w")


def draw_scene(canvas, mode, theme):
    canvas.create_rectangle(90, 245, 610, 365, theme["banner"])
    if mode in ["night", "stargazing"]:
        draw_moon(canvas, 120, 270, theme["icon"])
        draw_pixel_star(canvas, 230, 275, theme["icon"])
        draw_pixel_star(canvas, 360, 295, theme["icon"])
        draw_pixel_star(canvas, 500, 270, theme["icon"])
    else:
        draw_sun(canvas, 120, 285, theme["icon"])
        draw_tree(canvas, 500, 285, theme["accent"])
    draw_mountains(canvas, theme)


def draw_label_value(canvas, label, value, x, y, theme):
    canvas.create_text(x, y, text=f"{label}:", font="Courier 13",
                       color=theme["accent"], anchor="w")
    canvas.create_text(x + 140, y, text=value, font="Courier 13",
                       color=theme["text"], anchor="w")


def draw_details(canvas, place, prefs, theme):
    origin = prefs["origin"]
    mode = prefs["mode"]
    drive = place["drive_minutes"][origin]
    y = 410

    for label, value in [
        ("FROM", origin.upper()),
        ("DRIVE", f"~{drive} MIN"),
        ("MODE", mode.upper()),
        ("BEST TIME", place["best_time"].upper()),
        ("WEATHER", place["weather_note"]),
    ]:
        draw_label_value(canvas, label, value, 95, y, theme)
        y += 38

    y += 20
    canvas.create_text(95, y, text="WHY IT MATCHES", font="Courier 14",
                       color=theme["accent"], anchor="w")
    y += 30
    for reason in get_match_reasons(place, prefs):
        canvas.create_text(115, y, text=f"- {reason}", font="Courier 12",
                           color=theme["text"], anchor="w")
        y += 25

    y += 10
    if place.get("wildlife"):
        canvas.create_text(95, y, text="WILDLIFE", font="Courier 14",
                           color=theme["accent"], anchor="w")
        y += 25
        canvas.create_text(115, y, text=", ".join(place["wildlife"][:4]),
                           font="Courier 11", color=theme["text"], anchor="w")
        y += 35

    if place.get("photo_zones"):
        canvas.create_text(95, y, text="PHOTO ZONES", font="Courier 14",
                           color=theme["accent"], anchor="w")
        y += 25
        canvas.create_text(115, y, text=", ".join(place["photo_zones"][:3]),
                           font="Courier 11", color=theme["text"], anchor="w")
        y += 35

    if place.get("sky_note"):
        canvas.create_text(95, y, text="SKY NOTE", font="Courier 14",
                           color=theme["accent"], anchor="w")
        y += 25
        canvas.create_text(115, y, text=place["sky_note"],
                           font="Courier 10", color=theme["text"], anchor="w")


def draw_footer(canvas, theme):
    canvas.create_rectangle(75, 735, 625, 775, theme["banner"])
    canvas.create_text(350, 755, text="GO OUTSIDE  •  TOUCH GRASS  •  TAKE PHOTOS",
                       font="Courier 11", color=theme["accent"], anchor="center")


def draw_trip_card(canvas, place, prefs):
    mode = prefs["mode"]
    theme = THEMES.get(mode, THEMES["day"])
    draw_background(canvas, theme)
    draw_card_frame(canvas, theme)
    draw_header(canvas, place, theme)
    draw_scene(canvas, mode, theme)
    draw_details(canvas, place, prefs, theme)
    draw_footer(canvas, theme)


def show_cards(places, prefs):
    if not places:
        return
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_trip_card(canvas, places[0], prefs)
    canvas.mainloop()
