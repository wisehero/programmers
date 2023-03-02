# 우선 이모티콘 플러스 가입자를 늘린다.
# 그 다음 이모티콘 판매액을 늘린다.
from itertools import combinations_with_replacement, permutations, product


def solution(users, emoticons):
    answer = []
    result = []
    discount = [0.4, 0.3, 0.2, 0.1]
    discount_comb = list(product(discount, repeat=len(emoticons)))
    for comb in discount_comb:
        plus_user = 0
        emoticon_paid = 0
        dis_target = emoticons.copy()
        for i in range(len(dis_target)):
            dis_target[i] *= 1 - comb[i]
        for user in users:
            paid_price = 0
            percent = user[0] / 100
            for i in range(len(dis_target)):
                if comb[i] >= percent:
                    paid_price += dis_target[i]

            if paid_price >= user[1]:
                plus_user += 1
            else:
                emoticon_paid += paid_price
        result.append((plus_user, int(emoticon_paid)))
    result = sorted(result, key=lambda x: (-x[0], -x[1]))
    print(result)
    return list(result[0])


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
