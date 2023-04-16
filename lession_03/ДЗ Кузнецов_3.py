adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer_1 = (adwentures_of_tom_sawer.replace("\n", " ").replace("....", " ").replace("  ", ""))
print("# Task 01 - 03", adwentures_of_tom_sawer_1)

# task 02 ==
""" Замініть .... на пробіл
"""
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("# task 04", adwentures_of_tom_sawer_1.count("h"))
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

task_05 = (adwentures_of_tom_sawer.replace("\n", " ").replace("....", " ").replace("  ", "").split(" "))
count = 0
for item in task_05:
    if item[0].isupper():
        count += 1
print("# Task 05", count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

start = adwentures_of_tom_sawer_1.find("Tom")
print("# task 06", adwentures_of_tom_sawer_1.find("Tom", start + 1), "символ")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_1.split(".")
print("# task 07", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
for item in adwentures_of_tom_sawer_sentences:
    if item.strip(" ").startswith("By the time"):
        print("# task 08", item.lower())

# task 09
""" Перевірте чи починається якесь речення з "And while the".
"""
for item in adwentures_of_tom_sawer_sentences:
    if item.strip(" ").startswith("And while the"):
        print("# task 09", item)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
cnt_of_word = len(adwentures_of_tom_sawer_sentences[4].split())
print("# task 10", cnt_of_word)
