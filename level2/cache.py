from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque()

    if cacheSize == 0:
        return 5 * len(cities)
    else:
        for i in cities:
            i = i.lower()
            if i in q:
                answer += 1
            else:
                answer += 5
            if i in q:
                q.remove(i)
            else:
                if len(q) >= cacheSize:
                    q.popleft()
            q.append(i)

    return answer


print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
