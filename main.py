from collections import Counter


def solution(kor, usa, incs):
    answer = 0
    same_incs = {}

    for i in kor:
        for j in usa:
            same_incs[i + " " + j] = 0

    for key in same_incs.keys():
        k, u = key.split(" ")
        for inc in incs:
            inc = inc.split(" ")
            if k in inc and u in inc:
                same_incs[key] += 1

    counter = Counter(same_incs).most_common()[0][1]
    print(counter)
    return counter


solution(
    ["AAA", "BCD", "AAAAA", "ZY"],
    ["AB", "AA", "TTTT"],
    ["AB BCD AA AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"]
)

solution(
["CCC", "BCDF"], ["XXXX"], ["BCDF CCC", "XXXX"])
