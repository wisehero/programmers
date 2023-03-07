from collections import deque


def solution(queue1, queue2):
    answer = 0
    total1 = sum(queue1)
    total2 = sum(queue2)
    total_sum = total2 + total1
    limit = len(queue1) * 4
    q1 = deque(queue1)
    q2 = deque(queue2)

    if total_sum % 2 != 0:
        return -1

    while True:
        if total1 > total2:
            target = q1.popleft()
            q2.append(target)
            total1 -= target
            total2 += target
            answer += 1
        elif total1 < total2:
            target = q2.popleft()
            q1.append(target)
            total1 += target
            total2 -= target
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break

    return answer
