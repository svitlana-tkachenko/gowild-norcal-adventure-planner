import random
from data import PLACES
from recommender import get_recommendations
from utils import format_result
from card import show_cards


def ask_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def ask_origin():
    # San Jose and SF cover most Bay Area users.
    # Both are within reasonable driving distance of NorCal nature spots.
    print("Where are you starting from?")
    print("1. San Jose")
    print("2. San Francisco")
    choice = ask_choice("Your choice (1/2): ", ["1", "2"])
    return {"1": "San Jose", "2": "San Francisco"}[choice]


def ask_time():
    print("\nHow much time do you have for driving?")
    print("1. Up to 1 hour")
    print("2. Up to 1.5 hours")
    print("3. Up to 2.5 hours")
    choice = ask_choice("Your choice (1/2/3): ", ["1", "2", "3"])
    return {"1": 60, "2": 90, "3": 150}[choice]


def ask_mode():
    print("\nWhat kind of trip?")
    print("1. Day trip")
    print("2. Sunset / golden hour")
    print("3. Night")
    print("4. Stargazing")
    choice = ask_choice("Your choice (1/2/3/4): ", ["1", "2", "3", "4"])
    return {"1": "day", "2": "sunset", "3": "night", "4": "stargazing"}[choice]


def ask_stargazing_goal():
    # Stargazing has its own flow because the relevant factors are different:
    # dark sky quality matters more than hiking difficulty.
    print("\nWhat's your stargazing goal?")
    print("1. Easy viewpoint — quick and accessible")
    print("2. Real dark sky — away from city lights")
    print("3. Astrophotography — best photo conditions")
    choice = ask_choice("Your choice (1/2/3): ", ["1", "2", "3"])
    return {"1": "easy", "2": "medium", "3": "hard"}[choice]


def ask_vibes():
    print("\nWhat are you into? (pick all that apply, e.g. 1 3 4)")
    print("0. Surprise me — pick for me randomly")
    options = [
        "hiking", "ocean", "forest", "wildlife", "photography",
        "sunset", "caves", "water", "views", "hills",
        "surf", "chill", "stargazing"
    ]
    for i, v in enumerate(options, 1):
        print(f"{i}. {v}")
    while True:
        choices = input("Your choices: ").strip().split()

        # Surprise me mode: randomly picks 2-3 vibes
        if choices == ["0"]:
            selected = random.sample(options, random.randint(2, 3))
            print(f"\nSurprise! Your adventure goal: {', '.join(selected)}")
            return selected

        vibes = [options[int(c) - 1] for c in choices if c.isdigit() and 1 <= int(c) <= len(options)]
        if vibes:
            return vibes
        print("Invalid choice. Please enter one or more numbers from the list.")


def ask_difficulty():
    print("\nDifficulty?")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = ask_choice("Your choice (1/2/3): ", ["1", "2", "3"])
    return {"1": "easy", "2": "medium", "3": "hard"}[choice]


def save_plan(results, prefs):
    origin = prefs["origin"]
    filename = "my_trip_plan.txt"
    with open(filename, "w") as f:
        f.write("GOWILD NORCAL — MY TRIP PLAN\n")
        f.write("=" * 40 + "\n\n")
        for i, place in enumerate(results, 1):
            drive = place["drive_minutes"][origin]
            f.write(f"{i}. {place['name']}\n")
            f.write(f"   Drive: ~{drive} min from {origin}\n")
            f.write(f"   Best time: {place['best_time']}\n")
            f.write(f"   {place['description']}\n")
            link = f"https://www.google.com/maps/dir/?api=1&origin={origin.replace(' ', '+')}&destination={place['maps_query'].replace(' ', '+')}\n"
            f.write(f"   Map: {link}\n")
    print(f"\nPlan saved to {filename}")


def main():
    print("=" * 50)
    print("   GoWild NorCal Adventure Planner")
    print("   California nature trips, curated for you")
    print("=" * 50)

    mode = ask_mode()
    origin = ask_origin()
    max_drive = ask_time()

    if mode == "stargazing":
        # Stargazing gets its own question set — no vibes needed,
        # since the hard filter already ensures only stargazing spots show up.
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
        show_cards(results, user_prefs)
        for place in results:
            print(format_result(place, user_prefs["origin"], user_prefs["mode"]))

        # Optional: save plan to file
        save = input("\nSave your plan to a file? (y/n): ").strip().lower()
        if save == "y":
            save_plan(results, user_prefs)

    print("\n" + "=" * 50)
    print("   Go outside. Touch grass. Take photos.")
    print("=" * 50)


if __name__ == "__main__":
    main()
