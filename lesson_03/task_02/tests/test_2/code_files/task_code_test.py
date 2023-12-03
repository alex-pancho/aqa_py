import sys
from task_code import check_file_format

try:
    input_list = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
    ext = ".log"
    result = check_file_format(input_list, ext)
    expected_list = ["c.log", "e.log"]
    assert result == expected_list
    print(f'With the available value: {input_list} \
          and extention {ext} \
          the expected value is: {expected_list}. \
          The test is passed!')
except AssertionError:
    sys.exit(f'With the available value: {input_list} \
          and extention {ext} \
          the expected value is: {expected_list}. \
          The test is FAILED! \
          The function executed with value: {result}')
