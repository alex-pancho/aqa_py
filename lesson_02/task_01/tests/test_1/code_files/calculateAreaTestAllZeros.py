# all zeros
from calculate_area import calculate_area
import sys

test = calculate_area(0, 0)

try:
    assert test == 0
    print(f"All sides of a rectangular parallelepiped are equal - 0 cm. The test is passed! The function executed with value: {str(test)}")
except AssertionError as v:
    sys.exit(f"All sides of a rectangular parallelepiped are equal - 0 cm. The area of ​​such a rectangular parallelepiped must be equal to 0 cm². The function executed with value: {str(test)}")
