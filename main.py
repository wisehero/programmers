def solution(hp):
    answer = 0

    while hp:
        if hp >= 5:
            answer += hp // 5
            hp %= 5
        elif 3 <= hp < 5:
            answer += hp // 3
            hp %= 3
        else:
            answer += hp
            hp %= 1

    return answer