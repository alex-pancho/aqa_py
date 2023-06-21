import random
from my_logger import logger

#defy characters for gameplay

characters = {"1":{"name":"Geralt", "power" : 100},
              "2" : {"name":"Bruxa", "power" : 80}, 
              "3" : {"name":"Werewolf", "power" : 50}}

#defy possible game`s results
game_result = ["Wow! You win!", "It's a draw! Come back later", "Oops! You lose, R.I.P."]

#defy actions for gameplay and exceptions
class InvalidInputException(Exception):
    def __init__(self, input):
        self.input = input

    def __str__(self):
        logger.error(f"Player has made invalid input")
        return f"Invalid input: {self.input}"


def fight(power_player:int, power_comp:int):
    logger.info(f"Player's power - {power_player}, opponent's power - {power_comp}")
    if power_player > power_comp:
        logger.info("Player wins")
        return(game_result[0])
    elif power_player == power_comp:
        logger.info("Draw")
        return(game_result[1])
    else:
        logger.info("Player loses")
        return(game_result[2])
        
def play_gwent(random_power:int, power_comp:int):
    logger.info(f"Player's power - {random_power}, opponent's power - {power_comp}")
    if random_power > power_comp:
        logger.info("Player wins")
        return(game_result[0])
    elif random_power == power_comp:
        logger.info("Draw")
        return(game_result[1])
    else:
        logger.info("Player loses")
        return(game_result[2])
    
def sing_a_song():
    logger.info("Player wins with a cheatcode")
    return("You found secret superpowers and win!")

game_actions = {"1": fight, 
                "2": play_gwent,
                "3": sing_a_song}


#user chooses character and can see the choice

choose_char = input("Now you are entering the Dark forest. \nChoose your character: 1. Geralt 2. Bruxa 3. Werewolf  ")

def define_player(choose_char):

    if choose_char == "1":
        return characters["1"]
    elif choose_char == "2":
        return characters["2"]
    elif choose_char == "3":
        return characters["3"]
    elif not choose_char in characters.keys():
        raise InvalidInputException("Choose one of three available characters using their numbers")   

def define_opponents(choose_char):
    if choose_char in characters.keys():
        return {k: v for k, v in characters.items() if k != choose_char}
    elif not choose_char in characters.keys():
        raise InvalidInputException("Choose one of three available characters using their numbers")   

char_of_player = define_player(choose_char)
opponents = define_opponents(choose_char)

print(opponents)
print(f"Hello,", char_of_player["name"])


# introducing opponents and fighting
for opponent in opponents:
    print(f"Prepare to fight...", opponents[opponent]["name"], "!")
    choose_action = input("What will you do? 1. Fight 2. Play Gwent 3. Sing a song  ")

    
    #powers to compare in actions
    power_of_player = char_of_player["power"]
    power_of_comp = opponents[opponent]["power"]
    random_power = random.choice(list(range(100)))
    
    def choosing_action(choose_action):
        if choose_action == "1":
            game_res = fight(power_of_player, power_of_comp)
            print(game_res)
            if game_res == game_result[0] or game_res == game_result[1]:
                continue
            elif game_res == game_result[2]:
                break
        elif choose_action == "2":
            print("Let's see how lucky you can be...")
            print(random_power)
            game_res = play_gwent(random_power=random_power, power_comp=power_of_comp)
            print(game_res)
            if game_res == game_result[0] or game_res == game_result[1]:
                continue
            elif game_res == game_result[2]:
                break
        elif choose_action == "3":
            game_res = sing_a_song(power_initial=power_of_player)
            print(game_res)
            if game_res == game_result[0] or game_res == game_result[1]:
                continue
            elif game_res == game_result[2]:
                break  
        elif choose_action not in game_actions.keys():
            logger.error(f"Player has made the wrong choce, there is no such character")
            raise InvalidInputException("Choose one of three available actions using their numbers")
    # finally: 
    #     logger.info(f"Chosen action was {choose_action}, game result is {game_result}")
              
    
print("Thanks for playing!")    
