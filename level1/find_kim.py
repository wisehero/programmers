def solution(seoul):
    answer = ''

    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            kim = i
    answer = "김서방은 " + str(kim) +"에 있다"
    return answer