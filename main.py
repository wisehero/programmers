import bisect


def solution(A, B):
    answer = 0

    A.sort()

    before = 0
    for number in B:
        now = bisect.bisect_left(A, number)
        if before != now:
            answer += 1
            before = now

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
