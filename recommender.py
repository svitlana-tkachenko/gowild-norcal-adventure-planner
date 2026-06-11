def score_place(place, user_prefs):
    score = 0

    # Give extra weight when the place matches several user interests.
    for vibe in user_prefs["vibes"]:
        if vibe in place["vibes"]:
            score += 2

    # Strong bonus when the place fits the trip mode (day/sunset/night/stargazing).
    if user_prefs["mode"] in place["modes"]:
        score += 3

    # Stargazing trips need stronger matching — dark sky places get extra weight.
    if user_prefs["mode"] == "stargazing" and place.get("stargazing"):
        score += 2

    if place["difficulty"] == user_prefs["difficulty"]:
        score += 1

    if "photography" in user_prefs["vibes"] and place.get("photo_zones"):
        score += 1

    if "wildlife" in user_prefs["vibes"] and place.get("wildlife"):
        score += 1

    return score


def get_recommendations(places, user_prefs):
    scored = []
    origin = user_prefs["origin"]

    for place in places:
        if origin not in place["drive_minutes"]:
            continue

        # Drive time is a dealbreaker, not just a preference.
        if place["drive_minutes"][origin] > user_prefs["max_drive"]:
            continue

        # For stargazing, only show places with confirmed dark skies.
        # "Okay at night" is not the same as a real stargazing spot.
        if user_prefs["mode"] == "stargazing" and not place.get("stargazing"):
            continue

        score = score_place(place, user_prefs)

        if score > 0:
            scored.append((score, place))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [place for score, place in scored[:3]]
