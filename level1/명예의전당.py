from collections import deque


def solution(k, score):
    answer = []
    honor = []
    for i in score:
        honor.append(i)
        honor.sort(reverse=True)
        if len(honor) > 3:
            honor.pop()
        answer.append(honor[-1])
    return answer
