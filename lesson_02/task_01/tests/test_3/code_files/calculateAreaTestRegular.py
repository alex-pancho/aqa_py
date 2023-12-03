# all zeros
from calculate_area import calculate_area
import sys

test = calculate_area(3, 4)

try:
    assert test == 12
    print(f"This is a flat figure. The test is passed! The function executed with value: {str(test)}")
except AssertionError as v:
    sys.exit(f"This is a flat figure. The area of such a rectangular parallelepiped must be equal to 2 cm². The function executed with value: {str(test)}")
