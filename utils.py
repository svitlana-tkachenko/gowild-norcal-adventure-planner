def make_maps_link(origin, destination):
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    return f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}"


def format_result(place, origin):
    drive = place["drive_minutes"][origin]
    link = make_maps_link(origin, place["maps_query"])

    wildlife = place.get("wildlife", [])
    photo_zones = place.get("photo_zones", [])

    lines = [
        f"\n🌿 {place['name']}",
        f"   Drive: ~{drive} min from {origin}",
        f"   Vibe: {', '.join(place['vibes'])}",
        f"   Best time: {place['best_time']}",
        f"   Wildlife: {', '.join(wildlife) if wildlife else 'Not specified'}",
        f"   Photo zones: {', '.join(photo_zones) if photo_zones else 'Not specified'}",
        f"   Weather: {place['weather_note']}",
    ]

    if place.get("sky_note"):
        lines.append(f"   Sky: {place['sky_note']}")

    lines.append(f"   {place['description']}")
    lines.append(f"   Map: {link}")

    return "\n".join(lines)
