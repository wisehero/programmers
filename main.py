def solution(keymap, targets):
    answer = []

    for target in targets:
        t = True
        amount = 0
        for i in range(len(target)):
            count = 999
            for j in range(len(keymap)):
                if target[i] in keymap[j]:
                    count = min(keymap[j].index(target[i]) + 1, count)
                    t = True
                else:
                    t = False
            amount += count

        if t:
            answer.append(amount)
        else:
            answer.append(-1)

    return answer


solution(["AGZ", "BSSS"], ["ASA","BGZ"])
