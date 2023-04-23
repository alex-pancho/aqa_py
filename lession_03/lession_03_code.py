# Зріз строки
alice_in_wonderland = """ "Would you tell me, please, which way I ought to go from here?"
                       "That depends a good deal on where you want to get to," said the Cat.
                       "I don't much care where ——" said Alice.
                       "Then it doesn't matter which way you go," said the Cat.
                       "—— so long as I get somewhere," Alice added as an explanation.
                       "Oh, you're sure to do that," said the Cat, "if you only walk long enough." """


# ітерація строки

# Розділення на частини – split()
line_for_split = '  asdf fjdk; afed, fjek, asdf,      foo;bar , spam;eggs  '

# Обрізання зайвих символів строки: strip(), lstrip() та rstrip()


# Перевірка початку .startswith та закінчення .endswith
# filename.startswith(('http:', 'https:', 'ftp:'))
filename = 'spam.txt'


# Регістр символів строки - маленький, великий і перетворення
# .isupper() та .upper() також .islower() та .lower()
# str.capitalize() and str.title()

# Пошук у строці: .find() та in

# Заміна у строці: .replace()

# Комбінування строкових змінних ','.join(str)

# отримання довжини строки len()

# Перетворення строкових даних в інший тип даних
# s.isalpha() та s.isdecimal()

# String Formatting
'First: {} second: {}'.format(1, 'two')
'Second: {1}, first: {0}'.format(42, 'two')

"String: {0!s} Repr: {0!r} ASCII: {0!a}".format("banana 😀")

s = 'a string'
f'{s:>12s}'
f'{s:<12s}'
f'{s:^12s}'

x = -0.123
f'{x:.1f}'

for num in range(0,17):
    for base in 'dxob':
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
"\ooo"	# Octal value
"\xhh"	# Hex value

long_long_line = """\
Long long string\
"""