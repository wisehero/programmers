import random


def solution(participant, completion):
    answer = ''
    done = {}

    for key in participant:
        if key not in done:
            done[key] = 0
        else:
            done[key] -= 1

    for c in completion:
        if c in done:
            done[c] += 1

    for p in participant:
        if done[p] <= 0:
            return p
