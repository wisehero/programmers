import sys

n, k = map(int, sys.stdin.readline().split(" "))
scores = list(map(int, sys.stdin.readline().split(" ")))

for _ in range(k):
    start, end = map(int, sys.stdin.readline().split(" "))
    print(
        format(round(sum(scores[start - 1:end]) / ((end - start) + 1), 2), '.2f')
    )
