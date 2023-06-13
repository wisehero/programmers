def solution(A, B):
    answer = 0
    if A == B:
        return 0
    A = list(A)
    for i in range(len(A)):
        last = A.pop()
        A.insert(0, last)
        answer += 1
        if "".join(A) == B:
            return answer

        if i == len(A) - 1:
            return -1

    return answer