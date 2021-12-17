def solution(L, x):
    if len(L) == 0:
        return -1
    answer = 0
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2

        if x not in L:
            return -1
        if x == L[middle]:
            answer = middle
            return answer
        # x가 중간보다 낮을 때
        elif x < L[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return answer
