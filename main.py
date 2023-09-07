from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    saram = list(input().split())
    if n > 32:
        print(0)
    else:
        answer = []
        cases = list(combinations(saram, 3))

        for case in cases:
            distance = 0
            for i in range(2):
                for j in range(i + 1, 3):
                    distance += len(set(case[i]).difference(case[j]))
            answer.append(distance)

        print(min(answer))
