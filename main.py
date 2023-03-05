def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(x - n), n - x))
    return answer


solution([1, 2, 3, 4, 5, 6], 4)
