def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].lower()
    for i in range(len(s)):
        s[i] = s[i][0].upper() + s[i][1:]
    answer += " ".join(s)
    return answer


print(solution("for me"))