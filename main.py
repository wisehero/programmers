n = int(input())

result = []
for _ in range(n):
    result.append(int(input()))

for i in sorted(result, reverse=True):
    print(i)