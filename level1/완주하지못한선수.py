from collections import Counter


def solution(participant, completion):
    answer = ''

    pc = Counter(participant)

    for c in completion:
        pc[c] -= 1

    for k in pc.keys():
        if pc[k] > 0:
            return k
