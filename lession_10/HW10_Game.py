import random
import time
from hw_10_Logger import logger


class Hero:
    """Hero params"""
    def __init__(self, name: str, health: int, power: tuple, ability: str, greetings: str, gues: str, answer: int):

        self.name = name
        self.health = health
        self.power = power
        self.ability = ability
        self.greetings = greetings
        self.gues = gues
        self.answer = answer

    def introduce(self):
        print(f'- {self.name} - Health: {self.health} Attack power: {self.power[0]}-{self.power[1]} damage')

    def hello(self):
        print(f'>>> {self.name}: {self.greetings} I gotta shake your ass... But I\'ll give you a chance. \
You can answer my question... ')

    def attack(self):
        print(f'>>> {self.name}: Ha-ha-ha Yo\'ll be done!!!')

    def gues_action(self):
        print(f'>>> {self.name}: Okay listen my question: {self.gues}')


#  Heroes

warrior = Hero('Warrior', 100, (30, 40), 'punch', 'Loctar ogar! Who is there?', 'How much will be 11**2?', 121)
wizard = Hero('Wizard', 50, (50, 70), 'throw a lighting bolt', 'Hello, I am foxy wizard', 'How much will be 40/5?', 8)
dragon = Hero('Dragon', 200, (10, 20), 'blow the fire', 'I am hungry dragon', 'How much will be 1+3*4?', 13)
pm = Hero('PM', 200, (200, 250), 'Assign task', 'Попавсь, It\'s your PM', 'How much tasks passed today?', 10)

#  Heroes dict for selecting

heroes_dict = {'warrior': warrior, 'wizard': wizard, 'dragon': dragon, 'pm': pm}


def select_hero(user_select: str, heroes: dict) -> tuple:
    """Receives args from user and search it in heroes dict which should contain two and more heroes. If hero exists
     this name become bocked in heroes_dict for AI. AI make random selection hero for itself. """

    heroes_available = []
    try:
        for keys, values in heroes.items():
            if user_select != keys:
                heroes_available.append(values)

        player_hero = heroes[user_select]
        ai_hero = random.choice(heroes_available)  # Choose any hero except player
        heroes_available.remove(ai_hero)  # Remove AI hero from available heroes list
        return player_hero, ai_hero, heroes_available

    except KeyError as k:
        logger.error(f'Incorrect arg {k} received')
        print(f'>>> System: "{user_select}" hero doesn\'t exist!')


def is_ai_guess_answered(user_answer: str, ai_hero) -> bool:
    """Receives user answer then search correct answer correspond to each hero gues tasks"""
    try:
        return True if int(user_answer) == ai_hero.answer else False
    except ValueError as v:
        logger.error(f'Incorrect arg {v} received')
        print(f'>>> System: Answer is not correct')


def contact(player_hero, ai_hero, user_answer: str):
    """ Contact key game function. Player has the possibility start auto-fight
    or answer on AI guess or run. Player wins if AI defeated in battle or AI's guess answered correct or player runs.
    Player receives correspond message from system then battle terminates automatically.
    In case when AI's guess answered not correct auto-fight depend on player Hero and AI params starts.
    If player wins this battle he pass level (scene) else he looses the game.
    """

    #  Contact text variables

    system_congratulations = f'>>> System: Congratulations you\'ve asked {ai_hero.name}\'s question. And he left you.'
    system_runner = f'>>> System You are really good runner {ai_hero.name} couldn\'t catch you... '

    # Contact code

    if user_answer == 'F':
        time.sleep(3)  # Smooth next scene First AI hero passed appearing
        fight_result = battle(player_hero=player_hero, ai_hero=ai_hero)  # Get fight result
        return fight_result
    elif user_answer == 'G':
        time.sleep(3)  # Smooth next scene First AI hero passed appearing
        ai_hero.gues_action()
        user_gues_answer = input('>>> You: ')
        gues_result = is_ai_guess_answered(user_gues_answer, ai_hero=ai_hero)  # Get gues result
        if gues_result:
            print(system_congratulations)
            return gues_result
        else:
            ai_hero.attack()  # AI attacks in case when player didn't ask the question
            fight_result = battle(player_hero=ai_hero, ai_hero=player_hero)  # AI attacks and starts battle first
            return fight_result
    elif user_answer == 'R':
        run_result = True  # Return for testing
        time.sleep(3)  # Smooth next scene First AI hero passed appearing
        print(system_runner)
        return run_result
    else:
        print('>>> System: Try again!')


def battle(player_hero, ai_hero) -> str:
    """Battle function by default player attacks first. Each hero uses correspond to him ability avg power attack
     and health points Returns name of winner"""

    while player_hero.health or ai_hero.health:

        print(f'>>> System: Bloody battle between {player_hero.name} and {ai_hero.name} starts...  ')
        player_strike = random.randrange(player_hero.power[0], player_hero.power[1])  # Get avg attack power
        print(f'>>> System: You {player_hero.ability} on {player_strike} damage.')
        ai_hero.health -= player_strike
        if ai_hero.health <= 0:
            print(f'>>> System: You are making final strike {ai_hero.name} looses the battle.')
            return player_hero.name
        else:
            print(f'>>> System: {ai_hero.name} still has {ai_hero.health} health points.')
            time.sleep(3)  # Smooth next action scene appearing

        ai_strike = random.randrange(ai_hero.power[0], ai_hero.power[1])  # Get avg attack power
        print(f'>>> System: {ai_hero.name} {ai_hero.ability} on {ai_strike} damage.')
        player_hero.health -= ai_strike
        if player_hero.health <= 0:
            return ai_hero.name
        else:
            print(f'>>> System: You are still have {player_hero.health} health points.')
            time.sleep(3)  # Smooth next action scene appearing


def action(player_hero, ai_hero) -> str:
    """Receive users action selecting and defines result of action.
    Player win level or AI"""

    user_answer = ''
    while user_answer not in ('F', 'G', 'R'):
        user_answer = input(f'>>> System: Type \'F\' - Fight with {ai_hero.name}, \'G\' guess {ai_hero.name}\'s task \
or \'R\'- run out here. You: ').upper()
        continue

    contact_result = contact(player_hero=player_hero, ai_hero=ai_hero, user_answer=user_answer)
    if contact_result == ai_hero.name:
        print(f'{ai_hero.name} is making final strike. You loose the battle.\nGame over!')
        return ai_hero.name
    else:
        time.sleep(3)  # Smooth next scene First AI hero passed appearing
        print(f'>>> System: Congratulations {ai_hero.name} hero level passed !!!')
        return player_hero.name


def game():
    """Main game function. Presenting to user heroes then user select hero. Then
    'adventures' start. Player meets one random AI hero with correspond greetings, abilities, guess, attack power.
    AI never selects players hero. Then Meets another random Ai hero.
    Game ends when both AI heroes passed.
    """
    global player, ai, players_available

    # System greetings scene

    print('>>> System: Welcome to Magic Island Adventures!')
    time.sleep(3)  # Smooth next action Presenting heroes appearing
    print('>>> System: Choose your hero!')
    for hero in heroes_dict.values():
        hero.introduce()  # Pretty heroes presenting
        time.sleep(1)  # Smooth heroes appearing

    # Players selecting code

    while True:  # Validate hero in heroes_dict
        user_hero = input('>>> (Type hero name to continue) You: ').lower()
        players_selected = select_hero(user_select=user_hero, heroes=heroes_dict)
        if players_selected is None:
            continue
        else:
            player = players_selected[0]
            ai = players_selected[1]
            players_available = players_selected[2]
            break

    print(f'>>> System: Cool, {player.name} chosen, good luck!')
    time.sleep(3)  # Smooth next action scene appearing

    # AI hero action scene

    print(f'>>> System: After long walking around island you met a {ai.name}...')
    time.sleep(3)  # Smooth next scene greetings from AI appearing

    ai.hello()
    time.sleep(3)  # Smooth next action scene appearing
    action_result = action(player_hero=player, ai_hero=ai)

    # AI 2 hero action scene

    if action_result == player.name:  # Second scene starts if player winner
        time.sleep(3)  # Smooth next action scene appearing

        ai2 = random.choice(players_available)  # Get random AI 2 key

        print(f">>> System: You continue your adventure through island and meet {ai2.name} ...")
        time.sleep(3)  # Smooth next scene greetings from AI 2 appearing
        ai2.hello()
        time.sleep(3)  # Smooth next action scene appearing
        action(player_hero=player, ai_hero=ai2)
        time.sleep(3)  # Smooth next action scene appearing

        print('>>> System: Congratulations \
After long treasure search you finally find it. You won the game!!!')


#  game()
