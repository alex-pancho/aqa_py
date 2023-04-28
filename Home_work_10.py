import json
import random


# Created a dictionary with character characteristics
characters = {
    "Catigoroshko": {"health": 100, "strength": 10},
    "Snake": {"health": 80, "strength": 15},
    "Horse": {"health": 120, "strength": 8}
}

# Save the dictionary of characters to a file
with open("characters.json", "w") as f:
    json.dump(characters, f)

# Load the dictionary of characters from a file
with open("characters.json", "r") as f:
    characters = json.load(f)

# Define the stages of the game
stages = [
    {
        "description": "Choose your hero:",
        "actions": characters.keys()
    },
    {
        "description": "Your hero encountered {enemy}. What will you do?",
        "actions": ["Dialogue", "Fight", "Escape"]
    },
    {
        "description": "The game is over. Your result: {result}."
    }
]

# Functions to handle each stage of the game


def select_character():
    print("Available characters:")
    for name, stats in characters.items():
        print(
            f"{name} (health: {stats['health']}, strength: {stats['strength']})")
    character = input("Choose your hero: ")
    if character not in characters:
        raise ValueError("Invalid character selection")
    return character


def encounter(enemy):
    print(f"Your hero met {enemy}. What will you do?")
    while True:
        action = input("1. Dialogue 2. Fight 3. Escape\n")
        try:
            action = int(action)
            if action not in [1, 2, 3]:
                raise ValueError(
                    "Invalid action selection. Please choose 1, 2, or 3.")
            break
        except ValueError:
            print("Invalid action selection. Please choose 1, 2, or 3.")
    return action


def battle(player, enemy):
    player_stats = characters[player]
    enemy_stats = characters[enemy]
    print(
        f"{player} (health: {player_stats['health']}, strength: {player_stats['strength']}) vs {enemy} (health: {enemy_stats['health']}, strength: {enemy_stats['strength']})")
    player_damage = random.randint(1, player_stats['strength'])
    enemy_damage = random.randint(1, enemy_stats['strength'])
    player_stats['health'] -= enemy_damage
    enemy_stats['health'] -= player_damage
    if player_stats['health'] <= 0 and enemy_stats['health'] <= 0:
        return "tie"
    elif player_stats['health'] <= 0:
        return "defeat"
    elif enemy_stats['health'] <= 0:
        return "victory"
    else:
        return None

# Main game function


def play_game():
    # Choosing a character
    try:
        character = select_character()
    except ValueError:
        print("Invalid character selection. Please choose one of the available characters.")
        return

    # Main game loop
    result = None
    for stage in stages:
        if stage["description"] == "Your hero encountered {enemy}. What will you do?":
            enemy = random.choice(
                [c for c in characters.keys() if c != character])
            stage["description"] = stage["description"].format(enemy=enemy)
            action = encounter(enemy)
            if action == 1:
                print(f"{character} attempts to engage {enemy} in dialogue.")
            elif action == 2:
                result = battle(character, enemy)
                if result == "tie":
                    print("Both heroes struck each other down. It's a tie.")
                    break
                elif result == "victory":
                    print(f"{character} defeated {enemy} in battle!")
                else:
                    print(f"{character} was defeated by {enemy} in battle.")
                    break
            else:
                print(f"{character} fled from {enemy}.")
                break
        elif stage["description"] == "The game has ended. Your result: {result}.":
            stage["description"] = stage["description"].format(result=result)
            print(stage["description"])
            break


play_game()
