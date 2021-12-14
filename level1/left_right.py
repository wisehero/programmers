def solution(left, right):
    answer = 0
    li = []
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                li.append(j)
        if len(li) % 2 == 0:
            answer += i
        else:
            answer -= i
        print(answer)
        li = []
    return answer
