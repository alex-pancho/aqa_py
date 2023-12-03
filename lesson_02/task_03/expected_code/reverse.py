def solution(x):
    return x % 10 * 100 + x % 100 // 10 * 10 + x // 100
