def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        picture[i] = list(picture[i])
        pk = ''
        for j in range(len(picture[i])):
            pk += picture[i][j] * k

        for _ in range(k):
            answer.append(pk)
    return answer