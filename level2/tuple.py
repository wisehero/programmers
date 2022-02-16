from collections import deque


def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key=len)
    print(s)

    for i in s:
        i = i.split(",")
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
