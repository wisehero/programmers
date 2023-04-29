from heapq import heappop, heappush

def solution(book_time):
    answer = 1

    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()

    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap, e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    return answer

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])


"""
[[850, 1160], [860, 920], [900, 1020], [1000, 1100], [1100, 1280]]
[(850, 1160), (860, 920), (900, 1020), (1000, 1100), (1100, 1280)]"""