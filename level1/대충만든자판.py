def solution(keymap, targets):
    answer = []

    for target in targets:
        amount = 0
        for i in range(len(target)):
            count = 99999
            for j in range(len(keymap)):
                if target[i] in keymap[j]:
                    count = min(keymap[j].index(target[i]) + 1, count)

            if count != 99999:
                amount += count
            else:
                amount = -1
                break

        answer.append(amount)

    return answer


