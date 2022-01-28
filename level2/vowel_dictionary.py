from itertools import product

vowel = []

for i in list(product("AEIOU", repeat=1)):
    vowel.append("".join(i))

for i in list(product("AEIOU", repeat=2)):
    vowel.append("".join(i))

for i in list(product("AEIOU", repeat=3)):
    vowel.append("".join(i))

for i in list(product("AEIOU", repeat=4)):
    vowel.append("".join(i))

for i in list(product("AEIOU", repeat=5)):
    vowel.append("".join(i))

vowel.sort()


def solution(word):
    answer = vowel.index(word) + 1
    return answer


