def solution(s):
    answer = 0

    is_x = 0
    is_not_x = 0
    i = 0
    x = s[i]
    while True:
        if i == len(s) - 1:
            answer += 1
            break
        if s[i] == x:
            is_x += 1
        else:
            is_not_x += 1

        i += 1

        if is_x == is_not_x:
            answer += 1
            x = s[i]
            is_x = 0
            is_not_x = 0

    return answer
