def solution(s):
    answer = 0
    # 부호가 있는 경우
    if '+' in s:
        answer = int(s[1:])
    if '-' in s:
        answer = int(s[1:]) * -1
    # 부호가 없는 경우
    else:
        answer = int(s)
    return answer
