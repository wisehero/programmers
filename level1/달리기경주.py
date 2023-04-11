def solution(players, callings):
    answer = []

    d1 = {}
    rank = 1
    for player in players:
        d1[rank] = player
        rank += 1

    d2 = {}
    rank = 1
    for player in players:
        d2[player] = rank
        rank += 1

    for calling in callings:
        prev_rank = d2[calling] - 1  # 2등을 가져와
        prev = d1[prev_rank]  # prev = d1[2] = soe
        d2[prev] += 1  # d2["soe"] = 2 + 1
        d2[calling] -= 1  # d2["kai"] = 3 -> -1해서 2
        d1[d2[calling]] = calling  # d1[2] = kai
        d1[d2[prev]] = prev

    return list(d1.values())


solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
