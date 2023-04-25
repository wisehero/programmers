import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [(-1) * work for work in works]
    heapq.heapify(works)  # 힙으로 만든다. 여기서는 최소 힙이다.

    while n:
        curr_work = heapq.heappop(works)
        post_work = curr_work + 1
        heapq.heappush(works, post_work)
        n -= 1

    return sum([work ** 2 for work in works])


solution(4, [4, 3, 3])
