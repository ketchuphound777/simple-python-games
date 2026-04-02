
import random
import requests


url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(url)
data = response.json()
all_pokemon = data['results']
all_pokemon_names = [p['name'] for p in all_pokemon]
common_pokemon = []
uncommon_pokemon = []
rare_pokemon = []
legendary_pokemon = []


# Start the safari game
print("Welcome to the Pokemon Safari!")

input(" ")
player = input("Please enter your name: ")
print(f"Hello, {player}! Welcome to the Pokemon Safari!")
input(" ")

print("You will encounter different types of Pokemon in the safari.")
input(" ")
print("You may encounter common, uncommon, rare, or even legendary Pokemon.")
input(" ")
print("Try to catch as many Pokemon as you can!")
input(" ")
print("You will have 30 safari balls to catch pokemon. Once you run out of safari balls, the safari will end.")
input(" ")
print("Good luck, and have fun exploring the safari!")
input(" ")
print("One moment fetching Pokemon data from the API this may take awhile...")


caught_pokemon = []
safari_balls = 30


for name in all_pokemon_names:
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
    try:
        # add timeout to prevent hanging1
        species_response = requests.get(species_url, timeout=5)
        if species_response.status_code != 200:
            print(
                f"Skipping {name}, API returned {species_response.status_code}")
            continue
        species_data = species_response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Skipping {name}, request failed: {e}")
        continue

    if species_data["is_legendary"]:
        legendary_pokemon.append(name)
    else:
        roll = random.randint(1, 100)
        if roll <= 60:
            common_pokemon.append(name)
        elif roll <= 85:
            uncommon_pokemon.append(name)
        else:
            rare_pokemon.append(name)

# Safari game loop
while safari_balls > 0:
    roll = random.randint(1, 100)

    if roll == 1 and legendary_pokemon:
        # 1%
        wild_pokemon = random.choice(legendary_pokemon)
        print(f"\nA wild {wild_pokemon} appeared! It's a legendary pokemon!")

    elif roll <= 11 and rare_pokemon:
        # 10% (2–11)
        wild_pokemon = random.choice(rare_pokemon)
        print(f"\nA wild {wild_pokemon} appeared! It's a rare pokemon!")

    elif roll <= 51 and uncommon_pokemon:
        # 40% (12–51)
        wild_pokemon = random.choice(uncommon_pokemon)
        print(f"\nA wild {wild_pokemon} appeared! It's an uncommon pokemon!")

    elif common_pokemon:
        # Remaining 49% (52–100)
        wild_pokemon = random.choice(common_pokemon)
        print(f"\nA wild {wild_pokemon} appeared! It's a common pokemon!")

    else:
        # Emergency fallback if something is empty
        print("No Pokemon available to encounter.")

    pokerus_chance = random.randint(1, 65586)  # 1 in 65586 chance for pokerus
    shiny_chance = random.randint(1, 8192)  # 1 in 8192 chance for shiny
    if pokerus_chance == 1:
        print("Wow! A Pokemon with pokerus has appeared!")
    if shiny_chance == 1:
        print("Wow! A shiny Pokemon has appeared!")

    if wild_pokemon in legendary_pokemon:

        catch_chance, flee_chance = 5, 60
    elif wild_pokemon in common_pokemon:

        catch_chance, flee_chance = 70, 20

    elif wild_pokemon in uncommon_pokemon:

        catch_chance, flee_chance = 50, 40

    elif wild_pokemon in rare_pokemon:

        catch_chance, flee_chance = 30, 50
    while True:
        print(f"\nYou have {safari_balls} safari balls left.")
        print("\nChoose an action: ")
        print("1. Throw a safari ball")
        print("2. Throw a rock")
        print("3. Throw bait")
        choice = input("Choose an action (1, 2, or 3): ")

        if choice == "1":
            safari_balls -= 1
            if random.randint(1, 100) <= catch_chance:
                caught_pokemon.append(wild_pokemon)
                print(f"Congratulations! You caught {wild_pokemon}!")
                input("Press Enter to continue to the next encounter...")
                break
            elif random.randint(1, 100) <= flee_chance:
                print(
                    f"{wild_pokemon} broke free! {wild_pokemon} is watching carefully!")
            else:
                print(f"{wild_pokemon} fled!")
                input("Press Enter to continue to the next encounter...")
                break

        elif choice == "2":
            flee_chance += 10
            catch_chance -= 10
            flee_chance = max(0, min(100, flee_chance))
            catch_chance = max(0, min(100, catch_chance))
            if random.randint(1, 100) <= flee_chance:
                print(f"Oh no! The {wild_pokemon} fled!")
                input("Press Enter to continue to the next encounter...")
                break
            else:
                print(f"The {wild_pokemon} is angry but still there!")

        elif choice == "3":
            catch_chance += 10
            flee_chance -= 10
            flee_chance = max(0, min(100, flee_chance))
            catch_chance = max(0, min(100, catch_chance))
            if random.randint(1, 100) <= flee_chance:
                print(f"Oh no! The {wild_pokemon} fled!")
                input("Press Enter to continue to the next encounter...")
                break
            else:
                print(
                    f"The {wild_pokemon} is calm and still there!")

        else:
            print(f"{player} ran away from {wild_pokemon}!")
            break

    # End the safari
    # display a message that the safari has ended
print("\nThe safari has ended!")
print(f"You caught {len(caught_pokemon)} pokemon during the safari!")
if caught_pokemon:  # if the player caught any pokemon, display their names
    print("You caught the following pokemon:")
    for pokemon in caught_pokemon:
        print(f"- {pokemon}")
