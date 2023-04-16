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
print(adwentures_of_tom_sawer.replace("\n", " "))
# task 02 ==
""" Замініть .... на пробіл
"""
print(adwentures_of_tom_sawer.replace("....", " "))

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print(adwentures_of_tom_sawer.replace("....", " ").replace("\n", " ").replace("   ", " "))

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adwentures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_upper = 0
for char in adwentures_of_tom_sawer:
    if char.isupper():
        count_upper +=1
print(count_upper)       

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
start = adwentures_of_tom_sawer.find("Tom")
print(adwentures_of_tom_sawer.find("Tom",start+1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_text = adwentures_of_tom_sawer.replace("....", " ").replace("\n", " ").replace("   ", " ")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_text.split(".")
forth_sentence = adwentures_of_tom_sawer_sentences[3]
print(forth_sentence.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(adwentures_of_tom_sawer.find("By the time"))

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_text = adwentures_of_tom_sawer.replace("....", " ").replace("\n", " ").replace("   ", " ")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_text.split(". ")
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_words = last_sentence.split(" ")
print(len(last_sentence_words))

