def solution(dartResult):
    answer = 0
    score = []
    for index in range(len(dartResult)):
        if dartResult[index].isdigit():
            if dartResult[index] == "1" and dartResult[index + 1] == "0":
                score.append(int("10"))
                continue
            elif dartResult[index] == "0" and dartResult[index - 1] == "1":
                continue
            score.append(int(dartResult[index]))
        elif dartResult[index] in ["S", "D", "T"]:
            if dartResult[index] == "S":
                score[-1] = score[-1] ** 1
            elif dartResult[index] == "D":
                score[-1] = score[-1] ** 2
            else:
                score[-1] = score[-1] ** 3
        else:
            if dartResult[index] == "*":
                if score.index(score[-1]) == 0:
                    score[0] *= 2
                else:
                    score[-1] *= 2
                    score[-2] *= 2
            else:
                score[-1] *= -1
    answer = sum(score)
    return answer


print(solution("1D2S#10S"))
