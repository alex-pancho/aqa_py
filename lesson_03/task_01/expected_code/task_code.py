def solution(test_string: str):

    return test_string.split('TestCase: ')[-1]


if __name__ == "__main__":
    print(solution("2023-04-27 15:30:45 - TestCase: login_successful"))
    print(solution("2023-04-27 15:30:45 - test PASS"))