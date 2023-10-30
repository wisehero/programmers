import heapq


def solution(ability, number):
    heapq.heapify(ability)
    while number != 0:
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a + b)
        heapq.heappush(ability, a + b)
        number -= 1
    return sum(ability)
