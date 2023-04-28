def solution(cards):
    answer = 0
    visit = [0 for _ in range(len(cards))]
    saveCount = []

    for index, nowCard in enumerate(cards):

        if visit[index] == 0:  # 아직 안열어본 상자라면
            groupCount = 1  # 상자 1개 카운트
            visit[index] = 1  # 현재 상자 방문 처리
            nextIndex = nowCard - 1  # 다음에 열어볼 상자 인덱스

            while True:
                if visit[nextIndex] == 0:  # 다음 상자가 안열어본 상자라면
                    groupCount += 1
                    visit[nextIndex] = 1
                    nextIndex = cards[nextIndex] - 1  # 새로 열어볼 다음 상자
                else:
                    break

            saveCount.append(groupCount)

    if len(saveCount) > 1:  # 그룹이 2개 이상이라면
        answer = saveCount[0] * saveCount[1]
    else:
        answer = 0

    return answer
