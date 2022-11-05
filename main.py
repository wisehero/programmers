from collections import Counter


def solution(line):
    answer = ''
    pre = line[0]
    answer += pre
    if len(line) == 1:
        return pre
    for index in range(1, len(line)):
        if line[index] == pre:
            if answer[-1] == '*':
                continue
            answer += "*"
        else:
            answer += line[index]
            pre = line[index]

    return answer


line = "aabbbc"
print(solution(line))
