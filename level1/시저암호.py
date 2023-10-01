def solution(s, n):
    answer = ''
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lo = "abcdefghijklmnopqrstuvwxyz"

    length = len(up)

    for a in s:
        if a == " ":
            answer += a
        else:
            if a in lo:
                answer += lo[(lo.index(a) + n) % length]
            else:
                answer += up[(up.index(a) + n) % length]
    return answer
