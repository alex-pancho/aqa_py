import sys
from task_code import change_params

try:
    input_value = ("800x600", "1024x800")
    result = change_params(*input_value)
    expected = """\
    screen_size = 1024x800
    paralel_processes = 10
    db_conection = localhost:5432"""
    assert result == expected
    print(f'With the available value: {input_value} \
          the expected value is: {expected}. \
          The test is passed!')
except AssertionError:
    sys.exit(f'With the available value: {input_value} \
          the expected value is: {expected}. \
          The test is FAILED! \
          The function executed with value: {result}')
