import heapq

scoville = [1, 2, 3, 9, 10, 12]


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
        if scoville[0] >= K:
            break
        elif len(scoville) == 1:
            answer = -1
            break

    print(answer)
    return answer


solution(scoville, 7)
