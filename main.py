def solution(my_str, n):
    answer = []
    index = 1
    start = 0
    while True :
        if n * index >= len(my_str):
            answer.append(my_str[start:])
            break
        answer.append(my_str[start:n * index])
        start = n * index
        index += 1
    return answer