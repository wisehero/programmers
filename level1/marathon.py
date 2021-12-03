'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴
배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
'''


def solution(participant, completion):
    participant.sort()
    completion.sort()
    d = dict()
    d['participant'] = participant
    d['completion'] = completion
    for v in d['participant']:
        if v in d['completion']:
            d['completion'].remove(v)
        else:
            return v


from collections import Counter


def solution(participant, completion):
    cnt = Counter()
    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1
    return list(x for x, y in cnt.items() if y == 1).pop();


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
