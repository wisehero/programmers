# 회의는 한번 시작하면 중간에 중단될 수 없다.
# 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x: (x[1], x[0]))

answer = 0
start, end = 0, 0
for a in arr:
    if end <= a[0]:
        start, end = a[0], a[1]
        answer += 1

print(answer)
