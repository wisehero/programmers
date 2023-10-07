def solution(s):
    answer = ''
    s_li = s.lower().split(" ")
    for s in s_li:
        for k, v in enumerate(s):
            if k % 2 == 0:
                v = v.upper()
            answer += v
        answer += " "
    return answer[:-1]