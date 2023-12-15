from collections import deque


def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    for city in cities:
        city = city.lower()

        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5

        if len(cache) >= cacheSize:
            cache.popleft()

        cache.append(city)

    return answer


print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
