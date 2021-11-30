alist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"
    , "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def solution(s, n):
    answer = ''

    for i in range(len(s)):

        if s[i].isupper():
            if s[i] == 'Z':
                answer += alist[alist.index('a') + n - 1].upper()
                continue
            if alist.index(s[i].lower()) + n > 25:
                answer += alist[alist.index(s[i].lower()) + n - len(alist)]
            else:
                answer += alist[alist.index(s[i].lower()) + n].upper()

        elif s[i].isspace():
            answer += ' '
        elif s[i] == 'z':
            answer += alist[alist.index('a') + n - 1]
        elif alist.index(s[i]) + n > 25:
            answer += alist[alist.index(s[i]) + n - len(alist)]
        else:
            answer += alist[alist.index(s[i]) + n]
    return answer


print(solution("AaZz", 25))
