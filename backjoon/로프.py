n = int(input())
lines = []
answer = []
for _ in range(n):
    lines.append(int(input()))

lines.sort()
for line in lines:
    answer.append(line * n)
    n -= 1

print(max(answer))
