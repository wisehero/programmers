from itertools import product


def solution(word):
    answer = 0
    vowel = list("AEIOU")
    dic = []
    for i in range(1, 6):
        for case in list(product(vowel, repeat=i)):
            dic.append("".join(case))

    dic.sort()

    answer = dic.index(word) + 1
    return answer
