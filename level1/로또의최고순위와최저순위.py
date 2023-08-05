def solution(lottos, win_nums):
    answer = []
    if set(lottos) == set(win_nums):
        return [1, 1]
    if lottos.count(0) == 6:
        return [1, 6]

    max_rank = 7
    min_rank = 7
    # 0이 전부 다 맞춘 숫자가 아닐 경우
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_rank -= 1

    # 0이 전부 다 맞춘 숫자일 경우
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            max_rank -= 1

        if lottos[i] == 0:
            max_rank -= 1

    # 0도 없고 전부 다 다른 숫자일 경우
    if max_rank == 7 and min_rank == 7:
        return [6, 6]

    answer = [max_rank, min_rank]
    return answer
