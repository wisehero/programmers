"""

한 조는 최소 5명, 최대 7명이고 조의 개수는 최소화해야 한다.


"""
import random

members = [
    "서태주", "풍영연",
    "이진웅", "한우원", "강형철", "이은자", "서희주",
    "권재성", "표범수", "유병철", "유선주", "탁수원",
    "배성민", "유다혜", "강남일", "유미영", "설태하", "풍은석", "오지석", "김철진",
    "주서태", "홍영연",
    "성진웅", "우원재", "우형철", "김은자", "박희룡",
    "권나라", "김범수", "이병철", "배선주", "탁재훈",
    "한성민", "김다혜", "김남일", "김미영", "설경구"
]


def mix_members(members):
    dp = [0] * 101
    n = 2
    for i in range(10, 101):
        if i % 7 == 1:
            n += 1
        dp[i] = n

    group_count = dp[len(members)]
    answer = dict()
    for number in range(1, group_count + 1):
        answer.setdefault(f"{number}조", [])

    group_list = list(answer.keys())
    for group in group_list:
        while len(answer[group]) < 5:
            member = random.choice(members)
            members.remove(member)
            answer[group].append(member)

    while len(members) != 0:
        member = random.choice(members)
        members.remove(member)
        group = random.choice(group_list)
        if len(answer[group]) == 7:
            continue
        else:
            answer[group].append(member)
    return answer


print(mix_members(members))
