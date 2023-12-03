# all zeros
from calculate_area import calculate_area
import sys

test = calculate_area(2, 2)

try:
    assert test == 4
    print(f"This is a flat figure. The test is passed! The function executed with value: {str(test)}")
except AssertionError as v:
    sys.exit(f"This is a flat figure. The area of such a rectangular parallelepiped must be equal to 2 cm². The function executed with value: {str(test)}")
