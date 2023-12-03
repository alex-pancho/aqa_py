import sys
from task_code import solution

try:
    input_value = 1
    result = solution(input_value)
    expected = 1
    assert result == expected
    print(f'With the available value: {input_value} \
          the expected value is: {expected}. \
          The test is passed!')
except AssertionError:
    sys.exit(f'With the available value: {input_value} \
          the expected value is: {expected}. \
          The test is FAILED! \
          The function executed with value: {result}')
