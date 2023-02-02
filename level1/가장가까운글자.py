def solution(s):
    answer = []
    dic = dict()

    for i, c in enumerate(s):
        if c not in list(dic.keys()):
            dic[c] = i
            answer.append(-1)
        else:
            answer.append(i - dic[c])
            dic[c] = i

    print(dic)
    return answer


s = "banana"
print(solution(s))
