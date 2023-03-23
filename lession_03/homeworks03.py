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
print("Task 1 - >>>>>>", adwentures_of_tom_sawer.replace("\n", " "))

# task 02 ==
""" Замініть .... на пробіл
"""
ignore_points_adwentures = adwentures_of_tom_sawer.replace("....", " ")
print("Task 2 - >>>>>>", ignore_points_adwentures)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
ignore_points_adwentures.split()
new_text = ' '.join(ignore_points_adwentures.split())
print("Task 3->>> \n{}".format(new_text))

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
char_count = new_text.count("h")
print("Task 4->>> \n{}".format(char_count))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
counter = 0
for letter in new_text:
    if letter.isupper():
        counter += 1
print("Task 5->>> \n{}".format(counter))

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word = "Tom"
first_occurrence = new_text.find(word)
second_occurence = new_text.find(word, first_occurrence+1)
print("Task 6->>>", second_occurence)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('\n')
print("Task 7->>> \n{}".format (adwentures_of_tom_sawer_sentences))


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8 v1->>>", adwentures_of_tom_sawer_sentences[3].lower())
print("Task 8 v2->>>", adwentures_of_tom_sawer_sentences[3].casefold())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
phrase = "By the time"
count_numb = 0
count_numb_sentanse = []
for i in adwentures_of_tom_sawer_sentences:
    count_numb +=1
    if i.startswith(phrase):
        count_numb_sentanse.append(count_numb)
        print("The expected-phrase is located in sentanse", count_numb_sentanse)
        continue
    else:
        print("There is no expected phrase in sentanse",  count_numb)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_list = last_sentence.split()
print("The last sentence has {}".format(len(words_list)), "words")
