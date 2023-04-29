import json
import random

# Constants and enums


class Action:
    DIALOGUE = 1
    FIGHT = 2
    ESCAPE = 3


CHARACTER_FILE = "characters.json"
DESCRIPTION_CHOOSE_HERO = "Choose your hero:"
DESCRIPTION_ENCOUNTER_ENEMY = "Your hero encountered {enemy}. What will you do?"
DESCRIPTION_GAME_OVER = "The game is over. Your result: {result}."

# Created a dictionary with character characteristics
CHARACTERS = {
    "Catigoroshko": {"health": 100, "strength": 10},
    "Snake": {"health": 80, "strength": 15},
    "Horse": {"health": 120, "strength": 8}
}

# Save the dictionary of characters to a file
with open(CHARACTER_FILE, "w") as f:
    json.dump(CHARACTERS, f)

# Load the dictionary of characters from a file
with open(CHARACTER_FILE, "r") as f:
    CHARACTERS = json.load(f)

# Define the stages of the game
STAGES = [
    {
        "description": DESCRIPTION_CHOOSE_HERO,
        "actions": CHARACTERS.keys()
    },
    {
        "description": DESCRIPTION_ENCOUNTER_ENEMY,
        "actions": [Action.DIALOGUE, Action.FIGHT, Action.ESCAPE]
    },
    {
        "description": DESCRIPTION_GAME_OVER
    }
]

# Functions to handle each stage of the game


def select_character():
    print("Available characters:")
    for name, stats in CHARACTERS.items():
        print(
            f"{name} (health: {stats['health']}, strength: {stats['strength']})")
    character = input("Choose your hero: ")
    if character not in CHARACTERS:
        raise ValueError("Invalid character selection")
    return character


def encounter(enemy):
    print(f"Your hero met {enemy}. What will you do?")
    while True:
        try:
            action = int(input("1. Dialogue 2. Fight 3. Escape\n"))
            if action not in [Action.DIALOGUE, Action.FIGHT, Action.ESCAPE]:
                raise ValueError(
                    "Invalid action selection. Please choose 1, 2, or 3.")
            break
        except ValueError:
            print("Invalid action selection. Please choose 1, 2, or 3.")
    return action


def battle(player, enemy):
    player_stats = CHARACTERS[player]
    enemy_stats = CHARACTERS[enemy]
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

# Main Game


def play_game():
    stage_index = 0
    player = None
    enemy = None
    result = None

    while stage_index < len(STAGES):
        stage = STAGES[stage_index]

        # Handle the choose hero stage
        if stage_index == 0:
            player = select_character()
            print(f"You have chosen {player} as your hero.")

        # Handle the encounter enemy stage
        elif stage_index == 1:
            enemy = random.choice(list(CHARACTERS.keys()))
            print(stage['description'].format(enemy=enemy))
            action = encounter(enemy)
            if action == Action.DIALOGUE:
                print("You tried to talk to the enemy, but they didn't seem interested.")
            elif action == Action.FIGHT:
                result = battle(player, enemy)
                if result == "victory":
                    print(f"You defeated {enemy}! Congratulations!")
                elif result == "defeat":
                    print(f"You were defeated by {enemy}. Game over.")
                else:
                    print("It's a tie! Both you and the enemy have been defeated.")
            elif action == Action.ESCAPE:
                print("You run away from the enemy. Coward.")

        # Handle the game over stage
        elif stage_index == 2:
            if result == "victory":
                print(stage['description'].format(result="victory!"))
            else:
                print(stage['description'].format(result="defeat."))
            return

        # Move on to the next stage
        stage_index += 1


play_game()
