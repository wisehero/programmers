from collections import deque


def solution(S):
    answer = 0
    # 같을 경우 
    if len(set(S)) == 1:
        return len(S)

    q = deque(S)
    for i in range(len(S) - 1):
        if q[0] == q[-1]:
            answer += 1
        a = q.popleft()
        q.append(a)

    return answer


print(solution("abbaa"))