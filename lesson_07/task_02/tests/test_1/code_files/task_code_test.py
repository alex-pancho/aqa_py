import sys
from task_code import solution

try:
    grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
    grades_2 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}
    input_values = (grades_1, grades_2)
    result = solution(grades_1, grades_2)
    expected = {'Анна Коваленко': 2, 'Олег Петров': 0, 'Ірина Сидорова': -2}
    assert result == expected
    print(f'With the available value: {input_values} \
          the expected value is: {expected}. \
          The test is passed!')
except AssertionError:
    sys.exit(f'With the available value: {input_values} \
          the expected value is: {expected}. \
          The test is FAILED! \
          The function executed with value: {result}')
