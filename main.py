from collections import Counter


def solution(before, after):
    answer = 0
    before_counter = Counter(before)
    after_counter = Counter(after)
    if after_counter == before_counter:
        answer = 1
    return answer
