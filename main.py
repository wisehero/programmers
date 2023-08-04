def solution(spell, dic):
    answer = 0

    for word in dic:
        b = set(list(word))
        if set(spell) == b:
            answer += 1

    if answer == 0:
        return 2
    else:
        return 1

    return answer
