# 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다.
# 문자열은 정렬되어있어야한다.
from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split())

v = {"a", "i", "e", "o", "u"}
not_v = set("bcdfghjklmnpqrstvwxyz")

answer = []

cases = list(combinations(arr, l))
for case in cases:
    if len(set(case).intersection(v)) >= 1 and len(set(case).intersection(not_v)) >= 2:
        case = sorted(case)
        password = "".join(case)
        answer.append(password)

answer.sort()
for i in answer:
    print(i)
