import sys

n = int(input())
timetable = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    timetable.append([s, e])

timetable.sort(key=lambda x: (x[1], x[0]))

end = 0
answer = 0
for s, e in timetable:
    if end <= s:
        answer += 1
        end = e
print(answer)
