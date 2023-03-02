def solution(number, limit, power):
    answer = 0
    weapons = []
    for i in range(1, number + 1):
        count = 0
        if i == 1:
            weapons.append(1)
            continue
        else:
            for j in range(1, int(i ** (1 / 2)) + 1):
                if i % j == 0:
                    if j == i // j:
                        count += 1
                    else:
                        count += 2

        if count > limit:
            weapons.append(power)
        else:
            weapons.append(count)
    answer = sum(weapons)
    return answer

solution(10, 3, 2)