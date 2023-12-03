def solution(*args, sep="."):
    return sep.join(str(d) for d  in args)


if __name__ == "__main__":
    print(solution(11, 22, 2003))
    print(solution(11, 22, 2003, sep="/"))