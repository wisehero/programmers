import sys

t = int(sys.stdin.readline())
d = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 0, 1],
    2: [0, 1, 1, 1, 1, 1, 0],
    3: [0, 1, 1, 1, 0, 1, 1],
    4: [1, 0, 1, 1, 0, 0, 1],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 1],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
    10: [0, 0, 0, 0, 0, 0, 0]
}

result = 0

for _ in range(t):
    first, second = sys.stdin.readline().rstrip().split(" ")
    first = list(first)
    second = list(second)
    if len(first) > len(second):
        second = ["10"] * (len(first) - len(second)) + second
    elif len(second) > len(first):
        first = ["10"] * (len(second) - len(first)) + first

    for fv, sv in list(zip(first, second)):
        diff = 0
        for i in range(len(d[int(fv)])):
            if d[int(fv)][i] != d[int(sv)][i]:
                diff += 1
        print(diff)
        result += diff
    print(result)
    result = 0


