def solution(A, B):
    i = 0
    sum = 0
    A.sort()
    B.sort(reverse=True)
    while len(A) != i:
        sum += A[i] * B[i]
        i += 1
    return sum
