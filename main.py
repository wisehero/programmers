from itertools import permutations


def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    answer = 0

    for i in range(1, 30):

        for j in list(permutations(can_speak, i)):
            print(j)
            if "".join(j) in babbling:
                answer += 1

    return answer


solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])