from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine).most_common()
    for i in counter:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    return answer


# 1: 1, 2: 2, 3:2 , 4:1, 5: 2

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
