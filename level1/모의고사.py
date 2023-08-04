def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_point = 0
    two_point = 0
    three_point = 0

    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            one_point += 1
        if answers[i] == two[i % 8]:
            two_point += 1
        if answers[i] == three[i % 10]:
            three_point += 1

    rank = [(1, one_point), (2, two_point), (3, three_point)]
    rank.sort(key=lambda x: (-x[1], x[0]))
    print(rank)

    m = max(one_point, two_point, three_point)

    for r in rank:
        if r[1] == m:
            answer.append(r[0])
    return answer
