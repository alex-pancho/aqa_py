def solution(x):
    y1 = x * x
    y2 = x * 2
    y3 = (x / 2) + x
    return min(y1, y2, y3), max(y1, y2, y3)
