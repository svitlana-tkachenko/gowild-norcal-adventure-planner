def score_place(place, user_prefs):
    score = 0

    # Match user interests with place vibes.
    for vibe in user_prefs["vibes"]:
        if vibe in place["vibes"]:
            score += 2

    # Match trip mode: day, sunset, night, or stargazing.
    if user_prefs["mode"] in place["modes"]:
        score += 3

    # Extra bonus for stargazing places.
    if user_prefs["mode"] == "stargazing" and place.get("stargazing"):
        score += 2

    # Match hiking difficulty.
    if place["difficulty"] == user_prefs["difficulty"]:
        score += 1

    # Bonus if user wants photography and the place has photo zones.
    if "photography" in user_prefs["vibes"] and place.get("photo_zones"):
        score += 1

    # Bonus if user wants wildlife and the place has wildlife notes.
    if "wildlife" in user_prefs["vibes"] and place.get("wildlife"):
        score += 1

    return score


def get_recommendations(places, user_prefs):
    scored = []
    origin = user_prefs["origin"]

    for place in places:
        if origin not in place["drive_minutes"]:
            continue

        # Hard filter by maximum drive time.
        if place["drive_minutes"][origin] > user_prefs["max_drive"]:
            continue

        score = score_place(place, user_prefs)

        # Skip places with no real match.
        if score > 0:
            scored.append((score, place))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [place for score, place in scored[:3]]
