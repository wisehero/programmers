s = input()
answer = ''
for i in range(len(s)):
    answer += s[i]
    if len(answer) == 10:
        print(answer)
        answer = ''
    elif len(answer) < 10 and i == len(s) -1:
        print(answer)
