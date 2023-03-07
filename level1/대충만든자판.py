def solution(keymap, targets):
    answer = []
    for target in targets:
        total = 0
        n = len(target)
        for i in range(n):
            count = -1
            for j in range(len(keymap)):
                if target[i] in keymap[j]:
                    if count == -1:
                        count = keymap[j].index(target[i]) + 1
                    else:
                        count = min(count, keymap[j].index(target[i]) + 1)
                if j == len(keymap) - 1 and count == -1:
                    total = -1
            if count == -1:
                break
            total += count
        if total < 0:
            answer.append(-1)
        else:
            answer.append(total)

    return answer


print(solution(["ABACD", "BCEFD"], ["XABCD", "AABB"]))
