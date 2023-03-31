from collections import deque


def solution(A, B):
    if A == B:
        return 0
    answer = 0
    deque_A = deque(A)
    for _ in range(len(A)):
        deque_A.appendleft(deque_A.pop())
        answer += 1
        if "".join(deque_A) == B:
            return answer
        if A == "".join(deque_A):
            return -1
    return answer


print(solution("hello", "ohell"))
