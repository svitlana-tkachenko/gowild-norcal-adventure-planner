def make_maps_link(origin, destination):
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    return f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}"


def suggest_departure(drive_minutes, mode):
    if mode == "sunset":
        return f"Leave ~{drive_minutes + 60} min before sunset"
    elif mode in ["night", "stargazing"]:
        return "Leave after 8 PM for dark skies"
    else:
        return "Leave early morning to avoid crowds"


def format_result(place, origin, mode="day"):
    drive = place["drive_minutes"][origin]
    link = make_maps_link(origin, place["maps_query"])
    wildlife = place.get("wildlife", [])
    photo_zones = place.get("photo_zones", [])

    lines = [
        f"\n╔══════════════════════════════════════╗",
        f"  🌿 {place['name'].upper()}",
        f"  {place['description']}",
        f"╚══════════════════════════════════════╝",
        f"",
        f"  Drive:      ~{drive} min from {origin}",
        f"  Best time:  {place['best_time']}",
        f"  Depart:     {suggest_departure(drive, mode)}",
        f"  Difficulty: {place['difficulty']}",
        f"  Weather:    {place['weather_note']}",
    ]

    if wildlife:
        lines.append(f"  Wildlife:   {', '.join(wildlife)}")

    if photo_zones:
        lines.append(f"  Photo:      {', '.join(photo_zones)}")

    if place.get("sky_note"):
        lines.append(f"  Sky:        {place['sky_note']}")

    lines.append(f"  Map:        {link}")

    return "\n".join(lines)
