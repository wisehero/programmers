def solution(friends, gifts):
    m = len(friends)
    answer = [0] * m
    arr = [[0] * m for _ in range(m)]
    d = {}
    present = {}
    for i in range(m):
        present[i] = [0, 0]
    for friend in friends:
        d[friend] = friends.index(friend)

    for gift in gifts:
        give, receivce = gift.split(" ")
        i = d[give]
        j = d[receivce]
        if i != j:
            arr[i][j] += 1
        present[i][0] += 1
        present[j][1] += 1

    for i in range(m):
        for j in range(m):
            if arr[i][j] > arr[j][i]:
                answer[i] += 1

    print(answer)
    for i in range(m):
        for j in range(i, m):
            if arr[i][j] == arr[j][i]:
                if present[i][0] - present[i][1] < present[j][0] - present[j][1]:
                    answer[j] += 1
                elif present[i][0] - present[i][1] > present[j][0] - present[j][1]:
                    answer[i] += 1

    return answer


print(solution(

    ["joy", "brad", "alessandro", "conan", "david"],
    ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
