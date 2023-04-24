import random
from my_logger import logger

heroes = {
    'Жаба': {
        'особливість': 'дооовгий язик',
        'енергія': 100
    },
    'Віслюк': {
        'особливість': 'неперевершена посмішка',
        'енергія': 100
    },
    'Кіт у чоботях': {
        'особливість': 'пишний хвіст',
        'енергія': 100
    }
}

hero = 'Жаба'
ready = 'undefined'
name = 'undefined'
beer_count = 0
games = 0
points = 0
kurka = 0


def end():
    """Кінець гри, коли гравець витратив всю енергію"""
    if heroes[hero]["енергія"] <= 0:
        if points >= 0:
            print(f'Що ж, от і все на сьогодні, друже, {heroes[hero]["name"]}, ти витратив всю енергію!\n'
                  f'Ти зіграв {games} ігор\n'
                  f'Випив {beer_count} келихів пива\n'
                  f'Заробив {points} балів!')
            logger.info(f'Гра скінчилася. Ігри: {games}, келихи: {beer_count}, бали: {points}')
        else:
            print(f'Що ж, от і все на сьогодні, друже, {heroes[hero]["name"]}, ти витратив всю енергію!\n'
                  f'Ти зіграв {games} ігор\n'
                  f'Випив {beer_count} келихів пива\n'
                  f'Пішов у мінус {abs(points)} балів!')
            logger.info(f'Гра скінчилася. Ігри: {games}, келихи: {beer_count}, бали: {points}')
    if heroes[hero]["енергія"] > 0:
        if points >= 0:
            print(f'Що ж, от і все на сьогодні, друже, {heroes[hero]["name"]}!\n'
                  f'Ти зіграв {games} ігор\n'
                  f'Випив {beer_count} келихів пива\n'
                  f'Заробив {points} балів!')
            logger.info(f'Гра скінчилася. Ігри: {games}, келихи: {beer_count}, бали: {points}')
        else:
            print(f'Що ж, от і все на сьогодні, друже, {heroes[hero]["name"]}!\n'
                  f'Ти зіграв {games} ігор\n'
                  f'Випив {beer_count} келихів пива\n'
                  f'Пішов у мінус {abs(points)} балів!\n')
            logger.info(f'Гра скінчилася. Ігри: {games}, келихи: {beer_count}, бали: {points}')


def start():
    """Гра почалась, гравець обирає свого казкового персонажа"""
    print('Ви заходите до таверни магічних істот і одразу бачите похмурий погляд хазяїна, він підходить до Вас '
          'насупивши одну бров')

    global ready
    global hero
    global name

    while ready != 'так':
        hero = input('-Що ти таке? Жаба? Віслюк? Чи може кіт у чоботях!? ').capitalize()
        if hero in heroes:
            ready = input('Ти впевнений? Просте питання, так чи ні?: ').lower()
            if ready == 'так' or ready == 'да':
                break
            else:
                print('Добре, подумай ще трішки')
                continue
        else:
            print(f'Щось я не впевнений, що ти той за кого себе видаєш {hero}, ти більше схож на щось з переліку вище')

    logger.info(f'Героя обрано, герой: {hero}')

    print(f'О так, я зрзумів це одразу як побачив, що в тебе {heroes[hero]["особливість"]}, '
          f'та просто хотів тебе перевірити!')
    name = input(f'А тепер скажи но мені, {hero}, як тебе звуть? (придумайте власне ім`я для персонажа) ')
    heroes[hero]['name'] = name
    print(f'Приємно з тобою познайомитися, {name}')
    print('Ну що, пограємо?')
    logger.info(f'Персонажа створено. Обраний герой: {hero}, ім`я: {name}')

    return choose_game()


def choose_game():
    """Вибір гри"""
    print('Дивись, є декілька ігор на вибір: "Вгадай число", "Куркулятор", "Слово", чи завжди можна просто хильнути \n'
          'келих пінного, якщо просто скажеш мені "пиво". А якщо ти вже награвся, то просто скажи "кінець" і я порахую '
          'зароблені тобою бали')

    global beer_count
    global games
    global name

    logger.info(f'Бали: {points}, енергія: {heroes[hero]["енергія"]}, ігри :{games}, келихи: {beer_count}, '
                f'ігор в куркулятор: {kurka}')

    if heroes[hero]['енергія'] <= 0:
        return end()

    choose = input("То що ти обрав? ").lower()

    if choose == 'куркулятор':
        print('*Ви підходите до сцени*\n'
              '-Пані, та панове, Ви бачите перед собою ніщо інше як диво дивовижне, курку! Та не просто дурновату \n'
              'тварину з Вашого городу, а розумну курку, що навчилася рахувати! Ви можете задати їй будь-які цифри \n'
              'і дію яку потрібно виконати і вона Вам Їх порахує! Курка може робити: "віднімання", "додавання", \n'
              '"ділення", "множення", брати заданий відсоток від заданого числа та зводити у "ступінь"! '
              'Ось, Ви, наприклад\n '
              '*показує на Вас, Ви озираєтесь навколо себе*\n'
              f'-Так, саме Ви, {hero}, я до Вас говорю, спробуйте!')

        print(kurka_validator(num_1=input('Введи перше число '), num_2=input('Введи друге число '),
                              action=input('Введи дію ')))
        return choose_game()
    if choose == 'пиво' and beer_count < 10:
        heroes[hero]['енергія'] -= 1
        print('Келих пива за рахунок закладу нашому гостю!')
        print('Ваша енергія зменшилась на 1')
        logger.info(f'Келихи: {beer_count}, енергія: {heroes[hero]["енергія"]}')
        print(beer())
        return choose_game()
    if choose == 'пиво' and beer_count == 10:
        print('Ти вже достатньо випив, друже! Побережи себе та свою енергію для ігор!')
        return choose_game()
    if choose == 'кінець' and games == 0:
        print('Гей, друже, ти навіть не зіграв ще жодної гри, мій гість не може так просто піти!')
        return choose_game()
    if choose == 'кінець' and games > 0:
        print(f'Що ж, приємно було мати з тобою справу, {hero}!')
        return end()
    if choose == 'вгадай число':
        print('Пані, та панове, перед Вами магічний шар, що загадує число, яке Ви в свою чергу повинні відгадати.'
              'Число може бути від 1 до 100, вдалої гри!')
        return guess_number()
    if choose == 'слово':
        print(f'О, {hero}, як добре, що Ви не пройшли повз мене! Мене звати Лис-перевернис, скажіть мені слово і\n'
              f'я скажу Вам, чи отримаю те саме слово якщо прочитаю його задом наперед! Якщо це так, то Ви отримаєте \n'
              f'Але майте на увазі, що слово повинно містити лише букви і не менше аніж три букви та не більше аніж '
              f'10, інакше я не зможу нічого зробити!\n'
              f'До того ж, зауважу ще й те, що регістр букв не має значення!')
        print(word_validator(word=input('Введіть слово ')))
        return choose_game()
    else:
        print(f"На жаль цього я тобі дати не можу, {heroes[hero]['name']}")
        return choose_game()


def beer():
    global beer_count
    beer_count += 1
    return '*Ви кажете:* "Львівське різдвяне, це я люблю!"'


def word_validator(word: str):
    if word.isalpha():
        logger.info('Слово коректне')
        return palindrom_word(word)
    logger.info('Слово некоректне')
    return 'Я ж сказав, тільки букви!'


def kurka_validator(num_1, num_2, action: str):
    if num_1.isdigit() and num_2.isdigit:
        num_1 = float(num_1)
        num_2 = float(num_2)
        logger.info('Обидва числа коректні')
        return curculator(num_1, num_2, action)
    logger.info('Одне чи обидва числа некоректні')
    return 'Курка вміє рахувати лише числа!'


def curculator(num_1, num_2, action: str):
    """Магічна курка, що може робити зовсім недитячі обчислення"""

    global kurka
    global points
    global games

    if kurka == 10:
        return 'Курка вже втомилась рахувати!'

    kurka += 1
    games += 1
    heroes[hero]['енергія'] -= 1
    logger.info(f'Ігор зіграно:{games}, зіграно у куркулятор:{kurka}, енергія:{heroes[hero]["енергія"]}')

    if action == 'віднімання' or action == 'відняти' or action == 'мінус' or action == '-':
        points += 1
        logger.info(f'Бали: {points}, відповідь курки: {num_1} - {num_2} = {num_1 - num_2}')
        return f'Курка каже: {float(num_1 - num_2)}\n' \
               f'Ви отримали 1 бал!\n' \
               f'Ви втратили 1 енергії'
    if action == 'додавання' or action == 'додати' or action == 'плюс' or action == '+':
        points += 1
        logger.info(f'Бали: {points}, відповідь курки: {num_1} + {num_2} = {num_1 + num_2}')
        return f'Курка каже: {float(num_1 + num_2)}\n' \
               f'Ви отримали 1 бал!\n' \
               f'Ви втратили 1 енергії'
    if action == 'множення' or action == 'помножити' or action == '*':
        points += 1
        logger.info(f'Бали: {points}, відповідь курки: {num_1} * {num_2} = {num_1 * num_2}')
        return f'Курка каже: {float(num_1 * num_2)}\n' \
               f'Ви отримали 1 бал!\n' \
               f'Ви втратили 1 енергії'
    if action == 'ділення' or action == 'ділити' or action == 'поділити' or action == '/':
        if num_2 == 0:
            try:
                num_1 / num_2
            except ZeroDivisionError:
                points -= 10
                logger.info(f'Бали: {points}, відповідь курки: "ZeroDivisionError"')
                return f'Курка дзьобає Вас у лоба і правильно робить, тому що на нуль ділити не можна!\n' \
                       f'Ви втратили 10 балів!\n' \
                       f'Ви втратили 1 енергії'
        else:
            points += 1
            logger.info(f'Бали: {points}, відповідь курки: {num_1} / {num_2} = {num_1 / num_2}')
            return f'Курка каже: {float(num_1 / num_2)}\n' \
                   f'Ви отримали 1 бал!\n' \
                   f'Ви втратили 1 енергії'
    if action == 'ступінь' or action == '**':
        points += 1
        logger.info(f'Бали: {points}, відповідь курки: {num_1} ** {num_2} = {num_1 ** num_2}')
        return f'Курка каже: {float(num_1 ** num_2)}\n' \
               f'Ви отримали 1 бал!\n' \
               f'Ви втратили 1 енергії'
    if action == 'відсоток' or action == '%':
        points += 1
        logger.info(f'Бали: {points}, відповідь курки: {num_1} відсотки від {num_2} = {(num_2 / 100) * num_1}%')
        return f'Курка каже: {float((num_2 / 100) * num_1)}%\n' \
               f'Ви отримали 1 бал!\n' \
               f'Ви втратили 1 енергії'
    else:
        points -= 10
        logger.info(f'Бали: {points}, відповідь курки: Неправильна дія')
        return f'Курка дзьобає Вас у лоба і правильно робить, бо звісно ж як курка зробить {action}, майте совість!\n' \
               f'Ви втратили 10 балів!\n' \
               f'Ви втратили 1 енергії'


def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            logger.info('Число коректне')
            return True
        else:
            logger.info('Число некоректне')
            return False
    logger.info('Число некоректне')
    return False


def guess_number():
    """Гра, вгадай число"""

    global points
    global games

    games += 1
    guess_num = random.randint(1, 100)

    logger.info(f'Енергія: {heroes[hero]["енергія"]}, ігри: {games}, бали: {points}, загадане число: {guess_num}')

    while True:
        user_num = input('Введіть число від 1 до 100: ')
        if not is_valid(user_num):
            points -= 10
            heroes[hero]['енергія'] -= 5
            if heroes[hero]['енергія'] <= 0:
                return end()
            logger.info(f'Неправильне число, бали: {points}, енергія: {heroes[hero]["енергія"]}')
            print('Так діло не піде, треба ввести саме від 1 до 100! Штраф 10 балів! До того ж втрата 5 енергії!')
            continue
        user_num = int(user_num)

        if user_num < guess_num:
            print('Ваше число менше ніж загадане, спробуйте ще! Ви втратили 5 енергії!')
            heroes[hero]['енергія'] -= 5
            logger.info(f'Неправильне число, бали: {points}, енергія: {heroes[hero]["енергія"]}')
            if heroes[hero]['енергія'] <= 0:
                return end()
        elif user_num > guess_num:
            print('Ваше число більше ніж загадане, спробуйте ще раз! Ви втратили 5 енергії!')
            heroes[hero]['енергія'] -= 5
            logger.info(f'Неправильне число, бали: {points}, енергія: {heroes[hero]["енергія"]}')
            if heroes[hero]['енергія'] <= 0:
                return end()
        else:
            print('Ви вгадали, вітаю! Ви заробили 30 балів!')
            points += 30
            logger.info(f'Правильне число, бали: {points}, енергія: {heroes[hero]["енергія"]}')
            break

    return choose_game()


def palindrom_word(word: str):
    """Паліндром числа"""

    global games
    global points

    games += 1

    word = word.lower()
    inverse = word[::-1]
    if word == inverse and 3 <= len(word) <= 10:
        heroes[hero]["енергія"] -= 2
        points += 1
        logger.info(f'Енергія: {heroes[hero]["енергія"]}, ігри: {games}, бали: {points}, паліндром - так')
        return f'Це паліндром!\n' \
               f'Ваша енергія зменшилась на 2\n' \
               f'Ви отримали 2 бали!'
    if 3 > len(word) or 10 < len(word):
        heroes[hero]["енергія"] -= 2
        logger.info(f'Енергія: {heroes[hero]["енергія"]}, ігри: {games}, бали: {points}, паліндром - так')
        return f'Некоректне слово!\n' \
               f'Ваша енергія зменшилась на 2'
    heroes[hero]["енергія"] -= 2
    logger.info(f'Енергія: {heroes[hero]["енергія"]}, ігри: {games}, бали: {points}, паліндром - ні')
    return f'На жаль це не паліндром :(\n' \
           f'Ваша енергія зменшилась на 2'


if __name__ == '__main__':
    start()
