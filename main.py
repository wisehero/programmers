n = input()
m = input()

result = 0
i = 0

while i < len(n):
    if n[i:i + len(m)] == m:
        i += len(m)
        result += 1
    else:
        i += 1

print(result)
