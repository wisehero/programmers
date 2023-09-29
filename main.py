def solution(k, score):
    answer = []
    rank = []

    for i in range(len(score)):
        rank.append(score[i])
        rank.sort()

        if len(rank) < k:
            answer.append(min(rank))
        else:
            answer.append(min(rank[-k:]))

    return answer