def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}

    cnt = 0
    best = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            best += 1

    best_cnt = cnt + best

    if best_cnt in rank:
        answer.append(rank[best_cnt])
    else:
        answer.append(6)

    if cnt in rank:
        answer.append(rank[cnt])
    else:
        answer.append(6)
    return answer
