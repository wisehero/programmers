# A는 재배열해도 된다. B는 안된다.
import math
import heapq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

heapq.heapify(b)
a.sort(reverse=True)
answer = 0
for i in range(n):
    answer += a[i] * heapq.heappop(b)

print(answer)
