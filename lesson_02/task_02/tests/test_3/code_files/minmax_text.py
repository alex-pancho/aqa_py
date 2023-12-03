# x = 0
import sys
from minmax import solution

try:
    point = 0
    result = solution(point)
    expected = (0, 0)
    assert result == expected
    print(f'For point "{point}" expected value is {expected}. \
          The test is passed! The function executed with value: {result}')
except AssertionError:
    sys.exit(f'For point "{point}" expected value is {expected}. \
          The test is FAILED. The function executed with value: {result}')
