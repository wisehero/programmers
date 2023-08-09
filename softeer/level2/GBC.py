import sys

n, m = map(int, sys.stdin.readline().split(" "))

limit_info = [0] * 101

now = 1

for _ in range(n):
    section, speed = map(int, sys.stdin.readline().split(" "))
    for i in range(now, now + section):
        limit_info[i] = speed
    now += section

over = 0
now = 1
for _ in range(m):
    section, speed = map(int, sys.stdin.readline().split(" "))
    for i in range(now, now + section):
        over = max(speed - limit_info[i], over)
    now += section
print(over)
