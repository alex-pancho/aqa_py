# x = 0
import sys
from minmax import solution

try:
    point = 1
    result = solution(point)
    expected = (1, 2)
    assert result == expected
    print(f'For point "{point}" expected value is {expected}. \
          The test is passed! The function executed with value: {result}')
except AssertionError:
    sys.exit(f'For point "{point}" expected value is {expected}. \
          The test is FAILED. The function executed with value: {result}')
