def solution(cards):
    answer = 1
    group = []
    visited = [False] * len(cards)

    for i in range(len(cards)):
        card = cards[i]
        if visited[i]:
            continue
        visited[i] = True
        count = 1

        while not visited[card - 1]:
            count += 1
            visited[card - 1] = True
            card = cards[card - 1]

        group.append(count)

    group.sort(reverse=True)
    if len(group) > 1:
        return group[0] * group[1]
    else:
        return 0

    return answer