a, b = input().split()

if len(a) == len(b):
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
else:
    answer = 99999

    for i in range(len(b) - len(a) + 1):
        temp = 0
        s = b[i:i + len(a)]
        for j in range(len(s)):
            if a[j] != s[j]:
                temp += 1
        answer = min(answer, temp)

print(answer)
