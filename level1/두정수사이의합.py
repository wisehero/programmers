def solution(a, b):
    arr = []
    if a > b:
        arr = list(range(b, a+1))
    else:
        arr = list(range(a, b+1))
    return sum(arr)