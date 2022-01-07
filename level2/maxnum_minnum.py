def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = int(s[i])  # [1, 2, 3, 4]
    max_num = str(max(s))
    min_num = str(min(s))
    answer += min_num + " "
    answer += max_num
    return answer
