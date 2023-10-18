from itertools import product


def solution(users, emoticons):
    answer = []
    discount = [0.4, 0.3, 0.2, 0.1]
    discount_prod = list(product(discount, repeat=len(emoticons)))

    # 가능한 할인율 조합
    for prod in discount_prod:
        plus_user = 0 # 플러스 유저 수
        emoticon_paid = 0 # 이모티콘 구입액
        discount_emo = emoticons.copy()
        print(discount_emo)
        for i in range(len(discount_emo)):
            discount_emo[i] *= 1 - prod[i]

        for user in users:
            paid_price = 0
            percent = user[0] / 100
            for i in range(len(discount_emo)):
                if prod[i] >= percent:
                    paid_price += discount_emo[i]
            if paid_price >= user[1]:
                plus_user += 1
            else:
                emoticon_paid += paid_price
        answer.append((plus_user, int(emoticon_paid)))

    result = sorted(answer, key=lambda x: (-x[0], -x[1]))
    return list(result[0])


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
