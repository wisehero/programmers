def solution(s):
    count_x = 0
    count_not_x = 0
    answer = 0
    x = ''
    for i in range(len(s)):
        if x == '':
            if i == len(s) -1 :
                answer += 1
                break
            x = s[i]
            count_x += 1
            continue
        if s[i] == x:
            count_x += 1
        else:
            count_not_x += 1

        if count_x == count_not_x:
            x = ''
            count_x = 0
            count_not_x = 0
            answer += 1

    return answer


print(solution("aaabbaccccabbb"