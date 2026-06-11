from data import PLACES
from recommender import get_recommendations
from utils import format_result


def ask_origin():
    print("Where are you starting from?")
    print("1. San Jose")
    print("2. San Francisco")
    choice = input("Your choice (1/2): ").strip()
    return {"1": "San Jose", "2": "San Francisco"}.get(choice, "San Jose")


def ask_time():
    print("\nHow much time do you have for driving?")
    print("1. Up to 1 hour")
    print("2. Up to 1.5 hours")
    print("3. Up to 2.5 hours")
    choice = input("Your choice (1/2/3): ").strip()
    return {"1": 60, "2": 90, "3": 150}.get(choice, 90)


def ask_mode():
    print("\nWhat kind of trip?")
    print("1. Day trip")
    print("2. Sunset / golden hour")
    print("3. Night")
    print("4. Stargazing")
    choice = input("Your choice (1/2/3/4): ").strip()
    return {"1": "day", "2": "sunset", "3": "night", "4": "stargazing"}.get(choice, "day")


def ask_stargazing_goal():
    print("\nWhat's your stargazing goal?")
    print("1. Easy viewpoint — quick and accessible")
    print("2. Real dark sky — away from city lights")
    print("3. Astrophotography — best photo conditions")
    choice = input("Your choice (1/2/3): ").strip()
    return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "medium")


def ask_vibes():
    print("\nWhat are you into? (pick all that apply, e.g. 1 3 4)")
    options = [
        "hiking", "ocean", "forest", "wildlife", "photography",
        "sunset", "caves", "water", "views", "hills",
        "surf", "chill", "stargazing"
    ]
    for i, v in enumerate(options, 1):
        print(f"{i}. {v}")
    choices = input("Your choices: ").strip().split()
    vibes = [options[int(c) - 1] for c in choices if c.isdigit() and 1 <= int(c) <= len(options)]
    return vibes if vibes else ["views"]


def ask_difficulty():
    print("\nDifficulty?")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Your choice (1/2/3): ").strip()
    return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "easy")


def main():
    print("=" * 50)
    print("   GoWild NorCal Adventure Planner")
    print("   California nature trips, curated for you")
    print("=" * 50)

    mode = ask_mode()
    origin = ask_origin()
    max_drive = ask_time()

    if mode == "stargazing":
        difficulty = ask_stargazing_goal()
        vibes = ["stargazing", "photography"]
    else:
        vibes = ask_vibes()
        difficulty = ask_difficulty()

    user_prefs = {
        "origin": origin,
        "max_drive": max_drive,
        "mode": mode,
        "vibes": vibes,
        "difficulty": difficulty,
    }

    results = get_recommendations(PLACES, user_prefs)

    print("\n" + "=" * 50)
    print("   Your top adventures:")
    print("=" * 50)

    if not results:
        print("\n   No matches found. Try adjusting your preferences.")
    else:
        for place in results:
            print(format_result(place, user_prefs["origin"], user_prefs["mode"]))

    print("\n" + "=" * 50)
    print("   Go outside. Touch grass. Take photos.")
    print("=" * 50)


if __name__ == "__main__":
    main()
