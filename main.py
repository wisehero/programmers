def solution(hp):
    answer = 0
    new_hp = hp
    while True:

        if 0 < new_hp < 3:
            answer += new_hp
            break

        if new_hp // 5 != 0:
            ants, new_hp = divmod(new_hp, 5)
            answer += ants
        else:
            ants, new_hp = divmod(new_hp, 3)
            answer += ants

        if new_hp == 0:
            break

    return answer


solution(24)
