# Зріз строки
alice_in_wonderland =  'Would you tell me, please, which way I ought to go from here?" \
                       "That depends a good deal on where you want to get to," said the Cat. \
                       "I don\'t much care where ——" said Alice. \
                       "Then it doesn\'t matter which way you go," said the Cat. \
                       "—— so long as I get somewhere," Alice added as an explanation. \
                       "Oh, you\'re sure to do that," said the Cat, "if you only walk long enough'
print(len(alice_in_wonderland))
# ітерація строки
hello = "hello"
for i in hello:
    print(i)
# one item
print("[0]", alice_in_wonderland[0])
print("[-1]", alice_in_wonderland[-1])
# slice
print("[4:28]", alice_in_wonderland[4:28])
print("[-12:-3]", alice_in_wonderland[-12:-3])

print("[:42]", alice_in_wonderland[:42])
#print("[42:]", alice_in_wonderland[42:])

print("[4:28:2]", alice_in_wonderland[4:28:2])
print("[4:28:3]", alice_in_wonderland[4:28:3])

print("[42::-1]", alice_in_wonderland[42::-1])
#print("[::-1]", alice_in_wonderland[::-1])

# Розділення на частини – split()
line_for_split = 'xxx asdf fjdk; afed, fjek, asdf,      foo;bar , spam;eggs  ZZZZ'
value_list = line_for_split.split(",")
print(value_list)
value_list_2 = line_for_split.split(";")
print(value_list_2)
# Обрізання зайвих символів строки: strip(), lstrip() та rstrip()
print(line_for_split, len(line_for_split))
print(line_for_split.strip("Z").strip(), len(line_for_split.strip("Z").strip()))
print(line_for_split.lstrip("Z"))
print(line_for_split.rstrip("Z"))
# Перевірка початку .startswith та закінчення .endswith
# filename.startswith(('http:', 'https:', 'ftp:'))
filename = 'spam.txt'
print(filename.endswith("txt"))
print(line_for_split.endswith("spam;eggs  ZZZZ"))
url = "http://tratata.com"
print(url.startswith("http"))
# Регістр символів строки - маленький, великий і перетворення
# .isupper() та .upper() також .islower() та .lower()
user_name = "unkle sam jordan"
print(user_name.islower())
print(user_name.upper())
# str.capitalize() and str.title()
print(user_name.capitalize(), user_name.title())
print(len(user_name) < 256)
# Пошук у строці: .find() та in
start = alice_in_wonderland.find("Alice")
print(alice_in_wonderland.find("Alice", start+1, 256))
# Заміна у строці: .replace()
sub_alise = "That depends a good deal on where you want to get to, said the Cat"
print(alice_in_wonderland.replace("Cat", "Dog"))
# Комбінування строкових змінних ','.join(str)
sub_alise_tuple  = ("That", "depends","a_good","deal","on","where","you","want","to","get","to_said_the_Cat")
print(','.join(sub_alise_tuple))
# отримання довжини строки len()

# Перетворення строкових даних в інший тип даних
# s.isalpha() та s.isdecimal()
user_age = " 23 "
print(user_age.strip().isdecimal())
int_user_age = int(user_age)
print(int_user_age)
print(bool(""))
print(list("abc"))
# String Formatting
print('First: {} second: {}'.format(1, 'two'))
print('Second: {1}, first: {0}'.format(1, 'two'))

print("String: {0!s} Repr: {0!r} ASCII: {0!a}".format("banana 😀"))

s = 'a string'
print(f'{s:>12s}')
print(f'{s:<12s}')
print(f'{s:^12s}')

x = -0.123
f'{x:.1f}'

for num in range(0,17):
    for base in 'dfxob':
        print('{0:{width}{base}}'.format(num, base=base, width=6), end=' ')
    print()

# special character
"\'"	# Single Quote
"\\"	# Backslash
"\n"	# New Line
"\r"	# Carriage Return
"\t"	# Tab
"\b"	# Backspace
"\f"	# Form Feed

long_long_line = """\
Long long string\
"""
print(long_long_line)