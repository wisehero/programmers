def solution(number, limit, power):
    weapons = [1]
    for i in range(2, number + 1):
        count = 0

        # 약수의 개수를 구함에 있어서 시간복잡도를 줄이는 방법
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1

            if count > limit:
                count = power
                break
        weapons.append(count)

    answer = sum(weapons)
    return answer


solution(10, 3, 2)
