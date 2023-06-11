from itertools import permutations


def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    word = []

    for i in range(1, len(babbling)):
        for j in permutations(can_speak, i):
            word.append("".join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer


solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
