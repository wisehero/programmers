'''
1. 인쇄 대기목록의 가장 앞에 있는 문서를 대기목록에서 꺼낸다.
2. 나머지 인쇄 대기 목록에서 J보다 중요도가 높은 문서가 한개라도 존재하면
J를 대기목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄한다.
'''


from collections import deque


def solution(priorities, location):
    answer = 0

    pi = []
    count = 1
    for i, p in enumerate(priorities):
        pi.append([p, i])

    pi = deque(pi)
    while pi:
        p, i = pi.popleft()

        if p == max(priorities):
            if i == location:
                return count
            else:
                count += 1
            priorities.remove(max(priorities))
        else:
            pi.append([p, i])

    return answer