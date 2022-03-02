from collections import deque

s = "cdcd"


def solution(s):
    answer = 0
    q = deque()
    i = 0
    count = 0
    while count != len(s):
        q.append(s[count])
        if len(q) > 1:
            if q[i] == q[i + 1]:
                q.pop()
                q.pop()
                if i == 0:
                    count += 1
                    continue
                i -= 1
            else:
                i += 1
        count += 1

    if len(q) == 0:
        answer = 1
        return answer
    else:
        return answer


print(solution(s))
