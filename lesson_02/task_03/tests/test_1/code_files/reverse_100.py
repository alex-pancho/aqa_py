# x = 0
import sys
from reverse import solution

try:
    result = solution(100)
    assert result == 1
    print(f'Inverse the number 100. The test is passed! The function executed with value: {str(result)}')
except AssertionError:
    sys.exit("Inverse the number 100. Gotten value is wrong. Test is failed")