# 이진 탐색으로 시간 복잡도 극복하기
# in 연산자는 list보다 set에서 시간 복잡도 효율성 올라감

import bisect

n, q = map(int, input().split())
car = list(map(int, input().split()))
car.sort()
set_car = set(car)
for _ in range(q):
    m = int(input())
    if m not in set_car:
        print(0)
    else:
        idx = bisect.bisect_left(car, m)
        print(idx * (n - idx - 1))
