from itertools import permutations

dungeons = [[80, 20], [50, 40], [30, 10]]

a = list(permutations(dungeons, 3))
print(a)


def solution(k, dungeons):
    answer = 0
    fatigue = k
    case = list(permutations(dungeons, len(dungeons)))
    for c in case:
        result = 0
        for cc in c:
            if fatigue >= cc[0]:
                fatigue -= cc[1]
                result += 1
            else:
                continue
        if result > answer:
            answer = result
        fatigue = k
    return answer


print(solution(80, dungeons))
