def solution(x):
    answer = True
    x = str(x)
    c = 0
    for i in x:
        c += int(i)
    if int(x) % c != 0:
        answer = False
    return answer

print(solution(10))